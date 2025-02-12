@echo off
:: Obtém o diretório do arquivo .bat
set BAT_DIR=%~dp0

:: Caminho dinâmico para o script main.py
set SCRIPT_PATH=%USERPROFILE%\Desktop\procon\main.py

:: Inicia o script main.py com Python
python "%SCRIPT_PATH%"

pause
