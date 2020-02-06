# 递归函数

# 在函数内部，可以调用其他函数，如果一个函数在内部调用自身本身，
# 这个函数就是递归函数


# 求n！

'''
def fact(n):
    if  n == 1:
        return 1
    return n * fact(n - 1)

print(fact(10))
'''

# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈
# （stack）这种数据结构来实现的，每当进入一个函数调用，栈就会
# 加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是
# 无限的，所以，递归调用的次数太多，就会导致栈溢出。

# 使用尾递归的方式，可以在函数返回的时候，调用自身本身，并且
# return语句不能包含任何的表达式。这样编译器无论调用多少次
# 都只会占用一个栈帧，不会出现栈溢出的情况。


'''
def fact(n)
    return fact_iter(n,1)
    
def fact_iter(num,product):
    if num = 1:
        return product
    return fact_iter(num - 1,num * product)
    
# 可以看到return fact_iter(num - 1,num * product)仅返回递归函数
# 本身，num - 1 和 num * product在函数调用期间前就会被计算，不
# 影响函数调用。
'''

# 汉诺塔问题
# 请编写move(n,a,b,c)函数，它接收参数n，表示3个柱子A，B，C，
# 中第一个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到
# C的方法，例如：


def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        # 第n个盘子就是最下面的盘子
        # 将n - 1个盘子从A柱子借助C柱子移动到B柱子上
        move(n - 1,a,c,b)
        # 将A柱子上最下面的盘子，也就是第n个盘子移动到c柱子上
        print(a,'-->',c)
        move(n - 1,b,a,c)

print(move(6,'a','b','c'))    








