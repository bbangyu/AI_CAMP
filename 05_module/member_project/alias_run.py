print("="*50)
print("1. 모듈에 별칭 지정하기")
print("="*50)

import math as m

print(m.sqrt(25))

print("="*50)
print("2. 모듈에서 가져온 함수에 별칭 지정하기")
print("="*50)

from math import sqrt as square_root

print(square_root(25))