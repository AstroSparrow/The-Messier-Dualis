import sqlite3 as sql

def DBCon():
    DB = sql.connect("The_Messier_Dualis_Database.db")
    Cursor = DB.cursor()

    return Cursor