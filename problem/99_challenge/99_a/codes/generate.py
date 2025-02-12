from random import randint


def miller_rabin(num):
    """64bit整数の範囲内で高速に素数判定を行う"""
    assert 1 <= num < ((1 << 63) - 1)

    if num == 1:
        return False
    if num == 2:
        return True
    elif num % 2 == 0:
        return False

    d, s = num - 1, 0
    while d & 1 == 0:
        d >>= 1
        s += 1

    for test in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if test > num:
            break

        if pow(test, d, num) == 1:
            continue

        if any(pow(test, d * 2**i, num) == num - 1 for i in range(s)):
            continue

        return False

    return True


def gen_twin_prime(left, right):
    while True:
        p = randint(left, right)
        if miller_rabin(p) and miller_rabin(p + 2):
            return p


T = 100
problems = []

for _ in range(T):
    # if (r := randint(0, 100)) <= 30:
    #     p = gen_twin_prime(1, 10**9 - 1)
    #     print(p * (p + 2))
    # elif r <= 50:
    #     p = gen_twin_prime(1, 10**9 - 1)
    #     q = gen_twin_prime(1, 10**9 - 1)
    #     print(p * q)
    # elif r <= 70:
    #     x = randint(1, 10**9 - 2)
    #     print(x * (x + 2))
    # else:
    #     print(randint(1, 10**18))
    p = gen_twin_prime(5 * 10**8, 10**9 - 1)
    problems.append(p * (p + 2))

print(len(problems))
print(*problems, sep="\n")

# for i in range(T):
#     print(i + 1)
