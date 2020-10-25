from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey

HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = True

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://imperial:imperial-fdt-online-2019-colossal-shelf@imperial-2020.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com:5432/dvdrental"
db = SQLAlchemy(app)

class Actor(db.Model):
    __tablename__ = 'actor'
    actor_id = db.Column(db.String(255), primary_key=True, unique=True)
    first_name = db.Column(db.String(255), index=True)
    last_name =  db.Column(db.String(255), index=True)
    last_update = db.Column(db.DateTime)

    def __repr__(self):
       return 'Actor ID: ' + self.actor_id, 'First Name: ' + self.first_name, 'Last Name: ' + self.last_name, 'Last Updated: ' + self.last_update

@app.route('/')
@app.route('/home')
def ibsHW():
    return render_template("ibsHW.html")

@app.route('/actors')
def actors():
    actors = Actor.query.all()
    return render_template('actors.html', actors = actors)

if __name__ ==  '__main__':
    app.run(debug=DEBUG_MODE,host=HOST, port=PORT)