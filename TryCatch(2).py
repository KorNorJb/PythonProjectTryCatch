
try:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Делитель равен нулю!")
print("Конец!")