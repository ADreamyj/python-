# 循环

# python的循环方式有两种，一种是for ... in 循环，依次把list
# 或者tuple中的每个元素迭代出来，看例子：

# 依次把list或tuple中的每个元素迭代出来，看例子

'''
names = ["yangjie","pangfu","momo"]
for name in names:
    print(name)
'''

# range()函数，可以生成一个整数序列，再通过list()函数转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数：

# print(list(range(5)))


# 如果要提前结束循环，可以用break语句：

'''
n = 1
while n <= 100:
    if n > 10:# 当n = 11时，执行break语句
        break# break语句会结束当前循环
    print(n)
    n = n + 1
print("END")
'''

# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，
# 直接开始下次循环

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
    

# 练习
# 请利用循环依次对list中的每个名字打印出Hello,xxx!

'''
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello,",name)
'''

