import pdb
import sys
def add(num1=0,num2=0):
    return int(num1) + int(num2)
def sub(num1=0,num2=0):
    return int(num1)-int(num2)
def main():
    print(sys.argv)
    #设置断点
    pdb.set_trace()
    additon=add(sys.argv[1],sys.argv[2])
    print(additon)
    subtraction=sub(sys.argv[1],sys.argv[2])
    print(subtraction)
main()