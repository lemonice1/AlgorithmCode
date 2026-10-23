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

# 攻略，Python版
# 一共有n个节点，给定n-1条边，所有节点连成一棵树，每个点给定点权
# 规定1号点是头，任何路径都必须从头开始，然后走到某个叶节点停止
# 路径上的点，点权的累加和，叫做这个路径的收益
# 给定数字k，你可以随意选出k条路径，所有路径经过的点，需要取并集，也就是去重
# 并集中的点，点权的累加和，叫做k条路径的收益
# 打印k条路径的收益最大值
# 1 <= n、k <= 2 * 10^5
# 所有点权都是int类型的正数
# 测试链接 : https://www.luogu.com.cn/problem/P10641
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Walkthrough2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'fa': 'fa', 'son': 'son', 'top': 'top', 'money': 'money', 'sorted': 'sorted', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    n = 0
    k = 0
    arr = None
    # 链式前向星
    head = None
    next = None
    to = None
    cnt = 0
    # 长链剖分的改写，根据money的值来标记最值钱儿子
    fa = None
    son = None
    top = None
    money = None
    # 每条链的头节点收益排序
    sorted = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Walkthrough2.next, ((_java_obj_1 := Code05_Walkthrough2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Walkthrough2.head[u])
        Code05_Walkthrough2.to[Code05_Walkthrough2.cnt] = jcast('int', v)
        Code05_Walkthrough2.head[u] = jcast('int', Code05_Walkthrough2.cnt)

    # 递归版
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code05_Walkthrough2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_Walkthrough2.to[e])
            if (v != f):
                Code05_Walkthrough2.dfs1(v, u)
            e = jcast('int', Code05_Walkthrough2.next[e])
        e = jcast('int', Code05_Walkthrough2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_Walkthrough2.to[e])
            if (v != f):
                if ((Code05_Walkthrough2.son[u] == 0) or (Code05_Walkthrough2.money[Code05_Walkthrough2.son[u]] < Code05_Walkthrough2.money[v])):
                    Code05_Walkthrough2.son[u] = jcast('int', v)
            e = jcast('int', Code05_Walkthrough2.next[e])
        Code05_Walkthrough2.fa[u] = jcast('int', f)
        Code05_Walkthrough2.money[u] = jcast('long', jcast('long', jadd(Code05_Walkthrough2.money[Code05_Walkthrough2.son[u]], Code05_Walkthrough2.arr[u])))

    # 递归版
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code05_Walkthrough2.top[u] = jcast('int', t)
        if (Code05_Walkthrough2.son[u] == 0):
            return
        Code05_Walkthrough2.dfs2(Code05_Walkthrough2.son[u], t)
        e = jcast('int', Code05_Walkthrough2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_Walkthrough2.to[e])
            if ((v != Code05_Walkthrough2.fa[u]) and (v != Code05_Walkthrough2.son[u])):
                Code05_Walkthrough2.dfs2(v, v)
            e = jcast('int', Code05_Walkthrough2.next[e])

    fse = None
    stacksize = 0
    first = 0
    second = 0
    edge = 0
    @staticmethod
    def push(fir, sec, edg):
        fir = jcast('int', fir)
        sec = jcast('int', sec)
        edg = jcast('int', edg)
        jset(Code05_Walkthrough2.fse[Code05_Walkthrough2.stacksize], 0, fir)
        jset(Code05_Walkthrough2.fse[Code05_Walkthrough2.stacksize], 1, sec)
        jset(Code05_Walkthrough2.fse[Code05_Walkthrough2.stacksize], 2, edg)
        Code05_Walkthrough2.stacksize = jcast('int', (Code05_Walkthrough2.stacksize + 1))

    @staticmethod
    def pop():
        Code05_Walkthrough2.stacksize = jcast('int', (Code05_Walkthrough2.stacksize - 1))
        Code05_Walkthrough2.first = jcast('int', Code05_Walkthrough2.fse[Code05_Walkthrough2.stacksize][0])
        Code05_Walkthrough2.second = jcast('int', Code05_Walkthrough2.fse[Code05_Walkthrough2.stacksize][1])
        Code05_Walkthrough2.edge = jcast('int', Code05_Walkthrough2.fse[Code05_Walkthrough2.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code05_Walkthrough2.stacksize = jcast('int', 0)
        Code05_Walkthrough2.push(1, 0, jcast('int', (-1)))
        while (Code05_Walkthrough2.stacksize > 0):
            Code05_Walkthrough2.pop()
            if (Code05_Walkthrough2.edge == jcast('int', (-1))):
                Code05_Walkthrough2.edge = jcast('int', Code05_Walkthrough2.head[Code05_Walkthrough2.first])
            else:
                Code05_Walkthrough2.edge = jcast('int', Code05_Walkthrough2.next[Code05_Walkthrough2.edge])
            if (Code05_Walkthrough2.edge != 0):
                Code05_Walkthrough2.push(Code05_Walkthrough2.first, Code05_Walkthrough2.second, Code05_Walkthrough2.edge)
                if (Code05_Walkthrough2.to[Code05_Walkthrough2.edge] != Code05_Walkthrough2.second):
                    Code05_Walkthrough2.push(Code05_Walkthrough2.to[Code05_Walkthrough2.edge], Code05_Walkthrough2.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code05_Walkthrough2.head[Code05_Walkthrough2.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code05_Walkthrough2.to[e])
                    if (v != Code05_Walkthrough2.second):
                        if ((Code05_Walkthrough2.son[Code05_Walkthrough2.first] == 0) or (Code05_Walkthrough2.money[Code05_Walkthrough2.son[Code05_Walkthrough2.first]] < Code05_Walkthrough2.money[v])):
                            Code05_Walkthrough2.son[Code05_Walkthrough2.first] = jcast('int', v)
                    e = jcast('int', Code05_Walkthrough2.next[e])
                Code05_Walkthrough2.fa[Code05_Walkthrough2.first] = jcast('int', Code05_Walkthrough2.second)
                Code05_Walkthrough2.money[Code05_Walkthrough2.first] = jcast('long', jcast('long', jadd(Code05_Walkthrough2.money[Code05_Walkthrough2.son[Code05_Walkthrough2.first]], Code05_Walkthrough2.arr[Code05_Walkthrough2.first])))

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code05_Walkthrough2.stacksize = jcast('int', 0)
        Code05_Walkthrough2.push(1, 1, jcast('int', (-1)))
        while (Code05_Walkthrough2.stacksize > 0):
            try:
                Code05_Walkthrough2.pop()
                if (Code05_Walkthrough2.edge == jcast('int', (-1))):
                    Code05_Walkthrough2.top[Code05_Walkthrough2.first] = jcast('int', Code05_Walkthrough2.second)
                    if (Code05_Walkthrough2.son[Code05_Walkthrough2.first] == 0):
                        raise JContinue(None)
                    Code05_Walkthrough2.push(Code05_Walkthrough2.first, Code05_Walkthrough2.second, jcast('int', (-2)))
                    Code05_Walkthrough2.push(Code05_Walkthrough2.son[Code05_Walkthrough2.first], Code05_Walkthrough2.second, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code05_Walkthrough2.edge == jcast('int', (-2))):
                        Code05_Walkthrough2.edge = jcast('int', Code05_Walkthrough2.head[Code05_Walkthrough2.first])
                    else:
                        Code05_Walkthrough2.edge = jcast('int', Code05_Walkthrough2.next[Code05_Walkthrough2.edge])
                if (Code05_Walkthrough2.edge != 0):
                    Code05_Walkthrough2.push(Code05_Walkthrough2.first, Code05_Walkthrough2.second, Code05_Walkthrough2.edge)
                    if ((Code05_Walkthrough2.to[Code05_Walkthrough2.edge] != Code05_Walkthrough2.fa[Code05_Walkthrough2.first]) and (Code05_Walkthrough2.to[Code05_Walkthrough2.edge] != Code05_Walkthrough2.son[Code05_Walkthrough2.first])):
                        Code05_Walkthrough2.push(Code05_Walkthrough2.to[Code05_Walkthrough2.edge], Code05_Walkthrough2.to[Code05_Walkthrough2.edge], jcast('int', (-1)))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    @staticmethod
    def compute():
        len = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_Walkthrough2.n):
            if (Code05_Walkthrough2.top[i] == i):
                jset(Code05_Walkthrough2.sorted, (len := jcast('int', (len + (1)))), Code05_Walkthrough2.money[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Walkthrough2.sorted, 1, jcast('int', jadd(len, 1)))
        ans = jcast('long', 0)
        i = jcast('int', 1)
        j = jcast('int', len)
        while (i <= Code05_Walkthrough2.k):
            ans = jcast('long', jcast('long', jadd(ans, Code05_Walkthrough2.sorted[j])))
            i = jcast('int', (i + 1))
            j = jcast('int', (j - 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_Walkthrough2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_Walkthrough2.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code05_Walkthrough2.n):
            jcall(in_, 'nextToken')
            Code05_Walkthrough2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code05_Walkthrough2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_Walkthrough2.addEdge(u, v)
            Code05_Walkthrough2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code05_Walkthrough2.dfs3()
        Code05_Walkthrough2.dfs4()
        jcall(out, 'println', Code05_Walkthrough2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Walkthrough2.MAXN = jcast('int', 200001)
Code05_Walkthrough2.n = jcast('int', 0)
Code05_Walkthrough2.k = jcast('int', 0)
Code05_Walkthrough2.arr = jarray('int', [Code05_Walkthrough2.MAXN])
Code05_Walkthrough2.head = jarray('int', [Code05_Walkthrough2.MAXN])
Code05_Walkthrough2.next = jarray('int', [jcast('int', (Code05_Walkthrough2.MAXN << (1 & 31)))])
Code05_Walkthrough2.to = jarray('int', [jcast('int', (Code05_Walkthrough2.MAXN << (1 & 31)))])
Code05_Walkthrough2.cnt = jcast('int', 0)
Code05_Walkthrough2.fa = jarray('int', [Code05_Walkthrough2.MAXN])
Code05_Walkthrough2.son = jarray('int', [Code05_Walkthrough2.MAXN])
Code05_Walkthrough2.top = jarray('int', [Code05_Walkthrough2.MAXN])
Code05_Walkthrough2.money = jarray('long', [Code05_Walkthrough2.MAXN])
Code05_Walkthrough2.sorted = jarray('long', [Code05_Walkthrough2.MAXN])
Code05_Walkthrough2.fse = jarray('int', [Code05_Walkthrough2.MAXN, 3])
Code05_Walkthrough2.stacksize = jcast('int', 0)
Code05_Walkthrough2.first = jcast('int', 0)
Code05_Walkthrough2.second = jcast('int', 0)
Code05_Walkthrough2.edge = jcast('int', 0)

if __name__ == '__main__':
    Code05_Walkthrough2.main([])
