# p10_frozen_run.py

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x:int
    y:int


point = Point(10,20)

print(point)

point.x =  30 #dataclasses.FrozenInstanceError