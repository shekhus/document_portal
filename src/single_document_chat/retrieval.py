import sys
import os
from dotenv import load_dotenv
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.vectorstores import FAISS
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from utils.model_loader import ModelLoader
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import PromptType

class ConversationalRAG:
    def __init__(self,session_id: str, retriever) -> None:
       try:
           self.log = CustomLogger().get_logger(__name__)
       except Exception as e:
            self.log.error("Error initializing ConversationalRAG", error=str(e), session_id=session_id)
            raise DocumentPortalException("Failed to initialize ConversationalRAG", sys)
        
    
    def _load_llm(self):
        try:
            pass
        except Exception as e:
            self.log.error("Error loading LLM via ModelLoader", error=str(e))
            raise DocumentPortalException("Failed to load LLM", sys)
        
    def _get_session_history(self,ession_id: str):
        try:
            pass
        except Exception as e:
            self.log.error("Failed to access session history", session_id=session_id, error=str(e))
            raise DocumentPortalException("Failed to retrieve session history", sys)
        
    
    def load_retriever_from_faiss(self):
        try:
            pass
        
        except Exception as e:
            self.log.error("Failed to load retriever from FAISS", error=str(e))
            raise DocumentPortalException("Error loading retriever from FAISS", sys)
        

    def invoke(self):
        try:
            pass
        except Exception as e:
            self.log.error("Failed to invoke conversational RAG", error=str(e), session_id=self.session_id)
            raise DocumentPortalException("Failed to invoke RAG chain", sys)