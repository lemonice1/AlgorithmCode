# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树点涂色，Python版
# 一共n个节点，所有节点组成一棵树，规定1号节点是根
# 初始所有节点的颜色都不同，路径中的颜色数量叫做路径权值
# 接下来有m条操作，操作有三种类型，具体格式如下
# 操作 1 x   : 根到点x的路径上，所有点染上一种没有用过的新颜色
# 操作 2 x y : 查询点x到点y的路径权值
# 操作 3 x   : x为头的子树中选择一个点，希望该点到根节点的路径权值最大，打印这个值
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3703
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_TreeDyeing2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'pa': 'pa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'seg': 'seg', 'cntd': 'cntd', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'mostl': 'mostl', 'maxVal': 'maxVal', 'addTag': 'addTag', 'stau': 'stau', 'staf': 'staf', 'stat': 'stat', 'stae': 'stae', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 't': 't', 'e': 'e'}
    MAXN = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    # 树链剖分
    pa = None
    dep = None
    siz = None
    son = None
    top = None
    dfn = None
    seg = None
    cntd = 0
    # 辅助splay
    fa = None
    ls = None
    rs = None
    mostl = None
    # 线段树
    maxVal = None
    addTag = None
    # 递归改迭代需要的栈
    stau = None
    staf = None
    stat = None
    stae = None
    stacksize = 0
    u = 0
    f = 0
    t = 0
    e = 0
    @staticmethod
    def push(u, f, t, e):
        u = jcast('int', u)
        f = jcast('int', f)
        t = jcast('int', t)
        e = jcast('int', e)
        Code04_TreeDyeing2.stau[Code04_TreeDyeing2.stacksize] = jcast('int', u)
        Code04_TreeDyeing2.staf[Code04_TreeDyeing2.stacksize] = jcast('int', f)
        Code04_TreeDyeing2.stat[Code04_TreeDyeing2.stacksize] = jcast('int', t)
        Code04_TreeDyeing2.stae[Code04_TreeDyeing2.stacksize] = jcast('int', e)
        Code04_TreeDyeing2.stacksize = jcast('int', (Code04_TreeDyeing2.stacksize + 1))

    @staticmethod
    def pop():
        Code04_TreeDyeing2.stacksize = jcast('int', (Code04_TreeDyeing2.stacksize - 1))
        Code04_TreeDyeing2.u = jcast('int', Code04_TreeDyeing2.stau[Code04_TreeDyeing2.stacksize])
        Code04_TreeDyeing2.f = jcast('int', Code04_TreeDyeing2.staf[Code04_TreeDyeing2.stacksize])
        Code04_TreeDyeing2.t = jcast('int', Code04_TreeDyeing2.stat[Code04_TreeDyeing2.stacksize])
        Code04_TreeDyeing2.e = jcast('int', Code04_TreeDyeing2.stae[Code04_TreeDyeing2.stacksize])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_TreeDyeing2.nxt, ((_java_obj_1 := Code04_TreeDyeing2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_TreeDyeing2.head[u])
        Code04_TreeDyeing2.to[Code04_TreeDyeing2.cntg] = jcast('int', v)
        Code04_TreeDyeing2.head[u] = jcast('int', Code04_TreeDyeing2.cntg)

    # 递归版
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code04_TreeDyeing2.pa[u] = jcast('int', f)
        Code04_TreeDyeing2.dep[u] = jcast('int', jcast('int', jadd(Code04_TreeDyeing2.dep[f], 1)))
        Code04_TreeDyeing2.siz[u] = jcast('int', 1)
        e = jcast('int', Code04_TreeDyeing2.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code04_TreeDyeing2.to[e])
            if (v != f):
                Code04_TreeDyeing2.dfs1(v, u)
                Code04_TreeDyeing2.siz[u] = jcast('int', jcast('int', jadd(Code04_TreeDyeing2.siz[u], Code04_TreeDyeing2.siz[v])))
                if (Code04_TreeDyeing2.siz[v] > Code04_TreeDyeing2.siz[Code04_TreeDyeing2.son[u]]):
                    Code04_TreeDyeing2.son[u] = jcast('int', v)
            e = jcast('int', Code04_TreeDyeing2.nxt[e])

    # 递归版
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code04_TreeDyeing2.top[u] = jcast('int', t)
        jset(Code04_TreeDyeing2.dfn, u, ((_java_obj_4 := Code04_TreeDyeing2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code04_TreeDyeing2.seg[Code04_TreeDyeing2.cntd] = jcast('int', u)
        if (Code04_TreeDyeing2.son[u] != 0):
            Code04_TreeDyeing2.dfs2(Code04_TreeDyeing2.son[u], t)
        e = jcast('int', Code04_TreeDyeing2.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code04_TreeDyeing2.to[e])
            if ((v != Code04_TreeDyeing2.pa[u]) and (v != Code04_TreeDyeing2.son[u])):
                Code04_TreeDyeing2.dfs2(v, v)
            e = jcast('int', Code04_TreeDyeing2.nxt[e])

    # 树剖dfs1的迭代版
    @staticmethod
    def dfs3(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code04_TreeDyeing2.stacksize = jcast('int', 0)
        Code04_TreeDyeing2.push(cur, father, 0, jcast('int', (-1)))
        while (Code04_TreeDyeing2.stacksize > 0):
            Code04_TreeDyeing2.pop()
            if (Code04_TreeDyeing2.e == jcast('int', (-1))):
                Code04_TreeDyeing2.pa[Code04_TreeDyeing2.u] = jcast('int', Code04_TreeDyeing2.f)
                Code04_TreeDyeing2.dep[Code04_TreeDyeing2.u] = jcast('int', jcast('int', jadd(Code04_TreeDyeing2.dep[Code04_TreeDyeing2.f], 1)))
                Code04_TreeDyeing2.siz[Code04_TreeDyeing2.u] = jcast('int', 1)
                Code04_TreeDyeing2.e = jcast('int', Code04_TreeDyeing2.head[Code04_TreeDyeing2.u])
            else:
                Code04_TreeDyeing2.e = jcast('int', Code04_TreeDyeing2.nxt[Code04_TreeDyeing2.e])
            if (Code04_TreeDyeing2.e != 0):
                Code04_TreeDyeing2.push(Code04_TreeDyeing2.u, Code04_TreeDyeing2.f, 0, Code04_TreeDyeing2.e)
                if (Code04_TreeDyeing2.to[Code04_TreeDyeing2.e] != Code04_TreeDyeing2.f):
                    Code04_TreeDyeing2.push(Code04_TreeDyeing2.to[Code04_TreeDyeing2.e], Code04_TreeDyeing2.u, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code04_TreeDyeing2.head[Code04_TreeDyeing2.u])
                v = 0
                while (ei != 0):
                    v = jcast('int', Code04_TreeDyeing2.to[ei])
                    if (v != Code04_TreeDyeing2.f):
                        Code04_TreeDyeing2.siz[Code04_TreeDyeing2.u] = jcast('int', jcast('int', jadd(Code04_TreeDyeing2.siz[Code04_TreeDyeing2.u], Code04_TreeDyeing2.siz[v])))
                        if (Code04_TreeDyeing2.siz[v] > Code04_TreeDyeing2.siz[Code04_TreeDyeing2.son[Code04_TreeDyeing2.u]]):
                            Code04_TreeDyeing2.son[Code04_TreeDyeing2.u] = jcast('int', v)
                    ei = jcast('int', Code04_TreeDyeing2.nxt[ei])

    # 树剖dfs2的迭代版
    @staticmethod
    def dfs4(cur, curt):
        cur = jcast('int', cur)
        curt = jcast('int', curt)
        Code04_TreeDyeing2.stacksize = jcast('int', 0)
        Code04_TreeDyeing2.push(cur, 0, curt, jcast('int', (-1)))
        while (Code04_TreeDyeing2.stacksize > 0):
            try:
                Code04_TreeDyeing2.pop()
                if (Code04_TreeDyeing2.e == jcast('int', (-1))):
                    Code04_TreeDyeing2.top[Code04_TreeDyeing2.u] = jcast('int', Code04_TreeDyeing2.t)
                    jset(Code04_TreeDyeing2.dfn, Code04_TreeDyeing2.u, ((_java_obj_8 := Code04_TreeDyeing2), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    Code04_TreeDyeing2.seg[Code04_TreeDyeing2.cntd] = jcast('int', Code04_TreeDyeing2.u)
                    if (Code04_TreeDyeing2.son[Code04_TreeDyeing2.u] != 0):
                        Code04_TreeDyeing2.push(Code04_TreeDyeing2.u, 0, Code04_TreeDyeing2.t, jcast('int', (-2)))
                        Code04_TreeDyeing2.push(Code04_TreeDyeing2.son[Code04_TreeDyeing2.u], 0, Code04_TreeDyeing2.t, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code04_TreeDyeing2.e == jcast('int', (-2))):
                        Code04_TreeDyeing2.e = jcast('int', Code04_TreeDyeing2.head[Code04_TreeDyeing2.u])
                    else:
                        Code04_TreeDyeing2.e = jcast('int', Code04_TreeDyeing2.nxt[Code04_TreeDyeing2.e])
                if (Code04_TreeDyeing2.e != 0):
                    Code04_TreeDyeing2.push(Code04_TreeDyeing2.u, 0, Code04_TreeDyeing2.t, Code04_TreeDyeing2.e)
                    if ((Code04_TreeDyeing2.to[Code04_TreeDyeing2.e] != Code04_TreeDyeing2.pa[Code04_TreeDyeing2.u]) and (Code04_TreeDyeing2.to[Code04_TreeDyeing2.e] != Code04_TreeDyeing2.son[Code04_TreeDyeing2.u])):
                        Code04_TreeDyeing2.push(Code04_TreeDyeing2.to[Code04_TreeDyeing2.e], 0, Code04_TreeDyeing2.to[Code04_TreeDyeing2.e], jcast('int', (-1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def lca(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        while (Code04_TreeDyeing2.top[x] != Code04_TreeDyeing2.top[y]):
            if (Code04_TreeDyeing2.dep[Code04_TreeDyeing2.top[x]] < Code04_TreeDyeing2.dep[Code04_TreeDyeing2.top[y]]):
                y = jcast('int', Code04_TreeDyeing2.pa[Code04_TreeDyeing2.top[y]])
            else:
                x = jcast('int', Code04_TreeDyeing2.pa[Code04_TreeDyeing2.top[x]])
        return jcast('int', (x if (Code04_TreeDyeing2.dep[x] < Code04_TreeDyeing2.dep[y]) else y))

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code04_TreeDyeing2.mostl[x] = jcast('int', (x if (Code04_TreeDyeing2.ls[x] == 0) else Code04_TreeDyeing2.mostl[Code04_TreeDyeing2.ls[x]]))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code04_TreeDyeing2.ls[Code04_TreeDyeing2.fa[x]] != x) and (Code04_TreeDyeing2.rs[Code04_TreeDyeing2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code04_TreeDyeing2.ls[Code04_TreeDyeing2.fa[x]] == x) else 1))

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code04_TreeDyeing2.fa[x])
        g = jcast('int', Code04_TreeDyeing2.fa[f])
        if (Code04_TreeDyeing2.lr(x) == 0):
            Code04_TreeDyeing2.ls[f] = jcast('int', Code04_TreeDyeing2.rs[x])
            if (Code04_TreeDyeing2.ls[f] != 0):
                jset(Code04_TreeDyeing2.fa, Code04_TreeDyeing2.ls[f], f)
            Code04_TreeDyeing2.rs[x] = jcast('int', f)
        else:
            Code04_TreeDyeing2.rs[f] = jcast('int', Code04_TreeDyeing2.ls[x])
            if (Code04_TreeDyeing2.rs[f] != 0):
                jset(Code04_TreeDyeing2.fa, Code04_TreeDyeing2.rs[f], f)
            Code04_TreeDyeing2.ls[x] = jcast('int', f)
        if (not Code04_TreeDyeing2.isroot(f)):
            if (Code04_TreeDyeing2.lr(f) == 0):
                Code04_TreeDyeing2.ls[g] = jcast('int', x)
            else:
                Code04_TreeDyeing2.rs[g] = jcast('int', x)
        Code04_TreeDyeing2.fa[f] = jcast('int', x)
        Code04_TreeDyeing2.fa[x] = jcast('int', g)
        Code04_TreeDyeing2.up(f)
        Code04_TreeDyeing2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        while (not Code04_TreeDyeing2.isroot(x)):
            f = jcast('int', Code04_TreeDyeing2.fa[x])
            if (not Code04_TreeDyeing2.isroot(f)):
                if (Code04_TreeDyeing2.lr(x) == Code04_TreeDyeing2.lr(f)):
                    Code04_TreeDyeing2.rotate(f)
                else:
                    Code04_TreeDyeing2.rotate(x)
            Code04_TreeDyeing2.rotate(x)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code04_TreeDyeing2.maxVal[i] = jcast('int', Code04_TreeDyeing2.dep[Code04_TreeDyeing2.seg[l]])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_TreeDyeing2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code04_TreeDyeing2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_TreeDyeing2.upSeg(i)

    @staticmethod
    def upSeg(i):
        i = jcast('int', i)
        jset(Code04_TreeDyeing2.maxVal, i, jstatic('Math', 'max', Code04_TreeDyeing2.maxVal[jcast('int', (i << (1 & 31)))], Code04_TreeDyeing2.maxVal[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code04_TreeDyeing2.maxVal[i] = jcast('int', jcast('int', jadd(Code04_TreeDyeing2.maxVal[i], v)))
        Code04_TreeDyeing2.addTag[i] = jcast('int', jcast('int', jadd(Code04_TreeDyeing2.addTag[i], v)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code04_TreeDyeing2.addTag[i] != 0):
            Code04_TreeDyeing2.lazy(jcast('int', (i << (1 & 31))), Code04_TreeDyeing2.addTag[i])
            Code04_TreeDyeing2.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code04_TreeDyeing2.addTag[i])
            Code04_TreeDyeing2.addTag[i] = jcast('int', 0)

    @staticmethod
    def _java_add_0(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code04_TreeDyeing2.lazy(i, jobv)
        else:
            Code04_TreeDyeing2.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code04_TreeDyeing2._java_add_0(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_TreeDyeing2._java_add_0(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_TreeDyeing2.upSeg(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code04_TreeDyeing2.maxVal[i])
        Code04_TreeDyeing2.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code04_TreeDyeing2.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code04_TreeDyeing2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    # 以x为根的原树子树中，所有点的点权加上v
    @staticmethod
    def _java_add_1(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        Code04_TreeDyeing2._java_add_0(Code04_TreeDyeing2.dfn[x], jcast('int', (jcast('int', jadd(Code04_TreeDyeing2.dfn[x], Code04_TreeDyeing2.siz[x])) - 1)), v, 1, Code04_TreeDyeing2.n, 1)

    # 根节点到x的路径，涂新颜色，改写access方法
    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code04_TreeDyeing2.splay(x)
            if (Code04_TreeDyeing2.rs[x] != 0):
                Code04_TreeDyeing2._java_add_1(Code04_TreeDyeing2.mostl[Code04_TreeDyeing2.rs[x]], 1)
            if (y != 0):
                Code04_TreeDyeing2._java_add_1(Code04_TreeDyeing2.mostl[y], jcast('int', (-1)))
            Code04_TreeDyeing2.rs[x] = jcast('int', y)
            Code04_TreeDyeing2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code04_TreeDyeing2.fa[x])

    @staticmethod
    def pathQuery(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        xylca = jcast('int', Code04_TreeDyeing2.lca(x, y))
        a = jcast('int', Code04_TreeDyeing2.query(Code04_TreeDyeing2.dfn[x], Code04_TreeDyeing2.dfn[x], 1, Code04_TreeDyeing2.n, 1))
        b = jcast('int', Code04_TreeDyeing2.query(Code04_TreeDyeing2.dfn[y], Code04_TreeDyeing2.dfn[y], 1, Code04_TreeDyeing2.n, 1))
        c = jcast('int', Code04_TreeDyeing2.query(Code04_TreeDyeing2.dfn[xylca], Code04_TreeDyeing2.dfn[xylca], 1, Code04_TreeDyeing2.n, 1))
        return jcast('int', jcast('int', jadd(jcast('int', (jcast('int', jadd(a, b)) - jcast('int', (2 * c)))), 1)))

    @staticmethod
    def subtreeQuery(x):
        x = jcast('int', x)
        return jcast('int', Code04_TreeDyeing2.query(Code04_TreeDyeing2.dfn[x], jcast('int', (jcast('int', jadd(Code04_TreeDyeing2.dfn[x], Code04_TreeDyeing2.siz[x])) - 1)), 1, Code04_TreeDyeing2.n, 1))

    @staticmethod
    def main(args):
        in_ = Code04_TreeDyeing2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_TreeDyeing2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_TreeDyeing2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i < Code04_TreeDyeing2.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code04_TreeDyeing2.addEdge(x, y)
            Code04_TreeDyeing2.addEdge(y, x)
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        # dfs2(1, 1);
        Code04_TreeDyeing2.dfs3(1, 0)
        Code04_TreeDyeing2.dfs4(1, 1)
        Code04_TreeDyeing2.build(1, Code04_TreeDyeing2.n, 1)
        i = jcast('int', 1)
        while (i <= Code04_TreeDyeing2.n):
            Code04_TreeDyeing2.fa[i] = jcast('int', Code04_TreeDyeing2.pa[i])
            Code04_TreeDyeing2.mostl[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code04_TreeDyeing2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                Code04_TreeDyeing2.access(x)
            else:
                if (op == 2):
                    y = jcast('int', jcall(in_, 'nextInt'))
                    jcall(out, 'println', Code04_TreeDyeing2.pathQuery(x, y))
                else:
                    jcall(out, 'println', Code04_TreeDyeing2.subtreeQuery(x))
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code04_TreeDyeing2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int', 'int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code04_TreeDyeing2._java_add_0(*args)
        if _java_choice == 1:
            return Code04_TreeDyeing2._java_add_1(*args)
        raise TypeError("No matching overload for Code04_TreeDyeing2.add")


Code04_TreeDyeing2.MAXN = jcast('int', 100001)
Code04_TreeDyeing2.n = jcast('int', 0)
Code04_TreeDyeing2.m = jcast('int', 0)
Code04_TreeDyeing2.head = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.nxt = jarray('int', [jcast('int', (Code04_TreeDyeing2.MAXN << (1 & 31)))])
Code04_TreeDyeing2.to = jarray('int', [jcast('int', (Code04_TreeDyeing2.MAXN << (1 & 31)))])
Code04_TreeDyeing2.cntg = jcast('int', 0)
Code04_TreeDyeing2.pa = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.dep = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.siz = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.son = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.top = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.dfn = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.seg = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.cntd = jcast('int', 0)
Code04_TreeDyeing2.fa = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.ls = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.rs = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.mostl = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.maxVal = jarray('int', [jcast('int', (Code04_TreeDyeing2.MAXN << (2 & 31)))])
Code04_TreeDyeing2.addTag = jarray('int', [jcast('int', (Code04_TreeDyeing2.MAXN << (2 & 31)))])
Code04_TreeDyeing2.stau = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.staf = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.stat = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.stae = jarray('int', [Code04_TreeDyeing2.MAXN])
Code04_TreeDyeing2.stacksize = jcast('int', 0)
Code04_TreeDyeing2.u = jcast('int', 0)
Code04_TreeDyeing2.f = jcast('int', 0)
Code04_TreeDyeing2.t = jcast('int', 0)
Code04_TreeDyeing2.e = jcast('int', 0)

if __name__ == '__main__':
    Code04_TreeDyeing2.main([])
