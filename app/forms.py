from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
  name = StringField('name', validators=[DataRequired('A name is required.')])
  email = StringField('email', validators=[DataRequired('An email is required.'), Email()])
  subject = StringField('subject', validators=[DataRequired('A subject is required.')])
  message = TextAreaField('message', validators=[DataRequired('A message is required.')])
  send = SubmitField('send')