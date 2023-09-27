try:
    file = open("SomeFile.txt", "r")
    txt = file.read()
    print(f"Содержимое файла: \n{txt}")
except FileNotFoundError as e:
  print(f"К сожалению файл не существует {e}")
