import os
import sys
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from prompt.prompt_library import *


class DocumentAnalyzer:
    """
    Analyzes documents using a pre-trained model.
    Automatically logs all actions and supports session-based organization.
    """
    def __init__(self):
        pass

    def analyze_document(self):
        pass
    