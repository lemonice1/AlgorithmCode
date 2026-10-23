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

# 树上k级祖先，Python版
# 一共有n个节点，编号1~n，给定一个长度为n的数组arr，表示依赖关系
# 如果arr[i] = j，表示i号节点的父节点是j，如果arr[i] == 0，表示i号节点是树头
# 一共有m条查询，每条查询 x k : 打印x往上走k步的祖先节点编号
# 题目要求预处理的时间复杂度O(n * log n)，处理每条查询的时间复杂度O(1)
# 题目要求强制在线，必须按顺序处理每条查询，如何得到每条查询的入参，请打开测试链接查看
# 1 <= n <= 5 * 10^5
# 1 <= m <= 5 * 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P5903
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_TreeKthAncestor1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 's': 's', 'root': 'root', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'stjump': 'stjump', 'dep': 'dep', 'len': 'len', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'cntd': 'cntd', 'high': 'high', 'up': 'up', 'down': 'down', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    MAXP = 0
    n = 0
    m = 0
    s = 0
    root = 0
    # 链式前向星，注意是有向图，所以边的数量不需要增倍
    head = None
    next = None
    to = None
    cntg = 0
    # 倍增表 + 长链剖分
    stjump = None
    dep = None
    len = None
    son = None
    top = None
    dfn = None
    cntd = 0
    # 查询答案需要
    high = None
    up = None
    down = None
    # 题目规定如何得到输入数据的函数
    # 原始无符号整数范围使用 64 位整数兼容语义表示，位移与截断由运行时辅助函数处理
    @staticmethod
    def get(x):
        x = jcast('long', x)
        x = jcast('long', jcast('long', (x ^ jcast('long', (x << (13 & 63))))))
        x = jcast('long', jcast('long', (x & 4294967295)))
        x = jcast('long', jcast('long', (x ^ jcast('long', jushr(x, 17, 64)))))
        x = jcast('long', jcast('long', (x ^ jcast('long', (x << (5 & 63))))))
        x = jcast('long', jcast('long', (x & 4294967295)))
        return jcast('long', jset(Code04_TreeKthAncestor1, 's', x))

    @staticmethod
    def setUp(u, i, v):
        u = jcast('int', u)
        i = jcast('int', i)
        v = jcast('int', v)
        jset(Code04_TreeKthAncestor1.up, jcast('int', jadd(Code04_TreeKthAncestor1.dfn[u], i)), v)

    @staticmethod
    def getUp(u, i):
        u = jcast('int', u)
        i = jcast('int', i)
        return jcast('int', Code04_TreeKthAncestor1.up[jcast('int', jadd(Code04_TreeKthAncestor1.dfn[u], i))])

    @staticmethod
    def setDown(u, i, v):
        u = jcast('int', u)
        i = jcast('int', i)
        v = jcast('int', v)
        jset(Code04_TreeKthAncestor1.down, jcast('int', jadd(Code04_TreeKthAncestor1.dfn[u], i)), v)

    @staticmethod
    def getDown(u, i):
        u = jcast('int', u)
        i = jcast('int', i)
        return jcast('int', Code04_TreeKthAncestor1.down[jcast('int', jadd(Code04_TreeKthAncestor1.dfn[u], i))])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_TreeKthAncestor1.next, ((_java_obj_1 := Code04_TreeKthAncestor1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_TreeKthAncestor1.head[u])
        Code04_TreeKthAncestor1.to[Code04_TreeKthAncestor1.cntg] = jcast('int', v)
        Code04_TreeKthAncestor1.head[u] = jcast('int', Code04_TreeKthAncestor1.cntg)

    # 递归版
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        jset(Code04_TreeKthAncestor1.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p < Code04_TreeKthAncestor1.MAXP):
            jset(Code04_TreeKthAncestor1.stjump[u], p, Code04_TreeKthAncestor1.stjump[Code04_TreeKthAncestor1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        Code04_TreeKthAncestor1.dep[u] = jcast('int', jcast('int', jadd(Code04_TreeKthAncestor1.dep[f], 1)))
        e = jcast('int', Code04_TreeKthAncestor1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_TreeKthAncestor1.to[e])
            if (v != f):
                Code04_TreeKthAncestor1.dfs1(v, u)
            e = jcast('int', Code04_TreeKthAncestor1.next[e])
        e = jcast('int', Code04_TreeKthAncestor1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_TreeKthAncestor1.to[e])
            if (v != f):
                if ((Code04_TreeKthAncestor1.son[u] == 0) or (Code04_TreeKthAncestor1.len[Code04_TreeKthAncestor1.son[u]] < Code04_TreeKthAncestor1.len[v])):
                    Code04_TreeKthAncestor1.son[u] = jcast('int', v)
            e = jcast('int', Code04_TreeKthAncestor1.next[e])
        Code04_TreeKthAncestor1.len[u] = jcast('int', jcast('int', jadd(Code04_TreeKthAncestor1.len[Code04_TreeKthAncestor1.son[u]], 1)))

    # 递归版
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code04_TreeKthAncestor1.top[u] = jcast('int', t)
        jset(Code04_TreeKthAncestor1.dfn, u, ((_java_obj_4 := Code04_TreeKthAncestor1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (Code04_TreeKthAncestor1.son[u] == 0):
            return
        Code04_TreeKthAncestor1.dfs2(Code04_TreeKthAncestor1.son[u], t)
        e = jcast('int', Code04_TreeKthAncestor1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_TreeKthAncestor1.to[e])
            if ((v != Code04_TreeKthAncestor1.stjump[u][0]) and (v != Code04_TreeKthAncestor1.son[u])):
                Code04_TreeKthAncestor1.dfs2(v, v)
            e = jcast('int', Code04_TreeKthAncestor1.next[e])

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
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
        jset(Code04_TreeKthAncestor1.fse[Code04_TreeKthAncestor1.stacksize], 0, fir)
        jset(Code04_TreeKthAncestor1.fse[Code04_TreeKthAncestor1.stacksize], 1, sec)
        jset(Code04_TreeKthAncestor1.fse[Code04_TreeKthAncestor1.stacksize], 2, edg)
        Code04_TreeKthAncestor1.stacksize = jcast('int', (Code04_TreeKthAncestor1.stacksize + 1))

    @staticmethod
    def pop():
        Code04_TreeKthAncestor1.stacksize = jcast('int', (Code04_TreeKthAncestor1.stacksize - 1))
        Code04_TreeKthAncestor1.first = jcast('int', Code04_TreeKthAncestor1.fse[Code04_TreeKthAncestor1.stacksize][0])
        Code04_TreeKthAncestor1.second = jcast('int', Code04_TreeKthAncestor1.fse[Code04_TreeKthAncestor1.stacksize][1])
        Code04_TreeKthAncestor1.edge = jcast('int', Code04_TreeKthAncestor1.fse[Code04_TreeKthAncestor1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code04_TreeKthAncestor1.stacksize = jcast('int', 0)
        Code04_TreeKthAncestor1.push(Code04_TreeKthAncestor1.root, 0, jcast('int', (-1)))
        while (Code04_TreeKthAncestor1.stacksize > 0):
            Code04_TreeKthAncestor1.pop()
            if (Code04_TreeKthAncestor1.edge == jcast('int', (-1))):
                jset(Code04_TreeKthAncestor1.stjump[Code04_TreeKthAncestor1.first], 0, Code04_TreeKthAncestor1.second)
                p = jcast('int', 1)
                while (p < Code04_TreeKthAncestor1.MAXP):
                    jset(Code04_TreeKthAncestor1.stjump[Code04_TreeKthAncestor1.first], p, Code04_TreeKthAncestor1.stjump[Code04_TreeKthAncestor1.stjump[Code04_TreeKthAncestor1.first][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code04_TreeKthAncestor1.dep[Code04_TreeKthAncestor1.first] = jcast('int', jcast('int', jadd(Code04_TreeKthAncestor1.dep[Code04_TreeKthAncestor1.second], 1)))
                Code04_TreeKthAncestor1.edge = jcast('int', Code04_TreeKthAncestor1.head[Code04_TreeKthAncestor1.first])
            else:
                Code04_TreeKthAncestor1.edge = jcast('int', Code04_TreeKthAncestor1.next[Code04_TreeKthAncestor1.edge])
            if (Code04_TreeKthAncestor1.edge != 0):
                Code04_TreeKthAncestor1.push(Code04_TreeKthAncestor1.first, Code04_TreeKthAncestor1.second, Code04_TreeKthAncestor1.edge)
                if (Code04_TreeKthAncestor1.to[Code04_TreeKthAncestor1.edge] != Code04_TreeKthAncestor1.second):
                    Code04_TreeKthAncestor1.push(Code04_TreeKthAncestor1.to[Code04_TreeKthAncestor1.edge], Code04_TreeKthAncestor1.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code04_TreeKthAncestor1.head[Code04_TreeKthAncestor1.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code04_TreeKthAncestor1.to[e])
                    if (v != Code04_TreeKthAncestor1.second):
                        if ((Code04_TreeKthAncestor1.son[Code04_TreeKthAncestor1.first] == 0) or (Code04_TreeKthAncestor1.len[Code04_TreeKthAncestor1.son[Code04_TreeKthAncestor1.first]] < Code04_TreeKthAncestor1.len[v])):
                            Code04_TreeKthAncestor1.son[Code04_TreeKthAncestor1.first] = jcast('int', v)
                    e = jcast('int', Code04_TreeKthAncestor1.next[e])
                Code04_TreeKthAncestor1.len[Code04_TreeKthAncestor1.first] = jcast('int', jcast('int', jadd(Code04_TreeKthAncestor1.len[Code04_TreeKthAncestor1.son[Code04_TreeKthAncestor1.first]], 1)))

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code04_TreeKthAncestor1.stacksize = jcast('int', 0)
        Code04_TreeKthAncestor1.push(Code04_TreeKthAncestor1.root, Code04_TreeKthAncestor1.root, jcast('int', (-1)))
        while (Code04_TreeKthAncestor1.stacksize > 0):
            try:
                Code04_TreeKthAncestor1.pop()
                # edge == -1，表示第一次来到当前节点，并且先处理重儿子
                if (Code04_TreeKthAncestor1.edge == jcast('int', (-1))):
                    Code04_TreeKthAncestor1.top[Code04_TreeKthAncestor1.first] = jcast('int', Code04_TreeKthAncestor1.second)
                    jset(Code04_TreeKthAncestor1.dfn, Code04_TreeKthAncestor1.first, ((_java_obj_8 := Code04_TreeKthAncestor1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    if (Code04_TreeKthAncestor1.son[Code04_TreeKthAncestor1.first] == 0):
                        raise JContinue(None)
                    Code04_TreeKthAncestor1.push(Code04_TreeKthAncestor1.first, Code04_TreeKthAncestor1.second, jcast('int', (-2)))
                    Code04_TreeKthAncestor1.push(Code04_TreeKthAncestor1.son[Code04_TreeKthAncestor1.first], Code04_TreeKthAncestor1.second, jcast('int', (-1)))
                    raise JContinue(None)
                    # edge == -2，表示处理完当前节点的重儿子，回到了当前节点
                else:
                    if (Code04_TreeKthAncestor1.edge == jcast('int', (-2))):
                        Code04_TreeKthAncestor1.edge = jcast('int', Code04_TreeKthAncestor1.head[Code04_TreeKthAncestor1.first])
                        # edge >= 0, 继续处理其他的边
                    else:
                        Code04_TreeKthAncestor1.edge = jcast('int', Code04_TreeKthAncestor1.next[Code04_TreeKthAncestor1.edge])
                if (Code04_TreeKthAncestor1.edge != 0):
                    Code04_TreeKthAncestor1.push(Code04_TreeKthAncestor1.first, Code04_TreeKthAncestor1.second, Code04_TreeKthAncestor1.edge)
                    if ((Code04_TreeKthAncestor1.to[Code04_TreeKthAncestor1.edge] != Code04_TreeKthAncestor1.stjump[Code04_TreeKthAncestor1.first][0]) and (Code04_TreeKthAncestor1.to[Code04_TreeKthAncestor1.edge] != Code04_TreeKthAncestor1.son[Code04_TreeKthAncestor1.first])):
                        Code04_TreeKthAncestor1.push(Code04_TreeKthAncestor1.to[Code04_TreeKthAncestor1.edge], Code04_TreeKthAncestor1.to[Code04_TreeKthAncestor1.edge], jcast('int', (-1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def prepare():
        Code04_TreeKthAncestor1.dfs3()
        Code04_TreeKthAncestor1.dfs4()
        Code04_TreeKthAncestor1.high[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code04_TreeKthAncestor1.n):
            Code04_TreeKthAncestor1.high[i] = jcast('int', jcast('int', jadd(Code04_TreeKthAncestor1.high[jcast('int', jdiv(i, 2))], 1)))
            i = jcast('int', (i + 1))
        u = jcast('int', 1)
        while (u <= Code04_TreeKthAncestor1.n):
            if (Code04_TreeKthAncestor1.top[u] == u):
                i = jcast('int', 0)
                a = jcast('int', u)
                b = jcast('int', u)
                while (i < Code04_TreeKthAncestor1.len[u]):
                    Code04_TreeKthAncestor1.setUp(u, i, a)
                    Code04_TreeKthAncestor1.setDown(u, i, b)
                    i = jcast('int', (i + 1))
                    a = jcast('int', Code04_TreeKthAncestor1.stjump[a][0])
                    b = jcast('int', Code04_TreeKthAncestor1.son[b])
            u = jcast('int', (u + 1))

    @staticmethod
    def query(x, k):
        x = jcast('int', x)
        k = jcast('int', k)
        if (k == 0):
            return jcast('int', x)
        if (k == jcast('int', (1 << (Code04_TreeKthAncestor1.high[k] & 31)))):
            return jcast('int', Code04_TreeKthAncestor1.stjump[x][Code04_TreeKthAncestor1.high[k]])
        x = jcast('int', Code04_TreeKthAncestor1.stjump[x][Code04_TreeKthAncestor1.high[k]])
        k = jcast('int', jcast('int', (k - jcast('int', (1 << (Code04_TreeKthAncestor1.high[k] & 31))))))
        k = jcast('int', jcast('int', (k - jcast('int', (Code04_TreeKthAncestor1.dep[x] - Code04_TreeKthAncestor1.dep[Code04_TreeKthAncestor1.top[x]])))))
        x = jcast('int', Code04_TreeKthAncestor1.top[x])
        return jcast('int', (Code04_TreeKthAncestor1.getUp(x, k) if (k >= 0) else Code04_TreeKthAncestor1.getDown(x, jcast('int', (-k)))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_TreeKthAncestor1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_TreeKthAncestor1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_TreeKthAncestor1.s = jcast('long', jcast('long', jget(in_, 'nval')))
        i = jcast('int', 1)
        father = 0
        while (i <= Code04_TreeKthAncestor1.n):
            jcall(in_, 'nextToken')
            father = jcast('int', jcast('int', jget(in_, 'nval')))
            if (father == 0):
                Code04_TreeKthAncestor1.root = jcast('int', i)
            else:
                Code04_TreeKthAncestor1.addEdge(father, i)
            i = jcast('int', (i + 1))
        Code04_TreeKthAncestor1.prepare()
        ans = jcast('long', 0)
        i = jcast('int', 1)
        x = 0
        k = 0
        lastAns = jcast('int', 0)
        while (i <= Code04_TreeKthAncestor1.m):
            x = jcast('int', jcast('int', jcast('long', jadd(jcast('long', jmod(jcast('long', (Code04_TreeKthAncestor1.get(Code04_TreeKthAncestor1.s) ^ lastAns)), Code04_TreeKthAncestor1.n)), 1))))
            k = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (Code04_TreeKthAncestor1.get(Code04_TreeKthAncestor1.s) ^ lastAns)), Code04_TreeKthAncestor1.dep[x]))))
            lastAns = jcast('int', Code04_TreeKthAncestor1.query(x, k))
            ans = jcast('long', jcast('long', (ans ^ jcast('long', (jcast('long', i) * lastAns)))))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_TreeKthAncestor1.MAXN = jcast('int', 500001)
Code04_TreeKthAncestor1.MAXP = jcast('int', 20)
Code04_TreeKthAncestor1.n = jcast('int', 0)
Code04_TreeKthAncestor1.m = jcast('int', 0)
Code04_TreeKthAncestor1.s = jcast('long', 0)
Code04_TreeKthAncestor1.root = jcast('int', 0)
Code04_TreeKthAncestor1.head = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.next = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.to = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.cntg = jcast('int', 0)
Code04_TreeKthAncestor1.stjump = jarray('int', [Code04_TreeKthAncestor1.MAXN, Code04_TreeKthAncestor1.MAXP])
Code04_TreeKthAncestor1.dep = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.len = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.son = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.top = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.dfn = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.cntd = jcast('int', 0)
Code04_TreeKthAncestor1.high = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.up = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.down = jarray('int', [Code04_TreeKthAncestor1.MAXN])
Code04_TreeKthAncestor1.fse = jarray('int', [Code04_TreeKthAncestor1.MAXN, 3])
Code04_TreeKthAncestor1.stacksize = jcast('int', 0)
Code04_TreeKthAncestor1.first = jcast('int', 0)
Code04_TreeKthAncestor1.second = jcast('int', 0)
Code04_TreeKthAncestor1.edge = jcast('int', 0)

if __name__ == '__main__':
    Code04_TreeKthAncestor1.main([])
