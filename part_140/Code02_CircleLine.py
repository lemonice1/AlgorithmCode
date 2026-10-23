# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 圆上连线
# 圆上有2n个点，这些点成对连接起来，形成n条线段，任意两条线段不能相交，返回连接的方法数
# 注意！答案不对 10^9 + 7 取模！而是对 10^8 + 7 取模！
# 1 <= n <= 2999
# 测试链接 : https://www.luogu.com.cn/problem/P1976
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_CircleLine:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'fac': 'fac', 'inv': 'inv'}
    MOD = 0
    MAXN = 0
    fac = None
    inv = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        jset(Code02_CircleLine.fac, 0, jset(Code02_CircleLine.inv, 0, 1))
        Code02_CircleLine.fac[1] = jcast('long', 1)
        i = jcast('int', 2)
        while (i <= n):
            Code02_CircleLine.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', i) * Code02_CircleLine.fac[jcast('int', (i - 1))])), Code02_CircleLine.MOD)))
            i = jcast('int', (i + 1))
        jset(Code02_CircleLine.inv, n, Code02_CircleLine.power(Code02_CircleLine.fac[n], jcast('int', (Code02_CircleLine.MOD - 2))))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 1):
            Code02_CircleLine.inv[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jcast('int', jadd(i, 1))) * Code02_CircleLine.inv[jcast('int', jadd(i, 1))])), Code02_CircleLine.MOD)))
            i = jcast('int', (i - 1))

    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code02_CircleLine.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code02_CircleLine.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    @staticmethod
    def c(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        return jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code02_CircleLine.fac[n] * Code02_CircleLine.inv[k])), Code02_CircleLine.MOD)) * Code02_CircleLine.inv[jcast('int', (n - k))])), Code02_CircleLine.MOD)))

    # 这里用公式1
    @staticmethod
    def compute(n):
        n = jcast('int', n)
        Code02_CircleLine.build(jcast('int', (2 * n)))
        return jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (Code02_CircleLine.c(jcast('int', (2 * n)), n) - Code02_CircleLine.c(jcast('int', (2 * n)), jcast('int', (n - 1))))), Code02_CircleLine.MOD)), Code02_CircleLine.MOD)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code02_CircleLine.compute(n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CircleLine.MOD = jcast('int', 100000007)
Code02_CircleLine.MAXN = jcast('int', 1000001)
Code02_CircleLine.fac = jarray('long', [Code02_CircleLine.MAXN])
Code02_CircleLine.inv = jarray('long', [Code02_CircleLine.MAXN])

if __name__ == '__main__':
    Code02_CircleLine.main([])
