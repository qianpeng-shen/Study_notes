import requests
import re
import json
from multiprocessing import Pool
from multiprocessing import Manager
import time
import functools
import lianxi1
import logging
import matplotlib.pyplot as plt
logger = logging.getLogger("maoyan")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler =logging.FileHandler("maoyan.log")
file_handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

#下载页面
def get_one_page(url):
    ua_header={"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"}
    response = requests.get(url,headers=ua_header)
    if response.status_code == 200:
        return response.text
    return None
#提取信息
def parse_one_page(html):
    #使用正则提取想要的信息
    pattern = re.compile('<p class="name"[\s\S]*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern,html)
    #使用yield 把信息返回给调用者
    for item in items:
        yield{
            "title":item[0].strip(),
            "actor":item[1].strip(),
            "time":item[2].strip()
        }
#把信息保存到文件
def write_to_file(item):
    #存储成json格式,方便提取
    #　"a" 表示追加到文件,文件的一种读取方式
    with open("maoyanTop100.txt",'a',encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False)+'\n')
#将信息保存到数据库
def write_to_sql(item):
    dbhelper = myPymysql.DBHelper()
    title = item["title"]
    actor = item["actor"]
    time = item["time"]
    sql = "insert info testdb.maoyan(title,actor,time) values(%s,%s,%s);"
    params = (title,actor,time)
    if result == True:
        print("插入成功")
    else:
        logger.error("execute:"+sql)
        logger.error("params:"+params)
        print("插入失败")

#爬完一个页面之后，翻页，直到爬完为止
#http://maoyan.com/board/4?offset=90
def CrawlPage(lock,offset):
    url = "http://maoyan.com/board/4?offset="+str(offset) #将offset强转为字符串
    html = get_one_page(url)
    for item in parse_one_page(html):
        lock.acquire() #加锁，防止信息出错
        write_to_file(item)
        lock.release() #释放锁,
    time.sleep(1)
#将数据以比例的形式显示出来
def analysis():
    dbhelper = lianxi1.DBHelper()
    total = dbhelper.fetchCount("select count(*) from testdb.maoyan")
    Am = dbhelper.fetchCount("select count(*) from testdb.maoyan where time like'%美国%'")
    Ch = dbhelper.fetchCount("select count(*) from testdb.maoyan where time like'%中国%'")
    Jp = dbhelper.fetchCount("select count(*) from testdb.maoyan where time like'%日本%'")
    Other = total-Am-Ch-Jp
    sizes = Am,Ch,Jp,Other
    labels = 'America','China','Japan','Other'
    colors = 'Green','Red','Yellow','Blue'
    plt.pie(sizes,labels=labels,colors=colors)
    plt.show()
if __name__=="__main__":
    # manager = Manager()
    # lock = manager.Lock()
    # newCrawlPage = functools.partial(CrawlPage,lock)
    # pool = Pool()
    # pool.map(newCrawlPage, [i*10 for i in range(10)])
    # pool.close()
    # pool.join()
    analysis()
logger.removeHandler(file_handler)



