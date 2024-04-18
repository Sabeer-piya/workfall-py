import logging
import sys

logger=logging.getLogger()
formatter = logging.Formatter(fmt="%(asctime)s-%(levelname)s-%(message)s")
strem_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("app.log")
strem_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.handlers = [strem_handler, file_handler]
logger.setLevel(logging.INFO)