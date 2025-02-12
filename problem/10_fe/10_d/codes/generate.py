from random import randint

length = randint(1, 30)
print(*[randint(0, 1) for _ in range(length)], sep="")
