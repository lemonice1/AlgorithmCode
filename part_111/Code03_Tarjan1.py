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

# tarjan算法解法
# 测试链接 : https://www.luogu.com.cn/problem/P3379
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code03_Tarjan2.py
class Code03_Tarjan1:
    __java_fields__ = {'MAXN': 'MAXN', 'headEdge': 'headEdge', 'edgeNext': 'edgeNext', 'edgeTo': 'edgeTo', 'tcnt': 'tcnt', 'headQuery': 'headQuery', 'queryNext': 'queryNext', 'queryTo': 'queryTo', 'queryIndex': 'queryIndex', 'qcnt': 'qcnt', 'visited': 'visited', 'father': 'father', 'ans': 'ans'}
    MAXN = 0
    # 链式前向星建图
    headEdge = None
    edgeNext = None
    edgeTo = None
    tcnt = 0
    # 每个节点有哪些查询，也用链式前向星方式存储
    headQuery = None
    queryNext = None
    queryTo = None
    # 问题的编号，一旦有答案可以知道填写在哪
    queryIndex = None
    qcnt = 0
    # 某个节点是否访问过
    visited = None
    # 并查集
    father = None
    # 收集的答案
    ans = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code03_Tarjan1.tcnt = jcast('int', jset(Code03_Tarjan1, 'qcnt', 1))
        jstatic('Arrays', 'fill', Code03_Tarjan1.headEdge, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_Tarjan1.headQuery, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_Tarjan1.visited, 1, jcast('int', jadd(n, 1)), False)
        i = jcast('int', 1)
        while (i <= n):
            Code03_Tarjan1.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code03_Tarjan1.edgeNext[Code03_Tarjan1.tcnt] = jcast('int', Code03_Tarjan1.headEdge[u])
        Code03_Tarjan1.edgeTo[Code03_Tarjan1.tcnt] = jcast('int', v)
        jset(Code03_Tarjan1.headEdge, u, ((_java_obj_1 := Code03_Tarjan1), (_java_key_2 := 'tcnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def addQuery(u, v, i):
        u = jcast('int', u)
        v = jcast('int', v)
        i = jcast('int', i)
        Code03_Tarjan1.queryNext[Code03_Tarjan1.qcnt] = jcast('int', Code03_Tarjan1.headQuery[u])
        Code03_Tarjan1.queryTo[Code03_Tarjan1.qcnt] = jcast('int', v)
        Code03_Tarjan1.queryIndex[Code03_Tarjan1.qcnt] = jcast('int', i)
        jset(Code03_Tarjan1.headQuery, u, ((_java_obj_4 := Code03_Tarjan1), (_java_key_5 := 'qcnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])

    # 并查集找头节点递归版
    # 一般来说都这么写，但是本题附加的测试数据很毒
    # 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_Tarjan1.father[i]):
            jset(Code03_Tarjan1.father, i, Code03_Tarjan1.find(Code03_Tarjan1.father[i]))
        return jcast('int', Code03_Tarjan1.father[i])

    # tarjan算法递归版
    # 一般来说都这么写，但是本题附加的测试数据很毒
    # 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def tarjan(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_Tarjan1.visited[u] = jcast('boolean', True)
        e = jcast('int', Code03_Tarjan1.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_Tarjan1.edgeTo[e])
            if (v != f):
                Code03_Tarjan1.tarjan(v, u)
                Code03_Tarjan1.father[v] = jcast('int', u)
            e = jcast('int', Code03_Tarjan1.edgeNext[e])
        e = jcast('int', Code03_Tarjan1.headQuery[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_Tarjan1.queryTo[e])
            if Code03_Tarjan1.visited[v]:
                jset(Code03_Tarjan1.ans, Code03_Tarjan1.queryIndex[e], Code03_Tarjan1.find(v))
            e = jcast('int', Code03_Tarjan1.queryNext[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        root = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_Tarjan1.build(n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_Tarjan1.addEdge(u, v)
            Code03_Tarjan1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_Tarjan1.addQuery(u, v, i)
            Code03_Tarjan1.addQuery(v, u, i)
            i = jcast('int', (i + 1))
        Code03_Tarjan1.tarjan(root, 0)
        i = jcast('int', 1)
        while (i <= m):
            jcall(out, 'println', Code03_Tarjan1.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Tarjan1.MAXN = jcast('int', 500001)
Code03_Tarjan1.headEdge = jarray('int', [Code03_Tarjan1.MAXN])
Code03_Tarjan1.edgeNext = jarray('int', [jcast('int', (Code03_Tarjan1.MAXN << (1 & 31)))])
Code03_Tarjan1.edgeTo = jarray('int', [jcast('int', (Code03_Tarjan1.MAXN << (1 & 31)))])
Code03_Tarjan1.tcnt = jcast('int', 0)
Code03_Tarjan1.headQuery = jarray('int', [Code03_Tarjan1.MAXN])
Code03_Tarjan1.queryNext = jarray('int', [jcast('int', (Code03_Tarjan1.MAXN << (1 & 31)))])
Code03_Tarjan1.queryTo = jarray('int', [jcast('int', (Code03_Tarjan1.MAXN << (1 & 31)))])
Code03_Tarjan1.queryIndex = jarray('int', [jcast('int', (Code03_Tarjan1.MAXN << (1 & 31)))])
Code03_Tarjan1.qcnt = jcast('int', 0)
Code03_Tarjan1.visited = jarray('boolean', [Code03_Tarjan1.MAXN])
Code03_Tarjan1.father = jarray('int', [Code03_Tarjan1.MAXN])
Code03_Tarjan1.ans = jarray('int', [Code03_Tarjan1.MAXN])

if __name__ == '__main__':
    Code03_Tarjan1.main([])
