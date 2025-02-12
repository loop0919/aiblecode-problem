result = input()
N, K = map(int, input().split())
A = list(map(int, input().split()))
length = sum(len(str(a)) for a in A) + len(A) - 1

ans = input()
assert result == ans

if result == "No":
    exit()

S = input()
assert len(S) == length

exp = []
for s in S:
    if s in ("+", "-"):
        exp.append(s)
    elif s in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        if len(exp) == 0 or exp[-1] in ("+", "-"):
            exp.append(int(s))
        elif isinstance(exp[-1], int):
            exp[-1] = exp[-1] * 10 + int(s)
        else:
            assert False

op = "+"
val = 0

for i, x in enumerate(exp):
    if i % 2 == 0:
        x = int(x)
        assert A[i // 2] == x
        val += x * (1 if op == "+" else -1)

    else:
        if x in ("+", "-"):
            op = x
        else:
            assert False

assert val == K

try:
    input()
    assert False
except EOFError:
    pass
