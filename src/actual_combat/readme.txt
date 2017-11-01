项目名称
必须是高端大气上档次的名称，命名为awesome-python3-webapp。

项目计划
项目计划开发周期为16天。每天，你需要完成教程中的内容。如果你觉得编写代码难度实在太大，可以参考一下当天在GitHub上的代码。
第N天的代码在https://github.com/michaelliao/awesome-python3-webapp/tree/day-N上。比如第1天就是：
https://github.com/michaelliao/awesome-python3-webapp/tree/day-01
以此类推。


异步框架aiohttp：pip3 install aiohttp
前端模板引擎jinja2：pip3 install jinja2
MySQL的Python异步驱动程序aiomysql：pip3 install aiomysql



Day 1 - 搭建开发环境

阅读: 381986
搭建开发环境

首先，确认系统安装的Python版本是3.5.x：

$ python3 --version
Python 3.5.1
然后，用pip安装开发Web App需要的第三方库：

异步框架aiohttp：

$pip3 install aiohttp
前端模板引擎jinja2：

$ pip3 install jinja2
MySQL 5.x数据库，从官方网站下载并安装，安装完毕后，请务必牢记root口令。为避免遗忘口令，建议直接把root口令设置为password；

MySQL的Python异步驱动程序aiomysql：

$ pip3 install aiomysql
项目结构

选择一个工作目录，然后，我们建立如下的目录结构：

awesome-python3-webapp/  <-- 根目录
|
+- backup/               <-- 备份目录
|
+- conf/                 <-- 配置文件
|
+- dist/                 <-- 打包目录
|
+- www/                  <-- Web目录，存放.py文件
|  |
|  +- static/            <-- 存放静态文件
|  |
|  +- templates/         <-- 存放模板文件
|
+- ios/                  <-- 存放iOS App工程
|
+- LICENSE               <-- 代码LICENSE