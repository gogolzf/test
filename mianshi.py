# 一行代码实现1--100之和
# print(sum(range(0, 101)))

# 如何在一个函数内部修改全局变量
a = 10
def test():
    global a
    a = 5
test()
# print(a)

# 字典如何删除键和合并两个字典
dict1 = {'name': 'lin', 'ID': 1}
del dict1['name']
dict2 = {'test': 'fan'}
dict1.update(dict2)

# python实现列表去重的方法
list1 = [3, 2, 1]
# a = set(list1)
# list1 = list(a)
# print(list1)

# python2和python3的range（100）的区别
# python2返回列表 python返回迭代器
list2 = []
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list2.append(i)
# print(sum(list2))

#列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
list3 = [1, 2, 3, 4, 5]
def fn(x):
    return x**2

res = map(fn, list3)
res = [i for i in res if i > 10]
print(res)

# python中生成随机整数、随机小数、0--1之间小数方法
import random
# print(int(random.uniform(1,10))) # 随机整数
# print(random.random()) # 0-1之间的整数
# print('%.2f'%float(random.uniform(1,10))) # 小数随机数保留两位小数

# python中断言方法举例
m = 1
# assert (m>0)
# print("断言成功，程序继续")
# assert (m>2)
# print("断言失败，程序报错")

# 数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句

# select distinct name from student

# 10个Linux常用命令
# ls cp cd vim cat mkdir mv find pwd rm

# python2和python3区别？列举5个
# Python2 print不需要括号 python3 需要括号
# Python2 rang返回列表 python返回迭代器
# Python2 raw_input python3是input

#列出python中可变数据类型和不可变数据类型，并简述原理
# 不可变的数据类型：数值型，字符串型string和元组tuple
# 可变的数据型: 列表list，字典dict

# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse=False)
# for m in range(len(s)):
#     print(s[m])

# 用lambda函数实现两个数相乘,比较大小
data = lambda a, b: a * b
data1 = lambda x, y: x if x > y else y


# 字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
dict1 = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
data = sorted(dict1.items(), key=lambda i: i[0], reverse=False)
print(data)
# 利用collections库的Counter方法统计字符串每个单词出现的次数
from collections import Counter
str = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(str)

# 字符串a = "not 404 found 张三 99 深圳" 输出"张三 深圳"
a = "not 404 found 张三 99 深圳"
data = a.split(" ")

