# p09_runtime_checkable_run.py

from typing import Protocol, runtime_checkable

@runtime_checkable
class Printable(Protocol):
    def print_data(self) -> None: ...

class Report:
    def print_data(self) -> None: 
        print("보고서 출력")

print(isinstance(Report(), Printable))