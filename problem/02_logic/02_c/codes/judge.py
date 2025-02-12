# 隠しファイルを受け取る
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            s_i, s_j = i, j
        if grid[i][j] == "G":
            g_i, g_j = i, j

# 提出をジャッジする
X = input()
assert len(X) == abs(g_i - s_i) + abs(g_j - s_j)

curr_i, curr_j = s_i, s_j

for x in X:
    if x == "^":
        curr_i -= 1
    elif x == "v":
        curr_i += 1
    elif x == "<":
        curr_j -= 1
    elif x == ">":
        curr_j += 1
    else:
        assert False

    assert 0 <= curr_i < H and 0 <= curr_j < W

assert grid[curr_i][curr_j] == "G"

try:
    input()
    assert False
except EOFError:
    pass
