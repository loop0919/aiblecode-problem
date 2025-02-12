def solve():
    N, M = map(int, input().split())
    C = list(input())

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

    print("Alice" if alice(0, 0) else "Bob")


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
