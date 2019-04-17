import re

# pattern=r'ab'
# #获取正则表达式对象
# obj=re.compile(pattern,flags=0)
# l=obj.findall("abcdabcabab",6,9)
# l=re.findall(pattern,'abcdabcabab',flags=0)
#print(l)
# pattern=r'\s+'
# obj=re.compile(pattern)
#匹配目标字符串进行切割
# l=obj.split('hello workd  hello kitty  nihao china')
# l=re.split(pattern,'hello workd  hello kitty  nihao china')
# print(l)
# pattern=r'\s+'
# obj=re.compile(pattern)
# #替换目标字符串中匹配到的内容
# s=obj.sub('##','hello workd nihao China')
# s=re.sub(pattern,'##','hello workd nihao China')
# print(s)


pattern=r'\s+'
obj=re.compile(pattern)
#替换目标字符串中匹配到的内容
s=obj.subn('##','hello workd nihao China')
print(s)