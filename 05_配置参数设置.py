from flask import Flask, session

app = Flask(__name__,
            static_url_path="/python",  # 访问静态资源的url前缀，默认值是static
            static_folder="static",  # 静态文件的目录，默认就是static
            template_folder="templates",  # 模板文件的目录，默认是templates
            )

# 配置参数的使用方式
# 1. 使用配置文件
# app.config.from_pyfile("config.cfg")


# # 2.使用对象配置参数
# class Config(object):
#     DEBUG = True
#
#
# app.config.from_object(Config)


# 3.直接操作config的字典对象
app.config["DEBUG"] = False


@app.route('/index')
def index():
    return "hello flask"


if __name__ == "__main__":
    app.run()


