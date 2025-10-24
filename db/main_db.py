import sqlite3
from db import queries
from config import path_db

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASK)
    print("База данных подключена!")
    conn.commit()
    conn.close()


def add_spisok(spisoks):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_TASK, (spisoks, ))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return spisoks

def get_spisok():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_TASK)
    spisoks = cursor.fetchall()
    conn.close()
    return spisoks


def delete_spisok(spisok_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (spisok_id, ))
    conn.commit()
    conn.close()


def update_spisok(spisok_id, new_spisok):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK, (new_spisok, spisok_id))
    conn.commit()
    conn.close()