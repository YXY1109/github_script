from datetime import datetime

from peewee import *

db = MySQLDatabase("wx_article", user="", password="", host="")


class Article(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    title = CharField()
    url = CharField()
    create_time = DateTimeField(default=datetime.now)
    update_time = DateTimeField(default=datetime.now)

    # https://stackoverflow.com/questions/18522600/is-there-an-auto-update-option-for-datetimefield-in-peewee-like-timestamp-in-mys
    def save(self, *args, **kwargs):
        self.update_time = datetime.now()
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        database = db


def test_db():
    # 查询
    try:
        # 存在
        article = Article.get(Article.title == "我是标题2")
        # 更新
        Article.update(url="http://baidu.com222336666", update_time=datetime.now()).where(Article.id == 1).execute()
        print("更新完成")
    except Article.DoesNotExist as e:
        # 不存在，新增数据
        article = Article(title="我是标题2",
                          url="https://www.baidu.com/s?ie=utf-89")
        article.save()
        print("新增完成")


if __name__ == '__main__':
    Article.drop_table()
    Article.create_table()
    print("创建完成")
