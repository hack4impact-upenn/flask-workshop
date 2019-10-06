# Database Relationship Workshop

## One-To-Many Relationship Example

For this part, we're going to create a one-to-many relationship between oldies and newbie mentees. An oldie can have many newbie mentees, but a newbie only has one oldie mentor.

### Create `Oldie` model

The first thing we need to do is create an `Oldie` class. Create a file in `app/models/` called `oldie.py`:

<img src="./screenshots/database-workshop/oldie-file-location.png?raw=true" alt="Database Rows & Columns" width="150" />

Then in the file you just created, add the following code:
```py
from .. import db

class Oldie(db.Model):
    """
    Database model for our Oldie class
    """
    __tablename__ = "oldies"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    year = db.Column(db.Integer)
```

Whenever you add a new model file, you need to make sure to import it in `app/models/__init__.py` as well:

```py
# If you create a new model, you will need to import it into this file.
# This allows other parts of the application to access these models.

from .newbie import *
from .oldie import *
```

### Define the One-To-Many Relationship in `Oldie`

To specify that we want an oldie to have *many* newbie mentees, add the following line to the `Oldie` class in `app/models/oldie.py`:
```py
class Oldie(db.Model):
    ...
    # This defines a one-to-many relationship with the Newbie class!
    mentees = db.relationship('Newbie', backref='mentor')
```
* `'Newbie'` refers to the name of the model we want to build the relationship with.
* `backref='mentor'` creates a corresponding property `mentor` in the `Newbie` class that will point back to the `Oldie` mentor. For example:
```py
# Add Katie to the Oldie table
katie = Oldie(first_name='Katie', last_name='Jiang', year=2020)
db.session.add(katie); db.session.commit()

# Add Lisa to the Newbie table
lisa = Newbie(first_name='Lisa', last_name='Moshiro', year=2022)
db.session.add(lisa); db.session.commit()

# Add Lisa as one of Katie's mentees
katie.mentees = [lisa]
db.session.add(katie); db.session.commit()

# Now we can refer to `mentor` through the backref we defined earlier!
lisa.mentor == katie
# This should be True!
```

### Define the One-to-Many Relationship in `Newbie`

We also need to specify that a newbie has *one* oldie mentor. Add the following line to the `Newbie` class in `app/models/newbie.py`
```py
class Newbie(db.Model):
    ...
    # This defines a one-to-many relationship with the Oldie class
    mentor_id = db.Column(db.Integer, db.ForeignKey('oldies.id'), nullable=True)
```
* `mentor_id` stores the primary key of an entry in the `Oldie` class
* We use `db.ForeignKey` to indicate that this column refers to another "foreign" table
* `oldies.id` is the primary key of the SQL table name for Oldies: `__tablename__ = 'oldies'`

### Recreate the Database
Now that you've made all these model changes, you need to recreate the database. In terminal, run:
```sh
source venv/bin/activate
python manage.py recreate_db
```

We recommend downloading [DB Browser for SQLite](https://sqlitebrowser.org/), which allows you to open `app/flask-data.db` and inspect your database.

<img src="./screenshots/database-workshop/db-browser-tables.png?raw=true" alt="Database Rows & Columns" width="250" />

### Generate Fake Data
Add this method to `Newbie`:
```py
class Newbie(db.Model):
    ...
    @staticmethod
    def generate_fake():
        christina = Newbie(
            first_name='Christina',
            last_name='Lu',
            year=2022
        )
        lisa = Newbie(
            first_name='Lisa',
            last_name='Moshiro',
            year=2022
        )
        robin = Newbie(
            first_name='Robin',
            last_name='Tan',
            year=2022
        )
        
        for newbie in [christina, lisa, robin]:
            db.session.add(newbie)
        db.session.commit()
```

Add this method to `Oldie`:
```py
class Newbie(db.Model):
    ...
    @staticmethod
    def generate_fake():
        katie = Oldie(
            first_name='Katie',
            last_name='Jiang',
            year=2020
        )
        steph = Oldie(
            first_name='Stephanie',
            last_name='Shi',
            year=2020
        )

        db.session.add(katie)
        db.session.add(steph)
        db.session.commit()
```

Then, go to `manage.py` and add the following:
```py
...
from app.models import Newbie, Oldie

...

# Run in terminal with the command: python manage.py add_fake_data
@manager.command
def add_fake_data():
    """
    Adds fake data to the local database.
    """
    # Create some oldies and newbies
    Oldie.generate_fake()
    Newbie.generate_fake()

    # Randomly assign each newbie an oldie mentor
    import random
    oldies = Oldie.query.all()
    for newbie in Newbie.query.all():
        newbie.mentor = random.choice(oldies)
        db.session.add(newbie)
    db.session.commit()
```

Now you should be able to generate fake data by running the following command in terminal with your virtual environment activated:
```sh
python manage.py add_fake_data
```