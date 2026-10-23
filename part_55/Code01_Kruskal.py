# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Kruskal算法模版（洛谷）
# 静态空间实现
# 测试链接 : https://www.luogu.com.cn/problem/P3366
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 时间复杂度O(m * log m) + O(n + m)
class Code01_Kruskal:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'father': 'father', 'edges': 'edges', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    father = None
    # u, v, w
    edges = None
    n = 0
    m = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code01_Kruskal.n):
            Code01_Kruskal.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code01_Kruskal.father[i]):
            jset(Code01_Kruskal.father, i, Code01_Kruskal.find(Code01_Kruskal.father[i]))
        return jcast('int', Code01_Kruskal.father[i])

    # 如果x和y本来就是一个集合，返回false
    # 如果x和y不是一个集合，合并之后返回true
    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code01_Kruskal.find(x))
        fy = jcast('int', Code01_Kruskal.find(y))
        if (fx != fy):
            Code01_Kruskal.father[fx] = jcast('int', fy)
            return jcast('boolean', True)
        else:
            return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_Kruskal.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_Kruskal.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_Kruskal.build()
            i = jcast('int', 0)
            while (i < Code01_Kruskal.m):
                jcall(in_, 'nextToken')
                jset(Code01_Kruskal.edges[i], 0, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code01_Kruskal.edges[i], 1, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code01_Kruskal.edges[i], 2, jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'sort', Code01_Kruskal.edges, 0, Code01_Kruskal.m, (lambda a, b: (a[2] - b[2])))
            ans = jcast('int', 0)
            edgeCnt = jcast('int', 0)
            for edge in Code01_Kruskal.edges:
                if Code01_Kruskal.union(edge[0], edge[1]):
                    edgeCnt = jcast('int', (edgeCnt + 1))
                    ans = jcast('int', jcast('int', jadd(ans, edge[2])))
            jcall(out, 'println', (ans if (edgeCnt == jcast('int', (Code01_Kruskal.n - 1))) else 'orz'))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Kruskal.MAXN = jcast('int', 5001)
Code01_Kruskal.MAXM = jcast('int', 200001)
Code01_Kruskal.father = jarray('int', [Code01_Kruskal.MAXN])
Code01_Kruskal.edges = jarray('int', [Code01_Kruskal.MAXM, 3])
Code01_Kruskal.n = jcast('int', 0)
Code01_Kruskal.m = jcast('int', 0)

if __name__ == '__main__':
    Code01_Kruskal.main([])
