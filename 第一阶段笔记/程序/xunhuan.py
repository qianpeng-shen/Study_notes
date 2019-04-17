
print("1) 输入字符串:")
print("2) 退出")
c=0
a=[]
while c!= 2 :
    c=int(input("请选择:"))
    if c == 1 :
        s=input("请输入一个字符串:")
        a.append(s)
ren=[]
x=''
for x in a :
    ren.append(len(x))
han=max(ren)
n=0
b=""
while a !=[]:
    for b in a :
        if len(b) <=n:

            print(b.center(han,"~"))
            a.remove(b)
    n+=1
