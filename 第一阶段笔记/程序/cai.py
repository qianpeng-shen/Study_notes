
import random as R 

def mein():
    print("0) 石头")
    print("1) 剪刀")
    print("2) 布")
    print("3) 退出")

def guess_sign(sel):
    sign=["石头","剪刀","布"]
    s=[0,1,2]
    rs=R.choice(s)
    if rs==sel:
        print("平!","电脑选的是:",sign[rs],"\n  您选的是:",sign[sel])
    elif [sel,rs]==[0,1]or[sel,rs]==[1,2]or[sel,rs]==[2,0]:
        print("赢!","电脑选的是:",sign[rs],"\n  您选的是:",sign[sel])
    else :
        print("输!","电脑选的是:",sign[rs],"\n  您选的是:",sign[sel])

def main():

    while True :
        mein()
        sel=int(input("请选择:"))
        if 0<=sel<=2 :
            guess_sign(sel)
        else :
            break

main()

