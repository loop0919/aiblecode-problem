# 解答コードを書く
N = int(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


p = N

while True:
    if is_prime(p) and is_prime(p + 2):
        print(p, p + 2)
        break
    p += 1
