a = ""
b = 0
c = []
d = []

def a1(x):
    z = []
    x = x.lstrip(" ")
    x = x.rstrip(" ")
    y = x.split(' ')
    for i in y:
        z.append(float(i))
    return z

def a2(xx):
    for i in range(len(xx)):
        for j in range(len(xx) - i - 1):
            if xx[j] > xx[j + 1]:
                xx[j], xx[j + 1] = xx[j + 1], xx[j]
    return xx

def a3(xxx, yyy):
    i = 0
    j = len(xxx) - 1
    if xxx[i] < yyy < xxx[j]:
        while i < j:
            m = int((i + j) / 2)
            if yyy > xxx[m]:
                i = m + 1
            else:
                j = m
        if xxx[j] == yyy:
            return "Номер позиции элемента, который меньше введенного числа: " + str(j)
        else:
            return "Номер позиции элемента, который меньше введенного числа: " + str(i)
    elif yyy > xxx[j]:
        return "Введеное число больше любого из чисел в введенной последовательности"
    elif yyy < xxx[i]:
        return "Введеное число меньше любого из чисел в введенной последовательности"
    elif yyy == xxx[i]:
        return "Введеное число равно наименьшему числу в введенной последовательности"
    elif yyy == xxx[j]:
        return "Введеное число равно наибольшему числу в введенной последовательности"


a = input("Введите последовательность чисел через пробел: ")
b = float(input("Введите любое число: "))
c = a1(a)
c = a2(c)
#print("Отсортировоный список: ", c)
print(a3(c, b))