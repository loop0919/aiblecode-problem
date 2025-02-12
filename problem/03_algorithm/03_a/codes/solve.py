N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    X = int(input())

    ok, ng = 0, N + 1

    while ng - ok > 1:
        mid = (ok + ng) // 2

        if A[mid - 1] <= X:
            ok = mid
        else:
            ng = mid

    print(ok)
