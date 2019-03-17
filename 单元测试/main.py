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
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    #  接受参数
    username = request.form.get("username")
    passwd = request.form.get("passswd")
    # 参数判断
    if not all([username, passwd]):
        resp = {
            'code': 1,
            'message': 'invalid params'
        }
        return jsonify(resp)
    if username == "admin" and passwd == "python":
        resp = {
            "code": 0,
            "message": "login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "wrong username or passwd"
        }
        return jsonify(resp)


if __name__ == '__main__':
    print('====', app.url_map)  # 查看路由信息
    app.run(debug=True)



