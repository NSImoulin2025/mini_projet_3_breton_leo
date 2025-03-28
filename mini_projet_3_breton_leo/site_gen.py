from flask import Flask, render_template, request
import creation_graph
import numpy as np
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def site_fonction():
    args = request.args
    fonction = args.get('fonction')
    mon_graphique = 'mon_graphique.png'
    chemin_graphique = os.path.join("static", "images", mon_graphique) 
    creation_graph.graphique(chemin_graphique,
                             tab=[0, 2*np.pi, 60], 
                             fonction)
    return render_template('index.html',
                           chemin_graphique)

if __name__=="__main__":
    app.run(port=8080)
