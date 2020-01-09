# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
#from scrapy import log
import requests
import random
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
import pymysql
import csv
from padouban.settings import USER_AGENT
headers = {
    'Referer':'http://www.douban.com/',
    'User-Agent':USER_AGENT
}
"""
#保存入CSV文件
class CSVPipeline(object):
    def __init__(self):
        self.f = open("CSV1.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['rank', 'cover_url', 'is_playable', 'id', 'types', 'regions', 'title', 'movie_url', 'release_date','actor_count', 'vote_count','score','actors','is_watched'])

    def process_item(self, item, spider):
        CSV_list =  [item['rank'], item['cover_url'], item['is_playable'], item['id'],item['types'], item['regions'], item['title'], item['movie_url'],
                    item['release_date'], item['actor_count'], item['vote_count'],
                    item['score'],item['actors'],item['is_watched']]

        self.writer.writerow(CSV_list)
        return item
    def close_spider(self, spider):#关闭
        self.writer.close()
        self.f.close()
"""
#保存入JSON文件
#class PadoubanPipeline(object):


    #def open_spider(self, spider):
        #self.file = open('dou1.json', 'w')
    #def process_item(self, item, spider):
        #content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        #self.file.write(content)
        #return item
    #def close_spider(self, spider):
        #self.file.close()

#保存入MySQL数据库
class MySQLPipeline(object):
    def __init__(self):

        # connection database
        self.connect = pymysql.connect(host='localhost', port=3306, user='root', passwd='Wangzhenya1998',
                                        db='mysql',charset='utf8')  # 后面三个依次是数据库连接名、数据库密码、数据库名称
        #get cursor
        self.cursor = self.connect.cursor()
        print("连接数据库成功")
        #self.dbpool = adbapi.ConnectionPool("MySQLdb",
                                            #db="scrapy",  # 数据库名
                                            #user="root",  # 数据库用户名
                                            #passwd="Wangzhenya1998",  # 密码
                                            #cursorclass=MySQLdb.cursors.DictCursor,
                                            #charset="utf8",
                                            #use_unicode=False
                                               # )



    def process_item(self, item, spider):
        # sql语句

        insert_sql = "INSERT INTO doubanpachong(tk, coverurl, isplayable, id, ty, regions, title, movieurl, releasedate,ac, votecount,score,act,iswatched) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                     (item['rank'], item['cover_url'], item['is_playable'], item['id'],
                    item['types'], item['regions'], item['title'], item['movie_url'],
                    item['release_date'], item['actor_count'], item['vote_count'],
                    item['score'],item['actors'],item['is_watched'])

        # 执行插入数据到数据库操作
       # self.cursor.execute(insert_sql, (item['rank'], item['cover_url'], item['is_playable'], item['id'],
                    #item['types'], item['regions'], item['title'], item['movie_url'],
                    #item['release_date'], item['actor_count'], item['vote_count'],
                    #item['score'],item['actors'],item['is_watched']))
        # 提交，不进行提交无法保存到数据库
        self.cursor.execute(insert_sql)
        self.connect.commit()
        return item
    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()



'''
  #def process_item(self, item, spider):
      #query = self.dbpool.runInteraction(self._conditional_insert, item)
      #query.addErrback(self.handle_error)
      #return item

  #def _conditional_insert(self, tb, item):
      #tb.execute("insert into douban (rank, cover_url, is_playable, id, types, regions, title, movie_url, release_date,\
                         #actor_count, vote_count,score,actors,is_watched) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                 #(item['rank'], item['cover_url'], item['is_playable'], item['id'], \
                  #item['types'], item['regions'], item['title'], item['movie_url'], \
                 # item['release_date'], item['actor_count'], item['vote_count'],
                 # item['score'],item['actors'],item['is_watched']))
      #self.dbpool.commit()
  #def close_spider(self,spider):
     # self.
      #log.msg("Item data in db: %s" % item, level=log.DEBUG)

  #def handle_error(self, e):
      #log.err(e)
  #def get_media_requests(self, item, spider):
      #for image_url in item['cover_url']:
          #self.download_img(image_url)
      #return item
'''




