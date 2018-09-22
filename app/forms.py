from flask_wtf import FlaskForm
from wtforms.fields import (IntegerField, StringField, SubmitField)
from wtforms.validators import InputRequired, Length


class AddNewbieForm(FlaskForm):
    first_name = StringField('First name', validators=[InputRequired(), Length(1, 64)])
    last_name = StringField('Last name', validators=[InputRequired(), Length(1, 64)])
    year = IntegerField('Year', validators=[InputRequired()])
    submit = SubmitField('Submit')
