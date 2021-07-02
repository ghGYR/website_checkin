from bilibili_api import *

if __name__=="__main__":
    import sys
    csrf,cookie=sys.argv[1].split(" ")
    get_my5B(cookie,csrf)