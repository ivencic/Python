"""
    2. Напишите программу, которая принимает список чисел от пользователя и
    использует функцию reduce из модуля functools, чтобы найти произведение всех чисел в списке.
    Затем программа должна использовать функцию itertools.accumulate для накопления произведений чисел в новом списке.
    В результате программа должна вывести список, содержащий накопленные произведения.
"""

from functools import reduce
from itertools import accumulate
import operator

nums = [int(x) for x in input("Введите список чисел:").split()]

res_reduce = reduce(lambda x, y: x * y, nums)

print("Result of reduce numbers is: ", res_reduce)

res_accum = accumulate(nums, operator.mul)

print("Result of accumulate is: ", list(res_accum))


