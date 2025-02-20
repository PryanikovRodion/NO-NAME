@echo off
REM Переходим в папку со скриптами
cd /d "%~dp0"

REM Активируем виртуальное окружение
call VENV\Scripts\activate

REM Запускаем Python-скрипт
call VENV\Scripts\python.exe "%~dp0\main.py"

REM Деактивируем виртуальное окружение
call VENV\Scripts\deactivate

pause