from copy import deepcopy

P = 10**9 + 7


def multiple(A, B):
    x, y, z = len(A), len(B[0]), len(A[0])
    result = [[0] * y for _ in range(x)]

    for i in range(x):
        for j in range(y):
            for k in range(z):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= P

    return result


def power(A, K):
    log_K = len(bin(K)[2:])
    n = len(A)

    doubling = [[[0] * n for _ in range(n)] for _ in range(log_K)]
    doubling[0] = deepcopy(A)

    for i in range(log_K - 1):
        doubling[i + 1] = multiple(doubling[i], doubling[i])

    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for i in range(log_K):
        if (K >> i) & 1:
            result = multiple(result, doubling[i])

    return result


def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    matrix = [[0] * N for _ in range(N)]

    for i in range(N - 1):
        matrix[i][i + 1] = 1

    for i in range(N):
        matrix[N - 1][i] = 1

    print(multiple(power(matrix, M - 1), [[a] for a in A])[0][0])


T = int(input())
for _ in range(T):
    solve()
