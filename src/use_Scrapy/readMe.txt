
https://www.visualstudio.com/vs/community/

http://www.lfd.uci.edu/~gohlke/pythonlibs/
下载，进入.whl所在的文件夹，执行命令即可完成安装
pip install wheel
pip install 带后缀的完整文件名
pip install Twisted-17.9.0-cp35-cp35m-win_amd64.whl
pip install Scrapy‑1.4.0‑py2.py3‑none‑any.whl

Python之Scrapy爬虫框架安装及简单使用
http://www.cnblogs.com/liruihua/p/5957393.html

https://scrapy.org/download/

Scrapy入门教程
http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
http://scrapy-chs.readthedocs.io/zh_CN/latest/intro/tutorial.html#intro-tutorial

Scrapy安装介绍
pip install Scrapy 

Successfully built Twisted
Installing collected packages: Twisted, Scrapy
Successfully installed Scrapy-1.4.0 Twisted-17.9.0

2、从 http://sourceforge.net/projects/pywin32/ 安装 pywin32
请确认下载符合您系统的版本(win32或者amd64)


查看版本
C:\Users\Administrator>Scrapy version
Scrapy 1.4.0

创建Scrapy项目工程。
scrapy startproject tutorial 


2、文件目录结构如下：
解析scrapy框架结构：
scrapy.cfg: 项目的配置文件。
tutorial/: 该项目的python模块。之后您将在此加入代码。
tutorial/items.py: 项目中的item文件。
tutorial/pipelines.py: 项目中的pipelines文件。
tutorial/settings.py: 项目的设置文件。
tutorial/spiders/: 放置spider代码的目录。



http://blog.csdn.net/qq_31573519/article/details/71107162