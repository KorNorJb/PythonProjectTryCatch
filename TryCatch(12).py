SomeTuple = (1, 2, 3)
try:
  print(f"Значение: {SomeTuple[7]}")
except IndexError as e:
  print(f"Значение с таким индексом не существует {e}")
