import requests
import re
import json
from multiprocessing import Pool
from multiprocessing import Manager
import time
import functools #函数的包装器


def get_one_page(url):
    ua_header = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"}
    response = requests.get(url, headers=ua_header)
    if response.status_code == 200:#OK
       return response.text
    return None


#<em class="num"[\s\S]*?</b>([\s\S]*?)</em>[\s\S]*?</p>[\s\S]*?</style>[\s\S]*?</a>
def parse_one_page(html):
    pattern = re.compile('<em class="num"[\s\S]*?</b>([\s\S]*?)</em>[\s\S]*?<a title="([\s\S]*?)"[\s\S]*?>')
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield{
            "名称":item[1].strip(),
            "价格":item[0].strip(),
        }           


def write_to_file(item):
    with open("DogFood.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False)+'\n')


def CrawlPage(lock, offset):
    url = "https://search.yhd.com/c0-0/k力狼狗粮?cu=true&utm_source=baidu-nks&utm_medium=cpc&utm_campaign=t_262767352_baidunks&utm_term=86895147209_0_20fdeec883c64f14b0df6ea2d4e2966a#page="+str(offset)+"&sort=1"
    html = get_one_page(url)    
    for item in parse_one_page(html):
        lock.acquire()
        write_to_file(item) 
        lock.release()

    time.sleep(1)
    
     
if __name__ == "__main__":

    manager = Manager()
    lock = manager.Lock()
    newCrawlPage = functools.partial(CrawlPage, lock)    
    pool = Pool()
    pool.map(newCrawlPage, [i for i in range(1,11)])
    pool.close()
    pool.join()