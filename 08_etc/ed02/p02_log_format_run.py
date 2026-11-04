# p02_log_format_run.py
import logging

logging.basicConfig(

    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s %(filename)s %(funcName)s : %(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.debug("debug 메시지")
logging.info("info 메시지")
logging.warning("warning 메시지")
logging.error("error 메시지")
logging.critical("critical 메시지")