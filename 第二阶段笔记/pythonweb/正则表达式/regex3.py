import re 
# s="Hello World"
# l=re.findall('h\w+',s,re.I)
# print(l)

#M          对元字符　^ $ 起作用，可以匹配每一行的开头结尾位置
# s='''hello world
# Hello kitty
# nihao China
# '''
# l=re.findall('China$',s,re.M)
# print(l)

#S      对元字符　. 起作用　让其可以匹配换行
# s='''hello world
# Hello kitty
# nihao China
# '''
# l=re.findall('.+',s,re.S)
# print(l)

s='''Hello world
Hello kitty
nihao China
'''
pattern ='''(?P<dog>hello)#dog组
\s+#空字符
(world)#第二组用来匹配'''
l=re.findall(pattern,s,re.X | re.I)
print(l)
