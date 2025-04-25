from flask import Flask, render_template, request
import creation_graph
import numpy as np


app = Flask(__name__)

@app.route("/", methods=["GET"])
def site_fonction():
    expression = request.args.get('expression', default='x²')
    if not expression:
        expression = 'x²'
    mon_graphique = './static/mon_graphique.png'
    creation_graph.graphique(mon_graphique,
                             tab=[0, 2*np.pi, 60], 
                             f=expression)
    return render_template('index.html', chemin_graphique=mon_graphique)

if __name__=="__main__":
    app.run(debug=True, port=8180)
    
    
