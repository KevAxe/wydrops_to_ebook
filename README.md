# wydrops_to_ebook
抓取WooYunDrops生成电子书
# 使用方法
首先，需要安装calibre，可以到http://calibre-ebook.com/download 下载对应版本。

然后运行脚本即可，使用示例：

1.不输入参数的情况

Python wydrops_to_ebook.py

默认爬取WooYunDrops上所有内容，在脚本同级目录下生成名为WooYunDrops.mobi的mobi格式电子书，文章默认排序从新到旧，如果想更改排序为从旧到新，加-r即可。

2.爬取指定页码范围文章，文章排序从旧到新，保存为azw3格式

Python wydrops_to_ebook.py -s 2 –e 9 –f azw3 –r

爬取第二页到第九页的文章，如果不指定-e参数，默认爬取起始页之后的所有文章。

3.指定搜索关键词，爬取搜索结果

Python wydrops_to_ebook.py –k sqlmap

爬取和sqlmap有关的所有文章，当然你也可以指定页码范围和排序。

4.爬取指定类别的文章，比如你只想要web安全分类下的文章，你可以点击分类链接，查看分类名称，url/后面为“web”。那么，指定-c参数为web就可以了：

Python wydrops_to_ebook.py –c web

5.可以使用-h参数查看说明。

Python wydrops_to_ebook.py –h
# 参数说明
-h 使用帮助

-t 指定电子书标题，默认为WooYunDrops

-f 指定生成电子书格式，默认为mobi，支持mobi、epub、azw3、pdf等，更多格式请查看calibre支持的格式，在此不一一列举。

-s 指定爬取起始页

-e 指定爬取结束页

-r 更改文章排序为从旧到新，不加此参数时默认排序为从新到旧

-k 指定搜索关键字

-c 指定爬取文章类别
