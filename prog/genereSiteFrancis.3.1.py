#
#Creation du site pour francis
#
# Créer un dossier racine "xxx" 
# se placer dans le dossier "xxx" et lancer le serveur bottle
# mettre toute l'arborescence des fichiers dans le dossier "xxx/Documents"
# Utilise un dossier "/Documents" pour l'arborescence des fichiers du site
# Utilise un dossier "/prog"      pour les programmes générant le site , l'index , la table des matières
# Créer un dossier "/html"        pour les fichiers html du site
# Créer un dossier "/mef"         pour les fichier de mise en forme des fichiers 
# Créer un dossier "/complements" pour les fichiers de transformation des nom de fichiers en titre (ori et aff.csv),
#                                      les fichiers des remarques, introduction, conclusion des pages et élements d'index
#
import os
import argparse
import html
import io
import csv
import pprint
import bs4
import hjson
#
def trier(fichiers):
    nombreDeFichiers=len(fichiers)
    resu=[None]*(nombreDeFichiers+1)
    for el in fichiers:
        rep=translite(fichierSansExtension(el),"Position",None)
        if rep==None:
            print("Non Trouvé [{}]".format(el))
        else:
            if int(rep) > nombreDeFichiers:
                print("Erreur fichier=[{}] [{}] et position [{}]".format(el,nombreDeFichiers,rep))
                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint(fichiers)
            else:
                resu[int(rep)]=el
    return resu

def traiteDossier(parent_path, monDossier,parent_site_path, output_buf, level) -> str:
    recu=""
    cheminReel=os.path.abspath("/".join([parent_path, monDossier]))
    file_list=os.listdir(cheminReel)

    listeElements=trier(file_list)
    outlocal=[]
    monfichierReel=os.path.abspath("/".join([racineWeb,"htmlR",monDossier]))+".html"
    outlocal.append(tetePage)
    outlocal.append(ecrisBulle(encodeUTF8Web(parent_site_path)))  # voir si translite(parent_site_path)
    monFichierintro=os.path.abspath("/".join([racineWeb,"TeteQueue",monDossier+"_intro.html"]))
    existeIntro=os.path.isfile(monFichierintro)
    if existeIntro:
        intro=contenuFichier(monFichierintro)
        outlocal.append(intro)
    num=0
    for el in listeElements: #    pour tous les elements de monDossier
        if el!= None:
            if num == 0:
                outlocal.append(tableEnteteDossiers.format(translite(monDossier,"nomAAfficher",monDossier)))
            fse=fichierSansExtension(el)
            if os.path.isdir(os.path.abspath("/".join([parent_path,monDossier,el]))):#       si element est un dossier
                affichageElement=translite(fse,"nomAAfficher",fse)
                idFormat=translite(fse,"formatNomAAfficher",5)
                affichageElement=HTMLFormat[idFormat]["tete"]+affichageElement+HTMLFormat[idFormat]["queue"]
                chemin_ElementHTML="/".join([dossierHTML,el+".html"])
                nr,remarque=ecrisRemarque(el)
                nc,code=ecrisCode(el)
#                print(f"Dos-> {nc=}, C={code}, {nr=}, R={remarque}, CHE={chemin_siteElement}, AE={affichageElement}, ") # pour les Dossiers
                if nr=="":
                    if nc=="":
                        outlocal.append(tableCorps0.format(encodeUTF8Web(chemin_ElementHTML),"<center>"+affichageElement+"</center>"))
                    else:
                        outlocal.append(tableCorps1.format(encodeUTF8Web(chemin_ElementHTML),"<center>"+affichageElement+"</center>",code))
                else:
                    if nc=="":
                        outlocal.append(tableCorps2.format(encodeUTF8Web(chemin_ElementHTML),"<center>"+affichageElement+"</center>",remarque))
                    else:
                        outlocal.append(tableCorps3.format(encodeUTF8Web(chemin_ElementHTML),"<center>"+affichageElement+"</center>",code,remarque))
                nouveauParent_path=os.path.abspath("/".join([parent_path,monDossier]))
                recu+=traiteDossier(nouveauParent_path,el,"/".join([parent_site_path,monDossier]),output_buf,level+1)
            else:
                chemin_siteElement="/".join([""+racineSite+parent_site_path,monDossier,el])
                chemin_siteElement="/".join(["",racineSite+parent_site_path,monDossier,el])
                affichageElement=translite(fse,"nomAAfficher",fse)
                idFormat=translite(fse,"formatNomAAfficher",5)
                affichageElement=HTMLFormat[idFormat]["tete"]+affichageElement+HTMLFormat[idFormat]["queue"]
                nr,remarque=ecrisRemarque(el)
                nc,code=ecrisCode(el)
#                print(f"pdf-> {nc=}, C={code}, {nr=}, R={remarque}, CHE={chemin_siteElement}, AE={affichageElement}, ") # pour les pdf
                if nr=="":
                    if nc=="":
                        outlocal.append(tableCorps0.format(encodeUTF8Web(chemin_siteElement),affichageElement))
                    else:
                        outlocal.append(tableCorps1.format(encodeUTF8Web(chemin_siteElement),affichageElement,code))
                else:
                    if nc=="":
                        outlocal.append(tableCorps2.format(encodeUTF8Web(chemin_siteElement),affichageElement,remarque))
                    else:
                        outlocal.append(tableCorps3.format(encodeUTF8Web(chemin_siteElement),affichageElement,code,remarque))
            num+=1
    if num !=0:
        outlocal.append(tablePied)
    monFichierConclu=os.path.abspath("/".join([racineWeb,"TeteQueue",monDossier+"_conclu.html"]))
    existeConclu=os.path.isfile(monFichierConclu)
    if existeConclu:
        conclu=contenuFichier(monFichierConclu)
        outlocal.append(conclu)
    outlocal.append(piedPage)
    with io.open(monfichierReel,'w', encoding='utf8') as f:
        f.write(finligne.join(outlocal))
    return ""

def fichierSansExtension(element):
    fin=element.rfind(".")
    if len(element)-fin > 4 :
        fin = len(element)
    return element[0:fin]

def ecrisBulle(chemin):
    out=bulleTete
    for el in chemin.split("/"):
        if el != "" and el != "Documents":
            out+=bulleCorps.format(el+".html",nomBulleFichier(el))
    out+=bullePied
    return out

def nomBulleFichier(el):
    fSE=fichierSansExtension(el)
    if fSE in listeTranslite:
        n=listeTranslite[fSE]["nomAAfficher"]
        if n != "":
            nom=n
        else:
            nom=fSE
    else:
        nom=fSE
    return fichierSansExtension(nom)

def afficheFichier(el):
    fSE=fichierSansExtension(el)
    if fSE in listeTranslite:
        n=listeTranslite[fSE]["nomAAfficher"]
        if n != "":
            idFormat=listeTranslite[fSE]["formatNomAAfficher"]
            nom=HTMLFormat[idFormat]["tete"]+n+HTMLFormat[idFormat]["queue"]
        else:
            nom=el
    else:
        nom=el
    return encodeUTF8Web(fichierSansExtension(nom))

def ecrisRemarque(el):
    fSE=fichierSansExtension(el)
    n=""
    monFichierRemarque=os.path.abspath("/".join([racineWeb,"complements",fSE+"_remarque.html"]))
    existeRemarque=os.path.isfile(monFichierRemarque)
    if existeRemarque:
        remarque=contenuFichier(monFichierRemarque)
    elif fSE in listeTranslite:
        n=listeTranslite[fSE]["remarqueAAfficher"]
        if n != "":
            idFormat=listeTranslite[fSE]["formatRemarqueAAfficher"]
            remarque=HTMLFormat[idFormat]["tete"]+n+HTMLFormat[idFormat]["queue"]
        else:
            remarque=remarqueDefaut
    else:
        remarque=remarqueDefaut
    return n,remarque

def ecrisCode(el):
    fSE=fichierSansExtension(el)
    n=""
    if fSE in listeTranslite:
        n=listeTranslite[fSE]["codeAAfficher"]
        if n != "":
            idFormat=listeTranslite[fSE]["formatCodeAAfficher"]
            code=HTMLFormat[idFormat]["tete"]+n+HTMLFormat[idFormat]["queue"]
        else:
            code=codeDefaut
    else:
        code=codeDefaut
    return n,code


def contenuFichier(monFichier):
    contenu=None
    try:
        f = io.open(monFichier,"r", encoding = 'utf8')
        contenu=f.read()
    finally:
        f.close()
    return contenu

def encodeUTF8Web (stringToCode):
    return ''.join( '&{};'.format(html.entities.codepoint2name[ord(oneChar)])
        if ord(oneChar) in html.entities.codepoint2name
        else oneChar for oneChar in stringToCode )

def effaceFichiers(dossier):
    if not os.path.isdir(dossier):
        os.makedirs(dossier)
    for fichier in os.listdir(dossier) :
        if os.path.isfile(dossier): 
            os.remove("/".join([dossier , fichier]))


def translite(nom,champ,valeurDefaut=""):
    if nom in listeTranslite:
        n=listeTranslite[nom][champ]
        if n=="":
            n=valeurDefaut
    else:
        n=valeurDefaut
    return n

#
# Constantes
#
version="3.1"
racineWeb=os.path.abspath("/".join([os.getcwd(),'../']))
racineSite="hebreu3.1"
dossierHTML=f"/{racineSite}/html"
print(f"{version=}")
print(f"{racineWeb=}")
tetePage="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<title>Dans la bible h&#233;bra&#239;que</title>
<link rel="stylesheet" href="/{}/mef/monstyle.css">
</head>
<body><div class=monTitre>{}</div><br /><div class=monSousTitre>{}</div>""".format(racineSite,encodeUTF8Web("Hébreu biblique :"),encodeUTF8Web("Mes dossiers partagés"))
bulleTete="""<div>
<button class="monbouton" type="button"    onclick="window.location.href = '/{}/html/Documents.html';">Accueil</button>""".format(racineSite)
bulleCorps="""<button class="monbouton" type="button"    onclick="window.location.href = '{}';">{}</button>"""
bullePied="""</div>"""   # Version {}""".format(version)
piedPage="""<br>
<div style="height: 50px">
<hr style="margin: 0px; height:1px; width:100%; background-color: blue;" />
<div><center>Version {}</center></div>
</body>
</html>
""".format(version)
tableEntete="""<br><br><br><br><br><table class="paleBlueRows">
<thead>
<tr><th colspan=3>{}</th>
</tr><br>
<div style="height: 100px">
<hr style="margin: 0px; height:2px; width:100%; background-color: blue;" />
<p>Pour me joindre : <a href="mailto:fraboulanger@orange.fr">Francis Boulanger</a></p></div>
</body>
</html>

<tr>
<th width=70%>Documents</th>
<th width=15%>Code</th>
<th width=15%>Remarques</th>
</tr>
</thead>
<tbody>"""
tableEnteteDossiers="""<br><br><br><br><br><table class="dossiers">
<thead>
<tr><th colspan=3>{}</th>
</tr>
<tr>
<th width=70%>Groupe de documents</th>
<th width=15%>Code</th>
<th width=15%>Remarques</th>
</tr>
</thead>
<tbody>"""
tableCorps0="""<tr>
<td><a href="{}">{}</a></td>
</tr>"""
tableCorps1="""<tr>
<td><a href="{}">{}</a></td>
<td>{}</td>
</tr>"""
tableCorps2="""<tr>
<td><a href="{}">{}</a></td>
<td></td><td>{}</td>
</tr>"""
tableCorps3="""<tr>
<td><a href="{}">{}</a></td>
<td>{}</td><td>{}</td>
</tr>"""
tablePied="""</tr></tbody>
</table>"""
finligne="\r\n"
remarqueDefaut="<span class=maclass0></span>"
codeDefaut="<span class=maclass0></span>"
HTMLFormat=[{"tete":"<span class=maclass0>","queue":"</span>"}, # 0
            {"tete":"<span class=maclass1>","queue":"</span>"}, # 1
            {"tete":"<span class=maclass2>","queue":"</span>"}, # 2
            {"tete":"<span class=maclass3>","queue":"</span>"}, # 3
            {"tete":"<span class=maclass4>","queue":"</span>"}, # 4
            {"tete":"<span class=maclass5>","queue":"</span>"} # 5
            ]

champs=("position","nomAAfficher","formatNomAAfficher","codeAAfficher","formatCodeAAfficher","remarqueAAfficher","formatRemarqueAAfficher")
#         Programme principal
#
out=""
effaceFichiers(dossierHTML)
with open("/".join([racineWeb,"complements","struct.json"]), "r",encoding='utf8' ) as f_json:
    listeTranslite=hjson.load(f_json)
traiteDossier(racineWeb,"Documents","",out,0)
###
