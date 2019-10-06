# Flask Workshop

## About
A simple Flask application with routing and Jinja templates. Accompanying slides can be found [here](https://docs.google.com/presentation/d/1dbVouOH3zPJ6qISXl_Wzu1y4d9quf17YDtIX9eNoMMg/edit#slide=id.g32b928dd89_0_0).

![Demo](/images/demo.png)

## Setup
### Clone the repository
```sh
git clone http://github.com/hack4impact/flask-workshop.git
cd flask-workshop
```
If you do not have git installed on your computer, you can also download the .zip file.

### Install Python
[Tutorial](http://docs.python-guide.org/en/latest/starting/installation/)

[Another tutorial](https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html)

[Modifying your PATH environment variable](https://www.java.com/en/download/help/path.xml)

### Install Pip
If you do not have pip already installed on your computer, follow [this tutorial](https://pip.pypa.io/en/stable/installing/) to install pip.

### Install a virtual environment
```sh
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

### Install dependencies
```sh
pip install -r requirements.txt
```

## Creating the database
```sh
python manage.py recreate_db
python manage.py add_fake_data
```

## Running the application
```sh
source venv/bin/activate
python run.py
```
Then navigate to `http://localhost:5000/` on your preferred web browser.

## Exiting the virtual environmment
```sh
deactivate
```

## Related resources
* [Flask Workshop Slides](https://docs.google.com/presentation/d/1dbVouOH3zPJ6qISXl_Wzu1y4d9quf17YDtIX9eNoMMg/edit#slide=id.g32b928dd89_0_0)
* [Flask-Base](http://github.com/hack4impact/flask-base) is a simple Flask boilerplate app with SQLAlchemy, Redis, User Authentication, and more. Check out our [documentation](http://hack4impact.github.io/flask-base) as well!
* [Flask documentation](http://flask.pocoo.org/)
* [Jinja documentation](http://jinja.pocoo.org/)
* [Flask extensions](http://flask.pocoo.org/extensions/)

## Tinkering
1. Play around with the templates.
   * Try changing the text, color, etc. and see what happens!
2. Add new routes.
   * Add a new route `/noonoos` in `views.py` that will render `newbies.html`.
   * Add a new route `/newbiesf19` in `views.py` that redirects to `/newbies`.
      * Think about how these two might be different!
3. Create a new template and a new route.
   * Create a new template `bootcamp.html`. Put any HTML you want there (feel free to copy paste `index.html`!)
   * Create a new route `/bootcamp` in `views.py`.

## Recording Every Newbie's Favorite Snack
1. Add a new column to the `Newbie` model.
   * Add a column called `fave_snack` in `newbie.py`. This should be of type `String`.
      * Since you modified the database, you'll need to recreate the database. This can be done by running `python manage.py recreate_db`.
2. Now that you've added a new column to `Newbies`, you'll need to change the form so that `fave_snack` can be inputed as well.
   * Add a `StringField` called `fave_snack` to `AddNewbieForm` in `forms.py`.
3. Next, you need to update the frontend for the form so that a user can actually input this new information.
   * In `add_newbie.html`, render the new field you just added to `AddNewbieForm`.
4. This additional information needs to be added to the database once a user submits the form.
   * Edit `add_newbies()` in `views.py` to also include the new `fave_snack` data.
5. Display this new information.
   * Edit `newbies.html` to also display every newbie's `fave_snack` as well.

## Database Relationships Workshop
Learn about one-to-many and many-to-many relationships in the database-workshop branch by following [this guide](https://github.com/hack4impact/flask-workshop/blob/database-workshop/database-workshop.md). To view the example code:
```
git pull
git checkout database-workshop
```
