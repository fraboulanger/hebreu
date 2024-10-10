@echo off
echo active l'environnement virtuel base pour python
echo.
call C:\virpy11\Scripts\activate.bat
python serveurweb.py 
call C:\virpy11\Scripts\deactivate.bat
rem