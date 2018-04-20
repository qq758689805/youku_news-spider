# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoukuNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    url = scrapy.Field()            # 链接
    title = scrapy.Field()          # 标题
    thumb = scrapy.Field()          # 封面
    time = scrapy.Field()           # 时长
    num_play = scrapy.Field()       # 播放量
    num_comment = scrapy.Field()    # 评论数
