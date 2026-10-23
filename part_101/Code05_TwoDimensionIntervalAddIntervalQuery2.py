# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二维数组上范围增加、范围查询，使用树状数组的模版(Python)
# 测试链接 : https://www.luogu.com.cn/problem/P4514
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_TwoDimensionIntervalAddIntervalQuery2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'info1': 'info1', 'info2': 'info2', 'info3': 'info3', 'info4': 'info4', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    # 维护信息 : d[i][j]
    info1 = None
    # 维护信息 : d[i][j] * i
    info2 = None
    # 维护信息 : d[i][j] * j
    info3 = None
    # 维护信息 : d[i][j] * i * j
    info4 = None
    n = 0
    m = 0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def _java_add_0(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        v1 = jcast('int', v)
        v2 = jcast('int', jcast('int', (x * v)))
        v3 = jcast('int', jcast('int', (y * v)))
        v4 = jcast('int', jcast('int', (jcast('int', (x * y)) * v)))
        i = jcast('int', x)
        while (i <= Code05_TwoDimensionIntervalAddIntervalQuery2.n):
            j = jcast('int', y)
            while (j <= Code05_TwoDimensionIntervalAddIntervalQuery2.m):
                ((_java_obj_1 := Code05_TwoDimensionIntervalAddIntervalQuery2.info1[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), v1))))[2]
                ((_java_obj_3 := Code05_TwoDimensionIntervalAddIntervalQuery2.info2[i]), (_java_key_4 := j), jset(_java_obj_3, _java_key_4, jcast('int', jadd(jget(_java_obj_3, _java_key_4), v2))))[2]
                ((_java_obj_5 := Code05_TwoDimensionIntervalAddIntervalQuery2.info3[i]), (_java_key_6 := j), jset(_java_obj_5, _java_key_6, jcast('int', jadd(jget(_java_obj_5, _java_key_6), v3))))[2]
                ((_java_obj_7 := Code05_TwoDimensionIntervalAddIntervalQuery2.info4[i]), (_java_key_8 := j), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), v4))))[2]
                j = jcast('int', jcast('int', jadd(j, Code05_TwoDimensionIntervalAddIntervalQuery2.lowbit(j))))
            i = jcast('int', jcast('int', jadd(i, Code05_TwoDimensionIntervalAddIntervalQuery2.lowbit(i))))

    # 以(1,1)左上角，以(x,y)右下角
    @staticmethod
    def sum(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', 0)
        i = jcast('int', x)
        while (i > 0):
            j = jcast('int', y)
            while (j > 0):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(jcast('int', (jcast('int', (jcast('int', (jcast('int', (jcast('int', jadd(x, 1)) * jcast('int', jadd(y, 1)))) * Code05_TwoDimensionIntervalAddIntervalQuery2.info1[i][j])) - jcast('int', (jcast('int', jadd(y, 1)) * Code05_TwoDimensionIntervalAddIntervalQuery2.info2[i][j])))) - jcast('int', (jcast('int', jadd(x, 1)) * Code05_TwoDimensionIntervalAddIntervalQuery2.info3[i][j])))), Code05_TwoDimensionIntervalAddIntervalQuery2.info4[i][j])))))
                j = jcast('int', jcast('int', (j - Code05_TwoDimensionIntervalAddIntervalQuery2.lowbit(j))))
            i = jcast('int', jcast('int', (i - Code05_TwoDimensionIntervalAddIntervalQuery2.lowbit(i))))
        return jcast('int', ans)

    @staticmethod
    def _java_add_1(a, b, c, d, v):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        v = jcast('int', v)
        Code05_TwoDimensionIntervalAddIntervalQuery2._java_add_0(a, b, v)
        Code05_TwoDimensionIntervalAddIntervalQuery2._java_add_0(a, jcast('int', jadd(d, 1)), jcast('int', (-v)))
        Code05_TwoDimensionIntervalAddIntervalQuery2._java_add_0(jcast('int', jadd(c, 1)), b, jcast('int', (-v)))
        Code05_TwoDimensionIntervalAddIntervalQuery2._java_add_0(jcast('int', jadd(c, 1)), jcast('int', jadd(d, 1)), v)

    @staticmethod
    def range(a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        return jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (Code05_TwoDimensionIntervalAddIntervalQuery2.sum(c, d) - Code05_TwoDimensionIntervalAddIntervalQuery2.sum(jcast('int', (a - 1)), d))) - Code05_TwoDimensionIntervalAddIntervalQuery2.sum(c, jcast('int', (b - 1))))), Code05_TwoDimensionIntervalAddIntervalQuery2.sum(jcast('int', (a - 1)), jcast('int', (b - 1))))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        op = None
        a = 0
        b = 0
        c = 0
        d = 0
        v = 0
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            op = jget(in_, 'sval')
            if jcall(op, 'equals', 'X'):
                jcall(in_, 'nextToken')
                Code05_TwoDimensionIntervalAddIntervalQuery2.n = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code05_TwoDimensionIntervalAddIntervalQuery2.m = jcast('int', jcast('int', jget(in_, 'nval')))
            else:
                if jcall(op, 'equals', 'L'):
                    jcall(in_, 'nextToken')
                    a = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    b = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    c = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    d = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    v = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code05_TwoDimensionIntervalAddIntervalQuery2._java_add_1(a, b, c, d, v)
                else:
                    jcall(in_, 'nextToken')
                    a = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    b = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    c = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    d = jcast('int', jcast('int', jget(in_, 'nval')))
                    # 这里使用标准输出接口 print
                    jprint(Code05_TwoDimensionIntervalAddIntervalQuery2.range(a, b, c, d), newline=True)
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int'], ['int', 'int', 'int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code05_TwoDimensionIntervalAddIntervalQuery2._java_add_0(*args)
        if _java_choice == 1:
            return Code05_TwoDimensionIntervalAddIntervalQuery2._java_add_1(*args)
        raise TypeError("No matching overload for Code05_TwoDimensionIntervalAddIntervalQuery2.add")


Code05_TwoDimensionIntervalAddIntervalQuery2.MAXN = jcast('int', 2050)
Code05_TwoDimensionIntervalAddIntervalQuery2.MAXM = jcast('int', 2050)
Code05_TwoDimensionIntervalAddIntervalQuery2.info1 = jarray('int', [Code05_TwoDimensionIntervalAddIntervalQuery2.MAXN, Code05_TwoDimensionIntervalAddIntervalQuery2.MAXM])
Code05_TwoDimensionIntervalAddIntervalQuery2.info2 = jarray('int', [Code05_TwoDimensionIntervalAddIntervalQuery2.MAXN, Code05_TwoDimensionIntervalAddIntervalQuery2.MAXM])
Code05_TwoDimensionIntervalAddIntervalQuery2.info3 = jarray('int', [Code05_TwoDimensionIntervalAddIntervalQuery2.MAXN, Code05_TwoDimensionIntervalAddIntervalQuery2.MAXM])
Code05_TwoDimensionIntervalAddIntervalQuery2.info4 = jarray('int', [Code05_TwoDimensionIntervalAddIntervalQuery2.MAXN, Code05_TwoDimensionIntervalAddIntervalQuery2.MAXM])
Code05_TwoDimensionIntervalAddIntervalQuery2.n = jcast('int', 0)
Code05_TwoDimensionIntervalAddIntervalQuery2.m = jcast('int', 0)

if __name__ == '__main__':
    Code05_TwoDimensionIntervalAddIntervalQuery2.main([])
