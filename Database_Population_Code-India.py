#This Program is attempting to read and add the data from a text file that has some of the Data for the Database taken from a Wikipedia page (https://en.wikipedia.org/wiki/List_of_discoverers_of_Messier_objects) [PS: The Wikipedia page's Latest edit was by me!! :D]

import sqlite3 as sql
import time

Messier_Discoveries = {}
i = 0

DB = sql.connect("The_Messier_Dualis_Database.db")
Cursor = DB.cursor()

txtfile = open("MessierObjects_Discoveries.txt", "r", encoding="utf-8")
for line in txtfile:
    parts = line.strip().split(" ")
    Messier_Num = parts[1]
    Messier_Number = f"M{Messier_Num}"
    Discoverer = " ".join(parts[2:-1])
    Disco_Year = int(parts[-1])
    Messier_Discoveries[Messier_Number] = (Discoverer, Disco_Year)
print(Messier_Discoveries)
time.sleep(5)

for i in range(1, 111):
    Discoverer, Disco_Year = Messier_Discoveries[f"M{i}"]
    Cursor.execute("UPDATE The_Messier_Objects_Catalogue SET Discovery_Date = ?, Discoverer = ? WHERE Messier_Number = ?;", (Disco_Year, Discoverer, f"M{i}"))
    print(f"Info for Messier {i} has been added!")
    time.sleep(0.4)

print("All the Info has been added to the Database!! :D")
time.sleep(1)
print("PS: This Data was taken from a Wikipedia page whose latest Edit if by me! :D")
time.sleep(1)
print("Anyways, Biee!")

DB.commit()
DB.close()
txtfile.close()
exit()