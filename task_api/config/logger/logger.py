import logging

from task_api.config.logger import logger_type


class Logger:
    _logger = logger_type.get_json_logger()

    @classmethod
    def set_logger(cls, logging_type: logger_type.LoggingType):
        cls._logger.disabled = False
        cls._logger = logging.getLogger("DiagnoZip logger")

        cls._clear_logger()

        if logging_type == logger_type.LoggingType.PRETTY:
            cls._logger = logger_type.get_pretty_logger()
        else:
            cls._logger = logger_type.get_json_logger()

    @classmethod
    def get_logger(cls) -> logging.Logger:
        if cls._logger is None:
            cls.set_logger(logger_type.LoggingType.JSON)

        return cls._logger

    @classmethod
    def _clear_logger(cls):
        for handler in cls._logger.handlers:
            cls._logger.removeHandler(handler)
        for filter in cls._logger.filters:
            cls._logger.removeFilter(filter)
