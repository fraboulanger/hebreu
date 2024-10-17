#
# -*- coding: UTF-8 -*-
import os
import argparse
import html
import io
import re
import hjson
#----------------------------------------------------------------------------
modeleDocumentTete="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<title>Dans la bible h&#233;bra&#239;que</title>
<link rel="stylesheet" href="/§§site§§/mef/monstyle.css">
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
    <button class="monbouton" type="button" onclick="window.location.href = '/§§site§§/html/Documents.html';">Accueil</button>
</div>
<br />
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
elementCorps="""{0}<LI><a href="{1}">{2}</a></LI>"""
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

def traduction(el):
    elmodif=re.match(r"^(.+?)(\..{2,4})?$",el).group(1)
    return trans[elmodif]["nomAAfficher"]

def ecrire(el):
#    print(f"{el}")
    monfich.write(el+finLigne)

def recurse(parent,element,profondeur):
    dossierEnCours="/".join([parent,element])
#    print(f"{dossierEnCours=}")
    elementsEnCours=os.listdir(dossierEnCours)
    listeElements=trouveListeClassée(elementsEnCours)
#    print(f"{listeElements=}")
    for el in listeElements:
        if el != None:
            elementTraduit=traduction(el)
            elAbsolu="/".join([dossierEnCours,el])
            if os.path.isdir(elAbsolu):
                ecrire(dossierTete.format(indentation*profondeur,elementTraduit))
                ecrire(elementsTete.format(indentation*profondeur))
                recurse(dossierEnCours,el,profondeur+1)
                ecrire(elementsQueue.format(indentation*profondeur))
                ecrire(dossierQueue.format(indentation*profondeur))
                continue
            else:
                lien="/".join(["",racineSite,args.documents,parent[longDossierDocuments+2:],element,el])
#                print(f"{racineSite=},{args.documents=},{parent[longDossierDocuments+2:]=},{element=},{el=}")
                ecrire(elementCorps.format(indentation*(profondeur+1),lien,elementTraduit))
    return 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    dossierProg=os.path.normcase(os.path.abspath(os.getcwd()))
#    print(f"{dossierProg=}")
    parser.add_argument("-r", "--root", help="root of file tree", default="..\\")
    parser.add_argument("-d", "--documents", help="dossiers à traiter", default="Documents")
    parser.add_argument("-o", "--output", help="fichier pour l'arborescence en html", default="html/tdm.html")
    parser.add_argument("-t", "--temporaire", help="fichier de sortie temporaire", default="TeteQueue/tdm.html")
    parser.add_argument("-s", "--site", help="dossier racine des documents sur le site", default="hebreu3.1")
    args = parser.parse_args()
#
    version="1.3"
    finLigne="\r\n"
    indentation="    "
    if args.root=="..\\" :
        args.root=os.path.normcase(os.path.join(dossierProg,"..\\"))
    args.root=re.sub("/[^/]+/\.\./|/\./","/",args.root.replace("\\","/"))
#    print(f"{args.root=}")
    racineSite=args.site
#    print(f"{racineSite=}")
    fichierSortie=os.path.normcase(os.path.join(args.root,os.path.normcase(args.temporaire)))
    fichierSortie=re.sub("/[^/]+/\.\./|/\./","/",fichierSortie.replace("\\","/"))
    dossierDocuments=os.path.normcase(os.path.join(args.root,os.path.normcase(args.documents)))
    dossierDocuments=re.sub("/[^/]+/\.\./|/\./","/",dossierDocuments.replace("\\","/"))
    longDossierDocuments=len(dossierDocuments)
    with open("/".join([args.root,"complements","struct.json"]), "r",encoding='utf8' ) as f_json:
        trans=hjson.load(f_json)
#    print(f"{fichierSortie=}")
    with io.open (fichierSortie, "w",encoding='utf8' ) as monfich:
        ecrire(modeleDocumentTete.replace("§§site§§",racineSite))
        recurse(dossierDocuments,"",0)
        ecrire(DocumentQueue)
    fichierFinal=os.path.normcase(os.path.join(args.root,os.path.normcase(args.output)))
    fichierFinal=re.sub("/[^/]+/\.\./|/\./","/",fichierFinal.replace("\\","/"))
#    print(f"deplace {fichierSortie} -> {fichierFinal}")
    os.replace(fichierSortie,fichierFinal)
    print("---"*20)
    print("Etude de {}...".format(dossierDocuments))
    print("Résultats sur {}".format(fichierFinal))
    #####