# 使用list和tuple

# python 内置的一种数据类型就是列表：
# list是一种有序的集合，可以随时添加和删除其中的元素。

# 用len()函数可以获取list元素的个数。

# 索引来访问list中每一个位置的元素，记得索引是从0开始的。

classmates = ['Michael','Bob','Tracy']
print(classmates)

'''
print(len(classmates))
print(len(classmates[0]))
print(len(classmates[1]))
print(len(classmates[2]))

print(len(classmates[-1])) # -1结尾的话是倒数第一个元素

'''

# append()list是可变的有序表，可以在list中追加元素到末尾。

# insert()在指定元素的位置加上元素。

# pop()删除list末尾的元素。pop(i)方法删除指定元素的位置

# 用索引可以将元素替换为别的元素，可以直接赋值给对应的索引位置。

# list里面的元素的数据类型也可以是不同的。

'''
classmates.append('yangjie')
print(classmates)

classmates.insert(1,'pangfu')
print(classmates)

classmates.pop()
print(classmates)

classmates[2] = 'yangjie'
print(classmates)

classmates.append(20)
print(classmates)
'''

# 另一种有序列表叫做元组：tuple
# tuple和list非常相似，但是tuple一旦初始化，就不能修改。

# tuple要是表示一个元素的话。可以在后面加上一个','

'''
t = (1,)
print(t)
'''

# 可变的tuple是在tuple的基础上加上了list，

t = (1,2,[3,4])
t[2][0] = 5
t[2][1] = 6
print(t)

# 请用索引取出下面的list的指定元素：

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],L[1][1],L[2][2])






