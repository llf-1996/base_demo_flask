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
from flask_sqlalchemy import SQLAlchemy

# import pymysql
#
# pymysql.install_as_MySQLdb()

app = Flask(__name__)


class Config(object):
    '''配置参数'''
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/db_flask_base_demo"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

'''
表名的常见规范
数据库名缩写_表名
tbl_表名
'''


class Role(db.Model):
    """用户角色/身份表"""
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship("User", backref='role')

    def __repr__(self):
        '''定义之后，可以让显示对象的时候更直观'''
        return "Role object: name=%s" % self.name


# 创建数据库模型类
class User(db.Model):
    '''用户表'''
    __tablename__ = "tbl_users"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))

    def __repr__(self):
        '''定义之后，可以让显示对象的时候更直观'''
        return "User object: name=%s" % self.name


if __name__ == '__main__':
    # app.run(debug=True)
    # 清除数据库里的所有数据
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name='admin')
    # session记录对象
    db.session.add(role1)
    # 提交任务到数据库
    db.session.commit()

    role2 = Role(name='stuff')
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='zhao', email='zhao@qq.com', password='zhao', role_id=role1.id)
    us2 = User(name='qian', email='qian@qq.com', password='qian', role_id=role1.id)
    us3 = User(name='sun', email='sun@qq.com', password='sun', role_id=role1.id)
    us4 = User(name='li', email='li@qq.com', password='li', role_id=role1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()

    #############
    # 查询
    # 查询所有
    Role.query.all()
    # 第二种
    db.session.query(Role).all()

    # 查询第一条数据
    Role.query.first()

    # 查询指定主键值的一条数据
    Role.query.get(2)  # 返回对象

    # 过滤
    User.query.filter_by(name='zhao').all()
    User.query.filter_by(name='zhao').first()
    User.query.filter_by(name='zhao', role_id=1).first()  # 并且
    User.query.filter(User.name=='zhao', User.role_id==1).first()   # 并且

    from sqlalchemy import or_
    User.query.filter(or_(User.name=='wang', User.email.endswith('qq.com'))).all()  # 或者

    # offset偏移 跳过几条
    User.query.offset(2).all()

    # order_by
    User.query.order_by("-id").all()  # 不推荐
    User.query.order_by(User.id.desc()).all()  # 官方推荐
    User.query.order_by(User.id.asc()).all()  # 显式升序
    User.query.order_by(User.id).all()  # 升序

    # group_by
    from sqlalchemy import func
    db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()

    # 关联查询
    ro = Role.query.get(1)
    ro.users

    user = User.query.get(1)
    user.role

    ###############
    # 修改
    # 第一种
    user = User.query.get(1)
    user.name = 'python'
    db.session.add(user)
    db.session.commit()
    # 第二种
    User.query.filter_by(name='li').update({"name": "llf", "email": "15038712879@163.com"})
    db.session.commit()

    #################
    # 删除
    user = User.query.get(3)
    db.session.delete(user)
    db.session.commit()

    db.session.remove()  # 关闭数据库连接







