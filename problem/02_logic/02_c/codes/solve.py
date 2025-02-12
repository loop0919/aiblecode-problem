# 隠しファイルを受け取る
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

print(H, W)
for row in grid:
    print(*row, sep="")
