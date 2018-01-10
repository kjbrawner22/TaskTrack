from app import app
from app.forms import SearchForm,TaskForm
from app.models import List
from app.utils import list_exists,new_list_link,add_task
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

@app.route('/list/<link>/new-task')
def new_task(link):
	form = TaskForm()
	if form.validate_on_submit():
		if list_exists(link):
			l = get_list_by_link(link)
			add_task(text=form.text.data, do_by=form.do_by.data,
				       priority=form.priority.data, list_id=l)
			redirect(url_for('list', link=link))
		else:
			redirect(url_for('no_list', link=link))
	return render_template('new-task.html', link=link, form=form)

@app.route('/list/<link>')
def list(link):
	if not list_exists(link):
		return redirect(url_for('no_list', link=link))
	title = "Task Track | List " + link
	tasks = [
		{"text" : "test 1"},
		{"text" : "test 2"}
	]
	return render_template('list.html', 
		                     link=link, title=title, tasks=tasks)