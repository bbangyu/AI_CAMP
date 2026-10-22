# member_service.py

import json 
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data") / "members.json"

def save_members(members):
    """회원목록을 JSON파일에 기록"""

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w",encoding="utf-8") as file:
        json.dump(
            members,
            file,
            indent=4,          #들여 쓰기 4칸으로 가독성 향상
            ensure_ascii=False #한글을 \uxxxx로 변환하지 않고 출력
        )


def load_members():
    """JSON 파일에서 회원 목록 불러오기"""

    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def register_member(members, user_id, name):
    """회원 등록"""

    for member in members:
        if member['user_id'] == user_id:
            return False



    member = {
        "user_id": user_id,
        "name": name,
        "reg_date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    members.append(member)
    return True