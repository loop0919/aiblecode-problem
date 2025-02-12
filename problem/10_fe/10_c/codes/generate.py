import math
from decimal import Decimal
from random import randint

N = 100

A = [f"{randint(-10000, 10000) / 100:.2f}" for _ in range(N)]
B = [f"{randint(-10000, 10000) / 100:.2f}" for _ in range(N)]

print(N)
print(*A)
print(*B)
