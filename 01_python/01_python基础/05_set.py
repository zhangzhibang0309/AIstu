# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# author  Zhang Zhibang


if __name__ == '__main__':
    print("开始学习set")

    # 1. 集合的创建
    # 1.1 使用{}创建 集合值唯一可变无序
    a = {1, 2, 3}
    print(a)
    # 1.2使用set（）将列表 元组等可迭代对象转成集合 自动去重
    a = [1,1,2,3,4,5]
    print(set(a))

    # 2. 集合的添加
    a = {1, 2, 3}
    a.add(100)
    print(a)

    # 3. 集合的删除
    a = {1, 2, 3}
    a.remove(2)
    print(a)
    a.clear() # 清空
    print(a)
    # 4. 集合的其他操作
    a = {1, 3, "zzb"}
    b = {"zzb", "jklv", 282}
    # 4.1 并集
    print("并集：", a | b)
    print("并集：", a.union(b))
    # 4.2 交集
    print("交集：", a & b)
    print("交集：", a.intersection(b))
    # 4.3 差集
    print("差集：", a - b)
    print("差集：", a.difference(b))
