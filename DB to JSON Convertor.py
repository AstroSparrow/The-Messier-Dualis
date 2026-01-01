import sqlite3 as sql
import json

output_json = "Messier_Dualis_Datapoints.json"

db = sql.connect("The_Messier_Dualis_Database.db")
db.row_factory = sql.Row
cur = db.cursor()

cur.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table' AND name NOT LIKE 'sqlite_%';
""")
tables = [row["name"] for row in cur.fetchall()]

db_dict = {}

for table in tables:
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    db_dict[table] = [dict(row) for row in rows]

db.close()

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(db_dict, f, indent=2, ensure_ascii=False)

print("JSON ready!")