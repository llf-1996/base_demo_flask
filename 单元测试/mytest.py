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
import json
import unittest

from main import app


class LoginTest(unittest.TestCase):
    '''构造单元测试'''
    def test_empty_username_password(self):
        '''测试用户名密码不完整的情况'''
        # 创建进行web请求的客户端，使用flask提供的
        client = app.test_client()
        # 利用client客户端模拟发送web请求
        ret = client.post('/login', data={})
        # ret是视图返回的响应对象，data属性是响应体的数据
        resp = ret.data
        # login视图返回的是json数据
        resp = json.loads(resp)

        # 拿到返回值后进行断言测试
        self.assertIn('code', resp)
        self.assertEqual(resp['code'], 1)


if __name__ == '__main__':
    unittest.main()

