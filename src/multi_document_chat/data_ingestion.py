import uuid
from pathlib import Path
import sys
from datetime import datetime, timezone
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader



class DocumentIngestor:
    SUPPORTED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.md'}
    
    
# This is the `__init__` method of a class, likely `DocumentIngestor`. It initializes the object by:

# 1. Setting up a logger (`self.log`)
# 2. Creating base directories (`temp_dir` and `faiss_dir`) and their session-specific subdirectories (`session_temp_dir` and `session_faiss_dir`)
# 3. Generating a unique session ID if not provided
# 4. Initializing a `ModelLoader` object
# 5. Logging a success message with directory paths

# If any exception occurs during initialization, it logs an error message and raises a `DocumentPortalException`.
    
    def __init__(self, temp_dir:str = "data/multi_doc_chat",faiss_dir: str = "faiss_index", session_id: str | None = None):
        
        try:
            self.log = CustomLogger().get_logger(__name__)
            
            
            # base dirs
            self.temp_dir = Path(temp_dir)
            self.faiss_dir = Path(faiss_dir)
            self.temp_dir.mkdir(parents=True, exist_ok=True)
            self.faiss_dir.mkdir(parents=True, exist_ok=True)
            
            # sessionized paths
            self.session_id = session_id or f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
            self.session_temp_dir = self.temp_dir / self.session_id
            self.session_faiss_dir = self.faiss_dir / self.session_id
            self.session_temp_dir.mkdir(parents=True, exist_ok=True)
            self.session_faiss_dir.mkdir(parents=True, exist_ok=True)
            
            self.model_loader = ModelLoader()
            self.log.info(
                "DocumentIngestor initialized",
                temp_base=str(self.temp_dir),
                faiss_base=str(self.faiss_dir),
                session_id=self.session_id,
                temp_path=str(self.session_temp_dir),
                faiss_path=str(self.session_faiss_dir),
            )
        except Exception as e:
            self.log.error("Failed to initialize DocumentIngestor", error=str(e))
            raise DocumentPortalException("Initialization error in DocumentIngestor", sys)

    def ingest_files(self):
        # Logic to ingest the documents
        pass

    def _create_document_loader(self, documents):
        # Logic to create a document from the file path
        pass