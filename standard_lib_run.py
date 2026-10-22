print("="*50)
print("표준 라이브러리(Standard Library)")
print("="*50)

import math

radius = 5

area = radius ** 2 * math.pi

print(f'원의 넓이:,{area:.2f}')

print({math.gcd(12,18)})
print(round(3.6)) #4
print(round(2.5)) #2
print(round(3.5)) #4

print("="*50)
print("random 모듈 ㅡ 난수 생성")
print("="*50)

import random

print("실수 난수:",random.random())
print("정수 난수:",random.randint(1,10))
print("범위 난수:",random.randrange(1,10))
print("실수 범위:",random.uniform(1,10))

#seed() 사용
random.seed(100)
print(random.randint(1,100))

random.seed(100)
print(random.randint(1,100))

print("="*50)
print("datetime 모듈")
print("="*50)

from datetime import datetime, date, timedelta

#현재 날짜와 시간 : local의 시간 기준(변경 금지)

now = datetime.now()
today = date.today()
print("현재 날짜와 시간:",now)
print("오늘 날짜:", today)

print("연도:",now.year)
print("월:",now.month)
print("일:",now.day)
print("시:",now.hour)
print("분:",now.minute)
print("초:",now.second)

print("="*50)
print("날짜 출력 형식 변경: strftime()")
print("="*50)

now = datetime.now()

print(now.strftime("%Y/%m/%d"))
print(now.strftime("%Y%m%d"))
print(now.strftime("%Y/%m/%d %H:%M:%S"))

print("="*50)
print("날짜 계산: timedelta")
print("="*50)

today=date(2026,10,14)

tomorrow = today + timedelta(days=1)
after_week = today + timedelta(days=7)
yesterday = today - timedelta(days=1)

print('기준일:', today)
print('내일:', tomorrow)
print('7일 후:', after_week)
print('어제:', yesterday)

#mini 프로젝트 남은 기간 계산하기 
start_date = date(2026,10,14)
end_date = date(2026,10,30)

duration = end_date - start_date

print(f'프로젝트 시작일 : {start_date}')
print(f'프로젝트 종료일: {end_date}')
print(f'날짜 차이: {duration}일')

print("="*50)
print("os 모듈 ㅡ 운영체제 기능")
print("="*50)

import os

print("현재 작업 디렉터리:", os.getcwd())
print("현재 작업 디렉터리:", os.name)

print("="*50)
print("os 모듈 ㅡ 폴더 생성")
print("="*50)

folder_name = "data"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print('폴더 생성 완료')
else:
    print('이미 존재하는 폴더입니다.')

print("="*50)
print("os 모듈 ㅡ 여러 단계의 폴더 생성")
print("="*50)

folder_path = os.path.join("pcwk","data","backup")

os.makedirs(folder_path,exist_ok=True)

print("폴더 생성 완료",folder_path)

print("="*50)
print("os 환경변수 읽기")
print("="*50)

user_name = os.getenv("USERNAME")
path = os.getenv("PATH")

pcwk=os.getenv("PCWK_PASSWORD")

print("Windows 사용자:",user_name)
print("Windwos path:",path)
print("PCWK_PASSWORD:",pcwk)

print("="*50)
print(" pathlib 모듈 - 객체지향 파일 및 경로 관리")
print("="*50)

from pathlib import Path

path = Path("data/students.json")

print("파일 이름:",path.name)
print("확장자::",path.suffix)
print("확장자 제외:",path.stem)
print("상위 폴더:",path.parent)

print("="*50)
print(" pathlib 모듈 - 파일 생성 및 읽기")
print("="*50)

file_path = Path("data") / "pcwk.txt"

file_path.parent.mkdir(parents=True, exist_ok=True)

#pcwk.txt 파일에 내용 기록
file_path.write_text(
    "오늘은 즐거운 수요일!\n표준 라이브러리 학습",
    encoding="utf-8"
)

#pcwk.txt파일 내용 읽기

content = file_path.read_text(encoding="utf-8")

print(f'content:\n{content}')