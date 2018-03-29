## 热门微博爬虫+词云
新浪热门微博爬虫，外加词云分析。</br>
用到的第三方库：
1. bs4
1. requests
1. opencv———或者用*pil+numpy*也可，网上代码大多采用这种组合。
1. jieba分词
1. wordcloud。如果Windows安装困难可在[词云](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud)下载whl然后pip。

**且爬且珍惜……**微博反爬虫机制会不定时响应超时，甚至拒绝响应。</br>
![生成的word Cloud](https://github.com/yaleimeng/crawler-wordCloud_of_hotWeibo/blob/master/pics/new_wb20.png)
