from bilibili_api import *
import re
import json

if __name__=="__main__":
    import sys
    parameters=json.loads(sys.argv[1])
    csrf=parameters["csrf"]
    cookie=parameters["cookie"]
    get_dynamic(cookie)
    mydynmic=get_dynamic(cookie)
    pattern = re.compile(r'\\"aid\\":(\d+)')
    aids=pattern.findall(mydynmic)
    aids=set(aids)
    total=5
    for aid in aids:
        if total==0:
            break
        else:
            add_f=False
            try:
                req=auto_add_coins(cookie,csrf,aid)
                print(req)
                ret=json.loads(req)
                if ret['code']==0:
                    total-=1
                    add_f=True
            except:
                pass
            print(f"{aid}: {add_f}")

        
    
