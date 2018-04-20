import scrapy
from youku_news.items import YoukuNewsItem


class Spider(scrapy.Spider):
    name = 'youku'  # 爬虫唯一识别名
    allowed_domains = ['youku.com']  # 爬取域名范围

    # 返回初始requests
    def start_requests(self):
        yield scrapy.Request('http://news.youku.com/index/jrrm', self.parse)  # 今日热门
        yield scrapy.Request('http://news.youku.com/index/jkjs', self.parse)  # 监控纪实
        yield scrapy.Request('http://news.youku.com/index/jsqy', self.parse)  # 军事前沿

    # 解析函数
    def parse(self, response):
        for v in response.css('.v'):
            v_url = v.css('.v-link').xpath('./a/@href').re('(//v.youku.com/v_show/id_(?:[A-Za-z0-9=]+)\.html)')
            v_title = v.css('.v-link').xpath('./a/@title').extract()
            v_thumb = v.css('.v-thumb').xpath('./img/@src').extract()
            v_time = v.css('.v-time::text').extract()
            v_num_play = v.css('.v-meta-entry').xpath('./span[1]/text()').extract()
            v_num_comm = v.css('.v-meta-entry').xpath('./span[2]/text()').extract()

            yield YoukuNewsItem(url=v_url,
                                title=v_title,
                                thumb=v_thumb,
                                time=v_time,
                                num_play=v_num_play,
                                num_comment=v_num_comm)
