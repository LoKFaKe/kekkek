from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Функция для получения расписания (как в оригинальном боте)
def get_schedule(group_name):
    conn = sqlite3.connect('schedule.db')
    cursor = conn.cursor()
    cursor.execute("SELECT subject, day, time FROM schedule WHERE group_name = ?", (group_name,))
    results = cursor.fetchall()
    conn.close()
    return results

# Функция для получения FAQ (как в оригинальном боте)
def get_faq():
    conn = sqlite3.connect('schedule.db')
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM faq")
    results = cursor.fetchall()
    conn.close()
    return results

# Главная страница (аналог команды /start)
@app.route('/')
def home():
    return render_template('index.html')

# Обработка поиска расписания (аналог текстового сообщения в боте)
@app.route('/schedule', methods=['POST'])
def schedule():
    group_name = request.form['group_name'].strip()
    schedule = get_schedule(group_name)
    
    if schedule:
        response = []
        for subject, day, time in schedule:
            response.append(f"{day} - {subject} в {time}")
        return render_template('schedule.html', group_name=group_name, schedule=response)
    else:
        return render_template('not_found.html', group_name=group_name)

# Страница FAQ (аналог команды /faq)
@app.route('/faq')
def faq():
    faq_items = get_faq()
    return render_template('faq.html', faq_items=faq_items)

if __name__ == '__main__':
    app.run(debug=True)