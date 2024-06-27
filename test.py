print(123)

S1 = '123'
S2 = "123"
S3 = '''123'''
print(type(S1), type(S2), type(S3))
s4 = "It's ok"
s5 = 'It"s not'
s6 = '''
123
123
'''
print(type(s4), type(s5), type(s6))

# 转义符
s7 = 'hello \npython'
print(s7)

# 不希望被换行
path1 = 'D:\note1.txt'
path2 = 'd:\\note1.txt'
path3 = r'D:\note1.txt'
path4 = 'D:/note.txt'
print(path1, path2, path3, path4)

# 字符串的拼接
print('A' + 'B' + 'C')
print('A''B''C')
print('1' + 'abc')
print('a' * 5)

# 序列，索引（下标)和切片的特性
s = 'hello python'
# print(s[15]) # 越界
# 切片
# s[开始位置:结束位置]
print(s[1:3])
print(s[:8])
print(s[4:])
print(s[-3:])
# 步长,默认1
s = 'abcdefghijk'
print(s[2:8:1])
print(s[-4:-10:-1])

# 列表，也是序列，索引和切片,列表的元素可以是任意类型
list1 = [1, 3.14, 'a', [4, 8], (6, 8)]
# 在列表中添加内容append
# 方法一 在列表添加内容append
list1.append(3)
list1.append('a')
print(list1, type(list1))
# 方法二 指定位置插入，insert
list1.insert(0,666)
print(list1)

# 列表元素的修改，通过索引赋值
list1[-1] = 'A'
print(list1)
# 字符串不可以改变元素内容

# 列表的删除
list3 = [1, 2, 3]
# 方法一pop(),不指定下标，默认删除最后一位
list3.pop()
print(list3)
# 方法二pop(下标)，删除指定下标的值


# 方法三 remove(值)
list3.remove(1)
print(list3)
# 方法四 del list[下标]
del list3[-2]
print(list3)
del list3  # 删除列表

# 列表的拼接
list1 = [100, 200, 300]
list2 = [400, 500, 600]
s1 = 'abc'
list1.extend(list2)
list1.extend(s1)
print(list1)

# 元祖
t1 = (1, 3.14, 'abc')
print(type(t1))
# 元祖不可以改变元素内容
t1[1] = 333
print(t1)
# 列表和元祖的区别：
# 列表可以改变元素内容，元祖不可以改变元素内容
