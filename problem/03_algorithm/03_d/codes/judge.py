result = int(input())
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            s_i, s_j = i, j
            break

X = input()
assert len(X) == result

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
    assert grid[curr_i][curr_j] != "#"

assert grid[curr_i][curr_j] == "G"

try:
    input()
    assert False
except EOFError:
    pass
