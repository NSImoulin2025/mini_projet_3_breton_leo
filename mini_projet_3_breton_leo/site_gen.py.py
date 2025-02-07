from flask import Flask

app = Flask(__name__)

@app.route("/")
def site_fonction():
    return "<p>Hello world</p>"

if __name__=="__main__":
    app.run(port=8080)