"""Module logging initialization"""

import sys
from pathlib import Path
from loguru import logger


def logger_init(log_file_path: Path):
    """Init logging"""

    # Disable default logging with output to stderr
    logger.remove()

    logger.add(
        log_file_path,
        level="TRACE",
        mode="w",
        backtrace=True,
        diagnose=True,
        delay=True,
    )
    logger.add(
        sys.stdout,
        colorize=True,
        format="{level} | {message}",
        level="INFO",
    )


logger_init(log_file_path=Path("./logs/testrun.log"))
