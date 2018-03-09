import requests
from bs4 import BeautifulSoup
import re



def get_data():
    url = "https://bbs.125.la/forum.php?mod=forumdisplay&fid=169&sortid=214&sortid=214&page=2"
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9'
    }

    res = requests.get(url, headers=headers)

    doms = BeautifulSoup(res.text, 'lxml').find_all('tbody', id=re.compile('normalthread_[0-9]+'))
    for dom in doms:
        # print(dom.find('tr').find('th').find('a', class_='xst').get('href'))
        print()

get_data()