from flask import Flask, session

app = Flask(__name__)
# flask中session需要用到的秘钥字符串
app.config['SECRET_KEY'] = "ADFSDFSDFSFDSFDSFSSD"


@app.route('/login')
def login():
    # 设置session数据
    session["name"] = 'python'
    session['mobile'] = '18117473239'
    return 'login sucess'


@app.route('/index')
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == "__main__":
    app.run(debug=True)


