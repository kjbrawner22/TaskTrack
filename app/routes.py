from app import app
from app.forms import SearchForm,TaskForm
from flask import render_template

@app.route('/', methods=['GET','POST'])
def index():
	title = "Task Track | Home"
	form = SearchForm()
	return render_template('index.html', title=title, form=form)

@app.route('/about')
def about():
	title = "Task Track | About"
	return render_template('about.html', title=title)

@app.route('/list/new')
def new_list():
	return render_template('list.html')

@app.route('/list/<link>')
def list(link):
	return render_template('index.html', link=link)