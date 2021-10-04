# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# author  Zhang Zhibang


if __name__ == '__main__':
    print("开始学习dict")

    # 1字典的创建
    # 1.1通过{}来创建字典
    a = {
        'name': 'zzb',
        'age': 18,
        'job': 'programmer'
    }  # 最直接的dict创建方法，key要加''
    b = dict(name='gaoqiao', age=99, job='programmer')  # 用dict() key不虚要''
    c = dict([("name", "name"), ("age", "11"), ("job", "program")])  # 这个是将列表强转成字典
    d = {}  # 空的dict对象
    e = dict()  # 空的dict对象
    print('dict a is', a)
    print('dict b is', b)
    print('dict c is', c)
    print('dict d is', d)
    print('dict e is', e)

    # 1.2通过zip创建dict
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    d = dict(zip(a, b))  # 字典是无序的 所以不会按照a b c的顺序去输出
    print(d)

    # 1.3通过fromkeys创建值为空的dict
    a = dict.fromkeys(['name', 'age', 'job'])
    print(a)

    # 2字典的访问
    # 2.1通过[key]获得值
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    d = dict(zip(a, b))
    print(d['a'])
    # 一个小例子
    a = ['你', '我', '他', '爱', '天安门']
    b = [1, 2, 3, 4, 5]
    d = dict(zip(a, b))
    sentence = '我 爱 天安门'
    words = sentence.split(' ')
    result = [d[word] for word in words]
    print(result)
    # 2.2通过get获取访问字典值
    a = ['你', '我', '他', '爱', '天安门']
    b = [1, 2, 3, 4, 5]
    d = dict(zip(a, b))
    print(d.get('你'))

    # 3字典的常见操作
    # 3.1通过[key]添加元素
    print(d)
    d['哈哈哈'] = 100
    print(d)
    # 3.2update--用一个字典的内容更新另一个元素
    z = {}
    print(z)
    z.update(d)
    print(z)
    # 3.3删除的两种方法
    # del
    print(z)
    del z['哈哈哈']
    print(z)
    # pop
    z.update(d)
    print(z)
    print(z.pop('我'))
    print(z)
    print(z.popitem())
    print(z.popitem())
    print(z.popitem())
    print(z)

    # 4字典几个常用方法
    # items keys values
    a = ['你', '我', '他', '爱', '天安门']
    b = [1, 2, 3, 4, 5]
    d = dict(zip(a, b))
    for i in d.items():
        print(i)
    for key in d.keys():
        print(key)
    for value in d.values():
        print(value)

    # 5序列的解包
    x, y, z = [1, 2, 3]
    print(x, y, z)
    x, y, z = (1, 2, 3)
    print(x, y, z)
    x, y = {"name": "zzb", "age": 18}
    print(x, y)

    # 6enumerate()--对一个可遍历序列进行遍历 提供索引
    dd = {"name": "zzb", "age": 18}
    for i, key in enumerate(dd):
        print(i, key, dd[key])
    ll = [1, 2, 3, 4, 5]
    for i, value in enumerate(ll):
        print(i, value)
