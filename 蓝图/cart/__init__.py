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
from flask import Blueprint

# 创建了一个蓝图, 注意：蓝图需要显式的指定模板文件和静态文件的位置，否则蓝图将默认从项目根目录的templates文件中查找文件，而且根目录的优先级大于蓝图目录的优先级。
app_cart = Blueprint("app_cart", __name__, template_folder="templates", static_folder='static')

# 在__init__.py文件被执行的时候，把视图加载进来，让蓝图与应用程序知道有视图的存在
from .views import get_cart


