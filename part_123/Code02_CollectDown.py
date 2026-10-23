# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 向下收集获得最大能量
# 有一个n * m的区域，行和列的编号从1开始
# 每个能量点用(i, j, v)表示，i行j列上有价值为v的能量点
# 一共有k个能量点，并且所有能量点一定在不同的位置
# 一开始可以在第1行的任意位置，然后每一步必须向下移动
# 向下去往哪个格子是一个范围，如果当前在(i, j)位置
# 那么往下可以选择(i+1, j-t)...(i+1, j+t)其中的一个格子
# 到达最后一行时，收集过程停止，返回能收集到的最大能量价值
# 1 <= n、m、k、t <= 4000
# 1 <= v <= 100
# 测试链接 : https://www.luogu.com.cn/problem/P3800
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_CollectDown:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'dp': 'dp', 'queue': 'queue', 'l': 'l', 'r': 'r', 'n': 'n', 'm': 'm', 'k': 'k', 't': 't'}
    MAXN = 0
    MAXM = 0
    dp = None
    queue = None
    l = 0
    r = 0
    n = 0
    m = 0
    k = 0
    t = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code02_CollectDown.n):
            j = jcast('int', 1)
            while (j <= Code02_CollectDown.m):
                jset(Code02_CollectDown.dp[i], j, 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_CollectDown.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_CollectDown.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_CollectDown.k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_CollectDown.t = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_CollectDown.build()
        i = jcast('int', 1)
        r = 0
        c = 0
        v = 0
        while (i <= Code02_CollectDown.k):
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            c = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jset(Code02_CollectDown.dp[r], c, v)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code02_CollectDown.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 2)
        while (i <= Code02_CollectDown.n):
            Code02_CollectDown.l = jcast('int', jset(Code02_CollectDown, 'r', 0))
            j = jcast('int', 1)
            while (j <= Code02_CollectDown.t):
                Code02_CollectDown.add(jcast('int', (i - 1)), j)
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j <= Code02_CollectDown.m):
                Code02_CollectDown.add(jcast('int', (i - 1)), jcast('int', jadd(j, Code02_CollectDown.t)))
                Code02_CollectDown.overdue(jcast('int', (jcast('int', (j - Code02_CollectDown.t)) - 1)))
                ((_java_obj_1 := Code02_CollectDown.dp[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), Code02_CollectDown.dp[jcast('int', (i - 1))][Code02_CollectDown.queue[Code02_CollectDown.l]]))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        j = jcast('int', 1)
        while (j <= Code02_CollectDown.m):
            ans = jcast('int', jstatic('Math', 'max', ans, Code02_CollectDown.dp[Code02_CollectDown.n][j]))
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    @staticmethod
    def add(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if (j <= Code02_CollectDown.m):
            while ((Code02_CollectDown.l < Code02_CollectDown.r) and (Code02_CollectDown.dp[i][Code02_CollectDown.queue[jcast('int', (Code02_CollectDown.r - 1))]] <= Code02_CollectDown.dp[i][j])):
                Code02_CollectDown.r = jcast('int', (Code02_CollectDown.r - 1))
            jset(Code02_CollectDown.queue, ((_java_obj_3 := Code02_CollectDown), (_java_key_4 := 'r'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))), _java_old_5)[4], j)

    @staticmethod
    def overdue(t):
        t = jcast('int', t)
        if ((Code02_CollectDown.l < Code02_CollectDown.r) and (Code02_CollectDown.queue[Code02_CollectDown.l] == t)):
            Code02_CollectDown.l = jcast('int', (Code02_CollectDown.l + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CollectDown.MAXN = jcast('int', 4001)
Code02_CollectDown.MAXM = jcast('int', 4001)
Code02_CollectDown.dp = jarray('int', [Code02_CollectDown.MAXN, Code02_CollectDown.MAXM])
Code02_CollectDown.queue = jarray('int', [Code02_CollectDown.MAXM])
Code02_CollectDown.l = jcast('int', 0)
Code02_CollectDown.r = jcast('int', 0)
Code02_CollectDown.n = jcast('int', 0)
Code02_CollectDown.m = jcast('int', 0)
Code02_CollectDown.k = jcast('int', 0)
Code02_CollectDown.t = jcast('int', 0)

if __name__ == '__main__':
    Code02_CollectDown.main([])
