import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize('a,b,result', [
    (1, 2, 3),
    (2, 2, 4),
    ('hi', ' wuya', 'hi wuya')
])
def test_add(a, b, result):
    assert add(a, b) == result
