# 条件判断

# if条件判断

'''
age = 20
if age >= 18:
    print("your age is",age)
    print("adult")
else:
    print("your age is",age)
    print("teenager")
'''

# elif是else if的缩写，完全可以有多个elif，所以elif可以做更细致的判断

'''
age = 3
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
'''
    
# input读取用户的输入，这样就可以自己进行输入，但是要将字符串进行类型转换。

'''
birth = input("birth:")
birth = int(birth)
if birth < 2000:
    print("00前")
else:
    print("00后")
'''

# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮
# 小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5 - 25：正常
# 25 - 28：过重
# 28 - 32：肥胖
# 高于32：严重肥胖

heigth = input("请输入你的身高：")
heigth = float(heigth)
weigth = input("请输入你的体重：")
weigth = float(weigth)
flag = weigth/(heigth * heigth)

if flag > 32:
    print("bml指数为%.5f,严重配胖"% flag)
elif flag > 28:
    print("bml指数为%.5f,肥胖"% flag)
elif flag > 25:
    print("bml指数为%.5f,过重"% flag)
elif flag > 18.5:
    print("bml指数为%.5f,正常"% flag)
else:
    print("bml指数为%.5f,过轻"% flag)


