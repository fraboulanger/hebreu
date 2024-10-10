import bottle
import os
version="0.3"
racineWeb=os.path.abspath("/".join([os.getcwd(),'../../']))

print(f"Serveur Version [{version }] pour Francis situé en [{racineWeb}]")
print(f"départ http://localhost:8000/hebreu/index.html")

@bottle.route('/')
@bottle.route('/<filepath:path>')
def server_static(filepath="index.html"):
    fichierRel=filepath
    if filepath != "index.html":
        fichierAbs= os.path.abspath("/".join([racineWeb,filepath]))
        if os.path.isdir(fichierAbs):
            fichierRel= "/".join([filepath,"index.html"])
    print(f"affiche [{racineWeb}/{fichierRel}]")
    return bottle.static_file(fichierRel, root=racineWeb)

@bottle.error(404)
def error404(error):
    return 'Erreur 404, je ne trouve pas le fichier.'

bottle.run(host='localhost', port=8000, debug=False)