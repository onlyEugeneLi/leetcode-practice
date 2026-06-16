import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("dev.log")
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("V1--Division error occurred")  # Includes full traceback
    # OR
    # logger.error("Division error", exc_info=True)  # Explicit traceback
    logger.error("V2--Division error", exc_info=False)  # Inexplicit traceback