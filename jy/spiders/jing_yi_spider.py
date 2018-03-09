import scrapy
from bs4 import BeautifulSoup
import re

from jy.items import JyItem


class JingYiSpider(scrapy.Spider):
    name = 'jy'
    allowed_domains = ['bbs.125.la']
    start_urls = []
    i = 1
    while i <= 1000:
        url = 'https://bbs.125.la/forum.php?mod=forumdisplay&fid=169&sortid=214&sortid=214&page=' + str(i)
        start_urls.append(url)
        i += 1

    def parse(self, response):
        doms = BeautifulSoup(response.text, 'lxml') \
            .find_all('tbody', id=re.compile('normalthread_[0-9]+'))
        items = []
        for dom in doms:
            send_time = ''
            try:
                send_time = dom.find('tr').find('td', class_='by').find('em').find('span').find('span').get('title')
            except BaseException:
                send_time = dom.find('tr').find('td', class_='by').find('em').find('span').get_text()

            item = JyItem(name=dom.find('tr').find('th').find('a', class_='xst').get_text(),
                          url=dom.find('tr').find('th').find('a', class_='xst').get('href'),
                          classify=dom.find('tr').find('th').find_all('font')[0].get_text(),
                          over_time=dom.find('tr').find('th').find_all('font')[1].get_text().replace('　　　　　　　　 要求完成日期:',
                                                                                                     '').replace(
                              ' 　预算价格:', ''),
                          price=dom.find('tr').find('th').find_all('font')[2].get_text(),
                          send_time=send_time,
                          authot=dom.find('tr').find('td', class_='by').find('cite').find('a').get_text())
            items.append(item)
            print(item)

        return items
