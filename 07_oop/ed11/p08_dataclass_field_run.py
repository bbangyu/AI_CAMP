# p08_dataclass_field_run.py

from dataclasses import dataclass, field

@dataclass
class Student:
    name:str
    scores:list[int] = field(default_factory=list)


student1 = Student("홍길동")
student2 = Student("이상무")

student1.scores.append(90)

print(student1.scores)
print(student2.scores)
