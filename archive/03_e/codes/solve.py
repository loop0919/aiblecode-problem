from itertools import permutations


def solve():
    K = int(input())
    S = input()
    print(*sorted(set(permutations(S)))[K - 1], sep="")


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
