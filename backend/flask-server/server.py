from log import Log

from flask import Flask, request, jsonify

from flask_cors import CORS

import sqlite3

app = Flask(__name__)
CORS(app)

log = Log(__name__)

conn = sqlite3.connect("resources/dns_store.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS store (
               domain TEXT PRIMARY KEY,
               ip TEXT NOT NULL
        )
    ''')
conn.commit()

log.info("Created table \"store\"")

@app.route('/lookup')
def lookup():
    domain = request.args.get("domain")
    log.info(f"Received lookup request for {domain}")

    cursor.execute("SELECT ip FROM store WHERE domain = ? LIMIT 1", (domain,))
    result = cursor.fetchone()

    if result:
        ip = result[0]
        log.info(f"Result for {domain} was found in store: {ip}")
    else:
        ip = None
        log.warning(f"No result for {domain} was found in store")

    return jsonify({"ip": ip})

@app.route('/store')
def store():
    domain = request.args.get("domain")
    ip = request.args.get("ip")

    log.info(f"Received request to store: ({domain}, {ip})")

    cursor.execute("INSERT INTO store (domain, ip) VALUES (?, ?)", (domain, ip))
    conn.commit()

    log.info(f"Inserted into store: ({domain}, {ip})")

    return jsonify({"status":"success"})

if __name__ == '__main__':
    log.info("Service started.")
    app.run(host="0.0.0.0", port=5050, debug=False)