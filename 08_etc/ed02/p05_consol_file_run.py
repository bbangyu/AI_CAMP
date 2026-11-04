import logging
import sys
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logger = logging.getLogger("member_app")
logger.setLevel(logging.DEBUG)
logger.propagate = False


formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s %(funcName)s : %(lineno)d - %(message)s"
)

# 콘솔 Handler
consol_handler = logging.StreamHandler(sys.stdout)
consol_handler.setLevel(logging.DEBUG)
consol_handler.setFormatter(formatter)

# 파일 Handler
file_handler = logging.FileHandler("logs/member.log", encoding="utf-8",)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# 중복 Handler 등록 방지
if not logger.handlers:
    logger.addHandler(consol_handler)
    logger.addHandler(file_handler)


def do_save(member_id:str):
    logger.debug("do_save() 시작")

    logger.info("회원 저장: %s",member_id)

    logger.debug("do_save() 종료")

do_save("pcwk01")
