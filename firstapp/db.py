# db.py

import mysql.connector as m  # type: ignore


def getconnection():
    mydatabase = m.connect(
        host="localhost", user="root", password="Gourav@2806", database="pythondb1"
    )
    return mydatabase
