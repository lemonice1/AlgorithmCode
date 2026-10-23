# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 繁忙的都市
# 一个非常繁忙的大都市，城市中的道路十分的拥挤，于是市长决定对其中的道路进行改造
# 城市的道路是这样分布的：城市中有n个交叉路口，有些交叉路口之间有道路相连
# 两个交叉路口之间最多有一条道路相连接，这些道路是双向的
# 且把所有的交叉路口直接或间接的连接起来了
# 每条道路都有一个分值，分值越小表示这个道路越繁忙，越需要进行改造
# 但是市政府的资金有限，市长希望进行改造的道路越少越好，于是他提出下面的要求：
# 1. 改造的那些道路能够把所有的交叉路口直接或间接的连通起来
# 2. 在满足要求1的情况下，改造的道路尽量少
# 3. 在满足要求1、2的情况下，改造的那些道路中分值最大的道路分值尽量小
# 作为市规划局的你，应当作出最佳的决策，选择哪些道路应当被修建
# 返回选出了几条道路 以及 分值最大的那条道路的分值是多少
# 测试链接 : https://www.luogu.com.cn/problem/P2330
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_BusyCities:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'father': 'father', 'edges': 'edges', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    father = None
    edges = None
    n = 0
    m = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code05_BusyCities.n):
            Code05_BusyCities.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code05_BusyCities.father[i]):
            jset(Code05_BusyCities.father, i, Code05_BusyCities.find(Code05_BusyCities.father[i]))
        return jcast('int', Code05_BusyCities.father[i])

    # 如果x和y本来就是一个集合，返回false
    # 如果x和y不是一个集合，合并之后返回true
    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code05_BusyCities.find(x))
        fy = jcast('int', Code05_BusyCities.find(y))
        if (fx != fy):
            Code05_BusyCities.father[fx] = jcast('int', fy)
            return jcast('boolean', True)
        else:
            return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            try:
                Code05_BusyCities.n = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code05_BusyCities.m = jcast('int', jcast('int', jget(in_, 'nval')))
                Code05_BusyCities.build()
                i = jcast('int', 0)
                while (i < Code05_BusyCities.m):
                    jcall(in_, 'nextToken')
                    jset(Code05_BusyCities.edges[i], 0, jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    jset(Code05_BusyCities.edges[i], 1, jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    jset(Code05_BusyCities.edges[i], 2, jcast('int', jget(in_, 'nval')))
                    i = jcast('int', (i + 1))
                jstatic('Arrays', 'sort', Code05_BusyCities.edges, 0, Code05_BusyCities.m, (lambda a, b: (a[2] - b[2])))
                ans = jcast('int', 0)
                edgeCnt = jcast('int', 0)
                for edge in Code05_BusyCities.edges:
                    try:
                        if Code05_BusyCities.union(edge[0], edge[1]):
                            edgeCnt = jcast('int', (edgeCnt + 1))
                            ans = jcast('int', jstatic('Math', 'max', ans, edge[2]))
                        if (edgeCnt == jcast('int', (Code05_BusyCities.n - 1))):
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                jcall(out, 'println', jadd(jadd(jcast('int', (Code05_BusyCities.n - 1)), ' '), ans))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_BusyCities.MAXN = jcast('int', 301)
Code05_BusyCities.MAXM = jcast('int', 8001)
Code05_BusyCities.father = jarray('int', [Code05_BusyCities.MAXN])
Code05_BusyCities.edges = jarray('int', [Code05_BusyCities.MAXM, 3])
Code05_BusyCities.n = jcast('int', 0)
Code05_BusyCities.m = jcast('int', 0)

if __name__ == '__main__':
    Code05_BusyCities.main([])
