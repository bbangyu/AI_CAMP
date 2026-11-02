# p03_abstract_class_run.py
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,emp_id:str, name:str):
        self.emp_id = emp_id
        self.name = name
    @abstractmethod
    def calculate_salary(self)-> int:
        pass

    def show_info(self) -> None:
        print(f"사번: {self.emp_id}")
        print(f"이름: {self.name}")
        print(f"급여: {self.calculate_salary():,}원")

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, salary, bonus):
        super().__init__(emp_id, name)
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self) -> int:
        return self.salary + self.bonus
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, hours:int, hourly_rate:int):
        super().__init__(emp_id, name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self) -> int:
        return self.hours * self.hourly_rate

def main():
 
    employees = [FullTimeEmployee("E001", "김철수", 3_000_000, 500_000),
                 ContractEmployee("E002", "이영희", 160, 15_000)]

    for employee in employees:
        employee.show_info()

if __name__ == "__main__":
    main()