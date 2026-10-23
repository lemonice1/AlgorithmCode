# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 杨辉三角
# 给定数字n，打印杨辉三角的前n行
# 1 <= n <= 20
# 测试链接 : https://www.luogu.com.cn/problem/P5732
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_PascalTriangle:
    __java_fields__ = {'MAXN': 'MAXN', 'tri': 'tri'}
    MAXN = 0
    tri = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < n):
            jset(Code01_PascalTriangle.tri[i], 0, jset(Code01_PascalTriangle.tri[i], i, 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < n):
            j = jcast('int', 1)
            while (j < i):
                jset(Code01_PascalTriangle.tri[i], j, jcast('long', jadd(Code01_PascalTriangle.tri[jcast('int', (i - 1))][j], Code01_PascalTriangle.tri[jcast('int', (i - 1))][jcast('int', (j - 1))])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j <= i):
                jcall(out, 'print', jadd(Code01_PascalTriangle.tri[i][j], ' '))
                j = jcast('int', (j + 1))
            jcall(out, 'println')
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_PascalTriangle.MAXN = jcast('int', 20)
Code01_PascalTriangle.tri = jarray('long', [Code01_PascalTriangle.MAXN, Code01_PascalTriangle.MAXN])

if __name__ == '__main__':
    Code01_PascalTriangle.main([])
