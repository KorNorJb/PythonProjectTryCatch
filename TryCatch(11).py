try:
    file = open("SomeText.txt", "r")
    inner = file.read()
    print(innner)
except FileNotFoundError as e:
  print(f"Такого файла не найдена : {e}")
