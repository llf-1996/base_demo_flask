from flask import Flask, abort, request, Response

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    '''登录'''
    # name = request.form.get()
    # pwd = request.form.get()
    name = ''
    pwd = ''
    if name != "" or pwd != "admin":
        # 使用abort函数可以立即终止视图函数的执行
        # 并可以返回给前端特定的信息
        ## 1.传递状态码信息，必须是标准的http状态码
        # abort(404)
        ## 2. 传递响应信息
        resp = Response("login failed")
        abort(resp)
    return "login success"


if __name__ == '__main__':
    app.run(debug=True)
