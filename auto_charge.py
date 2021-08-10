from bilibili_api import *

if __name__=="__main__":
    import sys
    csrf,cookie=sys.argv[1].split(" ")
    for i in range(5,1,-1):
        try:
            req=chrage(cookie,csrf,i)
            ret=json.loads(req)
            if int(ret["data"]["bp_num"])>0:
                break
        except:
            print("error")
            break