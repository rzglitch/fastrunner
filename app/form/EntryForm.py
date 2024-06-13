from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, validators


class AddEntryForm(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(min=2, max=32)
    ])
    content = TextAreaField('Content', [
        validators.DataRequired(),
        validators.Length(min=2)
    ])
    entry_metadata = TextAreaField('JSON Metadata', [
        validators.DataRequired(),
        validators.Length(min=1)
    ])
    board_name = HiddenField('board_name', [
        validators.DataRequired()
    ])


class UpdateEntryForm(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(min=2, max=32)
    ])
    content = TextAreaField('Content', [
        validators.DataRequired(),
        validators.Length(min=2)
    ])
    entry_metadata = TextAreaField('JSON Metadata', [
        validators.DataRequired(),
        validators.Length(min=1)
    ])
