# -*- coding: utf-8 -*-


#%%
#IO编程

#文件读写
#读文件open()
f = open('testio.txt', 'r')
#文件不存在，open()函数就会抛出一个IOError的错误
print f.read(4)
f.close()
try:
    f = open('testio.txt', 'r')
    print f.read(4)
finally:
    if f:
        f.close()
with open('testio.txt', 'r') as f:
    print f.read(4)
#read()一次读取文件的全部内容 str对象
#read(size)方法，每次最多读取size个字节的内容
#readline()可以每次读取一行内容
#readlines()一次读取所有内容并按行返回list
#for line in f.readlines():
#    print(line.strip()) # 把末尾的'\n'删掉
#

#
#字符编码
#要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件
#f = open('/Users/michael/gbk.txt', 'rb')
#u = f.read().decode('gbk')
#u #u'\u6d4b\u8bd5'
#print u #测试
#自动转换
#import codecs
#with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
#    f.read() # u'\u6d4b\u8bd5'
#
#写文件
#标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('testio.txt', 'w')
f.write('Hello, world!')
f.close()#会覆盖原来的内容
with open('testio.txt', 'w') as f:
    f.write('Hello, world!')



#%%

#正则表达式
'''
字符串是编程时涉及到的最多的一种数据结构，
对字符串进行操作的需求几乎无处不在。
比如判断一个字符串是否是合法的Email地址，
虽然可以编程提取@前后的子串，
再分别判断是否是单词和域名，
但这样做不但麻烦，而且代码难以复用。
正则表达式是一种用来匹配字符串的强有力的武器。
它的设计思想是用一种描述性的语言
来给字符串定义一个规则，凡是符合规则的字符串，
我们就认为它“匹配”了，否则，该字符串就是不合法的。
所以我们判断一个字符串是否是合法的Email的方法是：
1.创建一个匹配Email的正则表达式；
2.用该正则表达式去匹配用户的输入来判断是否合法。
因为正则表达式也是用字符串表示的，
所以，我们要首先了解如何用字符来描述字符。
在正则表达式中，如果直接给出字符，就是精确匹配。
用\d可以匹配一个数字，\w可以匹配一个字母或数字，
所以：
•'00\d'可以匹配'007'，但无法匹配'00A'；
•'\d\d\d'可以匹配'010'；
•'\w\w\d'可以匹配'py3'；
.可以匹配任意字符，所以：
•'py.'可以匹配'pyc'、'pyo'、'py!'等等。
要匹配变长的字符，在正则表达式中，
用*表示任意个字符（包括0个），用+表示至少一个字符，
用?表示0个或1个字符，用{n}表示n个字符，
用{n,m}表示n-m个字符：
来看一个复杂的例子：\d{3}\s+\d{3,8}。
我们来从左到右解读一下：
1.\d{3}表示匹配3个数字，例如'010'；
2.\s可以匹配一个空格（也包括Tab等空白符），
所以\s+表示至少有一个空格，例如匹配' '，'   '等；
3.\d{3,8}表示3-8个数字，例如'1234567'。
综合起来，上面的正则表达式可以匹配以任意个
空格隔开的带区号的电话号码。
如果要匹配'010-12345'这样的号码呢？
由于'-'是特殊字符，在正则表达式中，
要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。
但是，仍然无法匹配'010 - 12345'，
因为带有空格。所以我们需要更复杂的匹配方式。
进阶
要做更精确地匹配，可以用[]表示范围，比如：
•[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
•[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者
下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
•[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或
下划线开头，后接任意个由一个数字、字母或者
下划线组成的字符串，也就是Python合法的变量；
•[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地
限制了变量的长度是1-20个字符（前面1个字符+后面
最多19个字符）。
A|B可以匹配A或B，所以(P|p)ython可以
匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
你可能注意到了，py也可以匹配'python'，
但是加上^py$就变成了整行匹配，就只能匹配'py'了。
'''
#re模块
#由于Python的字符串本身也用\转义，所以要特别注意
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'
#使用Python的r前缀，就不用考虑转义的问题了
s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'
import re
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
#<_sre.SRE_Match object at 0x1026e18b8>
print re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
#match()方法判断是否匹配，如果匹配成功，
#返回一个Match对象，否则返回None
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print 'ok'
else:
    print 'failed'
#
#切分字符串
#用正则表达式切分字符串比用固定的字符更灵活
print 'a b   c'.split(' ')
print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,]+', 'a,b, c  d')
print re.split(r'[\s\,\;]+', 'a,b;; c  d')
#
#分组
#提取子串的强大功能。用()表示的就是要提取的分组（Group）
#比如：^(\d{3})-(\d{3,8})$分别定义了两个组，
#可以直接从匹配的字符串中提取出区号和本地号码
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m
print m.group(0)
print m.group(1)
print m.group(2)
print m.groups()
#group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m.groups()
#
#贪婪匹配
#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print re.match(r'^(\d+)(0*)$', '102300').groups()
#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串
#必须让\d+采用非贪婪匹配（也就是尽可能少匹配），
#才能把后面的0匹配出来，
#加个?就可以让\d+采用非贪婪匹配：
print re.match(r'^(\d+?)(0*)$', '102300').groups()
#
#编译
#在Python中使用正则表达式时，re模块内部会干两件事情：
#1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
#2.用编译后的正则表达式去匹配字符串
#出于效率的考虑，我们可以预编译该正则表达式，
#接下来重复使用时就不需要编译这个步骤了
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()
print '-------------------------------------------------------'
#%%
# -*- coding: utf-8 -*-
#
L=[i*i for i in range(5)]
print(L)
for i in reversed(L):
    print(i)
for index,data in enumerate(L,1):
    print("%s:%s"%(index,data))
L2=range(2,7)
for i in zip(L,L2):
    print(i)
for i,j in zip(L,L2):
    print("%s+%s"%(i,j))
print(map(lambda x:x*x,range(1,5)))
n=5
isum=0
while n > 0:
    isum = isum + n
    n = n - 2
#

#%%
#使用list和tuple
#list
classmates = ['Michael', 'Bob', 'Tracy']
print len(classmates)
print classmates[0]
print classmates[-1]
classmates.append('Adam')#追加
print classmates
classmates.insert(1, 'Jack')#插入
print classmates.pop()#删末尾
print classmates
classmates.pop(1)#删指定
classmates[1] = 'Sarah'
alist = ['python', True, [100, 'php'], 'scheme']
print alist
print alist[2][1]
a=[[0 for i in range(5)] for i in range(3)]
b=[[a[i][j] for i in range(3)] for j in range(5)]