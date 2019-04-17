import random

# 获得数据库的属性的操作指令返回得到数据库信息的ＳＱＬ指令
class get_user(object):
    def __init__(self,name):
        pass

    def kjk(self,)


class pk(object):
    def __init__(self,use1,use2):
        self.use1=use1
        self.use2=use2
    def pkfangfa(self):
        s1 = self.user1.gongji - self.use2.fangyu
        s2 = self.user2.gongji - self.use1.fangyu
        if s1 > s2:
            s4=random.choice([1,2,3,4,5])
            self.use1.money += s4
            return self.use1.name
        elif s1 < s2:
            self.use2.money-=s4
            return self.use2.name
        else:
            return '='
        