"""Module logging initialization"""

import sys
from loguru import logger


def logger_init():
    """Init logger"""

    # Disable default logging with output to stderr
    logger.remove()

    logger.add(
        sys.stdout,
        colorize=True,
        format="{level} | {message}",
        level="INFO",
    )


logger_init()
