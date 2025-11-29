@echo off
cd ..\backend

rem Remove old venv and create new one
rmdir /s /q venv 2>nul
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt

rem Build Go executable
cd api
del api.exe 2>nul
go build -o api.exe api.go

cd ..\..
echo Build complete