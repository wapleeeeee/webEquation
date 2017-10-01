#environment: Python 3.6.0 |Anaconda custom (x86_64)|

import sys
from random import randint
from random import choice

from fractions import Fraction

class Equation():
	def __init__(self):
		self.op = ["+","-","*","÷","/"]
		self.priority = {'+':1,'-':1,'*':2,'÷':2}
		self.equ = ''
		self.answer = 0

	#生成随机等式
	#@profile
	def getEquation(self):
		number = randint(2,9)
		tmpstring = ""
		tmpop = ''
		tmpint = 0
		for i in range(number):
			if tmpop == '/':            #分数情况
				tmpint = randint(tmpint+1,9)
				tmpop = choice(self.op[:-1])
			elif tmpop == '÷':          #除号情况
				tmpint = randint(1,8)
				tmpop = choice(self.op)
			else:
				tmpint = randint(0,8)
				tmpop = choice(self.op)
			#添加到算式中
			tmpstring += str(tmpint)
			tmpstring += tmpop
		tmpstring = list(tmpstring)
		#修改最后一个符号为=
		tmpstring[-1] = '='
		tmpstring = ''.join(tmpstring)

		#加括号
		finalstring = self.insertBracket(tmpstring,number)

		return finalstring

	#加括号
	#@profile
	def insertBracket(self,st,length):
		left_list = []
		right_list = []
		tmplist = list(st)
		#括号数量控制在[0,2]
		if length > 4:
			bracketNum = randint(0,2)
		elif length > 2:
			bracketNum = randint(0,1)
		else:
			bracketNum = 0
		for branum in range(bracketNum):
			left = randint(0,length-2)
			right = randint(left+1,length-1)
			#判断括号无意义情况
			judgeString = st[2*left:2*right]
			judgeleft = st[2*left-1]
			judgeright = st[2*right+1] if len(st)>2*right+1 else ''
			if (not '+' in judgeString and not '-' in judgeString) or '/' == judgeleft or '/' == judgeright:
				continue
			if (left in left_list and right in right_list) or left in right_list or right in left_list or st[left*2-1] == '÷':
				continue
			left_list.append(left)
			right_list.append(right)
		left_list.sort()
		right_list.sort()
		#插入括号
		for i in range(len(left_list)):
			tmplist.insert(2*left_list[i]+i,'(')
		for j in range(len(right_list)):
			if right_list[j] < left_list[-1]:
				tmplist.insert(2*right_list[j]+j+len(left_list),')')
			else:
				tmplist.insert(2*right_list[j]+j+len(left_list)+1,')')
		return ''.join(tmplist)


	#求算式答案
	#@profile
	def getAnswer(self,exp):
		#将带有分号的表达式化成带分数的list
		equlist = []
		i = 0
		while(i < len(exp)-1):
			if exp[i+1] != '/':
				equlist.append(exp[i])
				i += 1
			else:
				equlist.append(Fraction(int(exp[i]),int(exp[i+2])))
				i += 3
		#将中缀表达式转化为后缀
		new_equlist = self.change_list(equlist)
		#计算后缀表达式的结果
		return(self.calculate(new_equlist))

	#转化为后缀表达式
	#@profile
	def change_list(self,equation):
		tmplist = []
		stack = []
		for op in equation:
			if type(op) == str and op >= '0' and op <= '9':
				tmplist.append(int(op))
			elif type(op) != str:
				tmplist.append(op)
			elif op == ')':
				tmpTopStack = ''
				while tmpTopStack != '(':
					tmpTopStack = stack.pop()
					if tmpTopStack != '(':
						tmplist.append(tmpTopStack)
			elif len(stack) == 0 or op == '(' or stack[-1] == '(':
				stack.append(op)
			else:
				while(len(stack) > 0 and stack[-1] != '(' and self.priority[stack[-1]] >= self.priority[op]): #栈顶优先级大于等于该符号，持续出栈
					tmplist.append(stack.pop())
				stack.append(op)
		while(len(stack) != 0):
			tmplist.append(stack.pop())
		return tmplist 	

	#计算后缀表达式的结果
	#@profile
	def calculate(self,_list):
		tmpStack = []
		for tmpValue in _list:
			if type(tmpValue) != str:
				tmpStack.append(tmpValue)
			else:
				number_y = tmpStack.pop()
				number_x = tmpStack.pop()
				if tmpValue == "+":
					tmp = number_x+number_y
				elif tmpValue == "-":
					tmp = number_x-number_y
				elif tmpValue == "*":
					tmp = number_x*number_y
				else:
					tmp = Fraction(number_x,number_y)
				tmpStack.append(tmp)
		return tmpStack[0]

	#四则运算
	def plus(self,num1,num2):
		return num1+num2

	def minus(self,num1,num2):
		return num1-num2

	def multiply(self,num1,num2):
		return num1*num2

	def divide(self,num1,num2):
		return Fraction(num1,num2)

	#开始生成表达式及计算结果
	def start(self):
		self.equ = self.getEquation()
		self.answer = self.getAnswer(self.equ)

def main():
	if sys.argv[1] != "-n":
		raise IOError("Please enter the right command!")
	num = int(sys.argv[2])
	score = 0
	print("本次测试共{}题，满分100分".format(num))
	for i in range(1,num+1):
		equation = Equation()
		equation.start()
		print("-----------------------------")
		print("第{}题: {}".format(i,equation.equ),end = '')
		ans = input().strip()
		if ans == str(equation.answer):
			score += 1
			print("回答正确！：）")
		else:
			print("回答错误。：（ 正确答案：{}".format(equation.answer))
	print("-----------------------------")
	print("测试结束，本次测试得分：{}分".format(round(float(score)/float(num)*100)))

#效能测试
def performance_main():
	test_num = 100000
	for i in range(test_num):
		equation = Equation()
		equation.start()
		#print("{}{}".format(equation.equ,equation.answer))

if __name__ == '__main__':
	main()
