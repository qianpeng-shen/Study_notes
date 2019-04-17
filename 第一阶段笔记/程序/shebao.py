
def shu():
    print("0) 进入计算")
    print("1) 退出计算")
def sum():
    s=int(input("请输入你在北京的社保基数(3082~23118):"))
    if 3082<= s <=23118:
        gy=s*0.008
        dy=s*0.19
        gh=input("户口是否为城镇(yes/no):")
        if gh=="yes" :
            gs=s*0.002
            ds=s*0.008
        else :
            gz=s*0
            dz=s*0.008
        gg=s*0
        dg=s*0.005
        ge=s*0
        de=s*0.008
        gl=s*0.02+3
        dl=s*0.1
        gj=s*0.12
        dj=s*0.12
        if gh=="yes":
            sum_g=gy+gs+gg+ge+gl+gj
            sum_d=dy+ds+dg+de+dl+dj
        else :
            sum_g=gy+gz+gg+ge+gl+gj
            sum_d=dy+dz+dg+de+dl+dj
        print("            个人缴费比例      ","  单位缴费比例  ")
        print("养老:         ",gy, "             ",dy         )
        if gh=="yes":
            print("失业(城镇):    ",gs,"             ",ds      )
        else:
            print("失业(农村):      ",gz,"             ",dz    )
        print("工伤:          ",gg,"             ",dg          )
        print("生育:          ",ge,"             ",de           )
        print("医疗:          ",gl,"             ",dl        )
        print("公积金:        ",gj,"             ",dj         )
        if gh=="yes":
            print("总和:        ",sum_g,"            ",sum_d)
        else:
            print("总和 :        ",sum_g,"            ",sum_d)
    else :
        print("输入有误，请重新选择")
def ji():
    while True:
        shu()
        p=int(input("请选择:"))
        if p==0:
            sum()
        else :
            break
ji()