# import logging
# import os
# from datetime import datetime
# import structlog


# class CustomLogger:
#     def __init__(self, log_dir="logs"):
#         # Ensure logs directory exists
#         self.logs_dir = os.path.join(os.getcwd(), log_dir)
#         os.makedirs(self.logs_dir, exist_ok=True)

#         # Timestamped log file (for persistence)
#         log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#         self.log_file_path = os.path.join(self.logs_dir, log_file)

#     def get_logger(self, name=__file__):
#         logger_name = os.path.basename(name)

#         # Configure logging for console + file (both JSON)
#         file_handler = logging.FileHandler(self.log_file_path)
#         file_handler.setLevel(logging.INFO)
#         file_handler.setFormatter(logging.Formatter("%(message)s"))  # Raw JSON lines

#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(logging.INFO)
#         console_handler.setFormatter(logging.Formatter("%(message)s"))

#         logging.basicConfig(
#             level=logging.INFO,
#             format="%(message)s",  # Structlog will handle JSON rendering
#             handlers=[console_handler, file_handler]
#         )

#         # Configure structlog for JSON structured logging
#         structlog.configure(
#             processors=[
#                 structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
#                 structlog.processors.add_log_level,
#                 structlog.processors.EventRenamer(to="event"),
#                 structlog.processors.JSONRenderer()
#             ],
#             logger_factory=structlog.stdlib.LoggerFactory(),
#             cache_logger_on_first_use=True,
#         )

#         return structlog.get_logger(logger_name)


# # --- Usage Example ---
# if __name__ == "__main__":
#     logger = CustomLogger().get_logger(__file__)
#     logger.info("User uploaded a file", user_id=123, filename="report.pdf")
#     logger.error("Failed to process PDF", error="File not found", user_id=123)

# +++++++


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
        
#     def get_logger(self,name=__file__):
#         return logging.getLogger(os.path.basename(name))
    
# if __name__ == "__main__":
#     logger=CustomLogger()
#     logger=logger.get_logger(__file__)
#     logger.info("Custom logger initialized.")
        
        
# class CustomLogger:
#     def __init__(self, log_dir="logs"):
#         # Ensure logs directory exists
#         self.logs_dir = os.path.join(os.getcwd(), log_dir)
#         os.makedirs(self.logs_dir, exist_ok=True)

#         # Create timestamped log file
#         log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#         self.log_file_path = os.path.join(self.logs_dir, log_file)

#     def get_logger(self, name=__file__):
#         """
#         Returns a logger instance with file + console handlers.
#         Default name is the current file name (without path).
#         """
#         logger_name = os.path.basename(name)
#         logger = logging.getLogger(logger_name)
#         logger.setLevel(logging.INFO)

#         # Formatter for both handlers
#         file_formatter = logging.Formatter(
#             "[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s"
#         )
#         console_formatter = logging.Formatter(
#             "[ %(levelname)s ] %(message)s"
#         )

#         # File handler (logs saved to file)
#         file_handler = logging.FileHandler(self.log_file_path)
#         file_handler.setFormatter(file_formatter)

#         # Console handler (logs printed on terminal)
#         console_handler = logging.StreamHandler()
#         console_handler.setFormatter(console_formatter)

#         # Avoid duplicate handlers if logger is reused
#         if not logger.handlers:
#             logger.addHandler(file_handler)
#             logger.addHandler(console_handler)

#         return logger


# # --- Usage Example ---
# if __name__ == "__main__":
#     logger = CustomLogger().get_logger(__file__)  # Logger will use file name as its name
#     logger.info("Logger initialized successfully.")



# import logging
# import os
# from datetime import datetime
# import structlog


# class CustomLogger:
#     _instance = None  # Singleton instance
#     _log_file_path = None  # Shared log file path for all loggers

#     def __new__(cls, log_dir="logs"):
#         # Ensure singleton pattern
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance._init_logger(log_dir)
#         return cls._instance

#     def _init_logger(self, log_dir):
#         # Ensure logs directory exists
#         self.logs_dir = os.path.join(os.getcwd(), log_dir)
#         os.makedirs(self.logs_dir, exist_ok=True)

#         # Create ONE timestamped log file for the whole run
#         if CustomLogger._log_file_path is None:
#             log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#             CustomLogger._log_file_path = os.path.join(self.logs_dir, log_file)

#     def get_logger(self, name=__file__):
#         logger_name = os.path.basename(name)

#         file_handler = logging.FileHandler(CustomLogger._log_file_path)
#         file_handler.setLevel(logging.INFO)
#         file_handler.setFormatter(logging.Formatter("%(message)s"))

#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(logging.INFO)
#         console_handler.setFormatter(logging.Formatter("%(message)s"))

#         logging.basicConfig(
#             level=logging.INFO,
#             format="%(message)s",
#             handlers=[console_handler, file_handler]
#         )

#         structlog.configure(
#             processors=[
#                 structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
#                 structlog.processors.add_log_level,
#                 structlog.processors.EventRenamer(to="event"),
#                 structlog.processors.JSONRenderer()
#             ],
#             logger_factory=structlog.stdlib.LoggerFactory(),
#             cache_logger_on_first_use=True,
#         )

#         return structlog.get_logger(logger_name)


# # --- Usage Example ---
# if __name__ == "__main__":
#     logger1 = CustomLogger().get_logger(__file__)
#     logger1.info("First logger instance created")

#     logger2 = CustomLogger().get_logger("another_module.py")
#     logger2.error("Still writing to the same file")


import os
import logging
from datetime import datetime
import structlog

class CustomLogger:
    _log_file_path = None  # shared across all instances

    def __init__(self, log_dir="logs"):
        # Ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create log file path ONCE
        if CustomLogger._log_file_path is None:
            log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
            CustomLogger._log_file_path = os.path.join(self.logs_dir, log_file)

    def get_logger(self, name=__file__):
        logger_name = os.path.basename(name)

        file_handler = logging.FileHandler(CustomLogger._log_file_path)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter("%(message)s"))

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter("%(message)s"))

        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[console_handler, file_handler]
        )

        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
                structlog.processors.add_log_level,
                structlog.processors.EventRenamer(to="event"),
                structlog.processors.JSONRenderer()
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )

        return structlog.get_logger(logger_name)

