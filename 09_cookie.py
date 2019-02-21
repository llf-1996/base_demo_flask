from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response('success')
    resp.set_cookie("itcast", "python")
    resp.set_cookie("itcast1", 'python1')
    # 设置cookies过期时间，单位秒
    resp.set_cookie("itcast2", "python2", max_age=3600)
    resp.headers['Set-Cookie'] = 'itcast3=python3; Expires=Sat, 02-Feb-2019 09:28:21 GMT; Max-Age=3600; Path=/'
    return resp


@app.route('/get_cookie')
def get_cookie():
    c = request.cookies.get('itcast')
    return c


@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('del success')
    # 删除cookie
    resp.delete_cookie("itcast1")
    return resp


if __name__ == '__main__':
    app.run(debug=True)


