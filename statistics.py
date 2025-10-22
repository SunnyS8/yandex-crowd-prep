import pandas as pd
import matplotlib.pyplot as plt

# === Исходные данные ===
data = {
    'task_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'user_id': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'C'],
    'status': ['done', 'done', 'error', 'in_progress', 'done', 'done', 'error', 'done', 'in_progress', 'done'],
    'time_spent': [30, 45, 20, 60, 50, 40, 25, 35, 55, 65]
}


# === Функции анализа ===
def compute_stats(df: pd.DataFrame) -> dict:
    total_tasks = len(df)

    expected_statuses = ['done', 'in_progress', 'error']
    status_counts = df['status'].value_counts().reindex(expected_statuses, fill_value=0)
    status_percent = (status_counts / total_tasks * 100).round(2)

    avg_time_per_user = df.groupby('user_id')['time_spent'].mean().round(2)
    avg_time_done_per_user = df[df['status'] == 'done'].groupby('user_id')['time_spent'].mean().round(2)
    total_time_per_user = df.groupby('user_id')['time_spent'].sum()

    user_with_max_total_time = total_time_per_user.idxmax()
    max_time = total_time_per_user.max()

    return {
        'status_counts': status_counts,
        'status_percent': status_percent,
        'avg_time_per_user': avg_time_per_user,
        'avg_time_done_per_user': avg_time_done_per_user,
        'total_time_per_user': total_time_per_user,
        'user_with_max_total_time': user_with_max_total_time,
        'max_time': max_time
    }


# === Главная функция ===
def main():
    df = pd.DataFrame(data)
    stats = compute_stats(df)

    print("Исполнитель с самым большим суммарным временем:",
          stats['user_with_max_total_time'], "–", stats['max_time'], "минут")

    # Таблицы
    status_table = pd.DataFrame({'Count': stats['status_counts'], 'Percent': stats['status_percent']})
    avg_all = stats['avg_time_per_user'].reset_index().rename(columns={'user_id': 'User', 'time_spent': 'Average Time (All)'})
    avg_done = stats['avg_time_done_per_user'].reset_index().rename(columns={'user_id': 'User', 'time_spent': 'Average Time (Done)'})
    total_per_user = stats['total_time_per_user'].reset_index().rename(columns={'user_id': 'User', 'time_spent': 'Total Time'})

    # === Сохранение таблиц ===
    status_table.to_csv('1_status_table.csv', index=True, encoding='utf-8-sig')
    avg_all.to_csv('2_avg_all.csv', index=False, encoding='utf-8-sig')
    avg_done.to_csv('3_avg_done.csv', index=False, encoding='utf-8-sig')
    total_per_user.to_csv('4_total_per_user.csv', index=False, encoding='utf-8-sig')

    print("Таблицы успешно сохранены.")

    # === Визуализация ===
    # 1. Гистограмма по статусам
    plt.figure(figsize=(6, 4))
    stats['status_counts'].plot(kind='bar', color=['#4caf50', '#ff9800', '#f44336'])
    plt.title('Количество задач по статусу')
    plt.xlabel('Статус')
    plt.ylabel('Количество')
    plt.tight_layout()
    plt.savefig('status_distribution.png')
    plt.close()

    # 2. Среднее время по пользователям
    plt.figure(figsize=(6, 4))
    stats['avg_time_per_user'].plot(kind='bar', color='#2196f3')
    plt.title('Среднее время выполнения по пользователям')
    plt.xlabel('Пользователь')
    plt.ylabel('Среднее время, мин')
    plt.tight_layout()
    plt.savefig('avg_time_per_user.png')
    plt.close()

    # 3. Круговая диаграмма статусов
    plt.figure(figsize=(5, 5))
    stats['status_counts'].plot(kind='pie', autopct='%1.1f%%', colors=['#4caf50', '#ff9800', '#f44336'])
    plt.title('Структура задач по статусу')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('status_pie.png')
    plt.close()

    print("Графики сохранены: status_distribution.png, avg_time_per_user.png, status_pie.png")


if __name__ == "__main__":
    main()
