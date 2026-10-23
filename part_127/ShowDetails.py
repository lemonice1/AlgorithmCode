# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 课上讲述高斯消元解决异或方程组的例子
class ShowDetails:
    __java_fields__ = {'MAXN': 'MAXN', 'mat': 'mat'}
    MAXN = 0
    mat = None
    # 高斯消元解决异或方程组模版
    # 需要保证变量有n个，表达式也有n个
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        if ((j < i) and (ShowDetails.mat[j][j] == 1)):
                            raise JContinue(None)
                        if (ShowDetails.mat[j][i] == 1):
                            ShowDetails.swap(i, j)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (ShowDetails.mat[i][i] == 1):
                    j = jcast('int', 1)
                    while (j <= n):
                        if ((i != j) and (ShowDetails.mat[j][i] == 1)):
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                ((_java_obj_3 := ShowDetails.mat[j]), (_java_key_4 := k), jset(_java_obj_3, _java_key_4, jcast('int', (jget(_java_obj_3, _java_key_4) ^ ShowDetails.mat[i][k]))))[2]
                                k = jcast('int', (k + 1))
                        j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = ShowDetails.mat[a]
        ShowDetails.mat[a] = ShowDetails.mat[b]
        ShowDetails.mat[b] = tmp

    @staticmethod
    def print(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(n, 1))):
                jprint(jadd(ShowDetails.mat[i][j], ' '), newline=False)
                j = jcast('int', (j + 1))
            jprint(newline=True)
            i = jcast('int', (i + 1))
        jprint('========================', newline=True)

    @staticmethod
    def main(args):
        jprint('课上图解的例子，有唯一解', newline=True)
        # x1 ^ x2 ^ x3 = 0
        # x1 ^ x3 ^ x4 = 1
        # x2 ^ x3 ^ x4 = 1
        # x3 ^ x4 = 0
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 1)
        jset(ShowDetails.mat[1], 3, 1)
        jset(ShowDetails.mat[1], 4, 0)
        jset(ShowDetails.mat[1], 5, 0)
        jset(ShowDetails.mat[2], 1, 1)
        jset(ShowDetails.mat[2], 2, 0)
        jset(ShowDetails.mat[2], 3, 1)
        jset(ShowDetails.mat[2], 4, 1)
        jset(ShowDetails.mat[2], 5, 1)
        jset(ShowDetails.mat[3], 1, 0)
        jset(ShowDetails.mat[3], 2, 1)
        jset(ShowDetails.mat[3], 3, 1)
        jset(ShowDetails.mat[3], 4, 1)
        jset(ShowDetails.mat[3], 5, 1)
        jset(ShowDetails.mat[4], 1, 0)
        jset(ShowDetails.mat[4], 2, 0)
        jset(ShowDetails.mat[4], 3, 1)
        jset(ShowDetails.mat[4], 4, 1)
        jset(ShowDetails.mat[4], 5, 0)
        ShowDetails.gauss(4)
        ShowDetails.print(4)
        jprint('表达式存在矛盾的例子', newline=True)
        # x1 ^ x2 = 1
        # x1 ^ x3 = 1
        # x2 ^ x3 = 1
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 1)
        jset(ShowDetails.mat[1], 3, 0)
        jset(ShowDetails.mat[1], 4, 1)
        jset(ShowDetails.mat[2], 1, 1)
        jset(ShowDetails.mat[2], 2, 0)
        jset(ShowDetails.mat[2], 3, 1)
        jset(ShowDetails.mat[2], 4, 1)
        jset(ShowDetails.mat[3], 1, 0)
        jset(ShowDetails.mat[3], 2, 1)
        jset(ShowDetails.mat[3], 3, 1)
        jset(ShowDetails.mat[3], 4, 1)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        jprint('表达式存在多解的例子', newline=True)
        # x1 ^ x3 = 1
        # x2 ^ x3 = 1
        # x1 ^ x2 = 0
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 0)
        jset(ShowDetails.mat[1], 3, 1)
        jset(ShowDetails.mat[1], 4, 1)
        jset(ShowDetails.mat[2], 1, 0)
        jset(ShowDetails.mat[2], 2, 1)
        jset(ShowDetails.mat[2], 3, 1)
        jset(ShowDetails.mat[2], 4, 1)
        jset(ShowDetails.mat[3], 1, 1)
        jset(ShowDetails.mat[3], 2, 1)
        jset(ShowDetails.mat[3], 3, 0)
        jset(ShowDetails.mat[3], 4, 0)
        jset(ShowDetails.mat[4], 1, 1)
        jset(ShowDetails.mat[4], 2, 1)
        jset(ShowDetails.mat[4], 3, 0)
        jset(ShowDetails.mat[4], 4, 0)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        jprint('注意下面这个多解的例子', newline=True)
        # x1 ^ x3 ^ x4 = 0
        # x2 ^ x3 ^ x4 = 0
        # x1 ^ x2 = 0
        # x3 ^ x4 = 1
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 0)
        jset(ShowDetails.mat[1], 3, 1)
        jset(ShowDetails.mat[1], 4, 1)
        jset(ShowDetails.mat[1], 5, 0)
        jset(ShowDetails.mat[2], 1, 0)
        jset(ShowDetails.mat[2], 2, 1)
        jset(ShowDetails.mat[2], 3, 1)
        jset(ShowDetails.mat[2], 4, 1)
        jset(ShowDetails.mat[2], 5, 0)
        jset(ShowDetails.mat[3], 1, 1)
        jset(ShowDetails.mat[3], 2, 1)
        jset(ShowDetails.mat[3], 3, 0)
        jset(ShowDetails.mat[3], 4, 0)
        jset(ShowDetails.mat[3], 5, 0)
        jset(ShowDetails.mat[4], 1, 0)
        jset(ShowDetails.mat[4], 2, 0)
        jset(ShowDetails.mat[4], 3, 1)
        jset(ShowDetails.mat[4], 4, 1)
        jset(ShowDetails.mat[4], 5, 1)
        ShowDetails.gauss(4)
        ShowDetails.print(4)
        jprint('最后一个例子里', newline=True)
        jprint('主元x1和x2，不受其他自由元影响，值可以直接确定', newline=True)
        jprint('但是主元x3，受到自由元x4的影响，x3 ^ x4 = 1', newline=True)
        jprint('只有自由元x4确定了值，主元x3的值才能确定', newline=True)
        jprint('这里是想说，消元完成后，如果结论是多解，那么', newline=True)
        jprint('有些主元的值可以直接确定', newline=True)
        jprint('有些主元的值需要若干自由元确定之后才能确定', newline=True)
        jprint('这就是上节课，也就是讲解133讲的：', newline=True)
        jprint('主元和自由元之间的依赖关系', newline=True)
        jprint('请确保已经掌握', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


ShowDetails.MAXN = jcast('int', 101)
ShowDetails.mat = jarray('int', [ShowDetails.MAXN, ShowDetails.MAXN])

if __name__ == '__main__':
    ShowDetails.main([])
