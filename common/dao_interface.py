from abc import ABC, abstractmethod
from common.base_dto import BaseDTO


class DaoInterface(ABC):
    @abstractmethod
    def do_update(self,dto: BaseDTO) -> int:
        pass

    @abstractmethod
    def do_retrieve(self) -> list[BaseDTO]:
        pass

    @abstractmethod
    def do_delete(self,dto_id: str) -> int:
        pass

    @abstractmethod
    def do_select_one(self,dto_it: str) -> BaseDTO:
        pass

    @abstractmethod
    def do_save(self,dto:BaseDTO)->int:
        """ 공통 dao interface 저장 """
        pass