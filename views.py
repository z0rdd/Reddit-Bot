from flask import render_template, request, redirect, flash, url_for
from webapp import app
from models import db, stats


# srf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template("index.html")
