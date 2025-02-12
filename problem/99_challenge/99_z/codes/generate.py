# テストケースの生成コードを書く
from string import digits
from random import randint

import sys

sys.setrecursionlimit(10**5)


class Scanner:
    def __init__(self, S):
        self.tokens = []
        self.pos = 0

        for s in S:
            if s in ("x", "(", ")", "&", "^", "|", "="):
                self.tokens.append(s)
            elif s in digits:
                if self.tokens and isinstance(self.tokens[-1], int):
                    self.tokens[-1] = 10 * self.tokens[-1] + int(s)
                else:
                    self.tokens.append(int(s))
            else:
                raise TypeError

    def peek(self):
        return self.tokens[self.pos]

    def pop(self):
        val = self.tokens[self.pos]
        self.pos += 1
        return val

    def is_end(self):
        return self.pos >= len(self.tokens)

    def reset(self):
        self.pos = 0


class Solver:
    def __init__(self, scanner):
        self.sc = scanner

    def parse(self, x_val):
        sc = self.sc

        def expression():
            expr_val = xor_term()

            while not sc.is_end():
                if sc.peek() == "|":
                    sc.pop()
                    term_val = xor_term()
                    expr_val |= term_val
                else:
                    break

            return expr_val

        def xor_term():
            val = term()

            while not sc.is_end():
                if sc.peek() == "^":
                    sc.pop()
                    val ^= term()
                else:
                    break
            return val

        def term():
            term_val = value()

            while not sc.is_end():
                if sc.peek() == "&":
                    sc.pop()
                    value_val = value()
                    term_val &= value_val
                else:
                    break

            return term_val

        def value():
            if sc.peek() == "x":
                sc.pop()
                return x_val
            elif type(sc.peek()) == int:
                return sc.pop()
            elif sc.peek() == "(":
                sc.pop()
                expr_val = expression()
                sc.pop()
                return expr_val
            else:
                return

        result = expression()
        sc.reset()
        return result


class Generator:
    def __init__(self):
        pass

    def generate(self, x_val):
        def equation():
            expr = expression()

            # ans = Solver(Scanner(expr)).parse(x_val)
            ans = randint(0, 2**30 - 1)
            assert len(f"{expr}={ans}") <= 2000
            return f"{expr}={ans}"

        def expression():
            expr_val = xor_term()

            while randint(0, 100) <= 40 and len(expr_val) < 400:
                expr_val = f"{expr_val}|{xor_term()}"
            return expr_val

        def xor_term():
            val = term()

            while randint(0, 100) <= 40 and len(val) < 400:
                val = f"{val}^{term()}"
            return val

        def term():
            term_val = value()

            while randint(0, 100) <= 40 and len(term_val) < 400:
                term_val = f"{term_val}&{value()}"

            return term_val

        def value():
            if (r := randint(0, 100)) <= 40:
                return "x"
            elif r <= 80:
                return str(randint(0, 2**30 - 1))
            else:
                return "(" + expression() + ")"

        result = equation()
        return result

    def solve(self):
        ans = 0
        for i in range(30, -1, -1):
            if self.parse(i, 0):
                pass
            elif self.parse(i, 1):
                ans |= 1 << i
            else:
                return -1

        return ans


T = randint(1, 2)
print(T)
for _ in range(T):
    print(Generator().generate(randint(0, 2**30 - 1)))
