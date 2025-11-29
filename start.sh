#!/bin/bash

source backend/venv/bin/activate
python backend/flask-server/server.py &
./backend/api/api