import sqlite3 as sq
from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

db = sq.connect('mydatabase_gr.db')
cur = db.cursor()

async def create_table():
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                groups TEXT,
                num_groups INTEGER,
                pod_groups INTEGER,
                user_id INTEGER
            )
        """)
        db.commit()
        return True
    except sq.Error as e:
        print(f"Ошибка при создании таблицы: {e}")
        return False

