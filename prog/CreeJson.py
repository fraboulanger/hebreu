#
# -*- coding: UTF-8 -*-
import os
import argparse
import io
import re
import json
arbre={}
version = "1.0" #20241014
def lister_fichiers_recursivement(repertoire):
    global arbre,longDosIni
    nd=0
    for racine, repertoires, fichiers in os.walk(repertoire):

        r=racine.split("\\")[-1]
        dP=("/".join(r.split("\\")[:-1]))
        dirPère=dP[longDosIni+1:]
        dirPère+= "/" if dirPère=="" else ""
#        print(f"Départ: {racine}")
#        print(f"{ancien_arbre=}")
        #Traitement des dossiers
        posi = list(x for x in range(1,len(repertoires)+len(racine)))
        """"""
        for dirfils in repertoires:
#            print(f"[{dirPère}] [{dirfils}]")
#            print(f"DBG (lister_fichiers_recursivement)D: {dirPère=}, {dirfils=} dp dans ancien {dirfils in ancien_arbre}")
            if dirfils in ancien_arbre:
                d=ancien_arbre[dirfils]
                if d["Position"] in posi :
                    posi.remove(d["Position"])
                else:
                    d["Position"]=posi.pop(0)
            else:
                d={ "Commentaire": "",
                    "Position": posi.pop(0),
                    "nomAAfficher": dirfils,
                    "formatNomAAfficher": 1,
                    "codeAAfficher": "",
                    "formatCodeAAfficher": 5,
                    "remarqueAAfficher": "",
                    "formatRemarqueAAfficher": 5
                    }
                print(f"*** Attention *** La présentation du dossier {dirfils} est mise par défaut")
            arbre[dirfils]=d
        """"""
        # Traitement des fichiers
        d2="/".join(dP.split("\\")[:-1])
        for f in fichiers:
            if "." == f[-4]:
                fichier=f[:-4]
            else:
                fichier=f
#            print(f"[{dirPère}] {fichier}")
#            print(f"DBG (lister_fichiers_recursivement)D: {dirPère=}, {fichier=} dp dans ancien {fichier in ancien_arbre}")
            if fichier in ancien_arbre:
                d=ancien_arbre[fichier]
                if d["Position"] in posi :
                    posi.remove(d[Position])
                else:
                    d["Position"]=posi.pop(0)
            else:
                d={ "Commentaire": "",
                    "Position": posi.pop(0),
                    "nomAAfficher": fichier,
                    "formatNomAAfficher": 3,
                    "codeAAfficher": "",
                    "formatCodeAAfficher": 3,
                    "remarqueAAfficher": "",
                    "formatRemarqueAAfficher": 3
                } 
                print(f"*** Attention *** La présentation du fichier {fichier} est mise par défaut")
            arbre[fichier]=d
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    dossierProg=os.path.normcase(os.path.abspath(os.getcwd()))
    parser.add_argument("-r", "--root", help="root of file tree", default=r"..\\")
    parser.add_argument("-d", "--documents", help="dossiers à traiter", default="Documents")
    parser.add_argument("-o", "--output", help="fichier pour l'arborescence en JSON", default="resultat.json")
    parser.add_argument("-a", "--ancien", help="Ancien fichier pour l'arborescence en JSON", default="resultat.json.anc")
    args = parser.parse_args()
#
    version="1.0"
    racine=args.root
    if racine==r"..\\" :
        racine=os.path.normcase(os.path.join(dossierProg,"..\\"))
    dossier_initial = os.path.normcase(os.path.join(racine,args.documents))
    dossier_initial=re.sub(r"/[^/]+/\.\./|/\./",r"/",dossier_initial.replace("\\",r"/"))
    longDosIni=len(dossier_initial)
#    print(f"Dossier_initial : {dossier_initial}")
    fichierSortie=os.path.normcase(os.path.join(racine,os.path.normcase(args.output)))
    fichierSortie=re.sub(r"/[^/]+/\.\./|/\./",r"/",fichierSortie.replace("\\",r"/"))
#    print(f"Fichier json résultat : {fichierSortie}")
    AncienSortie=os.path.normcase(os.path.join(racine,os.path.normcase(args.ancien)))
    AncienSortie=re.sub(r"/[^/]+/\.\./|/\./",r"/",AncienSortie.replace("\\",r"/"))
#    print(f"Ancien Fichier json : {AncienSortie}")
    dossierDocuments=os.path.normcase(os.path.join(racine,os.path.normcase(args.documents)))
    dossierDocuments=re.sub(r"/[^/]+/\.\./|/\./",r"/",dossierDocuments.replace("\\",r"/"))
#    longDossierDocuments=len(dossierDocuments)
    if os.path.isfile(AncienSortie):
        with io.open (AncienSortie, "r",encoding='utf8' ) as monfich:
#           print("DBG (Cree Json) : lecture du fichier ancien")
           ancien_arbre=json.load(monfich)
    else:
#        print("DBG (Cree Json) : pas d'ancien {AncienSortie}")
        ancien_arbre={}
    lister_fichiers_recursivement(dossier_initial)
    with io.open (fichierSortie, "w",encoding='utf8' ) as monfich:
        json.dump(arbre, monfich, indent=4)
   