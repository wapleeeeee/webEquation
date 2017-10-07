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
	answer = FieldList(StringField(validators=[Length(min=1,max=10,message="输入长度错误")]), label = '答案列表', min_entries=1)