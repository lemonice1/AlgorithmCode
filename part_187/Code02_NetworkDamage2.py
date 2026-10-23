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

# 通讯网破坏，Python版
# 给定一张无向图，一共n个点、m条边，所有点保证连通
# 一共q条查询，格式 x y z : 如果删除点z，打印x和y是否断连
# 1 <= n <= 2 * 10^4
# 1 <= m <= 10 ^ 5
# 1 <= q <= 10 ^ 5
# 测试链接 : https://www.luogu.com.cn/problem/P3854
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_NetworkDamage2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'dep': 'dep', 'stjump': 'stjump', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
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
    dep = None
    stjump = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code02_NetworkDamage2.stack[Code02_NetworkDamage2.stacksize], 0, u)
        jset(Code02_NetworkDamage2.stack[Code02_NetworkDamage2.stacksize], 1, status)
        jset(Code02_NetworkDamage2.stack[Code02_NetworkDamage2.stacksize], 2, e)
        Code02_NetworkDamage2.stacksize = jcast('int', (Code02_NetworkDamage2.stacksize + 1))

    @staticmethod
    def pop():
        Code02_NetworkDamage2.stacksize = jcast('int', (Code02_NetworkDamage2.stacksize - 1))
        Code02_NetworkDamage2.u = jcast('int', Code02_NetworkDamage2.stack[Code02_NetworkDamage2.stacksize][0])
        Code02_NetworkDamage2.status = jcast('int', Code02_NetworkDamage2.stack[Code02_NetworkDamage2.stacksize][1])
        Code02_NetworkDamage2.e = jcast('int', Code02_NetworkDamage2.stack[Code02_NetworkDamage2.stacksize][2])

    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_NetworkDamage2.next1, ((_java_obj_1 := Code02_NetworkDamage2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_NetworkDamage2.head1[u])
        Code02_NetworkDamage2.to1[Code02_NetworkDamage2.cnt1] = jcast('int', v)
        Code02_NetworkDamage2.head1[u] = jcast('int', Code02_NetworkDamage2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_NetworkDamage2.next2, ((_java_obj_4 := Code02_NetworkDamage2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code02_NetworkDamage2.head2[u])
        Code02_NetworkDamage2.to2[Code02_NetworkDamage2.cnt2] = jcast('int', v)
        Code02_NetworkDamage2.head2[u] = jcast('int', Code02_NetworkDamage2.cnt2)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code02_NetworkDamage2.dfn, u, jset(Code02_NetworkDamage2.low, u, ((_java_obj_7 := Code02_NetworkDamage2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code02_NetworkDamage2.sta, ((_java_obj_10 := Code02_NetworkDamage2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code02_NetworkDamage2.head1[u])
        while (e > 0):
            v = jcast('int', Code02_NetworkDamage2.to1[e])
            if (Code02_NetworkDamage2.dfn[v] == 0):
                Code02_NetworkDamage2.tarjan1(v)
                jset(Code02_NetworkDamage2.low, u, jstatic('Math', 'min', Code02_NetworkDamage2.low[u], Code02_NetworkDamage2.low[v]))
                if (Code02_NetworkDamage2.low[v] >= Code02_NetworkDamage2.dfn[u]):
                    Code02_NetworkDamage2.cntn = jcast('int', (Code02_NetworkDamage2.cntn + 1))
                    Code02_NetworkDamage2.addEdge2(Code02_NetworkDamage2.cntn, u)
                    Code02_NetworkDamage2.addEdge2(u, Code02_NetworkDamage2.cntn)
                    pop = 0
                    while True:
                        pop = jcast('int', Code02_NetworkDamage2.sta[((_java_obj_13 := Code02_NetworkDamage2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code02_NetworkDamage2.addEdge2(Code02_NetworkDamage2.cntn, pop)
                        Code02_NetworkDamage2.addEdge2(pop, Code02_NetworkDamage2.cntn)
                        if not ((pop != v)):
                            break
            else:
                jset(Code02_NetworkDamage2.low, u, jstatic('Math', 'min', Code02_NetworkDamage2.low[u], Code02_NetworkDamage2.dfn[v]))
            e = jcast('int', Code02_NetworkDamage2.next1[e])

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code02_NetworkDamage2.stacksize = jcast('int', 0)
        Code02_NetworkDamage2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code02_NetworkDamage2.stacksize > 0):
            Code02_NetworkDamage2.pop()
            if (Code02_NetworkDamage2.status == jcast('int', (-1))):
                jset(Code02_NetworkDamage2.dfn, Code02_NetworkDamage2.u, jset(Code02_NetworkDamage2.low, Code02_NetworkDamage2.u, ((_java_obj_16 := Code02_NetworkDamage2), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code02_NetworkDamage2.sta, ((_java_obj_19 := Code02_NetworkDamage2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code02_NetworkDamage2.u)
                Code02_NetworkDamage2.e = jcast('int', Code02_NetworkDamage2.head1[Code02_NetworkDamage2.u])
            else:
                v = jcast('int', Code02_NetworkDamage2.to1[Code02_NetworkDamage2.e])
                if (Code02_NetworkDamage2.status == 0):
                    jset(Code02_NetworkDamage2.low, Code02_NetworkDamage2.u, jstatic('Math', 'min', Code02_NetworkDamage2.low[Code02_NetworkDamage2.u], Code02_NetworkDamage2.low[v]))
                    if (Code02_NetworkDamage2.low[v] >= Code02_NetworkDamage2.dfn[Code02_NetworkDamage2.u]):
                        Code02_NetworkDamage2.cntn = jcast('int', (Code02_NetworkDamage2.cntn + 1))
                        Code02_NetworkDamage2.addEdge2(Code02_NetworkDamage2.cntn, Code02_NetworkDamage2.u)
                        Code02_NetworkDamage2.addEdge2(Code02_NetworkDamage2.u, Code02_NetworkDamage2.cntn)
                        pop = 0
                        while True:
                            pop = jcast('int', Code02_NetworkDamage2.sta[((_java_obj_22 := Code02_NetworkDamage2), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                            Code02_NetworkDamage2.addEdge2(Code02_NetworkDamage2.cntn, pop)
                            Code02_NetworkDamage2.addEdge2(pop, Code02_NetworkDamage2.cntn)
                            if not ((pop != v)):
                                break
                else:
                    jset(Code02_NetworkDamage2.low, Code02_NetworkDamage2.u, jstatic('Math', 'min', Code02_NetworkDamage2.low[Code02_NetworkDamage2.u], Code02_NetworkDamage2.dfn[v]))
                Code02_NetworkDamage2.e = jcast('int', Code02_NetworkDamage2.next1[Code02_NetworkDamage2.e])
            if (Code02_NetworkDamage2.e != 0):
                v = jcast('int', Code02_NetworkDamage2.to1[Code02_NetworkDamage2.e])
                if (Code02_NetworkDamage2.dfn[v] == 0):
                    Code02_NetworkDamage2.push(Code02_NetworkDamage2.u, 0, Code02_NetworkDamage2.e)
                    Code02_NetworkDamage2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code02_NetworkDamage2.push(Code02_NetworkDamage2.u, 1, Code02_NetworkDamage2.e)

    # 圆方树上建立深度和倍增表
    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_NetworkDamage2.dep[u] = jcast('int', jcast('int', jadd(Code02_NetworkDamage2.dep[fa], 1)))
        jset(Code02_NetworkDamage2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code02_NetworkDamage2.MAXP):
            jset(Code02_NetworkDamage2.stjump[u], p, Code02_NetworkDamage2.stjump[Code02_NetworkDamage2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code02_NetworkDamage2.head2[u])
        while (e > 0):
            v = jcast('int', Code02_NetworkDamage2.to2[e])
            if (v != fa):
                Code02_NetworkDamage2.dfs(v, u)
            e = jcast('int', Code02_NetworkDamage2.next2[e])

    # 圆方树上任意两点的最低公共祖先
    @staticmethod
    def getLca(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (Code02_NetworkDamage2.dep[x] < Code02_NetworkDamage2.dep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code02_NetworkDamage2.MAXP - 1)))
        while (p >= 0):
            if (Code02_NetworkDamage2.dep[Code02_NetworkDamage2.stjump[x][p]] >= Code02_NetworkDamage2.dep[y]):
                x = jcast('int', Code02_NetworkDamage2.stjump[x][p])
            p = jcast('int', (p - 1))
        if (x == y):
            return jcast('int', x)
        p = jcast('int', jcast('int', (Code02_NetworkDamage2.MAXP - 1)))
        while (p >= 0):
            if (Code02_NetworkDamage2.stjump[x][p] != Code02_NetworkDamage2.stjump[y][p]):
                x = jcast('int', Code02_NetworkDamage2.stjump[x][p])
                y = jcast('int', Code02_NetworkDamage2.stjump[y][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code02_NetworkDamage2.stjump[x][0])

    # 圆方树上任意两点间的距离
    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code02_NetworkDamage2.dep[x], Code02_NetworkDamage2.dep[y])) - jcast('int', (2 * Code02_NetworkDamage2.dep[Code02_NetworkDamage2.getLca(x, y)])))))

    @staticmethod
    def main(args):
        in_ = Code02_NetworkDamage2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_NetworkDamage2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_NetworkDamage2.m = jcast('int', jcall(in_, 'nextInt'))
        Code02_NetworkDamage2.cntn = jcast('int', Code02_NetworkDamage2.n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code02_NetworkDamage2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code02_NetworkDamage2.addEdge1(u, v)
            Code02_NetworkDamage2.addEdge1(v, u)
            i = jcast('int', (i + 1))
        # tarjan1(1);
        Code02_NetworkDamage2.tarjan2(1)
        Code02_NetworkDamage2.dfs(1, 0)
        Code02_NetworkDamage2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        z = 0
        while (i <= Code02_NetworkDamage2.q):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            z = jcast('int', jcall(in_, 'nextInt'))
            if (Code02_NetworkDamage2.getDist(x, y) == jcast('int', jadd(Code02_NetworkDamage2.getDist(x, z), Code02_NetworkDamage2.getDist(y, z)))):
                jcall(out, 'println', 'yes')
            else:
                jcall(out, 'println', 'no')
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
            raise TypeError("No matching overload for Code02_NetworkDamage2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_NetworkDamage2.MAXN = jcast('int', 20001)
Code02_NetworkDamage2.MAXM = jcast('int', 100001)
Code02_NetworkDamage2.MAXP = jcast('int', 18)
Code02_NetworkDamage2.n = jcast('int', 0)
Code02_NetworkDamage2.m = jcast('int', 0)
Code02_NetworkDamage2.q = jcast('int', 0)
Code02_NetworkDamage2.cntn = jcast('int', 0)
Code02_NetworkDamage2.head1 = jarray('int', [Code02_NetworkDamage2.MAXN])
Code02_NetworkDamage2.next1 = jarray('int', [jcast('int', (Code02_NetworkDamage2.MAXM << (1 & 31)))])
Code02_NetworkDamage2.to1 = jarray('int', [jcast('int', (Code02_NetworkDamage2.MAXM << (1 & 31)))])
Code02_NetworkDamage2.cnt1 = jcast('int', 0)
Code02_NetworkDamage2.head2 = jarray('int', [jcast('int', (Code02_NetworkDamage2.MAXN << (1 & 31)))])
Code02_NetworkDamage2.next2 = jarray('int', [jcast('int', (Code02_NetworkDamage2.MAXM << (2 & 31)))])
Code02_NetworkDamage2.to2 = jarray('int', [jcast('int', (Code02_NetworkDamage2.MAXM << (2 & 31)))])
Code02_NetworkDamage2.cnt2 = jcast('int', 0)
Code02_NetworkDamage2.dfn = jarray('int', [Code02_NetworkDamage2.MAXN])
Code02_NetworkDamage2.low = jarray('int', [Code02_NetworkDamage2.MAXN])
Code02_NetworkDamage2.cntd = jcast('int', 0)
Code02_NetworkDamage2.sta = jarray('int', [Code02_NetworkDamage2.MAXN])
Code02_NetworkDamage2.top = jcast('int', 0)
Code02_NetworkDamage2.dep = jarray('int', [jcast('int', (Code02_NetworkDamage2.MAXN << (1 & 31)))])
Code02_NetworkDamage2.stjump = jarray('int', [jcast('int', (Code02_NetworkDamage2.MAXN << (1 & 31))), Code02_NetworkDamage2.MAXP])
Code02_NetworkDamage2.stack = jarray('int', [jcast('int', (Code02_NetworkDamage2.MAXN << (1 & 31))), 3])
Code02_NetworkDamage2.u = jcast('int', 0)
Code02_NetworkDamage2.status = jcast('int', 0)
Code02_NetworkDamage2.e = jcast('int', 0)
Code02_NetworkDamage2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code02_NetworkDamage2.main([])
