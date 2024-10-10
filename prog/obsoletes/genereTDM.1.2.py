#
# -*- coding: UTF-8 -*-
import os
import argparse
import html
import io
import re
#----------------------------------------------------------------------------
DocumentTete="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<title>Dans la bible h&#233;bra&#239;que</title>
<link rel="stylesheet" href="/hebreu/mef/monstyle.css">
</head>
<body>
<style type="text/css">
H1.demo {
           text-align:center ;
           border:solid;
           margin-top:0px;
}
<!--/*
UL, LI {font-size:.8rem;}
*/-->
UL.arbre, .arbre LI {list-style: none;}
UL INPUT {
    position: absolute;
    opacity: 0;
}
.arbre LABEL {display: inline-block;}
UL INPUT ~ UL { display: none;}
UL INPUT:checked ~ UL {display: block;}
UL.arbre1, .arbre1 LI {list-style: none;}
.arbre1 LABEL{
    display: inline-block;
    cursor: pointer;
    height: 1REM;
    line-height: 1REM;
    vertical-align: middle;
    background: url(icons.gif) no-repeat;
    background-position: 18px 0;
}
 
.arbre1 LABEL::before{
    display: inLIne-block;
    cursor: pointer;
    height: 1REM;
    LIne-height: 1REM;
    vertical-align: middle;
    background: url(icons.gif) no-repeat;
    content: "";
    width: 1REM;
    margin: 0 22px 0 0;
    background-position: 0 -32px;
}
 
.arbre1 INPUT:checked + LABEL::before{background-position: 0 -16px;}

.arbre1 INPUT:disabled + LABEL {
    cursor: default;
    opacity: .6;
}

</style>
<div class=monTitre>H&eacute;breu biblique :</div><br /><div class=monSousTitre>Mes dossiers partag&eacute;s</div>
<div>
    <button class="monbouton" type="button" onclick="window.location.href = '/hebreu/html/Documents.html';">Accueil</button>
</div>
<br /><small><small> Essai de table des matières. Version 1.3</small></small>
<br />Cliquez sur les + pour faire appara&icirc;tre la structure du site.<br />
<div>
  <UL class=arbre1>
    <LI>
      <INPUT type="checkbox" id="dossier_d1" checked="checked"/>
      <LABEL for="dossier_d1">Accueil</LABEL>
"""
dossierTete="""{0}<UL>
{0}  <LI>
{0}    <INPUT type="checkbox" id="dossier_d1_1" />
{0}    <LABEL for="dossier_d1_1">{1}</LABEL>"""
elementsTete="""{0}    <UL>"""
elementCorps="""{0}<LI><a href="/{1}">{2}</a></LI>"""
elementsQueue="""{0}    </UL>"""
dossierQueue="""{0}  </LI>
{0}</UL>"""
DocumentQueue="""
</div>
<br>
<div style="height: 50px">
    <hr style="margin: 0px; height:1px; width:100%; background-color: blue;" />
    <center>Version 3.1</center>
</div>
</body>
</html>
"""

def trouveListeClassée(fichiers):
	nombreDeFichiers=len(fichiers)
	resu=[None]*nombreDeFichiers
	for el in fichiers:
		elmodif=re.match(r"^(.+?)(\..{2,4})?$",el).group(1)
		rep=int(trans[elmodif]["Position"])-1
		if rep==None:
			print("Non Trouvé [{}]".format(el))
		else:
			if ((rep >= nombreDeFichiers) or (rep < 0)):
				print("Erreur fichier=[{}] [{}] et position [{}]".format(el,nombreDeFichiers,rep))
			else:
				resu[rep]=el
	return resu

def lireCSVs(ficOri,ficAff):
    rep={}
    ori=io.open(ficOri, 'r', encoding='utf8')
    aff=io.open(ficAff, 'r', encoding='utf8')
    numeroLigne=1
    for lig in ori.readlines():
        ligOri=lig.strip('\n')
        eclate=ligOri.split("\t")
        ligAff=aff.readline().strip('\n')
        if eclate[0].isdigit(): 
            eclateAff=ligAff.split("\t")
            nomAAfficher,formatNomAAfficher=eclateAff[1].split("§")
            if eclateAff[2]=="":
                codeAAfficher,formatCodeAAfficher="","5"
            else:
                codeAAfficher,formatCodeAAfficher=eclateAff[2].split("§")
            if eclateAff[3]=="":
                remarqueAAfficher,formatRemarqueAAfficher="","5"
            else:
                remarqueAAfficher,formatRemarqueAAfficher=eclateAff[3].split("§")
            rep[eclate[1]]={"Position":eclate[0],
                            "nomAAfficher":nomAAfficher,
                            "formatNomAAfficher":int(formatNomAAfficher),
                            "codeAAfficher":codeAAfficher,
                            "formatCodeAAfficher":int(formatCodeAAfficher),
                            "remarqueAAfficher":remarqueAAfficher,
                            "formatRemarqueAAfficher":int(formatRemarqueAAfficher)
                            }
        numeroLigne+=1
    return rep

def traduction(el):
	elmodif=re.match(r"^(.+?)(\..{2,4})?$",el).group(1)
	return trans[elmodif]["nomAAfficher"]

def ecrire(el):
#	print(f"{el}")
	monfich.write(el+finLigne)

def recurse(parent,element,profondeur):
	dossierEnCours=os.path.join(parent,element)
	elementsEnCours=os.listdir(dossierEnCours)
	listeElements=trouveListeClassée(elementsEnCours)
	for el in listeElements:
			elementTraduit=traduction(el)
			elAbsolu=os.path.join(dossierEnCours,el)
			if os.path.isdir(elAbsolu):
				ecrire(dossierTete.format(indentation*profondeur,elementTraduit))
				ecrire(elementsTete.format(indentation*profondeur))
				recurse(dossierEnCours,el,profondeur+1)
				ecrire(elementsQueue.format(indentation*profondeur))
				ecrire(dossierQueue.format(indentation*profondeur))
				continue
			else:
				lien="/".join([args.documents,parent[longDossierDocuments:],element,el])
				ecrire(elementCorps.format(indentation*(profondeur+1),lien,elementTraduit))
	return 


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	dossierProg=os.path.normcase(os.path.abspath(os.getcwd()))
	print(f"{dossierProg=}")
	parser.add_argument("-r", "--root", help="root of file tree", default="..\\")
	parser.add_argument("-d", "--documents", help="dossiers à traiter", default="Documents")
	parser.add_argument("-o", "--output", help="fichier pour l'arborescence en html", default="html/tdm.html")
	args = parser.parse_args()
#
	version="1.3"
	finLigne="\r\n"
	indentation="    "
	if args.root=="..\\" :
		args.root=os.path.normcase(os.path.join(dossierProg,"..\\"))
	print(f"{args.root=}")
	fichierSortie=os.path.normcase(os.path.join(args.root,os.path.normcase(args.output)))
	dossierDocuments=os.path.normcase(os.path.join(args.root,os.path.normcase(args.documents)))
	longDossierDocuments=len(dossierDocuments)
	ficOri="/".join([args.root,"complements","ori.csv"])
	ficAff="/".join([args.root,"complements","aff.csv"])
	trans=lireCSVs(ficOri,ficAff)
	with io.open (fichierSortie, "w",encoding='utf8' ) as monfich:
		ecrire(DocumentTete)
		recurse(dossierDocuments,"",0)
		ecrire(DocumentQueue)
		print("---"*20)
		print("Etude de {}...".format(dossierDocuments))
		print("Résultats sur {}".format(fichierSortie))
	#####