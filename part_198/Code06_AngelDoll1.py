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

# 天使玩偶，Python版
# 本题就是讲解170，题目6，讲了CDQ分治的解法，这里用kdt的解法
# 规定(x1, y1)和(x2, y2)之间的距离 = | x1 - x2 | + | y1 - y2 |
# 一开始先给定n个点的位置，接下来有m条操作，每种操作是如下两种类型中的一种
# 操作 1 x y : 在(x, y)位置添加一个点
# 操作 2 x y : 打印已经添加的所有点中，距离(x, y)最近的点有多远
# 1 <= n、m <= 3 * 10^5
# 0 <= x、y <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P4169
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_AngelDoll1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'x': 'x', 'y': 'y', 'cntkdt': 'cntkdt', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'siz': 'siz', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'ALPHA': 'ALPHA', 'top': 'top', 'topFather': 'topFather', 'topSide': 'topSide', 'topDimension': 'topDimension', 'arr': 'arr', 'treeSiz': 'treeSiz', 'first': 'first', 'last': 'last', 'queryAns': 'queryAns'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    x = None
    y = None
    cntkdt = 0
    root = 0
    ls = None
    rs = None
    siz = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    ALPHA = 0.0
    top = 0
    topFather = 0
    topSide = 0
    topDimension = 0
    arr = None
    treeSiz = 0
    @staticmethod
    def init(qx, qy):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        Code06_AngelDoll1.cntkdt = jcast('int', (Code06_AngelDoll1.cntkdt + 1))
        Code06_AngelDoll1.x[Code06_AngelDoll1.cntkdt] = jcast('int', qx)
        Code06_AngelDoll1.y[Code06_AngelDoll1.cntkdt] = jcast('int', qy)
        jset(Code06_AngelDoll1.ls, Code06_AngelDoll1.cntkdt, jset(Code06_AngelDoll1.rs, Code06_AngelDoll1.cntkdt, 0))
        Code06_AngelDoll1.siz[Code06_AngelDoll1.cntkdt] = jcast('int', 1)
        jset(Code06_AngelDoll1.xmin, Code06_AngelDoll1.cntkdt, jset(Code06_AngelDoll1.xmax, Code06_AngelDoll1.cntkdt, qx))
        jset(Code06_AngelDoll1.ymin, Code06_AngelDoll1.cntkdt, jset(Code06_AngelDoll1.ymax, Code06_AngelDoll1.cntkdt, qy))
        return jcast('int', Code06_AngelDoll1.cntkdt)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        Code06_AngelDoll1.siz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(1, Code06_AngelDoll1.siz[Code06_AngelDoll1.ls[i]])), Code06_AngelDoll1.siz[Code06_AngelDoll1.rs[i]])))
        jset(Code06_AngelDoll1.xmin, i, jstatic('Math', 'min', Code06_AngelDoll1.x[i], jstatic('Math', 'min', Code06_AngelDoll1.xmin[Code06_AngelDoll1.ls[i]], Code06_AngelDoll1.xmin[Code06_AngelDoll1.rs[i]])))
        jset(Code06_AngelDoll1.xmax, i, jstatic('Math', 'max', Code06_AngelDoll1.x[i], jstatic('Math', 'max', Code06_AngelDoll1.xmax[Code06_AngelDoll1.ls[i]], Code06_AngelDoll1.xmax[Code06_AngelDoll1.rs[i]])))
        jset(Code06_AngelDoll1.ymin, i, jstatic('Math', 'min', Code06_AngelDoll1.y[i], jstatic('Math', 'min', Code06_AngelDoll1.ymin[Code06_AngelDoll1.ls[i]], Code06_AngelDoll1.ymin[Code06_AngelDoll1.rs[i]])))
        jset(Code06_AngelDoll1.ymax, i, jstatic('Math', 'max', Code06_AngelDoll1.y[i], jstatic('Math', 'max', Code06_AngelDoll1.ymax[Code06_AngelDoll1.ls[i]], Code06_AngelDoll1.ymax[Code06_AngelDoll1.rs[i]])))

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('int', (Code06_AngelDoll1.x[i] if (dimension == 0) else Code06_AngelDoll1.y[i]))
        v2 = jcast('int', (Code06_AngelDoll1.x[j] if (dimension == 0) else Code06_AngelDoll1.y[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code06_AngelDoll1.arr[i])
        Code06_AngelDoll1.arr[i] = jcast('int', Code06_AngelDoll1.arr[j])
        Code06_AngelDoll1.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code06_AngelDoll1.first = jcast('int', l)
        Code06_AngelDoll1.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code06_AngelDoll1.last):
            cmp = jcast('int', Code06_AngelDoll1.compareNode(Code06_AngelDoll1.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code06_AngelDoll1.swap(((_java_obj_1 := Code06_AngelDoll1), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code06_AngelDoll1.swap(i, ((_java_obj_5 := Code06_AngelDoll1), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code06_AngelDoll1.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code06_AngelDoll1.partition(l, r, pidx, dimension)
                if (i < Code06_AngelDoll1.first):
                    r = jcast('int', jcast('int', (Code06_AngelDoll1.first - 1)))
                else:
                    if (i > Code06_AngelDoll1.last):
                        l = jcast('int', jcast('int', jadd(Code06_AngelDoll1.last, 1)))
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
        Code06_AngelDoll1.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code06_AngelDoll1.arr[mid])
        jset(Code06_AngelDoll1.ls, rt, Code06_AngelDoll1.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code06_AngelDoll1.rs, rt, Code06_AngelDoll1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code06_AngelDoll1.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code06_AngelDoll1.ALPHA * Code06_AngelDoll1.siz[i]) >= jstatic('Math', 'max', Code06_AngelDoll1.siz[Code06_AngelDoll1.ls[i]], Code06_AngelDoll1.siz[Code06_AngelDoll1.rs[i]])))

    @staticmethod
    def dfs(i):
        i = jcast('int', i)
        if (i != 0):
            jset(Code06_AngelDoll1.arr, ((_java_obj_9 := Code06_AngelDoll1), (_java_key_10 := 'treeSiz'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], i)
            Code06_AngelDoll1.dfs(Code06_AngelDoll1.ls[i])
            Code06_AngelDoll1.dfs(Code06_AngelDoll1.rs[i])

    @staticmethod
    def rebuild():
        if (Code06_AngelDoll1.top != 0):
            Code06_AngelDoll1.treeSiz = jcast('int', 0)
            Code06_AngelDoll1.dfs(Code06_AngelDoll1.top)
            newRoot = jcast('int', Code06_AngelDoll1.build(1, Code06_AngelDoll1.treeSiz, Code06_AngelDoll1.topDimension))
            if (Code06_AngelDoll1.topFather == 0):
                Code06_AngelDoll1.root = jcast('int', newRoot)
            else:
                if (Code06_AngelDoll1.topSide == 1):
                    Code06_AngelDoll1.ls[Code06_AngelDoll1.topFather] = jcast('int', newRoot)
                else:
                    Code06_AngelDoll1.rs[Code06_AngelDoll1.topFather] = jcast('int', newRoot)

    @staticmethod
    def _java_add_0(insertNode, u, fa, side, dimension):
        insertNode = jcast('int', insertNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if (u == 0):
            return jcast('int', insertNode)
        if (Code06_AngelDoll1.compareNode(insertNode, u, dimension) <= 0):
            jset(Code06_AngelDoll1.ls, u, Code06_AngelDoll1._java_add_0(insertNode, Code06_AngelDoll1.ls[u], u, 1, jcast('int', (dimension ^ 1))))
        else:
            jset(Code06_AngelDoll1.rs, u, Code06_AngelDoll1._java_add_0(insertNode, Code06_AngelDoll1.rs[u], u, 2, jcast('int', (dimension ^ 1))))
        Code06_AngelDoll1.maintain(u)
        if (not Code06_AngelDoll1.balance(u)):
            Code06_AngelDoll1.top = jcast('int', u)
            Code06_AngelDoll1.topFather = jcast('int', fa)
            Code06_AngelDoll1.topSide = jcast('int', side)
            Code06_AngelDoll1.topDimension = jcast('int', dimension)
        return jcast('int', u)

    @staticmethod
    def _java_add_1(qx, qy):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        Code06_AngelDoll1.top = jcast('int', jset(Code06_AngelDoll1, 'topFather', jset(Code06_AngelDoll1, 'topSide', jset(Code06_AngelDoll1, 'topDimension', 0))))
        insertNode = jcast('int', Code06_AngelDoll1.init(qx, qy))
        Code06_AngelDoll1.root = jcast('int', Code06_AngelDoll1._java_add_0(insertNode, Code06_AngelDoll1.root, 0, 0, 0))
        Code06_AngelDoll1.rebuild()

    # 估计查询点到i的掌管区域中，最小的曼哈顿距离
    @staticmethod
    def guess(qx, qy, i):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', Code06_AngelDoll1.INF)
        ans = jcast('int', (jcast('int', (Code06_AngelDoll1.xmin[i] - qx)) if (qx < Code06_AngelDoll1.xmin[i]) else (jcast('int', (qx - Code06_AngelDoll1.xmax[i])) if (qx > Code06_AngelDoll1.xmax[i]) else 0)))
        ans = jcast('int', jcast('int', jadd(ans, (jcast('int', (Code06_AngelDoll1.ymin[i] - qy)) if (qy < Code06_AngelDoll1.ymin[i]) else (jcast('int', (qy - Code06_AngelDoll1.ymax[i])) if (qy > Code06_AngelDoll1.ymax[i]) else 0)))))
        return jcast('int', ans)

    queryAns = 0
    @staticmethod
    def updateAns(qx, qy, i):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        i = jcast('int', i)
        if (i == 0):
            return
        # 单点的答案
        Code06_AngelDoll1.queryAns = jcast('int', jstatic('Math', 'min', Code06_AngelDoll1.queryAns, jcast('int', jadd(jstatic('Math', 'abs', jcast('int', (qx - Code06_AngelDoll1.x[i]))), jstatic('Math', 'abs', jcast('int', (qy - Code06_AngelDoll1.y[i])))))))
        gl = jcast('int', Code06_AngelDoll1.guess(qx, qy, Code06_AngelDoll1.ls[i]))
        gr = jcast('int', Code06_AngelDoll1.guess(qx, qy, Code06_AngelDoll1.rs[i]))
        if (gl < gr):
            if (gl < Code06_AngelDoll1.queryAns):
                Code06_AngelDoll1.updateAns(qx, qy, Code06_AngelDoll1.ls[i])
            if (gr < Code06_AngelDoll1.queryAns):
                Code06_AngelDoll1.updateAns(qx, qy, Code06_AngelDoll1.rs[i])
        else:
            if (gr < Code06_AngelDoll1.queryAns):
                Code06_AngelDoll1.updateAns(qx, qy, Code06_AngelDoll1.rs[i])
            if (gl < Code06_AngelDoll1.queryAns):
                Code06_AngelDoll1.updateAns(qx, qy, Code06_AngelDoll1.ls[i])

    @staticmethod
    def main(args):
        in_ = Code06_AngelDoll1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_AngelDoll1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_AngelDoll1.m = jcast('int', jcall(in_, 'nextInt'))
        jset(Code06_AngelDoll1.xmin, 0, jset(Code06_AngelDoll1.ymin, 0, Code06_AngelDoll1.INF))
        jset(Code06_AngelDoll1.xmax, 0, jset(Code06_AngelDoll1.ymax, 0, jcast('int', (-Code06_AngelDoll1.INF))))
        i = jcast('int', 1)
        qx = 0
        qy = 0
        while (i <= Code06_AngelDoll1.n):
            qx = jcast('int', jcall(in_, 'nextInt'))
            qy = jcast('int', jcall(in_, 'nextInt'))
            Code06_AngelDoll1._java_add_1(qx, qy)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        qx = 0
        qy = 0
        while (i <= Code06_AngelDoll1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            qx = jcast('int', jcall(in_, 'nextInt'))
            qy = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                Code06_AngelDoll1._java_add_1(qx, qy)
            else:
                Code06_AngelDoll1.queryAns = jcast('int', Code06_AngelDoll1.INF)
                Code06_AngelDoll1.updateAns(qx, qy, Code06_AngelDoll1.root)
                jcall(out, 'println', Code06_AngelDoll1.queryAns)
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
            raise TypeError("No matching overload for Code06_AngelDoll1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code06_AngelDoll1._java_add_0(*args)
        if _java_choice == 1:
            return Code06_AngelDoll1._java_add_1(*args)
        raise TypeError("No matching overload for Code06_AngelDoll1.add")


Code06_AngelDoll1.MAXN = jcast('int', 1000001)
Code06_AngelDoll1.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code06_AngelDoll1.n = jcast('int', 0)
Code06_AngelDoll1.m = jcast('int', 0)
Code06_AngelDoll1.x = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.y = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.cntkdt = jcast('int', 0)
Code06_AngelDoll1.root = jcast('int', 0)
Code06_AngelDoll1.ls = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.rs = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.siz = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.xmin = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.xmax = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.ymin = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.ymax = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.ALPHA = jcast('double', 0.7)
Code06_AngelDoll1.top = jcast('int', 0)
Code06_AngelDoll1.topFather = jcast('int', 0)
Code06_AngelDoll1.topSide = jcast('int', 0)
Code06_AngelDoll1.topDimension = jcast('int', 0)
Code06_AngelDoll1.arr = jarray('int', [Code06_AngelDoll1.MAXN])
Code06_AngelDoll1.treeSiz = jcast('int', 0)
Code06_AngelDoll1.first = jcast('int', 0)
Code06_AngelDoll1.last = jcast('int', 0)
Code06_AngelDoll1.queryAns = jcast('int', 0)

if __name__ == '__main__':
    Code06_AngelDoll1.main([])
