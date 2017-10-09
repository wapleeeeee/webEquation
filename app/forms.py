from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, FieldList
from wtforms.validators import DataRequired,Length,InputRequired,NumberRange

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class MyLoginForm(Form):
	username = StringField('waple', validators=[Length(min=1,max=15,message="用户名长度错误")])
	numbers = IntegerField(1, validators=[NumberRange(min=1,max=20,message="请输入1-20的整数")])

class AnswerForm(Form):
	def __init__(self, *args, **kwargs):
		kwargs['csrf_enabled'] = False
		super(AnswerForm, self).__init__(*args, **kwargs)

	answer = FieldList(StringField(validators=[DataRequired(),Length(1,10)]), label = '答案列表', min_entries=1)