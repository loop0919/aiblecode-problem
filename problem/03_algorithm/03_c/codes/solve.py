from itertools import product

N, K = map(int, input().split())
A = list(map(int, input().split()))


def check():
    for prod in product(("+", "-"), repeat=N - 1):
        val = A[0]
        for i in range(1, N):
            val += A[i] * (1 if prod[i - 1] == "+" else -1)

        if val == K:
            return "Yes"

    return "No"


print(check())
print(N, K)
print(*A)
