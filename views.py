from flask import render_template, request, redirect, flash, url_for
from webapp import app
from models import db, Stats
from sqlalchemy import func, desc, Date
from plots import main_plot, person_plot



@app.route('/')
def index():
    first_hit = db.session.query(Stats).filter(Stats.id == 1).one().date.strftime("%Y-%m-%d %H:%M:%S")
    query = db.session.query(Stats.author, func.sum(Stats.hit_count).label("Total")).group_by(Stats.author)
    query_top = query.order_by(desc(func.sum(Stats.hit_count).label("Total"))).first()
    query_chart = db.session.query(func.cast(Stats.date, Date),
                                   func.sum(Stats.hit_count).label("Total")).group_by(func.cast(Stats.date, Date))
    script, div = main_plot(query_chart)


    return render_template("index.html", count=db.session.query(Stats).count(), first_hit=first_hit, top=query_top,
                           script=script, div=div)


@app.route('/raw')
def raw():
    return render_template("raw.html", stats=db.session.query(Stats))


@app.route('/lb')
def lb():
    query = db.session.query(Stats.author, func.sum(Stats.hit_count).label("Total")).group_by(Stats.author)
    query = query.order_by(desc(func.sum(Stats.hit_count).label("Total")))
    query_all = query.all()

    return render_template("lb.html", qry=query_all)


@app.route('/individual/<person>')
def individual(person):
    personal_query = db.session.query(Stats).filter(Stats.author == person)
    post_count = personal_query.count()
    sum_query = db.session.query(Stats.author,
                                 func.sum(Stats.hit_count).label("Total")).group_by(Stats.author). \
        filter(Stats.author == person).first()

    query_chart = db.session.query(func.cast(Stats.date, Date).label("Date"),
                                   func.sum(Stats.hit_count).label("Total"),
                                   Stats.author).group_by(func.cast(Stats.date, Date),
                                                          Stats.author).filter(Stats.author == person)
    script, div = person_plot(query_chart, person, query_chart.count())


    return render_template("person.html", stats=personal_query, script=script, div=div, person_total=sum_query,
                           post_count=post_count)
