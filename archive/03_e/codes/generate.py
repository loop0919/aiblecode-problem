from itertools import permutations
from random import randint
from string import ascii_lowercase

T = 100
print(T)

for i in range(T):
    length = randint(2, 7)
    S = "".join([ascii_lowercase[randint(0, 25)] for _ in range(length)])
    X = sorted(set(permutations(S)))
    print(randint(1, len(X)))
    print(*X[randint(0, len(X) - 1)], sep="")
