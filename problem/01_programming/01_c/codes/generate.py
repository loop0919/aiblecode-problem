# テストケースの生成コードを書く
from random import randint

A = randint(0, 5) if randint(0, 2) == 0 else randint(6, 100)
H = (randint(1000, 1199) if randint(0, 2) == 0 else randint(1200, 2000)) / 10

print(f"{A} {H:.1f}")
