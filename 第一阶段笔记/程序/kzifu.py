a=input("请输入一个字符串:")
print("第一个字符为:",a[0])
print("最后一个字符为:",a[-1])
if len(a)%2 ==0 :
    print("|")
else :
    d=len(a)//2
    
    print(a[d])