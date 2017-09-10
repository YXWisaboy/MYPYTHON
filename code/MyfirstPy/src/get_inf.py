#!/usr/bin/env Python
#coding=utf-8
import urllib.request
import re
def get_book():
    c=re.compile('<h1.*?id=".*?">(.*?)</h1>.*?<p><em>.*?</em></p>.*?<p><strong>(.*)</p>.*?<ol.*?id="page-nav">',re.S)
    for i in range(1,10):
        s=r'http://www.zysj.com.cn/lilunshuji/ziwuliuzhuzhenjing/931-5-%d.html'%i
        e=urllib.request.urlopen(s)
        book=e.read().decode('UTF-8')
        g=c.findall(book)
        print(g)
get_book()