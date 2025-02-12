# テストケースの生成コードを書く
from random import randint

N = 2 * 10**5
Q = 10**4
A = [randint(10**9 - 9, (10**9 - 1)) for _ in range(N)]
A.sort()

print(N, Q)
print(*A)

for _ in range(Q):
    print(randint(10**9 - 10, (10**9)))
