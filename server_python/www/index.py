from django.http import HttpResponse
from django.template import Template,Context
from django.db import connection as con
import os
def index(request,seg):
	print(os.path.dirname(__file__))
	f=open('index.html','r')
	content=f.read()
	tp=Template(content)
	d = run('ha')
	data={'title':'hello','content':'nice to meet','goods':d}
	c=Context(data)
	html=tp.render(c)
	#a=run(seg)
	return HttpResponse(html)

def run(act):
	cursor = con.cursor()
	cursor.execute('SELECT * FROM hr_goods limit 5')
	data=cursor.fetchall()
	return data