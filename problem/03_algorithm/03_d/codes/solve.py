import sys

sys.setrecursionlimit(10**5 + 1)


ways = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            start_i, start_j = i, j
        elif grid[i][j] == "G":
            goal_i, goal_j = i, j

dist = [[-1] * W for _ in range(H)]
dist[start_i][start_j] = 0

visited = [[False] * W for _ in range(H)]
visited[start_i][start_j] = True

que = deque([(start_i, start_j)])

while que:
    curr_i, curr_j = que.popleft()

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_i, next_j = curr_i + di, curr_j + dj

        if not (0 <= next_i < H and 0 <= next_j < W):
            continue

        if grid[next_i][next_j] == "#":
            continue

        if visited[next_i][next_j]:
            continue

        dist[next_i][next_j] = dist[curr_i][curr_j] + 1
        visited[next_i][next_j] = True
        que.append((next_i, next_j))

print(dist[goal_i][goal_j])

print(H, W)
for row in grid:
    print(*row, sep="")
