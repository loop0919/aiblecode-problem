# テストケースの生成コードを書く
from random import randint

T = 100
print(T)
for _ in range(T):
    N = randint(1, 10)
    M = randint(1, N)

    print(N, M)
    print(*[randint(0, 10**9 + 6) for _ in range(N)])
