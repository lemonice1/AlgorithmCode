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

# 组合数问题
# 组合公式c(i, j)，表示从i个物品中选出j个物品的方案数
# 如果该数值是k的整数倍，那么称(i, j)是一个合法对
# 给定具体的一组数字n和m，当i和j满足：0 <= i <= n，0 <= j <= min(i, m)
# 返回有多少合法对
# 一共有t组测试，所有测试的k都为同一个值
# 每组测试给定n和m，打印每组测试的答案
# 1 <= t <= 10^4
# 2 <= k <= 21
# 0 <= n、m <= 2000
# 测试链接 : https://www.luogu.com.cn/problem/P2822
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_CombinationNumber:
    __java_fields__ = {'MAXV': 'MAXV', 'MAXN': 'MAXN', 'c': 'c', 'f': 'f', 'sum': 'sum', 't': 't', 'k': 'k', 'n': 'n', 'm': 'm'}
    MAXV = 0
    MAXN = 0
    c = None
    f = None
    sum = None
    t = 0
    k = 0
    n = 0
    m = 0
    @staticmethod
    def build():
        i = jcast('int', 0)
        while (i <= Code03_CombinationNumber.MAXV):
            jset(Code03_CombinationNumber.c[i], 0, 1)
            j = jcast('int', 1)
            while (j <= i):
                jset(Code03_CombinationNumber.c[i], j, jcast('int', jmod(jcast('int', jadd(Code03_CombinationNumber.c[jcast('int', (i - 1))][j], Code03_CombinationNumber.c[jcast('int', (i - 1))][jcast('int', (j - 1))])), Code03_CombinationNumber.k)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_CombinationNumber.MAXV):
            j = jcast('int', 1)
            while (j <= i):
                jset(Code03_CombinationNumber.f[i], j, (1 if (jcast('int', jmod(Code03_CombinationNumber.c[i][j], Code03_CombinationNumber.k)) == 0) else 0))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 2)
        while (i <= Code03_CombinationNumber.MAXV):
            j = jcast('int', 1)
            while (j <= i):
                jset(Code03_CombinationNumber.sum[i], j, jcast('int', jadd(jcast('int', (jcast('int', jadd(Code03_CombinationNumber.sum[i][jcast('int', (j - 1))], Code03_CombinationNumber.sum[jcast('int', (i - 1))][j])) - Code03_CombinationNumber.sum[jcast('int', (i - 1))][jcast('int', (j - 1))])), Code03_CombinationNumber.f[i][j])))
                j = jcast('int', (j + 1))
            jset(Code03_CombinationNumber.sum[i], jcast('int', jadd(i, 1)), Code03_CombinationNumber.sum[i][i])
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_CombinationNumber.t = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_CombinationNumber.k = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_CombinationNumber.build()
        i = jcast('int', 1)
        while (i <= Code03_CombinationNumber.t):
            jcall(in_, 'nextToken')
            Code03_CombinationNumber.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_CombinationNumber.m = jcast('int', jcast('int', jget(in_, 'nval')))
            if (Code03_CombinationNumber.m > Code03_CombinationNumber.n):
                jcall(out, 'println', Code03_CombinationNumber.sum[Code03_CombinationNumber.n][Code03_CombinationNumber.n])
            else:
                jcall(out, 'println', Code03_CombinationNumber.sum[Code03_CombinationNumber.n][Code03_CombinationNumber.m])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_CombinationNumber.MAXV = jcast('int', 2000)
Code03_CombinationNumber.MAXN = jcast('int', 2002)
Code03_CombinationNumber.c = jarray('int', [Code03_CombinationNumber.MAXN, Code03_CombinationNumber.MAXN])
Code03_CombinationNumber.f = jarray('int', [Code03_CombinationNumber.MAXN, Code03_CombinationNumber.MAXN])
Code03_CombinationNumber.sum = jarray('int', [Code03_CombinationNumber.MAXN, Code03_CombinationNumber.MAXN])
Code03_CombinationNumber.t = jcast('int', 0)
Code03_CombinationNumber.k = jcast('int', 0)
Code03_CombinationNumber.n = jcast('int', 0)
Code03_CombinationNumber.m = jcast('int', 0)

if __name__ == '__main__':
    Code03_CombinationNumber.main([])
