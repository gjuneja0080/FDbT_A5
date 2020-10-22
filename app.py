from flask import Flask, render_template
app = Flask(__name__, template_folder='/Users/gopaljuneja/Desktop/Assignment5/server/')

@app.route('/')

def ibsHW():
    return render_template("ibsHW.html")