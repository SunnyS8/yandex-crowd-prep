import sqlite3
import pandas as pd

# 1. создаем или открываем файл базы данных
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 2. создаем таблицу (если её ещё нет)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT
)
''')

# 3. добавляем данные только если таблица пустая
cursor.execute('SELECT COUNT(*) FROM users')
rows = cursor.fetchone()[0]
if rows == 0:
    cursor.executemany('INSERT INTO users (name, country) VALUES (?, ?)', [
        ('Alice', 'Russia'),
        ('Bob', 'USA'),
        ('Charlie', 'Germany'),
        ('Diana', 'Russia')
    ])
    conn.commit()
    print("✅ Данные добавлены")
else:
    print("ℹ️ Таблица уже заполнена, пропускаем вставку")

# 4. пишем SQL‑запрос
query = "SELECT * FROM users;"

# 5. выполняем запрос и показываем результат в виде таблицы
df = pd.read_sql_query(query, conn)
print("\nРезультат запроса:")
print(df.to_markdown(index=False))

# 6. закрываем соединение
conn.close()
df.to_csv("users_table.csv", index=False, encoding="utf-8-sig")
print("Таблица сохранена в файл users_table.csv")

