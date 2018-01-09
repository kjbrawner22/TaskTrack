from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
	search = StringField('Enter List ID', validators=[DataRequired()])
	submit = SubmitField('Search')

class TaskForm(FlaskForm):
	text = StringField('Task', validators=[DataRequired()])
	submit = SubmitField('Submit')