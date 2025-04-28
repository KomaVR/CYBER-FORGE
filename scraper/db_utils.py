import sqlite3

DB_PATH = 'tools.db'

def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tools (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            description TEXT,
            url         TEXT    NOT NULL UNIQUE,
            category    TEXT    NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_tool(name, description, url, category):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute('''
            INSERT OR IGNORE INTO tools (name, description, url, category)
            VALUES (?, ?, ?, ?)
        ''', (name, description, url, category))
        conn.commit()
    finally:
        conn.close()
      
