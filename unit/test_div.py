import pytest
import allure


def div(a, b):
    return a / b


# def test_div_int():
#     assert div(10, 2) == 5
#     assert div(10, 5) == 2
#     assert div(10000, 1) == 10000
#
#
# def test_div_float():
#     assert div(10, 3) == 3.3333333333333335
#     assert div(10.2, 0.2) == 50.99999999999999
#
#
# def test_div_exception():
#     assert div(10, 'a')
#     assert div('abc', 10)
#
#
# def test_div_zero():
#     with pytest.raises(ZeroDivisionError):
#         div(10,0)
err_data = [(2, 0, ZeroDivisionError), (10, "a", TypeError), ("a", 9, TypeError), (None, None, TypeError)]


@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,result", [
    (10, 2, 5),
    (10, 3, 3.3333333333333335),
    (-10, -2, 5),
    (-10, 5, -2),
    (100000000, 1, 100000000),
    (2, 20000, 0.0001),
    (66.72, 11.12, 6),
    (0, 200, 0)
])
def test_div(number1, number2, result):
    print("hello world")
    assert div(number1, number2) == result


@pytest.mark.exception
@allure.title("expected exception")
@pytest.mark.parametrize("first_para, second_para, expected", err_data)
def test_div_error(first_para, second_para, expected):
    with pytest.raises(Exception) as exc_info:
        div(first_para, second_para)
    assert exc_info.type == expected


if __name__ == '__main__':
    pytest.main('--alluredir=unit/allure_results', 'unit/')
