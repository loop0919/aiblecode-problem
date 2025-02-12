from random import randint

H, W = 100, 100
grid = [["."] * W for _ in range(H)]

s_i, s_j = randint(0, H - 1), randint(0, W - 1)
while True:
    g_i, g_j = randint(0, H - 1), randint(0, W - 1)
    if (s_i, s_j) != (g_i, g_j):
        break

grid[s_i][s_j] = "S"
grid[g_i][g_j] = "G"

print(H, W)
for row in grid:
    print(*row, sep="")
