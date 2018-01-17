from app import db
from app.models import List,Task
import string
from datetime import datetime
from random import choice

def new_list_link(links):
	allchars = string.ascii_letters + string.digits
	link = "".join(choice(allchars) for x in range(8))
	while link in links:
		link = "".join(choice(allchars) for x in range(8))	
	l = List(link=link)
	db.session.add(l)
	db.session.commit()
	return link

def list_exists(link):
	lists = List.query.filter_by(link=link).first()
	if lists is not None:
		return True
	else:
		return False

def get_list_by_link(link):
	return List.query.filter_by(link=link).first()

def add_task(text, do_by_date, hour, minute, priority, list):
	do_by = datetime(day=do_by_date.day, month=do_by_date.month,
									 year = do_by_date.year, hour=hour,
									 minute=minute, second=0)
	t = Task(text=text, do_by=do_by,
		       priority=priority, list=list)
	db.session.add(t)
	db.session.commit()

def set_colors(tasks):
	for task in tasks:
		if task.priority == "Low":
			task.color = "green"
		if task.priority == "Medium":
			task.color = "yellow"
		if task.priority == "Medium":
			task.color = "red"
	return tasks

