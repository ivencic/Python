# 1.
N = int(input("Введите число N: "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(i * j, end="\t")
    print("")


# 2.
l1 = input("Введите элементы первого списка, разделенные пробелом: ").split()
l2 = input("Введите элементы второго списка, разделенные пробелом: ").split()

res = list(zip(l1, l2))

print("Список пар элементов:", res)

