import logging
from logging.handlers import RotatingFileHandler
import sys
import datetime

def create_logger(name):
    # log path
    logFile = 'storage/logs/logs_'+datetime.datetime.now().strftime("%Y_%m_%d")+'.log'
    my_handler = RotatingFileHandler(logFile)
    # set format
    formatter = logging.Formatter("""%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(funcName)s():line %(lineno)d  - %(relativeCreated)6d - %(threadName)s :\n %(message)s\n""")
    my_handler.setFormatter(formatter)
    # logger name
    mylogger = logging.getLogger(name)
    # logger level
    mylogger.setLevel(logging.DEBUG)
    # add file handler
    mylogger.addHandler(my_handler)
    # add console handler
    mylogger.addHandler(logging.StreamHandler(sys.stdout))
    return mylogger
   