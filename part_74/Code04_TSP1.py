# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 售货员的难题 - TSP问题
# 某乡有n个村庄(1<=n<=20)，有一个售货员，他要到各个村庄去售货
# 各村庄之间的路程s(1<=s<=1000)是已知的
# 且A村到B村的路程，与B到A的路大多不同(有向带权图)
# 为了提高效率，他从商店出发到每个村庄一次，然后返回商店所在的村，
# 假设商店所在的村庄为1
# 他不知道选择什么样的路线才能使所走的路程最短
# 请你帮他选择一条最短的路
# 测试链接 : https://www.luogu.com.cn/problem/P1171
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# MAXN 需覆盖最大输入规模；状态数随节点数量指数增长
# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 但如果把MAXN改成19，会有一个测试用例通过不了
# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 下面继续减少状态存储和常数开销
# 另一种实现可参考 Code04_TSP2.py
class Code04_TSP1:
    __java_fields__ = {'MAXN': 'MAXN', 'graph': 'graph', 'dp': 'dp', 'n': 'n'}
    MAXN = 0
    graph = None
    dp = None
    n = 0
    @staticmethod
    def build():
        s = jcast('int', 0)
        while (s < jcast('int', (1 << (Code04_TSP1.n & 31)))):
            i = jcast('int', 0)
            while (i < Code04_TSP1.n):
                jset(Code04_TSP1.dp[s], i, jcast('int', (-1)))
                i = jcast('int', (i + 1))
            s = jcast('int', (s + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_TSP1.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_TSP1.build()
            i = jcast('int', 0)
            while (i < Code04_TSP1.n):
                j = jcast('int', 0)
                while (j < Code04_TSP1.n):
                    jcall(in_, 'nextToken')
                    jset(Code04_TSP1.graph[i], j, jcast('int', jget(in_, 'nval')))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_TSP1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        return jcast('int', Code04_TSP1.f(1, 0))

    # s : 村里走没走过的状态，1走过了不要再走了，0可以走
    # i : 目前在哪个村
    @staticmethod
    def f(s, i):
        s = jcast('int', s)
        i = jcast('int', i)
        if (s == jcast('int', (jcast('int', (1 << (Code04_TSP1.n & 31))) - 1))):
            # n : 000011111
            return jcast('int', Code04_TSP1.graph[i][0])
        if (Code04_TSP1.dp[s][i] != jcast('int', (-1))):
            return jcast('int', Code04_TSP1.dp[s][i])
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        j = jcast('int', 0)
        while (j < Code04_TSP1.n):
            # 0...n-1这些村，都看看是不是下一个落脚点
            if (jcast('int', (s & jcast('int', (1 << (j & 31))))) == 0):
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code04_TSP1.graph[i][j], Code04_TSP1.f(jcast('int', (s | jcast('int', (1 << (j & 31))))), j)))))
            j = jcast('int', (j + 1))
        jset(Code04_TSP1.dp[s], i, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_TSP1.MAXN = jcast('int', 19)
Code04_TSP1.graph = jarray('int', [Code04_TSP1.MAXN, Code04_TSP1.MAXN])
Code04_TSP1.dp = jarray('int', [jcast('int', (1 << (Code04_TSP1.MAXN & 31))), Code04_TSP1.MAXN])
Code04_TSP1.n = jcast('int', 0)

if __name__ == '__main__':
    Code04_TSP1.main([])
