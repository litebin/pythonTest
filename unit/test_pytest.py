import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x


class TestClass:
    def setup(self):
        print("setup")

    @classmethod
    def setup_class(self):
        print("setup_class")

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")





#
# class TestDesimal:
#     def test_div(self):
#         a = div(2, 4)
#         assert a == 0.5
#
#     def test_mo_zero(self):
#         b = div(1, 0)
#         assert b == 0
#
#     def test_De_zero(self):
#         c = div(0, 1)
#         assert c == 0


