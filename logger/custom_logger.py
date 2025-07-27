# import os
# import logging
# from datetime import datetime


# class CustomLogger:

#     def __init__(self,log_dir="logs"):
#         # Ensure logs directory exists
#         self.logs_dir = os.path.join(os.getcwd(), log_dir)
#         os.makedirs(self.logs_dir, exist_ok=True)

#         # Create timestamped log file name
#         log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#         log_file_path = os.path.join(self.logs_dir, log_file)

#         # Configure logging
#         logging.basicConfig(
#             filename=log_file_path,
#             format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
#             level=logging.INFO,
#         )
        

#     def log(self, name=__file__):
#         return logging.getLogger(os.path.basename(name))
        
# if __name__ == "__main__":
#         logger = CustomLogger()
#         logger = logger.get_logger(__file__)
#         logger.info("Custom logger initialized.")    
import os
import logging
from datetime import datetime

class CustomLogger:

    def __init__(self, log_dir="logs"):
        # 1. Create logs directory path relative to current folder
        self.logs_dir = os.path.join(os.getcwd(), log_dir)

        # 2. Make sure the logs folder exists
        os.makedirs(self.logs_dir, exist_ok=True)

        # 3. Create a unique log file name using date & time
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        log_file_path = os.path.join(self.logs_dir, log_file)

        # 4. Setup the logger settings globally
        logging.basicConfig(
            filename=log_file_path,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )

    def get_logger(self, name=__file__):
        # 5. Create a logger object and return it
        return logging.getLogger(os.path.basename(name))

if __name__ == "__main__":
    # 6. Create a CustomLogger object
    logger_obj = CustomLogger()

    # 7. Get the logger and use it
    logger = logger_obj.get_logger(__file__)
    logger.info("Custom logger initialized.")
