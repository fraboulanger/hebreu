#
# -*- coding: UTF-8 -*-
import os
import argparse
import io
import re
import json
#----------------------------------------------------------------------------

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    dossierProg=os.path.normcase(os.path.abspath(os.getcwd()))
    print(f"{dossierProg=}")
    parser.add_argument("-r", "--root", help="root of file tree", default="..\\")
    parser.add_argument("-d", "--documents", help="dossiers à traiter", default="complements")
    parser.add_argument("-o", "--output", help="fichier pour l'arborescence en JSON", default="complements/struct.json")
    args = parser.parse_args()
#
    version="1.0"
    if args.root=="..\\" :
        args.root=os.path.normcase(os.path.join(dossierProg,"..\\"))
    print(f"{args.root=}")
    fichierSortie=os.path.normcase(os.path.join(args.root,os.path.normcase(args.output)))
    dossierDocuments=os.path.normcase(os.path.join(args.root,os.path.normcase(args.documents)))
    dossierDocuments=re.sub("/[^/]+/\.\./|/\./","/",dossierDocuments.replace("\\","/"))
    longDossierDocuments=len(dossierDocuments)
    ficOri="/".join([dossierDocuments,"ori.csv"])
    ficAff="/".join([dossierDocuments,"aff.csv"])
    trans=lireCSVs(ficOri,ficAff)
    with io.open (fichierSortie, "w",encoding='utf8' ) as monfich:
        json.dump(trans, monfich, indent=4)
        print("---"*20)
        print("Etude de {}...".format(dossierDocuments))
        print("Résultats sur {}".format(fichierSortie))
    #####