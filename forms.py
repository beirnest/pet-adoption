from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(["cat", "dog", "porcupine"])])
    photo_url = StringField("URL to Picture of Pet", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(),NumberRange(min=0, max=30)])
    notes = StringField("Notes About Pet", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for updating pet details"""

    image_url = StringField("URL to Picture of Pet", validators=[Optional(), URL()])
    notes = StringField("Notes About Pet", validators=[Optional()])
    available = BooleanField("Available?", validators=[InputRequired()])
