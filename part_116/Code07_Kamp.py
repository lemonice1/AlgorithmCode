# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 聚会后送每个人回家最短用时
# 给定一棵n个点的树，边权代表走过边需要花费的时间
# 给定k个人分别在树上的哪些节点
# 这k个人选择了一个聚会点，所有的人都去往聚会点进行聚会
# 聚会结束后，所有人都会上一辆车，车会把每个人送回家
# 送完最后一个乘客，车不需要回到聚会点
# 如果聚会点在i，请问从聚会地点出发直到送最后一个人回家，最短用时多少
# i = 1 ~ n，打印所有的答案
# 测试链接 : https://www.luogu.com.cn/problem/P6419
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Kamp:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'people': 'people', 'incost': 'incost', 'inner1': 'inner1', 'inner2': 'inner2', 'choose': 'choose', 'outcost': 'outcost', 'outer': 'outer'}
    MAXN = 0
    n = 0
    k = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # people[i]: i内部，有多少乘客要送
    people = None
    # incost[i]: i内部，从i出发送完所有乘客回到i的最少代价
    incost = None
    # inner1[i]: i内部，从i出发送乘客的最长链
    inner1 = None
    # inner2[i]: i内部，从i出发送乘客的次长链
    inner2 = None
    # 注意 : inner1[i]和inner2[i]所代表的链，一定要来自i的不同儿子
    # choose[i]: 送乘客的最长链来自i的哪个儿子
    choose = None
    # outcost[i]: i外部，从i出发送完所有乘客回到i的最少代价
    outcost = None
    # outer[i]: i外部，从i出发送乘客的最长链
    outer = None
    @staticmethod
    def build():
        Code07_Kamp.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code07_Kamp.head, 1, jcast('int', jadd(Code07_Kamp.n, 1)), 0)
        jstatic('Arrays', 'fill', Code07_Kamp.people, 1, jcast('int', jadd(Code07_Kamp.n, 1)), 0)
        jstatic('Arrays', 'fill', Code07_Kamp.incost, 1, jcast('int', jadd(Code07_Kamp.n, 1)), 0)
        jstatic('Arrays', 'fill', Code07_Kamp.inner1, 1, jcast('int', jadd(Code07_Kamp.n, 1)), 0)
        jstatic('Arrays', 'fill', Code07_Kamp.inner2, 1, jcast('int', jadd(Code07_Kamp.n, 1)), 0)
        jstatic('Arrays', 'fill', Code07_Kamp.choose, 1, jcast('int', jadd(Code07_Kamp.n, 1)), 0)
        jstatic('Arrays', 'fill', Code07_Kamp.outcost, 1, jcast('int', jadd(Code07_Kamp.n, 1)), 0)
        jstatic('Arrays', 'fill', Code07_Kamp.outer, 1, jcast('int', jadd(Code07_Kamp.n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code07_Kamp.next[Code07_Kamp.cnt] = jcast('int', Code07_Kamp.head[u])
        Code07_Kamp.to[Code07_Kamp.cnt] = jcast('int', v)
        Code07_Kamp.weight[Code07_Kamp.cnt] = jcast('int', w)
        jset(Code07_Kamp.head, u, ((_java_obj_1 := Code07_Kamp), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code07_Kamp.head[u])
        v = 0
        w = 0
        while (e != 0):
            v = jcast('int', Code07_Kamp.to[e])
            w = jcast('int', Code07_Kamp.weight[e])
            if (v != f):
                Code07_Kamp.dfs1(v, u)
                Code07_Kamp.people[u] = jcast('int', jcast('int', jadd(Code07_Kamp.people[u], Code07_Kamp.people[v])))
                if (Code07_Kamp.people[v] > 0):
                    Code07_Kamp.incost[u] = jcast('long', jcast('long', jadd(Code07_Kamp.incost[u], jcast('long', jadd(Code07_Kamp.incost[v], jcast('long', (jcast('long', w) * 2)))))))
                    if (Code07_Kamp.inner1[u] < jcast('long', jadd(Code07_Kamp.inner1[v], w))):
                        Code07_Kamp.choose[u] = jcast('int', v)
                        Code07_Kamp.inner2[u] = jcast('long', Code07_Kamp.inner1[u])
                        Code07_Kamp.inner1[u] = jcast('long', jcast('long', jadd(Code07_Kamp.inner1[v], w)))
                    else:
                        if (Code07_Kamp.inner2[u] < jcast('long', jadd(Code07_Kamp.inner1[v], w))):
                            Code07_Kamp.inner2[u] = jcast('long', jcast('long', jadd(Code07_Kamp.inner1[v], w)))
            e = jcast('int', Code07_Kamp.next[e])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code07_Kamp.head[u])
        v = 0
        w = 0
        while (e != 0):
            v = jcast('int', Code07_Kamp.to[e])
            w = jcast('int', Code07_Kamp.weight[e])
            if (v != f):
                if (jcast('int', (Code07_Kamp.k - Code07_Kamp.people[v])) > 0):
                    if (Code07_Kamp.people[v] == 0):
                        Code07_Kamp.outcost[v] = jcast('long', jcast('long', jadd(jcast('long', jadd(Code07_Kamp.outcost[u], Code07_Kamp.incost[u])), jcast('long', (jcast('long', w) * 2)))))
                    else:
                        Code07_Kamp.outcost[v] = jcast('long', jcast('long', (jcast('long', jadd(Code07_Kamp.outcost[u], Code07_Kamp.incost[u])) - Code07_Kamp.incost[v])))
                    if (v != Code07_Kamp.choose[u]):
                        jset(Code07_Kamp.outer, v, jcast('long', jadd(jstatic('Math', 'max', Code07_Kamp.outer[u], Code07_Kamp.inner1[u]), w)))
                    else:
                        jset(Code07_Kamp.outer, v, jcast('long', jadd(jstatic('Math', 'max', Code07_Kamp.outer[u], Code07_Kamp.inner2[u]), w)))
                Code07_Kamp.dfs2(v, u)
            e = jcast('int', Code07_Kamp.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code07_Kamp.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code07_Kamp.build()
        jcall(in_, 'nextToken')
        Code07_Kamp.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code07_Kamp.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code07_Kamp.addEdge(u, v, w)
            Code07_Kamp.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        while (i <= Code07_Kamp.k):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            Code07_Kamp.people[u] = jcast('int', (Code07_Kamp.people[u] + 1))
            i = jcast('int', (i + 1))
        Code07_Kamp.dfs1(1, 0)
        Code07_Kamp.dfs2(1, 0)
        i = jcast('int', 1)
        while (i <= Code07_Kamp.n):
            jcall(out, 'println', jcast('long', (jcast('long', jadd(Code07_Kamp.incost[i], Code07_Kamp.outcost[i])) - jstatic('Math', 'max', Code07_Kamp.inner1[i], Code07_Kamp.outer[i]))))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Kamp.MAXN = jcast('int', 500001)
Code07_Kamp.n = jcast('int', 0)
Code07_Kamp.k = jcast('int', 0)
Code07_Kamp.head = jarray('int', [Code07_Kamp.MAXN])
Code07_Kamp.next = jarray('int', [jcast('int', (Code07_Kamp.MAXN << (1 & 31)))])
Code07_Kamp.to = jarray('int', [jcast('int', (Code07_Kamp.MAXN << (1 & 31)))])
Code07_Kamp.weight = jarray('int', [jcast('int', (Code07_Kamp.MAXN << (1 & 31)))])
Code07_Kamp.cnt = jcast('int', 0)
Code07_Kamp.people = jarray('int', [Code07_Kamp.MAXN])
Code07_Kamp.incost = jarray('long', [Code07_Kamp.MAXN])
Code07_Kamp.inner1 = jarray('long', [Code07_Kamp.MAXN])
Code07_Kamp.inner2 = jarray('long', [Code07_Kamp.MAXN])
Code07_Kamp.choose = jarray('int', [Code07_Kamp.MAXN])
Code07_Kamp.outcost = jarray('long', [Code07_Kamp.MAXN])
Code07_Kamp.outer = jarray('long', [Code07_Kamp.MAXN])

if __name__ == '__main__':
    Code07_Kamp.main([])
