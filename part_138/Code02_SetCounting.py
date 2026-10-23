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

# 集合计数
# 一共有n个不同的数，能构成2^n个不同集合
# 在2^n个集合中挑出若干个集合，至少挑一个
# 希望这若干个集合的交集，正好有k个数
# 返回挑选集合的方案数，答案对 1000000007 取模
# 1 <= n <= 10^6
# 0 <= k <= n
# 测试链接 : https://www.luogu.com.cn/problem/P10596
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_SetCounting:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'fac': 'fac', 'inv': 'inv', 'g': 'g', 'n': 'n', 'k': 'k'}
    MAXN = 0
    MOD = 0
    fac = None
    inv = None
    g = None
    n = 0
    k = 0
    @staticmethod
    def build():
        jset(Code02_SetCounting.fac, 0, jset(Code02_SetCounting.inv, 0, 1))
        Code02_SetCounting.fac[1] = jcast('long', 1)
        i = jcast('int', 2)
        while (i <= Code02_SetCounting.n):
            Code02_SetCounting.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', i) * Code02_SetCounting.fac[jcast('int', (i - 1))])), Code02_SetCounting.MOD)))
            i = jcast('int', (i + 1))
        jset(Code02_SetCounting.inv, Code02_SetCounting.n, Code02_SetCounting.power(Code02_SetCounting.fac[Code02_SetCounting.n], jcast('int', (Code02_SetCounting.MOD - 2))))
        i = jcast('int', jcast('int', (Code02_SetCounting.n - 1)))
        while (i >= 1):
            Code02_SetCounting.inv[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jcast('int', jadd(i, 1))) * Code02_SetCounting.inv[jcast('int', jadd(i, 1))])), Code02_SetCounting.MOD)))
            i = jcast('int', (i - 1))

    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code02_SetCounting.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code02_SetCounting.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    @staticmethod
    def c(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        return jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code02_SetCounting.fac[n] * Code02_SetCounting.inv[k])), Code02_SetCounting.MOD)) * Code02_SetCounting.inv[jcast('int', (n - k))])), Code02_SetCounting.MOD)))

    @staticmethod
    def compute():
        Code02_SetCounting.build()
        tmp = jcast('long', 2)
        i = jcast('int', Code02_SetCounting.n)
        while (i >= 0):
            Code02_SetCounting.g[i] = jcast('long', tmp)
            tmp = jcast('long', jcast('long', jmod(jcast('long', (tmp * tmp)), Code02_SetCounting.MOD)))
            i = jcast('int', (i - 1))
        i = jcast('int', 0)
        while (i <= Code02_SetCounting.n):
            # -1 和 (MOD-1) 同余
            jset(Code02_SetCounting.g, i, jcast('long', jmod(jcast('long', (jcast('long', (jcast('long', jadd(Code02_SetCounting.g[i], Code02_SetCounting.MOD)) - 1)) * Code02_SetCounting.c(Code02_SetCounting.n, i))), Code02_SetCounting.MOD)))
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', Code02_SetCounting.k)
        while (i <= Code02_SetCounting.n):
            if (jcast('int', (jcast('int', (i - Code02_SetCounting.k)) & 1)) == 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', jmod(jcast('long', (Code02_SetCounting.c(i, Code02_SetCounting.k) * Code02_SetCounting.g[i])), Code02_SetCounting.MOD)))), Code02_SetCounting.MOD)))
            else:
                # -1 和 (MOD-1) 同余
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code02_SetCounting.c(i, Code02_SetCounting.k) * Code02_SetCounting.g[i])), Code02_SetCounting.MOD)) * jcast('int', (Code02_SetCounting.MOD - 1)))), Code02_SetCounting.MOD)))), Code02_SetCounting.MOD)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_SetCounting.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_SetCounting.k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code02_SetCounting.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SetCounting.MAXN = jcast('int', 1000001)
Code02_SetCounting.MOD = jcast('int', 1000000007)
Code02_SetCounting.fac = jarray('long', [Code02_SetCounting.MAXN])
Code02_SetCounting.inv = jarray('long', [Code02_SetCounting.MAXN])
Code02_SetCounting.g = jarray('long', [Code02_SetCounting.MAXN])
Code02_SetCounting.n = jcast('int', 0)
Code02_SetCounting.k = jcast('int', 0)

if __name__ == '__main__':
    Code02_SetCounting.main([])
