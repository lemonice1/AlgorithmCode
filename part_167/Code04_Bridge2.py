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

# 桥梁，Python版
# 有n个点组成的无向图，依次给出m条无向边
# u v w : u到v的边，边权为w，边权同时代表限重
# 如果开车从边上经过，车的重量 <= 边的限重，车才能走过这条边
# 接下来有q条操作，每条操作的格式如下
# 操作 1 eid tow : 编号为eid的边，边权变成tow
# 操作 2 nid car : 编号为nid的点出发，车重为car，查询能到达几个不同的点
# 1 <= n <= 5 * 10^4    0 <= m <= 10^5
# 1 <= q <= 10^5        1 <= 其他数据 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P5443
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Bridge2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXQ': 'MAXQ', 'n': 'n', 'm': 'm', 'q': 'q', 'blen': 'blen', 'bnum': 'bnum', 'u': 'u', 'v': 'v', 'w': 'w', 'op': 'op', 'eid': 'eid', 'tow': 'tow', 'nid': 'nid', 'car': 'car', 'edge': 'edge', 'change': 'change', 'curw': 'curw', 'operate': 'operate', 'query': 'query', 'update': 'update', 'fa': 'fa', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'arr1': 'arr1', 'arr2': 'arr2', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    MAXQ = 0
    n = 0
    m = 0
    q = 0
    blen = 0
    bnum = 0
    u = None
    v = None
    w = None
    op = None
    eid = None
    tow = None
    nid = None
    car = None
    # edge是所有边的编号
    # change表示边的分类
    # curw表示边最新的权值
    edge = None
    change = None
    curw = None
    # operate是所有操作的编号
    # query是当前操作块查询操作的编号
    # update是当前操作块修改操作的编号
    operate = None
    query = None
    update = None
    # 可撤销并查集
    fa = None
    siz = None
    rollback = None
    opsize = 0
    # 归并的辅助数组
    arr1 = None
    arr2 = None
    # 所有查询的答案
    ans = None
    # idx[l..r]都是编号，编号根据val[编号]的值从大到小排序，手写双指针快排
    @staticmethod
    def sort(idx, val, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', val[idx[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))]])
        tmp = 0
        while (i <= j):
            while (val[idx[i]] > pivot):
                i = jcast('int', (i + 1))
            while (val[idx[j]] < pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', idx[i])
                idx[i] = jcast('int', idx[j])
                idx[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code04_Bridge2.sort(idx, val, l, j)
        Code04_Bridge2.sort(idx, val, i, r)

    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code04_Bridge2.n):
            Code04_Bridge2.fa[i] = jcast('int', i)
            Code04_Bridge2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(x):
        x = jcast('int', x)
        while (x != Code04_Bridge2.fa[x]):
            x = jcast('int', Code04_Bridge2.fa[x])
        return jcast('int', x)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code04_Bridge2.find(x))
        fy = jcast('int', Code04_Bridge2.find(y))
        if (fx == fy):
            return
        if (Code04_Bridge2.siz[fx] < Code04_Bridge2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code04_Bridge2.fa[fy] = jcast('int', fx)
        Code04_Bridge2.siz[fx] = jcast('int', jcast('int', jadd(Code04_Bridge2.siz[fx], Code04_Bridge2.siz[fy])))
        jset(Code04_Bridge2.rollback[((_java_obj_1 := Code04_Bridge2), (_java_key_2 := 'opsize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, fx)
        jset(Code04_Bridge2.rollback[Code04_Bridge2.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = 0
        fy = 0
        while (Code04_Bridge2.opsize > 0):
            fx = jcast('int', Code04_Bridge2.rollback[Code04_Bridge2.opsize][0])
            fy = jcast('int', Code04_Bridge2.rollback[Code04_Bridge2.opsize][1])
            Code04_Bridge2.fa[fy] = jcast('int', fy)
            Code04_Bridge2.siz[fx] = jcast('int', jcast('int', (Code04_Bridge2.siz[fx] - Code04_Bridge2.siz[fy])))
            Code04_Bridge2.opsize = jcast('int', (Code04_Bridge2.opsize - 1))

    @staticmethod
    def merge():
        siz1 = jcast('int', 0)
        siz2 = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Bridge2.m):
            if Code04_Bridge2.change[Code04_Bridge2.edge[i]]:
                jset(Code04_Bridge2.arr1, (siz1 := jcast('int', (siz1 + (1)))), Code04_Bridge2.edge[i])
            else:
                jset(Code04_Bridge2.arr2, (siz2 := jcast('int', (siz2 + (1)))), Code04_Bridge2.edge[i])
            i = jcast('int', (i + 1))
        Code04_Bridge2.sort(Code04_Bridge2.arr1, Code04_Bridge2.w, 1, siz1)
        i = jcast('int', 0)
        p1 = jcast('int', 1)
        p2 = jcast('int', 1)
        while ((p1 <= siz1) and (p2 <= siz2)):
            jset(Code04_Bridge2.edge, (i := jcast('int', (i + (1)))), (Code04_Bridge2.arr1[((_java_old_4 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_4)[2]] if (Code04_Bridge2.w[Code04_Bridge2.arr1[p1]] >= Code04_Bridge2.w[Code04_Bridge2.arr2[p2]]) else Code04_Bridge2.arr2[((_java_old_5 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_5)[2]]))
        while (p1 <= siz1):
            jset(Code04_Bridge2.edge, (i := jcast('int', (i + (1)))), Code04_Bridge2.arr1[((_java_old_6 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_6)[2]])
        while (p2 <= siz2):
            jset(Code04_Bridge2.edge, (i := jcast('int', (i + (1)))), Code04_Bridge2.arr2[((_java_old_7 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_7)[2]])

    # 当前操作编号[l..r]，之前的所有修改操作都已生效
    # 所有边的编号edge[1..m]，按照边权从大到小排序
    # 处理当前操作块的所有操作
    @staticmethod
    def compute(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        # 重建并查集，目前没有任何连通性
        # 清空边的修改标记
        Code04_Bridge2.build()
        jstatic('Arrays', 'fill', Code04_Bridge2.change, False)
        cntu = jcast('int', 0)
        cntq = jcast('int', 0)
        i = jcast('int', l)
        while (i <= r):
            if (Code04_Bridge2.op[Code04_Bridge2.operate[i]] == 1):
                jset(Code04_Bridge2.change, Code04_Bridge2.eid[Code04_Bridge2.operate[i]], True)
                jset(Code04_Bridge2.update, (cntu := jcast('int', (cntu + (1)))), Code04_Bridge2.operate[i])
            else:
                jset(Code04_Bridge2.query, (cntq := jcast('int', (cntq + (1)))), Code04_Bridge2.operate[i])
            i = jcast('int', (i + 1))
        # 查询操作的所有编号，根据车重从大到小排序
        # 然后依次处理所有查询
        Code04_Bridge2.sort(Code04_Bridge2.query, Code04_Bridge2.car, 1, cntq)
        i = jcast('int', 1)
        j = jcast('int', 1)
        while (i <= cntq):
            # 边权 >= 当前车重 的边全部连上，注意这是不回退的
            while ((j <= Code04_Bridge2.m) and (Code04_Bridge2.w[Code04_Bridge2.edge[j]] >= Code04_Bridge2.car[Code04_Bridge2.query[i]])):
                if (not Code04_Bridge2.change[Code04_Bridge2.edge[j]]):
                    Code04_Bridge2.union(Code04_Bridge2.u[Code04_Bridge2.edge[j]], Code04_Bridge2.v[Code04_Bridge2.edge[j]])
                j = jcast('int', (j + 1))
            # 注意需要用可撤销并查集，撤销会改值的边
            Code04_Bridge2.opsize = jcast('int', 0)
            # 会改值的边，边权先继承改之前的值
            k = jcast('int', 1)
            while (k <= cntu):
                jset(Code04_Bridge2.curw, Code04_Bridge2.eid[Code04_Bridge2.update[k]], Code04_Bridge2.w[Code04_Bridge2.eid[Code04_Bridge2.update[k]]])
                k = jcast('int', (k + 1))
            # 修改操作的时序 < 当前查询操作的时序，那么相关边的边权改成最新值
            k = jcast('int', 1)
            while ((k <= cntu) and (Code04_Bridge2.update[k] < Code04_Bridge2.query[i])):
                jset(Code04_Bridge2.curw, Code04_Bridge2.eid[Code04_Bridge2.update[k]], Code04_Bridge2.tow[Code04_Bridge2.update[k]])
                k = jcast('int', (k + 1))
            # 会改值的边，其中 边权 >= 当前车重 的边全部连上
            k = jcast('int', 1)
            while (k <= cntu):
                if (Code04_Bridge2.curw[Code04_Bridge2.eid[Code04_Bridge2.update[k]]] >= Code04_Bridge2.car[Code04_Bridge2.query[i]]):
                    Code04_Bridge2.union(Code04_Bridge2.u[Code04_Bridge2.eid[Code04_Bridge2.update[k]]], Code04_Bridge2.v[Code04_Bridge2.eid[Code04_Bridge2.update[k]]])
                k = jcast('int', (k + 1))
            # 并查集修改完毕，查询答案
            jset(Code04_Bridge2.ans, Code04_Bridge2.query[i], Code04_Bridge2.siz[Code04_Bridge2.find(Code04_Bridge2.nid[Code04_Bridge2.query[i]])])
            # 并查集的撤销
            Code04_Bridge2.undo()
            i = jcast('int', (i + 1))
        # 所有会改值的边，边权修改，因为即将去下个操作块
        i = jcast('int', 1)
        while (i <= cntu):
            jset(Code04_Bridge2.w, Code04_Bridge2.eid[Code04_Bridge2.update[i]], Code04_Bridge2.tow[Code04_Bridge2.update[i]])
            i = jcast('int', (i + 1))
        # 没改值的边和改了值的边，根据边权从大到小合并
        Code04_Bridge2.merge()

    @staticmethod
    def prepare():
        log2n = jcast('int', 0)
        while (jcast('int', (1 << (log2n & 31))) <= jcast('int', (Code04_Bridge2.n >> (1 & 31)))):
            log2n = jcast('int', (log2n + 1))
        Code04_Bridge2.blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jstatic('Math', 'sqrt', jcast('int', (Code04_Bridge2.q * log2n))))))
        Code04_Bridge2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code04_Bridge2.q, Code04_Bridge2.blen)) - 1)), Code04_Bridge2.blen)))
        Code04_Bridge2.sort(Code04_Bridge2.edge, Code04_Bridge2.w, 1, Code04_Bridge2.m)

    @staticmethod
    def main(args):
        in_ = Code04_Bridge2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Bridge2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Bridge2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Bridge2.m):
            jset(Code04_Bridge2.u, i, jcall(in_, 'nextInt'))
            jset(Code04_Bridge2.v, i, jcall(in_, 'nextInt'))
            jset(Code04_Bridge2.w, i, jcall(in_, 'nextInt'))
            Code04_Bridge2.edge[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code04_Bridge2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Bridge2.q):
            jset(Code04_Bridge2.op, i, jcall(in_, 'nextInt'))
            if (Code04_Bridge2.op[i] == 1):
                jset(Code04_Bridge2.eid, i, jcall(in_, 'nextInt'))
                jset(Code04_Bridge2.tow, i, jcall(in_, 'nextInt'))
            else:
                jset(Code04_Bridge2.nid, i, jcall(in_, 'nextInt'))
                jset(Code04_Bridge2.car, i, jcall(in_, 'nextInt'))
            Code04_Bridge2.operate[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code04_Bridge2.prepare()
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= Code04_Bridge2.bnum):
            l = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code04_Bridge2.blen)), 1)))
            r = jcast('int', jstatic('Math', 'min', jcast('int', (i * Code04_Bridge2.blen)), Code04_Bridge2.q))
            Code04_Bridge2.compute(l, r)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Bridge2.q):
            if (Code04_Bridge2.op[i] == 2):
                jcall(out, 'println', Code04_Bridge2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_8 := self), (_java_key_9 := 'ptr'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_Bridge2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Bridge2.MAXN = jcast('int', 50001)
Code04_Bridge2.MAXM = jcast('int', 100001)
Code04_Bridge2.MAXQ = jcast('int', 100001)
Code04_Bridge2.n = jcast('int', 0)
Code04_Bridge2.m = jcast('int', 0)
Code04_Bridge2.q = jcast('int', 0)
Code04_Bridge2.blen = jcast('int', 0)
Code04_Bridge2.bnum = jcast('int', 0)
Code04_Bridge2.u = jarray('int', [Code04_Bridge2.MAXM])
Code04_Bridge2.v = jarray('int', [Code04_Bridge2.MAXM])
Code04_Bridge2.w = jarray('int', [Code04_Bridge2.MAXM])
Code04_Bridge2.op = jarray('int', [Code04_Bridge2.MAXQ])
Code04_Bridge2.eid = jarray('int', [Code04_Bridge2.MAXQ])
Code04_Bridge2.tow = jarray('int', [Code04_Bridge2.MAXQ])
Code04_Bridge2.nid = jarray('int', [Code04_Bridge2.MAXQ])
Code04_Bridge2.car = jarray('int', [Code04_Bridge2.MAXQ])
Code04_Bridge2.edge = jarray('int', [Code04_Bridge2.MAXM])
Code04_Bridge2.change = jarray('boolean', [Code04_Bridge2.MAXM])
Code04_Bridge2.curw = jarray('int', [Code04_Bridge2.MAXM])
Code04_Bridge2.operate = jarray('int', [Code04_Bridge2.MAXQ])
Code04_Bridge2.query = jarray('int', [Code04_Bridge2.MAXQ])
Code04_Bridge2.update = jarray('int', [Code04_Bridge2.MAXQ])
Code04_Bridge2.fa = jarray('int', [Code04_Bridge2.MAXN])
Code04_Bridge2.siz = jarray('int', [Code04_Bridge2.MAXN])
Code04_Bridge2.rollback = jarray('int', [Code04_Bridge2.MAXM, 2])
Code04_Bridge2.opsize = jcast('int', 0)
Code04_Bridge2.arr1 = jarray('int', [Code04_Bridge2.MAXM])
Code04_Bridge2.arr2 = jarray('int', [Code04_Bridge2.MAXM])
Code04_Bridge2.ans = jarray('int', [Code04_Bridge2.MAXQ])

if __name__ == '__main__':
    Code04_Bridge2.main([])
