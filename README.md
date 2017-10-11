# webEquation
基于web的四则运算器
***
### 实现功能
- √ 记录用户的对错总数，程序退出再启动的时候，能把以前的对错数量保存并在此基础上增量计算。  
- √ 有计时功能，能显示用户开始答题后的消耗时间。  
- √ 界面支持中文简体/中文繁体/英语，用户可以选择一种。  
***
### 本地运行程序操作步骤：
1. clone webEquation到本地。
2. 开启管理员权限，并安装好pip环境。
3. 运行setup.py包，搭建flask标准环境。
4. 运行run.py，打开本地服务器。
5. 打开浏览器，输入localhost:5000即可打开页面。
***
### 说明：
setup.py中集成了flask框架所依赖的包，也可自行安装。
```
pip install flask
pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install flask-babel
pip install guess_language
pip install flipflop
pip install coverage
pip install flask_babel
```
***
博客地址：
