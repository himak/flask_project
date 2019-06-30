from flask import Flask, render_template
from random import choice


jokes = [
    "3 Database Admins walked into a NoSQL bar. A little later, they walked out because they couldn’t find a table.",
    "The C language combines all the power of assembly language with all the ease-of-use of assembly language.",
    "8 bytes walk into a bar, the bartenders asks \"What will it be?\" One of them says, \"Make us a double.\"",
    "Chuck Norris doesn’t have disk latency because the hard drive knows to hurry the hell up.",
]

app = Flask(__name__)

@app.route("/")
def home():
    # return "<h1>Super Blog</h1>"
    return render_template('home.html', active_page='home')

@app.route("/kontakt/")
def contact():
    return render_template('contact.html', active_page='contact')

@app.route("/vtip/")
@app.route("/vtip/<name>/")
def joke( name="Tajomný neznámy" ):
    return render_template( 'joke.html', joke=choice(jokes), name=name, active_page='joke' )



