from flask import render_template,flash,redirect,url_for,session
from app import app
from app import homework2
from .forms import LoginForm,MyLoginForm,AnswerForm
import flask


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/index/<user>', methods = ['GET', 'POST'])
def index():
	form = MyLoginForm()
	if flask.request.method == "GET":
		return render_template("index.html",form = form)
	else:	
		if form.validate_on_submit():
			return redirect(url_for('answer',user=form.username.data,num=form.numbers.data))
		else:
			return render_template("index.html", form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = MyLoginForm()
    if form.validate_on_submit():   
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@app.route('/answer/<user>/<num>', methods = ['GET', 'POST'])
def answer(user,num):
	form = AnswerForm()
	if form.validate_on_submit():
		flash("success")
		counter = 0
		for index,entry in enumerate(form.answer.entries):
			a = "answer"+str(index+1)
			if session[a] == entry.data.strip():
				counter += 1
		return redirect(url_for('finish',correct=counter,user = user,num=num))

	flash("???")
	posts = []
	for i in range(1,1+int(num)):
		ansstring = "answer"+str(i)
		equclass = homework2.Equation()
		equclass.start()
		_Dict = {'num':i, 'equ':equclass.equ, 'ans':equclass.answer}
		posts.append(_Dict)
		session[ansstring] = str(equclass.answer)

	return render_template("answer.html",
		title = 'Answer',
		form = form,
		posts = posts)

@app.route('/finish/<user>/<num>/<correct>', methods = ['GET', 'POST'])
def finish(user,num,correct):
	return render_template('finish.html',
		user = user,
		num = num,
		correct = correct)
