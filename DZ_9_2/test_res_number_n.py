from utils import res_number_n
import pytest

l_example = [(3, [1, 2, 6]), (4, [1, 2, 6, 24]), (5, [1, 2, 6, 24, 120])]


@pytest.mark.parametrize('number, expected_result', l_example)
def test_res_number_n(number, expected_result):
    assert res_number_n(number) == expected_result


# array ='5'  #TypeError: object of type 'int' has no len()
@pytest.mark.parametrize('expected_expeption, number', [(TypeError, '5')])
def test_type_error(expected_expeption, number):
    with pytest.raises(expected_expeption):
        assert res_number_n(number) == expected_expeption