
#autopep8 ./ --recursive --in-place -a




def summ_negativ_position(array):

    index = len(array)  # index - ЕСТЬ ТАКАЯ ВСТРОЕННАЯ ФУНКЦИЯ
    result = 0
    for i in range(0, index):
        if i % 2 != 0:
            result += array[i]
    return result


def first_end_ellem(array):

    index = len(array)-1  # index - ЕСТЬ ТАКАЯ ВСТРОЕННАЯ ФУНКЦИЯ
    result = []
    # res = 1  # ЛИШНЯЯ СТРОКА т.к. за пределами цикла не используется
    inde = (index//2)+1
    for i in range(inde):
        res = array[i]*array[(i+1)*-1]
        result.append(res)
    return result


def res_number_n(num):
    res = 1
    multi = []
    for i in range(1, num+1):
        res *= i
        multi.append(res)
    return multi