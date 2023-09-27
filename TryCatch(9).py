try:
    file = open("txt.txt", "w")
    file.write("Пытаюсь что то записать")
except PermissionError as e:
  print(f"Нету прав на запись данного файла! {e}")
