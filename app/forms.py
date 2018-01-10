from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateTimeField,SelectField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
	search = StringField('Enter List ID', validators=[DataRequired()])
	submit = SubmitField('Search')

class TaskForm(FlaskForm):
	text = StringField('Task', validators=[DataRequired()])
	do_by = DateTimeField('Do By', validators=[DataRequired()])
	priority = SelectField('Priority', 
		                    choices=[
		                      ('Priority', 'Priority'),
													('Low', 'Low'),
													('Medium', 'Medium'),
													('High', 'High')  	
												])
	submit = SubmitField('Add Task')