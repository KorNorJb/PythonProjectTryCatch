import sqlite3;
try:
    con = sqlite3.connect("")
    cursor = con.cursor()
    con.close()
    print("All Good")
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)