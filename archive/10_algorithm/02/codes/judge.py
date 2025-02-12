import math

expected_answer = float(input())
actual_answer = float(input())

assert math.isclose(
    expected_answer, actual_answer, rel_tol=5.01 * 10 ** (-2), abs_tol=5.01 * 10 ** (-2)
)

try:
    input()
    assert False
except EOFError:
    pass
