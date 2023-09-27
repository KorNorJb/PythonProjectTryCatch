try:
  a = float(input("Введите первое число: "))
  b = float(input("Введите второе число: "))
  if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    c = a/b
    print(f"Результат: {c}")
except ValueError as e:
  print(f"Ошибка: {e}")
