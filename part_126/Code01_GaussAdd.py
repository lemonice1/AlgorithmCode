# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 高斯消元解决加法方程组模版(区分是否有唯一解)
# 一共有n个变量，给定n个加法方程，构成一个加法方程组
# 如果方程组存在矛盾或者无法确定唯一解，打印"No Solution"
# 如果方程组存在唯一解，打印每个变量的值，保留小数点后两位
# 1 <= n <= 100
# 测试链接 : https://www.luogu.com.cn/problem/P3389
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_GaussAdd:
    __java_fields__ = {'MAXN': 'MAXN', 'mat': 'mat', 'n': 'n', 'sml': 'sml'}
    MAXN = 0
    mat = None
    n = 0
    # 0.0000001 == 1e-7
    # 因为double类型有精度问题，所以认为
    # 如果一个数字绝对值 <  sml，则认为该数字是0
    # 如果一个数字绝对值 >= sml，则认为该数字不是0
    sml = 0.0
    # 需要保证变量有n个，表达式也有n个
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            # 本题一旦没有唯一解，直接打印"No Solution"，于是可以这么写
            max = jcast('int', i)
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j <= n):
                if (jstatic('Math', 'abs', Code01_GaussAdd.mat[j][i]) > jstatic('Math', 'abs', Code01_GaussAdd.mat[max][i])):
                    max = jcast('int', j)
                j = jcast('int', (j + 1))
            Code01_GaussAdd.swap(i, max)
            if (jstatic('Math', 'abs', Code01_GaussAdd.mat[i][i]) < Code01_GaussAdd.sml):
                return jcast('int', 0)
            tmp = jcast('double', Code01_GaussAdd.mat[i][i])
            j = jcast('int', i)
            while (j <= jcast('int', jadd(n, 1))):
                ((_java_obj_1 := Code01_GaussAdd.mat[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jdiv(jget(_java_obj_1, _java_key_2), tmp)))[2]
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j <= n):
                if (i != j):
                    rate = jcast('double', jdiv(Code01_GaussAdd.mat[j][i], Code01_GaussAdd.mat[i][i]))
                    k = jcast('int', i)
                    while (k <= jcast('int', jadd(n, 1))):
                        ((_java_obj_3 := Code01_GaussAdd.mat[j]), (_java_key_4 := k), jset(_java_obj_3, _java_key_4, (jget(_java_obj_3, _java_key_4) - (Code01_GaussAdd.mat[i][k] * rate))))[2]
                        k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', 1)

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = Code01_GaussAdd.mat[a]
        Code01_GaussAdd.mat[a] = Code01_GaussAdd.mat[b]
        Code01_GaussAdd.mat[b] = tmp

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_GaussAdd.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_GaussAdd.n):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(Code01_GaussAdd.n, 1))):
                jcall(in_, 'nextToken')
                jset(Code01_GaussAdd.mat[i], j, jcast('double', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        sign = jcast('int', Code01_GaussAdd.gauss(Code01_GaussAdd.n))
        if (sign == 0):
            jcall(out, 'println', 'No Solution')
        else:
            i = jcast('int', 1)
            while (i <= Code01_GaussAdd.n):
                jcall(out, 'printf', '%.2f\n', Code01_GaussAdd.mat[i][jcast('int', jadd(Code01_GaussAdd.n, 1))])
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_GaussAdd.MAXN = jcast('int', 102)
Code01_GaussAdd.mat = jarray('double', [Code01_GaussAdd.MAXN, Code01_GaussAdd.MAXN])
Code01_GaussAdd.n = jcast('int', 0)
Code01_GaussAdd.sml = jcast('double', 1e-07)

if __name__ == '__main__':
    Code01_GaussAdd.main([])
