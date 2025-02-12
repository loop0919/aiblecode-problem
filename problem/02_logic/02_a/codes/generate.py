# テストケースの生成コードを書く
from random import randint, shuffle
from string import ascii_letters as alpha

N = randint(1, 5)

if randint(0, 1):
    S = ["I", "l"] + [alpha[randint(0, len(alpha) - 1)] for _ in range(N)]
    shuffle(S)
else:
    beta = set(alpha) - set("lI"[randint(0, 1)])
    S = [list(beta)[randint(0, len(beta) - 1)] for _ in range(N)]

print(*S, sep="")
