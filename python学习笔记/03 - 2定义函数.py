# 在Python中，定义一个函数要使用def语句，依次写出函数名，括号
# 括号中得参数和冒号：，然后，在缩进块中编写函数体，函数得返回
# 值用return语句返回。

# 我们以自定义一个绝对值得my_abs函数为例；

'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    
print(my_abs(-1000))
'''


# 空函数，什么也不做，可以使用pass，让代码先运行起来。

# 函数会检查出来，参数得个数，但是函数得类型有时候会检查不出来
# 所以我们可以使用写条件语句来检查函数参数的类型

'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs("20"))       
'''

# 函数可以返回多个值。

#表示导入math包，并允许后续代码引入math包里的sin，cos函数

'''
import math 

def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

r = move(100,100,60,math.pi/6)
print(r)
'''

# 练习：请定义一个函数quadratic(a,b,c)，接收3个参数，返回
# 一元二次方程ax^2 + bx + c = 0的两个解。

import math
def quadratic(a,b,c):
    if not isinstance(a, (int, float)) or a == 0:
        raise TypeError("argument 'a' must be number and cannot be zero")

    if not isinstance(b, (int, float)):
        raise TypeError("argument 'b' must be number")

    if not isinstance(c, (int, float)):
        raise TypeError("argument 'c' must be number")

    d = b**2 - 4 * a * c
    if d >= 0:
        x1 = (-b + math.sqrt(d) / (2 * a))
        x2 = (-b + math.sqrt(d) / (2 * a))
        return x1,x2
    else:
        return None
        
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


