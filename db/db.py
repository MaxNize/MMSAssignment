import sqlite3

def initing():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
userName TEXT PRIMARY KEY,
firstName TEXT,
lastName TEXT,
mail TEXT,
pw TEXT,
folders TEXT,
inbox TEXT,
outbox TEXT,
trash TEXT);
              ''')
    c.execute('''CREATE TABLE IF NOT EXISTS mails (
id INTEGER PRIMARY KEY AUTOINCREMENT,
topic TEXT,
"to" TEXT,
sender TEXT,
bcc TEXT,
cc TEXT,
content TEXT,
attachmentsPath TEXT,
folder TEXT);
              ''')
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
name TEXT,
firstName TEXT,
lastName TEXT,
mail TEXT,
userName Text,
FOREIGN KEY (userName) REFERENCES users(userName));
              ''')

    conn.commit()
    conn.close()