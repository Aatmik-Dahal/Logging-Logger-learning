import logging

logger = logging.getLogger("Testlogger")#this line is important
logging.basicConfig(level=logging.DEBUG)#this line is important too

logger.info("this is not showing up ")
logger.warning("This is a warning")
logger.error("This is a error i would say")
logger.critical("Idk this is a critical messege")
logger.debug("This is a debug shit")