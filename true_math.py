'''
В true_math создайте функцию divide, которая принимает
 два параметра first и second. Функция должна возвращать
  результат деления first на second, но когда в second
   записан 0 - возвращать бесконечность.
'''


# Если делим на 0, то возвращается inf (знак бесконечности)
from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second