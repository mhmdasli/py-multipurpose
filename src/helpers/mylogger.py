import logging

def create_logger(name):
    # name
    mylogger = logging.getLogger(name)
    # level
    mylogger.setLevel(logging.DEBUG)
    # file
    fh = logging.FileHandler('logs.log')
    fh.setLevel(logging.DEBUG)
    # format
    formatter = logging.Formatter("""%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(funcName)s():line %(lineno)d  - %(relativeCreated)6d - %(threadName)s :\n %(message)s\n""")
    fh.setFormatter(formatter)
    mylogger.addHandler(fh)
    
    return mylogger
   