
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
    def __init__(self):
        pass

    def delete_existing_files(self):
        """
        Delete any existing PDF files at specidied path
        """
        try:
          pass
        except Exception as e:
            self.log.error(f"Error deleting existing files: {e}")
            raise DocumentPortalException("An error occured while deleting existing files.",sys)

    def save_uploaded_files(self):
        """
        Save reference and actual PDF files in the session directory.
        """
        try:
          pass
        except Exception as e:
            self.log.error(f"Error saving uploaded files: {e}")
            raise DocumentPortalException("Error saving files", sys)
      

    def read_pdf(self):
        """
        Read text content of a PDF page-by-page.
        """
        try:    
            pass
        except Exception as e:
            self.log.error(f"Error reading PDF: {e}")
            raise DocumentPortalException("Error reading PDF", sys)
