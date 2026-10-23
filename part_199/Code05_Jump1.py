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

# 弹跳，Python版
# 一共有n个点，编号1~n，给定每个点的坐标(x, y)
# 一共有m个弹跳装置，给定每个弹跳装置的参数 p t l r d u
# 表示装置在p号点，花费t的时间，可以从p号点跳到[l, r] * [d, u]中的任意点
# 从1号点出发，可以重复经过点，也可以重复使用弹跳装置，题目保证可以到达每个点
# 打印从1号点到达2、3 .. n号点各自的最短用时
# 1 <= n <= 7 * 10^4
# 1 <= m <= 1.5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5471
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Jump1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'w': 'w', 'h': 'h', 'x': 'x', 'y': 'y', 'arr': 'arr', 'jump': 'jump', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headj': 'headj', 'nextj': 'nextj', 'toj': 'toj', 'cntj': 'cntj', 'dist': 'dist', 'vis': 'vis', 'heap': 'heap', 'first': 'first', 'last': 'last'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    w = 0
    h = 0
    x = None
    y = None
    arr = None
    # t、l、r、d、u
    jump = None
    # 静态K-D树
    root = 0
    ls = None
    rs = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    # 优化建图，链式前向星实现建图
    headg = None
    nextg = None
    tog = None
    cntg = 0
    # 每个真实点拥有的弹跳装置列表，链式前向星实现列表
    headj = None
    nextj = None
    toj = None
    cntj = 0
    # dijkstra
    dist = None
    vis = None
    # 距离、编号
    heap = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Jump1.nextg, ((_java_obj_1 := Code05_Jump1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Jump1.headg[u])
        Code05_Jump1.tog[Code05_Jump1.cntg] = jcast('int', v)
        Code05_Jump1.headg[u] = jcast('int', Code05_Jump1.cntg)

    @staticmethod
    def addJump(p, j):
        p = jcast('int', p)
        j = jcast('int', j)
        jset(Code05_Jump1.nextj, ((_java_obj_4 := Code05_Jump1), (_java_key_5 := 'cntj'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code05_Jump1.headj[p])
        Code05_Jump1.toj[Code05_Jump1.cntj] = jcast('int', j)
        Code05_Jump1.headj[p] = jcast('int', Code05_Jump1.cntj)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        jset(Code05_Jump1.xmin, i, jstatic('Math', 'min', Code05_Jump1.x[i], jstatic('Math', 'min', Code05_Jump1.xmin[Code05_Jump1.ls[i]], Code05_Jump1.xmin[Code05_Jump1.rs[i]])))
        jset(Code05_Jump1.xmax, i, jstatic('Math', 'max', Code05_Jump1.x[i], jstatic('Math', 'max', Code05_Jump1.xmax[Code05_Jump1.ls[i]], Code05_Jump1.xmax[Code05_Jump1.rs[i]])))
        jset(Code05_Jump1.ymin, i, jstatic('Math', 'min', Code05_Jump1.y[i], jstatic('Math', 'min', Code05_Jump1.ymin[Code05_Jump1.ls[i]], Code05_Jump1.ymin[Code05_Jump1.rs[i]])))
        jset(Code05_Jump1.ymax, i, jstatic('Math', 'max', Code05_Jump1.y[i], jstatic('Math', 'max', Code05_Jump1.ymax[Code05_Jump1.ls[i]], Code05_Jump1.ymax[Code05_Jump1.rs[i]])))

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('long', (Code05_Jump1.x[i] if (dimension == 0) else Code05_Jump1.y[i]))
        v2 = jcast('long', (Code05_Jump1.x[j] if (dimension == 0) else Code05_Jump1.y[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code05_Jump1.arr[i])
        Code05_Jump1.arr[i] = jcast('int', Code05_Jump1.arr[j])
        Code05_Jump1.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code05_Jump1.first = jcast('int', l)
        Code05_Jump1.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code05_Jump1.last):
            cmp = jcast('int', Code05_Jump1.compareNode(Code05_Jump1.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code05_Jump1.swap(((_java_obj_7 := Code05_Jump1), (_java_key_8 := 'first'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4], ((_java_old_10 := i), (i := jcast('int', (i + (1)))), _java_old_10)[2])
                else:
                    Code05_Jump1.swap(i, ((_java_obj_11 := Code05_Jump1), (_java_key_12 := 'last'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code05_Jump1.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code05_Jump1.partition(l, r, pidx, dimension)
                if (i < Code05_Jump1.first):
                    r = jcast('int', jcast('int', (Code05_Jump1.first - 1)))
                else:
                    if (i > Code05_Jump1.last):
                        l = jcast('int', jcast('int', jadd(Code05_Jump1.last, 1)))
                    else:
                        raise JBreak(None)
            except JContinue as _java_control_14:
                if _java_control_14.label not in (None,):
                    raise
            except JBreak as _java_control_14:
                if _java_control_14.label not in (None,):
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
        Code05_Jump1.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code05_Jump1.arr[mid])
        jset(Code05_Jump1.ls, rt, Code05_Jump1.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code05_Jump1.rs, rt, Code05_Jump1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code05_Jump1.maintain(rt)
        # 优化建图
        # n + rt是虚点，表示以rt为根的整棵子树
        # 虚点可以到达子树中的所有真实点
        Code05_Jump1.addEdge(jcast('int', jadd(Code05_Jump1.n, rt)), rt)
        if (Code05_Jump1.ls[rt] != 0):
            Code05_Jump1.addEdge(jcast('int', jadd(Code05_Jump1.n, rt)), jcast('int', jadd(Code05_Jump1.n, Code05_Jump1.ls[rt])))
        if (Code05_Jump1.rs[rt] != 0):
            Code05_Jump1.addEdge(jcast('int', jadd(Code05_Jump1.n, rt)), jcast('int', jadd(Code05_Jump1.n, Code05_Jump1.rs[rt])))
        return jcast('int', rt)

    # 1号点到i号点，出现了新距离d，尝试更新堆
    @staticmethod
    def heapAdd(d, i):
        d = jcast('int', d)
        i = jcast('int', i)
        if ((not Code05_Jump1.vis[i]) and (Code05_Jump1.dist[i] > d)):
            Code05_Jump1.dist[i] = jcast('int', d)
            jcall(Code05_Jump1.heap, 'add', jarray('int', [None], [d, i]))

    @staticmethod
    def jumpToRectangle(jl, jr, jd, ju, jdist, i):
        jl = jcast('int', jl)
        jr = jcast('int', jr)
        jd = jcast('int', jd)
        ju = jcast('int', ju)
        jdist = jcast('int', jdist)
        i = jcast('int', i)
        if (i == 0):
            return
        # 从1号点到当前虚点的最短距离，已经优于jdist，可以剪枝
        if (Code05_Jump1.dist[jcast('int', jadd(Code05_Jump1.n, i))] <= jdist):
            return
        # 弹跳装置在当前区域之外，可以剪枝
        if ((((Code05_Jump1.xmax[i] < jl) or (jr < Code05_Jump1.xmin[i])) or (Code05_Jump1.ymax[i] < jd)) or (ju < Code05_Jump1.ymin[i])):
            return
        # 弹跳装置包括了当前区域，更新1号点到当前区域虚点的最短距离
        if ((((jl <= Code05_Jump1.xmin[i]) and (Code05_Jump1.xmax[i] <= jr)) and (jd <= Code05_Jump1.ymin[i])) and (Code05_Jump1.ymax[i] <= ju)):
            Code05_Jump1.heapAdd(jdist, jcast('int', jadd(Code05_Jump1.n, i)))
            return
        # 弹跳装置包括了当前点，更新1号点到当前点的最短距离
        if ((((jl <= Code05_Jump1.x[i]) and (Code05_Jump1.x[i] <= jr)) and (jd <= Code05_Jump1.y[i])) and (Code05_Jump1.y[i] <= ju)):
            Code05_Jump1.heapAdd(jdist, i)
        Code05_Jump1.jumpToRectangle(jl, jr, jd, ju, jdist, Code05_Jump1.ls[i])
        Code05_Jump1.jumpToRectangle(jl, jr, jd, ju, jdist, Code05_Jump1.rs[i])

    @staticmethod
    def dijkstra():
        jstatic('Arrays', 'fill', Code05_Jump1.dist, 1, jcast('int', jadd(jcast('int', (Code05_Jump1.n << (1 & 31))), 1)), Code05_Jump1.INF)
        Code05_Jump1.dist[1] = jcast('int', 0)
        jcall(Code05_Jump1.heap, 'add', jarray('int', [None], [0, 1]))
        while (not jcall(Code05_Jump1.heap, 'isEmpty')):
            cur = jcall(Code05_Jump1.heap, 'poll')
            d = jcast('int', cur[0])
            i = jcast('int', cur[1])
            if (not Code05_Jump1.vis[i]):
                Code05_Jump1.vis[i] = jcast('boolean', True)
                # 如果是真实点，可能有若干弹跳装置，但一定没有出边
                # 如果是虚点，一定没有弹跳装置，但肯定有出边
                if (i <= Code05_Jump1.n):
                    # 枚举弹跳装置，利用dist信息尽量剪枝，优化常数时间
                    e = jcast('int', Code05_Jump1.headj[i])
                    while (e > 0):
                        j = jcast('int', Code05_Jump1.toj[e])
                        Code05_Jump1.jumpToRectangle(Code05_Jump1.jump[j][1], Code05_Jump1.jump[j][2], Code05_Jump1.jump[j][3], Code05_Jump1.jump[j][4], jcast('int', jadd(d, Code05_Jump1.jump[j][0])), Code05_Jump1.root)
                        e = jcast('int', Code05_Jump1.nextj[e])
                else:
                    # 区域虚点通过优化建图，去往区域内所有真实点
                    e = jcast('int', Code05_Jump1.headg[i])
                    while (e > 0):
                        Code05_Jump1.heapAdd(d, Code05_Jump1.tog[e])
                        e = jcast('int', Code05_Jump1.nextg[e])

    @staticmethod
    def main(args):
        in_ = Code05_Jump1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Jump1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Jump1.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_Jump1.w = jcast('int', jcall(in_, 'nextInt'))
        Code05_Jump1.h = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Jump1.n):
            jset(Code05_Jump1.x, i, jcall(in_, 'nextInt'))
            jset(Code05_Jump1.y, i, jcall(in_, 'nextInt'))
            Code05_Jump1.arr[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        j = jcast('int', 1)
        p = 0
        while (j <= Code05_Jump1.m):
            p = jcast('int', jcall(in_, 'nextInt'))
            jset(Code05_Jump1.jump[j], 0, jcall(in_, 'nextInt'))
            jset(Code05_Jump1.jump[j], 1, jcall(in_, 'nextInt'))
            jset(Code05_Jump1.jump[j], 2, jcall(in_, 'nextInt'))
            jset(Code05_Jump1.jump[j], 3, jcall(in_, 'nextInt'))
            jset(Code05_Jump1.jump[j], 4, jcall(in_, 'nextInt'))
            Code05_Jump1.addJump(p, j)
            j = jcast('int', (j + 1))
        jset(Code05_Jump1.xmin, 0, jset(Code05_Jump1.ymin, 0, Code05_Jump1.INF))
        jset(Code05_Jump1.xmax, 0, jset(Code05_Jump1.ymax, 0, jcast('int', (-Code05_Jump1.INF))))
        Code05_Jump1.root = jcast('int', Code05_Jump1.build(1, Code05_Jump1.n, 0))
        Code05_Jump1.dijkstra()
        i = jcast('int', 2)
        while (i <= Code05_Jump1.n):
            jcall(out, 'println', Code05_Jump1.dist[i])
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
            return jcast('int', self.buffer[((_java_obj_15 := self), (_java_key_16 := 'ptr'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))), _java_old_17)[4]])

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
            raise TypeError("No matching overload for Code05_Jump1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Jump1.MAXN = jcast('int', 200001)
Code05_Jump1.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code05_Jump1.n = jcast('int', 0)
Code05_Jump1.m = jcast('int', 0)
Code05_Jump1.w = jcast('int', 0)
Code05_Jump1.h = jcast('int', 0)
Code05_Jump1.x = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.y = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.arr = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.jump = jarray('int', [Code05_Jump1.MAXN, 5])
Code05_Jump1.root = jcast('int', 0)
Code05_Jump1.ls = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.rs = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.xmin = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.xmax = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.ymin = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.ymax = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.headg = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.nextg = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.tog = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.cntg = jcast('int', 0)
Code05_Jump1.headj = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.nextj = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.toj = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.cntj = jcast('int', 0)
Code05_Jump1.dist = jarray('int', [Code05_Jump1.MAXN])
Code05_Jump1.vis = jarray('boolean', [Code05_Jump1.MAXN])
Code05_Jump1.heap = jnew('PriorityQueue', (lambda a, b: (a[0] - b[0])))
Code05_Jump1.first = jcast('int', 0)
Code05_Jump1.last = jcast('int', 0)

if __name__ == '__main__':
    Code05_Jump1.main([])
