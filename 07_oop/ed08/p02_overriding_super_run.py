# p02_overriding_super_run.py

class Member:

    def show_info(self):
        print("회원 기본 정보")

class AdminMember(Member):

    def show_info(self):
        super().show_info()
        print("관리자 추가 정보")

admin = AdminMember()
admin.show_info()