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
subject TEXT,
"to" TEXT,
sender TEXT,
bcc TEXT,
cc TEXT,
content TEXT,
attachmentsPath TEXT,
folder TEXT,
userName Text,
timestamp Text,
FOREIGN KEY (userName) REFERENCES users(userName));
              ''')
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
name TEXT,
firstName TEXT,
lastName TEXT,
mail TEXT,
userName Text,
phone Text,
FOREIGN KEY (userName) REFERENCES users(userName));
              ''')

    conn.commit()
    conn.close()

def setupDBForTesting():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    c.execute('DELETE FROM users')
    c.execute('DELETE FROM mails')
    c.execute('DELETE FROM contacts')

    conn.commit()
    conn.close()

    setUsers([{"userName": "MMM", "firstName": "MMM","lastName": "MMM", "mail": "MMM@M.M", "pw": "123", "folders": "Inbox,Sent,Trash", "inbox": "Inbox","outbox":"Sent", "trash": "Trash"},{"userName": "M", "firstName": "M","lastName": "M", "mail": "M@M.M", "pw": "123", "folders": "Inbox,Sent,Trash", "inbox": "Inbox","outbox":"Sent", "trash": "Trash"}])   
    setMails([{"subject": "test", "to": "m@m.m", "sender": "m@m.m", "bcc": "m@m.m", "cc": "m@m.m", "content": "test", "attachmentsPath": "test", "folder": "Sent", "userName": "m"}])

#db.setUsers([{"userName": "MMM", "firstName": "MMM","lastName": "MMM", "mail": "MMM@M.M", "pw": "123", "folders": "Inbox,Sent,Trash", "inbox": "Inbox","outbox":"Sent", "trash": "Trash"},{"userName": "M", "firstName": "M","lastName": "M", "mail": "M@M.M", "pw": "123", "folders": "Inbox,Sent,Trash", "inbox": "Inbox","outbox":"Sent", "trash": "Trash"}])       
def getUsers():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users')
    users = c.fetchall()

    conn.close()
    return users

def setUsers(data):
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    # Prepare the SQL INSERT statement
    sql = '''
    INSERT INTO users (userName, firstName, lastName, mail, pw, folders, inbox, outbox, trash)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # Prepare data as a list of tuples
    values = [
        (
            mail["userName"],
            mail["firstName"],
            mail["lastName"],
            mail["mail"],
            mail["pw"],
            mail["folders"],
            mail["inbox"],
            mail["outbox"],
            mail["trash"]
        )
        for mail in data
    ]

    # Use executemany to insert all records
    c.executemany(sql, values)

    conn.commit()
    conn.close()

def deleteUsers():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    c.execute('DELETE FROM users')

    conn.commit()
    conn.close()

#db.setMails([{"subject": "test", "to": "m@m.m", "sender": "m@m.m", "bcc": "m@m.m", "cc": "m@m.m", "content": "test", "attachmentsPath": "test", "folder": "Sent", "userName": "m"}])
def getMails():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM mails')
    mails = c.fetchall()

    conn.close()
    return mails

def setMails(data):
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    # Prepare the SQL INSERT statement
    sql = '''
    INSERT INTO mails (subject, "to", sender, bcc, cc, content, attachmentsPath, folder, userName)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # Prepare data as a list of tuples
    values = [
        (
            mail["subject"],
            mail["to"],
            mail["sender"],
            mail["bcc"],
            mail["cc"],
            mail["content"],
            mail["attachmentsPath"],
            mail["folder"],
            mail["userName"]
        )
        for mail in data
    ]

    # Use executemany to insert all records
    c.executemany(sql, values)

    conn.commit()
    conn.close()

def deleteMails():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    c.execute('DELETE FROM mails')

    conn.commit()
    conn.close()

def getContacts():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM contacts')
    contacts = c.fetchall()

    conn.close()
    return contacts

def setContacts(data):
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    # Prepare the SQL INSERT statement
    sql = '''
    INSERT INTO contacts (name, firstName, lastName, mail, userName)
    VALUES (?, ?, ?, ?, ?)
    '''

    # Prepare data as a list of tuples
    values = [
        (
            contact["name"],
            contact["firstName"],
            contact["lastName"],
            contact["mail"],
            contact["userName"]
        )
        for contact in data
    ]

    # Use executemany to insert all records
    c.executemany(sql, values)

    conn.commit()
    conn.close()

def deleteContacts():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    c.execute('DELETE FROM contacts')

    conn.commit()
    conn.close()