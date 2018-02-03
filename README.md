# FemmeHacks Flask Workshop
Led by Katie Jiang & Aruna Prasad from Hack4Impact.

## About
A simple Flask application with routing and Jinja templates.

![Demo](/images/demo.png)

## Setup
### Clone the repository
```sh
$ git clone http://github.com/hack4impact/femmehacks-flask-workshop.git
$ cd femmehacks-flask-workshop
```
### Install a virtual environment
```sh
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
```

### Install dependencies
```sh
$ pip install -r requirements.txt
```

## Running the application
```sh
$ source env/bin/activate
$ python run.py
```
Then navigate to `http://localhost:5000/` on your preferred web browser.

## Related resources
* [FemmeHacks Python & Flask Workshop Slides](https://docs.google.com/presentation/d/1L1J1hmI3ROR3EzvYMZa2bAfZDG25WIoiY9DmAyk8zB4/edit?usp=sharing)
* [Flask-Base](http://github.com/hack4impact/flask-base) is a simple Flask boilerplate app with SQLAlchemy, Redis, User Authentication, and more. Check out our [documentation](http://hack4impact.github.io/flask-base) as well!
* [Flask documentation](http://flask.pocoo.org/)
* [Jinja documentation](http://jinja.pocoo.org/)
* [Flask extensions](http://flask.pocoo.org/extensions/)
