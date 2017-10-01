from flask import render_template
from app import app
from app import homework2

@app.route('/')
@app.route('/index')

def index():
	equ = homework2.Equation()
	equ.start()
	user = {'nickname':equ.equ}
	posts = [
	{
		'author' : {'nickname':'hahaha'},
		'body' : 'hahaha body'
	},
	{
		'author' : {'nickname':'gagaga'},
		'body' : 'gagaga body'
	}
	]
	return render_template("index.html",
		title = 'Home',
		user = user,
		posts = posts)