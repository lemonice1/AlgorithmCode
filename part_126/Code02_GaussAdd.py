# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 高斯消元解决加法方程组模版(区分矛盾、多解、唯一解)
# 一共有n个变量，给定n个加法方程，构成一个加法方程组
# 如果方程组存在矛盾，打印-1
# 如果方程组无法确定唯一解，打印0
# 如果方程组存在唯一解，打印每个变量的值，保留小数点后两位
# 1 <= n <= 50
# 测试链接 : https://www.luogu.com.cn/problem/P2455
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_GaussAdd:
    __java_fields__ = {'MAXN': 'MAXN', 'mat': 'mat', 'n': 'n', 'sml': 'sml'}
    MAXN = 0
    mat = None
    n = 0
    # 0.0000001 == 1e-7
    # 因为double类型有精度问题，所以认为
    # 如果一个数字绝对值 <  sml，则认为该数字是0
    # 如果一个数字绝对值 >= sml，则认为该数字不是0
    sml = 0.0
    # 高斯消元解决加法方程组模版
    # 需要保证变量有n个，表达式也有n个
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                # 本题需要严格区分矛盾、多解、唯一解，所以必须这么写
                max = jcast('int', i)
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        if ((j < i) and (jstatic('Math', 'abs', Code02_GaussAdd.mat[j][j]) >= Code02_GaussAdd.sml)):
                            raise JContinue(None)
                        if (jstatic('Math', 'abs', Code02_GaussAdd.mat[j][i]) > jstatic('Math', 'abs', Code02_GaussAdd.mat[max][i])):
                            max = jcast('int', j)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                Code02_GaussAdd.swap(i, max)
                if (jstatic('Math', 'abs', Code02_GaussAdd.mat[i][i]) >= Code02_GaussAdd.sml):
                    tmp = jcast('double', Code02_GaussAdd.mat[i][i])
                    j = jcast('int', i)
                    while (j <= jcast('int', jadd(n, 1))):
                        ((_java_obj_3 := Code02_GaussAdd.mat[i]), (_java_key_4 := j), jset(_java_obj_3, _java_key_4, jdiv(jget(_java_obj_3, _java_key_4), tmp)))[2]
                        j = jcast('int', (j + 1))
                    j = jcast('int', 1)
                    while (j <= n):
                        if (i != j):
                            rate = jcast('double', jdiv(Code02_GaussAdd.mat[j][i], Code02_GaussAdd.mat[i][i]))
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                ((_java_obj_5 := Code02_GaussAdd.mat[j]), (_java_key_6 := k), jset(_java_obj_5, _java_key_6, (jget(_java_obj_5, _java_key_6) - (Code02_GaussAdd.mat[i][k] * rate))))[2]
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
        tmp = Code02_GaussAdd.mat[a]
        Code02_GaussAdd.mat[a] = Code02_GaussAdd.mat[b]
        Code02_GaussAdd.mat[b] = tmp

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_GaussAdd.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code02_GaussAdd.n):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(Code02_GaussAdd.n, 1))):
                jcall(in_, 'nextToken')
                jset(Code02_GaussAdd.mat[i], j, jcast('double', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code02_GaussAdd.gauss(Code02_GaussAdd.n)
        sign = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= Code02_GaussAdd.n):
            try:
                if ((jstatic('Math', 'abs', Code02_GaussAdd.mat[i][i]) < Code02_GaussAdd.sml) and (jstatic('Math', 'abs', Code02_GaussAdd.mat[i][jcast('int', jadd(Code02_GaussAdd.n, 1))]) >= Code02_GaussAdd.sml)):
                    sign = jcast('int', jcast('int', (-1)))
                    raise JBreak(None)
                if (jstatic('Math', 'abs', Code02_GaussAdd.mat[i][i]) < Code02_GaussAdd.sml):
                    sign = jcast('int', 0)
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if (sign == 1):
            i = jcast('int', 1)
            while (i <= Code02_GaussAdd.n):
                jcall(out, 'printf', jadd(jadd(jadd('x', i), '='), '%.2f\n'), Code02_GaussAdd.mat[i][jcast('int', jadd(Code02_GaussAdd.n, 1))])
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', sign)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_GaussAdd.MAXN = jcast('int', 52)
Code02_GaussAdd.mat = jarray('double', [Code02_GaussAdd.MAXN, Code02_GaussAdd.MAXN])
Code02_GaussAdd.n = jcast('int', 0)
Code02_GaussAdd.sml = jcast('double', 1e-07)

if __name__ == '__main__':
    Code02_GaussAdd.main([])
