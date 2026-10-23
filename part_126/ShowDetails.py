# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 课上讲述高斯消元解决加法方程组的例子
class ShowDetails:
    __java_fields__ = {'MAXN': 'MAXN', 'mat': 'mat', 'sml': 'sml'}
    MAXN = 0
    mat = None
    # 0.0000001 == 1e-7
    # 因为double类型有精度问题，所以认为
    # 如果一个数字绝对值  <  sml，则认为该数字是0
    # 如果一个数字绝对值  >= sml，则认为该数字不是0
    sml = 0.0
    # 高斯消元解决加法方程组模版
    # 需要保证变量有n个，表达式也有n个
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                # 如果想严格区分矛盾、多解、唯一解，一定要这么写
                max = jcast('int', i)
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        if ((j < i) and (jstatic('Math', 'abs', ShowDetails.mat[j][j]) >= ShowDetails.sml)):
                            raise JContinue(None)
                        if (jstatic('Math', 'abs', ShowDetails.mat[j][i]) > jstatic('Math', 'abs', ShowDetails.mat[max][i])):
                            max = jcast('int', j)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                ShowDetails.swap(i, max)
                if (jstatic('Math', 'abs', ShowDetails.mat[i][i]) >= ShowDetails.sml):
                    tmp = jcast('double', ShowDetails.mat[i][i])
                    j = jcast('int', i)
                    while (j <= jcast('int', jadd(n, 1))):
                        ((_java_obj_3 := ShowDetails.mat[i]), (_java_key_4 := j), jset(_java_obj_3, _java_key_4, jdiv(jget(_java_obj_3, _java_key_4), tmp)))[2]
                        j = jcast('int', (j + 1))
                    j = jcast('int', 1)
                    while (j <= n):
                        if (i != j):
                            rate = jcast('double', jdiv(ShowDetails.mat[j][i], ShowDetails.mat[i][i]))
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                ((_java_obj_5 := ShowDetails.mat[j]), (_java_key_6 := k), jset(_java_obj_5, _java_key_6, (jget(_java_obj_5, _java_key_6) - (ShowDetails.mat[i][k] * rate))))[2]
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
                jcall(jget(System, 'out'), 'printf', '%.2f  ', ShowDetails.mat[i][j])
                j = jcast('int', (j + 1))
            jprint(newline=True)
            i = jcast('int', (i + 1))
        jprint('========================', newline=True)

    @staticmethod
    def main(args):
        # 唯一解
        # 1*x1 + 2*x2 - 1*x3 = 9
        # 2*x1 - 1*x2 + 2*x3 = 7
        # 1*x1 - 2*x2 + 2*x3 = 0
        jprint('唯一解', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, jcast('int', (-1)))
        jset(ShowDetails.mat[1], 4, 9)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, jcast('int', (-1)))
        jset(ShowDetails.mat[2], 3, 2)
        jset(ShowDetails.mat[2], 4, 7)
        jset(ShowDetails.mat[3], 1, 1)
        jset(ShowDetails.mat[3], 2, jcast('int', (-2)))
        jset(ShowDetails.mat[3], 3, 2)
        jset(ShowDetails.mat[3], 4, 0)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        # 矛盾
        # 1*x1 + 1*x2 = 3
        # 2*x1 + 2*x2 = 7
        jprint('矛盾', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 1)
        jset(ShowDetails.mat[1], 3, 3)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 2)
        jset(ShowDetails.mat[2], 3, 7)
        ShowDetails.gauss(2)
        ShowDetails.print(2)
        # 多解
        # 1*x1 + 1*x2 = 3
        # 2*x1 + 2*x2 = 6
        jprint('多解', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 1)
        jset(ShowDetails.mat[1], 3, 3)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 2)
        jset(ShowDetails.mat[2], 3, 6)
        ShowDetails.gauss(2)
        ShowDetails.print(2)
        # 表达式冗余，唯一解
        # 1*x1 + 2*x2 - 1*x3 + 0*x4 = 9
        # 2*x1 + 4*x2 - 2*x3 + 0*x4 = 18
        # 2*x1 - 1*x2 + 2*x3 + 0*x4 = 7
        # 1*x1 - 2*x2 + 2*x3 + 0*x4 = 0
        jprint('表达式冗余，唯一解', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, jcast('int', (-1)))
        jset(ShowDetails.mat[1], 4, 0)
        jset(ShowDetails.mat[1], 5, 9)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 4)
        jset(ShowDetails.mat[2], 3, jcast('int', (-2)))
        jset(ShowDetails.mat[2], 4, 0)
        jset(ShowDetails.mat[2], 5, 18)
        jset(ShowDetails.mat[3], 1, 2)
        jset(ShowDetails.mat[3], 2, jcast('int', (-1)))
        jset(ShowDetails.mat[3], 3, 2)
        jset(ShowDetails.mat[3], 4, 0)
        jset(ShowDetails.mat[3], 5, 7)
        jset(ShowDetails.mat[4], 1, 1)
        jset(ShowDetails.mat[4], 2, jcast('int', (-2)))
        jset(ShowDetails.mat[4], 3, 2)
        jset(ShowDetails.mat[4], 4, 0)
        jset(ShowDetails.mat[4], 5, 0)
        ShowDetails.gauss(4)
        ShowDetails.print(4)
        # 表达式冗余，矛盾
        # 1*x1 + 2*x2 - 1*x3 = 9
        # 2*x1 + 4*x2 - 2*x3 = 18
        # 2*x1 - 1*x2 + 2*x3 = 7
        # 4*x1 - 2*x2 + 4*x3 = 10
        jprint('表达式冗余，矛盾', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, jcast('int', (-1)))
        jset(ShowDetails.mat[1], 4, 0)
        jset(ShowDetails.mat[1], 5, 9)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 4)
        jset(ShowDetails.mat[2], 3, jcast('int', (-2)))
        jset(ShowDetails.mat[2], 4, 0)
        jset(ShowDetails.mat[2], 5, 18)
        jset(ShowDetails.mat[3], 1, 2)
        jset(ShowDetails.mat[3], 2, jcast('int', (-1)))
        jset(ShowDetails.mat[3], 3, 2)
        jset(ShowDetails.mat[3], 4, 0)
        jset(ShowDetails.mat[3], 5, 7)
        jset(ShowDetails.mat[4], 1, 4)
        jset(ShowDetails.mat[4], 2, jcast('int', (-2)))
        jset(ShowDetails.mat[4], 3, 4)
        jset(ShowDetails.mat[4], 4, 0)
        jset(ShowDetails.mat[4], 5, 10)
        ShowDetails.gauss(4)
        ShowDetails.print(4)
        # 表达式冗余，多解
        # 1*x1 + 2*x2 - 1*x3 = 9
        # 2*x1 + 4*x2 - 2*x3 = 18
        # 2*x1 - 1*x2 + 2*x3 = 7
        # 4*x1 - 2*x2 + 4*x3 = 14
        jprint('表达式冗余，多解', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, jcast('int', (-1)))
        jset(ShowDetails.mat[1], 4, 0)
        jset(ShowDetails.mat[1], 5, 9)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 4)
        jset(ShowDetails.mat[2], 3, jcast('int', (-2)))
        jset(ShowDetails.mat[2], 4, 0)
        jset(ShowDetails.mat[2], 5, 18)
        jset(ShowDetails.mat[3], 1, 2)
        jset(ShowDetails.mat[3], 2, jcast('int', (-1)))
        jset(ShowDetails.mat[3], 3, 2)
        jset(ShowDetails.mat[3], 4, 0)
        jset(ShowDetails.mat[3], 5, 7)
        jset(ShowDetails.mat[4], 1, 4)
        jset(ShowDetails.mat[4], 2, jcast('int', (-2)))
        jset(ShowDetails.mat[4], 3, 4)
        jset(ShowDetails.mat[4], 4, 0)
        jset(ShowDetails.mat[4], 5, 14)
        ShowDetails.gauss(4)
        ShowDetails.print(4)
        # 表达式不足，矛盾
        # 1*x1 + 2*x2 - 1*x3 = 5
        # 2*x1 + 4*x2 - 2*x3 = 7
        jprint('表达式不足，矛盾', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, jcast('int', (-1)))
        jset(ShowDetails.mat[1], 4, 5)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 4)
        jset(ShowDetails.mat[2], 3, jcast('int', (-2)))
        jset(ShowDetails.mat[2], 4, 7)
        jset(ShowDetails.mat[3], 1, 0)
        jset(ShowDetails.mat[3], 2, 0)
        jset(ShowDetails.mat[3], 3, 0)
        jset(ShowDetails.mat[3], 4, 0)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        # 表达式不足，多解
        # 1*x1 + 2*x2 - 1*x3 = 5
        # 2*x1 + 2*x2 - 1*x3 = 8
        jprint('表达式不足，多解', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, jcast('int', (-1)))
        jset(ShowDetails.mat[1], 4, 5)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 2)
        jset(ShowDetails.mat[2], 3, jcast('int', (-1)))
        jset(ShowDetails.mat[2], 4, 8)
        jset(ShowDetails.mat[3], 1, 0)
        jset(ShowDetails.mat[3], 2, 0)
        jset(ShowDetails.mat[3], 3, 0)
        jset(ShowDetails.mat[3], 4, 0)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        # 正确区分矛盾、多解、唯一解
        # 0*x1 + 2*x2 = 3
        # 0*x1 + 0*x2 = 0
        jprint('正确区分矛盾、多解、唯一解', newline=True)
        jset(ShowDetails.mat[1], 1, 0)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, 3)
        jset(ShowDetails.mat[2], 1, 0)
        jset(ShowDetails.mat[2], 2, 0)
        jset(ShowDetails.mat[2], 3, 0)
        ShowDetails.gauss(2)
        ShowDetails.print(2)
        # 有些主元可以确定值
        # a  + b + c = 5
        # 2a + b + c = 7
        jprint('有些主元可以确定值', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 1)
        jset(ShowDetails.mat[1], 3, 1)
        jset(ShowDetails.mat[1], 4, 5)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 1)
        jset(ShowDetails.mat[2], 3, 1)
        jset(ShowDetails.mat[2], 4, 7)
        jset(ShowDetails.mat[3], 1, 0)
        jset(ShowDetails.mat[3], 2, 0)
        jset(ShowDetails.mat[3], 3, 0)
        jset(ShowDetails.mat[3], 4, 0)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        # 有些主元还受到自由元的影响
        # a + b = 5
        jprint('有些主元还受到自由元的影响', newline=True)
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 1)
        jset(ShowDetails.mat[1], 3, 5)
        jset(ShowDetails.mat[2], 1, 0)
        jset(ShowDetails.mat[2], 2, 0)
        jset(ShowDetails.mat[2], 3, 0)
        ShowDetails.gauss(2)
        ShowDetails.print(2)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


ShowDetails.MAXN = jcast('int', 101)
ShowDetails.mat = jarray('double', [ShowDetails.MAXN, ShowDetails.MAXN])
ShowDetails.sml = jcast('double', 1e-07)

if __name__ == '__main__':
    ShowDetails.main([])
