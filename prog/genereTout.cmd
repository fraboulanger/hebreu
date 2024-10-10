@echo off
echo ****************************************
echo **   Creation du site pour Francis    **
echo ********************************* V.2 **
echo .
echo Pour fonctionner, cela necessite le langague python
echo           et les bibliotheques : beautifulsoup4, html5lib, bottle, hjson( en standard : csv, argparse, html, io ,os )
echo .
set versionsite=SiteGITHUB
rem les variables de chez guy et de chez francis
IF "%HOMEPATH%" EQU "\Users\easy.DESKTOP-3IRAM0C" (
set racine=C:\%versionsite%\hebreu3.1
) ELSE (
set racine=D:\Hebreu
)
set version=3.1
rem goto :serveurlocal
echo.
echo ****************************************
echo **      Efface les dossiers           **
echo ****************************************
echo.
if exist %racine%\html rmdir /S /Q %racine%\html
if exist %racine%\hebreu rmdir /S /Q %racine%\hebreu
if exist %racine%\mef rmdir /S /Q %racine%\mef
rem goto :sautecredos
echo.
echo ****************************************
echo **        Cree les dossiers           **
echo ****************************************
echo.
if not exist %racine%\html (mkdir %racine%\html)
if not exist %racine%\html\TDM (mkdir %racine%\html\TDM)
if not exist %racine%\html\mef (mkdir %racine%\html\mef)
echo fin Cree les dossiers
rem pause
:sautecredos
echo.
echo ****************************************
echo ** Ouvre environnement virtuel python **
echo ****************************************
echo.
IF "%HOMEPATH%" EQU "\Users\easy.DESKTOP-3IRAM0C" (
call D:\virPy11\Scripts\activate
) ELSE (
call D:\virPy13\Scripts\activate
)
echo fin Ouvre environnement virtuel python
pause
echo.
echo ***********************************************************************************************************
echo **      Recopie les fichier de aCopier en les modifiant si besoin avec le numero de version: %version%        **
echo ***********************************************************************************************************
echo.
python acopier.py --site=Hebreu
echo fin de copie des fichiers initiaux
rem pause
echo.
echo ****************************************
echo **         Cree la version %version%        **
echo ****************************************
echo.
echo off
cd %racine%\prog
rem goto :eof
python genereSiteFrancis.%version%%.py
rem ********************************************************************
echo pas de creation d'index
goto :sauteindex
echo fin Cree la version %version%
pause
echo.
echo ****************************************
echo **            Cree l'index            **
echo ****************************************
echo.
python genereIndex.py
echo fin Cree l'index
:sauteindex
rem pause
echo.
echo ****************************************
echo **     retouche les fichiers html     **
echo ****************************************
echo.
python mefHTML05.py
echo fin retouche les fichiers html
rem pause
echo.
echo ****************************************
echo **     Cree la table des matieres     **
echo ****************************************
echo.
rem goto :eof
rem goto :sautetdm
python genereTDM.1.3.py
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
:serveurlocal
echo.
echo ****************************************
echo **     Lance le serveur web local     **
echo ****************************************
echo.
rem ##############################################################""
call lanceServeur.cmd
echo fin lance le serveur web local 
rem pause
call D:\virPy13\Scripts\deactivate
:eof