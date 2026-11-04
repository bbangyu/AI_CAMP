import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

Path("logs").mkdir(exist_ok=True)

logger = logging.getLogger("rotate_app")
logger.setLevel(logging.DEBUG)
logger.propagate = False

handler = RotatingFileHandler(
    filename="logs/app.log",
    maxBytes=1024*1024,
    backupCount=5, #보관할 백업 로그 파일 수
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s %(funcName)s : %(lineno)d - %(message)s"
)

handler.setFormatter(formatter)

#중복 Handler 등록 방지
if not logger.handlers:
    logger.addHandler(handler)

for i in range(1000):
    logger.info("로그 테스트:%d",i)