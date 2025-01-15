from random import randint, shuffle

N, M = 12, 3
A_src = [1] * N + [0] * (M - 1)
shuffle(A_src)

A = [0]

for a in A_src:
    if a == 1:
        A[-1] += 1
    else:
        A.append(0)

tasks = [
    "".join(["o" if randint(0, 100) <= 60 else "x" for _ in range(M)]) for _ in range(N)
]

print(N, M)
print(*A)
print(*tasks, sep="\n")
