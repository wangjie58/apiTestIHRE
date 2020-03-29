import logging
import os
from logging import handlers
# 全局变量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {"Content-Type":"application/json"}
EMP_ID = ""
def init_logging():
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    sh=logging.StreamHandler()
    filename=os.path.dirname(os.path.abspath(__file__))+"/log/ihrm.log"
    fh=logging.handlers.TimedRotatingFileHandler(filename,when="M",interval=1,backupCount=3,encoding="utf-8")
    fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter=logging.Formatter(fmt)
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)
