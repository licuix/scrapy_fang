# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pip.cmdoptions import log


class FangDBPipeline(object):
    def __init__(self):
        #从配置文件settings获取报错;
        self.connect=pymysql.connect(
            host="127.0.0.1",
            db="test",
            user="root",
            password="",
            port=3306,
            charset='utf8',
            use_unicode=True)
        self.cursor=self.connect.cursor()
    def fang_item(self,item,spider):
        try:
            self.cursor.execute(
                'select * from fang where url=%s',item['url'])
            repetition = self.cursor.fetchone()
            if repetition:
                pass
            else:
                self.cursor.execute('insert into fang (title) VALUES (%s,%s)',(item['title']))
            #提交sql语句
            self.connect.commit()
        except Exception as error:
            log(error)
        return item

