class CallTest(object):
    def __call__(self,a,b):
        print("Thie is call test")
        print("a=",a)
        print("b=",b)


test=CallTest()
test(1,3)
