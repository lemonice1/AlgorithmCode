# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 铁人两项，Python版
# 给定一张无向图，一共n个点、m条边，图中可能存在多个连通区
# 有效的点对三元组(a, b, c)，首先要求a、b、c是不同的点
# 其次要求存在一条从a出发，经过b，最终到达c的路径，沿途无重复节点
# 打印有效的点对三元组的数量
# 1 <= n <= 10^5
# 1 <= m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4630
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Duathlon2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'deg': 'deg', 'siz': 'siz', 'total': 'total', 'ans': 'ans', 'stack': 'stack', 'u': 'u', 'status': 'status', 'fa': 'fa', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    cntn = 0
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
    top = 0
    # 方点才有deg，点双连通分量的节点数，也就是度
    deg = None
    # dfs过程中，子树中的圆点数量
    siz = None
    # 当前连通区的总节点数
    total = 0
    # 答案
    ans = 0
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    status = 0
    fa = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, fa, e):
        u = jcast('int', u)
        status = jcast('int', status)
        fa = jcast('int', fa)
        e = jcast('int', e)
        jset(Code05_Duathlon2.stack[Code05_Duathlon2.stacksize], 0, u)
        jset(Code05_Duathlon2.stack[Code05_Duathlon2.stacksize], 1, status)
        jset(Code05_Duathlon2.stack[Code05_Duathlon2.stacksize], 2, fa)
        jset(Code05_Duathlon2.stack[Code05_Duathlon2.stacksize], 3, e)
        Code05_Duathlon2.stacksize = jcast('int', (Code05_Duathlon2.stacksize + 1))

    @staticmethod
    def pop():
        Code05_Duathlon2.stacksize = jcast('int', (Code05_Duathlon2.stacksize - 1))
        Code05_Duathlon2.u = jcast('int', Code05_Duathlon2.stack[Code05_Duathlon2.stacksize][0])
        Code05_Duathlon2.status = jcast('int', Code05_Duathlon2.stack[Code05_Duathlon2.stacksize][1])
        Code05_Duathlon2.fa = jcast('int', Code05_Duathlon2.stack[Code05_Duathlon2.stacksize][2])
        Code05_Duathlon2.e = jcast('int', Code05_Duathlon2.stack[Code05_Duathlon2.stacksize][3])

    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Duathlon2.next1, ((_java_obj_1 := Code05_Duathlon2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Duathlon2.head1[u])
        Code05_Duathlon2.to1[Code05_Duathlon2.cnt1] = jcast('int', v)
        Code05_Duathlon2.head1[u] = jcast('int', Code05_Duathlon2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Duathlon2.next2, ((_java_obj_4 := Code05_Duathlon2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code05_Duathlon2.head2[u])
        Code05_Duathlon2.to2[Code05_Duathlon2.cnt2] = jcast('int', v)
        Code05_Duathlon2.head2[u] = jcast('int', Code05_Duathlon2.cnt2)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        Code05_Duathlon2.total = jcast('int', (Code05_Duathlon2.total + 1))
        jset(Code05_Duathlon2.dfn, u, jset(Code05_Duathlon2.low, u, ((_java_obj_7 := Code05_Duathlon2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code05_Duathlon2.sta, ((_java_obj_10 := Code05_Duathlon2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code05_Duathlon2.head1[u])
        while (e > 0):
            v = jcast('int', Code05_Duathlon2.to1[e])
            if (Code05_Duathlon2.dfn[v] == 0):
                Code05_Duathlon2.tarjan1(v)
                jset(Code05_Duathlon2.low, u, jstatic('Math', 'min', Code05_Duathlon2.low[u], Code05_Duathlon2.low[v]))
                if (Code05_Duathlon2.low[v] >= Code05_Duathlon2.dfn[u]):
                    Code05_Duathlon2.cntn = jcast('int', (Code05_Duathlon2.cntn + 1))
                    Code05_Duathlon2.addEdge2(Code05_Duathlon2.cntn, u)
                    Code05_Duathlon2.addEdge2(u, Code05_Duathlon2.cntn)
                    Code05_Duathlon2.deg[Code05_Duathlon2.cntn] = jcast('int', (Code05_Duathlon2.deg[Code05_Duathlon2.cntn] + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code05_Duathlon2.sta[((_java_obj_13 := Code05_Duathlon2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code05_Duathlon2.addEdge2(Code05_Duathlon2.cntn, pop)
                        Code05_Duathlon2.addEdge2(pop, Code05_Duathlon2.cntn)
                        Code05_Duathlon2.deg[Code05_Duathlon2.cntn] = jcast('int', (Code05_Duathlon2.deg[Code05_Duathlon2.cntn] + 1))
                        if not ((pop != v)):
                            break
            else:
                jset(Code05_Duathlon2.low, u, jstatic('Math', 'min', Code05_Duathlon2.low[u], Code05_Duathlon2.dfn[v]))
            e = jcast('int', Code05_Duathlon2.next1[e])

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code05_Duathlon2.stacksize = jcast('int', 0)
        Code05_Duathlon2.push(node, jcast('int', (-1)), 0, jcast('int', (-1)))
        v = 0
        while (Code05_Duathlon2.stacksize > 0):
            Code05_Duathlon2.pop()
            if (Code05_Duathlon2.status == jcast('int', (-1))):
                Code05_Duathlon2.total = jcast('int', (Code05_Duathlon2.total + 1))
                jset(Code05_Duathlon2.dfn, Code05_Duathlon2.u, jset(Code05_Duathlon2.low, Code05_Duathlon2.u, ((_java_obj_16 := Code05_Duathlon2), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code05_Duathlon2.sta, ((_java_obj_19 := Code05_Duathlon2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code05_Duathlon2.u)
                Code05_Duathlon2.e = jcast('int', Code05_Duathlon2.head1[Code05_Duathlon2.u])
            else:
                v = jcast('int', Code05_Duathlon2.to1[Code05_Duathlon2.e])
                if (Code05_Duathlon2.status == 0):
                    jset(Code05_Duathlon2.low, Code05_Duathlon2.u, jstatic('Math', 'min', Code05_Duathlon2.low[Code05_Duathlon2.u], Code05_Duathlon2.low[v]))
                    if (Code05_Duathlon2.low[v] >= Code05_Duathlon2.dfn[Code05_Duathlon2.u]):
                        Code05_Duathlon2.cntn = jcast('int', (Code05_Duathlon2.cntn + 1))
                        Code05_Duathlon2.addEdge2(Code05_Duathlon2.cntn, Code05_Duathlon2.u)
                        Code05_Duathlon2.addEdge2(Code05_Duathlon2.u, Code05_Duathlon2.cntn)
                        Code05_Duathlon2.deg[Code05_Duathlon2.cntn] = jcast('int', (Code05_Duathlon2.deg[Code05_Duathlon2.cntn] + 1))
                        pop = 0
                        while True:
                            pop = jcast('int', Code05_Duathlon2.sta[((_java_obj_22 := Code05_Duathlon2), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                            Code05_Duathlon2.addEdge2(Code05_Duathlon2.cntn, pop)
                            Code05_Duathlon2.addEdge2(pop, Code05_Duathlon2.cntn)
                            Code05_Duathlon2.deg[Code05_Duathlon2.cntn] = jcast('int', (Code05_Duathlon2.deg[Code05_Duathlon2.cntn] + 1))
                            if not ((pop != v)):
                                break
                else:
                    jset(Code05_Duathlon2.low, Code05_Duathlon2.u, jstatic('Math', 'min', Code05_Duathlon2.low[Code05_Duathlon2.u], Code05_Duathlon2.dfn[v]))
                Code05_Duathlon2.e = jcast('int', Code05_Duathlon2.next1[Code05_Duathlon2.e])
            if (Code05_Duathlon2.e != 0):
                v = jcast('int', Code05_Duathlon2.to1[Code05_Duathlon2.e])
                if (Code05_Duathlon2.dfn[v] == 0):
                    Code05_Duathlon2.push(Code05_Duathlon2.u, 0, 0, Code05_Duathlon2.e)
                    Code05_Duathlon2.push(v, jcast('int', (-1)), 0, jcast('int', (-1)))
                else:
                    Code05_Duathlon2.push(Code05_Duathlon2.u, 1, 0, Code05_Duathlon2.e)

    # 递归版
    @staticmethod
    def dpOnTree1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code05_Duathlon2.head2[u])
        while (e > 0):
            v = jcast('int', Code05_Duathlon2.to2[e])
            if (v != fa):
                Code05_Duathlon2.dpOnTree1(v, u)
                if (u <= Code05_Duathlon2.n):
                    Code05_Duathlon2.ans = jcast('long', jcast('long', jadd(Code05_Duathlon2.ans, jcast('long', (jcast('long', (1 * Code05_Duathlon2.siz[v])) * jcast('int', (jcast('int', (Code05_Duathlon2.total - Code05_Duathlon2.siz[v])) - 1)))))))
                else:
                    Code05_Duathlon2.ans = jcast('long', jcast('long', jadd(Code05_Duathlon2.ans, jcast('long', (jcast('long', (jcast('long', (1 * Code05_Duathlon2.siz[v])) * jcast('int', (Code05_Duathlon2.deg[u] - 2)))) * jcast('int', (Code05_Duathlon2.total - Code05_Duathlon2.siz[v])))))))
                Code05_Duathlon2.siz[u] = jcast('int', jcast('int', jadd(Code05_Duathlon2.siz[u], Code05_Duathlon2.siz[v])))
            e = jcast('int', Code05_Duathlon2.next2[e])
        Code05_Duathlon2.siz[u] = jcast('int', jcast('int', jadd(Code05_Duathlon2.siz[u], (1 if (u <= Code05_Duathlon2.n) else 0))))
        if (u <= Code05_Duathlon2.n):
            Code05_Duathlon2.ans = jcast('long', jcast('long', jadd(Code05_Duathlon2.ans, jcast('long', (jcast('long', (1 * jcast('int', (Code05_Duathlon2.siz[u] - 1)))) * jcast('int', (Code05_Duathlon2.total - Code05_Duathlon2.siz[u])))))))
        else:
            Code05_Duathlon2.ans = jcast('long', jcast('long', jadd(Code05_Duathlon2.ans, jcast('long', (jcast('long', (jcast('long', (1 * Code05_Duathlon2.siz[u])) * jcast('int', (Code05_Duathlon2.deg[u] - 2)))) * jcast('int', (Code05_Duathlon2.total - Code05_Duathlon2.siz[u])))))))

    # 迭代版
    @staticmethod
    def dpOnTree2(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code05_Duathlon2.stacksize = jcast('int', 0)
        Code05_Duathlon2.push(cur, 0, Code05_Duathlon2.fa, jcast('int', (-1)))
        while (Code05_Duathlon2.stacksize > 0):
            Code05_Duathlon2.pop()
            if (Code05_Duathlon2.e == jcast('int', (-1))):
                Code05_Duathlon2.e = jcast('int', Code05_Duathlon2.head2[Code05_Duathlon2.u])
            else:
                Code05_Duathlon2.e = jcast('int', Code05_Duathlon2.next2[Code05_Duathlon2.e])
            if (Code05_Duathlon2.e != 0):
                Code05_Duathlon2.push(Code05_Duathlon2.u, 0, Code05_Duathlon2.fa, Code05_Duathlon2.e)
                if (Code05_Duathlon2.to2[Code05_Duathlon2.e] != Code05_Duathlon2.fa):
                    Code05_Duathlon2.push(Code05_Duathlon2.to2[Code05_Duathlon2.e], 0, Code05_Duathlon2.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code05_Duathlon2.head2[Code05_Duathlon2.u])
                while (ei > 0):
                    v = jcast('int', Code05_Duathlon2.to2[ei])
                    if (v != Code05_Duathlon2.fa):
                        if (Code05_Duathlon2.u <= Code05_Duathlon2.n):
                            Code05_Duathlon2.ans = jcast('long', jcast('long', jadd(Code05_Duathlon2.ans, jcast('long', (jcast('long', (1 * Code05_Duathlon2.siz[v])) * jcast('int', (jcast('int', (Code05_Duathlon2.total - Code05_Duathlon2.siz[v])) - 1)))))))
                        else:
                            Code05_Duathlon2.ans = jcast('long', jcast('long', jadd(Code05_Duathlon2.ans, jcast('long', (jcast('long', (jcast('long', (1 * Code05_Duathlon2.siz[v])) * jcast('int', (Code05_Duathlon2.deg[Code05_Duathlon2.u] - 2)))) * jcast('int', (Code05_Duathlon2.total - Code05_Duathlon2.siz[v])))))))
                        Code05_Duathlon2.siz[Code05_Duathlon2.u] = jcast('int', jcast('int', jadd(Code05_Duathlon2.siz[Code05_Duathlon2.u], Code05_Duathlon2.siz[v])))
                    ei = jcast('int', Code05_Duathlon2.next2[ei])
                Code05_Duathlon2.siz[Code05_Duathlon2.u] = jcast('int', jcast('int', jadd(Code05_Duathlon2.siz[Code05_Duathlon2.u], (1 if (Code05_Duathlon2.u <= Code05_Duathlon2.n) else 0))))
                if (Code05_Duathlon2.u <= Code05_Duathlon2.n):
                    Code05_Duathlon2.ans = jcast('long', jcast('long', jadd(Code05_Duathlon2.ans, jcast('long', (jcast('long', (1 * jcast('int', (Code05_Duathlon2.siz[Code05_Duathlon2.u] - 1)))) * jcast('int', (Code05_Duathlon2.total - Code05_Duathlon2.siz[Code05_Duathlon2.u])))))))
                else:
                    Code05_Duathlon2.ans = jcast('long', jcast('long', jadd(Code05_Duathlon2.ans, jcast('long', (jcast('long', (jcast('long', (1 * Code05_Duathlon2.siz[Code05_Duathlon2.u])) * jcast('int', (Code05_Duathlon2.deg[Code05_Duathlon2.u] - 2)))) * jcast('int', (Code05_Duathlon2.total - Code05_Duathlon2.siz[Code05_Duathlon2.u])))))))

    @staticmethod
    def main(args):
        in_ = Code05_Duathlon2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Duathlon2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Duathlon2.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_Duathlon2.cntn = jcast('int', Code05_Duathlon2.n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code05_Duathlon2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code05_Duathlon2.addEdge1(u, v)
            Code05_Duathlon2.addEdge1(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Duathlon2.n):
            if (Code05_Duathlon2.dfn[i] == 0):
                Code05_Duathlon2.total = jcast('int', 0)
                # tarjan1(i);
                Code05_Duathlon2.tarjan2(i)
                # dpOnTree1(i, 0);
                Code05_Duathlon2.dpOnTree2(i, 0)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_Duathlon2.ans)
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
            return jcast('int', self.buffer[((_java_obj_25 := self), (_java_key_26 := 'ptr'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))), _java_old_27)[4]])

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
            raise TypeError("No matching overload for Code05_Duathlon2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Duathlon2.MAXN = jcast('int', 100001)
Code05_Duathlon2.MAXM = jcast('int', 200001)
Code05_Duathlon2.n = jcast('int', 0)
Code05_Duathlon2.m = jcast('int', 0)
Code05_Duathlon2.cntn = jcast('int', 0)
Code05_Duathlon2.head1 = jarray('int', [Code05_Duathlon2.MAXN])
Code05_Duathlon2.next1 = jarray('int', [jcast('int', (Code05_Duathlon2.MAXM << (1 & 31)))])
Code05_Duathlon2.to1 = jarray('int', [jcast('int', (Code05_Duathlon2.MAXM << (1 & 31)))])
Code05_Duathlon2.cnt1 = jcast('int', 0)
Code05_Duathlon2.head2 = jarray('int', [jcast('int', (Code05_Duathlon2.MAXN << (1 & 31)))])
Code05_Duathlon2.next2 = jarray('int', [jcast('int', (Code05_Duathlon2.MAXM << (2 & 31)))])
Code05_Duathlon2.to2 = jarray('int', [jcast('int', (Code05_Duathlon2.MAXM << (2 & 31)))])
Code05_Duathlon2.cnt2 = jcast('int', 0)
Code05_Duathlon2.dfn = jarray('int', [Code05_Duathlon2.MAXN])
Code05_Duathlon2.low = jarray('int', [Code05_Duathlon2.MAXN])
Code05_Duathlon2.cntd = jcast('int', 0)
Code05_Duathlon2.sta = jarray('int', [Code05_Duathlon2.MAXN])
Code05_Duathlon2.top = jcast('int', 0)
Code05_Duathlon2.deg = jarray('int', [jcast('int', (Code05_Duathlon2.MAXN << (1 & 31)))])
Code05_Duathlon2.siz = jarray('int', [jcast('int', (Code05_Duathlon2.MAXN << (1 & 31)))])
Code05_Duathlon2.total = jcast('int', 0)
Code05_Duathlon2.ans = jcast('long', 0)
Code05_Duathlon2.stack = jarray('int', [jcast('int', (Code05_Duathlon2.MAXN << (1 & 31))), 4])
Code05_Duathlon2.u = jcast('int', 0)
Code05_Duathlon2.status = jcast('int', 0)
Code05_Duathlon2.fa = jcast('int', 0)
Code05_Duathlon2.e = jcast('int', 0)
Code05_Duathlon2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code05_Duathlon2.main([])
