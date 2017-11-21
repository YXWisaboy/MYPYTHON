import re
import urllib.request
from lxml import etree

url = 'http://weibo.com/p/1003061266321801/follow?from=page_100306&wvr=6&mod=headfollow#place'

res = urllib.request.urlopen(url)
html = res.read()

f = open('follows.html', 'wb')
f.write(html)
f.close()

tr = etree.HTML(html)

for user_element in tr.xpath('//*[contains(@class, "follow_item")]'):
    user_link = user_element.xpath('.//div[contains(@class,"info_name")]/a')[0]
    print(re.findall('(.+)\?', user_link.get('href'))[0])
    print(user_element.text)