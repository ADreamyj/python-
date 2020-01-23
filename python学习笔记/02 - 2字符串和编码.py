# 字符串和编码


# print('包含中文的str')

# ord()获取字符的整数表示
# chr()函数把编码转换为对应的字符


'''
print(ord('A'))
print(ord('a'))
print(ord('中'))
print(chr(66))
print(chr(67))
'''


# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：

# print('ABC'.encode('ascii'))

# 要把byte变为str，就需要用decode()方法：

# print( b'ABC'.decode('ascii'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：

# print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 计算字符的长度len()函数，len()函数计算的是str的字符数，如果换成bytes，len()就计算字节数

# print(len("ABC"))

# 格式化方式与c语言是一致的
'''

print('Hello, %s'% 'world' )

print('Hi, %s, you have $%d.' % ('Michael',1000000))

print('%2d-%02d' % (3, 1))

print('%.2f' % 3.1415926)

print('growth rate: %d %%' % 7)
'''

# format()格式化字符串

# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点

'''
s1 = 72
s2 = 85
r = (s2/s1 - 1)*100
print("小明的成绩提升：%.1f %%" % r)
'''



