from random import randint

N = randint(2, 5)
print(N)
print(*[randint(1, 100) for _ in range(N - 1)])
