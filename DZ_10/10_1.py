# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# 1.1 (**) с помощью декоратора-логгера создать лог функции  (с замером
# времени выполнения функции)

import datetime
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Кеш функции при  n = {''.join(map(str, args))} составляет = ", end='')
        return func(*args, **kwargs)
    return wrapper


def cacher(func):
    cach = {}

    def wrapper(*args):
        key = ''.join(map(str, args))                           #
        if key not in cach:
            cach[key] = func(*args)
        print(cach)
        return cach[key]
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        res_time = finish - start
        log_msg += f'результат: {res}, время выполнения функции {res_time} \n'
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res
    return wrapper


@logger
@decorator
@cacher
def seq(n):
    res = []
    for i in range(n + 1):
        res.append((1 + i)**i)
    return res


def main():
    seq(3)
    seq(8)
    seq(1)
    seq(8)
    seq(3)
    seq(1)
    seq(2)


if __name__ == '__main__':
    main()