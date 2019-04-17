
a=int(input("请输入数字1:"))
b=int(input("请输入数字２:"))
c=int(input("请输入数字3:"))
if c<a>b and b>c :
    print("顺序依次为:",a,b,c)
elif c<a>b and c>b :
    print("顺序依次为:",a,c,b)

elif a<b>c and a>c:
    print("顺序依次为:",b,a,c)
elif a<b>c and c>a :
    print("顺序依次为:",b,c,a)
elif a<c>b:
    if a>b:
        print("顺序依次为:",c,a,b)
    elif b>a:
        print("顺序依次为:",c,b,a)