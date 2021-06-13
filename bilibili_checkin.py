import urllib.request as rq
from urllib import parse
from http import cookiejar
import json
import time

def query_privilege(cookie):
    url="https://api.bilibili.com/x/vip/privilege/my"
    headers={"Cookie":cookie}
    req = rq.Request(url=url,headers=headers)
    req = rq.urlopen(req)
    req=req.read().decode('utf-8')
    print(req)

def auto_add_coins(cookie,avid):
    url="https://api.bilibili.com/x/web-interface/coin/add"
    headers={"Cookie":cookie}
    headers={"Cookie":cookie}
    data={"aid":1,"csrf":csrf,"multiply":2,"select_like":1,"cross_domain":"false"}
    data=bytes(parse.urlencode(data),encoding="utf8")
    req = rq.Request(url=url,headers=headers,data=data, method='POST')
    req = rq.urlopen(req)
    req=req.read().decode('utf-8')
    print(req)

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
    with open("test.json","w") as f:
        f.write(req)
    print(json.loads(req))

if __name__=="__main__":
    csrf="11f7a1f66167e15c1bf39c3dafa4dfb6"
    cookie="SESSDATA=85919475%2C1631504845%2C795e8%2A31"
    #get_my5B(cookie,csrf)
    get_my5B(cookie,csrf)


