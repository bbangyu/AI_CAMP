# p12_inheritance_run.py

from dataclasses import dataclass

@dataclass
class BaseDTO:
    search_div : str
    search_word: str

@dataclass
class Member(BaseDTO):
    member_id : str
    name : str

member = Member(member_id ="pcwk01", name="이상무",search_div="",search_word="")

print(isinstance(member,Member))
print(isinstance(member,BaseDTO))

print(member)