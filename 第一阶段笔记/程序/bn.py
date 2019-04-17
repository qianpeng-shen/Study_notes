

# a=int(input("请输入数字:"))
# def fun(a):
#     i=1
#     b=1
#     while b<=a:
#         t="*"*i
#         print(t.center(a*2-1," "))
#         i+=2
#         b+=1

# fun(a)
# print("kjflaksuer","kdjflksd",sep="  ##  ")

# def avg_score(dic):
#     score=dic.values()
#     print(score)
#     avg=sum(score)/len(score)
#     print("平均分：",avg)
# def sort_score(v):
#     L=[(v.get(x),x) for x in v]
#     print(L)
#     L=sorted(L,reverse=True)
#     # print(L)
#     print(L[0],L[-1])
# def fun():
#     v={}
#     while True:
#         a=input("请输入姓名:")
#         if a=="":
#             break
#         b=int(input("请输入成绩:"))

#         v['%s' % a]=b
#     print(v)
#     avg_score(v)
#     sort_score(v)

# fun()
# def fun1():
#     s=19999968
#     a=s
#     t=0
#     x=0
#     while a >= 1 :
#         n=a//2
#         t+=n
#         a=a//2
#         if a%2==1:
#             x+=1
#         if a<=1:
#             if x%2==1:
#                 i=1
#                 n=x//2
#                 t+=n
#                 x=x//2


#         print(x)
#         print("n=",n)
#         print("t=",t)
#         print("a=",a)
#         print("------------")
#     print(t+s)
# fun1()

# def fun():
#     v={}
#     while True:
#         a=input("请输入姓名:")
#         if a=="":
#             break
#         b=int(input("请输入成绩:"))

#         v.update({a:b})
#     print(v)


# fun()
# 此示例示意用 try-execpt语句来捕获异常
# def div_apple(n):
#     """此示例用来分苹果来示意捕获异常"""
#     print("%d个苹果你想要分给几个人" % n)
#     s=input("请输入人数:")
#     cnt=int(s) #<<==此处可能引起valueError(值)类型的错误
#     result=n/cnt
#     print("每个人分了",result,"个苹果")
# try:
#     div_apple(10)
# except ValueError:
#     print("发生值错误，苹果收回")
# except:
#     print("发生了处了值错误以外的错误，在此处理")
# else:
#     print("没有发生错误，苹果分完了")
# finally:
#     # 此子句内的语句无论是否发生异常都一定会执行
#     print("我一定会执行!!!")

# print("程序正常退出")
# def get_score():
#     s=int(input("请输入成绩:"))
#     print("这个学生的成绩是:",s)
# try:
#     get_score()
# except:
#     print("这个学生成绩为",0)


# def get_score():
#     s=int(input("请输入成绩:"))
#     if 0<=s<=100:
#         return s
# try:
#     score=get_score()
# except:
#     score=0
# print("这个学生成绩为",score)
# def get_score():
#     s=input("请输入成绩:")
#     try:
#         i=int(s)
#     except ValueError:
#         return 0

#     if 0<=i<=100:
#         return i
# score=get_score()
# print("这个学生成绩为",score)
# def fry_egg():
#     print("打开天然气")
#     try:
#         count=int(input("请输入鸡蛋个数:"))
#         print("完成煎鸡蛋!共煎了%d个鸡蛋" % count)
#     finally:
#         print("关闭天然气")

# fry_egg()
# def fry_egg():
#     print("打开天然气")
#     try:
#         count=int(input("请输入鸡蛋个数:"))
#         print("完成煎鸡蛋!共煎了%d个鸡蛋" % count)

#     finally:
#         print("关闭天然气")
# try:
#     fry_egg()
# except ValueError:
#     print("程序转为正常")
# print("程序正常退出")
# def make_except(n):
#     # 假设n必须是0~100之间的数
#     print("begin...")
#     if n > 100: # 传过的参数无效，怎么告诉调用者呢？
#         raise ValueError
#     if n<0:
#         raise ValueError("参数小于零错误:%d" % n)
#     print("end")
# value=int(input("输入一个整数:"))
# try:
#     make_except(value)
# except ValueError as e:
#     print("make_except 抛出错误，此异常状态已处理")
#     print("错误的值是",e)
#     print("发生错误")
# print("程序正常完成")

# def make_except(n):
#     # 假设n必须是0~100之间的数
#     print("begin...")
#     if n > 100: # 传过的参数无效，怎么告诉调用者呢？
#         raise ValueError
#     if n<0:
#         raise ValueError
#     print("end")
# value=int(input("输入一个整数:"))
# make_except(value)
# def get_age():
#     a=input("请输入年龄:")
#     a=int(a)
#     assert a<140, "年龄不可能大于140!!!"
#     assert a>=0,  "年龄不可能是负数!!!"
#     return a
# try:
#     age=get_age()
# except AssertionError as err:
#     print("发生断言错误!错误对象是:",err)
#     age=0
# print("您输入的年龄是:",age)
# def f1():
#     print("开始盖房子打地基...")
#     # raise ValueError("代表挖出文物")
#     print("地基完工")

# def f2():
#     print("开始盖房子以上部分")
#     raise ZeroDivisionError("要建高压线")
#     print("房子完工")
# def f3():
#     """第二承包商找人干活"""
#     f1()
#     f2()
# def build_house():
#     f3()
# try:
#     build_house()
# except ZeroDivisionError as err:
#     print("房子没盖好,因为",err)
# else:
#     print("房子盖好了")


# def f1():
#     print("开始盖房子打地基...")
#     return -1 # -1 代表挖出文物
#     print("地基完工")
#     return 0
# def f2():
#     print("开始盖房子以上部分")
#     return -2 # -2 代表要建高压线
#     print("房子完工")
# def f3():
#     """第二承包商找人干活"""
#     r=f1()
#     if r<0:
#         return r
#     else:
#         r2=f2()
#         return r2
# def build_house():
#     r=f3()
#     if r<0:
#         return r
#     return 0
# r=build_house()
# if r==0:
#     print("房子盖好了")
# elif r==-1:
#     print("房子没盖好，因为文物问题")
# elif r==-2:
#     print("房子没盖好，因为高压线")
# import random
# def get_new_poker():
#     kinds = ['\u2660','\u2663','\u2665','\u2666']
#     numbers = ['A']
#     numbers += [str(x) for x in range(2,11)]
#     numbers += ['J','Q','K']
#     l=[k+n for k in kinds for n in numbers]
#     l += ['BK','SK']
#     return l
# def play():
#     poker=get_new_poker()
#     random.shuffle(poker)
#     input("按任意键发第一个人的牌:")
#     print("第一个人的牌是",poker[:17])
#     input("按任意键发第二个人的牌:")
#     print("第二个人的牌是",poker[17:34])
#     input("按任意键发第三个人的牌:")
#     print("第三个人的牌是",poker[34:51])
#     input("按任意键发底牌:")
#     print("底牌是",poker[51:])

# get_new_poker()it=iter(range(1,10,3))

# play()
# １．一个球从100米高度落下，每次落地反弹高度为原高度的一半，再落下
# １）写程序算出皮球从第十次落下后反弹高度是多少？
# ２）球一共经过多少米路径？
# def fun(n):
#     for x in range(10):
#         n=n/2
#     return n
# print(fun(100))
# def fun1(n):
#     a=n
#     t=0
#     for x in range(10):
#         a=a/2
#         t+=a*2
#     return t+n
# print(fun1(100))
# def fun2():
#     for x in range(1,10):
#         for y in range(1,x+1):
#             print(str(y)+"*"+str(x)+"=",x*y,end=" ")
#         print()
# fun2()
# 3.分解质因数：
# 输入一个正整数，分解质因数：
# 如输入：　90 则打印：
# 　　　90=2*3*3*5
# (原质因数是指最小能被原数整除的素数(不包含1))
# def fun3(n):
#     l=[]
#     for x in range(2,n):
#         for y in range(2,x):
#             if x % y ==0:
#                 break
#         else:
#             l.append(x)
#     return l
# def fun4(n):
#     r=n
#     at=fun3(n)
#     h=[]
#     t=0
#     for x in at:
#         while n%at[t]==0:
#             h.append(str(at[t]))
#             n=n/at[t]
#         t+=1
#     return str(r)+"="+("*".join(h))
# n=int(input("输入一个正整数:"))
# print(fun4(n))


# l=[2,3,5,7]
# it=iter(l)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break
# s={"工商银行","建设银行","中国银行","农业银行"}
# for x in s:
#     print(x)

# s={"工商银行","建设银行","中国银行","农业银行"}
# a=iter(s)
# while True:
#     try:
#         x=next(a)
#         print(x)
#     except StopIteration:
#         break

# def myyield():
#     print("即将生成2")
#     yield 2
#     print("即将生成3")
#     yield 3
#     print("即将生成5")
#     yield 5
#     print("即将生成7")
#     yield 7
#     print("生成器函数调用结束")
# gen=myyield()
# it=iter(gen)
# print(next(it))
# print(next(it))　　# myyield 将从上一次停止的位置(yield 2)开始执行
# def my_integer(n):
#     i=1  #　先初始化变量i将其设置为起始值
#     while i<n:  # 循环判断是否已到终止点，如果未到则生成
#         yield i  # 生成整数
#         i+=1   # 控制条件
# for x in my_integer(5000):
#     print(x)


# def fun():
#     a=int(input("输入开始值:"))
#     b=int(input("输入结束值:"))
#     i=a
#     l=[]
#     while i<b:
#         yield i
#         if i%2==1:
#             l.append(i)

#         i+=1
#     for x in l:
#         print(x)

# fun()

# def myodd(s,a):
#     i=s
#     while i<a:
#         if i%2==1:
#             yield i
#         i+=1
# for x in myodd(10,20):
#     print(x)
# gen=(x**2 for x in range(1,5))
# it=iter(gen)
# print(next(it))  # 1
# print(next(it))  # 4
# print(next(it))  # 9
# print(next(it))  # 16
# print(next(it))  # StopIteration
# numbers=[10086,10000,10010,95588]
# name=['中国移动','中国电信','中国联通']
# # for t in zip(numbers,name):
# #     print(t)
# print(dict(zip(numbers,name)))
# def myzip(iter1,iter2):
#     it1=iter(iter1)
#     it2=iter(iter2)
#     while True:
#         a=next(it1)
#         b=next(it2)

#         yield(a,b)

# numbers=[10086,10000,10010,95588]
# name=['中国移动','中国电信','中国联通']
# for t in myzip(numbers,name):
#     print(t)


# def myzip(iter1,iter2):
#     it1=iter(iter1)
#     it2=iter(iter2)
#     try:
#         while True:
#             a=next(it1)
#             b=next(it2)
#             yield(a,b)
#     except:
#         pass

# numbers=[10086,10000,10010,95588]
# name=['中国移动','中国电信','中国联通']
# for t in myzip(numbers,name):
#     print(t)
# numbers=[10086,10000,10010,95588]
# name=['中国移动','中国电信','中国联通']
# for t in zip(range(1,10000),numbers,name):
#     print(t)
# name=['中国移动','中国电信','中国联通']
# it=iter(enumerate(name,1))
# while True:
#     try:
#         k,n=next(it)

# # for k,t in enumerate(name,10):
#         print("xuhao",k,"-------->",n)
#     except StopIteration:
#         break
# def mytun():
#     d=[]
#     while True:
#         a=input("请输入文字:")
#         if a=="":
#             break
#         d.append(a)
#     return d
# def out_tex(d):
#     for k,n in enumerate(d,1):
#         print("第%d行:" % k,n)
# y=mytun()
# out_tex(y)
# def mydeco(fn):  # 装饰函数
#     def fx():
#         print("hello world")
#     return fx
# # @mydeco
# def hello():# 被装饰函数
#     print("hello tarena")

# hello=mydeco(hello)#此时将hello变量绑定在mydeco返回的函数上
# hello()

# def fun1():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print("%dx%d=%d" % (j,i,j*i),end=" ")
#         print()
# fun1()

# １．用生成器函数生成斐波那契数列的前n个数：
# 　　　　1,1,2,3,5,8,13
# 　　　　def fibonacci(n):
# 　　　1)输出前20个数
# 　　　2)求前30个数的和


# def fun1(n):
#     a=1
#     yield a
#     b=1
#     yield b
#     i=1
#     s=0
#     while i < n-1:
#         s=a+b
#         yield s
#         i+=1
#         a,b=b,a+b
# for d in fun1(20):
#     print(d)
# # def fun1(n):
#     a=1
#     yield a
#     b=1
#     yield b
#     i=1
#     s=0
#     while i < n-1:
#         s=a+b
#         yield s
#         i+=1
#         a,b=b,a+b
# z=[d for d in fun1(30)]
# print(sum(z))
# file=open("lian.py")
# print("打开文件成功")
# # 通常在此进行读写文件内容
# #关闭文件
# file.close()
# print("文件已关闭")
# try:
#     file=open("lian.py")
#     print("打开文件成功")
# # 通常在此进行读写文件内容
#     s=file.readline()
#     print("第一行内容是",s)
# #关闭文件
#     file.close()
#     print("文件已关闭")
# except IOError:
#     print("文件打开失败")
# def fun():
#     f=open("data.txt")
#     while True:
#         s=f.readline()
#         if not s:
#             f.close()
#             return
#         a=s.rstrip()
#         index=s.find(" ")
#         name=a[:index]
#         nuber=a[index+1:]
#         print("姓名:",name,"电话:",nuber)
# fun()
# def fun():
#     l=[1]
#     i=0
#     while i<7:
#         l.append(0)

#         l=[l[x-1]+l[x] for x in range(len(l))]
#         print(l)
#         i+=1
#     print(l)
# # for x in fun():
# #     print(" ".join(str(x)))
# fun()


# try:
#     f=open("asd.txt","w")# 以只写的方法打开文件
#     print("打开文件成功")
#     f.write("我是一行\n")
#     f.write("我是二行\n")
#     f.writelines(['我是三\n','我都是四\n','five\n'])
#     f.close()

# except IOError:
#     print("打开文件失败")
# def fun1():
#     l=[]
#     while True:
#         s=input("输入字符串:")
#         if s=="":

#             break
#         l.append(s)
#         l.append("\n")
#     return l
# def fun3(x):
#     f=open("input.txt",'w')
#     f.writelines(x)
#     f.close
# fun3(fun1())
# def fun1():
#     l=[]
#     while True:
#         s=input("请输入字符串:")
#         if not s :
#             break
#         l.append(s)
#     return l
# def fun2(l):
#     f=open("input.txt","w")
#     for x in l:
#         f.write(x)
#         f.write("\n")
#     f.close()

# fun2(fun1())
# def fun5(fa="input.txt"):
#     f=open(fa)
#     l=[]
#     while True:
#         s=f.readline()
#         if not s:
#             break
#         s=s.rstrip()
#         l.append(s)
#     f.close()
#     return l
# def print_file_info(l):
#     for x,n in enumerate(l,1):
#         print("第%d行" %x,n)

# lst=fun5()
# print_file_info(lst)
# f=open("myto.txt","w")
# f.write("aaaaaa")
# f.flush()# 把缓冲的内容写入到磁盘
# s=input("暂停...")
# f.write("bbbbb")
# f.close()

# try:
#     f=open("asd.txt","rb") # 打开模式为"rb"
#     print("打开文件成功")
#     b=f.read()
#     print(b)
#     s=b.decode('utf-8')
#     print("转码后:",s)
# except IOError:
#     print("打开文件失败")

# 此程序示意二进制方式打开文件后进行写操作
# f=open("mydata.bin","wb") # "wb"二进制写模式
# print("文件打开成功")
# f.write(b'hello\xe4\xb8\xad') # 写入五个字节
# s="我是汉字"
# r=f.write(s.encode('utf-8'))
# print("写入",s,"共写入",r,"个字节")
# f.close()
# f=open('alpha_number.bin','rb') # 二进制方式打开
# print("刚打开时的文件流位置为:",f.tell())
# b=f.read(5)
# print("读出五个字节后的文件流位置:",f.tell())
# f.close()

# f=open('myto.txt','rb')
# b=f.read(5)
# #f.seek(10,0)
# f.seek(-10,2)
# #f.seek(5,1)
# b=f.read(5)
# print(b)
# f.close()

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
#         print(("+"+"-"*10)*3+"+")
# def show_menu():
#     print("显示学生信息")
#     print("1)添加学生信息")
#     print("2)显示所有学生的信息")
#     print("3)删除学生信息")
#     print("4)修改学生成绩")
#     print("5)按学生成绩高-低显示学生信息")
#     print("6)按学生成绩低-高显示学生信息")
#     print("7)按学生年龄高-低显示学生信息")
#     print("8)按学生年龄低-高显示学生信息")
#     print("9)退出")
# def list_st(a):
#     s=input("请输入姓名:")
#     for x in a:
#         if x["name"]==s:
#             a.remove(x)
#             break
#     return a

# def modify(a):
#     a1=(input("请输入姓名:"))
#     b=int(input("请输入成绩:"))
#     for x in a:
#         if x["name"]==a1:
#             x["score"]=b
#             break
#         else:
#             print("无此人")
#     return a
# def asd(x):
#     return x["score"]
# def asdf(a):
#     l=sorted(a,key=asd,reverse=True)
#     output_student(a)
# def asd_e(x):
#     return x["score"]
# def asdf_e(a):
#     l=sorted(a,key=asd_e,reverse=False)
#     output_student(a)
# def asd_po(x):
#     return x["age"]
# def asdf_jk(a):
#     l=sorted(a,key=asd_po,reverse=True)
#     output_student(a)
# def asd_pu(x):
#     return x["age"]
# def asdf_uy(a):
#     l=sorted(a,key=asd_pu,reverse=False)
#     output_student(a)
# def fun1():
#     f=open("a.txt","w")


# def main ():
#     docs=[]
#     while True:
#         show_menu()
#         s=input("请选择:")
#         if s=="1":
#             docs+=input_student()
#         elif s=="2":
#             output_student(docs)
#         elif s=="3":
#             docs=list_st(docs)
#         elif s=="4":
#            docs= modify(docs)
#         elif s=="5":
#             asdf(docs)
#         elif s=="6":
#             asdf_e(docs)
#         elif s=="7":
#             asdf_jk(docs)
#         elif s=="8":
#             asdf_uy(docs)

#         elif s=="9":
#             fun1()


# main()
# import sys
# s=sys.stdin.read(10)#默认从键盘获取数据
# print(s)
# s2=sys.stdin.read(10)
# print(s2)
# print("请开始输入:")
# s=sys.stdin.read()
# print("输入的是:",s)
# class Dog:
#     pass
# dog1=Dog()
# print(id(dog1))
# dog2=Dog()
# print(id(dog2))
# print(dog1 is dog2)
# class Dog:
#     pass
# dog1=Dog()
# dog1.kinds="京巴" # 为dog1绑定的实例添加kinds属性
# dog1.color="白色"  # 添加属性
# print(dog1.kinds,dog1.color)  # 访问属性
# dog1.color="黄色"  # 改变对象的属性
# print(dog1.color)
# class student:
#     pass
# def input_student():
#     l=[]
#     while True:
#         s=input("请输入名字:")
#         if not s:
#             break
#         student.name=s
#         b=int(input("请输入成绩:"))
#         student.score=b
#         c=int(input("请输入年龄:"))
#         student.age=c
#         l.append((student.name,student.score,student.age))
#     return l
# def output_student(a):
#     for x in a:
#         print("姓名:%s 成绩:%d 年龄:%d" % x)
# a=input_student()
# output_student(a)
class student:
    pass
def input_student():
    l=[]
    while True:
        s = input("请输入名字:")
        if not s:
            break
        c = int(input("请输入年龄:"))
        b = int(input("请输入成绩:"))
        stu=student()
        stu.name = s
        stu.score = b
        stu.age = c
        l.append(stu)
    return l
def output_student(lst):
    for stu in lst:
        print("姓名:",stu.name,
             "年龄",stu.age,
             "成绩:",stu.score)
def main():
    a = input_student()
    output_student(a)


main()
# class Dog:
#     '''这是一个类，用于描述一个小动物的行为'''
#     def eat(self,food):
#         '''小狗有吃东西的行为'''
#         print("小狗吃了:",food)
#     def sleep(self,hour):
#         print("小狗睡了",hour,"小时")

# #实例.实例方法名(调用参数)
# dog1=Dog()  # 创建一个实例对象
# dog1.eat("骨头")  # 让狗吃东西
# dog1.sleep(1)   # 让狗睡觉
# dog2=Dog()  # 再创建一个实例对象
# dog2.eat("包子")
# dog2.sleep(2)

# #类名.实例方法名(实例，调用参数) 一般不这样做
# dog3=Dog()
# Dog.eat(dog3,"狗粮")
# Dog.sleep(dog3,3)
# class Dog:
#     '''这是一个类，用于描述一个小动物的行为'''
#     def eat(self,food):
#         '''小狗有吃东西的行为'''
#         print("小狗吃了:",food)
#         self.food=food # 为self的对象添加food属性记着狗吃的是什么
#     def food_info(self):
#         """能否在此方法内得到小狗上次吃的食物是什么"""
#         print("上次吃的是:", self.food)


# #实例.实例方法名(调用参数)
# dog1=Dog()  # 创建一个实例对象
# dog1.eat("骨头")  # 让狗吃东西
# dog1.food_info()
# dog1.eat("包子")
# dog2=Dog()  # 再创建一个实例对象
# dog2.eat("包子")

# # dog1.food_info()  # 得到上次dog1吃的是什么?
# dog2.food_info()

# class Car:
#     """小汽车类"""
#     def __init__(self,c,b,m):
#         self.color=c #颜色
#         self.brand=b #品牌
#         self.model=m #型号

#     def run(self,speed):
#         print(self.color,'的',self.brand,
#             self.model,'正在以',speed,
#             '公里/小时的速度行驶')
#     def change_color(self,c):
#         self.color=c

# a4=Car("红色",'奥迪','A4')
# a4.run(199)
# a4.change_color("白色")
# a4.run(200)
# x5=Car('蓝色','宝马','x5')
# # x5.run(280)

# class student:
#     def __init__(self,n,s,a):
#         self.name=n
#         self.score=s
#         self.age=a
# def input_student():
#     l=[]
#     while True:
#         n = input("请输入名字:")
#         if not n:
#             break
#         a = int(input("请输入年龄:"))
#         s = int(input("请输入成绩:"))
#         stu=student(n,s,a)
#         l.append(stu)
#     return l
# def output_student(lst):
#     df=input_student()
#     for stu in lst:
#         print("姓名:",stu.name,
#              "年龄",stu.age,
#              "成绩:",stu.score)
# def main():
#     a = input_student()
#     output_student(a)


# main()

# class FileManage:
#     """定义一个文件管理员"""
#     def __init__(self,filename='a.txt'):
#         self.file=open(filename,'w')
#     def writeline(self,string):
#         self.file.write(string)
#         self.file.write('\n')
#     def __del__(self):#在对象被销毁之前被自动调用
#         """析构方法会在对象销毁前自动调用"""
#         self.file.close()
#         print("文件已关闭")
# fm=FileManage()
# fm.writeline("hello world")
# fm.writeline("这是中文写的第二行")
# del fm
# while True:
#     pass
# print("程序结束")

# def fun(n):
#     count=0  # 记录当前已生成的个数
#     if count>=n:
#         return
#     yield 1
#     count+=1
#     if count>=n:
#         return
#     yield 1
#     count+=1
#     l=[1,1]
#     while count<n:
#         l.append(l[-1]+l[-2])
#         yield l[-1]
#         count+=1
# for x in fun(20):
#     print(x)


# def fun(n):
#     count=0  # 记录当前已生成的个数
#     if count>=n:
#         return
#     yield 1
#     count+=1
#     if count>=n:
#         return
#     yield 1
#     count+=1
#     a=1
#     b=1
#     while count<n:
#         yield a+b
#         a,b=b,a+b
#         count+=1
# for x in fun(20):
#     print(x)
# print(sum(fun(30)))

# def get_next_line(lst):
#     #先放入一个1
#     next_line=[1]# 先把最左边的数放入
#     # 第二步计算中间的那些数
#     for i in range(len(lst)-1):
#         next_line.append(lst[i]+lst[i+1])
#     #第三步，在最后加一个1
#     next_line.append(1)
#     return next_line
# def get_yang(n):
#     l=[1]
#     a=[]
#     for x in range(n):
#         a.append(l)# 把当前l存储的一行放入列表
#         l=get_next_line(l)# 用当前行来计算下一行
#     return a
# l=get_yang(6)
# for x in l:
#     print(x)
# 练习：
# 定义一个类(人类)
# 有三个属性：
# 姓名:name  年龄: age 家庭住址: address(可省略)
# 有如下方法:
# show_info(self) 用来显示人的信息
# update_age(self) 用来让这个人的年龄增加一岁
# def input_human():
#   输入一些人的信息，姓名为空结束
# def main():
# docs=input_human()
# for h in docs:
#     h.show_info()# 列出所有人的信息
# for h in docs:
#     h.update_age()# 让所有的人都长一岁
# for h in docs:
#     h.show_info()再次列出所有人的信息
# main()


# class humen:
#     def __init__(self,n,a,add="不详"):
#         self.name=n
#         self.age=a
#         self.address=add
#     def show_info(self):
#         print("姓名:",self.name,
#                 "年龄:",self.age,
#                 "家庭住址:",self.address)
#     def update_age(self):
#         self.age+=1
# def input_human():
#     l=[]
#     while True:
#         na=input("请输入姓名:")
#         if not na:
#             break
#         aj=int(input("请输入年龄:"))
#         dp=input("请输入家庭住址:")
#         stu=humen(na,aj,ap)
#         l.append(stu)
#     return l
# def main():
#     docs=input_human()
#     for h in docs:
#         h.show_info()
#     for h in docs:
#         h.update_age()
#     for h in docs:
#         h.show_info()
# main()
# class ren:
#     def __init__(self,n,a,s):
#         self.name=n
#         self.age=a
#         self.sex=s
#     def eat(self,f):
#         self.food=f
#     def kf(self,p):
#         self.play=p
#         print("一个:",self.age,"名字叫:",self.name,"的",self.sex,"孩吃完",self.food,"后开始玩",self.play)
# ren1=ren("小米","19","男")
# ren1.eat("米饭")
# ren1.kf("足球")

# #此示例示意类变量的用法和使用方法
# class human:
#     total_count=0 #类变量，用于记录对象的个数
#     def __init__(self,name):
#         self.name=name
#         self.__class__.total_count+=1#　人数加一
#         print(name,"对象创建")
#     def __del__(self):
#         self.__class__.total_count-=1#　总人数减一

# print("当前对象的个数是",human.total_count)
# h1=human("张飞")
# h2=human("赵云")
# print("当前对象个数是:",human.total_count)   # 2
# del h2 # 或 h2=None
# print("当前对象个数是:",human.total_count)   # 1

# class student:
#     # __slots__=["name","age"]
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
# s1=student("小张",20)
# s1.Age=21
# print(s1.__dict__)# 出错，因为没有__dict__字典
# class A:

#     v=0 # 类变量

#     @classmethod
#     def get_v(cls): #从方法不是实例方法，是类方法
#         return cls.v
#     @classmethod
#     def set_v(cls,value):
#         cls.v=value


# print(A.get_v()) # 0
# A.v=1
# print(A.get_v()) #1
# A.set_v(100)
# print(A.get_v()) # 100
# a=A() #创建一个实例
# a.set_v(200)  # 此时cls=a.__class__(属性)
# print(A.get_v())# 200

# class humen:
#     total_count=0
#     def __init__(self,n,a,add):
#         self.name=n
#         self.age=a
#         self.address=add
#         self.__class__.total_count+=1
#     def __del__(self):
#         self.__class__.total_count-=1
#     @classmethod
#     def get_humen_count(cls):
#         return cls.total_count # 返回总人数
#     def show_info(self):
#         print("姓名:",self.name,
#                 "年龄:",self.age,
#                 "家庭住址:",self.address)
#     def update_age(self):
#         self.age+=1
# def input_human():
#     l=[]
#     while True:
#         na=input("请输入姓名:")
#         if not na:
#             break
#         aj=int(input("请输入年龄:"))
#         dp=input("请输入家庭住址:")
#         stu=humen(na,aj,dp)
#         l.append(stu)
#     return l
# def main():
#     docs=input_human()
#     print("当前的总人数:",humen.get_humen_count())
#     # docs+=input_human()
#     # print("当前的总人数:",humen.get_humen_count())
#     for h in docs:
#         h.show_info()
#     for h in docs:
#         h.update_age()
#     for h in docs:
#         h.show_info()
# main()
# 此示例示意单继承的语法及使用方法
# class human:  # 人
#     def say(self,what):   # 说话的行为
#         print("说:",what)
#     def walk(self,distance):   # 走路的行为
#         print("走了",distance,"公里")

# class student(human):
#     def study(self,subject):
#         print("正在学习",subject)

# class teacher(student):
#     def teach(self,that):
#         print("老师在教:",that)

# h1=human()
# h1.say("今天天气不错!")
# h1.walk(5)
# print("------------")
# s1=student()
# s1.say("今天晚饭吃什么")
# s1.walk(3)
# s1.study("python")
# print("-----------")
# t1=teacher()
# t1.say("今天下班早点回家")
# t1.walk(1)
# t1.study("魔方")
# t1.teach("面向对象")

# class mylist(list):
#     def insert_head(self,element):
#         self[0:0]=[element]
# myl=mylist(range(3,6))
# print(myl)
# myl.insert_head(2)
# print(myl)

# class A:
#     def work(self):
#         print("A类的work方法被调用")
# class B(A):
#     def work(self):
#         print("B类的work方法被调用")
# b=B()
# b.work()  # 调用B
# 此示例示意用super函数访问父类的覆盖方法
# class A:
#     def work(self):
#         print("A类的work方法被调用")
# class B(A):
#     def work(self):
#         print("B类的work方法被调用")
#     def doworks(self):
#         self.work()  # 调用谁? #调用B类的方法
#         super(B,self).work()#调用超类的方法
#         super().work()#一样会调用超类方法
#         super(__class__,self).work()#一般不用这种方法
# b=B()
# b.work()  # 调用B　　，　此时子类已经覆盖父类的方法
# print("-----------------------------")
# super(B,b).work()
# b.doworks()

# class human:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#         print("human类的__init被调用")

#     def show_info(self):
#         print("姓名:",self.name)
#         print("年龄:",self.age)
# class student(human):
#     def __init__(self,n,a,s=0):
#         super().__init__(n,a)#显示调用基类的初始化方法
#         self.score=s
#         print("student类的__init__被调用")
#     def show_info(self):
#         super().show_info()
#         print("成绩",self.score)

# s1=student("张学友",40)
# s1.show_info()
# 写一个Biycycle(自行车)类，有run(骑行)方法，调用时显示
# 骑行里程km
# class Bycycle:
#     def run(self,km):
#         print("自行车骑行了:",km,"公里")
# 再写一个电动车类EBicycle继承自biycycle,添加电池电量valume
# 属性，同时有两个方法：
# fill_charge(vol)  用来充电vol为电量(度)
# run(km)方法用于骑行，每骑行10km消耗电量1度,当电量消耗尽时调
# 用biycycle的run方法骑行
# 并显示骑行结果
# 主程序:
# b=EBicycle(5)# 创建一个电动自行车，默认电量5度
# b.run(10)#骑行10km
# b.run(100)#骑行100km
# b.fill_charge(6)#充电6度b.fill_b.fill_charge(6)
# b.run(70)b.fill_charge(6)
# b.run(70)charge(6)
# b.run(70)
# b.run(70)  #又骑行70km

# class Biycycle:
#     def run(self,km):
#         print("自行车骑行了:",km,"公里")
# class EBicycle(Biycycle):
#     def __init__(self,vol):
#         self.valume=vol
#     def fill_charge(self,vol):
#         print("电动车充电:",vol,"度")
#         self.valume+=vol
#     def run(self,km):
#         if  km<=self.valume*10:
#             self.valume-=km/10
#             print("电动车骑行:",km,"公里")
#         else:
#             print("电动车骑行:",self.valume*10,"公里")
#             super().run(km-self.valume*10)
#             self.valume=0

# b=EBicycle(5)
# b.run(10)
# b.run(100)
# b.fill_charge(6)
# b.run(70)
# b.run(10)
# b.fill_charge(8)
# b.run(70)


# class student:
#     def __init__(self,name,phone,emil):
#         self.name=name
#         self.phone=phone
#         self.emil=emil
#         # print("姓名",self.name,"手机",self.phone,"友尽",self.emil)
#     def get_name(self):
#         print("姓名:",self.name)
#     def get_phone(self):
#         print("手机:",self.phone)
#     def get_emil(self):
#         print("邮件:",self.emil)


# s1=student("bob","13458793248","12123@qq.com")
# s1.get_name()
# s1.get_phone()
# s1.get_emil()
# class student:
#     # 限定此类创建的对象只能有name和age两个属性
#     # __slots__=["name","age"]
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a

# s1=student("小张",20)
# s1.Age=21
# print(s1.__dict__)　# 出错，因为没有__dict__字典


# 多态示例
# class Shape:
#     def draw(self):
#         pass
# class Point(Shape):
#     def draw(self):
#         print("正在画一个点")
# class Circle(Point):
#     def draw(self):
#         print("正在画一个圆")
# def my_draw(s):
#     s.draw() #　调用哪的方法 在运行时动态决定调用的方法
# s1=Circle()
# s2=Point()
# my_draw(s1)
# my_draw(s2)
# class Car:
#     def run(self,speed):
#         print("汽车以",speed,"km/h的速度行驶")
# class Plane:
#     def fly(self,height):
#         print("飞机以海拔",height,"米的高度飞行")

# class Planecar(Car,Plane):
#     """飞机汽车类，是继承　自 Car和Plane"""

# p1=Planecar()
# p1.fly(2000)
# p1.run(299)
# 小张写了一个类A
# class A:
#     def m(self):
#         print("A.m()被调用")
# #小李写了一个类B
# class B:
#     def m(self):
#         print("B.m()被调用")
# #小王感觉小张和小李写的两个类自己可以用
# class AB(A,B):
#     pass
# ab=AB()
# ab.m() # 请问调用谁

# 此示例示意 str(x) 函数的repr(x)函数的重写方法

# class MyNumber:
#     def __init__(self,value):
#         self.data=value
#     # def __str__(self):
#     #     print("__str__方法被调用")
#     #     return "数字: %d" % self.data
#     def __repr__(self):
#         """此方法供repr(obj)函数调用!"""
#         return "MyNumber(%d)" % self.data


# n1=MyNumber(100)
# print(str(n1)) # 此句其实等同于print(n1)
# print(n1)
# print(repr(n1))#他会调用n1.__repr__()方法
# class MyInteger:
#     def __init__(self,value):
#         self.data=value
#     def __repr__(self):
#         return 'MyInteger(%d)' % self.data
#     def __abs__(self):
#         if self.data<0:
#             return MyInteger(-self.data)#创建一个新的对象并返回值

#         return MyInteger(self.data)
#     def __len__(self):
#         """len(x)函数规定只能返回整数值，因此此方法不能放回字符串等其它类型的值"""
#         return 100

# I1=MyInteger(-10)
# print(I1)  # <--此处等同于print(str(I1))
# I2=abs(I1)  # I2=MyInteger(10)
# print(I2)  # MyInteger(10)
# print(len(I1))


# #此示例示意数值类型转换函数重写
# class MyNumber:
#     """此类是自定义的类，用于表示自定义数字的类型"""
#     def __init__(self,v):
#         self.data=v
#     def __repr__(self):
#         return 'MyNumber(%s)' % self.data
#     def __int__(self):
#         return int(self.data)
#     def __float__(self):
#         return float(self.data)

# n1=MyNumber("100")
# print('n1=',n1)
# print(int(n1)) # 100
# print(float(n1))# 需要实现__float__(self) 方法


# #此示例示意　bool真值测试函数的重写
# class MyList:
#     """定义一个容器，用于存储任意类型的数据
#     其内部的存储方式用list实现"""
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return 'MyList(%s)' % self.data
#     def __len__(self):
#         print("__len__方法被调用!")
#         return len(self.data)   #　返回列表长度

#     # def __bool__(self):
#     #     """此方法用于bool(obj)函数取值，优先取值此函数
#     #     的返回值，此方法用于定义bool(obj)的取值规则"""
#     #     # 规则，所有元素的和为0，咋返回False否则返回True
#     #     return sum(self.data)!=0

# myl=MyList([1,-2,5,-4])
# print(myl)
# print('bool(myl)=',bool(myl))
# if myl:
#     print("myl 的布尔值为True")
# else:
#     print("myl 的布尔值为False")
# 此示例示意　bool真值测试函数的重写


# class MyList:
#     """定义一个容器，用于存储任意类型的数据
#     其内部的存储方式用list实现"""
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return 'MyList(%s)' % self.data
#     def __iter__(self):
#         """此方法把MyList类型的对象作为可迭代对象使用
#         此方法需要返回迭代器"""
#         return MyListIterator(self.data)# return 迭代器

# class MyListIterator:
#     '''此类定义一个迭代器类，用于生成能够访问MyList对象的
#     迭代器'''
#     def __init__(self,lst_data):
#         print("迭代器已经被创建")
#         self.data=lst_data# 绑定要访问的数据列表
#         self.cur_pos=0# 设置迭代器的起始位置为0
#     def __next__(self):
#         '''此方法用来访问可迭代对象的数据，如果没有
#         数据时触发StopIterator 异常来通知调用者停止迭代，
#         即"迭代器协议"'''
#         #先判断索引是否越界，如果已越界则触发异常停止迭代
#         if self.cur_pos>=len(self.data):
#             raise StopIteration
#         index=self.cur_pos
#         self.cur_pos+=1# 将当前位置向后移动准备下次获取
#         return self.data[index]#返回当前位置的数据

# myl=MyList([1,-2,5,-4])
# for x in myl:
#     print(x)


# class MyList:
#     """定义一个容器，用于存储任意类型的数据
#     其内部的存储方式用list实现"""
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return 'MyList(%s)' % self.data
#     def __iter__(self):
#         self.cur_pos=0
#         """此方法把MyList类型的对象作为可迭代对象使用
#         此方法需要返回迭代器"""
#         return self# return 迭代器
#     def __next__(self):
#         '''此方法用来访问可迭代对象的数据，如果没有
#         数据时触发StopIterator 异常来通知调用者停止迭代，
#         即"迭代器协议"'''
#         #先判断索引是否越界，如果已越界则触发异常停止迭代
#         if self.cur_pos>=len(self.data):
#             raise StopIteration
#         index=self.cur_pos
#         self.cur_pos+=1# 将当前位置向后移动准备下次获取
#         return self.data[index]#返回当前位置的数据

# myl=MyList([1,-2,5,-4])
# for x in myl:
#     print(x)
# ３．写一个实现迭代器协议的类Primes
# 让此类可以生成从b开始的n个素数

# class Primes:
#     @staticmethod
#     def __isprime(x):
#         for i in range(2,x):
#             if x%i==0:
#                 return False
#         return True
#     def __init__(self, b, n):
#         self.begin=b
#         self.count=n
#     def __repr__(self):
#         return 'Primes(%s)' % self.data
#     def __iter__(self):
#         self.cur_pos = self.begin # 设置迭代的起始值
#         self.cur_count=0
#         return self
#     def __next__(self):
#         # 已经生成，不需要再生成，停止迭代
#         if self.cur_count >= self.count:
#             raise StopIteration
#         self.cur_count += 1 # 计数加1
#         while True:
#             if self.__isprime(self.cur_pos):
#                 v=self.cur_pos
#                 self.cur_pos +=1
#                 return v
#             self.cur_pos +=1  # 为下次循环做准备
         

# for x in Primes(10,4):
#     print(x)

# class Biycycle:
#     def run(self,km):
#         print("自行车骑行了:",km,"公里")
# class EBicycle(Biycycle):ds
#     def __init__(self,vol):
#         self.valume=vol
#     def fill_charge(self,vol):
#         print("电动车充电:",vol,"度")
#         self.valume+=vol
#     def run(self,km):
#         e_km=valume*10
#         e=min(km,e_km)
#         self.valume-=e/10
#         if e>0:
#             print("电动车骑行:",e,"公里")
#         elif km>e:
#             super().run(km-e)

# b=EBicycle(5)
# b.run(10)
# b.run(100)
# b.fill_charge(6)
# b.run(70)
# b.run(10)

# class Car:
#     def run(self,speed):
#         print("汽车以",speed,"km/h的速度行驶")
# class Plane:
#     def fly(self,height):
#         print("飞机以海拔",height,"米的高度飞行")

# class Planecar(Car,Plane):
#     # """飞机汽车类，是继承　自 Car和Plane"""
#     pass

# p1=Planecar()
# p1.fly(2000)
# p1.run(299)

# def get_func():
#     def myadd(x,y):
#         return x+y
#     return myadd

# fx=get_func()
# print(fx(400,300))

# def make_power(y):

#     def fn(x):
#         return x**y
#     return fn

# pow2=make_power(2)
# print("5的平方是:",pow2(5))
# sn=0
# def fun(x):
#     sn=0

#     def fn(y):
#         nonlocal sn
#         for i in range(y+1):
#             sn+=x**i
#         return sn
#     return fn
# s=fun(3.1)
# print(s(10))
# def pr(fn):
#     def fx(name,x):
#         print("正在权限验证....")
#         fn(name,x)
#     return fx
# @pr
# def sa(na,x):
#     print(na,"存钱",x,"元")
# @pr
# def withd(na,x):
#     print(na,"正在办理取钱",x,"的业务")

# sa("小张",200)
# withd("线路",500)
# def fun():
#     def fx():
#         x=5
#         print(x)
#     return fx
# f=fun()
# f()

# def fun(x):
#     for x in range(2,x):
#         for y in range(2,x):
#             if x%y==0:
#                 break
#             else:
#                 print(x)
#                 break
# fun(16)


# def fun():
#     x=5
#     print(x)

# print(x)


# def fun(x):
#     for i in range(1,x+1):
#         if i % 2 == 0:
#             continue
#         else:
#             print(i)

# fun(10)
# def fun():
#     while True:
#         s=input("请输入姓名:")
#         if not s:
#             break
#         n=int(input("请输入年龄:"))
#         a=int(input("请输入成绩:"))

# class A:
#     def __init__(self,s):
#         self.s =s
#     # def __str__ (self):
#     #     return "数字%d"%self.s
#     def __repr__ (self):
#         return "%d"%self.s
# a=A(100)
# print(eval(a))

# 本示例示意with语句的用法
# 打开文件读取文件数据
# def read_file():
#     try:
#         f=open("ssss.py")

#         try:
#             while True:
#                 s=f.readline()
#                 if not s:
#                  break
#                 int(input("请输入任意数自己打印下一行:"))
#                 print(s)
#         finally:
#             print("文件关闭")
#             f.close()
#     except IOError:
#         print("程序异常已经捕获!")
#     except ValueError:
#         print("程序已转为正常状态")

# read_file()
# print("程序结束")

# def read_file():
#     try:
#         with open("ssss.py") as f
#             while True:
#                 s=f.readline()
#                 if not s:
#                     break
#                 int(input("请输入任意数自己打印下一行:"))
#                 print(s)
#     except IOError:
#         print("程序异常已经捕获!")
#     except ValueError:
#         print("程序已转为正常状态")

# read_file()
# print("程序结束")


# 本程序示意自定义的类作为环境管理器使用
# class FileWriter:
#     def __init__(self,filename):
#         self.filename=filename  #此属性用于记住文件名

#     def writeline(self,s):
#         '''此方法用于向文件内写入字符串，同时自动添加换行'''
#         self.file.write(s)
#         self.file.write('\n')

#     def __enter__(self):
#         '''此方法用于实现环境管理器'''
#         self.file=open(self.filename,'w')
#         print("已进入__enter__方法，文件打开成功")
#         return self  # 返回值用于 with中的as绑定

#     def __exit__(self,exec_type,exec_value,exec_tb):
#         '''
#         exec_type  为异常类型，没有异常时为None
#         exec_value 为错误的对象，没有异常时为None
#         exec_tb    为错误的traceback对象
#         '''
#         self.file.colse()
#         print("文件",self.filename,"已经关闭")
#         if exec_type is None:
#             print("退出with时没有发生异常")
#         else:
#             print("退出with时,有异常，类型是",exec_type,
#                 "错误是",exec_value)
#         print("__exit__方法被调用，已离开with语句")
# try:
#     with FileWriter('log.txt') as fw:
#         while True:
#             s=input("请输入一行:")
#             if s=='exit':
#                 break
#             if s=='error':
#                 raise ValueError("故意制造值的错误")
#             fw.writeline(s)
# except:
#     print("有错误发生,已转为正常")

# print("这是with语句之外，也是程序的最后一条语句")

# class FileWriter:
#     def __init__(self,filename):
#         self.filename=filename

#     def readline(self,s):
#         self.file.read(s)

#     def __enter__(self):
#         self.file=open(self.filename,'w')
#         print("已进入__enter_-方法，文件打开成功")
#         return self

#     def __exit__(self,exec_type,exec_value,exec_tb):

#         self.file.colse()
#         print("文件",self.filename,"已经关闭")
#         if exec_type is None:
#             print("退出with时没有发生异常")
#         else:
#             print("退出with时,有异常，类型是",exec_type,
#                 "错误是",exec_value)
#         print("__exit__方法被调用，已离开with语句")
# try:
#     a=input("输入原文件:")
#     with FileWriter(a) as fw
#     with


# except:
#     print("有错误发生,已转为正常")

# print("这是with语句之外，也是程序的最后一条语句")


# def mycp(src_file,dst_file):
#     """
#     src_file 原文件名
#     dst_file 目标文件名
#     """
#     try:
#         with open(src_file,'rb') as fr,\
#             open(dst_file,'wb') as fw:
#                 # 如果文件太大则分次搬运
#                 while True:
#                     b=fr.read(4096)# 文件太大时，控制字节串字符
#                     if not b:# 如果字节串为空，停止复制
#                         break
#                     fw.write(b)
#     except:
#         print("打开失败")
#         return False
#     return True

# def main():
#     src=input("请输入原文件名:")
#     dst=input("请输入目标文件名:")
#     if mycp(src,dst):
#         print("复制文件成功")
#     else:
#         print("复制文件失败")

# main()

# def mycp(src_file,dst_file):
#     """
#     src_file 原文件名
#     dst_file 目标文件名
#     """
#     fr=open(src_file,'rb')
#     fw=open(dst_file,'wb')
#     d=fr.read()
#     fw.write(d)
#     return True

# def main():
#     src=input("请输入原文件名:")
#     dst=input("请输入目标文件名:")
#     if mycp(src,dst):
#         print("复制文件成功")
#     else:
#         print("复制文件失败")

# main()

# class MyNumber:
#     def __init__(self,v):
#         self.data=v
#     def __repr__(self):
#         return "MyNuber(%d)" % self.data
#     def __add__(self,other):
#         print("__add__方法被调用")
#         obj=MyNumber(self.data+other.data)
#         return obj
#     def __sub__(self,other):
#         print("__sub__方法被调用")
#         obj=MyNumber(self.data-other.data)
#         return obj


# n1=MyNumber(100)
# n2=MyNumber(200)
# n3=n1.__add__(n2) # 等同于 n3=n1+n2
# print(n3)
# n4=n2-n1
# print(n4)
# class MyList:
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __add__(self,other):
#         obj=MyList(self.data+other.data)
#         return obj
#     def __mul__(self,other):
#         obj=MyList(self.data*other)
#         return obj
# l1=MyList([1,2,3])
# l2=MyList(range(4,7))
# l3=l1+l2
# print("l3=",l3)# MyList([1,2,3,4,5,6])
# l4=l1*2 # 实现乘法运算
# print("l4=",l4)
# class MyList:
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __mul__(self,other):
#         obj=MyList(self.data*other)
#         return obj
#     def __rmul__(self,lh):
#         print("__rmul__方法被调用,lh=",lh)
#         obj=MyList(self.data*lh)
#         return obj
# l1=MyList([1,2,3])
# l2=MyList(range(4,7))
# l4=l1*2 # 实现乘法运算
# print("l4=",l4)
# l5=2*l1
# print("l5=",l5)


# 此示例示意复合赋值算术运算符的重载
# class MyList:
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __add__(self,rhs):
#         print("__add__方法被调用")
#         return MyList(self.data+rhs.data)
#     def __iadd__(self,rhs):
#         print("__iadd__方法被调用")
#         self.data.extend(rhs.data)
#         return self

# l1=MyList([1,2,3])
# l2=MyList(range(4,7))
# l1+=l2  # 相当于 l1=l1+l2  优先用iadd方法否则用add方法
# print("l1=",l1)

# #此示例示意一元算术运算符的重载
# class MyList:
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __neg__(self):
#         print("__neg__方法被调用")
#         l=[-x for x in self.data]
#         return MyList(l)


# l1=MyList([1,-2,3,-4,5])
# print("l1=",l1)
# l2 = -l1
# print("l2=",l2)
# 此示例示意一元算术运算符的重载
# class MyList:
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __contains__(self,e):  # e 代表测试元素
#         print("__contains__方法被调用")
#         for x in self.data:
#             if e==x:# 如果相同，则说明e在列表中
#                 return True
#         return False

# l1=MyList([1,-2,3,-4,5])
# if 2 in l1:  # 需要重载 __contains__方法
#     print("2在l1中")
# else:
#     print("2不在l1中")

# class MyList:
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % class MyList:

#     def __init__(self, iterable):
#         self.data = [x for x in iterable]

#     def __repr__(self):
#         return "MyList(%s)" % self.data

#     def __getitem__(self, i):
#         if type(i) is slice:
#             print("正在进行切片操作")
#         elif type(i) is int:
#             print("正在进行索引操作")
#         print("__getitem__被调用", i)
#         return self.data[i]

#     def __setitem__(self, i, v):
#         print("__setitem__被调用")
#         self.data[i] = v


# l1 = MyList([1, -2, 3, -4, 5])
# print(l1[::2])self.data
#     def __getitem__(self,i):
#         print("__getitem__被调用",i)
#         return self.data[i]

# l1=MyList([1,-2,3,-4,class MyList:    def __init__(self,iterable):        self.data=[x for x in iterable]    def __repr__(self):        return "MyList(%s)" % self.data    def __contains__(self,e):  # e 代表测试元素        print("__contains__方法被调用")        for x in self.data:            if e==x:# 如果相同，则说明e在列表中                return True        return False l1=MyList([1,-2,3,-4,5])if 2 in l1:  # 需要重载 __contains__方法    print("2在l1中")else:    print("2不在l1中")5])
# print(l1[2])
# class MyList:
#     def __init__(self,iterable):
#         self.data=[x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __getitem__(self,i):
#         print("__getitem__被调用",i)
#         return self.data[i]
#     def __setitem__(self,i,v):
#         print("__setitem__被调用")
#         self.data[i]=v


# l1=MyList([1,-2,3,-4,5])
# print(l1[2])
# l1[1]=2
# print(l1)
# class MyList:

#     def __init__(self, iterable):
#         self.data = [x for x in iterable]

#     def __repr__(self):
#         return "MyList(%s)" % self.data

#     def __getitem__(self, i):
#         if type(i) is slice:
#             print("正在进行切片操作")
#         elif type(i) is int:
#             print("正在进行索引操作")
#         print("__getitem__被调用", i)
#         return self.data[i]

#     def __setitem__(self, i, v):
#         print("__setitem__被调用")
#         self.data[i] = v


# l1 = MyList([1, -2, 3, -4, 5])
# print(l1[::2])
# 练习：
#   实现有序集合类 OreerSet(), 能实现两个集合的交集 &, 并集 |,
#   补集 -, 对称补集 ^, ==， !=, 等操作(写集合相同)
#   要求：
#     集合内部用list存储
#     class OrderSet:
#         def __init__(self,iterable):
#             self.data = [x for x in iterable]
#             ...
#   测试用例：
#     s1=OrderSet([1,2,3,4])
#     s2=OrderSet([3,4,5])
#     print(s1 & s2)  # OrderSet([3,4])
#     print(s1 | s2)  # OrderSet([1,2,3,4,5])
#     print(s1 ^ s2)  # OrderSet([1,2,5])
#     if OrderSet([1,2,3]) != OrderSet([1,2,3,4]):
#         print("不想同")
#     其他自己测试 

# class OrderSet:
#     def __init__(self,a):
#         self.data=[x for x in a]
#         self.a=[]
#         self.b=[]
#         self.c=[]
#     def __repr__(self):
#         return "OrderSet(%s)" % self.data
#     def __and__(self,e):
#         for x in self.data:
#             for y in e.data:
#                 if x==y:
#                     break
#             else:
#                 self.a.append(x)
#         return set(self.a)
#     def __or__(self,a):
#         for x in self.data:
#             if x not in self.b:
#                 self.b.append(x)
#         for y in a.data:
#             if y not in self.b:
#                 self.b.append(y)

#         return set(self.b)
#      def __xor__(self,c):
# s1=OrderSet([1,2,3,4])
# s2=OrderSet([3,4,5]) 
# print(s1 & s2)
# print(s1 | s2)
# print(s1 ^ s2)
# class OrderSet:
#     def __init__(self,a):
#         self.data=set(x for x in a)

#     def __repr__(self):
#         return "OrderSet(%s)" % self.data
#     def __and__(self,e):
#         a=OrderSet((self.data) &(e.data))
#         return a
#     def __or__(self,a):
#         b=OrderSet((self.data)|(a.data))
#         return b
#     def __xor__(self,c):
#         c=OrderSet((self.data) ^ (c.data))
#         return c
#     def __eq__(self,d):
#         if self.data ==d.data:
#             return True
#         return False
#     def __ne__(self,e):
#         if self.data !=e.data:
#             return True
#         return False

# s1=OrderSet([1,2,3,4])
# s2=OrderSet([3,4,5])
# print(s1 & s2)
# print(s1 | s2)
# print(s1 ^ s2)
# if s1 == s2:
#     print("相同")

# if s1 != s2:
#     print("不相同")
# print(' *','\n',' ***','\n', '*****')
# S = "ABCDEFG"
# print(S[-2,-5])


# class student:
#     def __init__(self,n,s,a):
#         self.name=n
#         self.score=s
#         self.age=a
# def input_student():
#     l=[]
#     while True:
#         n = input("请输入名字:")
#         if not n:
#             break
#         a = int(input("请输入年龄:"))
#         s = int(input("请输入成绩:"))
#         stu=student(n,s,a)
#         l.append(stu)
#     return l
# def output_student():
#     df=input_student()
#     for stu in df:
#         print("姓名:",stu.name,
#              "年龄",stu.age,
#              "成绩:",stu.score)