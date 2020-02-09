# 迭代

'''
Python的for循环抽象程度要高于c的for循环，因为Python的for
循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

list这种数据类型虽然有下标，但是有很多数据类型是没有下
标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，
比如dict就可以迭代。
'''

'''
d = {'a' : 1, 'b' : 2, 'c' : 3}
for key in d:
    print(key)
'''

# 如何判断一个对象是可迭代对象呢？
# 方法是通过collections模块的Iterable类型判断：

'''
from collections import Iterable
print(isinstance('abc',Iterable))

print(isinstance([1,2,3], Iterable))
'''

for i,value in enumerate(['a','b','c']):
    print(i,value)
    
# 练习：使用迭代查找一个list中最小和最大值，并返回一个tuple

def findMinAndMax(arr):
    min = max = None
    
    if len(arr) == 0:
        return min,max
    
    for x in arr:
        if min == None or min > x:
            min = x
            
        if max == None or max < x:
            max = x
    return min,max
    
    
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

