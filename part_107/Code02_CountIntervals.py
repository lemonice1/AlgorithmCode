# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 统计区间中的整数数目
# 实现CountIntervals类的如下三个方法
# 1) CountIntervals() : 初始化
# 2) void add(int l, int r) : 把[l, r]范围上的数字都设置成1
# 3) int count() : 返回整个区间有多少个1
# CountIntervals类需要支持1 ~ 10^9范围
# 调用add和count方法总共10^5次
# 测试链接 : https://leetcode.cn/problems/count-integers-in-intervals/
class Code02_CountIntervals:
    __java_fields__ = {}
    # 开点线段树的实现
    # 为了所有语言的同学都容易改出来
    # 选择用静态空间的方式实现
    # 该方法的打败比例不高但是非常好想
    # 有兴趣的同学可以研究其他做法
    class CountIntervals:
        __java_fields__ = {'n': 'n', 'LIMIT': 'LIMIT', 'left': 'left', 'right': 'right', 'sum': 'sum', 'cnt': 'cnt'}
        # 支持的最大范围
        n = 0
        # 空间大小定成这个值是实验的结果
        LIMIT = 0
        left = None
        right = None
        sum = None
        cnt = 0
        def _java_init_0(self):
            jstatic('Arrays', 'fill', Code02_CountIntervals.CountIntervals.left, 1, jcast('int', jadd(Code02_CountIntervals.CountIntervals.cnt, 1)), 0)
            jstatic('Arrays', 'fill', Code02_CountIntervals.CountIntervals.right, 1, jcast('int', jadd(Code02_CountIntervals.CountIntervals.cnt, 1)), 0)
            jstatic('Arrays', 'fill', Code02_CountIntervals.CountIntervals.sum, 1, jcast('int', jadd(Code02_CountIntervals.CountIntervals.cnt, 1)), 0)
            jset(Code02_CountIntervals.CountIntervals, 'cnt', 1)

        @staticmethod
        def up(h, l, r):
            h = jcast('int', h)
            l = jcast('int', l)
            r = jcast('int', r)
            jset(Code02_CountIntervals.CountIntervals.sum, h, jcast('int', jadd(Code02_CountIntervals.CountIntervals.sum[l], Code02_CountIntervals.CountIntervals.sum[r])))

        # 这个题的特殊性在于，只有改1的操作，没有改0的操作
        # 理解这个就可以分析出不需要懒更新机制，原因有两个
        # 1) 查询操作永远查的是整个范围1的数量，不会有小范围的查询，每次都返回sum[1]
        # 这意味着只要能把sum[1]更新正确即可，up函数可以保证这一点
        # 2) 一个范围已经全是1，那以后都会是1，没有必要把全是1的懒更新信息向下传递
        # 这个函数的功能比线段树能做到的范围修改功能简单很多
        # 功能有阉割就意味着存在优化的点
        @staticmethod
        def setOne(jobl, jobr, l, r, i):
            jobl = jcast('int', jobl)
            jobr = jcast('int', jobr)
            l = jcast('int', l)
            r = jcast('int', r)
            i = jcast('int', i)
            if (Code02_CountIntervals.CountIntervals.sum[i] == jcast('int', jadd(jcast('int', (r - l)), 1))):
                return
            if ((jobl <= l) and (r <= jobr)):
                jset(Code02_CountIntervals.CountIntervals.sum, i, jcast('int', jadd(jcast('int', (r - l)), 1)))
            else:
                mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
                if (jobl <= mid):
                    if (Code02_CountIntervals.CountIntervals.left[i] == 0):
                        jset(Code02_CountIntervals.CountIntervals.left, i, ((_java_obj_1 := Code02_CountIntervals.CountIntervals), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
                    Code02_CountIntervals.CountIntervals.setOne(jobl, jobr, l, mid, Code02_CountIntervals.CountIntervals.left[i])
                if (jobr > mid):
                    if (Code02_CountIntervals.CountIntervals.right[i] == 0):
                        jset(Code02_CountIntervals.CountIntervals.right, i, ((_java_obj_4 := Code02_CountIntervals.CountIntervals), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
                    Code02_CountIntervals.CountIntervals.setOne(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code02_CountIntervals.CountIntervals.right[i])
                Code02_CountIntervals.CountIntervals.up(i, Code02_CountIntervals.CountIntervals.left[i], Code02_CountIntervals.CountIntervals.right[i])

        def add(self, left, right):
            left = jcast('int', left)
            right = jcast('int', right)
            Code02_CountIntervals.CountIntervals.setOne(left, right, 1, Code02_CountIntervals.CountIntervals.n, 1)

        def count(self):
            return jcast('int', Code02_CountIntervals.CountIntervals.sum[1])

        def __init__(self, *args, _java_ctor=None):
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_CountIntervals.CountIntervals.CountIntervals")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CountIntervals.CountIntervals.n = jcast('int', 1000000000)
Code02_CountIntervals.CountIntervals.LIMIT = jcast('int', 700001)
Code02_CountIntervals.CountIntervals.left = jarray('int', [Code02_CountIntervals.CountIntervals.LIMIT])
Code02_CountIntervals.CountIntervals.right = jarray('int', [Code02_CountIntervals.CountIntervals.LIMIT])
Code02_CountIntervals.CountIntervals.sum = jarray('int', [Code02_CountIntervals.CountIntervals.LIMIT])
Code02_CountIntervals.CountIntervals.cnt = jcast('int', 1)
