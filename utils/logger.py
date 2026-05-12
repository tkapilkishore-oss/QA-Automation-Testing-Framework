import logging
import os


# Create logs folder if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")


def get_logger():

    logger = logging.getLogger("QA_Framework")

    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:

        file_handler = logging.FileHandler("logs/test_execution.log")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger