import sqlite3
conn = sqlite3.connect('school.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT
    )
''')
cursor.execute("INSERT INTO students_list (name, age, grade) VALUES (?,?,? )",  ("Alice", 15, "10th"))
cursor.execute("INSERT INTO students_list (name, age, grade) VALUES (?,?,? )", ("Abin", 16, "11th"))

cursor.execute("INSERT INTO teachers_list (name, subject) VALUES (?,?)", ("Mr. John", "Math"))
cursor.execute("INSERT INTO teachers_list (name, subject) VALUES (?,?)", ("Ms. Luna", "English"))

cursor.execute("UPDATE students_list SET grade = '13th' WHERE name = 'Alice'")

cursor.execute("UPDATE teachers_list SET subject = 'Science' WHERE name = 'Luna'")

print("Data before deletion:")
cursor.execute("SELECT * FROM students_list")
print(cursor.fetchall())

cursor.execute("DELETE FROM students_list WHERE name = 'Abin'")

print("Data after deletion:")
cursor.execute("SELECT * FROM students_list")
print(cursor.fetchall())
conn.commit()
conn.close()