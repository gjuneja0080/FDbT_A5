from flask import Flask, render_template
import os
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import relationship
#from sqlalchemy import Table, Column, Integer, ForeignKey


app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://imperial:imperial-fdt-online-2019-colossal-shelf@imperial-2020.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com/dvdrental'
#db = SQLAlchemy(app)

HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = True

@app.route('/')
def ibsHW():
    return render_template("ibsHW.html")

if __name__ ==  '__main__':
    app.run(debug=DEBUG_MODE,host=HOST, port=PORT)
