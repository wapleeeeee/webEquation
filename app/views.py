from flask import render_template,flash,redirect,url_for,session
from app import app
from app import homework2,db,models
from .forms import LoginForm,MyLoginForm,AnswerForm
import flask
from time import time as ti

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/index/<user>', methods = ['GET', 'POST'])
def index():
	form = MyLoginForm()
	if flask.request.method == "GET":
		return render_template("index.html",form = form)
	else:	
		if form.validate_on_submit():
			session["name"] = form.username.data
			return redirect(url_for('answer',user=form.username.data,num=form.numbers.data))
		else:
			return render_template("index.html", form = form)

@app.route('/hisScore', methods = ['GET', 'POST'])
def hisScore():
	if session.get("name",'') and models.User.query.filter_by(nickname = session.get("name",'')).all():
		user_db = models.User.query.filter_by(nickname = session.get("name",'')).first()
		return render_template('hisScore.html',
			user = user_db.nickname,
			count = user_db.numberOfQuestions,
			correct = user_db.correct,
			takeTime = user_db.time)
	else:
		flash("请输入用户名且至少完成一次答题")
		return redirect(url_for('index'))



@app.route('/answer/<user>/<num>', methods = ['GET', 'POST'])
def answer(user,num):
	form = AnswerForm()
	if form.validate_on_submit():
		time = int(ti())-session["starttime"]
		counter = 0
		for index,entry in enumerate(form.answer.entries):
			a = "answer_"+str(index+1)
			if session[a] == entry.data:
				counter += 1
		#整理数据库
		#如果存在记录
		if models.User.query.filter_by(nickname = user).all():
			old_db = models.User.query.filter_by(nickname = user).first()
			old_db.numberOfQuestions = int(num) + old_db.numberOfQuestions
			old_db.correct = counter + old_db.correct
			old_db.time = time + old_db.time
			db.session.add(old_db)
		else:
			u = models.User(nickname = user,numberOfQuestions = num,correct = counter,time = time)
			db.session.add(u)
		db.session.commit()

		return redirect(url_for('finish',correct=counter,user = user,num=num,time=time))

	posts = []
	for i in range(1,1+int(num)):
		ansstring = "answer_"+str(i)
		equclass = homework2.Equation()
		equclass.start()
		_Dict = {'num':i, 'equ':equclass.equ, 'ans':equclass.answer}
		posts.append(_Dict)
		session[ansstring] = str(equclass.answer)

	session["starttime"] = int(ti())
	return render_template("answer.html",
		title = 'Answer',
		form = form,
		posts = posts)

@app.route('/finish/<user>/<num>/<correct>/<time>', methods = ['GET', 'POST'])
def finish(user,num,correct,time):
	return render_template('finish.html',
		user = user,
		num = num,
		correct = correct,
		time = time)
