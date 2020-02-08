# 切片

'''
L = ["yangjie","pangfu","momo","qingchun","bowen"]

# 正序取出前三个元素
print(L[0:3])

# 倒序取出后两个元素
print(L[-2:])

L = list(range(100))

# 前10个数
print(L[0:10])

# 后10个数
print(L[-10:])

# 10 - 20个数
print(L[10:20])

# 所有的数，每5个取一个
print(L[::5])

# 只写[:]就可以复制一个list
print(L[:])
'''

# tuple的切片操作

L = (0,1,2,3,4)
print(L[:3])


# 练习
# 请利用切片操作，实现一个trim()函数，去除字符串首尾的空格，
# 注意不要使用str的strip()方法：

# 本代码思路：第一个循环，切片字符串首字符，判断为空格则删除，
# 直到出现非空格为止，进入下一个循环。第二个循环，切片字符串
# 尾字符，判断为空格则删除。最后返回收尾无空格的字符串。

def trim(s):
    # 从前往后看，
    while len(s) >= 2 and s[0] == ' ':
        s = s[1:]
    while len(s) >= 2 and s[-1] == ' ':
        s = s[:-1]
    if s == ' ':
        s = ''
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


