# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# author  Zhang Zhibang


if __name__ == '__main__':
    print("开始学习函数")


    # 1. 基本使用
    # 1.1 定义与调用
    def mytest(name, age):
        print("my name is %s,my age is %d" % (name, age))


    mytest("catalina", 18)


    # 1.2 函数注释
    def mytest():
        """这里测试函数的注释"""
        return 0;


    print(mytest.__doc__)


    # 2. 变量
    ## 2.1 局部变量
    def mytest1():
        a = 3
        return a


    # def mytest2():
    # return a # 报错
    # mytest2()
    ## 全局变量
    a = 3


    def mytest1():
        print(a)
        global b  # 声明为全局变量
        b = 10
        return b


    def mytest2():
        return b  # 报错


    mytest1()
    print(mytest2())


    # 3. 默认参数和可变参数
    # 3.1 默认参数
    def mytest(name, age, score=100):
        print("my name is %s,my age is %d" % (name, age))
        print(score)


    mytest("zzb", 18)
    mytest("zzb", 18, 60)


    # 3.2可变参数
    # 一个*会将变量转成一个元组，不传值就是()
    def mytest(name, age, *hobby):
        print("my name is %s,my age is %d" % (name, age))
        print(hobby)


    mytest("zzb", 18)
    mytest("zzb", 18, "篮球", "羽毛球", "乒乓球")


    # 两个*会将变量转成一个字典，不传值就是{}
    def mytest(name, age, **hobby):
        print("my name is %s,my age is %d" % (name, age))
        print(hobby)


    mytest("zzb", 18)
    mytest("zzb", 18, lq="篮球", ymq="羽毛球", ppq="乒乓球")

    # 3.3 递归
    data = list(range(1, 101))
    print(data)


    def my_add(a, b):
        if len(a) == 2:
            return a[0] + a[1] + b
        return my_add(a[:-1], a[-1]) + b


    my_add(data[:-1], data[-1])

    # 3 函数式编程
    # 高阶函数就是说的函数式编程，以函数为中心，把函数传来传去
    mydata = [123, 1, 6.2e8]


    def myfunc(num):
        return num * 2


    def convert(func, data):
        print("将序列中的值转换为统一的数值类型")
        return [func(eachNum) for eachNum in data]


    print(convert(int, mydata))
    print(convert(float, mydata))
    print(convert(myfunc,mydata))

    # 4