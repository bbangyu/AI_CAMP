class EmailSender:
    def send(self, message:str):
        print("메일 발송:", message)

class MemberService:
    def register(self, sender:EmailSender):
        sender.send("회원 가입을 환영합니다.")

service = MemberService()
service.register(EmailSender())