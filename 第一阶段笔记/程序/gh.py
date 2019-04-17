class student:
    pass
def input_student():
    l=[]
    while True:
        n = input("请输入名字:")
        if not n:
            break
        a = int(input("请输入年龄:"))
        s = int(input("请输入成绩:"))
        stu=student()
        stu.name=n
        stu.age=a
        stu.score=s
        l.append(stu)
    return l
def output_student():
    df=input_student()
    for x in df:
        print("姓名:",x.name,
             "年龄",x.age,
             "成绩:",x.score)
output_student()
def fun():
    x=100
print(x)