# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 三维偏序，Python版
# 本题就是讲解170，题目1，讲了CDQ分治的解法，这里用kdt的解法
# 一共有n个对象，每个对象有a、b、c三个属性，每个属性值的范围都是[1, k]
# f(i)表示，aj <= ai 且 bj <= bi 且 cj <= ci 且 j != i 的j的数量
# ans(d)表示，f(i) == d 的i的数量
# 打印所有的ans[d]，d的范围[0, n)
# 1 <= n <= 10^5
# 1 <= k <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3810
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_3DPartialOrder2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'k': 'k', 'abc': 'abc', 'b': 'b', 'c': 'c', 'cntkdt': 'cntkdt', 'root': 'root', 'siz': 'siz', 'ls': 'ls', 'rs': 'rs', 'bmin': 'bmin', 'bmax': 'bmax', 'cmin': 'cmin', 'cmax': 'cmax', 'ALPHA': 'ALPHA', 'top': 'top', 'topFather': 'topFather', 'topSide': 'topSide', 'topDimension': 'topDimension', 'arr': 'arr', 'treeSiz': 'treeSiz', 'ans': 'ans', 'first': 'first', 'last': 'last'}
    MAXN = 0
    INF = 0
    n = 0
    k = 0
    abc = None
    b = None
    c = None
    cntkdt = 0
    root = 0
    siz = None
    ls = None
    rs = None
    bmin = None
    bmax = None
    cmin = None
    cmax = None
    ALPHA = 0.0
    top = 0
    topFather = 0
    topSide = 0
    topDimension = 0
    arr = None
    treeSiz = 0
    ans = None
    @staticmethod
    def init(qb, qc):
        qb = jcast('int', qb)
        qc = jcast('int', qc)
        Code07_3DPartialOrder2.cntkdt = jcast('int', (Code07_3DPartialOrder2.cntkdt + 1))
        Code07_3DPartialOrder2.b[Code07_3DPartialOrder2.cntkdt] = jcast('int', qb)
        Code07_3DPartialOrder2.c[Code07_3DPartialOrder2.cntkdt] = jcast('int', qc)
        jset(Code07_3DPartialOrder2.ls, Code07_3DPartialOrder2.cntkdt, jset(Code07_3DPartialOrder2.rs, Code07_3DPartialOrder2.cntkdt, 0))
        Code07_3DPartialOrder2.siz[Code07_3DPartialOrder2.cntkdt] = jcast('int', 1)
        jset(Code07_3DPartialOrder2.bmin, Code07_3DPartialOrder2.cntkdt, jset(Code07_3DPartialOrder2.bmax, Code07_3DPartialOrder2.cntkdt, qb))
        jset(Code07_3DPartialOrder2.cmin, Code07_3DPartialOrder2.cntkdt, jset(Code07_3DPartialOrder2.cmax, Code07_3DPartialOrder2.cntkdt, qc))
        return jcast('int', Code07_3DPartialOrder2.cntkdt)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        Code07_3DPartialOrder2.siz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code07_3DPartialOrder2.siz[Code07_3DPartialOrder2.ls[i]], Code07_3DPartialOrder2.siz[Code07_3DPartialOrder2.rs[i]])), 1)))
        jset(Code07_3DPartialOrder2.bmin, i, jstatic('Math', 'min', Code07_3DPartialOrder2.b[i], jstatic('Math', 'min', Code07_3DPartialOrder2.bmin[Code07_3DPartialOrder2.ls[i]], Code07_3DPartialOrder2.bmin[Code07_3DPartialOrder2.rs[i]])))
        jset(Code07_3DPartialOrder2.bmax, i, jstatic('Math', 'max', Code07_3DPartialOrder2.b[i], jstatic('Math', 'max', Code07_3DPartialOrder2.bmax[Code07_3DPartialOrder2.ls[i]], Code07_3DPartialOrder2.bmax[Code07_3DPartialOrder2.rs[i]])))
        jset(Code07_3DPartialOrder2.cmin, i, jstatic('Math', 'min', Code07_3DPartialOrder2.c[i], jstatic('Math', 'min', Code07_3DPartialOrder2.cmin[Code07_3DPartialOrder2.ls[i]], Code07_3DPartialOrder2.cmin[Code07_3DPartialOrder2.rs[i]])))
        jset(Code07_3DPartialOrder2.cmax, i, jstatic('Math', 'max', Code07_3DPartialOrder2.c[i], jstatic('Math', 'max', Code07_3DPartialOrder2.cmax[Code07_3DPartialOrder2.ls[i]], Code07_3DPartialOrder2.cmax[Code07_3DPartialOrder2.rs[i]])))

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('int', (Code07_3DPartialOrder2.b[i] if (dimension == 0) else Code07_3DPartialOrder2.c[i]))
        v2 = jcast('int', (Code07_3DPartialOrder2.b[j] if (dimension == 0) else Code07_3DPartialOrder2.c[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code07_3DPartialOrder2.arr[i])
        Code07_3DPartialOrder2.arr[i] = jcast('int', Code07_3DPartialOrder2.arr[j])
        Code07_3DPartialOrder2.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code07_3DPartialOrder2.first = jcast('int', l)
        Code07_3DPartialOrder2.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code07_3DPartialOrder2.last):
            cmp = jcast('int', Code07_3DPartialOrder2.compareNode(Code07_3DPartialOrder2.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code07_3DPartialOrder2.swap(((_java_obj_1 := Code07_3DPartialOrder2), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code07_3DPartialOrder2.swap(i, ((_java_obj_5 := Code07_3DPartialOrder2), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code07_3DPartialOrder2.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code07_3DPartialOrder2.partition(l, r, pidx, dimension)
                if (i < Code07_3DPartialOrder2.first):
                    r = jcast('int', jcast('int', (Code07_3DPartialOrder2.first - 1)))
                else:
                    if (i > Code07_3DPartialOrder2.last):
                        l = jcast('int', jcast('int', jadd(Code07_3DPartialOrder2.last, 1)))
                    else:
                        raise JBreak(None)
            except JContinue as _java_control_8:
                if _java_control_8.label not in (None,):
                    raise
            except JBreak as _java_control_8:
                if _java_control_8.label not in (None,):
                    raise
                break

    @staticmethod
    def build(l, r, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        dimension = jcast('int', dimension)
        if (l > r):
            return jcast('int', 0)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code07_3DPartialOrder2.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code07_3DPartialOrder2.arr[mid])
        jset(Code07_3DPartialOrder2.ls, rt, Code07_3DPartialOrder2.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code07_3DPartialOrder2.rs, rt, Code07_3DPartialOrder2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code07_3DPartialOrder2.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code07_3DPartialOrder2.ALPHA * Code07_3DPartialOrder2.siz[i]) >= jstatic('Math', 'max', Code07_3DPartialOrder2.siz[Code07_3DPartialOrder2.ls[i]], Code07_3DPartialOrder2.siz[Code07_3DPartialOrder2.rs[i]])))

    @staticmethod
    def dfs(i):
        i = jcast('int', i)
        if (i != 0):
            jset(Code07_3DPartialOrder2.arr, ((_java_obj_9 := Code07_3DPartialOrder2), (_java_key_10 := 'treeSiz'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], i)
            Code07_3DPartialOrder2.dfs(Code07_3DPartialOrder2.ls[i])
            Code07_3DPartialOrder2.dfs(Code07_3DPartialOrder2.rs[i])

    @staticmethod
    def rebuild():
        if (Code07_3DPartialOrder2.top != 0):
            Code07_3DPartialOrder2.treeSiz = jcast('int', 0)
            Code07_3DPartialOrder2.dfs(Code07_3DPartialOrder2.top)
            newRoot = jcast('int', Code07_3DPartialOrder2.build(1, Code07_3DPartialOrder2.treeSiz, Code07_3DPartialOrder2.topDimension))
            if (Code07_3DPartialOrder2.topFather == 0):
                Code07_3DPartialOrder2.root = jcast('int', newRoot)
            else:
                if (Code07_3DPartialOrder2.topSide == 1):
                    Code07_3DPartialOrder2.ls[Code07_3DPartialOrder2.topFather] = jcast('int', newRoot)
                else:
                    Code07_3DPartialOrder2.rs[Code07_3DPartialOrder2.topFather] = jcast('int', newRoot)

    @staticmethod
    def _java_add_0(insertNode, u, fa, side, dimension):
        insertNode = jcast('int', insertNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if (u == 0):
            return jcast('int', insertNode)
        if (Code07_3DPartialOrder2.compareNode(insertNode, u, dimension) <= 0):
            jset(Code07_3DPartialOrder2.ls, u, Code07_3DPartialOrder2._java_add_0(insertNode, Code07_3DPartialOrder2.ls[u], u, 1, jcast('int', (dimension ^ 1))))
        else:
            jset(Code07_3DPartialOrder2.rs, u, Code07_3DPartialOrder2._java_add_0(insertNode, Code07_3DPartialOrder2.rs[u], u, 2, jcast('int', (dimension ^ 1))))
        Code07_3DPartialOrder2.maintain(u)
        if (not Code07_3DPartialOrder2.balance(u)):
            Code07_3DPartialOrder2.top = jcast('int', u)
            Code07_3DPartialOrder2.topFather = jcast('int', fa)
            Code07_3DPartialOrder2.topSide = jcast('int', side)
            Code07_3DPartialOrder2.topDimension = jcast('int', dimension)
        return jcast('int', u)

    @staticmethod
    def _java_add_1(qx, qy):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        Code07_3DPartialOrder2.top = jcast('int', jset(Code07_3DPartialOrder2, 'topFather', jset(Code07_3DPartialOrder2, 'topSide', jset(Code07_3DPartialOrder2, 'topDimension', 0))))
        insertNode = jcast('int', Code07_3DPartialOrder2.init(qx, qy))
        Code07_3DPartialOrder2.root = jcast('int', Code07_3DPartialOrder2._java_add_0(insertNode, Code07_3DPartialOrder2.root, 0, 0, 0))
        Code07_3DPartialOrder2.rebuild()

    # 查询 <= qb 并且 <= qc 点的数量
    @staticmethod
    def query(qb, qc, i):
        qb = jcast('int', qb)
        qc = jcast('int', qc)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if ((Code07_3DPartialOrder2.bmin[i] > qb) or (Code07_3DPartialOrder2.cmin[i] > qc)):
            return jcast('int', 0)
        if ((Code07_3DPartialOrder2.bmax[i] <= qb) and (Code07_3DPartialOrder2.cmax[i] <= qc)):
            return jcast('int', Code07_3DPartialOrder2.siz[i])
        ans = jcast('int', 0)
        if ((Code07_3DPartialOrder2.b[i] <= qb) and (Code07_3DPartialOrder2.c[i] <= qc)):
            ans = jcast('int', (ans + 1))
        ans = jcast('int', jcast('int', jadd(ans, Code07_3DPartialOrder2.query(qb, qc, Code07_3DPartialOrder2.ls[i]))))
        ans = jcast('int', jcast('int', jadd(ans, Code07_3DPartialOrder2.query(qb, qc, Code07_3DPartialOrder2.rs[i]))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code07_3DPartialOrder2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_3DPartialOrder2.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_3DPartialOrder2.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_3DPartialOrder2.n):
            jset(Code07_3DPartialOrder2.abc[i], 0, jcall(in_, 'nextInt'))
            jset(Code07_3DPartialOrder2.abc[i], 1, jcall(in_, 'nextInt'))
            jset(Code07_3DPartialOrder2.abc[i], 2, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_3DPartialOrder2.abc, 1, jcast('int', jadd(Code07_3DPartialOrder2.n, 1)), (lambda x, y: (x[0] - y[0])))
        jset(Code07_3DPartialOrder2.bmin, 0, jset(Code07_3DPartialOrder2.cmin, 0, Code07_3DPartialOrder2.INF))
        jset(Code07_3DPartialOrder2.bmax, 0, jset(Code07_3DPartialOrder2.cmax, 0, jcast('int', (-Code07_3DPartialOrder2.INF))))
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code07_3DPartialOrder2.n):
            while ((jcast('int', jadd(r, 1)) <= Code07_3DPartialOrder2.n) and (Code07_3DPartialOrder2.abc[jcast('int', jadd(r, 1))][0] == Code07_3DPartialOrder2.abc[l][0])):
                r = jcast('int', (r + 1))
            i = jcast('int', l)
            while (i <= r):
                Code07_3DPartialOrder2._java_add_1(Code07_3DPartialOrder2.abc[i][1], Code07_3DPartialOrder2.abc[i][2])
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= r):
                fi = jcast('int', jcast('int', (Code07_3DPartialOrder2.query(Code07_3DPartialOrder2.abc[i][1], Code07_3DPartialOrder2.abc[i][2], Code07_3DPartialOrder2.root) - 1)))
                Code07_3DPartialOrder2.ans[fi] = jcast('int', (Code07_3DPartialOrder2.ans[fi] + 1))
                i = jcast('int', (i + 1))
            l = jcast('int', (r := jcast('int', (r + (1)))))
        d = jcast('int', 0)
        while (d < Code07_3DPartialOrder2.n):
            jcall(out, 'println', Code07_3DPartialOrder2.ans[d])
            d = jcast('int', (d + 1))
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
            return jcast('int', self.buffer[((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]])

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
            raise TypeError("No matching overload for Code07_3DPartialOrder2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code07_3DPartialOrder2._java_add_0(*args)
        if _java_choice == 1:
            return Code07_3DPartialOrder2._java_add_1(*args)
        raise TypeError("No matching overload for Code07_3DPartialOrder2.add")


Code07_3DPartialOrder2.MAXN = jcast('int', 100001)
Code07_3DPartialOrder2.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code07_3DPartialOrder2.n = jcast('int', 0)
Code07_3DPartialOrder2.k = jcast('int', 0)
Code07_3DPartialOrder2.abc = jarray('int', [Code07_3DPartialOrder2.MAXN, 3])
Code07_3DPartialOrder2.b = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.c = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.cntkdt = jcast('int', 0)
Code07_3DPartialOrder2.root = jcast('int', 0)
Code07_3DPartialOrder2.siz = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.ls = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.rs = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.bmin = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.bmax = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.cmin = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.cmax = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.ALPHA = jcast('double', 0.7)
Code07_3DPartialOrder2.top = jcast('int', 0)
Code07_3DPartialOrder2.topFather = jcast('int', 0)
Code07_3DPartialOrder2.topSide = jcast('int', 0)
Code07_3DPartialOrder2.topDimension = jcast('int', 0)
Code07_3DPartialOrder2.arr = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.treeSiz = jcast('int', 0)
Code07_3DPartialOrder2.ans = jarray('int', [Code07_3DPartialOrder2.MAXN])
Code07_3DPartialOrder2.first = jcast('int', 0)
Code07_3DPartialOrder2.last = jcast('int', 0)

if __name__ == '__main__':
    Code07_3DPartialOrder2.main([])
