# テストケースの生成コードを書く
from random import randint

T = 100
print(T)

for _ in range(T):
    M = randint(1, 80)
    A = [randint(1, 100) for _ in range(2)]
    print(M)
    print(*A)
