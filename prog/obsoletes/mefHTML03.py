import bs4
import os
import argparse
import html
import io
import re
version="0.3"
class TraverseSite(object):
    def __init__(self, args):
        self.root = args.root
        self.tRoot=len(self.root)
        self.nouvHTML = args.nouvHTML
        self.exclude_name = args.exclude_name
        self.prog=args.prog
#
        print("root:%s" % self.root)
        self._recurse(self.root, os.listdir(self.root))
#        self.test(buf)
#        buf.append(piedpage)
#        output_str = "\n".join(buf)
#        if len(args.output) != 0:
#            with io.open(args.output, 'w', encoding='utf8') as sortie:
#                sortie.write(output_str)

    def _recurse(self, parent_path, file_list):
#        print(f"Va traiter :[{parent_path}], {file_list}")
        if len(file_list) == 0:
            return
        else:
            file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
            for idx, sub_path in enumerate(file_list):
                if dedans(sub_path,self.exclude_name):
                    continue
                print(f"Va traiter :[{idx:2}][{parent_path}], {sub_path},[{parent_path[self.tRoot:]}]")
                full_path = os.path.join(parent_path, sub_path)
                if os.path.isdir(full_path)and  not dedans(os.path.join(full_path,sub_path) , self.exclude_name):
                    dossierHtml=os.path.join(self.nouvHTML, full_path[self.tRoot:])
                    self._recurse(full_path, os.listdir(full_path))
                elif os.path.isfile(full_path):
                    nvc= parent_path[self.tRoot:]
                    if nvc == "":
                        DossierHtmlMEF=self.nouvHTML
                    else:
                        DossierHtmlMEF=os.path.join(self.nouvHTML,nvc)
                    #cree le nouveau fichier HTML
                    copyPretty(parent_path, DossierHtmlMEF, sub_path)
        return

def dedans( monNom, listeRE):
    for maRE in listeRE:
        if re.search(maRE, monNom):
            return True
    return False

def copyPretty(dosEnt="",dosSor="",fichier=""):
    if dosEnt == "" or dosSor=="" or fichier=="":
        print(f"Erreur pas de fichier {dosEnt=} , {dosSor=} , {fichier=}")
    elif debug:
        print(f"Traite [{dosEnt=}] [{dosSor=}] [{fichier=}]")
    else:
        html=[]
        with io.open(os.path.join(dosEnt,fichier), "r", encoding="UTF-8") as f:
            r=f.readlines()
        rep="\r\n".join(r)
        for lig in rep.split("\n"):
            r=lig.strip(" \r\n")
            if len(r) != 0:
#                print(r)
                html.append(r)
        pretty_html = bs4.BeautifulSoup("".join(html), 'html5lib').prettify(formatter="html5")
#        print(f"le fichier {fichSor} a ete cree :")
#        print(pretty_html)
        if not os.path.isdir(dosSor):
            os.makedirs(dosSor)
        with open(os.path.join(dosSor,fichier), "w", encoding="UTF-8") as f:
            f.write(pretty_html)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", help="root of file tree", default="../html")
    parser.add_argument("-nf", "--nouvHTML", help="nouvelle racine des fichiers", default="../htmlR")
    parser.add_argument("-p", "--prog", help="emplacement des fichiers prog", default="/prog")
    parser.add_argument("-xn", "--exclude_name", nargs='*', help="exclude name", default=["\.bak$","\.png$","^Code","\.pdf"])
    args = parser.parse_args()
#
    args.root=os.path.abspath("/".join([os.getcwd(),args.root]))
    args.nouvHTML=os.path.abspath("/".join([os.getcwd(),args.nouvHTML]))
    if not os.path.isdir(args.nouvHTML):
        os.makedirs(args.nouvHTML)
#
    debug=False
    monSite=TraverseSite(args)
    print(f'Les fichiers html bien structurés sont générée en {args.nouvHTML} avec la version {version} de mefHTML1.py')
####