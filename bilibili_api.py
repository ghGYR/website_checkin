import urllib.request as rq
from urllib import parse
from http import cookiejar
import json
import time
import gzip


def query_privilege(cookie):
    url="https://api.bilibili.com/x/vip/privilege/my"
    headers={"Cookie":cookie}
    req = rq.Request(url=url,headers=headers)
    req = rq.urlopen(req)
    req=req.read().decode('utf-8')
    print(req)

def auto_add_coins(cookie,csrf,avid):
    url="https://api.bilibili.com/x/web-interface/coin/add"
    headers={
    "Cookie":cookie,
    #"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #"accept-encoding": "gzip, deflate, br",
    "content-length": "94",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.39",
    "referer": "https://www.bilibili.com/video/" #必须有
}
    data={"aid":avid,"csrf":csrf,"multiply":"1","select_like":"1","cross_domain":"false"}
    data=bytes(parse.urlencode(data),encoding="utf8")
    req = rq.Request(url=url,headers=headers,data=data, method='POST')
    rep = rq.urlopen(req)
    rep=rep.read().decode('utf-8')
    return rep

def get_my5B(cookie,csrf):
    url="https://api.bilibili.com/x/vip/privilege/receive"
    headers={"Cookie":cookie}
    data={"type":1,"csrf":csrf}
    data=bytes(parse.urlencode(data),encoding="utf8")
    req = rq.Request(url=url,headers=headers,data=data, method='POST')
    req = rq.urlopen(req)
    req=req.read().decode('utf-8')
    print(req)

def get_dynamic(cookie):
    url="https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=10363537&type_list=268435455&from=weball&platform=web"
    headers={"Cookie":cookie}
    req = rq.Request(url=url,headers=headers)
    req = rq.urlopen(req)
    req=req.read().decode('utf-8')
    return req
    '''
    with open("test.json","w") as f:
        f.write(req)
    print(json.loads(req))
    '''

if __name__=="__main__":
    import sys
    csrf,cookie=sys.argv[1].split(" ")
    get_my5B(cookie,csrf)


