import hashlib
import threading
from collections import deque
from selenium import webdriver
import re
from lxml import etree
import time
from pybloom_live import BloomFilter
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd

user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)
def get_element_by_xpath(cur_driver, path):
    tried = 0
    while tried < 6:
        html = cur_driver.page_source
        tr = etree.HTML(html)
        elements = tr.xpath(path)
        if len(elements) == 0:
            time.sleep(1)

            continue
        return elements
download_bf = BloomFilter(1024*1024*16, 0.01)
# 两头list
cur_queue = deque()

def enqueueUrl(url):
    try:
        md5v = hashlib.md5(bytes(url,encoding='utf-8')).hexdigest()
        if md5v not in download_bf:
            #print(url + ' is added to queue')
            cur_queue.append(url)
            download_bf.add(md5v)
        # else:
            # print 'Skip %s' % (url)
    except ValueError:
        pass
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent

feeds_crawler = webdriver.PhantomJS(desired_capabilities=dcap)
feeds_crawler.set_window_size(1920, 1200)  # optional
def intoURL():
    count=0
    for k in range(1,24):
        domain = "www.zysj.com.cn/zhongyaocai/index__"+str(k)+".html"
        url_home = "http://" + domain

        feeds_crawler.get(url_home)
        sum = get_element_by_xpath(feeds_crawler, '//li/a')
        x=len(sum)
        for i in range(2,x-17):
            y="http://www.zysj.com.cn"+sum[i].get('href')
            enqueueUrl(y)
            count+=1
    print("共网址数：",count)

def tin(urlget,classid):
    sum=''
    x = urlget.find_elements_by_class_name(classid)
    if len(x) == 0:
        sum = 'NULL'
    else:
        sum = x[0].text
    return sum

def getdic(url_home):
    tried = 0
    while tried < 3:
        try:
            dic={}
            feeds_crawler.get(url_home)
            dic['药名'] = get_element_by_xpath(feeds_crawler, '//h1')[0].text
            #sum = re.findall('/([^/]+)$',feeds_crawler.find_elements_by_class_name('py')[0].text)[0];
            dic['拼音']=tin(feeds_crawler,'py')[2:]
            dic['别名'] = tin(feeds_crawler, 'bm')[2:]
            dic['出处'] = tin(feeds_crawler, 'cc')[2:]
            dic['来源'] = tin(feeds_crawler, 'ly')[2:]
            dic['原形态'] = tin(feeds_crawler, 'yxt')[3:]
            dic['生境分布'] = tin(feeds_crawler, 'sjfb')[4:]
            dic['性味'] = tin(feeds_crawler, 'xw')[2:]
            dic['功能主治'] = tin(feeds_crawler, 'gnzz')[4:]
            dic['摘录'] = tin(feeds_crawler, 'zl')[2:]
            dic['用法用量'] = tin(feeds_crawler, 'yfyl')[4:]
            dic['归经'] = tin(feeds_crawler, 'gj')[2:]
            break
        except Exception:
            tried += 1
            time.sleep(1)
    return  dic

def dequeuUrl():
    if len(cur_queue)==0:
        return False
    return cur_queue.popleft()
arr=[]
def crawl():
    count=0
    while True:
    #for h in range(10):
        url = dequeuUrl()
        if url==False:
            break
        s=getdic(url)
        arr1=[]
        for i in s:
            arr1.append(s[i])
        print(count,' ',url)
        count += 1
        arr.append(arr1)
    csv_pd = pd.DataFrame(arr)
    csv_pd.to_csv(r'C:\Users\sjzx\Desktop\test.csv', sep=',', header=False, index=False)
    print(1)

if __name__ == '__main__':
    intoURL()
    crawl()
    feeds_crawler.close()


