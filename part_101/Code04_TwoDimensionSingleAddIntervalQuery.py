# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二维数组上单点增加、范围查询，使用树状数组的模版
# 测试链接 : https://leetcode.cn/problems/range-sum-query-2d-mutable/
class Code04_TwoDimensionSingleAddIntervalQuery:
    __java_fields__ = {}
    class NumMatrix:
        __java_fields__ = {'tree': 'tree', 'nums': 'nums', 'n': 'n', 'm': 'm'}
        # tree：实例字段，在构造函数中初始化。
        # nums：实例字段，在构造函数中初始化。
        # n：实例字段，在构造函数中初始化。
        # m：实例字段，在构造函数中初始化。
        # 入参二维数组下标从0开始
        # 树状数组一定下标从1开始
        def _java_init_0(self, matrix):
            self.n = jcast('int', jget(matrix, 'length'))
            self.m = jcast('int', jget(matrix[0], 'length'))
            self.tree = jarray('int', [jcast('int', jadd(self.n, 1)), jcast('int', jadd(self.m, 1))])
            self.nums = jarray('int', [jcast('int', jadd(self.n, 1)), jcast('int', jadd(self.m, 1))])
            i = jcast('int', 0)
            while (i < self.n):
                j = jcast('int', 0)
                while (j < self.m):
                    self.update(i, j, matrix[i][j])
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))

        def lowbit(self, i):
            i = jcast('int', i)
            return jcast('int', jcast('int', (i & jcast('int', (-i)))))

        def add(self, x, y, v):
            x = jcast('int', x)
            y = jcast('int', y)
            v = jcast('int', v)
            i = jcast('int', x)
            while (i <= self.n):
                j = jcast('int', y)
                while (j <= self.m):
                    ((_java_obj_1 := self.tree[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), v))))[2]
                    j = jcast('int', jcast('int', jadd(j, self.lowbit(j))))
                i = jcast('int', jcast('int', jadd(i, self.lowbit(i))))

        # 从(1,1)到(x,y)这个部分的累加和
        def sum(self, x, y):
            x = jcast('int', x)
            y = jcast('int', y)
            ans = jcast('int', 0)
            i = jcast('int', x)
            while (i > 0):
                j = jcast('int', y)
                while (j > 0):
                    ans = jcast('int', jcast('int', jadd(ans, self.tree[i][j])))
                    j = jcast('int', jcast('int', (j - self.lowbit(j))))
                i = jcast('int', jcast('int', (i - self.lowbit(i))))
            return jcast('int', ans)

        # 实际二维数组的位置是(x,y)
        # 树状数组上的位置是(x+1, y+1)
        # 题目说的是单点更新，转化成单点增加(老值-新值)即可
        # 不要忘了在nums中把老值改成新值
        def update(self, x, y, v):
            x = jcast('int', x)
            y = jcast('int', y)
            v = jcast('int', v)
            self.add(jcast('int', jadd(x, 1)), jcast('int', jadd(y, 1)), jcast('int', (v - self.nums[jcast('int', jadd(x, 1))][jcast('int', jadd(y, 1))])))
            jset(self.nums[jcast('int', jadd(x, 1))], jcast('int', jadd(y, 1)), v)

        # 实际二维数组的位置是(x,y)
        # 树状数组上的位置是(x+1, y+1)
        def sumRegion(self, a, b, c, d):
            a = jcast('int', a)
            b = jcast('int', b)
            c = jcast('int', c)
            d = jcast('int', d)
            return jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (self.sum(jcast('int', jadd(c, 1)), jcast('int', jadd(d, 1))) - self.sum(a, jcast('int', jadd(d, 1))))) - self.sum(jcast('int', jadd(c, 1)), b))), self.sum(a, b))))

        def __init__(self, *args, _java_ctor=None):
            self.tree = None
            self.nums = None
            self.n = jcast('int', 0)
            self.m = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int[][]']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_TwoDimensionSingleAddIntervalQuery.NumMatrix.NumMatrix")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


