# 解答コードを書く
N, Q = map(int, input().split())
A = list(map(int, input().split()))

index = 0

for _ in range(Q):
    S = input()

    if S == "left":
        if index > 0:
            index -= 1

    elif S == "right":
        if index < N - 1:
            index += 1

    elif S == "answer":
        print(A[index])
