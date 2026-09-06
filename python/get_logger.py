import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

def get_logger(name, log_dir='logs'):
    """Zwraca skonfigurowany logger"""

    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f'app_{datetime.now():%Y-%m-%d}.log')

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        log_file, maxBytes=10 * 1024 * 1024, backupCount=3)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger