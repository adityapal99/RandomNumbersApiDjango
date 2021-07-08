@echo off

start cmd.exe /C "pip install virtualenv && virtualenv venv && venv\Scripts\pip.exe install -r requirements.txt"
start cmd.exe /C "venv\Scripts\python.exe manage.py runserver"

