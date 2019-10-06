from flask_script import Manager

from app import app, db
from app.models import Newbie, Oldie, Snack

import random

manager = Manager(app)


# Run in terminal with the command: python manage.py recreate_db
@manager.command
def recreate_db():
    """
    Recreates a local database.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


# Run in terminal with the command: python manage.py add_fake_data
@manager.command
def add_fake_data():
    """
    Adds fake data to the local database.
    """
    # Create some oldies, newbies, and snacks
    Oldie.generate_fake()
    Newbie.generate_fake()
    Snack.generate_fake()

    # Randomly assign each newbie an oldie mentor and
    # two favorite snacks
    oldies = Oldie.query.all()
    snacks = Snack.query.all()
    for newbie in Newbie.query.all():
        newbie.mentor = random.choice(oldies)
        newbie.favorite_snacks = random.sample(snacks, 2)
        db.session.add(newbie)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
