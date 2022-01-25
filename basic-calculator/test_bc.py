
class BaseToken:
    def __init__(self):
        pass


class EOFToken(BaseToken):
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, EOFToken)


class AnyIntToken(BaseToken):
    def __init__(self):
        pass

    def __str__(self):
        return 'AnyIntToken'

    def __eq__(self, other):
        return isinstance(other, IntToken)


class IntToken(BaseToken):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, IntToken) and self.value == other.value


class OpToken(BaseToken):
    def __init__(self, op):
        self.op = op

    def __str__(self):
        return self.op

    def __eq__(self, other):
        return isinstance(other, OpToken) and self.op == other.op


class Lexer:
    def __init__(self, s):
        self.tokens = Lexer.gen_tokens(s)
        self.last_token = None
        self.current_token = None
        self.next()

    @staticmethod
    def gen_tokens(s):
        ''
        i = 0
        while i < len(s):
            c = s[i]
            if c in '+-*/()':
                yield OpToken(c)
                i += 1
            elif c == ' ':
                i += 1
            else:
                num = 0
                while i < len(s) and (c := s[i]) in "0123456789":
                    num = 10*num + ord(c) - ord('0')
                    i += 1
                yield IntToken(num)

    def next(self):
        self.last_token = self.current_token
        self.current_token = next(self.tokens, EOFToken())

    def have(self, token):
        if token == self.current_token:
            self.next()
            return True
        else:
            return False


class Solution:
    def calculate(self, s: str) -> int:
        l = Lexer(s)

        def primary():
            if l.have(OpToken('(')):
                v = expression()
                assert l.have(OpToken(')'))
                return v
            elif l.have(OpToken('-')):
                return -primary()
            else:
                assert l.have(AnyIntToken())
                return l.last_token.value

        def term():
            v = primary()
            while True:
                if l.have(OpToken('*')):
                    v *= primary()
                elif l.have(OpToken('/')):
                    v //= primary()
                else:
                    break
            return v

        def expression():
            v = term()
            while True:
                if l.have(OpToken('+')):
                    v += term()
                elif l.have(OpToken('-')):
                    v -= term()
                else:
                    break
            return v

        v = expression()
        assert l.have(EOFToken())

        return v


def test_gen_tokens():
    assert list(Lexer.gen_tokens("3+2*2")) == [IntToken(3), OpToken('+'), IntToken(2), OpToken('*'), IntToken(2)]


def test_have():
    l = Lexer("3+2*2")
    assert l.have(IntToken(3))
    assert l.have(OpToken('+'))
    assert l.have(IntToken(2))
    assert l.have(OpToken('*'))
    assert l.have(IntToken(2))
    assert l.have(EOFToken())


def test_A0():
    assert Solution().calculate("3+2*2") == 7


def test_A1():
    assert Solution().calculate("3+2*(2+-3)") == 1
