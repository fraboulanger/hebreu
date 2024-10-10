@echo off
set ficresu="C:\SiteGITHUB\hebreu\complements\jstempo.json"
call :crejs 1 "Credo et Hymnes du N.T" "Credo et Hymnes du N.T."
call :crejs 2 "Guerir et Sauver dans les Evangiles" "Guérir et Sauver dans les Evangiles"
call :crejs 3 "Le 'Notre Pere' et sa traduction" "Le 'Notre Père' et sa traduction"
call :crejs 4 "La Transfiguration synopse Mt, Mc, Lc" "La Transfiguration : synopse Mt, Mc, Lc"
call :crejs 5 "Vocabulaire de la Redemption dans le N.T" "Vocabulaire de la Rédemption dans le N.T."
call :crejs 6 "Sujets en vrac" "Divers sujets en vrac"
call :crejs 1 "Formules liturgiques" "Formules liturgiques"
call :crejs 2 "Source = Evangiles en Grec (Mt 6 et Lc 11)" "Source = Evangiles en Grec (Mt 6 et Lc 11)"
call :crejs 3 "Source = Evangiles en langues orientales" "Source := Evangiles en langues orientales"
call :crejs 4 "Source = Evangiles en latin" "Source := Evangiles en latin"
call :crejs 5 "Traductions recentes" "Traductions récentes"
call :crejs 1 "l'herbe verte en Mc 6,39" "l'herbe verte en Mc 6,39"
call :crejs 2 "fruits bons et fruits pouris dans le N.T" "fruits bons et fruits pouris dans le N.T."
call :crejs 3 "au large' ou 'en eau profonde' Lc 5,1-11" "'au large' ou 'en eau profonde' ? Lc 5,1-11"
call :crejs 4 "splancnizomai = 'pris aux tripes' dans le N.T" "splancnizomai = 'pris aux tripes' dans le N.T. µ"
call :crejs 1 "Le N.P. liturgique en diverses langues" "Le N.P. liturgique en diverses langues"
call :crejs 2 "Le N.P. liturgique hebreu et semitique" "Le N.P. liturgique hebreu et semitique µ"
call :crejs 3 "Le N.P. liturgique neerlandais" "Le N.P. liturgique neerlandais µ"
call :crejs 4 "Le N.P. en arameen phonetique" "Le N.P. en arameen phonetique µ"
call :crejs 5 "Le Notre Pere liturgique. Evolution" "Le Notre Pere liturgique. Evolution"
call :crejs 1 "Synopse Grec STE = Etienne et Erasme 1546-1551" "Synopse Grec STE = Etienne et Erasme 1546-1551"
call :crejs 2 "Synopse Grec Elzevir Textus Receptus 1624" "Synopse Grec Elzevir Textus Receptus 1624"
call :crejs 3 "Synopse Crec SCR = Scrivener Textus Receptue 1894" "Synopse Crec SCR = Scrivener Textus Receptue 1894"
call :crejs 4 "Synopse Grec TRG = Tregelles 1857-1879-2009" "Synopse Grec TRG = Tregelles 1857-1879-2009"
call :crejs 5 "Synopse Grec TIS et WHT = Tischendorf et Westcott-Hort 1881-2010" "Synopse Grec TIS et WHT = Tischendorf et Westcott-Hort 1881-2010"
call :crejs 6 "Synopse Grec Nestle-Aland BNT, 27 edition, 1996-2010" "Synopse Grec Nestle-Aland BNT, 27 edition, 1996-2010 µ"
call :crejs 1 "Synopse Syriaque Peshitta en lettres hebraiques" "Synopse Syriaque Peshitta en lettres hebraiques µ"
call :crejs 2 "Synopse. Retroversion en Hebreu. Delitzsch 1923" "Synopse. Retroversion en Hebreu. Delitzsch 1923 µ"
call :crejs 3 "Synopse. Retroversion en Hebreu. Salkinson 1999" "Synopse. Retroversion en Hebreu. Salkinson 1999 µ"
call :crejs 1 "1546.Synopse Vulgate Biblia de Robert Estienne" "1546.Synopse Vulgate Biblia de Robert Estienne"
call :crejs 2 "1861.Synopse Vulgate Clementine" "1861.Synopse Vulgate Clementine"
call :crejs 3 "1979.Synopse Vulgate Nova Vulgata" "1979.Synopse Vulgate Nova Vulgata"
call :crejs 4 "1994.Synopse Vulgate de Stuttgart" "1994.Synopse Vulgate de Stuttgart"
call :crejs 1 "traduction Osty 1973" "traduction Osty 1973"
call :crejs 2 "traduction litterale de Sr J.d'Arc 1986-87" "traduction litterale de Sr J.d'Arc 1986-87 µ"
call :crejs 3 "traduction Bible de Jerusalem 1998" "traduction Bible de Jerusalem 1998 µ"
call :crejs 4 "traduction Bible Bayard.Nouvelle trad 2001" "traduction Bible Bayard.Nouvelle trad 2001"
call :crejs 5 "traduction Nouvelle Bible Segond 2002" "traduction Nouvelle Bible Segond 2002"
call :crejs 6 "traduction T.O.B. 2010" "traduction T.O.B. 2010"
call :crejs 7 "traduction liturgique 2013" "traduction liturgique 2013"
call :crejs 1 "l'herbe verte en Mc 6,39" "l'herbe verte en Mc 6,39"
call :crejs 2 "fruits bons et fruits pouris dans le N.T" "fruits bons et fruits pouris dans le N.T."
call :crejs 3 "'au large' ou 'en eau profonde' Lc 5,1-11" "'au large' ou 'en eau profonde'? Lc 5,1-11"
call :crejs 4 "splancnizomai = 'pris aux tripes' dans le N.T" "splancnizomai = 'pris aux tripes' dans le N.T. µ"
goto :eof
:crejs
echo     },>>%ficresu%
echo     %2: {>>%ficresu%
echo         "Position": "%1",>>%ficresu%
echo         "nomAAfficher": %3,>>%ficresu%
echo         "formatNomAAfficher": 4,>>%ficresu%
echo         "codeAAfficher": "",>>%ficresu%
echo         "formatCodeAAfficher": 5,>>%ficresu%
echo         "remarqueAAfficher": "En cours",>>%ficresu%
echo         "formatRemarqueAAfficher": 4 >>%ficresu%
echo         "ok" %1
goto :eof