import re
import sys

def getAddress(post):
    pattern=r'^\S+'
    f=open('1.txt','r')
    while True:
        data=''
        for line in f:
            if line != '\n':
                data+=line
            else:
                break
        if not data:
            break
        port=re.match(pattern,data).group()
        if post==port:
            pattern=r'address is (\S+)'
            addr=re.search(pattern,data).group(1)
            return addr
        else:
            continue

if __name__=="__main__":
    post=sys.argv[1]
    print(getAddress(post))