# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# author  Zhang Zhibang


if __name__ == '__main__':
    print("start to say something about set")
    print("----- 基本用法 -----")
    # 1.创建列表
    # 基本用法
    aList = [1, 2, 3, 4, 5]
    bList = list([2, 4, 6, 7, 9])
    print(aList)
    print(bList)

    print("----- 列表生成 -----")
    # 基本方式创造列表
    aList = []
    for x in range(1, 6):
        aList.append(x)
    print(aList)
    # 推导式生成列表
    a = [x ** 2 for x in range(1, 5, 2)]
    b = [x for x in range(1, 5)]
    c = [x for x in range(1, 20) if x % 5 == 0]
    print(a)
    print(b)
    print(c)

    print("----- 列表操作 -----")
    # 2.列表操作
    # 2.1append添加列表元素
    aList = []
    for x in range(1, 6):
        aList.append(x)
    print(aList)

    # 2.2用+号拼接list
    a = [1, 2, 3]
    b = [4, 5]
    print(a + b)
    print(b + a)

    # 2.3extend方法
    a = [1, 2, 3]
    b = [4, 5]
    print(id(a))
    a.extend(b)
    print(a)
    print(id(a))

    # 2.4insert()实现列表插入元素
    a = [1, 3, 4]
    a.insert(1, 2)
    print(a)

    # 2.5获取列表中的第几个元素
    a = [1, 2, 3]
    print(a[2])

    # 2.6从右侧获取
    a = [1, 2, 3]
    print(a[-2])

    # 2.7索引溢出
    a = [1, 2, 3]
    print(a[4])  # IndexError: list index out of range

    # 2.8使用index获取元素首次出现的索引
    a = [1, 2, 3, 4, 5, 1, 99, 0]
    print(a.index(2))
    print(a.index(1, 3))  # 从索引3后面开始查第一个1

    # 2.9修改
    a = [1, 2, 3]
    a[2] = 2
    print(a)

    # 2.10删除
    a = [1, 2, 3]
    del a[1]
    print(a)

    a.pop()  # 弹出最后一个元素并返回
    print(a)

    a = [1, 2, 3, 2]
    a.remove(2)  # 删除第一个值为2的元素
    print(a)

    # 2.11列表的乘法
    a = [1, 2, 3]
    a = a * 3
    print(a)

    # 2.12列表的三个函数
    a = [1, 2, 3]
    print(len(a))
    print(max(a))
    print(min(a))

    # 3列表的常用方法
    # 3.1copy
    a = [1, 2, 3]
    b = a  # 深拷贝
    b[1] = 1000
    print("list a is", a)
    print("list b is", b)

    a = [1, 2, 3]
    c = a.copy()  # 浅拷贝
    c[1] = 1000
    print("list a is", a)
    print("list c is", c)

    # 3.2count
    a = [1, 2, 3, 1, 1]
    print(a.count(1))
    print(a.count(2))

    # 3.3reverse
    a = [1, 2, 3]
    a.reverse()
    print(a)

    # 3.4sort
    a = [1, 3, 2]
    a.sort()  # 改变原list
    print(a)
    a.sort(reverse=True)  # 递减排序
    print(a)

    a = [1, 3, 2]
    b = sorted(a)  # 不改变原list
    print(a)
    print(b)

    a = [1, 3, 2]
    a = sorted(a, key=lambda x: -x)  # 按照lambda进行排序，这里是把元素改成负数之后升序排序，然后最后不会改变list元素的值
    print(a)
