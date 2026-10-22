print("="*50)
print("3. 웹사이트 방문 사용자 분석")
print("="*50)

yesterday = {
    "user01", "user02",
    "user03", "user04"
}

today = {
    "user02", "user03",
    "user05", "user06"
}

# 요구 사항

# #### 1. 어제와 오늘 모두 방문한 사용자를 구하세요.
print(f'어제와 오늘 모두 방문한 사용자: {yesterday & today}')
# #### 2. 오늘 새롭게 방문한 사용자를 구하세요.
print(f'오늘 새롭게 방문한 사용자: {yesterday - today}')
# #### 3. 이틀 동안 한 번이라도 방문한 전체 사용자를 구하세요.
print(f'전체 사용자: {yesterday | today}')

