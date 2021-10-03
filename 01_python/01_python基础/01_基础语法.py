# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author  Zhang Zhibang

# 这里是函数基本用法
def fun1(name):
    message = "my name is " + name
    return message


# 这个相当于c语言main函数，当然python不写main函数也是可以运行的，不过py的每个文件都是一个模块，
# 在进行模块导入的时候，如果你的函数调用不在main里面会自动去调用，加了main函数，main内部的代码就不会在import的时候嗲用了
# 所以
if __name__ == '__main__':
    # 单分支语句
    if 3 >= 2:
        print("好耶")
    # 多分支语句
    level = 8
    if level == 10:
        print("A+")
    elif level == 9:
        print("A")
    elif level == 8:
        print("A-")
    elif level == 7:
        print("B")
    elif level == 6:
        print("C")
    # 三目运算符
    print("我是true") if level >= 10 else print("我错了")

    # while语句
    count = 0
    while count <= 9:
        print(count, end=' ')
        count += 1
    print()
    print("DONE")
    # # while和else可以一起使用
    while count <= 9:
        print(count, end=' ')
        count += 1
    else:
        print("while结束")

    # for循环
    # py的for循环都是去遍历一个可迭代的数据类型，比如列表，str
    print("-----for------")
    message = "hello"
    for m in message:
        print(m)
    # 有个函数range()可以当做决定迭代次数去使用
    for i in range(5):
        print(i, end=" ")
    # 测试一下range函数到底返回什么
    print(range(5))  # range(0, 5),其实他会转成一个list列表,最后也就是[0,1,2,3,4],迭代五次
    print(list(range(5)))  # 转成list

    # whlie和for打印99乘法表
    for j in range(1, 10):
        for i in range(1, j + 1):
            print("%d * %d = %d" % (j, i, j * i), end="\t")
        print()

    print("----- while99乘法表 -----")
    j = 1
    while j < 10:
        i = 1
        while i <= j:
            print("%d * %d = %d" % (j, i, j * i), end="\t")
            i += 1
        print()
        j += 1

    # 切片
    # 切片就是取出列表种得一个子列表
    # 切片操作针对的是由sequence，有顺序的，包括string tuple list
    mes = "python"
    print(mes[:])
    print(mes[1:len(mes)])
    print(mes[1:5:2])  # 最后面的数字是step步长
    print(mes[::-1])  # 步长为- 倒着取
    print(mes[-1:-3:-1])  # 到数第一个到到数第四个
    print(mes[-3:-1])  # 到数第一个到到数第四个

    # 数据类型
    # 首先分为基本数据类型和高级数据类型
    # 基本数据类型
    # number int（整数） long（长整型） float（双精度浮点数） complex（复数）
    # Boolean
    # string
    # 高级数据类型
    # tuple -- sequence(有序) 元组 不可修改
    # list -- sequence(有序) 列表 可修改
    # dict -- sequence(有序) 字典 映射
    # set 集合

    # 常用类型转换api
    # int() long() float() complex(real,[,imag])--创建一个复数 Complex()--转成复数 str() tuple() list() set() dict()
    # repr() -- 将对象x转换为表达式字符串
    # eval() -- 将字符串转成真实的表达式

