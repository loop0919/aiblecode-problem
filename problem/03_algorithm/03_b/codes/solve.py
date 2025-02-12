from itertools import groupby

N = int(input())
A = list(map(int, input().split()))

answer = []

for a, li in groupby(A):
    answer.extend([a] * (4 - len(list(li))))

print(len(answer))
print(*answer[::-1])
