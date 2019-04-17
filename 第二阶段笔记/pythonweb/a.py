import re
import sys

def fun(a):
    f=open('1.txt','r')
    pattern=r'^\S+'
    while True:
        data=''
        for i in f:
            if i != '\n':
                data+=i
            else:
                break
        if not data:
            break
        port=re.match(pattern,data).group()
        if a==port:
            pattern=r'address is (\S+)'
            addr=re.search(pattern,data).group(1)
            return
        else:
            continue

if __name__=="__main__":
    a=sys.argv[1]
    fun(a)
