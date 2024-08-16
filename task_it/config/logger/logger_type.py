import json
import logging
from enum import Enum

import colorlog


class LoggingType(Enum):
    PRETTY = "pretty"
    JSON = "json"


def get_pretty_logger() -> logging.Logger:
    logger = logging.getLogger("DiagnoZip logger")

    log_format = "%(blue)s%(asctime)s%(reset)s - %(log_color)s%(levelname)s%(reset)s: %(thin)s%(filename)s:%(lineno)d%(reset)s\n  %(message)s"

    color_formatter = colorlog.ColoredFormatter(
        log_format,
        datefmt="%H:%M:%S",
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(color_formatter)

    logger.addHandler(console_handler)

    logger.setLevel(logging.INFO)

    return logger


def get_json_logger() -> logging.Logger:
    logger = logging.getLogger("DiagnoZip logger")

    class CustomJsonFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:
            super(CustomJsonFormatter, self).format(record)
            output = {k: str(v) for k, v in record.__dict__.items()}
            return json.dumps(output)

    cf = CustomJsonFormatter()
    sh = logging.StreamHandler()
    sh.setFormatter(cf)

    logger.addHandler(sh)
    logger.level = logging.INFO

    return logger
