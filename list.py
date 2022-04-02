import sqlite3
import sys
import os

conn = sqlite3.connect('todo.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS todo(
    title TEXT
   )
""")
conn.commit()

def AddTask(title):
    cur.execute(f"INSERT INTO todo VALUES(?)", [title])
    conn.commit()
    print("Complited")

def SortTasks(arg_list):
    i = 0
    while i < len(arg_list):
        a = arg_list[i]
        print(a[0])
        i += 1

def RemoveTask(title):
    cur.execute(f"DELETE FROM todo WHERE title = ?", [title])
    conn.commit()
    print("DELETED")

os.system('cls||clear') # чистим консоль перед стартом цикла (убираем мусор)

while True:
    tasks = cur.execute("SELECT * FROM todo")
    tasks_res = cur.fetchall()

    SortTasks(tasks_res)
    print('========================================')
    print('q === exit')
    print('d === delete task')
    print('========================================')

    name = input('>>>')
    if name == 'q':
        sys.exit()
    elif name == 'd':
        SortTasks(tasks_res)
        delete_name = input('d>>')
        RemoveTask(delete_name)
    else:
        AddTask(name)

    os.system('cls||clear') # чистим консоль
