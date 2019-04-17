def shu():
    print("闰年计算")
    print("0) 进入计算")
    print("1) 退出计算")
def shi():
    t=int(input("输入一个年份:"))
    if t%4 == 0 and t%100 !=0 :
        print("是闰年")
    elif t%400 == 0 :
        print("是闰年")
    else :
        print("是平年")
def shui():
    while True:
        shu()
        t=int(input("请选择:"))
        if t==0 :
            shi()
        else :
            break
shui()




