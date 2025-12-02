import csv
import sqlite3 as sql
import time

print("Starting...")
Main = {}
i = 0

DB = sql.connect("The_Messier_Dualis_Database.db")
Cursor = DB.cursor()

csvfile = open("Database_Messier_Descriptions.csv", "r")
reader = csv.reader(csvfile)
headers = next(reader)
values = next(reader)
Main = dict(zip(headers, values))
time.sleep(1)

for data in Main:
    i = i + 1
    Value = Main[data]

    addcommand = "UPDATE The_Messier_Objects_Catalogue SET Description = ? WHERE Messier_Number = ?;"
    Cursor.execute(addcommand, (Value, f"M{i}"))
    print(f"Messier {i} Description has been Added!")
    time.sleep(0.2)
    
time.sleep(1)
DB.commit()
DB.close()
csvfile.close()
print("All the Database Values have been Updated! We have a go for Liftoff!!")
time.sleep(1)
print("Exiting...")
time.sleep(0.5)
exit()