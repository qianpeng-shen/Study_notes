
class human :
    def __init__(self,name):
        seld.name=name
        self.money=0
        self.sons=[]
    def make_money(self,m):
        self.money+=m
    def show_money(self):
        print(self.name,"共有"，self.moey,"元钱")
    def show_sonns(self):
        print("第",i+1,"个孩子是",self.sons[i].name)
    def show_sons(self):
        print(self.name,"共有:",len(self.sons),"个孩子")
        i=0
        while i < len(self.sons):
            print("第",i+1,"个孩子是",self.sons[i].name)
            i+=1
    def born_sons(self,name):
        son=human(name)
        self.sons.append(son)
        return son

h1.show_money()
h1.show_sons()
h1.make_money(30000)

s1=h1.born_sons("张大")
s2=h1.born_sons("张二")
s3=h1.born_sons("张三")
s1.make_money(20000)
s3.borrow_money(s1,1000)
s1.money-=1000
s3.money+=500
       