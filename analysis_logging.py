"""Logging object for the project"""

import logging


class AnalysisLogger(logging.Logger):
    """
    Custom logger
    """

    def __init__(self, name: str, level=logging.NOTSET):
        super().__init__(name, level)


def configure_logger(enable_logging: bool):
    """
    Method to set whether logging is enabled or disabled
    """
    logger = AnalysisLogger(__name__, level=logging.DEBUG if enable_logging else logging.NOTSET)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Configure the logging handlers (e.g., file, console)
    if enable_logging:
        file_handler = logging.FileHandler('analysis_logs.log', mode='a', delay=True)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
