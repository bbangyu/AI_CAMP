import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler

Path("logs").mkdir(exist_ok=True)

logger = logging.getLogger("daily_app")
logger.setLevel(logging.DEBUG)
logger.propagate = False

handler = TimedRotatingFileHandler(
    filename="logs/app.log",
    when="midnight",
    interval=1,
    backupCount=7, #보관할 백업 로그 파일 수
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s %(funcName)s : %(lineno)d - %(message)s"
)

handler.setFormatter(formatter)

#중복 Handler 등록 방지
if not logger.handlers:
    logger.addHandler(handler)


logger.info("일별 로그 기록")