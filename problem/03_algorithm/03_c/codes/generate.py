from random import randint
from itertools import product

N, K = randint(2, 10), randint(-(100), 100)

A = [randint(1, 100) for _ in range(N)]


def check():
    for prod in product(("+", "-"), repeat=N - 1):
        val = A[0]
        for i in range(1, N):
            val += A[i] * (1 if prod[i - 1] == "+" else -1)

        if val == K:
            return "Yes"

    return "No"


while check() == "No":
    N, K = randint(2, 10), randint(-(100), 100)

    A = [randint(1, 100) for _ in range(N)]
print(N, K)
print(*A)
