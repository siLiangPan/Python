#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
>pip install elasticsearch
Collecting elasticsearch
  Downloading elasticsearch-5.4.0-py2.py3-none-any.whl (58kB)
    52% |████████████████▊               | 30kB 20kB/s eta 0:00
    69% |██████████████████████▍         | 40kB 15kB/s et
    87% |████████████████████████████     | 51kB 16kB
    100% |████████████████████████████████| 61kB 19kB/s
Collecting urllib3<2.0,>=1.8 (from elasticsearch)
  Downloading urllib3-1.22-py2.py3-none-any.whl (132kB)
    38% |████████████▍                   | 51kB 9.6kB/s eta 0:00:09
    46% |██████████████▉                 | 61kB 11kB/s eta 0:00:0
    54% |█████████████████▍              | 71kB 10kB/s eta 0:0
    61% |███████████████████▉            | 81kB 12kB/s eta 0
    69% |██████████████████████▎         | 92kB 11kB/s et
    77% |████████████████████████▊       | 102kB 11kB/s
    85% |███████████████████████████▎    | 112kB 11k
    92% |█████████████████████████████▊  | 122kB 1
    100% |████████████████████████████████| 133kB 10kB/s
Installing collected packages: urllib3, elasticsearch
Successfully installed elasticsearch-5.4.0 urllib3-1.22
'''


#import sys  
import json  
#from elasticsearch import Elasticsearch  
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import sys #引用sys模块进来，并不是进行sys的第一次加载  
#import imp

# 设置编码，避免中文乱码
#imp.reload(sys) #重新加载sys  
#sys.setdefaultencoding('utf8') #调用setdefaultencoding函数
  
######################################################  
# 用于连接ES环境，查询检索小区信息，返回排名靠前10的小区信息。  
# http_auth=('es_username', 'es_passwd')  
# es_search(city,name):es_search(深圳,登科花园)  
######################################################  
  
# 连接到集群，提供节点，不一定要全部节点  
es = Elasticsearch(  
        ['xxx.xxx.xxx.xxx'],  
        http_auth=('elastic', 'passwd'),  
        port=9200  
)  
  
  
def es_search(city, name):  
    query_json = {  
        "bool": {  
            "must": {  
                "term": {  
                    "city": city  
                }  
            },  
            "must_not":{  
                "term": {  
                    "base_inf.kind":'商铺'  
                }  
            },  
            "should": [  
                {  
                    "match": {  
                        "message": name  
                    }  
                }  
            ]  
        }  
    }  
  
    source_arr = ["name",  
                  "Long_lat.lon",  
                  "Long_lat.lat",  
                  "detail_inf",  
                  "avg_price",  
                  "base_inf.kind",  
                  "base_inf.build_time"]  
  
  
    # 获取所有数据  
    res = es.search(index="st_soufang", body={"query": query_json, "_source": source_arr})
  
    # 获取第一条数据，得分最高。  
    top_10_recodes = res['hits']['hits']  
    # print json.dumps(top_10_recodes)  
    return [top_10_recodes]  
    #  
    # for item in best_recode:  
    #     if item != '_source':  
    #         print item,best_recode[item]  
  
  
if __name__ == "__main__":  
    # 测试单例  
    city = '深圳'  
    name = '东方星大厦'  
    es_search(city, name)  