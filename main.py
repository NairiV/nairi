from flask import render_template, Flask
app= Flask (__name__)

@app.route("/")
def main():
    return "<h1>NINI <h1> "

@app.route ("/saluda")
def saluda(): 
    return"<marqueen><h2>Hola clase<h2></marquee>"
@app.route ("/login")
def login():
    return render_template("login.html")
app.run()