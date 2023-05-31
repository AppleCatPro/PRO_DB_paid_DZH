import os
import signal
import sqlite3
import sys
import threading

from flask import Flask, jsonify, request

app = Flask(__name__)

def run_server():
    app.run(debug=True)


def create_connection():
    conn = sqlite3.connect('db/home.db')
    return conn

def start_server():
    # Запуск сервера в отдельном потоке
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

@app.route('/')
def view_data():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM lr4")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


@app.route('/add/<name>/<x>/<y>')
def add_data(name, x, y):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO lr4 (name, coordinates) VALUES (?, ?)", (f'{name}', f'({x},{y})'))
    conn.commit()
    cur.close()
    conn.close()
    return f'Данные успешно созданы: "coordinates": ({x},{y}), "name": {name}'


@app.route('/del/<id>')
def del_data(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE from lr4 WHERE id = '{0}'".format(id))
    conn.commit()
    cur.close()
    conn.close()
    return f'Данные успешно удалены!'


@app.route('/update/<name>/<x>/<y>')
def update_data(name, x, y):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE lr4 SET coordinates = ? WHERE name = ?", (f'({x},{y})', f"{name}"))
    conn.commit()
    cur.close()
    conn.close()
    return f'Данные успешно изменены на "coordinates": ({x},{y}), "name": {name}'


@app.route('/locations')
def get_locations():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM lr4")
    fff = cur.fetchall()

    locations = []
    for location in fff:
        print(location)
        locations.append({'id': location[0], 'name': location[1], 'coordinates': location[2]})

    print(locations)

    return jsonify({'locations': locations})


@app.route('/locations/<city>')
def get_nearby_locations(city):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM lr4 WHERE name='{city}'""")
    fff = cur.fetchall()

    locations = []
    for location in fff:
        locations.append({'id': location[0], 'name': location[1], 'coordinates': location[2]})

    return jsonify({'locations': locations})


if __name__ == '__main__':
    run_server()