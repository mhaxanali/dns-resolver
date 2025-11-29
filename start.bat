@echo off
call backend\venv\Scripts\activate.bat
start /B python backend\flask-server\server.py
backend\api\api.exe