# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 背包(两次转圈法)
# 一共有n种物品，第i种物品的体积为v[i]，价值为c[i]，每种物品可以选择任意个，个数不能是负数
# 一共有m条查询，每次查询都会给定jobv，代表体积的要求
# 要求挑选物品的体积和一定要严格是jobv，返回能得到的最大价值和
# 如果没有方案能正好凑满jobv，返回-1
# 1 <= n <= 50
# 1 <= m <= 10^5
# 1 <= v[i] <= 10^5
# 1 <= c[i] <= 10^6
# 10^11 <= jobv <= 10^12
# 测试链接 : https://www.luogu.com.cn/problem/P9140
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Knapsack:
    __java_fields__ = {'MAXN': 'MAXN', 'inf': 'inf', 'v': 'v', 'c': 'c', 'dp': 'dp', 'n': 'n', 'm': 'm', 'x': 'x', 'y': 'y'}
    MAXN = 0
    inf = 0
    v = None
    c = None
    # dp[i] : 总体积为某数，先尽可能用基准物品填入，剩余的体积为i
    # 可以去掉若干基准物品，加入若干其他物品，最终凑齐总体积
    # 能获得的最大补偿是多少
    dp = None
    n = 0
    m = 0
    x = 0
    y = 0
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code05_Knapsack.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def compute():
        jstatic('Arrays', 'fill', Code05_Knapsack.dp, 0, Code05_Knapsack.x, Code05_Knapsack.inf)
        Code05_Knapsack.dp[0] = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code05_Knapsack.n):
            if (Code05_Knapsack.v[i] != Code05_Knapsack.x):
                j = jcast('int', 0)
                d = jcast('int', Code05_Knapsack.gcd(Code05_Knapsack.v[i], Code05_Knapsack.x))
                while (j < d):
                    cur = jcast('int', j)
                    next = 0
                    circle = jcast('int', 0)
                    while (circle < 2):
                        next = jcast('int', jcast('int', jmod(jcast('int', jadd(cur, Code05_Knapsack.v[i])), Code05_Knapsack.x)))
                        if (Code05_Knapsack.dp[cur] != Code05_Knapsack.inf):
                            jset(Code05_Knapsack.dp, next, jstatic('Math', 'max', Code05_Knapsack.dp[next], jcast('long', jadd(jcast('long', (Code05_Knapsack.dp[cur] - jcast('long', (jcast('long', jcast('int', jdiv(jcast('int', jadd(cur, Code05_Knapsack.v[i])), Code05_Knapsack.x))) * Code05_Knapsack.y)))), Code05_Knapsack.c[i]))))
                        cur = jcast('int', next)
                        circle = jcast('int', jcast('int', jadd(circle, (1 if (cur == j) else 0))))
                    j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_Knapsack.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_Knapsack.m = jcast('int', jcast('int', jget(in_, 'nval')))
        best = jcast('double', 0)
        ratio = 0.0
        i = jcast('int', 1)
        while (i <= Code05_Knapsack.n):
            jcall(in_, 'nextToken')
            Code05_Knapsack.v[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_Knapsack.c[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            ratio = jcast('double', jdiv(jcast('double', Code05_Knapsack.c[i]), Code05_Knapsack.v[i]))
            if (ratio > best):
                best = jcast('double', ratio)
                Code05_Knapsack.x = jcast('int', Code05_Knapsack.v[i])
                Code05_Knapsack.y = jcast('int', Code05_Knapsack.c[i])
            i = jcast('int', (i + 1))
        Code05_Knapsack.compute()
        jobv = 0
        i = jcast('int', 1)
        v = 0
        while (i <= Code05_Knapsack.m):
            jcall(in_, 'nextToken')
            jobv = jcast('long', jcast('long', jget(in_, 'nval')))
            v = jcast('int', jcast('int', jcast('long', jmod(jobv, Code05_Knapsack.x))))
            if (Code05_Knapsack.dp[v] == Code05_Knapsack.inf):
                jcall(out, 'println', '-1')
            else:
                jcall(out, 'println', jcast('long', jadd(jcast('long', (jcast('long', jdiv(jobv, Code05_Knapsack.x)) * Code05_Knapsack.y)), Code05_Knapsack.dp[v])))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Knapsack.MAXN = jcast('int', 100001)
Code05_Knapsack.inf = jcast('long', jget(Long, 'MIN_VALUE'))
Code05_Knapsack.v = jarray('int', [Code05_Knapsack.MAXN])
Code05_Knapsack.c = jarray('int', [Code05_Knapsack.MAXN])
Code05_Knapsack.dp = jarray('long', [Code05_Knapsack.MAXN])
Code05_Knapsack.n = jcast('int', 0)
Code05_Knapsack.m = jcast('int', 0)
Code05_Knapsack.x = jcast('int', 0)
Code05_Knapsack.y = jcast('int', 0)

if __name__ == '__main__':
    Code05_Knapsack.main([])
