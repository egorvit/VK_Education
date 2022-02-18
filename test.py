from my_func.main import func_return_dict, func_rounding

import pytest



#   Тест функции принимающей два аргумента и возвращающей словарь, где аргументы являются ключами,
#   а значением первого аргумената, является произведение двойки и самого аргумента, занчением второго,
#   частное первого и второго аргумента


@pytest.mark.parametrize("first, second, expected_result", [(2, 16, {2: 4, 16: 8}),
                                                            (3, 12, {3: 6, 12: 4})])
def test_return_dict(first, second, expected_result):
    assert func_return_dict(first, second) == expected_result


def test_type_error():
    with pytest.raises(TypeError):
        func_return_dict(4, '2')


def test_empty():
    assert len(func_return_dict(4, 2)) != 0




#   Тест функции округляющей число после деления ее оргументов

@pytest.mark.parametrize("first, second, expected_result", [(100, 74, 1),
                                                            (12, 7, 2)])

def test_rounding(first, second, expected_result):
    assert func_rounding(first, second) == expected_result


def test_zero():
    with pytest.raises(ZeroDivisionError):
        func_rounding(8, 0)