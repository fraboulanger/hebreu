# -*- coding: utf-8 -*-
"""Mettre ici la documentation
"""
__author__ = "Guy Tittelein"
__copyright__ = "Copyright 2021, Projet personnel"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Guy Tittelein"
__email__ = "guy.tittelein@xx.fr"
__status__ = "Développement"
#
import os
import io
#
listeHebraHTML=[
"א","&#x05D0","Lettre hébraïque alef",
"ב","&#x05D1","Lettre hébraïque bet / Lettre hébraïque bèt",
"ג","&#x05D2","Lettre hébraïque gimel / Lettre hébraïque guimel",
"ד","&#x05D3","Lettre hébraïque dalet / Lettre hébraïque dalèt",
"ה","&#x05D4","Lettre hébraïque he / Lettre hébraïque hè",
"ו","&#x05D5","Lettre hébraïque vav / Lettre hébraïque waw",
"ז","&#x05D6","Lettre hébraïque zayin / Lettre hébraïque zaïn",
"ח","&#x05D7","Lettre hébraïque het / Lettre hébraïque hèt",
"ט","&#x05D8","Lettre hébraïque tet / Lettre hébraïque tèt",
"י","&#x05D9","Lettre hébraïque yod / Lettre hébraïque youd",
"ך","&#x05DA","Lettre hébraïque kaf final",
"כ","&#x05DB","Lettre hébraïque kaf",
"ל","&#x05DC","Lettre hébraïque lamed / Lamèd",
"ם","&#x05DD","Lettre hébraïque mem final / Mém final",
"מ","&#x05DE","Lettre hébraïque mem / Lettre hébraïque Mém",
"ן","&#x05DF","Lettre hébraïque nun final / Lettre hébraïque noun final",
"נ","&#x05E0","Lettre hébraïque nun / Lettre hébraïque noun",
"ס","&#x05E1","Lettre hébraïque samekh / Lettre hébraïque samèkh",
"ע","&#x05E2","Lettre hébraïque ayin / Lettre hébraïque aïn",
"ף","&#x05E3","Lettre hébraïque pe final / Lettre hébraïque pé final",
"פ","&#x05E4","Lettre hébraïque pe / Lettre hébraïque pé",
"ץ","&#x05E5","Lettre hébraïque tsadi final / Lettre hébraïque tsadé final",
"צ","&#x05E6","Lettre hébraïque tsadi / Lettre hébraïque tsadé",
"ק","&#x05E7","Lettre hébraïque qof, kof / Lettre hébraïque qouf",
"ר","&#x05E8","Lettre hébraïque resh / Lettre hébraïque rèch",
"ש","&#x05E9","Lettre hébraïque shin / Lettre hébraïque chine",
"ת","&#x05EA","Lettre hébraïque tav",
"װ","&#x05F0","Ligature hébraïque yiddish vav double, Tsvy vovn / Lettre hébraïque yidiche double waw",
"ױ","&#x05F1","Ligature hébraïque yiddish vav yod, Vov yud / Lettre hébraïque yidiche waw yod",
"ײ","&#x05F2","Ligature hébraïque yiddish yod double, Tsvey yudn / Lettre hébraïque yidiche double youd  ",
"ָ","&#x05B8;","HEBREW POINT QAMATS",
"כּ","&#xFB3B;","HEBREW LETTER KAF WITH DAGESH",
"בּ","&#xFB31;","HEBREW LETTER ALEF",
"״","&#x05F4;","HEBREW PUNCTUATION GERSHAYIM",
"ּ","&#x05BC;","",
"׳","&#x05F3;","",
"","","",
"","","",
"","","",
"","","",
]
version="2.2"
racineWeb=os.path.abspath("/".join([os.getcwd(),'../']))


def creeDico(maListe):
	monDic={}
	for el in range(0,len(maListe),3):
		monDic[maListe[el]]=maListe[el+1]
	return monDic

def main():
	global monDico;
	monDico=creeDico(listeHebraHTML)
	rep={}
	ori=io.open(ficOri, 'r', encoding='utf8')
	numeroLigne=1
	chaineOri= ori.read()
	ori.close()
	for cara in monDico.keys():
		chaineOri=chaineOri.replace(cara,monDico[cara])
	aff=io.open(ficAff, 'w', encoding='utf8')
	aff.write(chaineOri)
	aff.close()
	return False
if __name__ == '__main__':
	ficOri="/".join([racineWeb,"complements","aff.csv"])
	ficAff="/".join([racineWeb,"complements","affmodi.csv"])

	exit (main())
