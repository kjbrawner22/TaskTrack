from app import app
from app.forms import SearchForm,TaskForm
from app.models import List,Task
from app.utils import list_exists,new_list_link,add_task,get_list_by_link
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

@app.route('/list/<link>/new-task', methods=['GET','POST'])
def new_task(link):
	title = "Task Track | New Task"
	form = TaskForm()
	if form.validate_on_submit():
		l = get_list_by_link(link)
		if l is not None:
			if form.priority.data == "Priority":
				form.priority.data = "None"
			add_task(text=form.text.data, do_by_date=form.do_by_date.data,
			       	 hour=form.do_by_time_h.data,minute=form.do_by_time_m.data,
			       	 priority=form.priority.data, list=l)
			return redirect(url_for('list', link=link))
		else:
			return redirect(url_for('no_list', link=link))
	print(form.errors)
	return render_template('new-task.html', link=link, form=form, title=title)

@app.route('/list/<link>')
def list(link):
	if not list_exists(link):
		return redirect(url_for('no_list', link=link))
	title = "Task Track | List " + link
	tasks = List.query.filter_by(link=link).first().tasks
	return render_template('list.html', 
		                     link=link, title=title, tasks=tasks)