
def ni():
    print(" 0) 进入年龄测试")
    print(" 1) 退出")
def an():
    t=int(input("请输入一个人的年龄:"))
    if 0<=t<=120:
        print("输入合法")
    else :
        print("输入不合法")

def nian():
    while True :
        ni()
        s=int(input("请选择:"))
        if s==0:
            an()
        else :
            break

nian(s)
