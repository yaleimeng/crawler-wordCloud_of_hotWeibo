# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:获取新浪热门微博内容。保存为txt文件
@DateTime: Created on 2017/10/3，at 15:48   '''
from bs4 import BeautifulSoup as bs
import requests as rq
import  time
import random
import json
import csv

def request_page(Page):
    head = {'Accept': 'application / json, text / plain, * / *', 
            'Cookie':'_T_WM=92ad429cbdf22c; M_WEIBOCN_PARAMS=3D10000011'   #将登陆后自己的cookie粘贴在这里即可。
            'Referer':'https://m.weibo.cn/p/index?containerid=102803',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) '
                         'Version/9.0 Mobile/13B143 Safari/601.1',
            'X-Requested-With':'XMLHttpRequest'                     }
    r = rq.get(Page,headers = head,timeout = 5)
    return r.json()

def get_text_from(page):
    js = request_page(page)
    cards = js.get('data').get('cards')
    print(len(cards))
    t_list = []
    if not cards:
        return t_list
    for a in range(len(js['data']['cards'])):
        try:
            a_txt = js['data']['cards'][a]['mblog']['text'].split('<')[0]
            # pub_time = js['cards'][a]['mblog']['created_at']
            # a_pic = js['cards'][a]['mblog'].get('original_pic')
            t_list.append(a_txt)
        except Exception as ex:
            print(ex)
    return t_list

#延迟刷新访问，可能存在微博内容重复的问题。需要注意去重。
url_list = ['https://m.weibo.cn/api/container/getIndex?containerid=102803&since_id={}'.format(str(i))
            for i in range(0,1000)]

#如果要批量访问，循环访问列表的url即可。注意访问间隔不能太短。小心被封号
for i, url in enumerate(url_list,1):
    mylist = get_text_from(url)
    print('当前第%d页'%i,mylist)
    with open('E:/weibo1010.txt', 'a',encoding= 'utf-8')as f:
        for my in mylist:
            f.write(my)
            f.write('\n')
    time.sleep(random.uniform(1.2,3.0))
print('恭喜，程序运行完毕！')
