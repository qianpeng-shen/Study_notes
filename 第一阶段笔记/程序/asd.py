class Dog:
    '''这是一个类，用于描述一个小动物的行为'''
    def eat(self,food):
        '''小狗有吃东西的行为'''
        print("小狗吃了:",food)


#实例.实例方法名(调用参数)
dog1=Dog()  # 创建一个实例对象
dog1.eat("骨头")  # 让狗吃东西

dog2=Dog()  # 再创建一个实例对象
dog2.eat("包子")

