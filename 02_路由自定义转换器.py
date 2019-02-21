from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 1.定义自己的转换器
class RegexConverter(BaseConverter):
    ''''''
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex


# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters['re'] = RegexConverter


@app.route('/')
def index():
    return 'Index Page'


@app.route('/goods/<goods_id>')  # 不加转换器类型，默认是普通字符串规则（除了/的字符）
def goods_detail(goods_id):
    '''
    定义
    :param goods_id:
    :return:
    '''
    return "goods detail page %s" % goods_id


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


# http://127.0.0.1:5000/send/18117473239
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_sms(mobile):
    return 'send sms to %s' % mobile


if __name__ == '__main__':
    # 第一种debug
    app.debug = True
    app.run()
    # 第二种
    # app.run(debug=True)
