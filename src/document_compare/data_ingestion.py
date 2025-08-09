
import sys
import uuid
from pathlib import Path
import fitz
from datetime import datetime, timezone
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException



class DocumentIngestion:
    """
    Handles saving, reading, and combining of PDFs for comparison with session-based versioning.
    """
    def __init__(self,base_dir:str="data/document_compare"):
        self.log = CustomLogger().get_logger(__name__)
        self.base_dir = Path(base_dir)
        self_base_dir.mkdir(parents=True, exist_ok=True)

    def delete_existing_files(self):
        """
        Delete any existing PDF files at specifided path
        """
        try:
            if self.base_dir.exists() and self.base_dir.is_dir():
                for file in self.base_dir.iterdir():
                  if file.is_file():
                    file.unlink()
                    self.log.info(f"Deleted file: {file}",Path=str(file))
        except Exception as e:
            self.log.error(f"Error deleting existing files: {e}")
            raise DocumentPortalException("An error occured while deleting existing files.",sys)


    def save_uploaded_files(self, reference_file, actual_file):
        """
        Save reference and actual PDF files in the session directory.
        """
        try:
            self.delete_existing_files()
            self.log.info("Existing files deleted successfully")
            
            ref_path = self.base_dir / reference_file.name
            act_path = self.base_dir / actual_file.name

            if not reference_file.name.lower().endswith(".pdf") or not actual_file.name.lower().endswith(".pdf"):
                raise ValueError("Only PDF files are allowed.")

            with open(ref_path, "wb") as f:
                f.write(reference_file.getbuffer())

            with open(act_path, "wb") as f:
                f.write(actual_file.getbuffer())

            self.log.info("Files saved", reference=str(ref_path), actual=str(act_path), session=self.session_id)
            return ref_path, act_path

        except Exception as e:
            self.log.error("Error saving PDF files", error=str(e), session=self.session_id)
            raise DocumentPortalException("Error saving files", sys)
      

    def read_pdf(self, pdf_path: Path) -> str:
        """
        Read text content of a PDF page-by-page.
        """
        try:
            with fitz.open(pdf_path) as doc:
                if doc.is_encrypted:
                    raise ValueError(f"PDF is encrypted: {pdf_path.name}")

                all_text = []
                for page_num in range(doc.page_count):
                    page = doc.load_page(page_num)
                    text = page.get_text()  # type: ignore
                    if text.strip():
                        all_text.append(f"\n --- Page {page_num + 1} --- \n{text}")

            self.log.info("PDF read successfully", file=str(pdf_path), pages=len(all_text))
            return "\n".join(all_text)

        except Exception as e:
            self.log.error(f"Error reading PDF: {e}")
            raise DocumentPortalException("Error reading PDF", sys)


    def combine_documents(self) -> str:
        """
        Combine content of all PDFs in session folder into a single string.
        """
        try:
            content_dict = {}
            doc_parts = []
            
            for filename in sorted(self.session_path.iterdir()):
                if filename.is_file() and filename.suffix == ".pdf":
                    content_dict[filename.name] = self.read_pdf(filename)
                    
            for filename, content in content_dict.items():
                doc_parts.append(f"\n--- {filename} ---\n{content}")
             
            combined_text = "\n".join(doc_parts)
            self.log.info("Documents combined successfully", count=len(doc_parts))
            return combined_text   
        
        except Exception as e:
            self.log.error("Error combining documents, error=str(e)")
            raise DocumentPortalException("Error combining documents", sys)