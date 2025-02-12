judge = input()
N, M = map(int, input().split())
A = list(map(int, input().split()))
tasks = [input() for _ in range(N)]

ans = input()
assert judge == ans

if judge == "No":
    exit()

count = [0] * M
for i in range(N):
    task = int(input())
    assert 1 <= task <= M
    assert tasks[i][task - 1] == "o"
    count[task - 1] += 1

assert count == A

try:
    input()
    assert False
except EOFError:
    pass
