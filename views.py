from flask import render_template, request, redirect, flash, url_for
from webapp import app
from models import db, Stats


# srf = CSRFProtect(app)


@app.route('/')
def index():
    first_hit = db.session.query(Stats).filter(Stats.id == 1).one().date.strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html", count=db.session.query(Stats).count(), first_hit=first_hit)


@app.route('/raw')
def raw():
    return render_template("raw.html", stats=db.session.query(Stats))
