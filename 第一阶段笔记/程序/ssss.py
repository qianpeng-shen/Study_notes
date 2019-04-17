# a=[2,9,27,36,91,100]
# d=[x for x in filter(lambda x: x%3==0,a)]
# print(d)
# a=[2,9,27,36,91,100]
# for x in filter(lambda x: x%3==0,a):
#     print(x)
# a=[2,9,27,36,91,100]
# d=filter(lambda x: x%3==0,a)
# for x in d:
#     print(x)

def fun()
    for i in range(1,10):
        for x in range(1,i+1):
            print(str(i)+"*"+str(x)+"=",i*x,end=" ")
        print()
fun()

