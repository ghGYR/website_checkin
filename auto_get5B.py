from bilibili_api import *

if __name__=="__main__":
    import sys
    parameters=json.loads(sys.argv[1])
    get_my5B(parameters["cookie"],parameters["csrf"])