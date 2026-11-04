from abc import ABC, abstractmethod

class DaoInterface(ABC):
    @abstractmethod
    def do_save(self, dto):
        pass

class MemberDao(DaoInterface):

    def do_save(self, dto):
        print("회원 저장:", dto)

dao = MemberDao()
dao.do_save("홍길동")