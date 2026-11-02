# common / __init__.py
# 모든 DTO의 조상 : Member, Book은 BaseDTO를 상속 받아야 한다.

#dataclass :
# __init__()
# __repr__()
# __eq__()
from dataclasses import dataclass

@dataclass
class BaseDTO:
    pass