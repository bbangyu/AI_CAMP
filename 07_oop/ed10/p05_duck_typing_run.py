# p05_duck_typing_run.py

class Report:
    def print_data(self) -> None:
        print("보고서를 출력 합니다.")

class Invoice:
    def print_data(self) -> None:
        print("청구서를 출력 합니다.")

def execute_print(obj):
    obj.print_data()

def main():
    execute_print(Report())
    execute_print(Invoice())

if __name__ == "__main__":
    main()