import math

expected = float(input())
answer = float(input())

assert math.isclose(
    expected, answer, rel_tol=1.01 * 10 ** (-3), abs_tol=1.01 * 10 ** (-3)
)

try:
    input()
    assert False
except EOFError:
    pass
