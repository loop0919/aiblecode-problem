from functools import lru_cache
from random import randint, shuffle


def solve(N, M, C):
    alice_cache = {}
    bob_cache = {}

    def alice(i, diff):
        if i >= N:
            return diff >= 0

        if (i, diff) in alice_cache:
            return alice_cache[(i, diff)]

        result = False
        cnt = 0
        for j in range(M):
            if i + j >= N:
                break

            cnt += 1 if C[i + j] == "o" else 0
            if bob(i + j + 1, diff + cnt) == False:
                result = True
                break

        alice_cache[(i, diff)] = result
        return result

    def bob(i, diff):
        if i >= N:
            return diff <= 0

        if (i, diff) in bob_cache:
            return bob_cache[(i, diff)]

        result = False
        cnt = 0
        for j in range(M):
            if i + j >= N:
                break

            cnt += 1 if C[i + j] == "o" else 0
            if alice(i + j + 1, diff - cnt) == False:
                result = True
                break

        bob_cache[(i, diff)] = result
        return result

    return "Alice" if alice(0, 0) else "Bob"


if __name__ == "__main__":
    T = 100
    print(T)
    problems = []

    for _ in range(100):
        win = ("Alice", "Bob")[randint(0, 1)]
        while True:
            N = randint(1, 100)
            M = randint(1, N)
            bit = 0
            while bit.bit_count() % 2 == 0:
                bit = randint(1, (1 << N) - 1)

            if (
                solve(N, M, "".join(["o" if (bit >> i) & 1 else "-" for i in range(N)]))
                == win
            ):
                problems.append(
                    (N, M, "".join(["o" if (bit >> i) & 1 else "-" for i in range(N)]))
                )
                break

    for N, M, C in problems[:100]:
        print(N, M)
        print(C)
