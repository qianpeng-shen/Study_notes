# begin=int(input("请输入开始值:"))
# seop=int(input("请输入一个结束值:"))
# a=" "
# for s in range(begin,seop):
#     a+=chr(s)
# print(a)
   
# 输入:2
#  *
# ***
#  *
#  *

# g=int(input("请输入一个整数:"))
# i=1
# p=1
# while i <= g*2-1:
#     r="*"*i
#     print(r.center(g*2-1))
#     i+=2
# while p<=g:
#     d="*"
#     print(d.center(g*2-1))
#     p+=1
# 3.输入如下圣诞树：
# 输入：３
# 　　1
#  222
# 33333
#   *
#   *
# #   *
# r=int(input("请输入一个整数:"))
# i=1
# a=1
# e=1
# while i <= r*2-1:
#     d=(str(a))*i
#     print(d.center(r*2-1))
#     i+=2
#     a+=1
# while e <= r:
#     z="*"
#     print(z.center(r*2-1))
#     e+=1
# 4.输入一个正整数，打印这个数是否是素数
# 素数也叫质数，只能被1和自身整除
# 如：
# 请输入：５
# # ５　是素数


# for i in [9,8]:
#     for j in [1,2,3]:

#         print(i,j)
#         break
#     else:
#         print("for-j")
# else:

#     print("for-i")
# for a in 'python':
#     if a=='h':
#         continue
# #     print(a)
# s=10
# while s>0:
#     s-=1
#     if s==5:
#         continue
#     print(s)
# print(d)
# d=input("shuru:")
# s=list(d)

# print(s[1])
# f=list([1,2,3,4])
# print(f)
# １）打印这些数的和
# ２）打印这些数的最大数和第二大数
# ３）删除最小的一个数
# ４）按原来输入的顺序打印出剩余的这些数
# a=[]
# d=[]
# while True:
#     s=int(input("请输入一个正整数:"))
#     if s<0:
#         break
#     a.append(s)
# print(a)
# d=a.copy()
# print(d)
# print(sum(a))
# a.sort(reverse=False)
# print(a[-1],a[-2])
# p=a.pop(0)
# d.remove(p)
# print(d)
# a=int(input("请输入一个开始数:"))
# b=int(input("请输入一个结束数:"))
# f=[x for x in range(a,b) if (x**2+1) % 5 == 0]
# # # print(f)
# c=[]
# n=int(input("请输入:"))
# for x in range(1,n):
#     if x>=2:
#         for y in range(2,x):
#             if x%y==0:
#                 break
#             else:
#                 c.append(x)
# # print(c)
# print(sum(c))

# ２．求100以内有哪些整数与自身加1　的乘积再对11求余的结果等于8
# # 打印这些数，将这些数存入列表当中(建议用列表推导式
# a=[x for x in range(1,101) if ((x+1)*x)%11==8]
# print(a)
# # ３．计算20百斐波那契数(fabonacci数)
# 存于列表中，最后打印这20个数
# # 1,1,2,3,5,8,13,...
# # # (从第三个数起，后一个数是前两个数之和)
# d=[1,1,2] 
# i=1
# a=2
# while i<18:
#     f=d[i]+d[ a]
#     d.append(f)
#     i+=1
#     a+=1
# print(d)

# n=int(input("输入一个数:"))
# x=1
# for a in range(1,n+1):
#     if x<=n:
#     d=str(x)*(2*a-1)
#     f=" "*(n-a)
#     print(f+d)
#     x+=1
#     else:
#         print("s")

# s1="welcome to china"
# # L=s.split(' ') # L=['Beijing, is, capital']
# l=s1.split(" ")
# print(l)
# s2=['hello','tar','gz']
# s='.'.join(s2)
# # print(s)
# s="python2best"

# s=['df ' ,'dfjk' ,1 , 'fjk' ]
# a="hello wolrd"
# s1=[3,4,5,2]
# # s2=",".join(s)
# # li=list(s2)
# # print(li)
# s2=list(s)

# print(s2)
# s2=list(s[0:6])+list(s1[0:1])
# s2[len(s2)-4]=3
# print(s2)
# s2[6:]="3"
# print(s2)
# s2.append("!")
# print(s2)
# s3=len(s2)
# print(s3)
# r=s2.pop(-2)
# print(s2)
# s2.clear()
# print(s2)
# print(sum(s1))
# s1.sort(reverse=False)
# print(s1)
# s1.reverse()
# print(s1)

# for x in range(2,10):
#     for   in range(2,x):
#         if x%y==0:
#             print(x)
#             break
# s=[]
# a=0
# while True:
#     d=int(input("输入一个数:"))
#     s.append(d)
#     a+=1
#     if a==10:
#         break
# i=0
# c=sum(s)/10
# for z in s:
#     if z>c:
#         i+=1
# print(i)
# print(c)

# s=[]
# q=0
# while True:
#     a=int(input("输入一个数:"))
#     s.append(a)
#     q+=1
#     if q==20:
#        break
# i=0
# ag=0
# ji=[]
# for r in s:
#     if r<0:
#         ag+=1


#     if r>0:
#         ji.append(r)
#         i+=1

# sd=sum(ji)/i
# print(round(sd))
# print(ag)
# q=[]
# w=[]
# a=int(input("输入一个数:"))
# b=int(input("输入一个数:"))
# for s in range(1,a+1):
#     if a%s==0 and b%s==0:
#         q.append(s)
#     if a//s==0 and b//s==0:
#         print(s)

# print("最大公约数",q[-1])
# print("最小公倍数:")









# a=input("输入字符串:")
# # b=" "
# # for x in a:
# #     if x != " ":
# #         b+=x
# # for d in reversed(b):
# #     print(d,end=""'')
# # print()

# s=a.split()
# s2=''.join(s)
# s2=s2[::-1]
# print(s2)
# l=[]
# a=1
# b=1
# l.append(a)
# l.append(b)
# while len(l)<20:
#     c=a+b         
#     l.append(c)   
#     a=b          
#     b=c           
# print(l)

# g=[]
# for x in range(100,1000):
#     d=str(x)
#     a=list(d)
#     if x==int(a[0])**3+int(a[1])**3+int(a[2])**3:
#         g.append(x) 
# print(g)
# 任意输入一些大于零的数，存于列表中l，当输入-1时结束输入
# 1)打印出这些数
# 2)打印出这些数的和
# 3)去掉列表中重复的数再次存入列表l1中
# 4)打印l1列表中数据的和
# 5)将l列表中，出现两次的数存到另一个列表l3中
# o=[]
# d=[]
# iu=[]
# er=[]
# while True:
#     a1=int(input("请输入一个大于零的数(-1 退出):"))
#     if a1==-1:
#         break
#     d.append(a1)
# print("这些数为:",d)
# print("和为",sum(d))

# # L.count(x)              返回列表中元素的个数 
# for a in d:
#     if d.count(a)==1:
#         o.append(a)
#     elif d.count(a)==2:
#         er.append(a)
#         d.remove(a)
#     elif d.count(a) >= 2:
#         num=d.count(a)
#         iu.append(a)
#         i=1
#         while i<=num:
#             d.remove(a)
#             i+=1

# print(o)
# poi=o+iu    
# print(poi)
# print(sum(poi))
# print(er)

# t=(20,30,40,50,40,30,20)

# f=dict(name="as",age=15)
# print(t.count(30))
# d={"name":"bob","age":30}
# d["score"]=90
# d["age"]=25
# print(d)
# print(d["age"])
# a=dict([("name","xioawei"),("age",63)])
# print(a)
# print(f)
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             for d in range(2):
#                 for e in range(2):
#                     for f in range(2):
#                         if a+b>=1 and a!=d and a+e+f==2 and b==c and c!=d and d==e:
#                             print(a,b,c,d,e,f)

# d={"1":"星期一","2":"星期二","3":"星期三","4":"星期四","0":"星期五","6":"星期六","0":"星期日","一":"星期一","二":"星期二","三":"星期三","四":"星期四","五":"星期五","六":"星期六","日":"星期日"}
# a=str(input("输入字符:"))
# if a in d:
#     print(a)

# a=["tarena","xiaozhang","hello"]
# for x in a:
#     d.append(len(x))
# df={ x : len(x) for x in a }
# print(df)


# # df={a[0]:d[0],a[1]:d[1],a[2]:d[2]}
# # print(df)
# 语法：
# {键表达式：值表达式　for 变量　in 可迭代对象[if 真值表达式]}
# 注[]的内容可以省略


# n=[1001,1002,1003,1004]
# name=['tom','jerry','spike','tyke']
# asdf={ n[x]:name[x]  for x in range(len(n)) }
# print(asdf)

# jingli={"曹操","刘备","周瑜"}
# jishuyuan={"曹操","周瑜","张飞","赵云"}
# print(jingli & jishuyuan)
# print(jingli-jishuyuan)
# print(jishuyuan-jingli)
# print( "是"if "张飞"in jingli else "不是")
# print(jishuyuan^jingli)
# print( " gonyou%d"  % len(jingli | jishuyuan))
# a=input("输入字符串:")
# b=set(a)
# print(" ".join(b))
# c=input("输入字符串:")
# d=list(c)
# for s in d:
#     print(d.count(s),s)
#     if d.count(s)>=2:
#         num=d.count(s)
#         i=1
#         while num>=i:
#             d.remove(s)
#             i+=1
# a=input("输入字符串:")
# l=[]
# for x in a:
#     if x not in l:
#         l.append(x)
# print(l)
# d=input("输入字符串:")
# a=set(d)
# for x in a:
#     print(x,d.count(x))
# a=1
# for x in range(1,10):
#     a=(a+1)*2
# print(a)
# # ２．完全数
# 1+2+3=6(6为完全数)
# 1,2,3都为6的因数(能被一个数x整除的数为y,则y为x的因数)
# 1*6=6
# 2*3=6
# 完全数是指除本身以外的所有的因数之和相加等于自身的数
# 求4~5个完全数，并打印出来
# 6  28  496  8128

# for x in range(1,100000):
#     l=[]
#     for a in range(1,x):
#         if x%a==0:
#             l.append(a)
#     if x == sum(l):
#         print(x)
# 3.任意输入一个n代表三角形的高度，打印此形状的三角形
# 如：输入：4
# 打印如下:
#    1
#   121
#  12321
# 1234321
# a=int(input("请输入:"))
# l=[]
# for i in range(1,a+1):
#     l.append(i)
#     print((a-i)*' ',end='')
#     for x in l: 
#         print(str(x),end="")
#     for d in l[-2: :-1]:
#         print(d,end="")
#     print()
# ds=1
# while ds<a:
#     l.pop()
#     print((ds)*" ",end="")
#     for r in l:
#         print(r,end="")
#     for o in l[-2::-1]:
#         print(o,end="")
#     print()
#     ds+=1

# n=int(input("输入一个数:"))
# for x in range(1,n+1):
#     a=""
#     b=""
#     for p in range(1,x+1):
#         a+=str(p)
#     while p >1 :
#         p-=1
#         b=str(p)
#         a+=b 
#     print(a.center((2*n-1)," "))
# i=1
# kl=n
# while i<n:
#     for sd in range(1,kl):
#         fi=""
#         jk=""
#         sd+=1
#     for gh in range(1,sd):
#         fi+=str(gh)
#     while gh>1:
#         gh-=1
#         jk=str(gh)
#         fi+=jk
#     print(fi.center((2*n-1)," "))
#     i+=1
#     kl-=1


# moe=int(input("输入金额:"))
# ay=moe-20 if moe>=100 else moe
# print(ay)
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if x==y or x==z or y==z :
#                 continue
#             print(x,y,z)

# i=2
# while i>=0 :
#     a=int(input("请输入登录密码:"))
#     b=str(a)
#     if b[0]=="5" and b[1]=="9" and b[2]=="2":
#         print("恭喜你答对了，进入程序")
#         break
#     elif i==0:
#         print("输入错误，请在等十分钟")
#         break
#     else:
#         print("还有",i,"此机会")
#     i-=1


# s=int(input("shu:"))
# d=str(s)
# print(d[0])
# def say_hello():
#     print("hello world")
#     print("hello tarena")
#     print("hello everyone")

# say_hello()

# def mymax(a,b):
#     if a>b:
#         print("最大的数是:",a)
#     else:
#         print("最大的数是:",b)

# mymax(100,200)

# mymax(1+5,5+9)
# mymax("ACD"，"ABCD")
# def mysum(x, y):
#     print(x + y)


# mysum(10, 20)

# def print_even(n):
#     for s in range(n):
#         if s % 2 != 0:
#             continue
#         else:
#             print(s,end=" ")
#     print()


# print_even(10)
# def test():
#     x=100
#     print(y)
# y=200  


# test()

# print(x) 
# def hello():
#     print("hello aaa")
#     print("hello bbb")
#     return[2,3] # 用于返回到调用的地方
#     print("hello ccc")

# v=hello()
# print(v)

# def mymax(a,b):
#     if a>b:
#         s=a
#     else:
#         s=b
    
#     return s

# print(mymax(10,20))
# print(mymax("acd","abcd"))


# def input_number():
#     s=[]
#     while True:
#         a=int(input("输入数:"))
        
#         if a<0:
#             break
#         s.append(a)
#     return s   

# l=input_number()
# print(sum(l))
# print(max(l))

# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             for d in range(2):
#                 if a !=1 and c==1 and d==1 and d != 1:
#                     print(a,b,c,d)
# def input_number():
#     s=[]   
#     while True:
#         a=int(input("输入数:"))
#         s.append(a)
#         if a<0:
#             return s
#         s.append(a) 
    

# l=input_number()
# print(sum(l))
# print(max(l))
# def info(name,age=1,address="不详"):
#     print("我叫",name,"我今年",age,"岁,家庭地址:",address)

# info("张飞",30,"中原")
# info("Tarena",10)
# info("赵云")

# def func(*args):
#     print("实参个数是:",len(args))
#     print("args的值是:",args)


# func(1,2,3)
# func(4,5,6)

# def myfun(a,*,k):
#     print("a=", a)
#     print("k=", k)

# # myfun(100,200) 
# myfun(100,k=200) 

# sdef func(**kwargs):
#     print("关键字传参的个数是:",len(kwargs))
#     print("kwargs=",kwargs)


# func(name="tarena",age=15)
# func(a=1,b="BBBB",c=[2,3,4],d=True)
# def sum_d(*arg):
#     return sum(arg)


# print(sum_d(1,2,3,4,5,6,))

# def max_ra(*agr):
#     a=[]
#     for s in agr:
#         a.append(s)
#     b=a[0]
#     for s in range(len(a)):
#         if a[s]>b :
#             b=a[s]
           
#     return b

# d=[4,5,7,8]
# print(max_ra(*d))
# print(max_ra(100,200))
# print(max_ra(1,3,9,7,5))

# ３．写一个函数minmax,可以给出任意个数字实参，返回这些实参的最大数和最小数，要求两个数字形成元组后返回(最小数在前，最大数在后)调用此函数，能得到实参的最小值和最大值
# def minmax(...):

# xiao,da=minmax(5,7,9,3,1)
# print("最小数是:",xiao)
# print("最大数是",da)

# def minmax(*agr):
#     a=[]
#     for s in agr:
#         a.append(s)
#     a.sort(reverse=False)
#     xiao=a[0]
#     da=a[-1]
#     return(xiao,da)
# x,y=minmax(9,6,3,5,2,45)
# print(x)
# print(y)



# def my(x):
#     if x>0:
#         print("zheng")
#         return x
#     else:
#         return x
#         print("fu")

# print(my(5))
# print(-1)
# def my(a,b,c):
#     print(a,b,c)



# my(1,2,3)



# my(*[4,5,6])


# my(a=41,c=98,b=52)

# my(**{"a":411,"b":562,"c":856})
# def f1(lst=[]):
#     print("f1函数被调用")
# f1()
# f1=None
# # f1()　# 出错

# def f1():
#     print("hello")
# def f1():
#     print("world")

# del f1
# f1()
# def f1():# f1=函数f1
#     print("f1函数被调用")
# def f2():# f2=函数f2
#     print("f2函数被调用")

# def fx(fn):# fn=函数fn
#     print("fn绑定的函数是:",fn)
#     # 在fx内调用fn绑定的函数
#     fn()

# fx(f1) # 调用fx,把f1作为实参传数
# fx(f2)
# def goodbye(l):
#     for x in l:
#         print("再见",x)
# def hello(l):
#     for x in l:
#         print("欢迎:",x)
# def fx(fn,l):
#     print("fx被调用")
#     fn(l)
# fx(hello,['Tom','Jerry','Spike'])
# fx(goodbye,['小张','小李'])
# def get_func(value):
#     if value ==1:
#         def myadd(x,y):
#             return x+y
#         return 
#     elif value ==2:
#         def mysub(x,y):
#             return x-y
#         return 6
# fx=get_func(1)
# print(fx(400,300))
# fx=get_func(2)
# print(fx(400,300))
# a=100
# b=200
# def fn(c):
#     d=400
#     print(a,b,c,d)
#     a=500
#     # print(a,b,c,d)

# fn(300)
# print('a=',a)
# print('b=',b)
# # print('c=',c)
# # print('d=',d)
# a=100
# b=200
# def fx(b,c):
#     print(a,b,c)
#     # 思考在此函数内部能否获取到全局变量b绑定的值?   不能
   
#     print("全局变量的字典是:",globals())
#     print("局部变量的字典是:",locals())
#     print("此处访问全局的b的值是:",globals()['b'])
# fx(300,400)  # (100,300,400)
 
# 100 300 400
# 全局变量的字典是: {'__name__': '__main__', 'b': 200, '__file__': 'wh.py', '__spec__': None, '__package__': None, 'fx': <function fx at 0x7f6751369f28>, '__cached__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f67512ab9e8>, 'a': 100, '__builtins__': <module 'builtins' (built-in)>, '__doc__': None}
# 局部变量的字典是: {'b': 300, 'c': 400}
# 此处访问全局的b的值是: 200

# # def mysum(n):
   
# #     d=[]
# #     for i in range(1,n+1):
# #         d.append(i)
# #     return sum(d)


# # print(mysum(100))


# # def mysum2(*age):
# #     if len(age)==1:
# #         s=0
# #         for x in range(age[0]):
# #             s+=x
# #         return s
# #     elif len(age)==2:
# #         s=0
# #         for x in range(age[0],age[1]):
# #             s+=x
# #         return s
# #     elif len(age)==3:
# #         s=0
# #         for x in range(age[0],age[1],age[2]):
# #             s+=x
# #         return s
  
# # print(mysum2(5))
# # print(mysum2(4,6))
# # print(mysum2(5,10,2))


# # def mysum2(a,b=0,c=1):
# #     if b is 0 :
# #         b=a
# #         a=0
# #     s=0
# #     for x in range(a,b,c):
# #         s+=x
# #     return s
# # print(mysum2(5))
# # print(mysum2(4,6))
# # print(mysum2(5,10,2))

# # def mysum2(a,b=0,c=1):
# #     if b is 0 :
# #         b=a
# #         a=0
# #     return sum(range(a,b,c))
  
# # print(mysum2(5))
# # print(mysum2(4,6))
# # print(mysum2(5,10,2))

# # v=100
# # def fx():
# #     v=200

# # # fx()
# # print(fx)   #100

# # v=100
# # def outter():
    
# #     v=200
# #     print("outter里的v=",v)
# #     def inner():
        
# #         v=300
# #         print("innter里的v=",v)

# #     inner()
# #     print("调用inner后,ouuter里的v=",v)
      
# # outter()
# # print("全局变量的v的值是:",v)


# # l=[]
# # def input_number():

# #     while True:
# #         i=int(input("请输入数字(-1结束):"))
# #         if i==-1:
# #             break
# #         l.append(i)
# #     return l

# # input_number()
# # print("您刚才输入的值是:",l)
# # ２．写一个函数isprime(x)判断x　是否为素数，如果为素数True,否则返回False
# # 测试代码
# # if isprime(5):
# #     print("是素数")
# # ３．写一个函数prime_m2n(m,n)返回从m开始，到n结束范围内的列表，并打印
# # l=prime_m2n(10,20)
# # print(l) #[11,13,17,19]
# # ４．写一个函数primes(n),返回小于n的所有的素数的列表
# # l=primes(10)
# # print(l) #[2,3,5,7]

# # def isprime(x):
# #     for i in range(2,x):
# #         if x%i == 0:
# #             return False 
               
# #     return True
            

# # isprime(2)
# # s=[]
# # def prime_m2n(m,n):
# #     for x in range(m,n):
# #         if x==1:
# #             continue
# #         for v in range(2,x):
# #             if x%v==0:
# #                 break
# #         else: 
# #             s.append(x)
# #     return s
    
# # l=prime_m2n(30,40)
# # print(l)
# # ４．写一个函数primes(n),返回小于n的所有的素数的列表
# # l=primes(10)
# # print(l) #[2,3,5,7]
# # s=[]
# # def primes(n):
# #     i=2
# #     while i<n:
# #         for x in range(2,i):
# #             if i%x==0:
# #                 break
# #         else:
# #             s.append(i)
# #         i+=1
# #     return s

# # l=primes(20)
# # print(l)


# # def mymax(*arg):
# #     if len(arg)==1:
# #         s=list(*arg)
# #         a=s[0]
# #         i=1
# #         while i<len(s):
# #             if s[i]>a:
# #                 a=s[i]
# #             i+=1
# #         return a
# #     elif len(arg) > 1:
# #         b=list(arg)
# #         d=b[0]
# #         o=1
# #         while o<len(arg):
# #             if b[o]>d:
# #                 d=b[o]
# #             o+=1

# #         return d

# # print(mymax([6,8,3,5]))
# # print(mymax(100,200))
# # print(mymax(1,3,9,7,5))


# # def mymax(a,*agr):
# #     if len(agr)==0:
# #         m=a[0]
# #         i=1
# #         while i<len(a):
# #             if a[i]>m:
# #                 m=a[i]
# #             i+=1
# #         return m
# #     elif len(agr) !=0:
# #         v=a
# #         for x in agr:
# #             if x > v:
# #                 v=x
# #         return v

# # print(mymax([6,8,3,5]))
# # print(mymax(100,200))
# # print(mymax(1,3,9,7,5))
# # def hello():
# #     print("hello aaa")
# #     print("hello bbb")
# #     return print("hello ccc")

# # v=hello()
# # print(v)
# # def mymax(a,b):
# #     return max(a,b)

# # print(mymax(100,20))
# # print(mymax("acd","abcd"))
# # def mymax(a,b):
# #     if a>b:
# #         s=a
# #     else:
# #         s=b
    
# #     return s 

# # print(mymax(10,20))
# # print(mymax("acd","abcd"))
# # def myfun1(a):
# #     global a
# #     a=111
# #     b=222
# #     def myfun2(b):
# #         nonlocal b
# # myfun1(3)
# # def f():
# #     def fg():
# #         print("sdfj")
# #         return True
# #     return fg

# # a=f()
# # a()
# # def fx():
# #     def hello():
# #         print("hello world")
# #         return None



# #     return hello()

# # fh=fx()
# # print(fh)
# # fx=lambda n : (n**2+1)%5==0 
# # print(fx(3))

# # mymax=lambda x,y: x if x>y else y
# # print(mymax(1,2))
# # def fx(f,x,y):
# #     r=x,y
# #     print(r)

# # fx((lambda a,b: a+b),100,200)
# # fx((lambda a,b: a**b),3,4)
# # x=100
# # y=200
# # s='x+y'
# # print(eval(s))
# # a=100
# # def f():
# #     a=200
# #     b=100
# #     print(a+b)
# # f()
# # s='print("hello"); x=100; x+=1; print(x)'
# # exec(s)
# # while True:
# #     s=input("请输入语句$>>>")
# #     if s=="bye":
# #         break
# #     exec(s)

# # def power2(x):
# #     return x**2
# # # for x in map(power2, range(1,10)):
# # #     print(x)
# # print(sum(map(power2,range(1,10))))
# # # g={}
# # l={}
# # while True:
# #     s=input("请输入语句$>>>")
# #     if s=="bye":
# #         break
# #     exec(s,g,l)
# # print(g)
# # print(l)

# # def yui(x):
# #     return x**3

# # print(sum(map(yui,range(1,10))))    
# # print(sum(map(lambda x: x**2,range(1,10))))
# # def isodd(x):
# #       return x%2==0
# # d=[x for x in filter(isodd,range(10))]
# # print(d)
# # l=[5,-2,-4,0,3,1]
# # l2=sorted(l,key=abs)
# # print(l2)
# # names=['Tom','Jerry','Spike','Tyke']
# # l=sorted(names)
# # a=sorted(l,key=len)
# # print(a)
# # names=['Tom','Jerry','Spike','Tyke']
# # def df(x):
# #     return x[::-1]
# # l=sorted(names,key=df)
# # print(l)
# # def f():
# #     f() 
# # f()
# # print("递归完成")
# # def fa():
# #     fb()

# # def fb():
# #     fa()
# # fa()
# # def story():
# #     print("从前有座山，山上有座庙，庙里有个老和尚讲故事:")
# #     story()
# #     print("故事讲完了")
# # story()
# # def story(times):
# #     print("第",times,"遍")
# #     print("从前有座山，山上有座庙，庙里有个老和尚讲故事:")
# #     if times >=3:
# #         return
# #     story(times+1)
# #     print("故事讲完了")
# # story(1)
# # def fx(n):
# #     print("现在是第",n,"层")
# #     # print("从前有座山，山上有座庙，庙里有个老和尚讲故事:")
# #     if n >= 3:
# #         return
# #     fx(n+1)
# #     print("第",n,"层")
# #     # print("故事讲完了")
# # fx(1)
# # print("程序结束")
# # def mysum(x):
# #     #　判断终止条件
# #     if x==1:
# #         return 1
# #     print(x)
# #     return(x + mysum(x-1))
# # print(mysum(5))

# # def isprime(x):
# #     if x<=1:#　排除小于1的数
# #         return False
# #     for i in range(2,x):
# #         if x%i==0:
# #             return False
# #     return True
# # if isprime(5)
# #     print("5是素数")
# # def myfac(x):
# #     for i in range(1,x):
# #         x*=i
# #     return x

# # print(myfac(5)) 

# # def mymab(m,n):
# #     return sum(map(myfac,range(m,n+1)))
# # print(mymab(1,20))

# # ３．已知有列表:
# # l=[[3,5,8],10,[[13,14],15],18]
# # 写一个函数print_list(lst)打印出列表中所有数字
# # print_list(l)
# # 写一个函数sum_list(lst)返回列表中所有数字的和
# # print(sum_list(l))
# # 注：type(x)可以返回容器类型
# # 如：　>>>type(20)  is int #True

# # s=[]
# # def print_list(a):
# #     for x in a:
# #         if type(x)!=int:
# #             print_list(x)
# #         else:
# #             s.append(x)
            
# #     return s
    
# # l=[[3,5,8],10,[[13,14],15],18]
# # print(print_list(l))

# # print(sum(print_list(l)))


# def input_student():
#     a=[]
#     while True:
#         name=input("请输入姓名:")
#         if name=="":
#             break
#         age=int(input("请输入年龄:"))
#         score=int(input("请输入成绩:"))
        
#         d={"name":name,"age":age,"score":score}
#         a.append(d)
#     return a
# def output_student(a):
#     print((("+"+"-"*10)*3)+"+","\n|"+"name".center(10)+"|"+"age".center(10)+"|"+"score".center(10)+"|","\n"+("+"+"-"*10)*3+"+")
#     for x in a:
#         print("|"+x["name"].center(10)+"|"+str(x["age"]).center(10)+"|"+str(x["score"]).center(10)+"|")
#     　　　　print(("+"+"-"*10)*3+"+")


# l=input_student()
# print(l)
# output_student(l)
# # i=0
# # for a in range(1,100):
# #     for b in range(a,100):
# #         for c in range(b,100):
# #             if a**2+b**2==c**2:
# #                 i+=1
# # #                 print(a,b,c)
                
# # # print(i)
# def mydeco(fn):  # 装饰函数
#     def fx():
#         print("+++++++++++++")
#         fn()
#         print("-------------")
#     return fx
# @mydeco
# def hello():# 被装饰函数
#     print("hello tarena")

# hello=mydeco(hello)　此时将hello变量绑定在mydeco返回的函数上

# hello() # 调用者

# # 以下是一个装饰器函数，在fn调用之前加一个权限验证功能
def priv_sheck(fn):
    def fx(name,x):
        print("正在权限验证...")
        fn(name,x)
    return fx
@priv_sheck
def save_money(name,x):
    print(name,"存钱",x,"元")
@priv_sheck
def withdraw(name,x):
    print(name,"正在办理取钱",x,"元的业务")

save_money("小张",200)
save_money("小李",500)
withdraw("小赵",300)
# # 示例一个函数可以用两个或两个以上装饰器

# # def message_send(fn):
# #     def fy(name,x):
# #         # 先办业务
# #         fn(name,x)
# #         print("短信:",name,"发生了",x,"元的操作,余额是xxx")
# #     return fy

# # def priv_sheck(fn):
# #     def fx(name,x):
# #         print("正在权限验证...")
# #         fn(name,x)
# #     return fx
# # @priv_sheck
# # def save_money(name,x):
# #     print(name,"存钱",x,"元")
# # # @priv_sheck
# # @message_send
# # def withdraw(name,x):
# #     print(name,"正在办理取钱",x,"元的业务")

# # save_money("小张",200)
# # save_money("小李",500)
# # withdraw("小赵",300)
# # import math
# # r=int(input("输入圆的半径:"))
# # d=math.pi*math.pow(r,2)
# # print(d)
# # n=int(input("输入一个圆的面积:"))
# # k=(n/math.pi)**0.5

# # print(k)
# import math as r
# # def fun(n):
# #     s=0
# #     for x in range(n+1):
# #         s+=1/r.factorial(x)
# #     return s
# # print(fun(10))
# def fun(x):
#     def fu(n):
#         sn=0
#         for a in range(n+1):
#             sn+=x**a/r.factorial(a)
#         return sn
#     return fu

# fg=fun(3.1)
# print(fg(10))

# def input_student():
#     lst=[] # 创建一个空列表用于存储学生的信息
#     while True:
#         n=input("请输入学生姓名:")
#         if not n:
#             break
#         a=int(input("请输入学生年龄:"))
#         s=int(input("请输入学生成绩:"))
#         # 创建一个字典
#         d={'name':n,'age':a,'score':s}
#         lst.append(d)# 把字典放到列表
#     return lst

# def output_student(lst):
#     print("+----------+---------+-----------+")
#     print("|   name   |    age  |   score   |")
#     print("+----------+---------+-----------+")
#     for d in lst:
#         info="| %9s | %6d | %7d |"%(d['name'],d['age'],d['score'])
#         print(info)
#         print("+----------+---------+-----------+")

# l=input_student()
# print(l)
# output_student(l)
