# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:获取新浪热门微博内容。保存为txt文件
@DateTime: Created on 2017/10/3，at 15:48            '''
from bs4 import BeautifulSoup as bs
import requests as rq
import  time
import random
import json
import csv

def request_page(Page):
    head = {'Accept': 'application / json, text / plain, * / *',  #将登陆后自己的cookie放在这里即可。
            'Cookie':'_T_WM=92ad429cbdf22c9524df87b0a55feefb; SUB=_2A250102iDeRhGedP4lUU-SzEyziIHXVUOFPqrDV6PUJbkd'
                     'ANLRXBkW1cStiPVBmhczc9vTY_Q7k41MP4Hw..; SUHB=05i7oALjQ5iteN; '
                     'SCF=ArLKFWAyxv5wvKrggRX2HLZuw2ZytN3pTdiiyTbXFs39Ig8BCBHMoT7sjUqb5TfNRzR9Jc3Hlo3FAIuJE4aiXqk.; '
                     'SSOLoginState=1507016178; H5_INDEX=2; H5_INDEX_TITLE=%E8%90%8C%E8%8A%BD%E8%95%BE; '
                     'H5:PWA:UID=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26fid%3D102803%26uicode%3D10000011',
            'Referer':'https://m.weibo.cn/p/index?containerid=102803',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) '
                         'Version/9.0 Mobile/13B143 Safari/601.1',
            'X-Requested-With':'XMLHttpRequest'                     }
    r = rq.get(Page,headers = head,timeout = 5)
    return r.json()

def get_text_from(page):
    js = request_page(page)
    print(len(js['cards']))
    t_list = []
    for a in range(len(js['cards'])):
        try:
            a_txt = js['cards'][a]['mblog']['text'].split('<')[0]
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