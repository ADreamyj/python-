# 使用dict和set


# dict内置了词典：dict的支持，dict全称为dictionary，在其他语言
# 也称为map，使用键 - 值（key - value）存储，具有极快的查找速度。

'''
d = {"yangjie" : 30, "pangfu" : 20, "momo" : 21}
print(d["yangjie"])

# 避免key不存在的话，一是可以使用in判断key是否存在：
print("yangjie" in d)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None
# 或者自己指定的value：
print(d.get("fu"))
print(d.get("fu",-1))

# 删除一个key，用pop(key)的方法，对应的value也会从dict中删除
print(d.pop("momo"))
'''

'''
和list比较，dict有以下几个特点：

1.查找和插入的速度极快，不会随着key的增加而变慢；
2.需要占用大量的内存，内存浪费多。
而list相反：

1.查找和插入的时间随着元素的增加而增加；
2.占用空间小，浪费内存很少。
'''

# set和dict类似，也是一组key的集合，但不存储value。由于key
# 不能重复，所以在set中，没有重复的key
# 创建一个set的时候，要提供一个list作为输入集合：

'''
s = set([1,2,3])
for name in s:
    print(name)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
for name in s:
    print(name)

# 通过remove(key)的方式可以删除元素：
s.remove(4)
for name in s:
    print(name)
'''

# set可以看成数学意义上的无序和无重复元素的集合，
# 因此，两个set可以做数学意义上的交集、并集等操作：

'''
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)
'''

# replace()方法，也确实变出了'Abc'，但是变量a最后也是'abc'
a = 'abc'
b = a.replace("a","A")
print(a)
print(b)

