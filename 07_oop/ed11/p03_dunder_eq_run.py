# p03_dunder_eq_run.py

class Employee:
    def __init__(self, emp_id:str, name:str)-> None:
        self.emp_id = emp_id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented

        return self.emp_id == other.emp_id

def main():
    a = Employee("E001", "김철수")
    b = Employee("E001", "김철수")
    c = Employee("E002", "이영희")

    print(a)
    print(b)
    print(a==b)
    print(a==c)
if __name__ == "__main__":
    main()