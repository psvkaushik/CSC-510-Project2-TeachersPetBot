"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""
import sqlite3
from sqlite3 import Error
import os

CON = None
def connect():
    ''' connect program to database file db.sqlite '''
    global CON
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db.sqlite')
    print(db_path)
    try:
        CON = sqlite3.connect(db_path)
        print("Connection to SQLite DB successful")
    except Error as err:
        print(f"The error '{err}' occurred when trying to connect to SQLite database")


def select_query(sql, args=()):
    ''' select query to return items from database '''
    cur = CON.cursor()
    return cur.execute(sql, args)


def mutation_query(sql, args=()):
    ''' do a mutation on the database '''
    cur = CON.cursor()
    cur.execute(sql, args)
    CON.commit()
