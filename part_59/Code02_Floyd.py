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

# Floyd算法模版（洛谷）
# 测试链接 : https://www.luogu.com.cn/problem/P2910
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Floyd:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'path': 'path', 'distance': 'distance', 'n': 'n', 'm': 'm', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    path = None
    distance = None
    n = 0
    m = 0
    ans = 0
    # 初始时设置任意两点之间的最短距离为无穷大，表示任何路不存在
    @staticmethod
    def build():
        i = jcast('int', 0)
        while (i < Code02_Floyd.n):
            j = jcast('int', 0)
            while (j < Code02_Floyd.n):
                jset(Code02_Floyd.distance[i], j, jget(Integer, 'MAX_VALUE'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_Floyd.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_Floyd.m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code02_Floyd.m):
                jcall(in_, 'nextToken')
                Code02_Floyd.path[i] = jcast('int', jcast('int', (jcast('int', jget(in_, 'nval')) - 1)))
                i = jcast('int', (i + 1))
            # 这道题给的图是邻接矩阵的形式
            # 任意两点之间的边权都会给定
            # 所以显得distance初始化不太必要
            # 但是一般情况下，distance初始化一定要做
            Code02_Floyd.build()
            i = jcast('int', 0)
            while (i < Code02_Floyd.n):
                j = jcast('int', 0)
                while (j < Code02_Floyd.n):
                    jcall(in_, 'nextToken')
                    jset(Code02_Floyd.distance[i], j, jcast('int', jget(in_, 'nval')))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            Code02_Floyd.floyd()
            Code02_Floyd.ans = jcast('int', 0)
            i = jcast('int', 1)
            while (i < Code02_Floyd.m):
                Code02_Floyd.ans = jcast('int', jcast('int', jadd(Code02_Floyd.ans, Code02_Floyd.distance[Code02_Floyd.path[jcast('int', (i - 1))]][Code02_Floyd.path[i]])))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code02_Floyd.ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def floyd():
        # O(N^3)的过程
        # 枚举每个跳板
        # 注意，跳板要最先枚举！跳板要最先枚举！跳板要最先枚举！
        # 跳板
        bridge = jcast('int', 0)
        while (bridge < Code02_Floyd.n):
            i = jcast('int', 0)
            while (i < Code02_Floyd.n):
                j = jcast('int', 0)
                while (j < Code02_Floyd.n):
                    # i -> .....bridge .... -> j
                    # distance[i][j]能不能缩短
                    # distance[i][j] = min ( distance[i][j] , distance[i][bridge] + distance[bridge][j])
                    if (((Code02_Floyd.distance[i][bridge] != jget(Integer, 'MAX_VALUE')) and (Code02_Floyd.distance[bridge][j] != jget(Integer, 'MAX_VALUE'))) and (Code02_Floyd.distance[i][j] > jcast('int', jadd(Code02_Floyd.distance[i][bridge], Code02_Floyd.distance[bridge][j])))):
                        jset(Code02_Floyd.distance[i], j, jcast('int', jadd(Code02_Floyd.distance[i][bridge], Code02_Floyd.distance[bridge][j])))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            bridge = jcast('int', (bridge + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Floyd.MAXN = jcast('int', 101)
Code02_Floyd.MAXM = jcast('int', 10001)
Code02_Floyd.path = jarray('int', [Code02_Floyd.MAXM])
Code02_Floyd.distance = jarray('int', [Code02_Floyd.MAXN, Code02_Floyd.MAXN])
Code02_Floyd.n = jcast('int', 0)
Code02_Floyd.m = jcast('int', 0)
Code02_Floyd.ans = jcast('int', 0)

if __name__ == '__main__':
    Code02_Floyd.main([])
