try:
    text = open("Hi.txt")
    print("Чтение прошло успешно")
except FileNotFoundError:
    print("Что то пошло не так")