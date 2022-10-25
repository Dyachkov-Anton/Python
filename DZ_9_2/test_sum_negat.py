from utils import summ_negativ_position
import pytest


l_example = [([2, 3, 5, 9, 3], 12),
             ([25, 3, 5, 9, 3, 6, 7, 8], 26),
             ([12, 3, 25, 9, 3, 55, 9, 4, 1], 71),
             ([20, 13, 55, 19, 0], 32)]


@pytest.mark.parametrize('array, expected_result', l_example)
def test_summ_negativ_position(array,expected_result):
    assert summ_negativ_position(array) == expected_result


# array =1  #TypeError: object of type 'int' has no len()
@pytest.mark.parametrize('expected_expeption, array', [(TypeError, 5)])
def test_type_int_error(expected_expeption, array):
    with pytest.raises(expected_expeption):
        assert summ_negativ_position(array) == expected_expeption


# array =['1','55','56','5']
# TypeError: unsupported operand type(s) for +=: 'int' and 'str'
@pytest.mark.parametrize('expected_expeption, array',
                         [(TypeError, ['1', '55', '56', '5'])])
def test_type_str_error(expected_expeption, array):
    with pytest.raises(expected_expeption):
        assert summ_negativ_position(array) == expected_expeption