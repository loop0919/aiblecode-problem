import sys

sys.setrecursionlimit(10**5 + 1)


ways = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

H, W = map(int, input().split())

grid = []
for i in range(H):
    S = list(input())
    grid.append(S)
    for j in range(W):
        if S[j] == "S":
            start_i, start_j = i, j
        elif S[j] == "G":
            goal_i, goal_j = i, j

visited = [[False] * W for _ in range(H)]
ans = []


def dfs(i, j):
    for way, (di, dj) in ways.items():
        next_i, next_j = i + di, j + dj
        if not (0 <= next_i < H and 0 <= next_j < W):
            continue

        if grid[i][j] == "#":
            continue

        if visited[next_i][next_j]:
            continue

        visited[i][j] = True
        ans.append(way)

        if (next_i, next_j) == (goal_i, goal_j):
            return True

        if dfs(next_i, next_j):
            return True
        ans.pop()
    return False


visited[start_i][start_j] = True
print("Yes" if dfs(start_i, start_j) else "No")

print(H, W)
for row in grid:
    print(*row, sep="")
