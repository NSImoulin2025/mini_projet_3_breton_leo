from flask import Flask, render_template
import creation_graph

app = Flask(__name__)

@app.route("/")
def site_fonction():
    return render_template('index.html')

if __name__=="__main__":
    app.run(port=8080)
