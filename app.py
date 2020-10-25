from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey

HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = True

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Falsev
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://imperial:imperial-fdt-online-2019-colossal-shelf@imperial-2020.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com:5432/dvdrental"
db = SQLAlchemy(app)

class Inventory(db.Model):
  film_id = db.Column(db.Integer(), primary_key=True)
  inventory_id = db.Column(db.Integer(), ForeignKey('film.film_id'))
  store_id = db.Column(db.Integer())

  def __repr__(self):
    return 'Inventory ID: ' + str(self.inventory_id)

class Film(db.Model):
  __tablename__ = 'film'
  film_id = db.Column(db.Integer, primary_key=True)

  title = db.Column(db.String(255), index=True, unique=True)
  description = db.column(db.Text())

  copies = relationship('Inventory')

  def __repr__(self):
    return 'FILM: title is ' + self.title

class Actor(db.model):
    __tablename__ = 'actor'
    actor_id = db.Column(db.String(255), primary_key=True, unique=True)
    first_name = db.Column(db.String(255), index=True)
    last_name =  db.Column(db.String(255), index=True)
    last_update = db.Column(db.DateTime)

    def __repr__(self):
        return 'actor_id: ' + self.actor_id, 'first_name: ' + self.first_name 

@app.route('/')
def ibsHW():
    return render_template("ibsHW.html")

@app.route('/films')
def films():
  films = Film.query.all()
  return render_template('films.html', films = films)

@app.route('/actors')
def actors():
    actors = Actor.query.all()
    return render_template('actors.html', actors = actors)
if __name__ ==  '__main__':
    app.run(debug=DEBUG_MODE,host=HOST, port=PORT)