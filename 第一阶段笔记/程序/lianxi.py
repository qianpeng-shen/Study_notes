a=int(input("请输入一个整数:"))
t=1
while t <= a:
    print("*"*t)
    t+=1


b=int(input("请输入一个整数:"))
a=int(b)
while b>=1:
    d="*"*b
    print("%%%ds" %a %d)
    b-=1

c=int(input("请输入一个整数:"))
while c >= 1:
    print("*"*c)
    c-=1

s=int(input("请输入一个整数:"))
h=1
while s>=h:
    p="*"*h
    print("%%%ds" %s %p) 
    h+=1

 
begin=int(input("请输入一个开始的整数值:"))
end=int(input("请输入一个结束整数值:"))
print("开始值为:",begin)
print("结束值为:",end)
i=1
while begin<=end:
    print(begin,end=" ")
    if i%5==0:
        print()
    begin+=1
    i+=1

ui=65
while ui<=90:
    print(chr(ui),end=" ")
    ui+=1

ui=65
op=97
while ui<=90 and op<= 122:
    print(chr(ui)+chr(op) ,end=" ")
    ui+=1
    op+=1
