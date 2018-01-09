from app import app
from app.forms import SearchForm,TaskForm
from app.models import List
from app.utils import list_exists,new_list_link
from flask import render_template,redirect,url_for

@app.route('/', methods=['GET','POST'])
def index():
	title = "Task Track | Home"
	form = SearchForm()
	if form.validate_on_submit():
		if list_exists(form.search.data):
			return redirect(url_for('list', link=form.search.data))
		else:
			return render_template('index.html',
				                     title=title, form=form,
				                     no_result=True)
	return render_template('index.html', title=title, form=form)

@app.route('/about')
def about():
	title = "Task Track | About"
	return render_template('about.html', title=title)

@app.route('/no-list/<link>')
def no_list(link):
	return render_template('no-list.html', link=link)

@app.route('/new-list')
def new_list():
	links = List.query.all()
	for l in links:
		l = l.link
	return redirect(url_for('list', link=new_list_link(links)))

@app.route('/list/<link>')
def list(link):
	if not list_exists(link):
		return redirect(url_for('no_list', link=link))
	title = "Task Track | List " + link
	return render_template('list.html', link=link, title=title)