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

# 二维差分模版(牛客)
# 测试链接 : https://www.nowcoder.com/practice/50e1a93989df42efb0b1dec386fb4ccc
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_DiffMatrixNowcoder:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'diff': 'diff', 'n': 'n', 'm': 'm', 'q': 'q'}
    MAXN = 0
    MAXM = 0
    diff = None
    n = 0
    m = 0
    q = 0
    @staticmethod
    def add(a, b, c, d, k):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        k = jcast('int', k)
        ((_java_obj_1 := Code03_DiffMatrixNowcoder.diff[a]), (_java_key_2 := b), jset(_java_obj_1, _java_key_2, jcast('long', jadd(jget(_java_obj_1, _java_key_2), k))))[2]
        ((_java_obj_3 := Code03_DiffMatrixNowcoder.diff[jcast('int', jadd(c, 1))]), (_java_key_4 := b), jset(_java_obj_3, _java_key_4, jcast('long', (jget(_java_obj_3, _java_key_4) - k))))[2]
        ((_java_obj_5 := Code03_DiffMatrixNowcoder.diff[a]), (_java_key_6 := jcast('int', jadd(d, 1))), jset(_java_obj_5, _java_key_6, jcast('long', (jget(_java_obj_5, _java_key_6) - k))))[2]
        ((_java_obj_7 := Code03_DiffMatrixNowcoder.diff[jcast('int', jadd(c, 1))]), (_java_key_8 := jcast('int', jadd(d, 1))), jset(_java_obj_7, _java_key_8, jcast('long', jadd(jget(_java_obj_7, _java_key_8), k))))[2]

    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code03_DiffMatrixNowcoder.n):
            j = jcast('int', 1)
            while (j <= Code03_DiffMatrixNowcoder.m):
                ((_java_obj_9 := Code03_DiffMatrixNowcoder.diff[i]), (_java_key_10 := j), jset(_java_obj_9, _java_key_10, jcast('long', jadd(jget(_java_obj_9, _java_key_10), jcast('long', (jcast('long', jadd(Code03_DiffMatrixNowcoder.diff[jcast('int', (i - 1))][j], Code03_DiffMatrixNowcoder.diff[i][jcast('int', (j - 1))])) - Code03_DiffMatrixNowcoder.diff[jcast('int', (i - 1))][jcast('int', (j - 1))]))))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= jcast('int', jadd(Code03_DiffMatrixNowcoder.n, 1))):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(Code03_DiffMatrixNowcoder.m, 1))):
                jset(Code03_DiffMatrixNowcoder.diff[i], j, 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_DiffMatrixNowcoder.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_DiffMatrixNowcoder.m = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_DiffMatrixNowcoder.q = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code03_DiffMatrixNowcoder.n):
                j = jcast('int', 1)
                while (j <= Code03_DiffMatrixNowcoder.m):
                    jcall(in_, 'nextToken')
                    Code03_DiffMatrixNowcoder.add(i, j, i, j, jcast('int', jget(in_, 'nval')))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            a = 0
            b = 0
            c = 0
            d = 0
            k = 0
            while (i <= Code03_DiffMatrixNowcoder.q):
                jcall(in_, 'nextToken')
                a = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                b = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                c = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                d = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                k = jcast('int', jcast('int', jget(in_, 'nval')))
                Code03_DiffMatrixNowcoder.add(a, b, c, d, k)
                i = jcast('int', (i + 1))
            Code03_DiffMatrixNowcoder.build()
            i = jcast('int', 1)
            while (i <= Code03_DiffMatrixNowcoder.n):
                jcall(out, 'print', Code03_DiffMatrixNowcoder.diff[i][1])
                j = jcast('int', 2)
                while (j <= Code03_DiffMatrixNowcoder.m):
                    jcall(out, 'print', jadd(' ', Code03_DiffMatrixNowcoder.diff[i][j]))
                    j = jcast('int', (j + 1))
                jcall(out, 'println')
                i = jcast('int', (i + 1))
            Code03_DiffMatrixNowcoder.clear()
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_DiffMatrixNowcoder.MAXN = jcast('int', 1005)
Code03_DiffMatrixNowcoder.MAXM = jcast('int', 1005)
Code03_DiffMatrixNowcoder.diff = jarray('long', [Code03_DiffMatrixNowcoder.MAXN, Code03_DiffMatrixNowcoder.MAXM])
Code03_DiffMatrixNowcoder.n = jcast('int', 0)
Code03_DiffMatrixNowcoder.m = jcast('int', 0)
Code03_DiffMatrixNowcoder.q = jcast('int', 0)

if __name__ == '__main__':
    Code03_DiffMatrixNowcoder.main([])
