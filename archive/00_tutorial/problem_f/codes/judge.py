N = int(input())
A, B = map(int, input().split())

assert 0 <= A
assert 0 <= B
assert A + B == N

try:
    input()
    assert False
except EOFError:
    pass
