# -*- coding: utf-8 -*-
# Python 3 算法实现；中文题意、算法说明与原课程顺序对应。
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 寻找最近和次近
# 给定一个长度为n的数组arr，下标1 ~ n范围，数组无重复值
# 关于近的定义，距离的定义如下:
# 对i位置的数字x来说，只关注右侧的数字，和x的差值绝对值越小就越近
# 距离为差值绝对值，如果距离一样，数值越小的越近
# 数值 : 3 5 7 1
# 下标 : 1 2 3 4
# 对1位置的数字3来说，第一近是4位置的1，距离为2；第二近是2位置的5，距离为2
# 每个位置的数字都求第一近的位置及其距离、第二近的位置及其距离
# 分别用to1、dist1、to2、dist2数组表示，0表示不存在
# 有序表的实现 + 数组手搓双向链表的实现
# 对数器验证
class Code04_FindNear:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'to1': 'to1', 'dist1': 'dist1', 'to2': 'to2', 'dist2': 'dist2', 'rank': 'rank', 'last': 'last', 'next': 'next', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'}
    MAXN = 0
    arr = None
    n = 0
    to1 = None
    dist1 = None
    to2 = None
    dist2 = None
    # 如下三个数组只有near2方法需要
    rank = None
    last = None
    next = None
    # 有序表的实现
    @staticmethod
    def near1():
        set = jnew('TreeSet', (lambda a, b: jcast('int', (a[1] - b[1]))))
        i = jcast('int', Code04_FindNear.n)
        while (i >= 1):
            Code04_FindNear.to1[i] = jcast('int', 0)
            Code04_FindNear.dist1[i] = jcast('int', 0)
            Code04_FindNear.to2[i] = jcast('int', 0)
            Code04_FindNear.dist2[i] = jcast('int', 0)
            cur = jarray('int', [None], [i, Code04_FindNear.arr[i]])
            p1 = jcall(set, 'floor', cur)
            p2 = (jcall(set, 'floor', jarray('int', [None], [p1[0], jcast('int', (p1[1] - 1))])) if (p1 != None) else None)
            p3 = jcall(set, 'ceiling', cur)
            p4 = (jcall(set, 'ceiling', jarray('int', [None], [p3[0], jcast('int', jadd(p3[1], 1))])) if (p3 != None) else None)
            Code04_FindNear.update(i, (p1[0] if (p1 != None) else 0))
            Code04_FindNear.update(i, (p2[0] if (p2 != None) else 0))
            Code04_FindNear.update(i, (p3[0] if (p3 != None) else 0))
            Code04_FindNear.update(i, (p4[0] if (p4 != None) else 0))
            jcall(set, 'add', cur)
            i = jcast('int', (i - 1))

    # 数组手搓双向链表的实现
    @staticmethod
    def near2():
        i = jcast('int', 1)
        while (i <= Code04_FindNear.n):
            jset(Code04_FindNear.rank[i], 0, i)
            jset(Code04_FindNear.rank[i], 1, Code04_FindNear.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_FindNear.rank, 1, jcast('int', jadd(Code04_FindNear.n, 1)), (lambda a, b: jcast('int', (a[1] - b[1]))))
        jset(Code04_FindNear.rank[0], 0, 0)
        jset(Code04_FindNear.rank[jcast('int', jadd(Code04_FindNear.n, 1))], 0, 0)
        i = jcast('int', 1)
        while (i <= Code04_FindNear.n):
            jset(Code04_FindNear.last, Code04_FindNear.rank[i][0], Code04_FindNear.rank[jcast('int', (i - 1))][0])
            jset(Code04_FindNear.next, Code04_FindNear.rank[i][0], Code04_FindNear.rank[jcast('int', jadd(i, 1))][0])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_FindNear.n):
            Code04_FindNear.to1[i] = jcast('int', 0)
            Code04_FindNear.dist1[i] = jcast('int', 0)
            Code04_FindNear.to2[i] = jcast('int', 0)
            Code04_FindNear.dist2[i] = jcast('int', 0)
            Code04_FindNear.update(i, Code04_FindNear.last[i])
            Code04_FindNear.update(i, Code04_FindNear.last[Code04_FindNear.last[i]])
            Code04_FindNear.update(i, Code04_FindNear.next[i])
            Code04_FindNear.update(i, Code04_FindNear.next[Code04_FindNear.next[i]])
            Code04_FindNear.delete(i)
            i = jcast('int', (i + 1))

    # i位置右侧的j位置
    # 看看能不能更新i右侧的最近或者次近
    # 如果j==0则不更新
    @staticmethod
    def update(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if (j == 0):
            return
        dist = jcast('int', jstatic('Math', 'abs', jcast('int', (Code04_FindNear.arr[i] - Code04_FindNear.arr[j]))))
        if (((Code04_FindNear.to1[i] == 0) or (dist < Code04_FindNear.dist1[i])) or ((dist == Code04_FindNear.dist1[i]) and (Code04_FindNear.arr[j] < Code04_FindNear.arr[Code04_FindNear.to1[i]]))):
            Code04_FindNear.to2[i] = jcast('int', Code04_FindNear.to1[i])
            Code04_FindNear.dist2[i] = jcast('int', Code04_FindNear.dist1[i])
            Code04_FindNear.to1[i] = jcast('int', j)
            Code04_FindNear.dist1[i] = jcast('int', dist)
        else:
            if (((Code04_FindNear.to2[i] == 0) or (dist < Code04_FindNear.dist2[i])) or ((dist == Code04_FindNear.dist2[i]) and (Code04_FindNear.arr[j] < Code04_FindNear.arr[Code04_FindNear.to2[i]]))):
                Code04_FindNear.to2[i] = jcast('int', j)
                Code04_FindNear.dist2[i] = jcast('int', dist)

    # 双向链表中删掉i位置
    @staticmethod
    def delete(i):
        i = jcast('int', i)
        l = jcast('int', Code04_FindNear.last[i])
        r = jcast('int', Code04_FindNear.next[i])
        if (l != 0):
            Code04_FindNear.next[l] = jcast('int', r)
        if (r != 0):
            Code04_FindNear.last[r] = jcast('int', l)

    # 随机生成arr[1...n]确保没有重复数值
    # 为了测试
    @staticmethod
    def random(v):
        v = jcast('int', v)
        set = jnew('HashSet')
        i = jcast('int', 1)
        cur = 0
        while (i <= Code04_FindNear.n):
            while True:
                cur = jcast('int', jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
                if not (jcall(set, 'contains', cur)):
                    break
            jcall(set, 'add', cur)
            Code04_FindNear.arr[i] = jcast('int', cur)
            i = jcast('int', (i + 1))

    # 如下四个数组用来做备份
    a = None
    b = None
    c = None
    d = None
    # 验证的过程
    # 为了测试
    @staticmethod
    def check():
        # near1方法会设置to1、dist1、to2、dist2
        Code04_FindNear.near1()
        # 把near1方法的结果备份
        i = jcast('int', 1)
        while (i <= Code04_FindNear.n):
            Code04_FindNear.a[i] = jcast('int', Code04_FindNear.to1[i])
            Code04_FindNear.b[i] = jcast('int', Code04_FindNear.dist1[i])
            Code04_FindNear.c[i] = jcast('int', Code04_FindNear.to2[i])
            Code04_FindNear.d[i] = jcast('int', Code04_FindNear.dist2[i])
            i = jcast('int', (i + 1))
        # near2方法会再次设置to1、dist1、to2、dist2
        Code04_FindNear.near2()
        # a、b、c、d，是near1生成的结果
        # to1、dist1、to2、dist2，是near2生成的结果
        i = jcast('int', 1)
        while (i <= Code04_FindNear.n):
            if ((Code04_FindNear.a[i] != Code04_FindNear.to1[i]) or (Code04_FindNear.b[i] != Code04_FindNear.dist1[i])):
                return jcast('boolean', False)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_FindNear.n):
            if ((Code04_FindNear.c[i] != Code04_FindNear.to2[i]) or (Code04_FindNear.d[i] != Code04_FindNear.dist2[i])):
                return jcast('boolean', False)
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    # 对数器
    # 为了测试
    @staticmethod
    def main(args):
        # 一定要确保arr中的数字无重复，所以让v大于n
        Code04_FindNear.n = jcast('int', 100)
        v = jcast('int', 500)
        testTime = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTime):
            Code04_FindNear.random(v)
            if (not Code04_FindNear.check()):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_FindNear.MAXN = jcast('int', 10001)
Code04_FindNear.arr = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.n = jcast('int', 0)
Code04_FindNear.to1 = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.dist1 = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.to2 = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.dist2 = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.rank = jarray('int', [Code04_FindNear.MAXN, 2])
Code04_FindNear.last = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.next = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.a = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.b = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.c = jarray('int', [Code04_FindNear.MAXN])
Code04_FindNear.d = jarray('int', [Code04_FindNear.MAXN])

if __name__ == '__main__':
    Code04_FindNear.main([])
