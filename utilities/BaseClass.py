import inspect
import logging
import time

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def time_5(self):
        time.sleep(5)

    def time_3(self):
        time.sleep(3)

    def get_logger(self):

        loggerName= inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)


        filehandler = logging.FileHandler('logfile.log')


        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)


        logger.setLevel(logging.DEBUG)
        return logger
