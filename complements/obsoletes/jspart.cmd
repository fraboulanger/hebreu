@echo off
set ficresu="C:\SiteGITHUB\hebreu\complements\jspart.json"
call :crejs 1 "Ani leDodi. Ct 6,3 ; 7,12" "Ani leDodi. Ct 6:3 ; 7:12"
call :crejs 2 "Ani ma'amin. Varshever Geto-Lid" "Ani ma'amin. Varshever Geto-Lid"
call :crejs 3 "Ashre ha-ish. Ps 1,1-2" "Ashré ha-ish. Ps 1:1-2"
call :crejs 4 "Av ha-rahaman. Da 9,18-19" "Av ha-rahaman. Da 9:18-19"
call :crejs 5 "Barukh Elohenu" "Barukh Elohénu"
call :crejs 6 "Barukh ha-Maqom" "Barukh ha-Maqom"
call :crejs 7 "Betset Israël. Ps 114" "Betsét Israël. Ps 114"
call :crejs 8 "ehad mi yodea . Comptine" "Èhad mi yodéa ?. Comptine"
call :crejs 9 "Hashivenu eleïkha" "Hashivénu elèïkha"
call :crejs 10 "Hinneh lo yanum. Ps 121,1" "Hinnéh lo yanum. Ps 121:1"
call :crejs 11 "Hinneh mah tov" "Hinnéh mah tov"
call :crejs 12 "Kol ha-'olam kullo. N. de Braslaw" "Kol ha-'olam kullo. N. de Braslaw"
call :crejs 13 "Lekhah Dodi. Accueil du Shabbat" "Lekhah Dodi. Accueil du Shabbat"
call :crejs 14 "Lomir allen. A glazele vaijn" "Lomir allen. A glazele vaijn"
call :crejs 15 "Lou Yehi. Naomi Shemer" "Lou Yehi. Naomi Shemer"
call :crejs 16 "Ma'oz Tsour yeshouati (Paroles)" "Ma'oz Tsour yeshouati (Paroles)"
call :crejs 17 "Mi ha-ish. Ps 34,13-15" "Mi ha-ish. Ps 34:13-15"
call :crejs 18 "Min ha-metsar. Ps 118,5-6" "Min ha-métsar. Ps 118:5-6"
call :crejs 19 "Od Yishama. Jr b33,10-11" "Od Yishama. Jr b33:10-11"
call :crejs 20 "Oyfn pripetschik RV" "Oyfn pripetschik (recto-verso)"
call :crejs 21 "Qol Dodi. Ct 2,8" "Qol Dodi. Ct 2:8"
call :crejs 22 "Ronni we-simhi. Za 2,14" "Ronni we-simhi. Za 2:14"
call :crejs 23 "Shema Yisrael. De 6,4" "Shema Yisrael. De 6:4"
call :crejs 24 "Sim shalom" "Sim shalom"
call :crejs 25 "Wihuda le-olam teshev. Jl 4,20" "Wihuda le-olam téshév. Jl 4:20"
call :crejs 26 "Yedid Nephesh" "Yedid Nèphèsh"
call :crejs 27 "Yepheh noph. cf.Ps 48,3" "Yephéh noph. cf.Ps 48:3"
call :crejs 28 "Yerushalayim shel zahav. Naomi Shemer" "Yerushalayim shèl zahav. Naomi Shemer"
call :crejs 29 "Yevarekhekha hashem mi-Sion. Ps 128,5-6" "Yevarekhekha hashem mi-Sion. Ps 128:5-6"
call :crejs 30 "Zekhor davar. Ps 119,49-51 RV" "Zekhor davar. Ps 119:49-51 [recto + verso]"
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