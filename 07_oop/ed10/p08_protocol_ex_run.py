# p08_protocol_ex_run.py

from typing import Protocol

class SalaryCalculable(Protocol):
    def calculate_salary(self) -> float:
        ...

class ContractEmployee:
    def __init__(self, hours:float, houlry_rate:float):
        self.hours = hours
        self.houlry_rate = houlry_rate

    def calculate_salary(self) -> float:
        return self.hours * self.houlry_rate


class FullTimeEmployee():

    def __init__(self,salary:float,bonus:float) -> None:
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.salary + self.bonus

def print_salary(employee:SalaryCalculable) -> None:
    print(f"급여: {employee.calculate_salary():,.0f}원")




def main():
    # full_emp = FullTimeEmployee(3_000_000,500_000)
    # print_salary(full_emp)

    employees : list[SalaryCalculable] = [
        FullTimeEmployee(3_000_000,500_000),
        ContractEmployee(160,15_000)
    ]

    for employee in employees:
        print_salary(employee)
        
if __name__ == "__main__":
    main()