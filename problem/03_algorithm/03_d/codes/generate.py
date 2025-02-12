import random
import sys

sys.setrecursionlimit(10**6)


def generate_maze(H, W):
    # 偶数のサイズに調整
    if H % 2 == 0:
        H += 1
    if W % 2 == 0:
        W += 1

    # 全てを道で埋める
    maze = [["."] * W for _ in range(H)]

    # 探索の方向（上下左右）
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def carve(x, y):
        maze[y][x] = "."  # 道を掘る
        random.shuffle(directions)  # ランダムな方向に進む
        for dy, dx in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < W - 1 and 0 < ny < H - 1 and maze[ny][nx] == ".":
                maze[y + dy // 2][x + dx // 2] = "."  # 途中の壁を壊す
                carve(nx, ny)

    # スタート地点（左上）とゴール地点（右下）
    maze[0][0] = "S"
    maze[H - 1][W - 1] = "G"

    # 掘り始める地点を適当に選ぶ
    carve(1, 1)

    return ["".join(row) for row in maze]


# 例: 高さ15、幅21の迷路を生成
H, W = 100, 100

maze = generate_maze(H, W)
print(len(maze), len(maze[0]))
for row in maze:
    print(row)
