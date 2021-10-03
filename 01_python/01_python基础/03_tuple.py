# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# author  Zhang Zhibang


if __name__ == '__main__':
    print("开始学习tuple")

    # 元组的各种操作 元组不能修改
    # 1元组的创建
    # 通过（）创建
    a = (1, 2, 3)  # 用（）创建元组
    b = 1, 2, 3  # 不用（）创建元组
    c = (1,)  # 创建只有一个元素的元组
    d = ()  # 创建一个空的元组
    print(a, b, c, d)

    # 通过tuple（）创建
    a = tuple("abc")
    b = tuple(range(3))
    c = tuple((1, 2, 3))
    print(a, b, c)

    # 2元组的基本操作
    # 2.1元组不能修改/赋值

    # 2.2元组切片
    a = (1, 2, 3, 4, 5)
    print(a[:])
    print(a[2:])
    print(a[:3])

    # 2.3元组的排序 没有tuple.sort
    a = (2, 1, 5, 4, 3)
    print(sorted(a))

    # 3zip
    a = (1, 2, 3)
    b = ('你', '你', '他')
    print(tuple(zip(a, b)))  # 将二者zip起来形成二维元组
    print(list(zip(a, b)))  # 将二者zip起来形成二维列表

    # 4生成器
    a = (x ** 2 for x in range(5))
    print(tuple(a))
    print(tuple(a))

    a = (x ** 2 for x in range(5))
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
