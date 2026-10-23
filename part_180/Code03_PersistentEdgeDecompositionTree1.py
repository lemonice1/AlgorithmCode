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

# 可持久化边分树，Python版
# 树上有n个节点，给定n-1条边，每条边有边权
# 给定长度为n的数组arr，代表点编号组成的一个排列
# 接下来有q条操作，每条操作是如下两种类型中的一种
# 操作 1 x y z : 打印arr[x..y]中每个节点到节点z的简单路径距离之和
# 操作 2 x     : 交换arr[x]和arr[x+1]的值，输入保证 1 <= x < n
# 1 <= n、q <= 2 * 10^5
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/CF757G
# 测试链接 : https://codeforces.com/problemset/problem/757/G
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_PersistentEdgeDecompositionTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'q': 'q', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'weight1': 'weight1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'weight2': 'weight2', 'cnt2': 'cnt2', 'vis': 'vis', 'siz': 'siz', 'up': 'up', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'lcnt': 'lcnt', 'rcnt': 'rcnt', 'lsum': 'lsum', 'rsum': 'rsum', 'cntt': 'cntt', 'arr': 'arr', 'pre': 'pre'}
    MAXN = 0
    MAXT = 0
    n = 0
    q = 0
    cntn = 0
    head1 = None
    next1 = None
    to1 = None
    weight1 = None
    cnt1 = 0
    head2 = None
    next2 = None
    to2 = None
    weight2 = None
    cnt2 = 0
    vis = None
    siz = None
    up = None
    root = None
    ls = None
    rs = None
    lcnt = None
    rcnt = None
    lsum = None
    rsum = None
    cntt = 0
    arr = None
    pre = None
    @staticmethod
    def addEdge1(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_PersistentEdgeDecompositionTree1.next1, ((_java_obj_1 := Code03_PersistentEdgeDecompositionTree1), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_PersistentEdgeDecompositionTree1.head1[u])
        Code03_PersistentEdgeDecompositionTree1.to1[Code03_PersistentEdgeDecompositionTree1.cnt1] = jcast('int', v)
        Code03_PersistentEdgeDecompositionTree1.weight1[Code03_PersistentEdgeDecompositionTree1.cnt1] = jcast('int', w)
        Code03_PersistentEdgeDecompositionTree1.head1[u] = jcast('int', Code03_PersistentEdgeDecompositionTree1.cnt1)

    @staticmethod
    def addEdge2(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_PersistentEdgeDecompositionTree1.next2, ((_java_obj_4 := Code03_PersistentEdgeDecompositionTree1), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code03_PersistentEdgeDecompositionTree1.head2[u])
        Code03_PersistentEdgeDecompositionTree1.to2[Code03_PersistentEdgeDecompositionTree1.cnt2] = jcast('int', v)
        Code03_PersistentEdgeDecompositionTree1.weight2[Code03_PersistentEdgeDecompositionTree1.cnt2] = jcast('int', w)
        Code03_PersistentEdgeDecompositionTree1.head2[u] = jcast('int', Code03_PersistentEdgeDecompositionTree1.cnt2)

    @staticmethod
    def rebuild(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        last = jcast('int', 0)
        e = jcast('int', Code03_PersistentEdgeDecompositionTree1.head1[u])
        while (e > 0):
            v = jcast('int', Code03_PersistentEdgeDecompositionTree1.to1[e])
            w = jcast('int', Code03_PersistentEdgeDecompositionTree1.weight1[e])
            if (v != fa):
                if (last == 0):
                    last = jcast('int', u)
                    Code03_PersistentEdgeDecompositionTree1.addEdge2(u, v, w)
                    Code03_PersistentEdgeDecompositionTree1.addEdge2(v, u, w)
                else:
                    add = jcast('int', ((_java_obj_7 := Code03_PersistentEdgeDecompositionTree1), (_java_key_8 := 'cntn'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                    Code03_PersistentEdgeDecompositionTree1.addEdge2(last, add, 0)
                    Code03_PersistentEdgeDecompositionTree1.addEdge2(add, last, 0)
                    Code03_PersistentEdgeDecompositionTree1.addEdge2(add, v, w)
                    Code03_PersistentEdgeDecompositionTree1.addEdge2(v, add, w)
                    last = jcast('int', add)
                Code03_PersistentEdgeDecompositionTree1.rebuild(v, u)
            e = jcast('int', Code03_PersistentEdgeDecompositionTree1.next1[e])

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_PersistentEdgeDecompositionTree1.siz[u] = jcast('int', 1)
        e = jcast('int', Code03_PersistentEdgeDecompositionTree1.head2[u])
        while (e > 0):
            v = jcast('int', Code03_PersistentEdgeDecompositionTree1.to2[e])
            if ((v != fa) and (not Code03_PersistentEdgeDecompositionTree1.vis[jcast('int', (e >> (1 & 31)))])):
                Code03_PersistentEdgeDecompositionTree1.getSize(v, u)
                Code03_PersistentEdgeDecompositionTree1.siz[u] = jcast('int', jcast('int', jadd(Code03_PersistentEdgeDecompositionTree1.siz[u], Code03_PersistentEdgeDecompositionTree1.siz[v])))
            e = jcast('int', Code03_PersistentEdgeDecompositionTree1.next2[e])

    @staticmethod
    def getCentroidEdge(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_PersistentEdgeDecompositionTree1.getSize(u, fa)
        total = jcast('int', Code03_PersistentEdgeDecompositionTree1.siz[u])
        half = jcast('int', jcast('int', (total >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code03_PersistentEdgeDecompositionTree1.head2[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code03_PersistentEdgeDecompositionTree1.to2[e])
                        if (((v != fa) and (not Code03_PersistentEdgeDecompositionTree1.vis[jcast('int', (e >> (1 & 31)))])) and (Code03_PersistentEdgeDecompositionTree1.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_11:
                        if _java_control_11.label not in (None,):
                            raise
                    except JBreak as _java_control_11:
                        if _java_control_11.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code03_PersistentEdgeDecompositionTree1.next2[e])
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
        best = jcast('int', 0)
        edge = jcast('int', 0)
        e = jcast('int', Code03_PersistentEdgeDecompositionTree1.head2[u])
        while (e > 0):
            if (not Code03_PersistentEdgeDecompositionTree1.vis[jcast('int', (e >> (1 & 31)))]):
                v = jcast('int', Code03_PersistentEdgeDecompositionTree1.to2[e])
                sub = jcast('int', (jcast('int', (total - Code03_PersistentEdgeDecompositionTree1.siz[u])) if (v == fa) else Code03_PersistentEdgeDecompositionTree1.siz[v]))
                if (sub > best):
                    best = jcast('int', sub)
                    edge = jcast('int', e)
            e = jcast('int', Code03_PersistentEdgeDecompositionTree1.next2[e])
        return jcast('int', edge)

    @staticmethod
    def dfs(u, fa, dist, op):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dist = jcast('long', dist)
        op = jcast('int', op)
        if (u <= Code03_PersistentEdgeDecompositionTree1.n):
            if (Code03_PersistentEdgeDecompositionTree1.up[u] == 0):
                jset(Code03_PersistentEdgeDecompositionTree1.up, u, ((_java_obj_12 := Code03_PersistentEdgeDecompositionTree1), (_java_key_13 := 'cntt'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3])
                Code03_PersistentEdgeDecompositionTree1.root[u] = jcast('int', Code03_PersistentEdgeDecompositionTree1.cntt)
            cur = jcast('int', Code03_PersistentEdgeDecompositionTree1.up[u])
            nxt = jcast('int', ((_java_obj_15 := Code03_PersistentEdgeDecompositionTree1), (_java_key_16 := 'cntt'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))))[3])
            if (op == 0):
                Code03_PersistentEdgeDecompositionTree1.ls[cur] = jcast('int', nxt)
                Code03_PersistentEdgeDecompositionTree1.lsum[cur] = jcast('long', dist)
                Code03_PersistentEdgeDecompositionTree1.lcnt[cur] = jcast('int', 1)
            else:
                Code03_PersistentEdgeDecompositionTree1.rs[cur] = jcast('int', nxt)
                Code03_PersistentEdgeDecompositionTree1.rsum[cur] = jcast('long', dist)
                Code03_PersistentEdgeDecompositionTree1.rcnt[cur] = jcast('int', 1)
            Code03_PersistentEdgeDecompositionTree1.up[u] = jcast('int', nxt)
        e = jcast('int', Code03_PersistentEdgeDecompositionTree1.head2[u])
        while (e > 0):
            v = jcast('int', Code03_PersistentEdgeDecompositionTree1.to2[e])
            if ((v != fa) and (not Code03_PersistentEdgeDecompositionTree1.vis[jcast('int', (e >> (1 & 31)))])):
                Code03_PersistentEdgeDecompositionTree1.dfs(v, u, jcast('long', jadd(dist, Code03_PersistentEdgeDecompositionTree1.weight2[e])), op)
            e = jcast('int', Code03_PersistentEdgeDecompositionTree1.next2[e])

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        edge = jcast('int', Code03_PersistentEdgeDecompositionTree1.getCentroidEdge(u, 0))
        if (edge > 0):
            Code03_PersistentEdgeDecompositionTree1.vis[jcast('int', (edge >> (1 & 31)))] = jcast('boolean', True)
            v1 = jcast('int', Code03_PersistentEdgeDecompositionTree1.to2[edge])
            v2 = jcast('int', Code03_PersistentEdgeDecompositionTree1.to2[jcast('int', (edge ^ 1))])
            Code03_PersistentEdgeDecompositionTree1.dfs(v1, 0, 0, 0)
            Code03_PersistentEdgeDecompositionTree1.dfs(v2, 0, Code03_PersistentEdgeDecompositionTree1.weight2[edge], 1)
            Code03_PersistentEdgeDecompositionTree1.solve(v1)
            Code03_PersistentEdgeDecompositionTree1.solve(v2)

    @staticmethod
    def add(p, i):
        p = jcast('int', p)
        i = jcast('int', i)
        if ((p == 0) or (i == 0)):
            return jcast('int', jcast('int', jadd(p, i)))
        rt = jcast('int', ((_java_obj_18 := Code03_PersistentEdgeDecompositionTree1), (_java_key_19 := 'cntt'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))))[3])
        Code03_PersistentEdgeDecompositionTree1.ls[rt] = jcast('int', Code03_PersistentEdgeDecompositionTree1.ls[p])
        Code03_PersistentEdgeDecompositionTree1.rs[rt] = jcast('int', Code03_PersistentEdgeDecompositionTree1.rs[p])
        Code03_PersistentEdgeDecompositionTree1.lcnt[rt] = jcast('int', jcast('int', jadd(Code03_PersistentEdgeDecompositionTree1.lcnt[p], Code03_PersistentEdgeDecompositionTree1.lcnt[i])))
        Code03_PersistentEdgeDecompositionTree1.rcnt[rt] = jcast('int', jcast('int', jadd(Code03_PersistentEdgeDecompositionTree1.rcnt[p], Code03_PersistentEdgeDecompositionTree1.rcnt[i])))
        Code03_PersistentEdgeDecompositionTree1.lsum[rt] = jcast('long', jcast('long', jadd(Code03_PersistentEdgeDecompositionTree1.lsum[p], Code03_PersistentEdgeDecompositionTree1.lsum[i])))
        Code03_PersistentEdgeDecompositionTree1.rsum[rt] = jcast('long', jcast('long', jadd(Code03_PersistentEdgeDecompositionTree1.rsum[p], Code03_PersistentEdgeDecompositionTree1.rsum[i])))
        if (Code03_PersistentEdgeDecompositionTree1.ls[i] > 0):
            jset(Code03_PersistentEdgeDecompositionTree1.ls, rt, Code03_PersistentEdgeDecompositionTree1.add(Code03_PersistentEdgeDecompositionTree1.ls[rt], Code03_PersistentEdgeDecompositionTree1.ls[i]))
        else:
            jset(Code03_PersistentEdgeDecompositionTree1.rs, rt, Code03_PersistentEdgeDecompositionTree1.add(Code03_PersistentEdgeDecompositionTree1.rs[rt], Code03_PersistentEdgeDecompositionTree1.rs[i]))
        return jcast('int', rt)

    @staticmethod
    def query(p1, p2, i):
        p1 = jcast('int', p1)
        p2 = jcast('int', p2)
        i = jcast('int', i)
        if ((Code03_PersistentEdgeDecompositionTree1.ls[i] == 0) and (Code03_PersistentEdgeDecompositionTree1.rs[i] == 0)):
            return jcast('long', 0)
        else:
            if (Code03_PersistentEdgeDecompositionTree1.ls[i] > 0):
                return jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(Code03_PersistentEdgeDecompositionTree1.query(Code03_PersistentEdgeDecompositionTree1.ls[p1], Code03_PersistentEdgeDecompositionTree1.ls[p2], Code03_PersistentEdgeDecompositionTree1.ls[i]), Code03_PersistentEdgeDecompositionTree1.rsum[p2])) - Code03_PersistentEdgeDecompositionTree1.rsum[p1])), jcast('long', (Code03_PersistentEdgeDecompositionTree1.lsum[i] * jcast('int', (Code03_PersistentEdgeDecompositionTree1.rcnt[p2] - Code03_PersistentEdgeDecompositionTree1.rcnt[p1])))))))
            else:
                return jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(Code03_PersistentEdgeDecompositionTree1.query(Code03_PersistentEdgeDecompositionTree1.rs[p1], Code03_PersistentEdgeDecompositionTree1.rs[p2], Code03_PersistentEdgeDecompositionTree1.rs[i]), Code03_PersistentEdgeDecompositionTree1.lsum[p2])) - Code03_PersistentEdgeDecompositionTree1.lsum[p1])), jcast('long', (Code03_PersistentEdgeDecompositionTree1.rsum[i] * jcast('int', (Code03_PersistentEdgeDecompositionTree1.lcnt[p2] - Code03_PersistentEdgeDecompositionTree1.lcnt[p1])))))))

    @staticmethod
    def main(args):
        in_ = Code03_PersistentEdgeDecompositionTree1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_PersistentEdgeDecompositionTree1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_PersistentEdgeDecompositionTree1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_PersistentEdgeDecompositionTree1.n):
            jset(Code03_PersistentEdgeDecompositionTree1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code03_PersistentEdgeDecompositionTree1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code03_PersistentEdgeDecompositionTree1.addEdge1(u, v, w)
            Code03_PersistentEdgeDecompositionTree1.addEdge1(v, u, w)
            i = jcast('int', (i + 1))
        Code03_PersistentEdgeDecompositionTree1.cntn = jcast('int', Code03_PersistentEdgeDecompositionTree1.n)
        Code03_PersistentEdgeDecompositionTree1.cnt2 = jcast('int', 1)
        Code03_PersistentEdgeDecompositionTree1.rebuild(1, 0)
        Code03_PersistentEdgeDecompositionTree1.solve(1)
        i = jcast('int', 1)
        while (i <= Code03_PersistentEdgeDecompositionTree1.n):
            jset(Code03_PersistentEdgeDecompositionTree1.pre, i, Code03_PersistentEdgeDecompositionTree1.add(Code03_PersistentEdgeDecompositionTree1.pre[jcast('int', (i - 1))], Code03_PersistentEdgeDecompositionTree1.root[Code03_PersistentEdgeDecompositionTree1.arr[i]]))
            i = jcast('int', (i + 1))
        mask = jcast('long', jcast('long', (jcast('long', (1 << (30 & 63))) - 1)))
        lastAns = jcast('long', 0)
        a = 0
        b = 0
        c = 0
        op = 0
        x = 0
        y = 0
        z = 0
        tmp = 0
        i = jcast('int', 1)
        while (i <= Code03_PersistentEdgeDecompositionTree1.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                a = jcast('long', jcall(in_, 'nextInt'))
                b = jcast('long', jcall(in_, 'nextInt'))
                c = jcast('long', jcall(in_, 'nextInt'))
                a = jcast('long', jcast('long', (a ^ lastAns)))
                b = jcast('long', jcast('long', (b ^ lastAns)))
                c = jcast('long', jcast('long', (c ^ lastAns)))
                x = jcast('int', jcast('int', a))
                y = jcast('int', jcast('int', b))
                z = jcast('int', jcast('int', c))
                lastAns = jcast('long', Code03_PersistentEdgeDecompositionTree1.query(Code03_PersistentEdgeDecompositionTree1.pre[jcast('int', (x - 1))], Code03_PersistentEdgeDecompositionTree1.pre[y], Code03_PersistentEdgeDecompositionTree1.root[z]))
                jcall(out, 'println', lastAns)
                lastAns = jcast('long', jcast('long', (lastAns & mask)))
            else:
                a = jcast('long', jcall(in_, 'nextInt'))
                a = jcast('long', jcast('long', (a ^ lastAns)))
                x = jcast('int', jcast('int', a))
                tmp = jcast('int', Code03_PersistentEdgeDecompositionTree1.arr[x])
                Code03_PersistentEdgeDecompositionTree1.arr[x] = jcast('int', Code03_PersistentEdgeDecompositionTree1.arr[jcast('int', jadd(x, 1))])
                Code03_PersistentEdgeDecompositionTree1.arr[jcast('int', jadd(x, 1))] = jcast('int', tmp)
                jset(Code03_PersistentEdgeDecompositionTree1.pre, x, Code03_PersistentEdgeDecompositionTree1.add(Code03_PersistentEdgeDecompositionTree1.pre[jcast('int', (x - 1))], Code03_PersistentEdgeDecompositionTree1.root[Code03_PersistentEdgeDecompositionTree1.arr[x]]))
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
            return jcast('int', self.buffer[((_java_obj_21 := self), (_java_key_22 := 'ptr'), (_java_old_23 := jget(_java_obj_21, _java_key_22)), jset(_java_obj_21, _java_key_22, jcast('int', (_java_old_23 + (1)))), _java_old_23)[4]])

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
            raise TypeError("No matching overload for Code03_PersistentEdgeDecompositionTree1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_PersistentEdgeDecompositionTree1.MAXN = jcast('int', 400001)
Code03_PersistentEdgeDecompositionTree1.MAXT = jcast('int', jcast('int', (Code03_PersistentEdgeDecompositionTree1.MAXN * 30)))
Code03_PersistentEdgeDecompositionTree1.n = jcast('int', 0)
Code03_PersistentEdgeDecompositionTree1.q = jcast('int', 0)
Code03_PersistentEdgeDecompositionTree1.cntn = jcast('int', 0)
Code03_PersistentEdgeDecompositionTree1.head1 = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXN])
Code03_PersistentEdgeDecompositionTree1.next1 = jarray('int', [jcast('int', (Code03_PersistentEdgeDecompositionTree1.MAXN << (1 & 31)))])
Code03_PersistentEdgeDecompositionTree1.to1 = jarray('int', [jcast('int', (Code03_PersistentEdgeDecompositionTree1.MAXN << (1 & 31)))])
Code03_PersistentEdgeDecompositionTree1.weight1 = jarray('int', [jcast('int', (Code03_PersistentEdgeDecompositionTree1.MAXN << (1 & 31)))])
Code03_PersistentEdgeDecompositionTree1.cnt1 = jcast('int', 0)
Code03_PersistentEdgeDecompositionTree1.head2 = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXN])
Code03_PersistentEdgeDecompositionTree1.next2 = jarray('int', [jcast('int', (Code03_PersistentEdgeDecompositionTree1.MAXN << (1 & 31)))])
Code03_PersistentEdgeDecompositionTree1.to2 = jarray('int', [jcast('int', (Code03_PersistentEdgeDecompositionTree1.MAXN << (1 & 31)))])
Code03_PersistentEdgeDecompositionTree1.weight2 = jarray('int', [jcast('int', (Code03_PersistentEdgeDecompositionTree1.MAXN << (1 & 31)))])
Code03_PersistentEdgeDecompositionTree1.cnt2 = jcast('int', 0)
Code03_PersistentEdgeDecompositionTree1.vis = jarray('boolean', [Code03_PersistentEdgeDecompositionTree1.MAXN])
Code03_PersistentEdgeDecompositionTree1.siz = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXN])
Code03_PersistentEdgeDecompositionTree1.up = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXN])
Code03_PersistentEdgeDecompositionTree1.root = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXN])
Code03_PersistentEdgeDecompositionTree1.ls = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXT])
Code03_PersistentEdgeDecompositionTree1.rs = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXT])
Code03_PersistentEdgeDecompositionTree1.lcnt = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXT])
Code03_PersistentEdgeDecompositionTree1.rcnt = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXT])
Code03_PersistentEdgeDecompositionTree1.lsum = jarray('long', [Code03_PersistentEdgeDecompositionTree1.MAXT])
Code03_PersistentEdgeDecompositionTree1.rsum = jarray('long', [Code03_PersistentEdgeDecompositionTree1.MAXT])
Code03_PersistentEdgeDecompositionTree1.cntt = jcast('int', 0)
Code03_PersistentEdgeDecompositionTree1.arr = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXN])
Code03_PersistentEdgeDecompositionTree1.pre = jarray('int', [Code03_PersistentEdgeDecompositionTree1.MAXN])

if __name__ == '__main__':
    Code03_PersistentEdgeDecompositionTree1.main([])
