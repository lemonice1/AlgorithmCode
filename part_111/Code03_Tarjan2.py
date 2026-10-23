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

# tarjan算法解法迭代版
# 测试链接 : https://www.luogu.com.cn/problem/P3379
# 所有递归函数一律改成等义的迭代版
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Tarjan2:
    __java_fields__ = {'MAXN': 'MAXN', 'headEdge': 'headEdge', 'edgeNext': 'edgeNext', 'edgeTo': 'edgeTo', 'tcnt': 'tcnt', 'headQuery': 'headQuery', 'queryNext': 'queryNext', 'queryTo': 'queryTo', 'queryIndex': 'queryIndex', 'qcnt': 'qcnt', 'visited': 'visited', 'father': 'father', 'ans': 'ans', 'stack': 'stack', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    headEdge = None
    edgeNext = None
    edgeTo = None
    tcnt = 0
    headQuery = None
    queryNext = None
    queryTo = None
    queryIndex = None
    qcnt = 0
    visited = None
    father = None
    ans = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code03_Tarjan2.tcnt = jcast('int', jset(Code03_Tarjan2, 'qcnt', 1))
        jstatic('Arrays', 'fill', Code03_Tarjan2.headEdge, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_Tarjan2.headQuery, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_Tarjan2.visited, 1, jcast('int', jadd(n, 1)), False)
        i = jcast('int', 1)
        while (i <= n):
            Code03_Tarjan2.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code03_Tarjan2.edgeNext[Code03_Tarjan2.tcnt] = jcast('int', Code03_Tarjan2.headEdge[u])
        Code03_Tarjan2.edgeTo[Code03_Tarjan2.tcnt] = jcast('int', v)
        jset(Code03_Tarjan2.headEdge, u, ((_java_obj_1 := Code03_Tarjan2), (_java_key_2 := 'tcnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def addQuery(u, v, i):
        u = jcast('int', u)
        v = jcast('int', v)
        i = jcast('int', i)
        Code03_Tarjan2.queryNext[Code03_Tarjan2.qcnt] = jcast('int', Code03_Tarjan2.headQuery[u])
        Code03_Tarjan2.queryTo[Code03_Tarjan2.qcnt] = jcast('int', v)
        Code03_Tarjan2.queryIndex[Code03_Tarjan2.qcnt] = jcast('int', i)
        jset(Code03_Tarjan2.headQuery, u, ((_java_obj_4 := Code03_Tarjan2), (_java_key_5 := 'qcnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])

    # 为了实现迭代版而准备的栈
    stack = None
    # 并查集找头节点迭代版
    @staticmethod
    def find(i):
        i = jcast('int', i)
        size = jcast('int', 0)
        while (i != Code03_Tarjan2.father[i]):
            jset(Code03_Tarjan2.stack, ((_java_old_7 := size), (size := jcast('int', (size + (1)))), _java_old_7)[2], i)
            i = jcast('int', Code03_Tarjan2.father[i])
        while (size > 0):
            jset(Code03_Tarjan2.father, Code03_Tarjan2.stack[(size := jcast('int', (size + (-1))))], i)
        return jcast('int', i)

    # 为了实现迭代版而准备的栈
    ufe = None
    stackSize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code03_Tarjan2.ufe[Code03_Tarjan2.stackSize], 0, u)
        jset(Code03_Tarjan2.ufe[Code03_Tarjan2.stackSize], 1, f)
        jset(Code03_Tarjan2.ufe[Code03_Tarjan2.stackSize], 2, e)
        Code03_Tarjan2.stackSize = jcast('int', (Code03_Tarjan2.stackSize + 1))

    @staticmethod
    def pop():
        Code03_Tarjan2.stackSize = jcast('int', (Code03_Tarjan2.stackSize - 1))
        Code03_Tarjan2.u = jcast('int', Code03_Tarjan2.ufe[Code03_Tarjan2.stackSize][0])
        Code03_Tarjan2.f = jcast('int', Code03_Tarjan2.ufe[Code03_Tarjan2.stackSize][1])
        Code03_Tarjan2.e = jcast('int', Code03_Tarjan2.ufe[Code03_Tarjan2.stackSize][2])

    # 为了容易改成迭代版，修改一下递归版
    @staticmethod
    def _java_tarjan_0(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_Tarjan2.visited[u] = jcast('boolean', True)
        e = jcast('int', Code03_Tarjan2.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_Tarjan2.edgeTo[e])
            if (v != f):
                Code03_Tarjan2._java_tarjan_0(v, u)
                # 注意这里，注释了一行
                # father[v] = u;
            e = jcast('int', Code03_Tarjan2.edgeNext[e])
        e = jcast('int', Code03_Tarjan2.headQuery[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_Tarjan2.queryTo[e])
            if Code03_Tarjan2.visited[v]:
                jset(Code03_Tarjan2.ans, Code03_Tarjan2.queryIndex[e], Code03_Tarjan2.find(v))
            e = jcast('int', Code03_Tarjan2.queryNext[e])
        # 注意这里，增加了一行
        Code03_Tarjan2.father[u] = jcast('int', f)

    # tarjan算法迭代版，根据上面的递归版改写
    @staticmethod
    def _java_tarjan_1(root):
        root = jcast('int', root)
        Code03_Tarjan2.stackSize = jcast('int', 0)
        # 栈里存放三个信息
        # u : 当前处理的点
        # f : 当前点u的父节点
        # e : 处理到几号边了
        # 如果e==-1，表示之前没有处理过u的任何边
        # 如果e==0，表示u的边都已经处理完了
        Code03_Tarjan2.push(root, 0, jcast('int', (-1)))
        while (Code03_Tarjan2.stackSize > 0):
            Code03_Tarjan2.pop()
            if (Code03_Tarjan2.e == jcast('int', (-1))):
                Code03_Tarjan2.visited[Code03_Tarjan2.u] = jcast('boolean', True)
                Code03_Tarjan2.e = jcast('int', Code03_Tarjan2.headEdge[Code03_Tarjan2.u])
            else:
                Code03_Tarjan2.e = jcast('int', Code03_Tarjan2.edgeNext[Code03_Tarjan2.e])
            if (Code03_Tarjan2.e != 0):
                Code03_Tarjan2.push(Code03_Tarjan2.u, Code03_Tarjan2.f, Code03_Tarjan2.e)
                if (Code03_Tarjan2.edgeTo[Code03_Tarjan2.e] != Code03_Tarjan2.f):
                    Code03_Tarjan2.push(Code03_Tarjan2.edgeTo[Code03_Tarjan2.e], Code03_Tarjan2.u, jcast('int', (-1)))
            else:
                # e == 0代表u后续已经没有边需要处理了
                q = jcast('int', Code03_Tarjan2.headQuery[Code03_Tarjan2.u])
                v = 0
                while (q != 0):
                    v = jcast('int', Code03_Tarjan2.queryTo[q])
                    if Code03_Tarjan2.visited[v]:
                        jset(Code03_Tarjan2.ans, Code03_Tarjan2.queryIndex[q], Code03_Tarjan2.find(v))
                    q = jcast('int', Code03_Tarjan2.queryNext[q])
                Code03_Tarjan2.father[Code03_Tarjan2.u] = jcast('int', Code03_Tarjan2.f)

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
        Code03_Tarjan2.build(n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_Tarjan2.addEdge(u, v)
            Code03_Tarjan2.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_Tarjan2.addQuery(u, v, i)
            Code03_Tarjan2.addQuery(v, u, i)
            i = jcast('int', (i + 1))
        Code03_Tarjan2._java_tarjan_1(root)
        i = jcast('int', 1)
        while (i <= m):
            jcall(out, 'println', Code03_Tarjan2.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def tarjan(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code03_Tarjan2._java_tarjan_0(*args)
        if _java_choice == 1:
            return Code03_Tarjan2._java_tarjan_1(*args)
        raise TypeError("No matching overload for Code03_Tarjan2.tarjan")


Code03_Tarjan2.MAXN = jcast('int', 500001)
Code03_Tarjan2.headEdge = jarray('int', [Code03_Tarjan2.MAXN])
Code03_Tarjan2.edgeNext = jarray('int', [jcast('int', (Code03_Tarjan2.MAXN << (1 & 31)))])
Code03_Tarjan2.edgeTo = jarray('int', [jcast('int', (Code03_Tarjan2.MAXN << (1 & 31)))])
Code03_Tarjan2.tcnt = jcast('int', 0)
Code03_Tarjan2.headQuery = jarray('int', [Code03_Tarjan2.MAXN])
Code03_Tarjan2.queryNext = jarray('int', [jcast('int', (Code03_Tarjan2.MAXN << (1 & 31)))])
Code03_Tarjan2.queryTo = jarray('int', [jcast('int', (Code03_Tarjan2.MAXN << (1 & 31)))])
Code03_Tarjan2.queryIndex = jarray('int', [jcast('int', (Code03_Tarjan2.MAXN << (1 & 31)))])
Code03_Tarjan2.qcnt = jcast('int', 0)
Code03_Tarjan2.visited = jarray('boolean', [Code03_Tarjan2.MAXN])
Code03_Tarjan2.father = jarray('int', [Code03_Tarjan2.MAXN])
Code03_Tarjan2.ans = jarray('int', [Code03_Tarjan2.MAXN])
Code03_Tarjan2.stack = jarray('int', [Code03_Tarjan2.MAXN])
Code03_Tarjan2.ufe = jarray('int', [Code03_Tarjan2.MAXN, 3])
Code03_Tarjan2.stackSize = jcast('int', 0)
Code03_Tarjan2.u = jcast('int', 0)
Code03_Tarjan2.f = jcast('int', 0)
Code03_Tarjan2.e = jcast('int', 0)

if __name__ == '__main__':
    Code03_Tarjan2.main([])
