from string import digits


class Scanner:
    def __init__(self, S):
        self.tokens = []
        self.pos = 0

        for s in S:
            if s in ("x", "(", ")", "|", "^", "&", "="):
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

    def parse(self, digit, x_val):
        sc = self.sc

        def equation():
            expr = expression()
            sc.pop()
            return expr == (sc.pop() >> digit) & 1

        def expression():
            return or_term()

        def or_term():
            val = xor_term()

            while not sc.is_end() and sc.peek() == "|":
                sc.pop()
                val |= xor_term()

            return val

        def xor_term():
            val = and_term()

            while not sc.is_end() and sc.peek() == "^":
                sc.pop()
                val ^= and_term()

            return val

        def and_term():
            val = value()

            while not sc.is_end() and sc.peek() == "&":
                sc.pop()
                val &= value()

            return val

        def value():
            if sc.peek() == "x":
                sc.pop()
                return x_val

            elif type(sc.peek()) == int:
                return (sc.pop() >> digit) & 1

            elif sc.peek() == "(":
                sc.pop()
                expr_val = expression()
                sc.pop()
                return expr_val

            else:
                return

        result = equation()
        sc.reset()
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


T = int(input())

for _ in range(T):
    S = input()
    scanner = Scanner(S)
    solver = Solver(scanner)
    print(solver.solve())
