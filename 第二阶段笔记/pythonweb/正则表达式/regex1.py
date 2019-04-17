import re

# #匹配内容返回迭代器
# it=re.finditer(r'\d+','2008年是个多事之秋,512地震,08奥运等')
# for i in it:
#     print(dir(i))
#     print(i.group())


#match　匹配
obj=re.match('foo','foo,food on the table')

print(obj.group())
#search匹配
obj=re.search('foo','Foo,food on the table')

print(obj.group())

try:
    obj=re.fullmatch('\w+','abcde123')
    print(obj.group())
except AttributeError as e:
    print(e)