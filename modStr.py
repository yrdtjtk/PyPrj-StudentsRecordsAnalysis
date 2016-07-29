#encoding=utf-8

# 一次完成多个字符串替换
#利用正则表达式re的sub方法

import re
def multiple_replace(text,adict):
    rx = re.compile('|'.join(map(re.escape,adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat,text) #每遇到一次匹配就会调用回调函数

if __name__ == '__main__':
    #把key做成了 |分割的内容，也就是正则表达式的OR
    map1={'1':'2','3':'4',}
    print '|'.join(map(re.escape,map1))

    str='1133'
    print multiple_replace(str,map1)