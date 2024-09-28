import sqlite3
conn = sqlite3.connect('user_credentials.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("Rosh","anc"))
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("Jack", "njg"))
conn.commit()
conn.close()
def check_login(username, password):
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
if check_login(input_username, input_password):
    print("Login successful!")
else:
    print("Invalid username or password.")