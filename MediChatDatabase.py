import sqlite3

def create_table():
    conn = sqlite3.connect('medical_chatbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS medical_data (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

create_table()