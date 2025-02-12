# テストケースの生成コードを書く
from random import randint

N = 10**4

A = []
while (add := randint(1, 3)) + len(A) <= N:
    val = randint(1, N)
    while len(A) > 0 and (val := randint(1, N)) == A[-1]:
        pass
    A.extend([val] * add)

assert all(1 <= a <= len(A) for a in A)

print(len(A))
print(*A)
