import math
a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
def NOD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print("НОД:", a)
    return a
t = NOD(a, b)
def NOK(a, b):
    a = a * b // t
    print("НОК:", a)
NOK(a, b)
