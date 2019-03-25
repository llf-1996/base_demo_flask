import unittest

from ..author_book import Author, db, app


class DatabaseTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        # sqlalchemy的配置参数
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flask_test"
        db.create_all()

    def test_add_author(self):
        '''测试添加作者的数据库操作'''
        author = Author(name="zhang", email="123@qq.com", mobile="123")
        db.session.add(author)
        db.session.commit()

        result = Author.query.filter_by(name="zhang").first()

        self.assertIsNotNone(result)

    def tearDown(self):
        '''在所有的测试执行后执行，通常用来进行清理操作'''
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()

