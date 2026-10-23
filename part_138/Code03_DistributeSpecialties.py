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

# 分特产
# 一共有m种特产，arr[i]表示i种特产有几个
# 一共有n个同学，每个同学至少要得到一个特产
# 返回分配特产的方法数，答案对 1000000007 取模
# 0 <= n、m <= 1000
# 0 <= arr[i] <= 1000
# 测试链接 : https://www.luogu.com.cn/problem/P5505
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_DistributeSpecialties:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'MOD': 'MOD', 'arr': 'arr', 'c': 'c', 'g': 'g', 'n': 'n', 'k': 'k', 'm': 'm'}
    MAXN = 0
    MAXK = 0
    MOD = 0
    arr = None
    c = None
    g = None
    n = 0
    k = 0
    m = 0
    @staticmethod
    def compute():
        i = jcast('int', 0)
        while (i <= Code03_DistributeSpecialties.k):
            jset(Code03_DistributeSpecialties.c[i], 0, 1)
            j = jcast('int', 1)
            while (j <= i):
                jset(Code03_DistributeSpecialties.c[i], j, jcast('long', jmod(jcast('long', jadd(Code03_DistributeSpecialties.c[jcast('int', (i - 1))][j], Code03_DistributeSpecialties.c[jcast('int', (i - 1))][jcast('int', (j - 1))])), Code03_DistributeSpecialties.MOD)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code03_DistributeSpecialties.n):
            Code03_DistributeSpecialties.g[i] = jcast('long', Code03_DistributeSpecialties.c[Code03_DistributeSpecialties.n][i])
            j = jcast('int', 1)
            while (j <= Code03_DistributeSpecialties.m):
                Code03_DistributeSpecialties.g[i] = jcast('long', jcast('int', jcast('long', jmod(jcast('long', (Code03_DistributeSpecialties.g[i] * Code03_DistributeSpecialties.c[jcast('int', (jcast('int', (jcast('int', jadd(Code03_DistributeSpecialties.arr[j], Code03_DistributeSpecialties.n)) - i)) - 1))][jcast('int', (jcast('int', (Code03_DistributeSpecialties.n - i)) - 1))])), Code03_DistributeSpecialties.MOD))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code03_DistributeSpecialties.g[Code03_DistributeSpecialties.n] = jcast('long', 0)
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while (i <= Code03_DistributeSpecialties.n):
            if (jcast('int', (i & 1)) == 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, Code03_DistributeSpecialties.g[i])), Code03_DistributeSpecialties.MOD)))
            else:
                # -1 和 (MOD-1) 同余
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', jmod(jcast('long', (Code03_DistributeSpecialties.g[i] * jcast('int', (Code03_DistributeSpecialties.MOD - 1)))), Code03_DistributeSpecialties.MOD)))), Code03_DistributeSpecialties.MOD)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_DistributeSpecialties.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_DistributeSpecialties.k = jcast('int', jcast('int', (Code03_DistributeSpecialties.n * 2)))
        jcall(in_, 'nextToken')
        Code03_DistributeSpecialties.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_DistributeSpecialties.m):
            jcall(in_, 'nextToken')
            Code03_DistributeSpecialties.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code03_DistributeSpecialties.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_DistributeSpecialties.MAXN = jcast('int', 1001)
Code03_DistributeSpecialties.MAXK = jcast('int', jcast('int', (Code03_DistributeSpecialties.MAXN * 2)))
Code03_DistributeSpecialties.MOD = jcast('int', 1000000007)
Code03_DistributeSpecialties.arr = jarray('int', [Code03_DistributeSpecialties.MAXN])
Code03_DistributeSpecialties.c = jarray('long', [Code03_DistributeSpecialties.MAXK, Code03_DistributeSpecialties.MAXK])
Code03_DistributeSpecialties.g = jarray('long', [Code03_DistributeSpecialties.MAXN])
Code03_DistributeSpecialties.n = jcast('int', 0)
Code03_DistributeSpecialties.k = jcast('int', 0)
Code03_DistributeSpecialties.m = jcast('int', 0)

if __name__ == '__main__':
    Code03_DistributeSpecialties.main([])
