# a=int(input("输入:"))
# b=1
# i=1
# c=0
# while i<=a:
#     if i<4:
#         c+=b
#         # print(b,c)
#     if i>=4:
#         b+=1
#         c+=b
#         c-=1
#         # print(b,c)
#     i+=1
# print(c+b)





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
#             return



# main()

# def fdu():
#     s=10
#     for x in range(1,5):
#         s+=2
#     return s
# print(fdu())
# import time
# def myfn(n):

    
#     """myfn函数是输出n编的"hello world"n为参数"""
#     if n==0:
#         return 
#     print("hello world")
#     time.sleep(1)
#     return myfn(n-1)

# myfn(100)

# l1=[x for x in map(lambda x,y: x+y,[1,2,3,4],[5,6,7])]
# print(l1)
# n=filter(lambda x:x%2==1,l1)
# for x in n:
#     print(x)

# def hello():
#     print("hello aaa")
#     print("hello bbb")
#     return # 用于返回到调用的地方
#     print("hello ccc")

# # # v=hello()
# # print(hello())
# hello()
# a=100
# b=200
# s=input("请输入字符串:")
# m=eval(s)
# n=exec(s)
# print(m)

# print(n)

# import time 
# def show_time():
#     while True:
#         t=time.localtime()
#         # s="\r %02d:%02d:%02d"% (t[3],t[4],t[5])
#         s="\r %02d:%02d:%02d"% t[3:6]
#         print(s,end="")
#         time.sleep(1)
# show_time()
 
# import time 
# def show():
# t=time.localtime()
# s="%2d:%2d:%2d" %t[3:6]
# print(s)
#     print(s)
# show()
# y=int(input("输入年"))
# m=int(input("输入月"))
# d=int(input("输入日"))
# t=time.mktime((y,m,d,0,0,0,0,0,0))
# print(t)
# d=time.localtime(t)
# w=d[6]
# print(w)
# er=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
# print(er[w])
# qw=time.time()-t
# asd=qw/(60*60*24)
# print(asd)


# import sys
# def fun():
#     print("进入函数")
#     sys.exit()
#     print("退出函数")

# fun()
# print("退出程序")

# def fun():
#     print("hello")

# def _fun():
#     print("hello")


# name="tarena"
# _name="world"
# import random as r
# s=[]
# for x in range(1,10):
#     s.append(x)
# for d in range(97,123):
#     s.append(chr(d))
# for b in range(65,91):
#     s.append(chr(b))
# print(s)
# a=r.sample(s,6)
# print(a)
# def get_random_passwd(n):
#     source=[0,1, 2, 3, 4, 5, 6, 7, 8, 9,a,b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z,_]
#     s=''
#     for _ in range(n):
#         s+=r.choice(source)
#     return s
# print("生成的密码:",get_random_passwd(6))
# １．编写一个闹钟程序，启动设置定时时间：
# (小时和分钟)到时间后打印"时间到......"然后退出程序
# import time 
# def myfun():
#     a=int(input("请输入您要设定的小时:"))
#     b=int(input("请输入您要设置的分钟:"))
#     while True:
#         t=time.localtime()
#         print(t[3], t[4], t[5])
#         time.sleep(1)
#         if t[3]==a and t[4]==b:
#             return print("时间到,时间为","%2d" %t[3],"小时","%2d" %t[4],"分钟")
#             break

# myfun()

# ２．模拟斗地主发牌，扑克牌共54张:
# 花色：
# 　　黑桃('\u2660'),梅花('\u2663')
#   方块('\u2665'),红桃('\u2666')
#   数值：
#   A2-10JQK
#   大小王
#   三个人，每人发17张牌，底牌三张
#   输入回车，打印第一个人17张牌
#  　输入回车，打印第二个人17张牌
#  　输入回车，打印第三个人17张牌
#  再输入回车，打印三张底牌
# import random as r
# def fun():
#     z = []
#     s = []
#     a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
#     b = ["A", "J", "Q", "K"]
#     d = ["BK","SK"]
#     for x in a:
#         z.append('\u2660' + str(x))
#         z.append('\u2663' + str(x))
#         z.append('H\u2665' + str(x))
#         z.append('\u2666' + str(x))
#     for c in b:
#         z.append('\u2660' + str(c))
#         z.append('\u2663' + str(c))
#         z.append('H\u2665' + str(c))
#         z.append('\u2666' + str(c))
#     for f in d:
#         z.append(f)
#     for t in z:
#         m = "+" + "----" + "+\n" + "|" + t.center(4) + "|\n" + "+" + "----" + "+"
#         s.append(m)
#     return s
# def fun1(s):
#     df=[]
#     sx=[]
#     kn=[]
#     for x in range(17):
#         az=r.choice(s)
#         df.append(az)
#         s.remove(az)
#     for o in range(17):
#         kl=r.choice(s)
#         sx.append(kl)
#         s.remove(kl)
#     for g in range(17):
#         lm=r.choice(s)
#         kn.append(lm)
#         s.remove(lm)
#     if input("请输入回车")=="":
#         print("第一个人的牌:")
#         for x in df:
#             print(x)
#     if input("请输入回车")=="":
#         print("第二个人的牌:")
#         for x in sx:
#             print(x)
#     if input("请输入回车")=="":
#         print("第三个人的牌:")
#         for x in kn:
#             print(x)
#     if input("请输入回车")=="":
#         print("最后三张:")
#         for x in s:
#             print(x)



# lmk=fun()
# fun1(lmk)


    

# class MyInteger:
#     def __init__(self,value):
#         self.data=value
#     # def __repr__(self):
#     #     return 'MyInteger(%d)' % self.data
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
# class MyNumber:
#     def __init__(self,value):
#         self.data=value
#     def __str__(self):
#         print("__str__方法被调用")
#         return "数字: %d" % self.data

# n1=MyNumber(100)
# # print(str(n1)) # 此句其实等同于print(n1)
# print(n1)
# # print(repr(n1))#他会调用n1.__repr__()方法
class MyNumber:
    def __init__(self,value):
        self.data=value
    def __str__(self):
        print("__str__方法被调用")
        return "数字: %d" % self.data

    def __repr__(self):
        """此方法供repr(obj)函数调用!"""
        print("调用repr")
        return "MyNumber(%d)" % self.data
n1=MyNumber(100)
print(str(n1)) 
print(n1)
print(repr(n1))
##################
MyNumber(100)
MyNumber(100)
MyNumber(100)