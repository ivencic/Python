# 1.
"""
Даны формулы: ¬((A ∨ B) ∧ (C ∨ D)) и ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)).
Используя закон Де Моргана, докажите, что эти формулы эквивалентны.
"""

"""

¬((A ∨ B) ∧ (C ∨ D)) по закону Де Моргана знаки меняются ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)),
 сравниваем с ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)): Одинаковые, значит формулы эквивалентны.

"""
# 2.
first_input = input('Введите первое логическое значение (True или False): ')
second_input = input('Введите второе логическое значение (True или False): ')

res1 = None
res2 = None

if first_input == 0:
    res1 = True
else:
    res1 = False
if second_input == 0:
    res2 = True
else:
    res2 = False

# and
if (res1 and res2) == 1:
    a = 'True'
else:
    a = 'False'

# or
if res1 and res2 == 0:
    b = 'False'
else:
    b = 'True'

# not
if first_input == 'True':
    c = 'False'
else:
    c = 'True'
if second_input == 'True':
    d = 'False'
else:
    d = 'True'

# ==
if first_input == second_input:
    e = 'True'
else:
    e = 'False'

# !=
if first_input != second_input:
   f = 'True'
else:
    f = 'False'

print('Результат логического И:', a)
print('Результат логического ИЛИ: ', b)
print('Результат логического НЕ (для первого значения):', c)
print('Результат логического НЕ (для второго значения): ', d)
print('Результат сравнения на равенство: ', e)
print('Результат сравнения на неравенство: ', f)

















