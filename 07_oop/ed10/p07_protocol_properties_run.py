# p07_protocol_properties_run.py

from typing import Protocol

class Named(Protocol):
    name: str

    def display(self) -> str:
        ...

class Member:
    def __init__(self, name:str) ->None:
        self.name = name
        
    def display(self) -> str:
        return f"회원:{self.name}"

def show_name(obj:Named) -> None:
    print(obj.display())

def main():
    show_name(Member("김철수"))


if __name__ == "__main__":
    main()