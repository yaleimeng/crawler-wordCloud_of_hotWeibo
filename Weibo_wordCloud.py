# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:
@DateTime: Created on 2017/10/7，at 13:53            '''
import cv2
import jieba
from wordcloud import WordCloud,ImageColorGenerator

stop = set()
with open('./weibo1010.txt', 'r',encoding='utf-8') as f, open('./stopwords.txt', 'r',encoding='utf-8') as s:
    text = f.read()
    for line in s.readlines():
        if line[:-1] not in stop:
            stop.add(line[:-1])

# 首先使用 jieba 中文分词工具进行分词
wordlist = (jieba.cut(text, cut_all = False))  # cut_all, True为全模式，False为精确模式
wordlist_space_split = ' '.join(wordlist)  #使用空格连接区分出来的各个词语。仿照英文的风格。
src = cv2.imread('./hua.jpg')  #图片是生成词云的掩膜。
my_wordcloud = WordCloud( font_path='C:/Windows/Fonts/simkai.ttf',
                         background_color='white', max_words=130, mask=src,
                         max_font_size=250, random_state= 130, stopwords= stop,min_font_size=15
                         ).generate(wordlist_space_split)
image_colors = ImageColorGenerator(src)
my_wordcloud.recolor(color_func= image_colors)
fileName = './new_wb20.png'
my_wordcloud.to_file(fileName )
cv2.imshow('word cloud',cv2.imread(fileName))
cv2.waitKey()
