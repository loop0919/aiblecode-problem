from random import randint

H, W = randint(1, 100), randint(1, 100)

grid = [
    ["." if randint(0, 100) <= randint(40, 95) else "#" for _ in range(W)]
    for _ in range(H)
]

s_i, s_j = randint(1, H), randint(1, W)
while True:
    g_i, g_j = randint(1, H), randint(1, W)
    if (s_i, s_j) != (g_i, g_j):
        break

grid[s_i - 1][s_j - 1] = "S"
grid[g_i - 1][g_j - 1] = "G"

print(H, W)
for row in grid:
    print(*row, sep="")
