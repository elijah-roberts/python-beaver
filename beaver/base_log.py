# -*- coding: utf-8 -*-


class BaseLog(object):

    def __init__(self, logger=None):
        self._logger = logger
        print("test")

    def _log_debug(self, message):
        if self._logger:
            self._logger.debug(self._log_template.format(message))

    def _log_info(self, message):
        if self._logger:
            self._logger.info(self._log_template.format(message))

    def _log_warning(self, message):
        if self._logger:
            self._logger.warning(self._log_template.format(message))
