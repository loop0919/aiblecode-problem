import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False

    return True


def solve():
    N = int(input())

    ok, ng = 0, 10**9 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if mid * (mid + 2) <= N:
            ok = mid
        else:
            ng = mid

    if ok * (ok + 2) == N and is_prime(ok) and is_prime(ok + 2):
        print("Yes")
    else:
        print("No")


T = int(input())
for _ in range(T):
    solve()
