print("="*50)
print("2. 회원 정보 추가 및 수정하기")
print("="*50)

user = {
	"user_id":"Kim",
	"name":"Kim",
	"grade":"NORMAL"
}
# 새로운 데이터 추가:
# email" : "jamesol@naver.com"
user['email']='jamesol@naver.com'

# 수정: "grade": "NORMAL" -> "grade" : "VIP"
user['grade']='VIP'
print(user)