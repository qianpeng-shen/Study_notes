
y=int(input("请输入年数: "))
t=365
s=y*t
r=s//7
i=s%7
print(y,"年有",r, "周","余",i,"天")


a=int(input("当前小时为:"))
b=int(input("当前分钟为:"))
c=int(input("当前秒为:"))
e=a*3600+b*60+c
print("当前距离0:0:0:过了", e , "秒")