def shu() :
    print("0) 石头")
    print("1) 剪刀")
    print("2) 布")
    print("3) 退出")
def guessas(sel) :
    dian=0
    if sel==dian:
        print("平!电脑出的是石头,您选的也是石头")
    elif sel==1:
        print("输!电脑出的是石头,您出的是剪刀")
    elif sel==2:
        print("赢!电脑出的是石头,您出的是布")
def ji() :
    while True:
        shu()
        sel=int(input("请选择:"))
        if 0<=sel<=2:
            guessas(sel)
        else :
            break
ji()