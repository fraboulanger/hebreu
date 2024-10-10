#
# -*- coding: UTF-8 -*-
import os
import argparse
import re
#----------------------------------------------------------------------------

def recurse(dossierEnCoursOri,dossierEnCoursCible,trouve,remplace):
#    print(f"{dossierEnCoursOri=},{dossierEnCoursCible=},{trouve=},{remplace}")
    for el in os.listdir(dossierEnCoursOri):
        if el[-4:] != ".mod":
            elAbsolu="/".join([dossierEnCoursOri,el])
            if os.path.isdir(elAbsolu):
                cibleAbsolu="/".join([dossierEnCoursCible,el])
                #si le dossier n'existe pas dans la cible le creer
                if not os.path.isdir(cibleAbsolu):
#                    print(f"Crée le dossier {cibleAbsolu}")
                    os.mkdir(cibleAbsolu)
                recurse(elAbsolu,cibleAbsolu,trouve,remplace)
            else:
                cibleAbsolu="/".join([dossierEnCoursCible,el])
#                print(f"recopie {elAbsolu} -> {cibleAbsolu} idem")
                with open(elAbsolu,"rb") as ori, open(cibleAbsolu,"wb") as cible:
                    while True:
                        block = ori.read(16*1024*1024)  # work by blocks of 16 MB
                        if not block:  # end of file
                            break
                        cible.write(block)
        else:
            elAbsolu="/".join([dossierEnCoursOri,el])
            cibleAbsolu="/".join([dossierEnCoursCible,el[:-4]])
#            print(f"recopie {elAbsolu} -> {cibleAbsolu} modifié")
            with open(elAbsolu,"r",encoding='utf8' ) as ori, open(cibleAbsolu,"w",encoding='utf8' ) as cible:
                cible.write(ori.read().replace("§§site§§",racineSite))
    return 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    dossierProg=os.path.normcase(os.path.abspath(os.getcwd()))
    dossierProg=re.sub("/[^/]+/\.\./|/\./","/",dossierProg.replace("\\","/"))
#    print(f"{dossierProg=}")
    parser.add_argument("-r", "--root", help="root of file tree", default="../aCopier")
    parser.add_argument("-s", "--site", help="dossier racine des documents sur le site", default="hebreu3.1")
    args = parser.parse_args()
#
    version="1.0"
    if args.root[0:3]=="../" :
        args.root=os.path.normcase(os.path.join(dossierProg,"..\\"))
    args.root=re.sub("/[^/]+/\.\./|/\./","/",args.root.replace("\\","/"))
    args.root=re.sub("/$","",args.root)
#    print(f"{args.root=}")
    racineSite=args.site
#    print(f"{racineSite=}")
#
    recurse(args.root+"/complements/aCopier",args.root,"§§site§§",racineSite)
#
    #####