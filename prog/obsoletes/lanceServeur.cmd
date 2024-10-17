@echo off
echo active l'environnement virtuel base pour python
echo.
IF "%HOMEPATH%" EQU "\Users\easy.DESKTOP-3IRAM0C" (
call c:\virPy13\Scripts\activate
) ELSE (
call D:\virPy13\Scripts\activate
)
python serveurweb.py
IF "%HOMEPATH%" EQU "\Users\easy.DESKTOP-3IRAM0C" (
call c:\virPy13\Scripts\deactivate
) ELSE (
call D:\virPy13\Scripts\deactivate
)
