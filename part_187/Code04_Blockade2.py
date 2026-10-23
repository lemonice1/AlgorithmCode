# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 城市阻断，Python版
# 给定一张无向图，一共n个点、m条边，所有点保证连通
# 对每个点i，打印如下的答案
# 节点i相连的边去掉以后，无向图有多少点对(x, y)，x和y不连通
# 注意(x, y)和(y, x)是不同点对
# 删掉和i相连的边，但是节点i本身不删掉，要参与点对数量的计算
# 1 <= n <= 10^5
# 1 <= m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3469
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Blockade2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'siz': 'siz', 'ans': 'ans', 'stack': 'stack', 'u': 'u', 'status': 'status', 'fa': 'fa', 'e': 'e', 'stacksize': 'stacksize'}
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
    # dfs过程中，子树中的圆点数量
    siz = None
    # 每个原图中的点，如果把相邻的边删掉，所统计的答案
    ans = None
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
        jset(Code04_Blockade2.stack[Code04_Blockade2.stacksize], 0, u)
        jset(Code04_Blockade2.stack[Code04_Blockade2.stacksize], 1, status)
        jset(Code04_Blockade2.stack[Code04_Blockade2.stacksize], 2, fa)
        jset(Code04_Blockade2.stack[Code04_Blockade2.stacksize], 3, e)
        Code04_Blockade2.stacksize = jcast('int', (Code04_Blockade2.stacksize + 1))

    @staticmethod
    def pop():
        Code04_Blockade2.stacksize = jcast('int', (Code04_Blockade2.stacksize - 1))
        Code04_Blockade2.u = jcast('int', Code04_Blockade2.stack[Code04_Blockade2.stacksize][0])
        Code04_Blockade2.status = jcast('int', Code04_Blockade2.stack[Code04_Blockade2.stacksize][1])
        Code04_Blockade2.fa = jcast('int', Code04_Blockade2.stack[Code04_Blockade2.stacksize][2])
        Code04_Blockade2.e = jcast('int', Code04_Blockade2.stack[Code04_Blockade2.stacksize][3])

    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_Blockade2.next1, ((_java_obj_1 := Code04_Blockade2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Blockade2.head1[u])
        Code04_Blockade2.to1[Code04_Blockade2.cnt1] = jcast('int', v)
        Code04_Blockade2.head1[u] = jcast('int', Code04_Blockade2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_Blockade2.next2, ((_java_obj_4 := Code04_Blockade2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_Blockade2.head2[u])
        Code04_Blockade2.to2[Code04_Blockade2.cnt2] = jcast('int', v)
        Code04_Blockade2.head2[u] = jcast('int', Code04_Blockade2.cnt2)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code04_Blockade2.dfn, u, jset(Code04_Blockade2.low, u, ((_java_obj_7 := Code04_Blockade2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code04_Blockade2.sta, ((_java_obj_10 := Code04_Blockade2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code04_Blockade2.head1[u])
        while (e > 0):
            v = jcast('int', Code04_Blockade2.to1[e])
            if (Code04_Blockade2.dfn[v] == 0):
                Code04_Blockade2.tarjan1(v)
                jset(Code04_Blockade2.low, u, jstatic('Math', 'min', Code04_Blockade2.low[u], Code04_Blockade2.low[v]))
                if (Code04_Blockade2.low[v] >= Code04_Blockade2.dfn[u]):
                    Code04_Blockade2.cntn = jcast('int', (Code04_Blockade2.cntn + 1))
                    Code04_Blockade2.addEdge2(Code04_Blockade2.cntn, u)
                    Code04_Blockade2.addEdge2(u, Code04_Blockade2.cntn)
                    pop = 0
                    while True:
                        pop = jcast('int', Code04_Blockade2.sta[((_java_obj_13 := Code04_Blockade2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code04_Blockade2.addEdge2(Code04_Blockade2.cntn, pop)
                        Code04_Blockade2.addEdge2(pop, Code04_Blockade2.cntn)
                        if not ((pop != v)):
                            break
            else:
                jset(Code04_Blockade2.low, u, jstatic('Math', 'min', Code04_Blockade2.low[u], Code04_Blockade2.dfn[v]))
            e = jcast('int', Code04_Blockade2.next1[e])

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code04_Blockade2.stacksize = jcast('int', 0)
        Code04_Blockade2.push(node, jcast('int', (-1)), 0, jcast('int', (-1)))
        v = 0
        while (Code04_Blockade2.stacksize > 0):
            Code04_Blockade2.pop()
            if (Code04_Blockade2.status == jcast('int', (-1))):
                jset(Code04_Blockade2.dfn, Code04_Blockade2.u, jset(Code04_Blockade2.low, Code04_Blockade2.u, ((_java_obj_16 := Code04_Blockade2), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code04_Blockade2.sta, ((_java_obj_19 := Code04_Blockade2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code04_Blockade2.u)
                Code04_Blockade2.e = jcast('int', Code04_Blockade2.head1[Code04_Blockade2.u])
            else:
                v = jcast('int', Code04_Blockade2.to1[Code04_Blockade2.e])
                if (Code04_Blockade2.status == 0):
                    jset(Code04_Blockade2.low, Code04_Blockade2.u, jstatic('Math', 'min', Code04_Blockade2.low[Code04_Blockade2.u], Code04_Blockade2.low[v]))
                    if (Code04_Blockade2.low[v] >= Code04_Blockade2.dfn[Code04_Blockade2.u]):
                        Code04_Blockade2.cntn = jcast('int', (Code04_Blockade2.cntn + 1))
                        Code04_Blockade2.addEdge2(Code04_Blockade2.cntn, Code04_Blockade2.u)
                        Code04_Blockade2.addEdge2(Code04_Blockade2.u, Code04_Blockade2.cntn)
                        pop = 0
                        while True:
                            pop = jcast('int', Code04_Blockade2.sta[((_java_obj_22 := Code04_Blockade2), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                            Code04_Blockade2.addEdge2(Code04_Blockade2.cntn, pop)
                            Code04_Blockade2.addEdge2(pop, Code04_Blockade2.cntn)
                            if not ((pop != v)):
                                break
                else:
                    jset(Code04_Blockade2.low, Code04_Blockade2.u, jstatic('Math', 'min', Code04_Blockade2.low[Code04_Blockade2.u], Code04_Blockade2.dfn[v]))
                Code04_Blockade2.e = jcast('int', Code04_Blockade2.next1[Code04_Blockade2.e])
            if (Code04_Blockade2.e != 0):
                v = jcast('int', Code04_Blockade2.to1[Code04_Blockade2.e])
                if (Code04_Blockade2.dfn[v] == 0):
                    Code04_Blockade2.push(Code04_Blockade2.u, 0, 0, Code04_Blockade2.e)
                    Code04_Blockade2.push(v, jcast('int', (-1)), 0, jcast('int', (-1)))
                else:
                    Code04_Blockade2.push(Code04_Blockade2.u, 1, 0, Code04_Blockade2.e)

    # 递归版
    @staticmethod
    def dpOnTree1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code04_Blockade2.head2[u])
        while (e > 0):
            v = jcast('int', Code04_Blockade2.to2[e])
            if (v != fa):
                Code04_Blockade2.dpOnTree1(v, u)
                if (u <= Code04_Blockade2.n):
                    Code04_Blockade2.ans[u] = jcast('long', jcast('long', jadd(Code04_Blockade2.ans[u], jcast('long', (jcast('long', (1 * Code04_Blockade2.siz[v])) * jcast('int', (jcast('int', (Code04_Blockade2.n - Code04_Blockade2.siz[v])) - 1)))))))
                Code04_Blockade2.siz[u] = jcast('int', jcast('int', jadd(Code04_Blockade2.siz[u], Code04_Blockade2.siz[v])))
            e = jcast('int', Code04_Blockade2.next2[e])
        Code04_Blockade2.siz[u] = jcast('int', jcast('int', jadd(Code04_Blockade2.siz[u], (1 if (u <= Code04_Blockade2.n) else 0))))
        if (u <= Code04_Blockade2.n):
            Code04_Blockade2.ans[u] = jcast('long', jcast('long', jadd(Code04_Blockade2.ans[u], jcast('long', (jcast('long', (1 * jcast('int', (Code04_Blockade2.n - Code04_Blockade2.siz[u])))) * jcast('int', (Code04_Blockade2.siz[u] - 1)))))))
            Code04_Blockade2.ans[u] = jcast('long', jcast('long', jadd(Code04_Blockade2.ans[u], jcast('long', (2 * jcast('int', (Code04_Blockade2.n - 1)))))))

    # 迭代版
    @staticmethod
    def dpOnTree2(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code04_Blockade2.stacksize = jcast('int', 0)
        Code04_Blockade2.push(cur, 0, Code04_Blockade2.fa, jcast('int', (-1)))
        while (Code04_Blockade2.stacksize > 0):
            Code04_Blockade2.pop()
            if (Code04_Blockade2.e == jcast('int', (-1))):
                Code04_Blockade2.e = jcast('int', Code04_Blockade2.head2[Code04_Blockade2.u])
            else:
                Code04_Blockade2.e = jcast('int', Code04_Blockade2.next2[Code04_Blockade2.e])
            if (Code04_Blockade2.e != 0):
                Code04_Blockade2.push(Code04_Blockade2.u, 0, Code04_Blockade2.fa, Code04_Blockade2.e)
                if (Code04_Blockade2.to2[Code04_Blockade2.e] != Code04_Blockade2.fa):
                    Code04_Blockade2.push(Code04_Blockade2.to2[Code04_Blockade2.e], 0, Code04_Blockade2.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code04_Blockade2.head2[Code04_Blockade2.u])
                while (ei > 0):
                    v = jcast('int', Code04_Blockade2.to2[ei])
                    if (v != Code04_Blockade2.fa):
                        if (Code04_Blockade2.u <= Code04_Blockade2.n):
                            Code04_Blockade2.ans[Code04_Blockade2.u] = jcast('long', jcast('long', jadd(Code04_Blockade2.ans[Code04_Blockade2.u], jcast('long', (jcast('long', (1 * Code04_Blockade2.siz[v])) * jcast('int', (jcast('int', (Code04_Blockade2.n - Code04_Blockade2.siz[v])) - 1)))))))
                        Code04_Blockade2.siz[Code04_Blockade2.u] = jcast('int', jcast('int', jadd(Code04_Blockade2.siz[Code04_Blockade2.u], Code04_Blockade2.siz[v])))
                    ei = jcast('int', Code04_Blockade2.next2[ei])
                Code04_Blockade2.siz[Code04_Blockade2.u] = jcast('int', jcast('int', jadd(Code04_Blockade2.siz[Code04_Blockade2.u], (1 if (Code04_Blockade2.u <= Code04_Blockade2.n) else 0))))
                if (Code04_Blockade2.u <= Code04_Blockade2.n):
                    Code04_Blockade2.ans[Code04_Blockade2.u] = jcast('long', jcast('long', jadd(Code04_Blockade2.ans[Code04_Blockade2.u], jcast('long', (jcast('long', (1 * jcast('int', (Code04_Blockade2.n - Code04_Blockade2.siz[Code04_Blockade2.u])))) * jcast('int', (Code04_Blockade2.siz[Code04_Blockade2.u] - 1)))))))
                    Code04_Blockade2.ans[Code04_Blockade2.u] = jcast('long', jcast('long', jadd(Code04_Blockade2.ans[Code04_Blockade2.u], jcast('long', (2 * jcast('int', (Code04_Blockade2.n - 1)))))))

    @staticmethod
    def main(args):
        in_ = Code04_Blockade2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Blockade2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Blockade2.m = jcast('int', jcall(in_, 'nextInt'))
        Code04_Blockade2.cntn = jcast('int', Code04_Blockade2.n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code04_Blockade2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_Blockade2.addEdge1(u, v)
            Code04_Blockade2.addEdge1(v, u)
            i = jcast('int', (i + 1))
        # tarjan1(1);
        Code04_Blockade2.tarjan2(1)
        # dpOnTree1(1, 0);
        Code04_Blockade2.dpOnTree2(1, 0)
        i = jcast('int', 1)
        while (i <= Code04_Blockade2.n):
            jcall(out, 'println', Code04_Blockade2.ans[i])
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
            raise TypeError("No matching overload for Code04_Blockade2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Blockade2.MAXN = jcast('int', 100001)
Code04_Blockade2.MAXM = jcast('int', 500001)
Code04_Blockade2.n = jcast('int', 0)
Code04_Blockade2.m = jcast('int', 0)
Code04_Blockade2.cntn = jcast('int', 0)
Code04_Blockade2.head1 = jarray('int', [Code04_Blockade2.MAXN])
Code04_Blockade2.next1 = jarray('int', [jcast('int', (Code04_Blockade2.MAXM << (1 & 31)))])
Code04_Blockade2.to1 = jarray('int', [jcast('int', (Code04_Blockade2.MAXM << (1 & 31)))])
Code04_Blockade2.cnt1 = jcast('int', 0)
Code04_Blockade2.head2 = jarray('int', [jcast('int', (Code04_Blockade2.MAXN << (1 & 31)))])
Code04_Blockade2.next2 = jarray('int', [jcast('int', (Code04_Blockade2.MAXM << (2 & 31)))])
Code04_Blockade2.to2 = jarray('int', [jcast('int', (Code04_Blockade2.MAXM << (2 & 31)))])
Code04_Blockade2.cnt2 = jcast('int', 0)
Code04_Blockade2.dfn = jarray('int', [Code04_Blockade2.MAXN])
Code04_Blockade2.low = jarray('int', [Code04_Blockade2.MAXN])
Code04_Blockade2.cntd = jcast('int', 0)
Code04_Blockade2.sta = jarray('int', [Code04_Blockade2.MAXN])
Code04_Blockade2.top = jcast('int', 0)
Code04_Blockade2.siz = jarray('int', [jcast('int', (Code04_Blockade2.MAXN << (1 & 31)))])
Code04_Blockade2.ans = jarray('long', [Code04_Blockade2.MAXN])
Code04_Blockade2.stack = jarray('int', [jcast('int', (Code04_Blockade2.MAXN << (1 & 31))), 4])
Code04_Blockade2.u = jcast('int', 0)
Code04_Blockade2.status = jcast('int', 0)
Code04_Blockade2.fa = jcast('int', 0)
Code04_Blockade2.e = jcast('int', 0)
Code04_Blockade2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code04_Blockade2.main([])
