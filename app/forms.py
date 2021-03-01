from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired


class PhotoForm(FlaskForm):
    photo=FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','png', 'Images only!'])
    ])
    description = StringField('Description', validators=[DataRequired()])
    

    

