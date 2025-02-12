from functools import lru_cache

N = int(input())
A = list(map(int, input().split()))


@lru_cache(10**5)
def dp(n):
    if n >= N - 1:
        return 0

    ans = 0
    for i in range(1, A[n] + 1):
        ans += dp(n + i) + 1
    ans /= A[n]
    return ans


print(dp(0))
