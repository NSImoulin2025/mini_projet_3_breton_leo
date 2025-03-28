from flask import Flask, render_template, request
import creation_graph
import numpy as np
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def site_fonction():
    args = request.args
    mon_graphique = 'mon_graphique.png'
    fonction = args.get("choix")
    creation_graph.graphique(mon_graphique,
                             tab=[0, 2*np.pi, 60], 
                             fonction="x²")
    return render_template('index.html', chemin_graphique=mon_graphique)

if __name__=="__main__":
    app.run(port=8080)
