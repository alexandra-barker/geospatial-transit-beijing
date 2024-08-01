from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def w209():
    return render_template("index.html") 

@app.route("/background")
def background():
    return render_template("background.html") 

@app.route("/spatial")
def spatial():
    return render_template("spatial.html") 

@app.route("/temporal")
def temporal():
    return render_template("temporal.html") 

@app.route("/composition")
def composition():
    return render_template("composition.html") 

if __name__ == "__main__":
    app.run()
