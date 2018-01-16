from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,IntegerField
from wtforms_components import DateField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
	search = StringField('Enter List ID', validators=[DataRequired()])
	submit = SubmitField('Search')

class TaskForm(FlaskForm):
	text = StringField('Task', validators=[DataRequired()])
	do_by_date = DateField('Do By Date')
	do_by_time_h = IntegerField('Hour')
	do_by_time_m = IntegerField('Minute')
	priority = SelectField('Priority', 
		                    choices=[
		                      ('Priority', 'Priority'),
													('Low', 'Low'),
													('Medium', 'Medium'),
													('High', 'High')  	
												])
	submit = SubmitField('Add Task')