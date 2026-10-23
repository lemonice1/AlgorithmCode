# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 沙漠，Python版
# 一共n个数字，所有数字都在 1 ~ 10^9 的范围，这是范围说明
# 接下来给定s条设置说明，格式 x v ，表示第x个数的值确定是v
# 接下来给定m条关系说明，格式 l r k x1 x2 ... xk 含义如下
# 第l到第r个数字，其中有k个数字，分别是第x1、第x2 .. 第xk个数字
# 这k个数字中的每一个，都比剩下的(r - l + 1 - k)个数字要大，严格大于
# 根据上面的说明，找到没有矛盾的，给每个数字赋值的方案，任何一个方案即可
# 如果存在方案打印"TAK"，然后打印每个数字，不存在方案打印"NIE"
# 1 <= n、s <= 10^5
# 1 <= m <= 2 * 10^5
# 所有k的累加和 <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3588
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Desert1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'LIMIT': 'LIMIT', 'n': 'n', 's': 's', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'ls': 'ls', 'rs': 'rs', 'root': 'root', 'cntt': 'cntt', 'val': 'val', 'atMost': 'atMost', 'indegree': 'indegree', 'que': 'que'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    LIMIT = 0
    n = 0
    s = 0
    m = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    ls = None
    rs = None
    root = 0
    cntt = 0
    val = None
    atMost = None
    indegree = None
    que = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_Desert1.nxt, ((_java_obj_1 := Code04_Desert1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Desert1.head[u])
        Code04_Desert1.to[Code04_Desert1.cntg] = jcast('int', v)
        Code04_Desert1.weight[Code04_Desert1.cntg] = jcast('int', w)
        Code04_Desert1.head[u] = jcast('int', Code04_Desert1.cntg)
        Code04_Desert1.indegree[v] = jcast('int', (Code04_Desert1.indegree[v] + 1))

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_4 := Code04_Desert1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code04_Desert1.ls, rt, Code04_Desert1.build(l, mid))
            jset(Code04_Desert1.rs, rt, Code04_Desert1.build(jcast('int', jadd(mid, 1)), r))
            Code04_Desert1.addEdge(rt, Code04_Desert1.ls[rt], 0)
            Code04_Desert1.addEdge(rt, Code04_Desert1.rs[rt], 0)
        return jcast('int', rt)

    @staticmethod
    def xToRange(jobx, jobl, jobr, jobw, l, r, i):
        jobx = jcast('int', jobx)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobw = jcast('int', jobw)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobl > jobr):
            return
        if ((jobl <= l) and (r <= jobr)):
            Code04_Desert1.addEdge(jobx, i, jobw)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code04_Desert1.xToRange(jobx, jobl, jobr, jobw, l, mid, Code04_Desert1.ls[i])
            if (jobr > mid):
                Code04_Desert1.xToRange(jobx, jobl, jobr, jobw, jcast('int', jadd(mid, 1)), r, Code04_Desert1.rs[i])

    @staticmethod
    def topo():
        qi = jcast('int', 1)
        qsiz = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Desert1.cntt):
            if (Code04_Desert1.indegree[i] == 0):
                jset(Code04_Desert1.que, (qsiz := jcast('int', (qsiz + (1)))), i)
            Code04_Desert1.atMost[i] = jcast('int', (Code04_Desert1.LIMIT if (Code04_Desert1.val[i] == 0) else Code04_Desert1.val[i]))
            i = jcast('int', (i + 1))
        while (qi <= qsiz):
            u = jcast('int', Code04_Desert1.que[((_java_old_7 := qi), (qi := jcast('int', (qi + (1)))), _java_old_7)[2]])
            e = jcast('int', Code04_Desert1.head[u])
            while (e > 0):
                v = jcast('int', Code04_Desert1.to[e])
                w = jcast('int', Code04_Desert1.weight[e])
                if (Code04_Desert1.atMost[v] > jcast('int', jadd(Code04_Desert1.atMost[u], w))):
                    Code04_Desert1.atMost[v] = jcast('int', jcast('int', jadd(Code04_Desert1.atMost[u], w)))
                    if (((Code04_Desert1.val[v] != 0) and (Code04_Desert1.atMost[v] < Code04_Desert1.val[v])) or (Code04_Desert1.atMost[v] < 1)):
                        return jcast('boolean', False)
                if (((_java_obj_8 := Code04_Desert1.indegree), (_java_key_9 := v), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))))[3] == 0):
                    jset(Code04_Desert1.que, (qsiz := jcast('int', (qsiz + (1)))), v)
                e = jcast('int', Code04_Desert1.nxt[e])
        return jcast('boolean', (qsiz == Code04_Desert1.cntt))

    @staticmethod
    def main(args):
        in_ = Code04_Desert1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Desert1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Desert1.s = jcast('int', jcall(in_, 'nextInt'))
        Code04_Desert1.m = jcast('int', jcall(in_, 'nextInt'))
        Code04_Desert1.cntt = jcast('int', Code04_Desert1.n)
        Code04_Desert1.root = jcast('int', Code04_Desert1.build(1, Code04_Desert1.n))
        i = jcast('int', 1)
        while (i <= Code04_Desert1.s):
            x = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_Desert1.val[x] = jcast('int', v)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Desert1.m):
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            k = jcast('int', jcall(in_, 'nextInt'))
            vnode = jcast('int', ((_java_obj_11 := Code04_Desert1), (_java_key_12 := 'cntt'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3])
            j = jcast('int', 1)
            while (j <= k):
                x = jcast('int', jcall(in_, 'nextInt'))
                Code04_Desert1.addEdge(x, vnode, 0)
                Code04_Desert1.xToRange(vnode, l, jcast('int', (x - 1)), jcast('int', (-1)), 1, Code04_Desert1.n, Code04_Desert1.root)
                l = jcast('int', jcast('int', jadd(x, 1)))
                j = jcast('int', (j + 1))
            Code04_Desert1.xToRange(vnode, l, r, jcast('int', (-1)), 1, Code04_Desert1.n, Code04_Desert1.root)
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code04_Desert1.topo())
        if check:
            jcall(out, 'println', 'TAK')
            i = jcast('int', 1)
            while (i <= Code04_Desert1.n):
                jcall(out, 'print', jadd(Code04_Desert1.atMost[i], ' '))
                i = jcast('int', (i + 1))
            jcall(out, 'println')
        else:
            jcall(out, 'println', 'NIE')
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
            return jcast('int', self.buffer[((_java_obj_14 := self), (_java_key_15 := 'ptr'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]])

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
            raise TypeError("No matching overload for Code04_Desert1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Desert1.MAXN = jcast('int', 100001)
Code04_Desert1.MAXT = jcast('int', jcast('int', (Code04_Desert1.MAXN * 5)))
Code04_Desert1.MAXE = jcast('int', jcast('int', (Code04_Desert1.MAXN * 20)))
Code04_Desert1.LIMIT = jcast('int', 1000000000)
Code04_Desert1.n = jcast('int', 0)
Code04_Desert1.s = jcast('int', 0)
Code04_Desert1.m = jcast('int', 0)
Code04_Desert1.head = jarray('int', [Code04_Desert1.MAXT])
Code04_Desert1.nxt = jarray('int', [Code04_Desert1.MAXE])
Code04_Desert1.to = jarray('int', [Code04_Desert1.MAXE])
Code04_Desert1.weight = jarray('int', [Code04_Desert1.MAXE])
Code04_Desert1.cntg = jcast('int', 0)
Code04_Desert1.ls = jarray('int', [Code04_Desert1.MAXT])
Code04_Desert1.rs = jarray('int', [Code04_Desert1.MAXT])
Code04_Desert1.root = jcast('int', 0)
Code04_Desert1.cntt = jcast('int', 0)
Code04_Desert1.val = jarray('int', [Code04_Desert1.MAXT])
Code04_Desert1.atMost = jarray('int', [Code04_Desert1.MAXT])
Code04_Desert1.indegree = jarray('int', [Code04_Desert1.MAXT])
Code04_Desert1.que = jarray('int', [Code04_Desert1.MAXT])

if __name__ == '__main__':
    Code04_Desert1.main([])
