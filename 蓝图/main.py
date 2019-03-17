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

from goods import get_goods
from users import register
from orders import app_orders  # 导入创建的蓝图
from cart import app_cart

app = Flask(__name__)

app.route("/get_goods")(get_goods)
app.route("/register")(register)

# 注册蓝图
# app.register_blueprint(app_orders)
app.register_blueprint(app_orders, url_prefix="/orders")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route("/")
def index():
    return "index page"


if __name__ == '__main__':
    print('====', app.url_map)  # 查看路由信息
    app.run(debug=True)



