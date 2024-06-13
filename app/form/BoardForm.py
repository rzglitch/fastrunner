from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class CreateBoardForm(FlaskForm):
    name = StringField('Board name', [
        validators.DataRequired(),
        validators.Length(min=2, max=32)
    ])
    display_name = StringField('Display name', [
        validators.DataRequired(),
        validators.Length(min=2, max=32)
    ])
    description = TextAreaField('Description', [
        validators.DataRequired(),
        validators.Length(min=1, max=140)
    ])
