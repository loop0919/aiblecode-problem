# テストケースの生成コードを書く
from random import randint

N = 100
M = N - 1

v = randint(1, N)

print(N, M)
for u in range(1, N + 1):
    if u == v:
        continue
    print(*sorted([u, v]))
