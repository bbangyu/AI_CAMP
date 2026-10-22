print("="*50)
print("1. 중복 회원 ID제거하기")
print("="*50)

user_ids = [
    "kim", "lee", "park",
    "kim", "hong", "lee",
    "choi", "park"
]

# - set을 이용하여 중복 회원 ID를 제거하세요.
result = set(user_ids)
print(result)
# - 고유한 회원 수를 출력하세요.
print(len(result))
print(f'고유한 회원 수: {len(result)}')

