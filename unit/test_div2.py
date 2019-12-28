import pytest
import allure

int_data = [(3, 1, 3), (0, 100, 0), (100000000000000, 1, 100000000000000), (-8, 4, -2), (-9, -3, 3)]
float_data = [(10, 3, 3.3333333), (3.33333, 3.33333, 1), (1000000000000.0, 3, 333333333333.3333333), (-4.0, 2, -2.0),
              (-17.0, -7, 2.4285714)]
err_data = [(2, 0, ZeroDivisionError), (10, "a", TypeError), ("a", 9, TypeError), (None, None, TypeError)]


def div(a, b):
    return a / b


@pytest.mark.welldone
@allure.title("welldone int")
@pytest.mark.parametrize("first_para, second_para, expected", int_data)
def test_div_int(first_para, second_para, expected):
    assert div(first_para, second_para) == expected


@allure.title("test_method11")
@pytest.mark.test_method
@pytest.mark.parametrize("a,b,result", [(1, 2, 0.5), (1, 1, 1)])
def test_method(a, b, result):
    assert div(a, b) == result


@pytest.mark.goodjob
@allure.title("goodjob float")
@pytest.mark.parametrize("first_para, second_para, expected", float_data)
def test_div_float(first_para, second_para, expected):
    assert abs(div(first_para, second_para) - expected) <= 0.0000001


@pytest.mark.exception
@allure.title("expected exception")
@pytest.mark.parametrize("first_para, second_para, expected", err_data)
def test_div_error(first_para, second_para, expected):
    with pytest.raises(Exception) as exc_info:
        div(first_para, second_para)
    assert exc_info.type == expected


if __name__ == '__main__':
    pytest.main('--alluredir=unit/allure_results', 'unit/')
