from bilibili_checkin import *
import re
import json

if __name__=="__main__":
    import sys
    csrf,cookie=sys.argv[1].split(" ")
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
            req=auto_add_coins(cookie,csrf,aid)
            ret=json.loads(req)
            if ret['code']==0:
                total-=1
                print(f"{aid}")

        
    
