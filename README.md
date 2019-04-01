# 准星户外广告媒体数据抓取
## 1.项目描述


&emsp;&emsp;根据准星户外媒体地图获取全国范围内准星收集的户外广告媒体详细信息。  
&emsp;&emsp;目标网站地址：http://www.xooh.com/  
## 2.运行方式
&emsp;&emsp;首先，根据城市ID获取各个城市的广告牌ID，经纬度以及sn，其中id和sn都是可以作为识别广告牌的唯一标识.  
&emsp;&emsp;运行：Xooh/xooh/run.py  

&emsp;&emsp;接着，根据广告牌sn(之前是根据ID，现已更改接口结构)拼接详单级URL，抓取广告牌详情信息.  
&emsp;&emsp;运行：Xooh/xooh/run.py   

## 3.抓取结构
item：抓取字段的定义、插入SQL语句以及查重SQL语句  

querydata：数据库查询功能，查询城市ID以及广告牌sn（ID）  

tools：数据库功能封装  

xooh：抓取代码部分，其中  
##### pipeline：  
&emsp;&emsp;分为两种，一种存储到MySQL库中，一种存储到MongoDB中，在使用之前，更改settings中相应的数据库参数（账号，密码，库名，表名等），并在settings的ITEM_PIPELINES中打开响应的Pipeline.  

##### middlewares：  
&emsp;&emsp;XoohHeadersMiddleware：使数据变为json格式  
&emsp;&emsp;XoohProxyMiddleware：代理中间件
