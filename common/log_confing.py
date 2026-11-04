import logging
import sys
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler


def setup_logging():
    Path("logs").mkdir(exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)s :%(lineno)d - %(message)s"
    )
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # 중복 Handler 등록 방지
    # 기존에 등록한 Handler가 있으면 중복 설정 방지
    if any(
        getattr(handler, "_myapp_handler", False)
        for handler in root_logger.handlers
    ):
        return
        
    # 콘솔 Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    console_handler._myapp_handler = True
    
    # TimedRotatingFileHandler 

    file_handler = TimedRotatingFileHandler(
        filename="logs/app.log", 
        when="midnight",
        interval=1,
        backupCount=365,  # 일별 백업 파일 최대 365개
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    file_handler._myapp_handler = True

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    
    