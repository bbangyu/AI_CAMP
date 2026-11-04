# p03_logger_obj_run.py
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(

    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s %(filename)s %(funcName)s : %(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def do_save(member_id:str):
    logger.debug("do_save() 시작")

    logger.info("회원 저장: %s",member_id)

    logger.debug("do_save() 종료")

do_save("pcwk01")

