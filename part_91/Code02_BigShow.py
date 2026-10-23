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

# 矩阵乘法
# 矩阵快速幂
# 矩阵快速幂解决斐波那契第n项的问题
class Code02_BigShow:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        jprint('f1() : ', newline=True)
        jprint('矩阵乘法展示开始', newline=True)
        Code02_BigShow.f1()
        jprint('矩阵乘法展示结束', newline=True)
        jprint(newline=True)
        jprint('f2() : ', newline=True)
        jprint('矩阵快速幂展示开始', newline=True)
        Code02_BigShow.f2()
        jprint('矩阵快速幂展示结束', newline=True)
        jprint(newline=True)
        jprint('f3() : ', newline=True)
        jprint('求斐波那契数列第n项', newline=True)
        jprint('用矩阵乘法解决', newline=True)
        jprint('展示开始', newline=True)
        Code02_BigShow.f3()
        jprint('展示结束', newline=True)
        jprint(newline=True)
        jprint('f4() : ', newline=True)
        jprint('求斐波那契数列第n项', newline=True)
        jprint('用矩阵快速幂解决', newline=True)
        jprint('展示开始', newline=True)
        Code02_BigShow.f4()
        jprint('展示结束', newline=True)
        jprint(newline=True)

    # 矩阵相乘
    # a的列数一定要等于b的行数
    @staticmethod
    def multiply(a, b):
        n = jcast('int', jget(a, 'length'))
        m = jcast('int', jget(b[0], 'length'))
        k = jcast('int', jget(a[0], 'length'))
        ans = jarray('int', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                c = jcast('int', 0)
                while (c < k):
                    ((_java_obj_1 := ans[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), jcast('int', (a[i][c] * b[c][j]))))))[2]
                    c = jcast('int', (c + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return ans

    # 矩阵快速幂
    # 要求矩阵m是正方形矩阵
    @staticmethod
    def power(m, p):
        p = jcast('int', p)
        n = jcast('int', jget(m, 'length'))
        # 对角线全是1、剩下数字都是0的正方形矩阵，称为单位矩阵
        # 相当于正方形矩阵中的1，矩阵a * 单位矩阵 = 矩阵a
        ans = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans[i], i, 1)
            i = jcast('int', (i + 1))
        while (p != 0):
            if (jcast('int', (p & 1)) != 0):
                ans = Code02_BigShow.multiply(ans, m)
            m = Code02_BigShow.multiply(m, m)
            p = jcast('int', jcast('int', (p >> (1 & 31))))
        return ans

    # 打印二维矩阵
    @staticmethod
    def print(m):
        i = jcast('int', 0)
        while (i < jget(m, 'length')):
            j = jcast('int', 0)
            while (j < jget(m[0], 'length')):
                if (m[i][j] < 10):
                    jprint(jadd(m[i][j], '   '), newline=False)
                else:
                    if (m[i][j] < 100):
                        jprint(jadd(m[i][j], '  '), newline=False)
                    else:
                        jprint(jadd(m[i][j], ' '), newline=False)
                j = jcast('int', (j + 1))
            jprint(newline=True)
            i = jcast('int', (i + 1))

    # 矩阵乘法的展示
    @staticmethod
    def f1():
        a = jarray('int', [None, None], [[1, 3], [4, 2]])
        b = jarray('int', [None, None], [[2, 3], [3, 2]])
        # 2  3
        # 3  2
        #
        # 1  3  11  9
        # 4  2  14 16
        ans1 = Code02_BigShow.multiply(a, b)
        Code02_BigShow.print(ans1)
        jprint('======', newline=True)
        c = jarray('int', [None, None], [[2, 4], [3, 2]])
        d = jarray('int', [None, None], [[2, 3, 2], [3, 2, 3]])
        # 2  3  2
        # 3  2  3
        #
        # 2  4   16 14 16
        # 3  2   12 13 12
        ans2 = Code02_BigShow.multiply(c, d)
        Code02_BigShow.print(ans2)
        jprint('======', newline=True)
        e = jarray('int', [None, None], [[2, 4], [1, 2], [3, 1]])
        f = jarray('int', [None, None], [[2, 3], [4, 1]])
        # 2  3
        # 4  1
        #
        # 2  4    20 10
        # 1  2    10  5
        # 3  1    10 10
        ans3 = Code02_BigShow.multiply(e, f)
        Code02_BigShow.print(ans3)
        jprint('======', newline=True)
        g = jarray('int', [None, None], [[3, 1, 2]])
        h = jarray('int', [None, None], [[1, 2, 1], [3, 2, 1], [4, 2, jcast('int', (-2))]])
        # 1  2  1
        # 3  2  1
        # 4  2 -2
        #
        # 3  1  2  14 12  0
        ans4 = Code02_BigShow.multiply(g, h)
        Code02_BigShow.print(ans4)

    # 矩阵快速幂用法的展示
    @staticmethod
    def f2():
        # 只有正方形矩阵可以求幂
        a = jarray('int', [None, None], [[1, 2], [3, 4]])
        # 连乘得到矩阵a的5次方
        b = Code02_BigShow.multiply(a, Code02_BigShow.multiply(a, Code02_BigShow.multiply(a, Code02_BigShow.multiply(a, a))))
        Code02_BigShow.print(b)
        jprint('======', newline=True)
        # 矩阵快速幂得到矩阵a的5次方
        Code02_BigShow.print(Code02_BigShow.power(a, 5))

    # 用矩阵乘法解决斐波那契第n项的问题
    @staticmethod
    def f3():
        # 0  1  1  2  3  5  8 13 21 34...
        # 0  1  2  3  4  5  6  7  8  9
        start = jarray('int', [None, None], [[1, 0]])
        m = jarray('int', [None, None], [[1, 1], [1, 0]])
        a = Code02_BigShow.multiply(start, m)
        # 1  1
        # 1  0
        #
        # 1  0  1  1
        Code02_BigShow.print(a)
        jprint('======', newline=True)
        b = Code02_BigShow.multiply(a, m)
        # 1  1
        # 1  0
        #
        # 1  1  2  1
        Code02_BigShow.print(b)
        jprint('======', newline=True)
        c = Code02_BigShow.multiply(b, m)
        # 1  1
        # 1  0
        #
        # 2  1  3  2
        Code02_BigShow.print(c)
        jprint('======', newline=True)
        d = Code02_BigShow.multiply(c, m)
        # 1  1
        # 1  0
        #
        # 3  2  5  3
        Code02_BigShow.print(d)

    # 用矩阵快速幂解决斐波那契第n项的问题
    @staticmethod
    def f4():
        # 0  1  1  2  3  5  8 13 21 34...
        # 0  1  2  3  4  5  6  7  8  9
        start = jarray('int', [None, None], [[1, 0]])
        m = jarray('int', [None, None], [[1, 1], [1, 0]])
        a = Code02_BigShow.multiply(start, Code02_BigShow.power(m, 1))
        Code02_BigShow.print(a)
        jprint('======', newline=True)
        b = Code02_BigShow.multiply(start, Code02_BigShow.power(m, 2))
        Code02_BigShow.print(b)
        jprint('======', newline=True)
        c = Code02_BigShow.multiply(start, Code02_BigShow.power(m, 3))
        Code02_BigShow.print(c)
        jprint('======', newline=True)
        d = Code02_BigShow.multiply(start, Code02_BigShow.power(m, 4))
        Code02_BigShow.print(d)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_BigShow.main([])
