import sqlite3

def create_table():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('''
          CREATE TABLE IF NOT EXISTS EMPLOYEES (
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   role TEXT,
                   gender TEXT,
                   status TEXT)''')
    conn.commit()
    conn.close()

def fetch_employees():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM EMPLOYEES')
    employees = cursor.fetchall()  # Fixed the incorrect assignment to cursor.execute
    conn.close()
    return employees

def insert_employee(id, name, role, gender, status):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO EMPLOYEES (id, name, role, gender, status) VALUES (?, ?, ?, ?, ?)', (id, name, role, gender, status))
    conn.commit()
    conn.close()

def delete_employee(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM EMPLOYEES WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def update_employee(new_name, new_role, new_gender, new_status, id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE EMPLOYEES SET name = ?, role = ?, gender = ?, status = ? WHERE id = ?", (new_name, new_role, new_gender, new_status, id))  # Added missing id parameter in the placeholders
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM EMPLOYEES WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def search_employee(search_term):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPLOYEES WHERE id LIKE ? OR name LIKE ? OR role LIKE ? OR gender LIKE ? OR status LIKE ?", ('%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%'))
    employees = cursor.fetchall()
    conn.close()
    return employees



create_table()
