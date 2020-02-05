'''
函数参数
定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义
就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，
以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，
调用者无需了解。

Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必
选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定
义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
'''


# 位置参数

'''
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5,2))
'''


# 默认参数

'''
def power(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    
print(power(5))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('yangjie','nan'))
'''

# 可变参数

'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,2,3]))
'''

# 定义可变参数和定义一个list或者tuple参数相比，仅仅在参数前面
# 加上了一个*号，在函数内部，参数numbers接收到的是一个tuple，
# 函数代码完全不变。但是，在调用该函数时，可以传入任意个参数
# 包括0个参数

'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2))
print(calc())
'''

# 关键字参数

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时
# 自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数
# 名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
