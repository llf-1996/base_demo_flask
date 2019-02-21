"""
__title__ = ''
__author__ = 'llf'
__mtime__ = '...'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    print('index 被执行')
    return 'Hello World!'


@app.before_first_request
def handle_before_first_request():
    '''在第一次请求处理之前先被执行'''
    print('handle_before_first_request 被执行')


@app.before_request
def handle_before_request():
    '''在每次请求之前都被执行'''
    print("handle_before_request 被执行")


@app.after_request
def handle_after_request(response):
    '''在每次请求之后都被执行，前提是视图函数没有出现异常'''
    print("handle_after_request 被执行")
    print(response)
    print(type(response))
    return response


@app.teardown_request
def handle_teardown_request(response):
    '''在每次请求之后都被执行，无论视图函数是否出现异常，都被执行'''
    print('handle_teardown_request 被执行')
    return response


if __name__ == '__main__':
    app.run()


