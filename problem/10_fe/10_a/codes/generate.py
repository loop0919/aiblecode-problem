from random import randint, shuffle

A = [0, 0, 0]
while len(set(A)) < 3:
    A = [randint(1, 10 ** (9)) for _ in range(3)]

shuffle(A)

print(*A)
