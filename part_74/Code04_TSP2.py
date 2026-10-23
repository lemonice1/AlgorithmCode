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
# 卡空间是吧？绕一下！
class Code04_TSP2:
    __java_fields__ = {'MAXN': 'MAXN', 'start': 'start', 'back': 'back', 'graph': 'graph', 'dp': 'dp', 'n': 'n'}
    MAXN = 0
    start = None
    back = None
    # 这个图中，其实是不算起始村的，其他村庄彼此到达的路径长度
    graph = None
    # 不算起始村庄的
    dp = None
    n = 0
    @staticmethod
    def build():
        s = jcast('int', 0)
        while (s < jcast('int', (1 << (Code04_TSP2.n & 31)))):
            i = jcast('int', 0)
            while (i < Code04_TSP2.n):
                jset(Code04_TSP2.dp[s], i, jcast('int', (-1)))
                i = jcast('int', (i + 1))
            s = jcast('int', (s + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_TSP2.n = jcast('int', jcast('int', (jcast('int', jget(in_, 'nval')) - 1)))
            Code04_TSP2.build()
            jcall(in_, 'nextToken')
            i = jcast('int', 0)
            while (i < Code04_TSP2.n):
                jcall(in_, 'nextToken')
                Code04_TSP2.start[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            i = jcast('int', 0)
            while (i < Code04_TSP2.n):
                jcall(in_, 'nextToken')
                Code04_TSP2.back[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                j = jcast('int', 0)
                while (j < Code04_TSP2.n):
                    jcall(in_, 'nextToken')
                    jset(Code04_TSP2.graph[i], j, jcast('int', jget(in_, 'nval')))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_TSP2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        # 起始村无编号
        i = jcast('int', 0)
        while (i < Code04_TSP2.n):
            # 起始村 -> i号村  +  i号村出发所有村子都走最终回到起始村
            ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code04_TSP2.start[i], Code04_TSP2.f(jcast('int', (1 << (i & 31))), i)))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # s : 不包含起始村的
    @staticmethod
    def f(s, i):
        s = jcast('int', s)
        i = jcast('int', i)
        if (s == jcast('int', (jcast('int', (1 << (Code04_TSP2.n & 31))) - 1))):
            return jcast('int', Code04_TSP2.back[i])
        if (Code04_TSP2.dp[s][i] != jcast('int', (-1))):
            return jcast('int', Code04_TSP2.dp[s][i])
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        j = jcast('int', 0)
        while (j < Code04_TSP2.n):
            if (jcast('int', (s & jcast('int', (1 << (j & 31))))) == 0):
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code04_TSP2.graph[i][j], Code04_TSP2.f(jcast('int', (s | jcast('int', (1 << (j & 31))))), j)))))
            j = jcast('int', (j + 1))
        jset(Code04_TSP2.dp[s], i, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_TSP2.MAXN = jcast('int', 19)
Code04_TSP2.start = jarray('int', [Code04_TSP2.MAXN])
Code04_TSP2.back = jarray('int', [Code04_TSP2.MAXN])
Code04_TSP2.graph = jarray('int', [Code04_TSP2.MAXN, Code04_TSP2.MAXN])
Code04_TSP2.dp = jarray('int', [jcast('int', (1 << (Code04_TSP2.MAXN & 31))), Code04_TSP2.MAXN])
Code04_TSP2.n = jcast('int', 0)

if __name__ == '__main__':
    Code04_TSP2.main([])
