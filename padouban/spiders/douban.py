# -*- coding: utf-8 -*-
import scrapy
import json
import time
import random
import requests
from padouban.items import PadoubanItem

#item['image_urls'] = sel.xpath('//*[@id="mainpic"]/a/img/@src').extract()
class DoubanSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban'
    # 目标网站域名
    allowed_domains = ['movie.douban.com']
    # 起始url, 豆瓣电影分类排行榜 - 剧情片
    start_urls = ['https://movie.douban.com/j/chart/top_list?type=1&interval_id=100:90&action=&start=0&limit=180']
    url_list = []
    offset = 20
    j = 9
    def parse(self, response):
        # 接收响应加载为json
        list_data = json.loads(response.text)
        # 实例化item对象
        item = PadoubanItem()
        if not list_data:
            #item.j=0
            #for item.j in range(10):
                #item.m = 10 * item.j
                #item.n = 10 * (item.j + 1)
                #item.j=item.j+1
            #for item.s in range(20,120):
            #    item.s=+20
            # 如果list_data没有数据，则结束执行
            print("wrong")
            return

        # 从响应对象中获取指定数据并添加到字典item中
        for data in list_data:
            item['rank'] = data.get("rank")
            item['cover_url'] = data.get("cover_url")
            response = requests.get(data.get("cover_url"))
            img = response.content
            with open('C:/Users/53581/padouban/imgs/%s' % '{}.jpg'.format(data.get("title")), 'wb') as f:
                f.write(img)
            item['is_playable']=data.get("is_playable")
            item['id'] = data.get("id")

            #item['types'] = data.get("types")
            types = data.get("types")
            types=(' '.join(types))
            item['types']=types

            #item['regions'] = data.get("regions")
            regions = data.get("regions")
            regions = (' '.join(regions))
            item['regions'] = regions

            item['title'] =data.get("title")
            #title = data.get("title")
            #title = (' '.join(title))
            #item['title'] = title

            item['movie_url'] = data.get("url")
            item['release_date'] = data.get("release_date")
            item['actor_count'] = data.get("actor_count")
            item['vote_count'] = data.get("vote_count")
            item['score'] = data.get("score")

            #item['actors'] = data.get("actors")
            actors = data.get("actors")
            actors = (' '.join(actors))
            item['actors'] = actors

            item['is_watched'] = data.get("is_watched")
            # 每执行一次便生成一个字典item
            yield item


        #按照单一类型爬取
        url_list = []
        for self.j in range(9):
            m = 10*self.j
            n = 10*(self.j-1)
            url = 'https://movie.douban.com/j/chart/top_list?type=1&interval_id={}:{}&action=&start=0&limit=180'.format(m,n)
            url_list.append((url))
            time.sleep(random.randint(1, 2))
            self.j=self.j-1
            yield scrapy.Request(url=url, callback=self.parse)

        """
        #通过电影类型爬取        
        self.offset += 20
        url = 'https://movie.douban.com/explore#!type=movie&tag=热门&sort=recommend&page_limit=20&page_start={}'.format\
            (self.offset)
        time.sleep(random.randint(1, 2))
        yield scrapy.Request(url=url, callback=self.parse)
        #self.offset)  # 目标下一组数据的网址
        # 当以上代码执行结束时，使用新的url进行回调，callback即回调parse方法
        #yield scrapy.Request(url=url, callback=self.parse)
        """

"""
"rating":["9.3","50"],
"rank":1,
"cover_url":"https://img9.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p513344864.webp",
"is_playable":true,
"id":"3541415",
"types":["剧情","科幻","悬疑","冒险"],
"regions":["美国","英国"],
"title":"盗梦空间",
"url":"https:\/\/movie.douban.com\/subject\/3541415\/",
"release_date":"2010-09-01",
"actor_count":28,
"vote_count":1311687,
"score":"9.3",
"actors":["莱昂纳多·迪卡普里奥","约瑟夫·高登-莱维特","艾伦·佩吉","汤姆·哈迪","渡边谦","迪利普·劳","基里安·墨菲","汤姆·贝伦杰","玛丽昂·歌迪亚","皮特·波斯尔思韦特","迈克尔·凯恩","卢卡斯·哈斯","李太力","克莱尔·吉尔蕾","马格努斯·诺兰","泰勒·吉蕾","乔纳森·吉尔","水源士郎","冈本玉二","厄尔·卡梅伦","瑞恩·海沃德","米兰达·诺兰","拉什·费加","蒂姆·科勒赫","妲露拉·莱莉","玛格丽特·因索利亚","吉尔·马德雷尔","迈克尔·加斯顿"],
"is_watched":true},
"""