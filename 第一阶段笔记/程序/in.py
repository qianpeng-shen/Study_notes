
def sum():
    while True:
        print("0) 进入")
        print("1) 退出")
        t=int(input("请选择:"))
        if t==0 :
            a=input("输入字符串１:")
            b=input("输入字符串2:")
            c=input("输入字符串3:")
            if len(a)>len(b) and len(a)>len(c):
                print(" "*(len(a)-len(b))+b)
                print(" "*(len(a)-len(c))+c)
                print(a)
            elif len(b)>len(a) and len(b)>len(c):
                print(" "*(len(b)-len(a))+a)
                print(" "*(len(b)-len(c))+c)
                print(b)
            else :
                print(" "*(len(c)-len(a))+a)
                print(" "*(len(c)-len(b))+b)
                print(c)
        else :
            break
sum()