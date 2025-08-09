import sys
from dotenv import load_dotenv
import pandas as pd
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import SummaryResponse,PromptType


class DocumentComparatorLLM:
    def __init__(self):
        load_dotenv()
        self.log = CustomLogger().get_logger(__name__)
        self.loader = ModelLoader()
        self.llm = self.loader.load_llm()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)
        self.prompt = PROMPT_REGISTRY["document_comparison"]
        self.chain = self.prompt | self.llm | self.parser
        self.log.info("DocumentComparatorLLM initialized", model=self.llm)

    def compare_documents(self):
        """ compare two documnets and return a structured comparison response """
        
        try:
            pass
        except Exception as e:
            self.log.error(f"Document comparison failed: {e}")  
            raise DocumentPortalException("An error occured while comparing documents" , sys) from e
    
    def _format_response(self):
        """format the comparison response from LLM to a structured format """
        try:
           pass
        except Exception as e:
            self.log.error("Error formatting response into DataFrame", error=str(e))
            DocumentPortalException("Error formatting response", sys)