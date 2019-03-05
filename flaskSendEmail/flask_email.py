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
from flask_mail import Mail, Message

app = Flask(__name__)
# 配置邮件：服务器、端口、传输层安全协议、邮箱名、密码
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    # MAIL_USE_TLS=True,  # 报错
    MAIL_USE_SSL=True,  # 使用ssl安全连接
    MAIL_USERNAME="2367746876@qq.com",
    MAIL_PASSWORD='passwd'  # 邮箱授权码
)

mail = Mail(app)


@app.route('/email')
def email():
    # sender发送方， recipients 接收方列表
    msg = Message("Flask email test", sender='2367746876@qq.com', recipients=['15038712879@163.com'])
    # 邮件内容
    # msg.body = "Hello World!"
    msg.html = '''<!DOCTYPE html><html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask Send Email Test</title>
    </head>
    <body>
        <b>Hello World!</b>
        <p>good time!</p>
    </body>
    </html>
    '''
    # 发送邮件
    mail.send(msg)
    return "send eamil succeed!"


@app.route('/index')
def index():
    return "succeed!"


if __name__ == "__main__":
    app.run()
