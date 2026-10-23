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

# 二维差分模版(洛谷)
# 测试链接 : https://www.luogu.com.cn/problem/P3397
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_DiffMatrixLuogu:
    __java_fields__ = {'MAXN': 'MAXN', 'diff': 'diff', 'n': 'n', 'q': 'q'}
    MAXN = 0
    diff = None
    n = 0
    q = 0
    @staticmethod
    def add(a, b, c, d, k):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        k = jcast('int', k)
        ((_java_obj_1 := Code03_DiffMatrixLuogu.diff[a]), (_java_key_2 := b), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), k))))[2]
        ((_java_obj_3 := Code03_DiffMatrixLuogu.diff[jcast('int', jadd(c, 1))]), (_java_key_4 := b), jset(_java_obj_3, _java_key_4, jcast('int', (jget(_java_obj_3, _java_key_4) - k))))[2]
        ((_java_obj_5 := Code03_DiffMatrixLuogu.diff[a]), (_java_key_6 := jcast('int', jadd(d, 1))), jset(_java_obj_5, _java_key_6, jcast('int', (jget(_java_obj_5, _java_key_6) - k))))[2]
        ((_java_obj_7 := Code03_DiffMatrixLuogu.diff[jcast('int', jadd(c, 1))]), (_java_key_8 := jcast('int', jadd(d, 1))), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), k))))[2]

    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code03_DiffMatrixLuogu.n):
            j = jcast('int', 1)
            while (j <= Code03_DiffMatrixLuogu.n):
                ((_java_obj_9 := Code03_DiffMatrixLuogu.diff[i]), (_java_key_10 := j), jset(_java_obj_9, _java_key_10, jcast('int', jadd(jget(_java_obj_9, _java_key_10), jcast('int', (jcast('int', jadd(Code03_DiffMatrixLuogu.diff[jcast('int', (i - 1))][j], Code03_DiffMatrixLuogu.diff[i][jcast('int', (j - 1))])) - Code03_DiffMatrixLuogu.diff[jcast('int', (i - 1))][jcast('int', (j - 1))]))))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= jcast('int', jadd(Code03_DiffMatrixLuogu.n, 1))):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(Code03_DiffMatrixLuogu.n, 1))):
                jset(Code03_DiffMatrixLuogu.diff[i], j, 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_DiffMatrixLuogu.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_DiffMatrixLuogu.q = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            a = 0
            b = 0
            c = 0
            d = 0
            while (i <= Code03_DiffMatrixLuogu.q):
                jcall(in_, 'nextToken')
                a = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                b = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                c = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                d = jcast('int', jcast('int', jget(in_, 'nval')))
                Code03_DiffMatrixLuogu.add(a, b, c, d, 1)
                i = jcast('int', (i + 1))
            Code03_DiffMatrixLuogu.build()
            i = jcast('int', 1)
            while (i <= Code03_DiffMatrixLuogu.n):
                jcall(out, 'print', Code03_DiffMatrixLuogu.diff[i][1])
                j = jcast('int', 2)
                while (j <= Code03_DiffMatrixLuogu.n):
                    jcall(out, 'print', jadd(' ', Code03_DiffMatrixLuogu.diff[i][j]))
                    j = jcast('int', (j + 1))
                jcall(out, 'println')
                i = jcast('int', (i + 1))
            Code03_DiffMatrixLuogu.clear()
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_DiffMatrixLuogu.MAXN = jcast('int', 1002)
Code03_DiffMatrixLuogu.diff = jarray('int', [Code03_DiffMatrixLuogu.MAXN, Code03_DiffMatrixLuogu.MAXN])
Code03_DiffMatrixLuogu.n = jcast('int', 0)
Code03_DiffMatrixLuogu.q = jcast('int', 0)

if __name__ == '__main__':
    Code03_DiffMatrixLuogu.main([])
