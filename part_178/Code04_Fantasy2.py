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

# 幻想乡战略游戏，Python版
# 树上有n个点，每个点的初始点权是0，给定n-1条边，每条边有边权
# 如果点x是指挥点，它指挥点y的花费 = x到y的简单路径权值和 * y的点权
# 树上存在某个最佳的指挥点，指挥所有点的总花费最小，叫做最小指挥总花费
# 一共m条操作，格式 x v : 先把x的点权增加v，然后打印此时的最小指挥总花费
# 注意参数v有可能是负数，但题目保证任何时候，点权不会出现负数
# 1 <= n、m <= 10^5
# 1 <= 边权 <= 1000
# -1000 <= v <= +1000
# 测试链接 : https://www.luogu.com.cn/problem/P3345
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Fantasy2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cent': 'cent', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dist': 'dist', 'vis': 'vis', 'centfa': 'centfa', 'sum': 'sum', 'addCost': 'addCost', 'minusCost': 'minusCost', 'stack': 'stack', 'u': 'u', 'f': 'f', 'a': 'a', 'b': 'b', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    weight = None
    cent = None
    cntg = 0
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    dist = None
    vis = None
    centfa = None
    sum = None
    addCost = None
    minusCost = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    a = 0
    b = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, a, b, e):
        u = jcast('int', u)
        f = jcast('int', f)
        a = jcast('int', a)
        b = jcast('int', b)
        e = jcast('int', e)
        jset(Code04_Fantasy2.stack[Code04_Fantasy2.stacksize], 0, u)
        jset(Code04_Fantasy2.stack[Code04_Fantasy2.stacksize], 1, f)
        jset(Code04_Fantasy2.stack[Code04_Fantasy2.stacksize], 2, a)
        jset(Code04_Fantasy2.stack[Code04_Fantasy2.stacksize], 3, b)
        jset(Code04_Fantasy2.stack[Code04_Fantasy2.stacksize], 4, e)
        Code04_Fantasy2.stacksize = jcast('int', (Code04_Fantasy2.stacksize + 1))

    @staticmethod
    def pop():
        Code04_Fantasy2.stacksize = jcast('int', (Code04_Fantasy2.stacksize - 1))
        Code04_Fantasy2.u = jcast('int', Code04_Fantasy2.stack[Code04_Fantasy2.stacksize][0])
        Code04_Fantasy2.f = jcast('int', Code04_Fantasy2.stack[Code04_Fantasy2.stacksize][1])
        Code04_Fantasy2.a = jcast('int', Code04_Fantasy2.stack[Code04_Fantasy2.stacksize][2])
        Code04_Fantasy2.b = jcast('int', Code04_Fantasy2.stack[Code04_Fantasy2.stacksize][3])
        Code04_Fantasy2.e = jcast('int', Code04_Fantasy2.stack[Code04_Fantasy2.stacksize][4])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_Fantasy2.nxt, ((_java_obj_1 := Code04_Fantasy2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Fantasy2.head[u])
        Code04_Fantasy2.to[Code04_Fantasy2.cntg] = jcast('int', v)
        Code04_Fantasy2.weight[Code04_Fantasy2.cntg] = jcast('int', w)
        Code04_Fantasy2.head[u] = jcast('int', Code04_Fantasy2.cntg)

    @staticmethod
    def dfs1(u, f, dis):
        u = jcast('int', u)
        f = jcast('int', f)
        dis = jcast('int', dis)
        Code04_Fantasy2.fa[u] = jcast('int', f)
        Code04_Fantasy2.dep[u] = jcast('int', jcast('int', jadd(Code04_Fantasy2.dep[f], 1)))
        Code04_Fantasy2.dist[u] = jcast('int', dis)
        Code04_Fantasy2.siz[u] = jcast('int', 1)
        e = jcast('int', Code04_Fantasy2.head[u])
        while (e > 0):
            v = jcast('int', Code04_Fantasy2.to[e])
            w = jcast('int', Code04_Fantasy2.weight[e])
            if (v != f):
                Code04_Fantasy2.dfs1(v, u, jcast('int', jadd(dis, w)))
            e = jcast('int', Code04_Fantasy2.nxt[e])
        ei = jcast('int', Code04_Fantasy2.head[u])
        v = 0
        while (ei > 0):
            v = jcast('int', Code04_Fantasy2.to[ei])
            if (v != f):
                Code04_Fantasy2.siz[u] = jcast('int', jcast('int', jadd(Code04_Fantasy2.siz[u], Code04_Fantasy2.siz[v])))
                if ((Code04_Fantasy2.son[u] == 0) or (Code04_Fantasy2.siz[Code04_Fantasy2.son[u]] < Code04_Fantasy2.siz[v])):
                    Code04_Fantasy2.son[u] = jcast('int', v)
            ei = jcast('int', Code04_Fantasy2.nxt[ei])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code04_Fantasy2.top[u] = jcast('int', t)
        if (Code04_Fantasy2.son[u] == 0):
            return
        Code04_Fantasy2.dfs2(Code04_Fantasy2.son[u], t)
        e = jcast('int', Code04_Fantasy2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_Fantasy2.to[e])
            if ((v != Code04_Fantasy2.fa[u]) and (v != Code04_Fantasy2.son[u])):
                Code04_Fantasy2.dfs2(v, v)
            e = jcast('int', Code04_Fantasy2.nxt[e])

    @staticmethod
    def dfs3(cur, father, distance):
        cur = jcast('int', cur)
        father = jcast('int', father)
        distance = jcast('int', distance)
        Code04_Fantasy2.stacksize = jcast('int', 0)
        Code04_Fantasy2.push(cur, father, distance, 0, jcast('int', (-1)))
        while (Code04_Fantasy2.stacksize > 0):
            Code04_Fantasy2.pop()
            if (Code04_Fantasy2.e == jcast('int', (-1))):
                Code04_Fantasy2.fa[Code04_Fantasy2.u] = jcast('int', Code04_Fantasy2.f)
                Code04_Fantasy2.dep[Code04_Fantasy2.u] = jcast('int', jcast('int', jadd(Code04_Fantasy2.dep[Code04_Fantasy2.f], 1)))
                Code04_Fantasy2.dist[Code04_Fantasy2.u] = jcast('int', Code04_Fantasy2.a)
                Code04_Fantasy2.siz[Code04_Fantasy2.u] = jcast('int', 1)
                Code04_Fantasy2.e = jcast('int', Code04_Fantasy2.head[Code04_Fantasy2.u])
            else:
                Code04_Fantasy2.e = jcast('int', Code04_Fantasy2.nxt[Code04_Fantasy2.e])
            if (Code04_Fantasy2.e != 0):
                Code04_Fantasy2.push(Code04_Fantasy2.u, Code04_Fantasy2.f, Code04_Fantasy2.a, 0, Code04_Fantasy2.e)
                v = jcast('int', Code04_Fantasy2.to[Code04_Fantasy2.e])
                w = jcast('int', Code04_Fantasy2.weight[Code04_Fantasy2.e])
                if (v != Code04_Fantasy2.f):
                    Code04_Fantasy2.push(v, Code04_Fantasy2.u, jcast('int', jadd(Code04_Fantasy2.a, w)), 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code04_Fantasy2.head[Code04_Fantasy2.u])
                while (ei > 0):
                    v = jcast('int', Code04_Fantasy2.to[ei])
                    if (v != Code04_Fantasy2.f):
                        Code04_Fantasy2.siz[Code04_Fantasy2.u] = jcast('int', jcast('int', jadd(Code04_Fantasy2.siz[Code04_Fantasy2.u], Code04_Fantasy2.siz[v])))
                        if ((Code04_Fantasy2.son[Code04_Fantasy2.u] == 0) or (Code04_Fantasy2.siz[Code04_Fantasy2.son[Code04_Fantasy2.u]] < Code04_Fantasy2.siz[v])):
                            Code04_Fantasy2.son[Code04_Fantasy2.u] = jcast('int', v)
                    ei = jcast('int', Code04_Fantasy2.nxt[ei])

    @staticmethod
    def dfs4(cur, tag):
        cur = jcast('int', cur)
        tag = jcast('int', tag)
        Code04_Fantasy2.stacksize = jcast('int', 0)
        Code04_Fantasy2.push(cur, 0, 0, tag, jcast('int', (-1)))
        while (Code04_Fantasy2.stacksize > 0):
            try:
                Code04_Fantasy2.pop()
                if (Code04_Fantasy2.e == jcast('int', (-1))):
                    Code04_Fantasy2.top[Code04_Fantasy2.u] = jcast('int', Code04_Fantasy2.b)
                    if (Code04_Fantasy2.son[Code04_Fantasy2.u] == 0):
                        raise JContinue(None)
                    Code04_Fantasy2.push(Code04_Fantasy2.u, 0, 0, Code04_Fantasy2.b, jcast('int', (-2)))
                    Code04_Fantasy2.push(Code04_Fantasy2.son[Code04_Fantasy2.u], 0, 0, Code04_Fantasy2.b, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code04_Fantasy2.e == jcast('int', (-2))):
                        Code04_Fantasy2.e = jcast('int', Code04_Fantasy2.head[Code04_Fantasy2.u])
                    else:
                        Code04_Fantasy2.e = jcast('int', Code04_Fantasy2.nxt[Code04_Fantasy2.e])
                if (Code04_Fantasy2.e != 0):
                    Code04_Fantasy2.push(Code04_Fantasy2.u, 0, 0, Code04_Fantasy2.b, Code04_Fantasy2.e)
                    v = jcast('int', Code04_Fantasy2.to[Code04_Fantasy2.e])
                    if ((v != Code04_Fantasy2.fa[Code04_Fantasy2.u]) and (v != Code04_Fantasy2.son[Code04_Fantasy2.u])):
                        Code04_Fantasy2.push(v, 0, 0, v, jcast('int', (-1)))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        while (Code04_Fantasy2.top[a] != Code04_Fantasy2.top[b]):
            if (Code04_Fantasy2.dep[Code04_Fantasy2.top[a]] <= Code04_Fantasy2.dep[Code04_Fantasy2.top[b]]):
                b = jcast('int', Code04_Fantasy2.fa[Code04_Fantasy2.top[b]])
            else:
                a = jcast('int', Code04_Fantasy2.fa[Code04_Fantasy2.top[a]])
        return jcast('int', (a if (Code04_Fantasy2.dep[a] <= Code04_Fantasy2.dep[b]) else b))

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code04_Fantasy2.dist[x], Code04_Fantasy2.dist[y])) - jcast('int', (Code04_Fantasy2.dist[Code04_Fantasy2.getLca(x, y)] << (1 & 31))))))

    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_Fantasy2.siz[u] = jcast('int', 1)
        e = jcast('int', Code04_Fantasy2.head[u])
        while (e > 0):
            v = jcast('int', Code04_Fantasy2.to[e])
            if ((v != fa) and (not Code04_Fantasy2.vis[v])):
                Code04_Fantasy2.getSize1(v, u)
                Code04_Fantasy2.siz[u] = jcast('int', jcast('int', jadd(Code04_Fantasy2.siz[u], Code04_Fantasy2.siz[v])))
            e = jcast('int', Code04_Fantasy2.nxt[e])

    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code04_Fantasy2.stacksize = jcast('int', 0)
        Code04_Fantasy2.push(cur, fa, 0, 0, jcast('int', (-1)))
        while (Code04_Fantasy2.stacksize > 0):
            Code04_Fantasy2.pop()
            if (Code04_Fantasy2.e == jcast('int', (-1))):
                Code04_Fantasy2.siz[Code04_Fantasy2.u] = jcast('int', 1)
                Code04_Fantasy2.e = jcast('int', Code04_Fantasy2.head[Code04_Fantasy2.u])
            else:
                Code04_Fantasy2.e = jcast('int', Code04_Fantasy2.nxt[Code04_Fantasy2.e])
            if (Code04_Fantasy2.e != 0):
                Code04_Fantasy2.push(Code04_Fantasy2.u, Code04_Fantasy2.f, 0, 0, Code04_Fantasy2.e)
                v = jcast('int', Code04_Fantasy2.to[Code04_Fantasy2.e])
                if ((v != Code04_Fantasy2.f) and (not Code04_Fantasy2.vis[v])):
                    Code04_Fantasy2.push(v, Code04_Fantasy2.u, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code04_Fantasy2.head[Code04_Fantasy2.u])
                while (ei > 0):
                    v = jcast('int', Code04_Fantasy2.to[ei])
                    if ((v != Code04_Fantasy2.f) and (not Code04_Fantasy2.vis[v])):
                        Code04_Fantasy2.siz[Code04_Fantasy2.u] = jcast('int', jcast('int', jadd(Code04_Fantasy2.siz[Code04_Fantasy2.u], Code04_Fantasy2.siz[v])))
                    ei = jcast('int', Code04_Fantasy2.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code04_Fantasy2.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code04_Fantasy2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code04_Fantasy2.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code04_Fantasy2.to[e])
                        if (((v != fa) and (not Code04_Fantasy2.vis[v])) and (Code04_Fantasy2.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                    except JBreak as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code04_Fantasy2.nxt[e])
            except JContinue as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
            except JBreak as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def centroidTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_Fantasy2.centfa[u] = jcast('int', fa)
        Code04_Fantasy2.vis[u] = jcast('boolean', True)
        e = jcast('int', Code04_Fantasy2.head[u])
        while (e > 0):
            v = jcast('int', Code04_Fantasy2.to[e])
            if (not Code04_Fantasy2.vis[v]):
                nextCent = jcast('int', Code04_Fantasy2.getCentroid(v, u))
                Code04_Fantasy2.cent[e] = jcast('int', nextCent)
                Code04_Fantasy2.centroidTree(nextCent, u)
            e = jcast('int', Code04_Fantasy2.nxt[e])

    @staticmethod
    def add(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        Code04_Fantasy2.sum[x] = jcast('long', jcast('long', jadd(Code04_Fantasy2.sum[x], v)))
        cur = jcast('int', x)
        fa = jcast('int', Code04_Fantasy2.centfa[cur])
        while (fa > 0):
            dist = jcast('int', Code04_Fantasy2.getDist(x, fa))
            Code04_Fantasy2.sum[fa] = jcast('long', jcast('long', jadd(Code04_Fantasy2.sum[fa], v)))
            Code04_Fantasy2.addCost[fa] = jcast('long', jcast('long', jadd(Code04_Fantasy2.addCost[fa], jcast('long', (jcast('long', (1 * v)) * dist)))))
            Code04_Fantasy2.minusCost[cur] = jcast('long', jcast('long', jadd(Code04_Fantasy2.minusCost[cur], jcast('long', (jcast('long', (1 * v)) * dist)))))
            cur = jcast('int', fa)
            fa = jcast('int', Code04_Fantasy2.centfa[cur])

    @staticmethod
    def query(x):
        x = jcast('int', x)
        ans = jcast('long', Code04_Fantasy2.addCost[x])
        cur = jcast('int', x)
        fa = jcast('int', Code04_Fantasy2.centfa[cur])
        while (fa > 0):
            dist = jcast('int', Code04_Fantasy2.getDist(x, fa))
            ans = jcast('long', jcast('long', jadd(ans, Code04_Fantasy2.addCost[fa])))
            ans = jcast('long', jcast('long', (ans - Code04_Fantasy2.minusCost[cur])))
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', (Code04_Fantasy2.sum[fa] - Code04_Fantasy2.sum[cur])) * dist)))))
            cur = jcast('int', fa)
            fa = jcast('int', Code04_Fantasy2.centfa[cur])
        return jcast('long', ans)

    @staticmethod
    def compute(u):
        u = jcast('int', u)
        ans = jcast('long', Code04_Fantasy2.query(u))
        e = jcast('int', Code04_Fantasy2.head[u])
        while (e > 0):
            v = jcast('int', Code04_Fantasy2.to[e])
            if (Code04_Fantasy2.query(v) < ans):
                return jcast('long', Code04_Fantasy2.compute(Code04_Fantasy2.cent[e]))
            e = jcast('int', Code04_Fantasy2.nxt[e])
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code04_Fantasy2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Fantasy2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Fantasy2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code04_Fantasy2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code04_Fantasy2.addEdge(u, v, w)
            Code04_Fantasy2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        # dfs1(1, 0, 0);
        # dfs2(1, 1);
        Code04_Fantasy2.dfs3(1, 0, 0)
        Code04_Fantasy2.dfs4(1, 1)
        root = jcast('int', Code04_Fantasy2.getCentroid(1, 0))
        Code04_Fantasy2.centroidTree(root, 0)
        i = jcast('int', 1)
        x = 0
        v = 0
        while (i <= Code04_Fantasy2.m):
            x = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_Fantasy2.add(x, v)
            jcall(out, 'println', Code04_Fantasy2.compute(root))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_Fantasy2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Fantasy2.MAXN = jcast('int', 100001)
Code04_Fantasy2.n = jcast('int', 0)
Code04_Fantasy2.m = jcast('int', 0)
Code04_Fantasy2.head = jarray('int', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.nxt = jarray('int', [jcast('int', (Code04_Fantasy2.MAXN << (1 & 31)))])
Code04_Fantasy2.to = jarray('int', [jcast('int', (Code04_Fantasy2.MAXN << (1 & 31)))])
Code04_Fantasy2.weight = jarray('int', [jcast('int', (Code04_Fantasy2.MAXN << (1 & 31)))])
Code04_Fantasy2.cent = jarray('int', [jcast('int', (Code04_Fantasy2.MAXN << (1 & 31)))])
Code04_Fantasy2.cntg = jcast('int', 0)
Code04_Fantasy2.fa = jarray('int', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.dep = jarray('int', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.siz = jarray('int', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.son = jarray('int', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.top = jarray('int', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.dist = jarray('int', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.vis = jarray('boolean', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.centfa = jarray('int', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.sum = jarray('long', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.addCost = jarray('long', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.minusCost = jarray('long', [Code04_Fantasy2.MAXN])
Code04_Fantasy2.stack = jarray('int', [Code04_Fantasy2.MAXN, 5])
Code04_Fantasy2.u = jcast('int', 0)
Code04_Fantasy2.f = jcast('int', 0)
Code04_Fantasy2.a = jcast('int', 0)
Code04_Fantasy2.b = jcast('int', 0)
Code04_Fantasy2.e = jcast('int', 0)
Code04_Fantasy2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code04_Fantasy2.main([])
