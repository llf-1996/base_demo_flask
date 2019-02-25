'''
# 安装扩展包
pip install Flask-Script

启动：
python filename runserver
python filename runserver -h 0.0.0.0 -p 6000

# 打开导入此文件后的交互器
python filename shell

>python filename --help
>python filename runserver --help
'''

from flask import Flask
from flask_script import Manager  # 启动命令的管理类

app = Flask(__name__)
# 创建Manager管理类的对象
manager = Manager(app)


@app.route('/')
def index():
    return "index page"


if __name__ == "__main__":
    # app.run(debug=True)
    # 通过管理对象来启动flask
    manager.run()

