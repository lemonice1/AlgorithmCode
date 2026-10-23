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

# 跑路
# 一共有n个节点，编号1~n，一共有m条有向边，每条边1公里
# 有一个空间跑路器，每秒你都可以直接移动2^k公里，每秒钟可以随意决定k的值
# 题目保证1到n之间一定可以到达，返回1到n最少用几秒
# 2 <= n <= 50
# m <= 10^4
# k <= 64
# 测试链接 : https://www.luogu.com.cn/problem/P1613
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_RanAway:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'NA': 'NA', 'st': 'st', 'time': 'time', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXP = 0
    NA = 0
    # st[i][j][p] : i到j的距离是不是2^p
    st = None
    # time[i][j] : i到j的最短时间
    time = None
    n = 0
    m = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code02_RanAway.n):
            j = jcast('int', 1)
            while (j <= Code02_RanAway.n):
                jset(Code02_RanAway.st[i][j], 0, False)
                jset(Code02_RanAway.time[i], j, Code02_RanAway.NA)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_RanAway.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_RanAway.build()
        jcall(in_, 'nextToken')
        Code02_RanAway.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code02_RanAway.m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jset(Code02_RanAway.st[u][v], 0, True)
            jset(Code02_RanAway.time[u], v, 1)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code02_RanAway.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 需要先掌握，讲解065 - Floyd算法
    @staticmethod
    def compute():
        # 先枚举次方
        # 再枚举跳板
        # 最后枚举每一组(i,j)
        p = jcast('int', 1)
        while (p <= Code02_RanAway.MAXP):
            jump = jcast('int', 1)
            while (jump <= Code02_RanAway.n):
                i = jcast('int', 1)
                while (i <= Code02_RanAway.n):
                    j = jcast('int', 1)
                    while (j <= Code02_RanAway.n):
                        if (Code02_RanAway.st[i][jump][jcast('int', (p - 1))] and Code02_RanAway.st[jump][j][jcast('int', (p - 1))]):
                            jset(Code02_RanAway.st[i][j], p, True)
                            jset(Code02_RanAway.time[i], j, 1)
                        j = jcast('int', (j + 1))
                    i = jcast('int', (i + 1))
                jump = jcast('int', (jump + 1))
            p = jcast('int', (p + 1))
        if (Code02_RanAway.time[1][Code02_RanAway.n] != 1):
            # 先枚举跳板
            # 最后枚举每一组(i,j)
            jump = jcast('int', 1)
            while (jump <= Code02_RanAway.n):
                i = jcast('int', 1)
                while (i <= Code02_RanAway.n):
                    j = jcast('int', 1)
                    while (j <= Code02_RanAway.n):
                        if ((Code02_RanAway.time[i][jump] != Code02_RanAway.NA) and (Code02_RanAway.time[jump][j] != Code02_RanAway.NA)):
                            jset(Code02_RanAway.time[i], j, jstatic('Math', 'min', Code02_RanAway.time[i][j], jcast('int', jadd(Code02_RanAway.time[i][jump], Code02_RanAway.time[jump][j]))))
                        j = jcast('int', (j + 1))
                    i = jcast('int', (i + 1))
                jump = jcast('int', (jump + 1))
        return jcast('int', Code02_RanAway.time[1][Code02_RanAway.n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_RanAway.MAXN = jcast('int', 61)
Code02_RanAway.MAXP = jcast('int', 64)
Code02_RanAway.NA = jcast('int', jget(Integer, 'MAX_VALUE'))
Code02_RanAway.st = jarray('boolean', [Code02_RanAway.MAXN, Code02_RanAway.MAXN, jcast('int', jadd(Code02_RanAway.MAXP, 1))])
Code02_RanAway.time = jarray('int', [Code02_RanAway.MAXN, Code02_RanAway.MAXN])
Code02_RanAway.n = jcast('int', 0)
Code02_RanAway.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_RanAway.main([])
