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

# 游客，Python版
# 一共n个城市、m条双向道路，所有城市都连通，商品只有一种
# 每个城市给定商品报价，接下来有q条操作，操作类型有两种
# 操作 C x y : 城市x的商品报价改成y
# 操作 A x y : 从x到y可自由选路，但不能有重复城市，打印能遇到的最低报价
# 1 <= n、m、q <= 10^5
# 1 <= 商品报价 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/CF487E
# 测试链接 : https://codeforces.com/problemset/problem/487/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_Tourists2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 'q': 'q', 'cntn': 'cntn', 'arr': 'arr', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'cnts': 'cnts', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'nid': 'nid', 'cnti': 'cnti', 'maps': 'maps', 'val': 'val', 'minv': 'minv'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    m = 0
    q = 0
    cntn = 0
    arr = None
    head1 = None
    next1 = None
    to1 = None
    cnt1 = 0
    head2 = None
    next2 = None
    to2 = None
    cnt2 = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    cnts = 0
    # nid是圆方树的点获得的dfn序号
    # cnti是圆方树的dfn序号计数
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    nid = None
    cnti = 0
    # 每个方点分配有序表
    maps = None
    # 圆方树中每个点的点权
    val = None
    # 线段树
    minv = None
    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_Tourists2.next1, ((_java_obj_1 := Code08_Tourists2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_Tourists2.head1[u])
        Code08_Tourists2.to1[Code08_Tourists2.cnt1] = jcast('int', v)
        Code08_Tourists2.head1[u] = jcast('int', Code08_Tourists2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_Tourists2.next2, ((_java_obj_4 := Code08_Tourists2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code08_Tourists2.head2[u])
        Code08_Tourists2.to2[Code08_Tourists2.cnt2] = jcast('int', v)
        Code08_Tourists2.head2[u] = jcast('int', Code08_Tourists2.cnt2)

    @staticmethod
    def addNum(u, num):
        u = jcast('int', u)
        num = jcast('int', num)
        if (not jcall(Code08_Tourists2.maps, 'containsKey', u)):
            jcall(Code08_Tourists2.maps, 'put', u, jnew('TreeMap'))
        jcall(jcall(Code08_Tourists2.maps, 'get', u), 'put', num, jadd(jcall(jcall(Code08_Tourists2.maps, 'get', u), 'getOrDefault', num, 0), 1))

    @staticmethod
    def delNum(u, num):
        u = jcast('int', u)
        num = jcast('int', num)
        cnt = jcast('int', jcall(jcall(Code08_Tourists2.maps, 'get', u), 'get', num))
        if (cnt == 1):
            jcall(jcall(Code08_Tourists2.maps, 'get', u), 'remove', num)
        else:
            jcall(jcall(Code08_Tourists2.maps, 'get', u), 'put', num, jcast('int', (cnt - 1)))

    @staticmethod
    def getMin(u):
        u = jcast('int', u)
        return jcast('int', jcall(jcall(Code08_Tourists2.maps, 'get', u), 'firstKey'))

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code08_Tourists2.dfn, u, jset(Code08_Tourists2.low, u, ((_java_obj_7 := Code08_Tourists2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code08_Tourists2.sta, ((_java_obj_10 := Code08_Tourists2), (_java_key_11 := 'cnts'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code08_Tourists2.head1[u])
        while (e > 0):
            v = jcast('int', Code08_Tourists2.to1[e])
            if (Code08_Tourists2.dfn[v] == 0):
                Code08_Tourists2.tarjan(v)
                jset(Code08_Tourists2.low, u, jstatic('Math', 'min', Code08_Tourists2.low[u], Code08_Tourists2.low[v]))
                if (Code08_Tourists2.low[v] >= Code08_Tourists2.dfn[u]):
                    Code08_Tourists2.cntn = jcast('int', (Code08_Tourists2.cntn + 1))
                    Code08_Tourists2.addEdge2(Code08_Tourists2.cntn, u)
                    Code08_Tourists2.addEdge2(u, Code08_Tourists2.cntn)
                    pop = 0
                    while True:
                        pop = jcast('int', Code08_Tourists2.sta[((_java_obj_13 := Code08_Tourists2), (_java_key_14 := 'cnts'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code08_Tourists2.addEdge2(Code08_Tourists2.cntn, pop)
                        Code08_Tourists2.addEdge2(pop, Code08_Tourists2.cntn)
                        if not ((pop != v)):
                            break
            else:
                jset(Code08_Tourists2.low, u, jstatic('Math', 'min', Code08_Tourists2.low[u], Code08_Tourists2.dfn[v]))
            e = jcast('int', Code08_Tourists2.next1[e])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code08_Tourists2.fa[u] = jcast('int', f)
        Code08_Tourists2.dep[u] = jcast('int', jcast('int', jadd(Code08_Tourists2.dep[f], 1)))
        Code08_Tourists2.siz[u] = jcast('int', 1)
        e = jcast('int', Code08_Tourists2.head2[u])
        while (e > 0):
            v = jcast('int', Code08_Tourists2.to2[e])
            if (v != f):
                Code08_Tourists2.dfs1(v, u)
                Code08_Tourists2.siz[u] = jcast('int', jcast('int', jadd(Code08_Tourists2.siz[u], Code08_Tourists2.siz[v])))
                if ((Code08_Tourists2.son[u] == 0) or (Code08_Tourists2.siz[Code08_Tourists2.son[u]] < Code08_Tourists2.siz[v])):
                    Code08_Tourists2.son[u] = jcast('int', v)
                if (u > Code08_Tourists2.n):
                    Code08_Tourists2.addNum(u, Code08_Tourists2.arr[v])
            e = jcast('int', Code08_Tourists2.next2[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code08_Tourists2.top[u] = jcast('int', t)
        jset(Code08_Tourists2.nid, u, ((_java_obj_16 := Code08_Tourists2), (_java_key_17 := 'cnti'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3])
        jset(Code08_Tourists2.val, Code08_Tourists2.nid[u], (Code08_Tourists2.arr[u] if (u <= Code08_Tourists2.n) else Code08_Tourists2.getMin(u)))
        if (Code08_Tourists2.son[u] == 0):
            return
        Code08_Tourists2.dfs2(Code08_Tourists2.son[u], t)
        e = jcast('int', Code08_Tourists2.head2[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code08_Tourists2.to2[e])
            if ((v != Code08_Tourists2.fa[u]) and (v != Code08_Tourists2.son[u])):
                Code08_Tourists2.dfs2(v, v)
            e = jcast('int', Code08_Tourists2.next2[e])

    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code08_Tourists2.minv, i, jstatic('Math', 'min', Code08_Tourists2.minv[jcast('int', (i << (1 & 31)))], Code08_Tourists2.minv[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code08_Tourists2.minv[i] = jcast('int', Code08_Tourists2.val[l])
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code08_Tourists2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code08_Tourists2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code08_Tourists2.up(i)

    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code08_Tourists2.minv[i] = jcast('int', jobv)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                Code08_Tourists2.update(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code08_Tourists2.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code08_Tourists2.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code08_Tourists2.minv[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', Code08_Tourists2.INF)
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code08_Tourists2.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code08_Tourists2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def pathMin(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', Code08_Tourists2.INF)
        while (Code08_Tourists2.top[x] != Code08_Tourists2.top[y]):
            if (Code08_Tourists2.dep[Code08_Tourists2.top[x]] < Code08_Tourists2.dep[Code08_Tourists2.top[y]]):
                tmp = jcast('int', x)
                x = jcast('int', y)
                y = jcast('int', tmp)
            ans = jcast('int', jstatic('Math', 'min', ans, Code08_Tourists2.query(Code08_Tourists2.nid[Code08_Tourists2.top[x]], Code08_Tourists2.nid[x], 1, Code08_Tourists2.cnti, 1)))
            x = jcast('int', Code08_Tourists2.fa[Code08_Tourists2.top[x]])
        if (Code08_Tourists2.dep[x] < Code08_Tourists2.dep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        ans = jcast('int', jstatic('Math', 'min', ans, Code08_Tourists2.query(Code08_Tourists2.nid[y], Code08_Tourists2.nid[x], 1, Code08_Tourists2.cnti, 1)))
        if (y > Code08_Tourists2.n):
            ans = jcast('int', jstatic('Math', 'min', ans, Code08_Tourists2.arr[Code08_Tourists2.fa[y]]))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code08_Tourists2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_Tourists2.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_Tourists2.m = jcast('int', jcall(in_, 'nextInt'))
        Code08_Tourists2.q = jcast('int', jcall(in_, 'nextInt'))
        Code08_Tourists2.cntn = jcast('int', Code08_Tourists2.n)
        i = jcast('int', 1)
        while (i <= Code08_Tourists2.n):
            jset(Code08_Tourists2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code08_Tourists2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code08_Tourists2.addEdge1(u, v)
            Code08_Tourists2.addEdge1(v, u)
            i = jcast('int', (i + 1))
        Code08_Tourists2.tarjan(1)
        Code08_Tourists2.dfs1(1, 0)
        Code08_Tourists2.dfs2(1, 1)
        Code08_Tourists2.build(1, Code08_Tourists2.cnti, 1)
        i = jcast('int', 1)
        while (i <= Code08_Tourists2.q):
            op = jcast('char', jcall(in_, 'nextChar'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == jchar('C')):
                father = jcast('int', Code08_Tourists2.fa[x])
                if (father > 0):
                    Code08_Tourists2.delNum(father, Code08_Tourists2.arr[x])
                    Code08_Tourists2.addNum(father, y)
                    Code08_Tourists2.update(Code08_Tourists2.nid[father], Code08_Tourists2.getMin(father), 1, Code08_Tourists2.cnti, 1)
                Code08_Tourists2.arr[x] = jcast('int', y)
                Code08_Tourists2.update(Code08_Tourists2.nid[x], y, 1, Code08_Tourists2.cnti, 1)
            else:
                jcall(out, 'println', Code08_Tourists2.pathMin(x, y))
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
            return jcast('int', self.buffer[((_java_obj_19 := self), (_java_key_20 := 'ptr'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]])

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

        def nextChar(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((not (((c >= jchar('A')) and (c <= jchar('Z'))) or ((c >= jchar('a')) and (c <= jchar('z')))))):
                    break
            return jcast('char', jcast('char', c))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code08_Tourists2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_Tourists2.MAXN = jcast('int', 100001)
Code08_Tourists2.MAXM = jcast('int', 100001)
Code08_Tourists2.INF = jcast('int', 1000000001)
Code08_Tourists2.n = jcast('int', 0)
Code08_Tourists2.m = jcast('int', 0)
Code08_Tourists2.q = jcast('int', 0)
Code08_Tourists2.cntn = jcast('int', 0)
Code08_Tourists2.arr = jarray('int', [Code08_Tourists2.MAXN])
Code08_Tourists2.head1 = jarray('int', [Code08_Tourists2.MAXN])
Code08_Tourists2.next1 = jarray('int', [jcast('int', (Code08_Tourists2.MAXM << (1 & 31)))])
Code08_Tourists2.to1 = jarray('int', [jcast('int', (Code08_Tourists2.MAXM << (1 & 31)))])
Code08_Tourists2.cnt1 = jcast('int', 0)
Code08_Tourists2.head2 = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (1 & 31)))])
Code08_Tourists2.next2 = jarray('int', [jcast('int', (Code08_Tourists2.MAXM << (2 & 31)))])
Code08_Tourists2.to2 = jarray('int', [jcast('int', (Code08_Tourists2.MAXM << (2 & 31)))])
Code08_Tourists2.cnt2 = jcast('int', 0)
Code08_Tourists2.dfn = jarray('int', [Code08_Tourists2.MAXN])
Code08_Tourists2.low = jarray('int', [Code08_Tourists2.MAXN])
Code08_Tourists2.cntd = jcast('int', 0)
Code08_Tourists2.sta = jarray('int', [Code08_Tourists2.MAXN])
Code08_Tourists2.cnts = jcast('int', 0)
Code08_Tourists2.fa = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (1 & 31)))])
Code08_Tourists2.dep = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (1 & 31)))])
Code08_Tourists2.siz = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (1 & 31)))])
Code08_Tourists2.son = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (1 & 31)))])
Code08_Tourists2.top = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (1 & 31)))])
Code08_Tourists2.nid = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (1 & 31)))])
Code08_Tourists2.cnti = jcast('int', 0)
Code08_Tourists2.maps = jnew('HashMap')
Code08_Tourists2.val = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (1 & 31)))])
Code08_Tourists2.minv = jarray('int', [jcast('int', (Code08_Tourists2.MAXN << (3 & 31)))])

if __name__ == '__main__':
    Code08_Tourists2.main([])
