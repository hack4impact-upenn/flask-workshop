from flask_wtf import FlaskForm
from wtforms.fields import (IntegerField, StringField, SubmitField)
from wtforms.validators import InputRequired, Length


class AddNewbieForm(FlaskForm):
    """
    Form for adding a Newbie to our database
    """
    # first_name is the property name in our form
    # In the template with this form, we can render this field by calling {{ form.first_name }}
    first_name = StringField(
        'First name",
        # The label displayed for this field would be 'First name'
        validators=[InputRequired(), Length(1, 64)])
        # Flask-WTF gives us validators to make sure the user has good input

    last_name = StringField(
        'Last name',
        validators=[InputRequired(), Length(1, 64)])

    year = IntegerField(
        'Year',
        validators=[InputRequired()])

    submit = SubmitField('Submit')
