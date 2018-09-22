from flask import redirect, render_template
from app import app

from . import db
from .models import Newbie
from .forms import AddNewbieForm


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/<name>/<int:rating>", methods=['GET'])
def welcome(name, rating):
    return render_template('welcome.html', name=name, rating=rating)


@app.route("/newbies", methods=['GET'])
def view_newbies():
    """View all newbie."""
    newbies = Newbie.query.all()
    return render_template('newbies.html', newbies=newbies)


@app.route("/newbies/add", methods=['GET', 'POST'])
def add_newbies():
    form = AddNewbieForm()
    if form.validate_on_submit():
        newbie = Newbie(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            year=form.year.data
        )
        db.session.add(newbie)
        db.session.commit()
        return redirect('/newbies')
    return render_template('new_newbie.html', form=form)
