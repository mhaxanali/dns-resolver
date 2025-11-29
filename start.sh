#!/bin/bash

# Start Flask in background
cd backend/flask-server && python server.py &

# Start Go server in foreground
cd backend/api && go run api.go