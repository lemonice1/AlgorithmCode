# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 已经没有什么好害怕的了
# 给定两个长度为n的数组，a[i]表示第i个糖果的能量，b[i]表示第i个药片的能量
# 所有能量数值都不相同，每一个糖果要选一个药片进行配对
# 如果配对之后，糖果能量 > 药片能量，称为糖果大的配对
# 如果配对之后，糖果能量 < 药片能量，称为药片大的配对
# 希望做到，糖果大的配对数量 = 药片大的配对数量 + k
# 返回配对方法数，答案对 1000000009 取模
# 举例，a = [5, 35, 15, 45]，b = [40, 20, 10, 30]，k = 2，返回4，因为有4种配对方法
# (5-40，35-20，15-10，45-30)、(5-40，35-30，15-10，45-20)
# (5-20，35-30，15-10，45-40)、(5-30，35-20，15-10，45-40)
# 1 <= n <= 2000
# 0 <= k <= n
# 测试链接 : https://www.luogu.com.cn/problem/P4859
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_NothingFear:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'n': 'n', 'k': 'k', 'a': 'a', 'b': 'b', 'fac': 'fac', 'c': 'c', 'small': 'small', 'dp': 'dp', 'g': 'g'}
    MAXN = 0
    MOD = 0
    n = 0
    k = 0
    a = None
    b = None
    fac = None
    c = None
    small = None
    dp = None
    g = None
    @staticmethod
    def build():
        Code04_NothingFear.fac[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code04_NothingFear.n):
            Code04_NothingFear.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (Code04_NothingFear.fac[jcast('int', (i - 1))] * i)), Code04_NothingFear.MOD)))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i <= Code04_NothingFear.n):
            jset(Code04_NothingFear.c[i], 0, 1)
            j = jcast('int', 1)
            while (j <= i):
                jset(Code04_NothingFear.c[i], j, jcast('long', jmod(jcast('long', jadd(Code04_NothingFear.c[jcast('int', (i - 1))][j], Code04_NothingFear.c[jcast('int', (i - 1))][jcast('int', (j - 1))])), Code04_NothingFear.MOD)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        Code04_NothingFear.build()
        jstatic('Arrays', 'sort', Code04_NothingFear.a, 1, jcast('int', jadd(Code04_NothingFear.n, 1)))
        jstatic('Arrays', 'sort', Code04_NothingFear.b, 1, jcast('int', jadd(Code04_NothingFear.n, 1)))
        i = jcast('int', 1)
        cnt = jcast('int', 0)
        while (i <= Code04_NothingFear.n):
            while ((jcast('int', jadd(cnt, 1)) <= Code04_NothingFear.n) and (Code04_NothingFear.b[jcast('int', jadd(cnt, 1))] < Code04_NothingFear.a[i])):
                cnt = jcast('int', (cnt + 1))
            Code04_NothingFear.small[i] = jcast('long', cnt)
            i = jcast('int', (i + 1))
        jset(Code04_NothingFear.dp[0], 0, 1)
        i = jcast('int', 1)
        while (i <= Code04_NothingFear.n):
            jset(Code04_NothingFear.dp[i], 0, Code04_NothingFear.dp[jcast('int', (i - 1))][0])
            j = jcast('int', 1)
            while (j <= i):
                jset(Code04_NothingFear.dp[i], j, jcast('long', jmod(jcast('long', jadd(Code04_NothingFear.dp[jcast('int', (i - 1))][j], jcast('long', jmod(jcast('long', (Code04_NothingFear.dp[jcast('int', (i - 1))][jcast('int', (j - 1))] * jcast('long', jadd(jcast('long', (Code04_NothingFear.small[i] - j)), 1)))), Code04_NothingFear.MOD)))), Code04_NothingFear.MOD)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i <= Code04_NothingFear.n):
            Code04_NothingFear.g[i] = jcast('long', jcast('long', jmod(jcast('long', (Code04_NothingFear.fac[jcast('int', (Code04_NothingFear.n - i))] * Code04_NothingFear.dp[Code04_NothingFear.n][i])), Code04_NothingFear.MOD)))
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', Code04_NothingFear.k)
        while (i <= Code04_NothingFear.n):
            if (jcast('int', (jcast('int', (i - Code04_NothingFear.k)) & 1)) == 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', jmod(jcast('long', (Code04_NothingFear.c[i][Code04_NothingFear.k] * Code04_NothingFear.g[i])), Code04_NothingFear.MOD)))), Code04_NothingFear.MOD)))
            else:
                # -1 和 (MOD-1) 同余
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code04_NothingFear.c[i][Code04_NothingFear.k] * Code04_NothingFear.g[i])), Code04_NothingFear.MOD)) * jcast('int', (Code04_NothingFear.MOD - 1)))), Code04_NothingFear.MOD)))), Code04_NothingFear.MOD)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_NothingFear.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_NothingFear.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code04_NothingFear.n):
            jcall(in_, 'nextToken')
            Code04_NothingFear.a[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_NothingFear.n):
            jcall(in_, 'nextToken')
            Code04_NothingFear.b[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        if (jcast('int', (jcast('int', jadd(Code04_NothingFear.n, Code04_NothingFear.k)) & 1)) == 0):
            Code04_NothingFear.k = jcast('int', jcast('int', jdiv(jcast('int', jadd(Code04_NothingFear.n, Code04_NothingFear.k)), 2)))
            jcall(out, 'println', Code04_NothingFear.compute())
        else:
            jcall(out, 'println', 0)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_NothingFear.MAXN = jcast('int', 2001)
Code04_NothingFear.MOD = jcast('int', 1000000009)
Code04_NothingFear.n = jcast('int', 0)
Code04_NothingFear.k = jcast('int', 0)
Code04_NothingFear.a = jarray('int', [Code04_NothingFear.MAXN])
Code04_NothingFear.b = jarray('int', [Code04_NothingFear.MAXN])
Code04_NothingFear.fac = jarray('long', [Code04_NothingFear.MAXN])
Code04_NothingFear.c = jarray('long', [Code04_NothingFear.MAXN, Code04_NothingFear.MAXN])
Code04_NothingFear.small = jarray('long', [Code04_NothingFear.MAXN])
Code04_NothingFear.dp = jarray('long', [Code04_NothingFear.MAXN, Code04_NothingFear.MAXN])
Code04_NothingFear.g = jarray('long', [Code04_NothingFear.MAXN])

if __name__ == '__main__':
    Code04_NothingFear.main([])
