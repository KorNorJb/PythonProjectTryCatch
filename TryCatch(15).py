try:
    a = input("Введите что либо: ")
    с = float(a)
    print(f"Преобразование: {c}")
except ValueError as e:
    print(f"Ой что то пошло не так! : {e}")
