import sys
import os

# Add backend/ to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
db_path = os.path.join(project_root, 'resources', 'dns_store.db')

from log.log import Log

from flask import Flask, request, jsonify

from flask_cors import CORS

import sqlite3
import logging
import time

# Silence Flask's request logs
_ = logging.getLogger('werkzeug')
_.setLevel(logging.ERROR)

# Silence the "development server" warning
import os
os.environ['FLASK_ENV'] = 'production'

app = Flask(__name__)
CORS(app)

log = Log(__name__)

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS store (
               domain TEXT PRIMARY KEY,
               ip TEXT NOT NULL,
               timestamp INT NOT NULL
        )
    ''')
conn.commit()
TTL = 86400

log.info("Created table \"store\"")

@app.route('/lookup')
def lookup():
    domain = request.args.get("domain")
    log.info(f"Received lookup request for {domain}")

    cursor.execute("SELECT ip, timestamp FROM store WHERE domain = ? LIMIT 1", (domain,))
    result = cursor.fetchone()

    if result:
        ip, timestamp = result
        age = int(time.time()) - timestamp
        
        if age < TTL:
            log.info(f"Cache hit for {domain}: {ip} (age: {age}s)")
            return jsonify({"ip": ip})
        else:
            log.warning(f"Cache expired for {domain} (age: {age}s)")
            return jsonify({"ip": None})
    else:
        log.warning(f"No result for {domain} was found in store")
        return jsonify({"ip": None})

@app.route('/store')
def store():
    domain = request.args.get("domain")
    ip = request.args.get("ip")
    
    log.info(f"Received request to store: ({domain}, {ip})")
    
    timestamp = int(time.time())
    cursor.execute("INSERT OR REPLACE INTO store (domain, ip, timestamp) VALUES (?, ?, ?)", 
                   (domain, ip, timestamp))
    conn.commit()
    
    log.info(f"Inserted into store: ({domain}, {ip})")
    return jsonify({"status": "success"})