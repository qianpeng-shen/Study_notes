#通过pymngo进行增删改查操作
from pymongo import MongoClient


#创建连接对象
conn=MongoClient('localhost',27017)
#创建集合对象和数据库对象
db=conn.stu 
my_set=db.class4
#__getitem__  __setitem__
# db=conn['stu']
# my_set=db['class3']
# print(my_set)
# print(dir(my_set))


#插入数据
# my_set.insert({'name':'阿狸','King':'法师'})
# my_set.insert([{'name':'猴子','King':'刺客'},{'name':'诸葛亮','King':'法师'}])
# my_set.insert_many([{'name':'杨戬','King':'战士'},{'name':'鱼','King':'坦克'}])

# my_set.insert_one({'name':'鲁班','King':'射手'})

# my_set.save({'name':'百丽','King':'射手'})


#删除数据
# my_set.remove({'name':'百丽'})
# #只删除一条符合条件文档
# my_set.remove({'name':'鲁班'},multi=False)
# #删除所有文档
# my_set.remove()


#查找操作
# cursor=my_set.find({},{'_id':0})
# for i in cursor:
#     print(i['name'],'------',i['King'])

cls=db.class0
#使用到修改器
cursor=cls.find({'gender':{'$exists':True}},{'_id':0})
# for i in cur:
    # print(i)
# print(cursor)
# print(cursor.next())
# print(cursor.count())

# for i in cursor.skip(2).limit(3):
#     print(i)
# for i in cursor.sort([('name',1)]):
#     print(i)

# dic={'$or':[{'name':{'$gt':'Tom'}},{'gender':'w'}]}
# data=cls.find_one(dic)
# print(data)

##修改操作
# my_set.update({'name':'阿狸'},{'$set':{'name':'狐狸'}})

## 如果文档不存在则插入文档
# my_set.update({"name":'冰冰'},{'$set':{'King':'武则天'}},upsert=True)

#修改多条文档
# my_set.update({'King':'法师'},{'$set':{'King_name':'铭文'}},multi=True)


# my_set.update_many({'King':'射手'},{'$set':{'King_name':'末世'}})

# my_set.update_one({'King_name':None},{'$set':{'King_name':'恢弘'}})

#查找并删除查找结果会返回
# print(my_set.find_one_and_delete({'name':'冰冰'}))








conn.close()
