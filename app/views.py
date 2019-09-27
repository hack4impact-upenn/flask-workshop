from flask import redirect, render_template
from app import app

from . import db
from .models import Newbie
from .forms import AddNewbieForm


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


# We can allow the user/client to give us data through the route.
@app.route("/<name>/<int:rating>", methods=['GET'])
def welcome(name, rating):
    return render_template('welcome.html', name=name, rating=rating)


@app.route("/newbies", methods=['GET'])
def view_newbies():
    """View all newbies."""
    # Get all the newbies from the database
    newbies = Newbie.query.all()
    # Pass it to the frontend
    return render_template('newbies.html', newbies=newbies)

@app.route("/newbies/delete/<int:newbie_id>", methods=['GET'])
def delete_newbie(newbie_id):
    """Delete newbie."""
    newbie = Newbie.query.get(newbie_id)
    if newbie is not None:
        db.session.delete(newbie)
        db.session.commit()
    return redirect('/newbies')

# Note that in methods we also added 'POST'. This allows the client to send info
# back to the server.
@app.route("/newbies/add", methods=['GET', 'POST'])
def add_newbies():
    """Add a new newbie."""
    # First we create a new form
    form = AddNewbieForm()
    # If the form is validated:
    if form.validate_on_submit():
        # Create a new Newbie based on the data in the form
        newbie = Newbie(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            year=form.year.data
        )
        # Add and commit the data to the database
        db.session.add(newbie)
        # Data must be committed or it won't actually show up
        db.session.commit()
        return redirect('/newbies')
    # Here we specify which template to be rendered and the form we want to use
    return render_template('add_newbie.html', form=form)
