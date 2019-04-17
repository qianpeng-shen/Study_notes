
def shu():
    print("0) 进入计算:")
    print("1) 退出")
def mian():
    r=float(input("请输入半径:"))
    mianji=3.14*r**2
    print("圆的面积为:",mianji)
def ji():
    while True:
        shu()
        d=int(input("请选择:"))
        if d==0:
            mian()
        else:
            break
ji()