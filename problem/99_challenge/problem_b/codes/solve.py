# 解答コードを書く
from collections import defaultdict

N, M, P = map(int, input().split())

cache = defaultdict(lambda: 1)
cache[N + 1] = N % P
sum_val = N % P

for i in range(1, M):
    sum_val -= cache[i]
    sum_val += cache[N + i]
    sum_val %= P

    cache[N + i + 1] = sum_val

print(cache[N + M])
