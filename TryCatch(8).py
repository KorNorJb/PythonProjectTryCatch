from datetime import datetime
try:
    txt = str(input("dfdfdf"))
    dttxt = datetime.strptime(txt, "%Y-%m-%d")
    print(dttxt)
except ValueError:
     print("УХХХХХХХ")