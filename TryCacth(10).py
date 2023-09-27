obj = {"1": "first", "2": "second", "3": "third"}
try:
  print(obj["5"])
except KeyError as e:
  print(f"Ключ не найден! {e}")
