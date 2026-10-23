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

# 树上莫队入门题，Python版
# 一共有n个节点，每个节点给定颜色值，给定n-1条边，所有节点连成一棵树
# 一共有m条查询，格式 u v : 打印点u到点v的简单路径上，有几种不同的颜色
# 1 <= n <= 4 * 10^4
# 1 <= m <= 10^5
# 1 <= 颜色值 <= 2 * 10^9
# 测试链接 : https://www.luogu.com.cn/problem/SP10707
# 测试链接 : https://www.spoj.com/problems/COT2/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code07_MoOnTree2.py
# 两个版本保留相同的算法逻辑
class Code07_MoOnTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'color': 'color', 'sorted': 'sorted', 'cntv': 'cntv', 'query': 'query', 'head': 'head', 'to': 'to', 'next': 'next', 'cntg': 'cntg', 'dep': 'dep', 'seg': 'seg', 'st': 'st', 'ed': 'ed', 'stjump': 'stjump', 'cntd': 'cntd', 'bi': 'bi', 'vis': 'vis', 'cnt': 'cnt', 'kind': 'kind', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    color = None
    sorted = None
    cntv = 0
    # 查询的参数，jobl、jobr、lca、id
    # 如果是类型1，那么lca == 0，表示空缺
    # 如果是类型2，那么lca > 0，查询结果需要补充这个单点信息
    query = None
    # 链式前向星
    head = None
    to = None
    next = None
    cntg = 0
    # dep是深度
    # seg是括号序
    # st是节点开始序
    # ed是节点结束序
    # stjump是倍增表
    # cntd是括号序列的长度
    dep = None
    seg = None
    st = None
    ed = None
    stjump = None
    cntd = 0
    # 分块
    bi = None
    # 窗口信息
    vis = None
    cnt = None
    kind = 0
    ans = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_MoOnTree1.next, ((_java_obj_1 := Code07_MoOnTree1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_MoOnTree1.head[u])
        Code07_MoOnTree1.to[Code07_MoOnTree1.cntg] = jcast('int', v)
        Code07_MoOnTree1.head[u] = jcast('int', Code07_MoOnTree1.cntg)

    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code07_MoOnTree1.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code07_MoOnTree1.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code07_MoOnTree1.dep[u] = jcast('int', jcast('int', jadd(Code07_MoOnTree1.dep[fa], 1)))
        jset(Code07_MoOnTree1.seg, ((_java_obj_4 := Code07_MoOnTree1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)
        Code07_MoOnTree1.st[u] = jcast('int', Code07_MoOnTree1.cntd)
        jset(Code07_MoOnTree1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code07_MoOnTree1.MAXP):
            jset(Code07_MoOnTree1.stjump[u], p, Code07_MoOnTree1.stjump[Code07_MoOnTree1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code07_MoOnTree1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_MoOnTree1.to[e])
            if (v != fa):
                Code07_MoOnTree1.dfs(v, u)
            e = jcast('int', Code07_MoOnTree1.next[e])
        jset(Code07_MoOnTree1.seg, ((_java_obj_7 := Code07_MoOnTree1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        Code07_MoOnTree1.ed[u] = jcast('int', Code07_MoOnTree1.cntd)

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code07_MoOnTree1.dep[a] < Code07_MoOnTree1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code07_MoOnTree1.MAXP - 1)))
        while (p >= 0):
            if (Code07_MoOnTree1.dep[Code07_MoOnTree1.stjump[a][p]] >= Code07_MoOnTree1.dep[b]):
                a = jcast('int', Code07_MoOnTree1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code07_MoOnTree1.MAXP - 1)))
        while (p >= 0):
            if (Code07_MoOnTree1.stjump[a][p] != Code07_MoOnTree1.stjump[b][p]):
                a = jcast('int', Code07_MoOnTree1.stjump[a][p])
                b = jcast('int', Code07_MoOnTree1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code07_MoOnTree1.stjump[a][0])

    # 普通莫队经典排序
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code07_MoOnTree1.bi[a[0]] != Code07_MoOnTree1.bi[b[0]]):
                return jcast('int', jcast('int', (Code07_MoOnTree1.bi[a[0]] - Code07_MoOnTree1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 窗口不管是加入还是删除node
    # 只要遇到node就翻转信息即可
    @staticmethod
    def invert(node):
        node = jcast('int', node)
        val = jcast('int', Code07_MoOnTree1.color[node])
        if Code07_MoOnTree1.vis[node]:
            if (((_java_obj_10 := Code07_MoOnTree1.cnt), (_java_key_11 := val), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))))[3] == 0):
                Code07_MoOnTree1.kind = jcast('int', (Code07_MoOnTree1.kind - 1))
        else:
            if (((_java_obj_13 := Code07_MoOnTree1.cnt), (_java_key_14 := val), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3] == 1):
                Code07_MoOnTree1.kind = jcast('int', (Code07_MoOnTree1.kind + 1))
        Code07_MoOnTree1.vis[node] = jcast('boolean', (not Code07_MoOnTree1.vis[node]))

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_MoOnTree1.m):
            jobl = jcast('int', Code07_MoOnTree1.query[i][0])
            jobr = jcast('int', Code07_MoOnTree1.query[i][1])
            lca = jcast('int', Code07_MoOnTree1.query[i][2])
            id = jcast('int', Code07_MoOnTree1.query[i][3])
            while (winl > jobl):
                Code07_MoOnTree1.invert(Code07_MoOnTree1.seg[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code07_MoOnTree1.invert(Code07_MoOnTree1.seg[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code07_MoOnTree1.invert(Code07_MoOnTree1.seg[((_java_old_16 := winl), (winl := jcast('int', (winl + (1)))), _java_old_16)[2]])
            while (winr > jobr):
                Code07_MoOnTree1.invert(Code07_MoOnTree1.seg[((_java_old_17 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_17)[2]])
            if (lca > 0):
                Code07_MoOnTree1.invert(lca)
            Code07_MoOnTree1.ans[id] = jcast('int', Code07_MoOnTree1.kind)
            if (lca > 0):
                Code07_MoOnTree1.invert(lca)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_MoOnTree1.n):
            Code07_MoOnTree1.sorted[i] = jcast('int', Code07_MoOnTree1.color[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_MoOnTree1.sorted, 1, jcast('int', jadd(Code07_MoOnTree1.n, 1)))
        Code07_MoOnTree1.cntv = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code07_MoOnTree1.n):
            if (Code07_MoOnTree1.sorted[Code07_MoOnTree1.cntv] != Code07_MoOnTree1.sorted[i]):
                jset(Code07_MoOnTree1.sorted, ((_java_obj_18 := Code07_MoOnTree1), (_java_key_19 := 'cntv'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))))[3], Code07_MoOnTree1.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_MoOnTree1.n):
            jset(Code07_MoOnTree1.color, i, Code07_MoOnTree1.kth(Code07_MoOnTree1.color[i]))
            i = jcast('int', (i + 1))
        # 括号序列分块
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code07_MoOnTree1.cntd)))
        i = jcast('int', 1)
        while (i <= Code07_MoOnTree1.cntd):
            Code07_MoOnTree1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_MoOnTree1.query, 1, jcast('int', jadd(Code07_MoOnTree1.m, 1)), Code07_MoOnTree1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code07_MoOnTree1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_MoOnTree1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_MoOnTree1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_MoOnTree1.n):
            jset(Code07_MoOnTree1.color, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_MoOnTree1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code07_MoOnTree1.addEdge(u, v)
            Code07_MoOnTree1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code07_MoOnTree1.dfs(1, 0)
        i = jcast('int', 1)
        u = 0
        v = 0
        uvlca = 0
        while (i <= Code07_MoOnTree1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            if (Code07_MoOnTree1.st[v] < Code07_MoOnTree1.st[u]):
                tmp = jcast('int', u)
                u = jcast('int', v)
                v = jcast('int', tmp)
            uvlca = jcast('int', Code07_MoOnTree1.lca(u, v))
            if (u == uvlca):
                jset(Code07_MoOnTree1.query[i], 0, Code07_MoOnTree1.st[u])
                jset(Code07_MoOnTree1.query[i], 1, Code07_MoOnTree1.st[v])
                jset(Code07_MoOnTree1.query[i], 2, 0)
            else:
                jset(Code07_MoOnTree1.query[i], 0, Code07_MoOnTree1.ed[u])
                jset(Code07_MoOnTree1.query[i], 1, Code07_MoOnTree1.st[v])
                jset(Code07_MoOnTree1.query[i], 2, uvlca)
            jset(Code07_MoOnTree1.query[i], 3, i)
            i = jcast('int', (i + 1))
        Code07_MoOnTree1.prepare()
        Code07_MoOnTree1.compute()
        i = jcast('int', 1)
        while (i <= Code07_MoOnTree1.m):
            jcall(out, 'println', Code07_MoOnTree1.ans[i])
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
            raise TypeError("No matching overload for Code07_MoOnTree1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_MoOnTree1.MAXN = jcast('int', 40001)
Code07_MoOnTree1.MAXM = jcast('int', 100001)
Code07_MoOnTree1.MAXP = jcast('int', 20)
Code07_MoOnTree1.n = jcast('int', 0)
Code07_MoOnTree1.m = jcast('int', 0)
Code07_MoOnTree1.color = jarray('int', [Code07_MoOnTree1.MAXN])
Code07_MoOnTree1.sorted = jarray('int', [Code07_MoOnTree1.MAXN])
Code07_MoOnTree1.cntv = jcast('int', 0)
Code07_MoOnTree1.query = jarray('int', [Code07_MoOnTree1.MAXM, 4])
Code07_MoOnTree1.head = jarray('int', [Code07_MoOnTree1.MAXN])
Code07_MoOnTree1.to = jarray('int', [jcast('int', (Code07_MoOnTree1.MAXN << (1 & 31)))])
Code07_MoOnTree1.next = jarray('int', [jcast('int', (Code07_MoOnTree1.MAXN << (1 & 31)))])
Code07_MoOnTree1.cntg = jcast('int', 0)
Code07_MoOnTree1.dep = jarray('int', [Code07_MoOnTree1.MAXN])
Code07_MoOnTree1.seg = jarray('int', [jcast('int', (Code07_MoOnTree1.MAXN << (1 & 31)))])
Code07_MoOnTree1.st = jarray('int', [Code07_MoOnTree1.MAXN])
Code07_MoOnTree1.ed = jarray('int', [Code07_MoOnTree1.MAXN])
Code07_MoOnTree1.stjump = jarray('int', [Code07_MoOnTree1.MAXN, Code07_MoOnTree1.MAXP])
Code07_MoOnTree1.cntd = jcast('int', 0)
Code07_MoOnTree1.bi = jarray('int', [jcast('int', (Code07_MoOnTree1.MAXN << (1 & 31)))])
Code07_MoOnTree1.vis = jarray('boolean', [Code07_MoOnTree1.MAXN])
Code07_MoOnTree1.cnt = jarray('int', [Code07_MoOnTree1.MAXN])
Code07_MoOnTree1.kind = jcast('int', 0)
Code07_MoOnTree1.ans = jarray('int', [Code07_MoOnTree1.MAXM])

if __name__ == '__main__':
    Code07_MoOnTree1.main([])
