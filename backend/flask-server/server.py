from flask import Flask, request, jsonify

from flask_cors import CORS

import sqlite3

app = Flask(__name__)
CORS(app)

conn = sqlite3.connect("resources/dns_store.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cache (
               domain TEXT PRIMARY KEY,
               ip TEXT NOT NULL
        )
    ''')
conn.commit()

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    domain = data["domain"]

@app.route('/cache')
def cache():
    ...

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)