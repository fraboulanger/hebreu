@echo off
echo ****************************************
echo **   Creation du site pour Francis    **
echo ********************************* V.5 **
echo .
echo Pour fonctionner, cela necessite le langague python
echo           et les bibliotheques : beautifulsoup4, html5lib, bottle, hjson( en standard : csv, argparse, html, io ,os )
echo .
set ServeurLocal=OK
rem les variables de chez guy et de chez francis
IF "%HOMEPATH%" EQU "\Users\easy.DESKTOP-3IRAM0C" (
set racine=D:\hebreu
) ELSE (
set racine=D:\hebreu
)
set site=hebreu
set version=3.2
rem goto :serveurlocal
echo.
echo ****************************************
echo **      Efface les dossiers           **
echo ****************************************
echo.
if exist %racine%\html rmdir /S /Q %racine%\html
rem if exist %racine%\hebreu rmdir /S /Q %racine%\hebreu
if exist %racine%\mef rmdir /S /Q %racine%\mef
rem goto :sautecredos
rem pause
echo.
echo ****************************************
echo **        Cree les dossiers           **
echo ****************************************
echo.
if not exist %racine%\html (mkdir %racine%\html)
if not exist %racine%\html\TDM (mkdir %racine%\html\TDM)
if not exist %racine%\mef (mkdir %racine%\mef)
echo fin Cree les dossiers
:sautecredos
echo.
echo ****************************************
echo ** Ouvre environnement virtuel python **
echo ****************************************
echo.
IF "%HOMEPATH%" EQU "\Users\easy.DESKTOP-3IRAM0C" (
call c:\virPy13\Scripts\activate
) ELSE (
call D:\virPy13\Scripts\activate
)
echo fin Ouvre environnement virtuel python
rem pause
echo.
echo ****************************************
echo **    Recopie les fichiers de aCopier **
echo ****************************************
echo.
IF "%HOMEPATH%" EQU "\Users\easy.DESKTOP-3IRAM0C" (
python acopier.py --site %site%
) ELSE (
python acopier.py --site %site%
)
echo fin de copie des fichiers initiaux

echo.
echo ****************************************
echo **      Creation du fichier JSON      **
echo ****************************************
echo.
cd %racine%\prog
rem goto :eof
python creejson.py --root=..\ --documents=Documents --output=complements\struct.json --ancien=complements\corrections.json
echo fin Cree la version %version%
rem pause
echo.
echo ****************************************
echo **   Cree la version %version%           **
echo ****************************************
echo.
cd %racine%\prog
rem goto :eof
python genereSiteFrancis.py --version=%version%
echo fin Cree la version %version%
rem pause
echo.
echo ****************************************
echo **     Retouche les fichiers html     **
echo ****************************************
echo.
python mefHTML.py
echo fin retouche les fichiers html
rem pause
echo.
echo ****************************************
echo **     Cree la table des matieres     **
echo ****************************************
echo.
rem goto :eof
rem goto :sautetdm
python genereTDM.py --site=%site%
echo fin Cree la table des matieres 
rem pause
:sautetdm
echo.
echo ****************************************
echo **     Efface le dossier temporaire   **
echo ****************************************
echo.
del /Q /S ..\TeteQueue >NUL
rd  ..\TeteQueue
echo fin Efface TeteQueue 
rem pause
IF "%ServeurLocal%" EQU "OK" (
echo.
echo ****************************************
echo **     Lance le serveur web local     **
echo ****************************************
echo.
python serveurweb.py
echo fin lance le serveur web local 
goto :eof
)
echo.
echo ****************************************
echo ** Ferme environnement virtuel python **
echo ****************************************
echo.
call D:\virPy13\Scripts\deactivate
echo "*** C'est tout pour aujourd'hui ! ***"
:eof