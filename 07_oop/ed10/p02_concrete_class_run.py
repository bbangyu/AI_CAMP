# p02_concrete_class_run.py

class Employee:
    def __init__(self,emp_id:str, name:str):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self)-> int:
        return  0

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, salary, bonus):
        super().__init__(emp_id, name)
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self) -> int:
        return self.salary + self.bonus

def main():
    employee = Employee("E000", "임시직원")
    full_time = FullTimeEmployee("E001", "김철수", 3_000_000, 500_000)
    print(employee.calculate_salary())
    print(f"{full_time.calculate_salary():,}")

if __name__ == "__main__":
    main()