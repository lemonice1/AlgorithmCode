# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 震波，Python版
# 树上有n个点，每个点有点权，给定n-1条边，边权都是1
# 接下来有m条操作，每条操作是如下两种类型中的一种
# 操作 0 x y : 点x出发，距离<=y的所有点，打印点权累加和
# 操作 1 x y : 点x的点权变成y
# 1 <= n、m <= 10^5
# 1 <= 点权 <= 10^4
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P6329
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Wave2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'vis': 'vis', 'centfa': 'centfa', 'addTree': 'addTree', 'minusTree': 'minusTree', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'cntt': 'cntt', 'stack': 'stack', 'u': 'u', 'f': 'f', 't': 't', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    arr = None
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
    addTree = None
    minusTree = None
    ls = None
    rs = None
    sum = None
    cntt = 0
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
        jset(Code01_Wave2.stack[Code01_Wave2.stacksize], 0, u)
        jset(Code01_Wave2.stack[Code01_Wave2.stacksize], 1, f)
        jset(Code01_Wave2.stack[Code01_Wave2.stacksize], 2, t)
        jset(Code01_Wave2.stack[Code01_Wave2.stacksize], 3, e)
        Code01_Wave2.stacksize = jcast('int', (Code01_Wave2.stacksize + 1))

    @staticmethod
    def pop():
        Code01_Wave2.stacksize = jcast('int', (Code01_Wave2.stacksize - 1))
        Code01_Wave2.u = jcast('int', Code01_Wave2.stack[Code01_Wave2.stacksize][0])
        Code01_Wave2.f = jcast('int', Code01_Wave2.stack[Code01_Wave2.stacksize][1])
        Code01_Wave2.t = jcast('int', Code01_Wave2.stack[Code01_Wave2.stacksize][2])
        Code01_Wave2.e = jcast('int', Code01_Wave2.stack[Code01_Wave2.stacksize][3])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_Wave2.nxt, ((_java_obj_1 := Code01_Wave2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_Wave2.head[u])
        Code01_Wave2.to[Code01_Wave2.cntg] = jcast('int', v)
        Code01_Wave2.head[u] = jcast('int', Code01_Wave2.cntg)

    # 重链剖分收集信息递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code01_Wave2.fa[u] = jcast('int', f)
        Code01_Wave2.dep[u] = jcast('int', jcast('int', jadd(Code01_Wave2.dep[f], 1)))
        Code01_Wave2.siz[u] = jcast('int', 1)
        e = jcast('int', Code01_Wave2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_Wave2.to[e])
            if (v != f):
                Code01_Wave2.dfs1(v, u)
            e = jcast('int', Code01_Wave2.nxt[e])
        ei = jcast('int', Code01_Wave2.head[u])
        v = 0
        while (ei > 0):
            v = jcast('int', Code01_Wave2.to[ei])
            if (v != f):
                Code01_Wave2.siz[u] = jcast('int', jcast('int', jadd(Code01_Wave2.siz[u], Code01_Wave2.siz[v])))
                if ((Code01_Wave2.son[u] == 0) or (Code01_Wave2.siz[Code01_Wave2.son[u]] < Code01_Wave2.siz[v])):
                    Code01_Wave2.son[u] = jcast('int', v)
            ei = jcast('int', Code01_Wave2.nxt[ei])

    # 根据重儿子剖分的递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code01_Wave2.top[u] = jcast('int', t)
        if (Code01_Wave2.son[u] == 0):
            return
        Code01_Wave2.dfs2(Code01_Wave2.son[u], t)
        e = jcast('int', Code01_Wave2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_Wave2.to[e])
            if ((v != Code01_Wave2.fa[u]) and (v != Code01_Wave2.son[u])):
                Code01_Wave2.dfs2(v, v)
            e = jcast('int', Code01_Wave2.nxt[e])

    # dfs1改成迭代版
    @staticmethod
    def dfs3(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code01_Wave2.stacksize = jcast('int', 0)
        Code01_Wave2.push(cur, father, 0, jcast('int', (-1)))
        while (Code01_Wave2.stacksize > 0):
            Code01_Wave2.pop()
            if (Code01_Wave2.e == jcast('int', (-1))):
                Code01_Wave2.fa[Code01_Wave2.u] = jcast('int', Code01_Wave2.f)
                Code01_Wave2.dep[Code01_Wave2.u] = jcast('int', jcast('int', jadd(Code01_Wave2.dep[Code01_Wave2.f], 1)))
                Code01_Wave2.siz[Code01_Wave2.u] = jcast('int', 1)
                Code01_Wave2.e = jcast('int', Code01_Wave2.head[Code01_Wave2.u])
            else:
                Code01_Wave2.e = jcast('int', Code01_Wave2.nxt[Code01_Wave2.e])
            if (Code01_Wave2.e != 0):
                Code01_Wave2.push(Code01_Wave2.u, Code01_Wave2.f, 0, Code01_Wave2.e)
                v = jcast('int', Code01_Wave2.to[Code01_Wave2.e])
                if (v != Code01_Wave2.f):
                    Code01_Wave2.push(v, Code01_Wave2.u, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code01_Wave2.head[Code01_Wave2.u])
                while (ei > 0):
                    v = jcast('int', Code01_Wave2.to[ei])
                    if (v != Code01_Wave2.f):
                        Code01_Wave2.siz[Code01_Wave2.u] = jcast('int', jcast('int', jadd(Code01_Wave2.siz[Code01_Wave2.u], Code01_Wave2.siz[v])))
                        if ((Code01_Wave2.son[Code01_Wave2.u] == 0) or (Code01_Wave2.siz[Code01_Wave2.son[Code01_Wave2.u]] < Code01_Wave2.siz[v])):
                            Code01_Wave2.son[Code01_Wave2.u] = jcast('int', v)
                    ei = jcast('int', Code01_Wave2.nxt[ei])

    # dfs2改成迭代版
    @staticmethod
    def dfs4(cur, tag):
        cur = jcast('int', cur)
        tag = jcast('int', tag)
        Code01_Wave2.stacksize = jcast('int', 0)
        Code01_Wave2.push(cur, 0, tag, jcast('int', (-1)))
        while (Code01_Wave2.stacksize > 0):
            try:
                Code01_Wave2.pop()
                if (Code01_Wave2.e == jcast('int', (-1))):
                    Code01_Wave2.top[Code01_Wave2.u] = jcast('int', Code01_Wave2.t)
                    if (Code01_Wave2.son[Code01_Wave2.u] == 0):
                        raise JContinue(None)
                    Code01_Wave2.push(Code01_Wave2.u, 0, Code01_Wave2.t, jcast('int', (-2)))
                    Code01_Wave2.push(Code01_Wave2.son[Code01_Wave2.u], 0, Code01_Wave2.t, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code01_Wave2.e == jcast('int', (-2))):
                        Code01_Wave2.e = jcast('int', Code01_Wave2.head[Code01_Wave2.u])
                    else:
                        Code01_Wave2.e = jcast('int', Code01_Wave2.nxt[Code01_Wave2.e])
                if (Code01_Wave2.e != 0):
                    Code01_Wave2.push(Code01_Wave2.u, 0, Code01_Wave2.t, Code01_Wave2.e)
                    v = jcast('int', Code01_Wave2.to[Code01_Wave2.e])
                    if ((v != Code01_Wave2.fa[Code01_Wave2.u]) and (v != Code01_Wave2.son[Code01_Wave2.u])):
                        Code01_Wave2.push(v, 0, v, jcast('int', (-1)))
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
        while (Code01_Wave2.top[a] != Code01_Wave2.top[b]):
            if (Code01_Wave2.dep[Code01_Wave2.top[a]] <= Code01_Wave2.dep[Code01_Wave2.top[b]]):
                b = jcast('int', Code01_Wave2.fa[Code01_Wave2.top[b]])
            else:
                a = jcast('int', Code01_Wave2.fa[Code01_Wave2.top[a]])
        return jcast('int', (a if (Code01_Wave2.dep[a] <= Code01_Wave2.dep[b]) else b))

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code01_Wave2.dep[x], Code01_Wave2.dep[y])) - jcast('int', (Code01_Wave2.dep[Code01_Wave2.getLca(x, y)] << (1 & 31))))))

    # 找重心需要计算子树大小的递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code01_Wave2.siz[u] = jcast('int', 1)
        e = jcast('int', Code01_Wave2.head[u])
        while (e > 0):
            v = jcast('int', Code01_Wave2.to[e])
            if ((v != fa) and (not Code01_Wave2.vis[v])):
                Code01_Wave2.getSize1(v, u)
                Code01_Wave2.siz[u] = jcast('int', jcast('int', jadd(Code01_Wave2.siz[u], Code01_Wave2.siz[v])))
            e = jcast('int', Code01_Wave2.nxt[e])

    # getSize1的迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code01_Wave2.stacksize = jcast('int', 0)
        Code01_Wave2.push(cur, fa, 0, jcast('int', (-1)))
        while (Code01_Wave2.stacksize > 0):
            Code01_Wave2.pop()
            if (Code01_Wave2.e == jcast('int', (-1))):
                Code01_Wave2.siz[Code01_Wave2.u] = jcast('int', 1)
                Code01_Wave2.e = jcast('int', Code01_Wave2.head[Code01_Wave2.u])
            else:
                Code01_Wave2.e = jcast('int', Code01_Wave2.nxt[Code01_Wave2.e])
            if (Code01_Wave2.e != 0):
                Code01_Wave2.push(Code01_Wave2.u, Code01_Wave2.f, 0, Code01_Wave2.e)
                v = jcast('int', Code01_Wave2.to[Code01_Wave2.e])
                if ((v != Code01_Wave2.f) and (not Code01_Wave2.vis[v])):
                    Code01_Wave2.push(v, Code01_Wave2.u, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code01_Wave2.head[Code01_Wave2.u])
                while (ei > 0):
                    v = jcast('int', Code01_Wave2.to[ei])
                    if ((v != Code01_Wave2.f) and (not Code01_Wave2.vis[v])):
                        Code01_Wave2.siz[Code01_Wave2.u] = jcast('int', jcast('int', jadd(Code01_Wave2.siz[Code01_Wave2.u], Code01_Wave2.siz[v])))
                    ei = jcast('int', Code01_Wave2.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code01_Wave2.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code01_Wave2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code01_Wave2.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code01_Wave2.to[e])
                        if (((v != fa) and (not Code01_Wave2.vis[v])) and (Code01_Wave2.siz[v] > half)):
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
                    e = jcast('int', Code01_Wave2.nxt[e])
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
        Code01_Wave2.centfa[u] = jcast('int', fa)
        Code01_Wave2.vis[u] = jcast('boolean', True)
        e = jcast('int', Code01_Wave2.head[u])
        while (e > 0):
            v = jcast('int', Code01_Wave2.to[e])
            if (not Code01_Wave2.vis[v]):
                Code01_Wave2.centroidTree(Code01_Wave2.getCentroid(v, u), u)
            e = jcast('int', Code01_Wave2.nxt[e])

    @staticmethod
    def _java_add_0(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_7 := Code01_Wave2), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        if (l == r):
            Code01_Wave2.sum[i] = jcast('int', jcast('int', jadd(Code01_Wave2.sum[i], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code01_Wave2.ls, i, Code01_Wave2._java_add_0(jobi, jobv, l, mid, Code01_Wave2.ls[i]))
            else:
                jset(Code01_Wave2.rs, i, Code01_Wave2._java_add_0(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code01_Wave2.rs[i]))
            Code01_Wave2.sum[i] = jcast('int', jcast('int', jadd(Code01_Wave2.sum[Code01_Wave2.ls[i]], Code01_Wave2.sum[Code01_Wave2.rs[i]])))
        return jcast('int', i)

    @staticmethod
    def _java_query_0(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code01_Wave2.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code01_Wave2._java_query_0(jobl, jobr, l, mid, Code01_Wave2.ls[i]))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code01_Wave2._java_query_0(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code01_Wave2.rs[i]))))
        return jcast('int', ans)

    @staticmethod
    def _java_add_1(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        jset(Code01_Wave2.addTree, x, Code01_Wave2._java_add_0(0, v, 0, jcast('int', (Code01_Wave2.n - 1)), Code01_Wave2.addTree[x]))
        cur = jcast('int', x)
        fa = jcast('int', Code01_Wave2.centfa[cur])
        while (fa > 0):
            dist = jcast('int', Code01_Wave2.getDist(x, fa))
            jset(Code01_Wave2.addTree, fa, Code01_Wave2._java_add_0(dist, v, 0, jcast('int', (Code01_Wave2.n - 1)), Code01_Wave2.addTree[fa]))
            jset(Code01_Wave2.minusTree, cur, Code01_Wave2._java_add_0(dist, v, 0, jcast('int', (Code01_Wave2.n - 1)), Code01_Wave2.minusTree[cur]))
            cur = jcast('int', fa)
            fa = jcast('int', Code01_Wave2.centfa[cur])

    @staticmethod
    def _java_query_1(x, k):
        x = jcast('int', x)
        k = jcast('int', k)
        ans = jcast('int', Code01_Wave2._java_query_0(0, k, 0, jcast('int', (Code01_Wave2.n - 1)), Code01_Wave2.addTree[x]))
        cur = jcast('int', x)
        fa = jcast('int', Code01_Wave2.centfa[cur])
        while (fa > 0):
            dist = jcast('int', Code01_Wave2.getDist(x, fa))
            if (jcast('int', (k - dist)) >= 0):
                ans = jcast('int', jcast('int', jadd(ans, Code01_Wave2._java_query_0(0, jcast('int', (k - dist)), 0, jcast('int', (Code01_Wave2.n - 1)), Code01_Wave2.addTree[fa]))))
                ans = jcast('int', jcast('int', (ans - Code01_Wave2._java_query_0(0, jcast('int', (k - dist)), 0, jcast('int', (Code01_Wave2.n - 1)), Code01_Wave2.minusTree[cur]))))
            cur = jcast('int', fa)
            fa = jcast('int', Code01_Wave2.centfa[cur])
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code01_Wave2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_Wave2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_Wave2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_Wave2.n):
            jset(Code01_Wave2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_Wave2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code01_Wave2.addEdge(u, v)
            Code01_Wave2.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        # dfs2(1, 1);
        Code01_Wave2.dfs3(1, 0)
        Code01_Wave2.dfs4(1, 1)
        Code01_Wave2.centroidTree(Code01_Wave2.getCentroid(1, 0), 0)
        i = jcast('int', 1)
        while (i <= Code01_Wave2.n):
            Code01_Wave2._java_add_1(i, Code01_Wave2.arr[i])
            i = jcast('int', (i + 1))
        lastAns = jcast('int', 0)
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code01_Wave2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcast('int', (x ^ lastAns)))
            y = jcast('int', jcast('int', (y ^ lastAns)))
            if (op == 0):
                lastAns = jcast('int', Code01_Wave2._java_query_1(x, y))
                jcall(out, 'println', lastAns)
            else:
                Code01_Wave2._java_add_1(x, jcast('int', (y - Code01_Wave2.arr[x])))
                Code01_Wave2.arr[x] = jcast('int', y)
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code01_Wave2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code01_Wave2._java_add_0(*args)
        if _java_choice == 1:
            return Code01_Wave2._java_add_1(*args)
        raise TypeError("No matching overload for Code01_Wave2.add")

    @staticmethod
    def query(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code01_Wave2._java_query_0(*args)
        if _java_choice == 1:
            return Code01_Wave2._java_query_1(*args)
        raise TypeError("No matching overload for Code01_Wave2.query")


Code01_Wave2.MAXN = jcast('int', 100001)
Code01_Wave2.MAXT = jcast('int', 10000001)
Code01_Wave2.n = jcast('int', 0)
Code01_Wave2.m = jcast('int', 0)
Code01_Wave2.arr = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.head = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.nxt = jarray('int', [jcast('int', (Code01_Wave2.MAXN << (1 & 31)))])
Code01_Wave2.to = jarray('int', [jcast('int', (Code01_Wave2.MAXN << (1 & 31)))])
Code01_Wave2.cntg = jcast('int', 0)
Code01_Wave2.fa = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.dep = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.siz = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.son = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.top = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.vis = jarray('boolean', [Code01_Wave2.MAXN])
Code01_Wave2.centfa = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.addTree = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.minusTree = jarray('int', [Code01_Wave2.MAXN])
Code01_Wave2.ls = jarray('int', [Code01_Wave2.MAXT])
Code01_Wave2.rs = jarray('int', [Code01_Wave2.MAXT])
Code01_Wave2.sum = jarray('int', [Code01_Wave2.MAXT])
Code01_Wave2.cntt = jcast('int', 0)
Code01_Wave2.stack = jarray('int', [Code01_Wave2.MAXN, 4])
Code01_Wave2.u = jcast('int', 0)
Code01_Wave2.f = jcast('int', 0)
Code01_Wave2.t = jcast('int', 0)
Code01_Wave2.e = jcast('int', 0)
Code01_Wave2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code01_Wave2.main([])
