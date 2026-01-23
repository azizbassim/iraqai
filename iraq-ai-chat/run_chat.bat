@echo off
chcp 65001 >nul
cd /d "%~dp0"
python iraq_chatbot_app.py
pause