

t=int(input("输入公里数:"))
d=13
a=2.3
b=2.3+1.15
if t <= 3:
    print(t,"公里收费：",d,"元")
elif t > 3 and t <= 15:
    g=(t-3)*2.3+13
    print(t,"公里收费：",round(g),"元")
elif  t > 15:
    h=(t-15)*b+(t-3)*2.3+13
    print(t,"公里收费：",round(h),"元")