# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Atm的树，Python版
# 树上有n个点，给定n-1条边，每条边有边权
# 现在关心，从节点x出发到达其他点的距离中，第k小的距离
# 注意，节点x到自己的距离0，不参与距离评比
# 给定正数k，打印每个节点的第k小距离，一共n条打印
# 1 <= n <= 15000
# 1 <= k <= 5000
# 1 <= 边权 <= 10
# 测试链接 : https://www.luogu.com.cn/problem/P10604
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_AtmTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'MAXT': 'MAXT', 'n': 'n', 'k': 'k', 'sumw': 'sumw', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dep': 'dep', 'dist': 'dist', 'stjump': 'stjump', 'vis': 'vis', 'siz': 'siz', 'centfa': 'centfa', 'addTree': 'addTree', 'minusTree': 'minusTree', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'cntt': 'cntt'}
    MAXN = 0
    MAXP = 0
    MAXT = 0
    n = 0
    k = 0
    sumw = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    dep = None
    dist = None
    stjump = None
    vis = None
    siz = None
    centfa = None
    addTree = None
    minusTree = None
    ls = None
    rs = None
    sum = None
    cntt = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_AtmTree1.nxt, ((_java_obj_1 := Code03_AtmTree1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_AtmTree1.head[u])
        Code03_AtmTree1.to[Code03_AtmTree1.cntg] = jcast('int', v)
        Code03_AtmTree1.weight[Code03_AtmTree1.cntg] = jcast('int', w)
        Code03_AtmTree1.head[u] = jcast('int', Code03_AtmTree1.cntg)

    @staticmethod
    def dfs(u, fa, dis):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dis = jcast('int', dis)
        Code03_AtmTree1.dep[u] = jcast('int', jcast('int', jadd(Code03_AtmTree1.dep[fa], 1)))
        Code03_AtmTree1.dist[u] = jcast('int', dis)
        jset(Code03_AtmTree1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code03_AtmTree1.MAXP):
            jset(Code03_AtmTree1.stjump[u], p, Code03_AtmTree1.stjump[Code03_AtmTree1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code03_AtmTree1.head[u])
        while (e > 0):
            v = jcast('int', Code03_AtmTree1.to[e])
            w = jcast('int', Code03_AtmTree1.weight[e])
            if (v != fa):
                Code03_AtmTree1.dfs(v, u, jcast('int', jadd(dis, w)))
            e = jcast('int', Code03_AtmTree1.nxt[e])

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code03_AtmTree1.dep[a] < Code03_AtmTree1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code03_AtmTree1.MAXP - 1)))
        while (p >= 0):
            if (Code03_AtmTree1.dep[Code03_AtmTree1.stjump[a][p]] >= Code03_AtmTree1.dep[b]):
                a = jcast('int', Code03_AtmTree1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code03_AtmTree1.MAXP - 1)))
        while (p >= 0):
            if (Code03_AtmTree1.stjump[a][p] != Code03_AtmTree1.stjump[b][p]):
                a = jcast('int', Code03_AtmTree1.stjump[a][p])
                b = jcast('int', Code03_AtmTree1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code03_AtmTree1.stjump[a][0])

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code03_AtmTree1.dist[x], Code03_AtmTree1.dist[y])) - jcast('int', (Code03_AtmTree1.dist[Code03_AtmTree1.getLca(x, y)] << (1 & 31))))))

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_AtmTree1.siz[u] = jcast('int', 1)
        e = jcast('int', Code03_AtmTree1.head[u])
        while (e > 0):
            v = jcast('int', Code03_AtmTree1.to[e])
            if ((v != fa) and (not Code03_AtmTree1.vis[v])):
                Code03_AtmTree1.getSize(v, u)
                Code03_AtmTree1.siz[u] = jcast('int', jcast('int', jadd(Code03_AtmTree1.siz[u], Code03_AtmTree1.siz[v])))
            e = jcast('int', Code03_AtmTree1.nxt[e])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_AtmTree1.getSize(u, fa)
        half = jcast('int', jcast('int', (Code03_AtmTree1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code03_AtmTree1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code03_AtmTree1.to[e])
                        if (((v != fa) and (not Code03_AtmTree1.vis[v])) and (Code03_AtmTree1.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code03_AtmTree1.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def centroidTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_AtmTree1.centfa[u] = jcast('int', fa)
        Code03_AtmTree1.vis[u] = jcast('boolean', True)
        e = jcast('int', Code03_AtmTree1.head[u])
        while (e > 0):
            v = jcast('int', Code03_AtmTree1.to[e])
            if (not Code03_AtmTree1.vis[v]):
                Code03_AtmTree1.centroidTree(Code03_AtmTree1.getCentroid(v, u), u)
            e = jcast('int', Code03_AtmTree1.nxt[e])

    @staticmethod
    def _java_add_0(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_6 := Code03_AtmTree1), (_java_key_7 := 'cntt'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3])
        if (l == r):
            Code03_AtmTree1.sum[i] = jcast('int', jcast('int', jadd(Code03_AtmTree1.sum[i], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code03_AtmTree1.ls, i, Code03_AtmTree1._java_add_0(jobi, jobv, l, mid, Code03_AtmTree1.ls[i]))
            else:
                jset(Code03_AtmTree1.rs, i, Code03_AtmTree1._java_add_0(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code03_AtmTree1.rs[i]))
            Code03_AtmTree1.sum[i] = jcast('int', jcast('int', jadd(Code03_AtmTree1.sum[Code03_AtmTree1.ls[i]], Code03_AtmTree1.sum[Code03_AtmTree1.rs[i]])))
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
            return jcast('int', Code03_AtmTree1.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code03_AtmTree1._java_query_0(jobl, jobr, l, mid, Code03_AtmTree1.ls[i]))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code03_AtmTree1._java_query_0(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code03_AtmTree1.rs[i]))))
        return jcast('int', ans)

    @staticmethod
    def _java_add_1(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        jset(Code03_AtmTree1.addTree, x, Code03_AtmTree1._java_add_0(0, v, 0, Code03_AtmTree1.sumw, Code03_AtmTree1.addTree[x]))
        cur = jcast('int', x)
        fa = jcast('int', Code03_AtmTree1.centfa[cur])
        while (fa > 0):
            dist = jcast('int', Code03_AtmTree1.getDist(x, fa))
            jset(Code03_AtmTree1.addTree, fa, Code03_AtmTree1._java_add_0(dist, v, 0, Code03_AtmTree1.sumw, Code03_AtmTree1.addTree[fa]))
            jset(Code03_AtmTree1.minusTree, cur, Code03_AtmTree1._java_add_0(dist, v, 0, Code03_AtmTree1.sumw, Code03_AtmTree1.minusTree[cur]))
            cur = jcast('int', fa)
            fa = jcast('int', Code03_AtmTree1.centfa[cur])

    @staticmethod
    def _java_query_1(x, limit):
        x = jcast('int', x)
        limit = jcast('int', limit)
        ans = jcast('int', Code03_AtmTree1._java_query_0(0, limit, 0, Code03_AtmTree1.sumw, Code03_AtmTree1.addTree[x]))
        cur = jcast('int', x)
        fa = jcast('int', Code03_AtmTree1.centfa[cur])
        while (fa > 0):
            dist = jcast('int', Code03_AtmTree1.getDist(x, fa))
            if (jcast('int', (limit - dist)) >= 0):
                ans = jcast('int', jcast('int', jadd(ans, Code03_AtmTree1._java_query_0(0, jcast('int', (limit - dist)), 0, Code03_AtmTree1.sumw, Code03_AtmTree1.addTree[fa]))))
                ans = jcast('int', jcast('int', (ans - Code03_AtmTree1._java_query_0(0, jcast('int', (limit - dist)), 0, Code03_AtmTree1.sumw, Code03_AtmTree1.minusTree[cur]))))
            cur = jcast('int', fa)
            fa = jcast('int', Code03_AtmTree1.centfa[cur])
        return jcast('int', ans)

    @staticmethod
    def compute(x):
        x = jcast('int', x)
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', Code03_AtmTree1.sumw)
        mid = 0
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code03_AtmTree1._java_query_1(x, mid) >= Code03_AtmTree1.k):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code03_AtmTree1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_AtmTree1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_AtmTree1.k = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code03_AtmTree1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code03_AtmTree1.addEdge(u, v, w)
            Code03_AtmTree1.addEdge(v, u, w)
            Code03_AtmTree1.sumw = jcast('int', jcast('int', jadd(Code03_AtmTree1.sumw, w)))
            i = jcast('int', (i + 1))
        Code03_AtmTree1.dfs(1, 0, 0)
        Code03_AtmTree1.centroidTree(Code03_AtmTree1.getCentroid(1, 0), 0)
        i = jcast('int', 1)
        while (i <= Code03_AtmTree1.n):
            Code03_AtmTree1._java_add_1(i, 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_AtmTree1.n):
            jcall(out, 'println', Code03_AtmTree1.compute(i))
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
            return jcast('int', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

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
            raise TypeError("No matching overload for Code03_AtmTree1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code03_AtmTree1._java_add_0(*args)
        if _java_choice == 1:
            return Code03_AtmTree1._java_add_1(*args)
        raise TypeError("No matching overload for Code03_AtmTree1.add")

    @staticmethod
    def query(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code03_AtmTree1._java_query_0(*args)
        if _java_choice == 1:
            return Code03_AtmTree1._java_query_1(*args)
        raise TypeError("No matching overload for Code03_AtmTree1.query")


Code03_AtmTree1.MAXN = jcast('int', 20001)
Code03_AtmTree1.MAXP = jcast('int', 18)
Code03_AtmTree1.MAXT = jcast('int', 1000001)
Code03_AtmTree1.n = jcast('int', 0)
Code03_AtmTree1.k = jcast('int', 0)
Code03_AtmTree1.sumw = jcast('int', 0)
Code03_AtmTree1.head = jarray('int', [Code03_AtmTree1.MAXN])
Code03_AtmTree1.nxt = jarray('int', [jcast('int', (Code03_AtmTree1.MAXN << (1 & 31)))])
Code03_AtmTree1.to = jarray('int', [jcast('int', (Code03_AtmTree1.MAXN << (1 & 31)))])
Code03_AtmTree1.weight = jarray('int', [jcast('int', (Code03_AtmTree1.MAXN << (1 & 31)))])
Code03_AtmTree1.cntg = jcast('int', 0)
Code03_AtmTree1.dep = jarray('int', [Code03_AtmTree1.MAXN])
Code03_AtmTree1.dist = jarray('int', [Code03_AtmTree1.MAXN])
Code03_AtmTree1.stjump = jarray('int', [Code03_AtmTree1.MAXN, Code03_AtmTree1.MAXP])
Code03_AtmTree1.vis = jarray('boolean', [Code03_AtmTree1.MAXN])
Code03_AtmTree1.siz = jarray('int', [Code03_AtmTree1.MAXN])
Code03_AtmTree1.centfa = jarray('int', [Code03_AtmTree1.MAXN])
Code03_AtmTree1.addTree = jarray('int', [Code03_AtmTree1.MAXN])
Code03_AtmTree1.minusTree = jarray('int', [Code03_AtmTree1.MAXN])
Code03_AtmTree1.ls = jarray('int', [Code03_AtmTree1.MAXT])
Code03_AtmTree1.rs = jarray('int', [Code03_AtmTree1.MAXT])
Code03_AtmTree1.sum = jarray('int', [Code03_AtmTree1.MAXT])
Code03_AtmTree1.cntt = jcast('int', 0)

if __name__ == '__main__':
    Code03_AtmTree1.main([])
