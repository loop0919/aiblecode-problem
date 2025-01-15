# 解答コードを書く

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A - 1].append(B)
    graph[B - 1].append(A)

for i in range(N):
    print(len(graph[i]))
