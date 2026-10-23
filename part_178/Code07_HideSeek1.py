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

# 捉迷藏，点分树的解，Python版
# 树上有n个点，点的初始颜色为黑，给定n-1条边，边权都是1
# 一共有m条操作，每条操作是如下两种类型中的一种
# 操作 C x : 改变点x的颜色，黑变成白，白变成黑
# 操作 G   : 打印最远的两个黑点的距离，只有一个黑点打印0，无黑点打印-1
# 1 <= n <= 10^5    1 <= m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2056
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本节课Code07_HideSeek3文件是最优解的实现
class Code07_HideSeek1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'black': 'black', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'vis': 'vis', 'centfa': 'centfa', 'distFa': 'distFa', 'sonMax': 'sonMax', 'maxDist': 'maxDist', 'stack': 'stack', 'u': 'u', 'f': 'f', 't': 't', 'e': 'e', 'stacksize': 'stacksize'}
    class Set:
        __java_fields__ = {'addHeap': 'addHeap', 'delHeap': 'delHeap'}
        # addHeap：实例字段，在构造函数中初始化。
        # delHeap：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.addHeap = jnew('PriorityQueue', (lambda a, b: jcall(b, 'compareTo', a)))
            self.delHeap = jnew('PriorityQueue', (lambda a, b: jcall(b, 'compareTo', a)))

        def clean(self):
            while ((not jcall(self.delHeap, 'isEmpty')) and jcall(jcall(self.delHeap, 'peek'), 'equals', jcall(self.addHeap, 'peek'))):
                jcall(self.addHeap, 'poll')
                jcall(self.delHeap, 'poll')

        def popHead(self):
            ans = jcast('int', jcall(self.addHeap, 'poll'))
            self.clean()
            return jcast('int', ans)

        def size(self):
            return jcast('int', jcast('int', (jcall(self.addHeap, 'size') - jcall(self.delHeap, 'size'))))

        def add(self, v):
            v = jcast('int', v)
            jcall(self.addHeap, 'add', v)

        def del_(self, v):
            v = jcast('int', v)
            jcall(self.delHeap, 'add', v)
            self.clean()

        def first(self):
            return jcast('int', jcall(self.addHeap, 'peek'))

        def second(self):
            a = jcast('int', self.popHead())
            b = jcast('int', self.first())
            self.add(a)
            return jcast('int', b)

        def __init__(self, *args, _java_ctor=None):
            self.addHeap = None
            self.delHeap = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_HideSeek1.Set.Set")


    MAXN = 0
    n = 0
    m = 0
    black = None
    head = None
    nxt = None
    to = None
    cntg = 0
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    vis = None
    centfa = None
    # distFa[u] : u的连通区里，每个黑点到上级重心的距离，组成的集合
    # sonMax[u] : u的每个儿子连通区里，都选一个最远的黑点，到u的最大距离，组成的集合
    # 如果u自己是黑点，那么0要加入集合
    # maxDist   : 每个重心在连通区里，选两个最远黑点的最大距离，作为自己的答案，放入全局集合
    distFa = None
    sonMax = None
    maxDist = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    t = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, t, e):
        u = jcast('int', u)
        f = jcast('int', f)
        t = jcast('int', t)
        e = jcast('int', e)
        jset(Code07_HideSeek1.stack[Code07_HideSeek1.stacksize], 0, u)
        jset(Code07_HideSeek1.stack[Code07_HideSeek1.stacksize], 1, f)
        jset(Code07_HideSeek1.stack[Code07_HideSeek1.stacksize], 2, t)
        jset(Code07_HideSeek1.stack[Code07_HideSeek1.stacksize], 3, e)
        Code07_HideSeek1.stacksize = jcast('int', (Code07_HideSeek1.stacksize + 1))

    @staticmethod
    def pop():
        Code07_HideSeek1.stacksize = jcast('int', (Code07_HideSeek1.stacksize - 1))
        Code07_HideSeek1.u = jcast('int', Code07_HideSeek1.stack[Code07_HideSeek1.stacksize][0])
        Code07_HideSeek1.f = jcast('int', Code07_HideSeek1.stack[Code07_HideSeek1.stacksize][1])
        Code07_HideSeek1.t = jcast('int', Code07_HideSeek1.stack[Code07_HideSeek1.stacksize][2])
        Code07_HideSeek1.e = jcast('int', Code07_HideSeek1.stack[Code07_HideSeek1.stacksize][3])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_HideSeek1.nxt, ((_java_obj_1 := Code07_HideSeek1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_HideSeek1.head[u])
        Code07_HideSeek1.to[Code07_HideSeek1.cntg] = jcast('int', v)
        Code07_HideSeek1.head[u] = jcast('int', Code07_HideSeek1.cntg)

    # 重链剖分收集信息递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code07_HideSeek1.fa[u] = jcast('int', f)
        Code07_HideSeek1.dep[u] = jcast('int', jcast('int', jadd(Code07_HideSeek1.dep[f], 1)))
        Code07_HideSeek1.siz[u] = jcast('int', 1)
        e = jcast('int', Code07_HideSeek1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_HideSeek1.to[e])
            if (v != f):
                Code07_HideSeek1.dfs1(v, u)
            e = jcast('int', Code07_HideSeek1.nxt[e])
        ei = jcast('int', Code07_HideSeek1.head[u])
        v = 0
        while (ei > 0):
            v = jcast('int', Code07_HideSeek1.to[ei])
            if (v != f):
                Code07_HideSeek1.siz[u] = jcast('int', jcast('int', jadd(Code07_HideSeek1.siz[u], Code07_HideSeek1.siz[v])))
                if ((Code07_HideSeek1.son[u] == 0) or (Code07_HideSeek1.siz[Code07_HideSeek1.son[u]] < Code07_HideSeek1.siz[v])):
                    Code07_HideSeek1.son[u] = jcast('int', v)
            ei = jcast('int', Code07_HideSeek1.nxt[ei])

    # 根据重儿子剖分的递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code07_HideSeek1.top[u] = jcast('int', t)
        if (Code07_HideSeek1.son[u] == 0):
            return
        Code07_HideSeek1.dfs2(Code07_HideSeek1.son[u], t)
        e = jcast('int', Code07_HideSeek1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_HideSeek1.to[e])
            if ((v != Code07_HideSeek1.fa[u]) and (v != Code07_HideSeek1.son[u])):
                Code07_HideSeek1.dfs2(v, v)
            e = jcast('int', Code07_HideSeek1.nxt[e])

    # dfs1改成迭代版
    @staticmethod
    def dfs3(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code07_HideSeek1.stacksize = jcast('int', 0)
        Code07_HideSeek1.push(cur, father, 0, jcast('int', (-1)))
        while (Code07_HideSeek1.stacksize > 0):
            Code07_HideSeek1.pop()
            if (Code07_HideSeek1.e == jcast('int', (-1))):
                Code07_HideSeek1.fa[Code07_HideSeek1.u] = jcast('int', Code07_HideSeek1.f)
                Code07_HideSeek1.dep[Code07_HideSeek1.u] = jcast('int', jcast('int', jadd(Code07_HideSeek1.dep[Code07_HideSeek1.f], 1)))
                Code07_HideSeek1.siz[Code07_HideSeek1.u] = jcast('int', 1)
                Code07_HideSeek1.e = jcast('int', Code07_HideSeek1.head[Code07_HideSeek1.u])
            else:
                Code07_HideSeek1.e = jcast('int', Code07_HideSeek1.nxt[Code07_HideSeek1.e])
            if (Code07_HideSeek1.e != 0):
                Code07_HideSeek1.push(Code07_HideSeek1.u, Code07_HideSeek1.f, 0, Code07_HideSeek1.e)
                v = jcast('int', Code07_HideSeek1.to[Code07_HideSeek1.e])
                if (v != Code07_HideSeek1.f):
                    Code07_HideSeek1.push(v, Code07_HideSeek1.u, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code07_HideSeek1.head[Code07_HideSeek1.u])
                while (ei > 0):
                    v = jcast('int', Code07_HideSeek1.to[ei])
                    if (v != Code07_HideSeek1.f):
                        Code07_HideSeek1.siz[Code07_HideSeek1.u] = jcast('int', jcast('int', jadd(Code07_HideSeek1.siz[Code07_HideSeek1.u], Code07_HideSeek1.siz[v])))
                        if ((Code07_HideSeek1.son[Code07_HideSeek1.u] == 0) or (Code07_HideSeek1.siz[Code07_HideSeek1.son[Code07_HideSeek1.u]] < Code07_HideSeek1.siz[v])):
                            Code07_HideSeek1.son[Code07_HideSeek1.u] = jcast('int', v)
                    ei = jcast('int', Code07_HideSeek1.nxt[ei])

    # dfs2改成迭代版
    @staticmethod
    def dfs4(cur, tag):
        cur = jcast('int', cur)
        tag = jcast('int', tag)
        Code07_HideSeek1.stacksize = jcast('int', 0)
        Code07_HideSeek1.push(cur, 0, tag, jcast('int', (-1)))
        while (Code07_HideSeek1.stacksize > 0):
            try:
                Code07_HideSeek1.pop()
                if (Code07_HideSeek1.e == jcast('int', (-1))):
                    Code07_HideSeek1.top[Code07_HideSeek1.u] = jcast('int', Code07_HideSeek1.t)
                    if (Code07_HideSeek1.son[Code07_HideSeek1.u] == 0):
                        raise JContinue(None)
                    Code07_HideSeek1.push(Code07_HideSeek1.u, 0, Code07_HideSeek1.t, jcast('int', (-2)))
                    Code07_HideSeek1.push(Code07_HideSeek1.son[Code07_HideSeek1.u], 0, Code07_HideSeek1.t, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code07_HideSeek1.e == jcast('int', (-2))):
                        Code07_HideSeek1.e = jcast('int', Code07_HideSeek1.head[Code07_HideSeek1.u])
                    else:
                        Code07_HideSeek1.e = jcast('int', Code07_HideSeek1.nxt[Code07_HideSeek1.e])
                if (Code07_HideSeek1.e != 0):
                    Code07_HideSeek1.push(Code07_HideSeek1.u, 0, Code07_HideSeek1.t, Code07_HideSeek1.e)
                    v = jcast('int', Code07_HideSeek1.to[Code07_HideSeek1.e])
                    if ((v != Code07_HideSeek1.fa[Code07_HideSeek1.u]) and (v != Code07_HideSeek1.son[Code07_HideSeek1.u])):
                        Code07_HideSeek1.push(v, 0, v, jcast('int', (-1)))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    # 找重心需要计算子树大小的递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code07_HideSeek1.siz[u] = jcast('int', 1)
        e = jcast('int', Code07_HideSeek1.head[u])
        while (e > 0):
            v = jcast('int', Code07_HideSeek1.to[e])
            if ((v != fa) and (not Code07_HideSeek1.vis[v])):
                Code07_HideSeek1.getSize1(v, u)
                Code07_HideSeek1.siz[u] = jcast('int', jcast('int', jadd(Code07_HideSeek1.siz[u], Code07_HideSeek1.siz[v])))
            e = jcast('int', Code07_HideSeek1.nxt[e])

    # getSize1的迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code07_HideSeek1.stacksize = jcast('int', 0)
        Code07_HideSeek1.push(cur, fa, 0, jcast('int', (-1)))
        while (Code07_HideSeek1.stacksize > 0):
            Code07_HideSeek1.pop()
            if (Code07_HideSeek1.e == jcast('int', (-1))):
                Code07_HideSeek1.siz[Code07_HideSeek1.u] = jcast('int', 1)
                Code07_HideSeek1.e = jcast('int', Code07_HideSeek1.head[Code07_HideSeek1.u])
            else:
                Code07_HideSeek1.e = jcast('int', Code07_HideSeek1.nxt[Code07_HideSeek1.e])
            if (Code07_HideSeek1.e != 0):
                Code07_HideSeek1.push(Code07_HideSeek1.u, Code07_HideSeek1.f, 0, Code07_HideSeek1.e)
                v = jcast('int', Code07_HideSeek1.to[Code07_HideSeek1.e])
                if ((v != Code07_HideSeek1.f) and (not Code07_HideSeek1.vis[v])):
                    Code07_HideSeek1.push(v, Code07_HideSeek1.u, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code07_HideSeek1.head[Code07_HideSeek1.u])
                while (ei > 0):
                    v = jcast('int', Code07_HideSeek1.to[ei])
                    if ((v != Code07_HideSeek1.f) and (not Code07_HideSeek1.vis[v])):
                        Code07_HideSeek1.siz[Code07_HideSeek1.u] = jcast('int', jcast('int', jadd(Code07_HideSeek1.siz[Code07_HideSeek1.u], Code07_HideSeek1.siz[v])))
                    ei = jcast('int', Code07_HideSeek1.nxt[ei])

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        while (Code07_HideSeek1.top[a] != Code07_HideSeek1.top[b]):
            if (Code07_HideSeek1.dep[Code07_HideSeek1.top[a]] <= Code07_HideSeek1.dep[Code07_HideSeek1.top[b]]):
                b = jcast('int', Code07_HideSeek1.fa[Code07_HideSeek1.top[b]])
            else:
                a = jcast('int', Code07_HideSeek1.fa[Code07_HideSeek1.top[a]])
        return jcast('int', (a if (Code07_HideSeek1.dep[a] <= Code07_HideSeek1.dep[b]) else b))

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code07_HideSeek1.dep[x], Code07_HideSeek1.dep[y])) - jcast('int', (Code07_HideSeek1.dep[Code07_HideSeek1.getLca(x, y)] << (1 & 31))))))

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code07_HideSeek1.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code07_HideSeek1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code07_HideSeek1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code07_HideSeek1.to[e])
                        if (((v != fa) and (not Code07_HideSeek1.vis[v])) and (Code07_HideSeek1.siz[v] > half)):
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
                    e = jcast('int', Code07_HideSeek1.nxt[e])
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
        Code07_HideSeek1.centfa[u] = jcast('int', fa)
        Code07_HideSeek1.vis[u] = jcast('boolean', True)
        e = jcast('int', Code07_HideSeek1.head[u])
        while (e > 0):
            v = jcast('int', Code07_HideSeek1.to[e])
            if (not Code07_HideSeek1.vis[v]):
                Code07_HideSeek1.centroidTree(Code07_HideSeek1.getCentroid(v, u), u)
            e = jcast('int', Code07_HideSeek1.nxt[e])

    @staticmethod
    def addAns(x):
        x = jcast('int', x)
        if (jcall(Code07_HideSeek1.sonMax[x], 'size') >= 2):
            jcall(Code07_HideSeek1.maxDist, 'add', jcast('int', jadd(jcall(Code07_HideSeek1.sonMax[x], 'first'), jcall(Code07_HideSeek1.sonMax[x], 'second'))))

    @staticmethod
    def delAns(x):
        x = jcast('int', x)
        if (jcall(Code07_HideSeek1.sonMax[x], 'size') >= 2):
            jcall(Code07_HideSeek1.maxDist, 'del_', jcast('int', jadd(jcall(Code07_HideSeek1.sonMax[x], 'first'), jcall(Code07_HideSeek1.sonMax[x], 'second'))))

    @staticmethod
    def on(x):
        x = jcast('int', x)
        Code07_HideSeek1.delAns(x)
        jcall(Code07_HideSeek1.sonMax[x], 'del_', 0)
        Code07_HideSeek1.addAns(x)
        u = jcast('int', x)
        fa = jcast('int', Code07_HideSeek1.centfa[u])
        while (fa > 0):
            Code07_HideSeek1.delAns(fa)
            jcall(Code07_HideSeek1.sonMax[fa], 'del_', jcall(Code07_HideSeek1.distFa[u], 'first'))
            jcall(Code07_HideSeek1.distFa[u], 'del_', Code07_HideSeek1.getDist(x, fa))
            if (jcall(Code07_HideSeek1.distFa[u], 'size') > 0):
                jcall(Code07_HideSeek1.sonMax[fa], 'add', jcall(Code07_HideSeek1.distFa[u], 'first'))
            Code07_HideSeek1.addAns(fa)
            u = jcast('int', fa)
            fa = jcast('int', Code07_HideSeek1.centfa[u])

    @staticmethod
    def off(x):
        x = jcast('int', x)
        Code07_HideSeek1.delAns(x)
        jcall(Code07_HideSeek1.sonMax[x], 'add', 0)
        Code07_HideSeek1.addAns(x)
        u = jcast('int', x)
        fa = jcast('int', Code07_HideSeek1.centfa[u])
        while (fa > 0):
            Code07_HideSeek1.delAns(fa)
            if (jcall(Code07_HideSeek1.distFa[u], 'size') > 0):
                jcall(Code07_HideSeek1.sonMax[fa], 'del_', jcall(Code07_HideSeek1.distFa[u], 'first'))
            jcall(Code07_HideSeek1.distFa[u], 'add', Code07_HideSeek1.getDist(x, fa))
            jcall(Code07_HideSeek1.sonMax[fa], 'add', jcall(Code07_HideSeek1.distFa[u], 'first'))
            Code07_HideSeek1.addAns(fa)
            u = jcast('int', fa)
            fa = jcast('int', Code07_HideSeek1.centfa[u])

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_HideSeek1.n):
            Code07_HideSeek1.black[i] = jcast('boolean', True)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_HideSeek1.n):
            jset(Code07_HideSeek1.distFa, i, Code07_HideSeek1.Set(_java_ctor=0))
            jset(Code07_HideSeek1.sonMax, i, Code07_HideSeek1.Set(_java_ctor=0))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_HideSeek1.n):
            u = jcast('int', i)
            fa = jcast('int', Code07_HideSeek1.centfa[u])
            while (fa > 0):
                jcall(Code07_HideSeek1.distFa[u], 'add', Code07_HideSeek1.getDist(i, fa))
                u = jcast('int', fa)
                fa = jcast('int', Code07_HideSeek1.centfa[u])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_HideSeek1.n):
            jcall(Code07_HideSeek1.sonMax[i], 'add', 0)
            if (Code07_HideSeek1.centfa[i] > 0):
                jcall(Code07_HideSeek1.sonMax[Code07_HideSeek1.centfa[i]], 'add', jcall(Code07_HideSeek1.distFa[i], 'first'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_HideSeek1.n):
            Code07_HideSeek1.addAns(i)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_HideSeek1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_HideSeek1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_HideSeek1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code07_HideSeek1.addEdge(u, v)
            Code07_HideSeek1.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        # dfs2(1, 1);
        Code07_HideSeek1.dfs3(1, 0)
        Code07_HideSeek1.dfs4(1, 1)
        Code07_HideSeek1.centroidTree(Code07_HideSeek1.getCentroid(1, 0), 0)
        Code07_HideSeek1.prepare()
        Code07_HideSeek1.m = jcast('int', jcall(in_, 'nextInt'))
        blackCnt = jcast('int', Code07_HideSeek1.n)
        op = jchar(0)
        i = jcast('int', 1)
        x = 0
        while (i <= Code07_HideSeek1.m):
            op = jcast('char', jcall(in_, 'nextChar'))
            if (op == jchar('C')):
                x = jcast('int', jcall(in_, 'nextInt'))
                Code07_HideSeek1.black[x] = jcast('boolean', (not Code07_HideSeek1.black[x]))
                if Code07_HideSeek1.black[x]:
                    Code07_HideSeek1.off(x)
                    blackCnt = jcast('int', (blackCnt + 1))
                else:
                    Code07_HideSeek1.on(x)
                    blackCnt = jcast('int', (blackCnt - 1))
            else:
                if (blackCnt <= 1):
                    jcall(out, 'println', jcast('int', (blackCnt - 1)))
                else:
                    jcall(out, 'println', jcall(Code07_HideSeek1.maxDist, 'first'))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_HideSeek1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_HideSeek1.MAXN = jcast('int', 100001)
Code07_HideSeek1.n = jcast('int', 0)
Code07_HideSeek1.m = jcast('int', 0)
Code07_HideSeek1.black = jarray('boolean', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.head = jarray('int', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.nxt = jarray('int', [jcast('int', (Code07_HideSeek1.MAXN << (1 & 31)))])
Code07_HideSeek1.to = jarray('int', [jcast('int', (Code07_HideSeek1.MAXN << (1 & 31)))])
Code07_HideSeek1.cntg = jcast('int', 0)
Code07_HideSeek1.fa = jarray('int', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.dep = jarray('int', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.siz = jarray('int', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.son = jarray('int', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.top = jarray('int', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.vis = jarray('boolean', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.centfa = jarray('int', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.distFa = jarray('Set', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.sonMax = jarray('Set', [Code07_HideSeek1.MAXN])
Code07_HideSeek1.maxDist = Code07_HideSeek1.Set(_java_ctor=0)
Code07_HideSeek1.stack = jarray('int', [Code07_HideSeek1.MAXN, 4])
Code07_HideSeek1.u = jcast('int', 0)
Code07_HideSeek1.f = jcast('int', 0)
Code07_HideSeek1.t = jcast('int', 0)
Code07_HideSeek1.e = jcast('int', 0)
Code07_HideSeek1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code07_HideSeek1.main([])
