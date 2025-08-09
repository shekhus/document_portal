# import sys
# import traceback
# from logger.custom_logger import CustomLogger
# logger=CustomLogger().get_logger(__file__)


# class DocumentPortalException(Exception):
#     """Custom exception for Document Portal"""
#     def __init__(self,error_message,error_details:sys):
#         print(error_details.exc_info())
#         _,_,exc_tb=error_details.exc_info()
#         self.file_name=exc_tb.tb_frame.f_code.co_filename
#         self.lineno=exc_tb.tb_lineno
#         self.error_message=str(error_message)
#         self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info())) 
#     def __str__(self):
#        return f"""
#         Error in [{self.file_name}] at line [{self.lineno}]
#         Message: {self.error_message}
#         Traceback:
#         {self.traceback_str}
#         """
    
# if __name__ == "__main__":
#     try:
#         # Simulate an error
#         a = 1 / 0
#         print(a)
#     except Exception as e:
#         app_exc=DocumentPortalException(e,sys)
#         logger.error(app_exc)
#         raise app_exc

# ++++++

import sys
from logger.custom_logger import CustomLogger


class DocumentPortalException(Exception):
    """
    Custom exception for document portal errors.
    Automatically logs the error in the shared log file.
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        # Use the same shared log file from CustomLogger
        log = CustomLogger().get_logger(__name__)

        # Extract traceback info
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown file"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown line"

        # Log the exception in JSON format
        log.error(
            error_message,
            file=file_name,
            line=line_number,
            error_type=self.__class__.__name__
        )

        # Prepare detailed exception message for display
        self.error_message = (
            f"\nError in [{file_name}] at line [{line_number}]"
            f"\nMessage: {error_message}"
        )

    def __str__(self):
        return self.error_message
