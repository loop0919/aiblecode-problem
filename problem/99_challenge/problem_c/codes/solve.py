from itertools import product

N, M = map(int, input().split())
A = list(map(int, input().split()))

tasks = [input() for _ in range(N)]


def check():
    for aloc in product(range(M), repeat=N):
        count = [0] * M
        is_valid = True

        for i, a in enumerate(aloc):
            count[a] += 1
            if tasks[i][a] == "x":
                is_valid = False
                break

        if not is_valid or count != A:
            continue

        print("Yes")
        return

    print("No")


check()

print(N, M)
print(*A)
print(*tasks, sep="\n")
