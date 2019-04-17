
# for a in range(65,91):
#     print(chr(a) ,end=" ")
# else:
#     print()
x=0
for a in range(65,91):
    b=97
    q=[]
    while b<= 122:
        q+=chr(b)    
        b+=1
    print(chr(a)+q[x],end=" ")
    x+=1
    a+=1

b=int(input("请输入一个整数(10以内):"))
if 0< b <=10:
    for s in range(0,b):
        for d in range(1,b+1):
            print(s+d ,end=" ")
        print()
else:
    print("输入有错")



