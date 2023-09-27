try:
    a = input("Введи: ")
    int(a)
    print("Готово!")
except ValueError:
    print("Что то пошло не так")