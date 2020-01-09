# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PadoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影编号
    rank = scrapy.Field()
    # 电影海报url
    cover_url = scrapy.Field()
    # 图片信息
    cover = scrapy.Field()
    # 是否上映
    is_playable = scrapy.Field()
    # 电影ID
    id =scrapy.Field()
    # 电影类型
    types = scrapy.Field()
    # 电影地区
    regions = scrapy.Field()
    # 电影名
    title = scrapy.Field()
    # 详情页url
    movie_url = scrapy.Field()
    # 上映时间
    release_date = scrapy.Field()
    # 参演人数
    actor_count =scrapy.Field()
    # 评价人数
    vote_count =scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 演员
    actors =scrapy.Field()
    # 是否可观看
    is_watched =scrapy.Field()
    pass
