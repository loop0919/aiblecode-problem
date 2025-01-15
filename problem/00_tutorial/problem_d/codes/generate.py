from random import randint

N = randint(1, 100)
A = [randint(0, 10**9) for _ in range(N)]
Q = randint(1, 10**4)

cmd = ["left", "right"]

print(N, Q)
print(*A)
for _ in range(Q):
    print(cmd[randint(0, len(cmd) - 1)])
