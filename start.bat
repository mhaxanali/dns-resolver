@echo off
start /B python backend\flask-server\server.py
cd backend\api && go run api.go