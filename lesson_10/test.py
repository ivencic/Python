num = int(input("Введите целое число: "))

num_str = str(num)
num_digits = len(num_str)


sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)


if sum_of_digits == num:
    print(num, "является числом Армстронга.")
else:
    print(num, "не является числом Армстронга.")


