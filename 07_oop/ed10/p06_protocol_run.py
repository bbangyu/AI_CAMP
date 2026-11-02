# p06_protocol_run.py

from typing import Protocol

class Printable(Protocol):
    def print_data(self) -> None: ...

class Report:
    def print_data(self) -> None:
        print("보고서를 출력 합니다.")

class Invoice:
    def print_data(self) -> None:
        print("청구서를 출력 합니다.")

def execute_print(obj:Printable) -> None:
    obj.print_data()

def main():
    execute_print(Report())
    execute_print(Invoice())


if __name__ == "__main__":
    main()