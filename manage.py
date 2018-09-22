from flask_script import Manager

from app import app, db
from app.models import Newbie

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
    db.session.add(Newbie(
        first_name="Katie",
        last_name="Jiang",
        year=2020))
    db.session.add(Newbie(
        first_name="Stephanie",
        last_name="Shi",
        year=2020))
    # TODO: Try adding your own fake data here
    db.session.commit()


if __name__ == "__main__":
    manager.run()
