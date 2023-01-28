print("Введите a")
a = float(input())
print("Введите b")
b = float(input())
if (a == 0 and b == 0):
    print("Бесконечное количество решений")
if (a == 0 and b != 0):
    print("Решений нет")
if (a != 0):
    print(b/a)
