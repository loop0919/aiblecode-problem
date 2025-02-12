T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    fib = list(map(int, input().split()))
    for _ in range(2, M):
        fib.append(fib[-1] + fib[-2])
    print(fib[M - 1])
