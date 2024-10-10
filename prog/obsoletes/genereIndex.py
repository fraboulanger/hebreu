#
#
"""Remplissage d'une stucture pour un index html à partir d'un fichier csv
	structure du fichier de départ:
	nomIndex;lienHTML;
"""
import csv
import html
import io
import os

class créeIndex(object):
	def __init__(self,fichierEntrée,fichierSortie=""):
		self.fEntrée=fichierEntrée
		self.fSortie=fichierSortie
		self.maliste=[]
		with io.open(self.fEntrée,  encoding='utf-8') as csvfichier:
			lecture=csv.reader(csvfichier,dialect="excel",delimiter="\t")
			for ligne in lecture:
				self.maliste.append(ligne)
		self.maliste=sorted(self.maliste, key=lambda p: p[0])
#		print(f"{self.maliste}")

	def imprime(self):
		initiale=""
		for numeroligne,ligne in enumerate(self.maliste):
			nvInitiale = ligne[0][0].upper()
			if initiale != nvInitiale:
				initiale = nvInitiale
				print(f"======= {initiale[0]} ========")
			print(f"ligne{numeroligne}->[{ligne[0]}],[{ligne[1]}]")
#
	def imprimeResu(self) -> str:
		initiale=""
		resu=iniHTML
		numeroligne=0
		for ligne in self.maliste:
			lig=""
			nvInitiale = ligne[0][0].upper()
			if initiale != nvInitiale:
				if (numeroligne % 2) !=0:  #cherche modulo
					lig="".join([lig,"	</tr>\n"])
				initiale = nvInitiale
				numeroligne = 0
				lig="".join([lig,initialeHTML.format(initiale)])
			if (numeroligne % 2) ==0:
				lig="".join([lig,itemHTMLpair.format(encodeUTF8Web(ligne[0]),encodeUTF8Web(ligne[1]))])
			else:
				lig="".join([lig,itemHTMLimpair.format(encodeUTF8Web(ligne[0]),encodeUTF8Web(ligne[1]))])
			numeroligne+=1
			resu="".join([resu,lig])
		resu+=finHTML
#		print(resu)
		return resu
###

def encodeUTF8Web (stringToCode):
    return ''.join( '&{};'.format(html.entities.codepoint2name[ord(oneChar)])
                    if ord(oneChar) in html.entities.codepoint2name
                    else oneChar for oneChar in stringToCode )

iniHTML="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<style>
	.demo {
		border: 1px solide #C0C0C0;
		align:center;
		width:80%;
		margin-left:auto;
		margin-right:auto;
		border-spacing: 20px 2px;
		border-collapse: separate;
	}
/*	.demo th {
		border:1px solide #C0C0C0;
		padding:5px;
		background:#F0F0F0;
	}
*/	.demo td {
		width:50%;
		border:1px solide #C0C0C0;
		padding: 10px;
	}

	.LettreIndex {
		font-size: 25px;
		color: green;
		text-align: center;
		background-color: #EEEEEE;
		border-bottom: 2px solid black;
	}
	.ItemIndex {
		font-size: 18px;
		color: #FF0000;
}
</style>
</head>
<body>
<p><h2><a href="/html/Documents.html">Retour &agrave; l'accueil</a></h2></p>

<table class="demo" >
	<caption>Index</caption>
	<thead>
		<tr>
			<th></th>
		</tr>
	</thead>
	<tbody>
"""
initialeHTML="""	<tr>
		<td id={0} class="LettreIndex" colspan="2">{0}</td>
	</tr>"""
itemHTMLpair="""	<tr>
		<td><a class="ItemIndex" href="{1}.html">{0}</a></td>"""
itemHTMLimpair="""<td><a class="ItemIndex" href="{1}.html">{0}</a></td>
	</tr>"""
finHTML="""	<tbody>
</table>
</body>
</html>\n"""
version="1.9"
racineWeb=os.path.abspath("/".join([os.getcwd(),'../']))
ficCSV="/".join([racineWeb,"complements","indexSite.csv"])
monIndex=créeIndex(ficCSV)
#    monIndex.imprime()
resu=monIndex.imprimeResu()
with io.open("/".join([racineWeb,"html","indexSite.html"]),encoding='utf-8', mode='w+') as sortie:
	sortie.write(resu)
####