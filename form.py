
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


"""
sets up the form that will receive and store the user's question
"""
class QuestionForm(FlaskForm):
    question = StringField('question', validators=[DataRequired()])
    submit = SubmitField('submit')
