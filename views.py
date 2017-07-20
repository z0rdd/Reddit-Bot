from flask import render_template, request, redirect, flash, url_for
from webapp import app


# srf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template("index.html")