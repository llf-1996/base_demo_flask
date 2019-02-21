from flask import Flask, request

app = Flask(__name__)


@app.route('/index', methods=['get', 'post'])
def index():
    return 'index page'


@app.route('/upload', methods=['post'])
def upload():
    '''接收文件'''
    file_obj = request.files.get('pic')
    if not file_obj:
        return '未上传文件'

    # 第一种：保存文件
    # f = open('./demo.jpg', 'wb')
    # data = file_obj.read()
    # f.write(data)
    # f.close()
    # 第二种保存文件
    file_obj.save('./demo1.png')

    return '上传成功'


if __name__ == '__main__':
    app.run(debug=True)



