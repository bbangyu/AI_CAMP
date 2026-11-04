# p04_dunder_iter_run.py

class EmployeeCollection:
    def __init__(self):
        self.employees = []

    def add(self, name:str) -> None:
        self.employees.append(name)

    def __len__(self)-> int:
        return len(self.employees)

    def __iter__(self):
        return iter(self.employees)

def main():
    team = EmployeeCollection()

    team.add("김철수")
    team.add("이영희")

    print(f"직원수: {len(team)}")

    for name in team:
        print(name)


if __name__ == "__main__":
    main()