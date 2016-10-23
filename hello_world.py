from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
# starting section for jedi task

@app.route("/hello/jedi/<fname>/<lname>")
def jedi(fname,lname):
    jname = (lname[0:3] + fname[0:2])
    html = """
        <h1>
            Hello your Jedi name is: {}!
        </h1>
    """
    return html.format(jname.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))