# Data Analysis Automation — Task Statistics

## Описание проекта

Этот проект представляет собой учебный кейс по работе с SQL и Python для анализа данных о выполнении задач пользователями краудсорсинговой платформы. Проект демонстрирует навыки работы с базами данных SQLite, обработки данных с помощью Python и создания визуализаций.

## Структура проекта

```
yandex-crowd-prep/
├── data.db                      # База данных SQLite с таблицами tasks и users
├── python.py                    # Основной скрипт для работы с БД
├── statistics.py                # Скрипт для генерации статистики и графиков
├── sql_practice.py              # Примеры SQL-запросов
├── 1_status_table.csv           # Результат: количество задач по статусам
├── 2_avg_all.csv                # Результат: среднее время на все задачи
├── 3_avg_done.csv               # Результат: среднее время на выполненные задачи
├── 4_total_per_user.csv         # Результат: количество задач на пользователя
├── users_table.csv              # Экспортированные данные пользователей
├── status_distribution.png      # График: распределение статусов
├── status_pie.png               # График: круговая диаграмма статусов
├── avg_time_per_user.png        # График: среднее время выполнения по пользователям
└── README.md                    # Документация проекта
```

## База данных

База данных `data.db` содержит две таблицы:

### Таблица `tasks`
- `task_id` (INTEGER) — уникальный идентификатор задачи
- `user_id` (INTEGER) — идентификатор пользователя
- `status` (TEXT) — статус задачи (done, canceled, processing)
- `time_spent` (INTEGER) — время выполнения в секундах

### Таблица `users`
- `user_id` (INTEGER) — уникальный идентификатор пользователя
- `username` (TEXT) — имя пользователя
- `email` (TEXT) — электронная почта
- `registration_date` (TEXT) — дата регистрации

## Выполненные задачи

### 1. SQL-запросы (`python.py`)

#### Запрос 1: Количество задач по статусам
```sql
SELECT status, COUNT(*) as count 
FROM tasks 
GROUP BY status;
```
Результат сохранён в `1_status_table.csv`

#### Запрос 2: Среднее время выполнения всех задач
```sql
SELECT AVG(time_spent) as avg_time 
FROM tasks;
```
Результат сохранён в `2_avg_all.csv`

#### Запрос 3: Среднее время выполнения завершённых задач
```sql
SELECT AVG(time_spent) as avg_time_done 
FROM tasks 
WHERE status = 'done';
```
Результат сохранён в `3_avg_done.csv`

#### Запрос 4: Количество задач на каждого пользователя
```sql
SELECT user_id, COUNT(*) as task_count 
FROM tasks 
GROUP BY user_id;
```
Результат сохранён в `4_total_per_user.csv`

### 2. Экспорт данных
Таблица `users` экспортирована в формат CSV (`users_table.csv`)

### 3. Визуализация данных (`statistics.py`)

Созданы графики с использованием библиотеки `matplotlib`:

1. **status_distribution.png** — столбчатая диаграмма распределения задач по статусам
2. **status_pie.png** — круговая диаграмма процентного соотношения статусов
3. **avg_time_per_user.png** — график среднего времени выполнения задач по пользователям

## Требования

```
python >= 3.7
sqlite3 (встроен в Python)
matplotlib
pandas
```

## Установка зависимостей

```bash
pip install matplotlib pandas
```

## Запуск

### Выполнение SQL-запросов и экспорт данных
```bash
python python.py
```

### Генерация статистики и графиков
```bash
python statistics.py
```

### Практика SQL-запросов
```bash
python sql_practice.py
```

## Результаты

Все результаты сохраняются в CSV-файлы и PNG-изображения в корневой директории проекта.

## Автор

Учебный проект для демонстрации навыков работы с SQL, Python и анализом данных.

## Лицензия

MIT License