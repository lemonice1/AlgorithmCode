# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 平面最近点对，Python版
# 此实现展示一种非最优思路，复杂度可能不满足题目的最大数据规模
# 本题复杂度正确的正解，是平面最近点对的分治算法，计算几何专题会讲述
# 一共n个点，每个点给定坐标(x, y)，输出最近两个点的距离，保留四位小数
# 2 <= n <= 2 * 10^5
# 0 <= x、y <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1429
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_ClosestPair2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'x': 'x', 'y': 'y', 'arr': 'arr', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'ans': 'ans', 'first': 'first', 'last': 'last'}
    MAXN = 0
    INF = 0
    n = 0
    x = None
    y = None
    arr = None
    root = 0
    ls = None
    rs = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    ans = 0
    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('long', (Code01_ClosestPair2.x[i] if (dimension == 0) else Code01_ClosestPair2.y[i]))
        v2 = jcast('long', (Code01_ClosestPair2.x[j] if (dimension == 0) else Code01_ClosestPair2.y[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code01_ClosestPair2.arr[i])
        Code01_ClosestPair2.arr[i] = jcast('int', Code01_ClosestPair2.arr[j])
        Code01_ClosestPair2.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code01_ClosestPair2.first = jcast('int', l)
        Code01_ClosestPair2.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code01_ClosestPair2.last):
            cmp = jcast('int', Code01_ClosestPair2.compareNode(Code01_ClosestPair2.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code01_ClosestPair2.swap(((_java_obj_1 := Code01_ClosestPair2), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code01_ClosestPair2.swap(i, ((_java_obj_5 := Code01_ClosestPair2), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    # 讲解024，随机选择算法，无序数组中找到第k小的数，时间复杂度O(n)
    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code01_ClosestPair2.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code01_ClosestPair2.partition(l, r, pidx, dimension)
                if (i < Code01_ClosestPair2.first):
                    r = jcast('int', jcast('int', (Code01_ClosestPair2.first - 1)))
                else:
                    if (i > Code01_ClosestPair2.last):
                        l = jcast('int', jcast('int', jadd(Code01_ClosestPair2.last, 1)))
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
    def maintain(i):
        i = jcast('int', i)
        jset(Code01_ClosestPair2.xmin, i, jstatic('Math', 'min', Code01_ClosestPair2.x[i], jstatic('Math', 'min', Code01_ClosestPair2.xmin[Code01_ClosestPair2.ls[i]], Code01_ClosestPair2.xmin[Code01_ClosestPair2.rs[i]])))
        jset(Code01_ClosestPair2.xmax, i, jstatic('Math', 'max', Code01_ClosestPair2.x[i], jstatic('Math', 'max', Code01_ClosestPair2.xmax[Code01_ClosestPair2.ls[i]], Code01_ClosestPair2.xmax[Code01_ClosestPair2.rs[i]])))
        jset(Code01_ClosestPair2.ymin, i, jstatic('Math', 'min', Code01_ClosestPair2.y[i], jstatic('Math', 'min', Code01_ClosestPair2.ymin[Code01_ClosestPair2.ls[i]], Code01_ClosestPair2.ymin[Code01_ClosestPair2.rs[i]])))
        jset(Code01_ClosestPair2.ymax, i, jstatic('Math', 'max', Code01_ClosestPair2.y[i], jstatic('Math', 'max', Code01_ClosestPair2.ymax[Code01_ClosestPair2.ls[i]], Code01_ClosestPair2.ymax[Code01_ClosestPair2.rs[i]])))

    # 交替选维度
    @staticmethod
    def build1(l, r, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        dimension = jcast('int', dimension)
        if (l > r):
            return jcast('int', 0)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code01_ClosestPair2.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code01_ClosestPair2.arr[mid])
        jset(Code01_ClosestPair2.ls, rt, Code01_ClosestPair2.build1(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code01_ClosestPair2.rs, rt, Code01_ClosestPair2.build1(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code01_ClosestPair2.maintain(rt)
        return jcast('int', rt)

    # 返回dimension维度数据的方差
    @staticmethod
    def variance(l, r, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        dimension = jcast('int', dimension)
        siz = jcast('double', jcast('int', jadd(jcast('int', (r - l)), 1)))
        sum = jcast('double', 0)
        avg = jcast('double', 0)
        dif = jcast('double', 0)
        i = jcast('int', l)
        while (i <= r):
            sum = jcast('double', jadd(sum, (Code01_ClosestPair2.x[Code01_ClosestPair2.arr[i]] if (dimension == 0) else Code01_ClosestPair2.y[Code01_ClosestPair2.arr[i]])))
            i = jcast('int', (i + 1))
        avg = jcast('double', jdiv(sum, siz))
        sum = jcast('double', 0)
        i = jcast('int', l)
        while (i <= r):
            dif = jcast('double', ((Code01_ClosestPair2.x[Code01_ClosestPair2.arr[i]] if (dimension == 0) else Code01_ClosestPair2.y[Code01_ClosestPair2.arr[i]]) - avg))
            sum = jcast('double', jadd(sum, (dif * dif)))
            i = jcast('int', (i + 1))
        return jcast('double', jdiv(sum, siz))

    # 方差选维度
    @staticmethod
    def build2(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            return jcast('int', 0)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        dimension = jcast('int', (0 if (Code01_ClosestPair2.variance(l, r, 0) >= Code01_ClosestPair2.variance(l, r, 1)) else 1))
        Code01_ClosestPair2.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code01_ClosestPair2.arr[mid])
        jset(Code01_ClosestPair2.ls, rt, Code01_ClosestPair2.build2(l, jcast('int', (mid - 1))))
        jset(Code01_ClosestPair2.rs, rt, Code01_ClosestPair2.build2(jcast('int', jadd(mid, 1)), r))
        Code01_ClosestPair2.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def dist(qi, i):
        qi = jcast('int', qi)
        i = jcast('int', i)
        dx = jcast('long', jcast('long', (Code01_ClosestPair2.x[qi] - Code01_ClosestPair2.x[i])))
        dy = jcast('long', jcast('long', (Code01_ClosestPair2.y[qi] - Code01_ClosestPair2.y[i])))
        return jcast('long', jcast('long', jadd(jcast('long', (dx * dx)), jcast('long', (dy * dy)))))

    # 估计函数，估计查询点qi到i子树中所有点的最小距离平方
    @staticmethod
    def guess(qi, i):
        qi = jcast('int', qi)
        i = jcast('int', i)
        if (i == 0):
            return jcast('long', Code01_ClosestPair2.INF)
        qx = jcast('long', Code01_ClosestPair2.x[qi])
        qy = jcast('long', Code01_ClosestPair2.y[qi])
        dx = jcast('long', (jcast('long', (Code01_ClosestPair2.xmin[i] - qx)) if (qx < Code01_ClosestPair2.xmin[i]) else (jcast('long', (qx - Code01_ClosestPair2.xmax[i])) if (qx > Code01_ClosestPair2.xmax[i]) else 0)))
        dy = jcast('long', (jcast('long', (Code01_ClosestPair2.ymin[i] - qy)) if (qy < Code01_ClosestPair2.ymin[i]) else (jcast('long', (qy - Code01_ClosestPair2.ymax[i])) if (qy > Code01_ClosestPair2.ymax[i]) else 0)))
        return jcast('long', jcast('long', jadd(jcast('long', (dx * dx)), jcast('long', (dy * dy)))))

    @staticmethod
    def updateAns(qi, i):
        qi = jcast('int', qi)
        i = jcast('int', i)
        if (i == 0):
            return
        # 不能算自己到自己的距离
        if (qi != i):
            Code01_ClosestPair2.ans = jcast('long', jstatic('Math', 'min', Code01_ClosestPair2.ans, Code01_ClosestPair2.dist(qi, i)))
        gl = jcast('long', Code01_ClosestPair2.guess(qi, Code01_ClosestPair2.ls[i]))
        gr = jcast('long', Code01_ClosestPair2.guess(qi, Code01_ClosestPair2.rs[i]))
        if (gl < gr):
            if (gl < Code01_ClosestPair2.ans):
                Code01_ClosestPair2.updateAns(qi, Code01_ClosestPair2.ls[i])
            if (gr < Code01_ClosestPair2.ans):
                Code01_ClosestPair2.updateAns(qi, Code01_ClosestPair2.rs[i])
        else:
            if (gr < Code01_ClosestPair2.ans):
                Code01_ClosestPair2.updateAns(qi, Code01_ClosestPair2.rs[i])
            if (gl < Code01_ClosestPair2.ans):
                Code01_ClosestPair2.updateAns(qi, Code01_ClosestPair2.ls[i])

    @staticmethod
    def main(args):
        in_ = Code01_ClosestPair2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_ClosestPair2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_ClosestPair2.n):
            jset(Code01_ClosestPair2.x, i, jcall(in_, 'nextLong'))
            jset(Code01_ClosestPair2.y, i, jcall(in_, 'nextLong'))
            Code01_ClosestPair2.arr[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jset(Code01_ClosestPair2.xmin, 0, jset(Code01_ClosestPair2.ymin, 0, Code01_ClosestPair2.INF))
        jset(Code01_ClosestPair2.xmax, 0, jset(Code01_ClosestPair2.ymax, 0, jcast('long', (-Code01_ClosestPair2.INF))))
        Code01_ClosestPair2.root = jcast('int', Code01_ClosestPair2.build1(1, Code01_ClosestPair2.n, 0))
        # root = build2(1, n);
        Code01_ClosestPair2.ans = jcast('long', Code01_ClosestPair2.dist(1, 2))
        i = jcast('int', 1)
        while (i <= Code01_ClosestPair2.n):
            try:
                Code01_ClosestPair2.updateAns(i, Code01_ClosestPair2.root)
                if (Code01_ClosestPair2.ans == 0):
                    raise JBreak(None)
            except JContinue as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
            except JBreak as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        jcall(out, 'printf', '%.4f\n', jstatic('Math', 'sqrt', Code01_ClosestPair2.ans))
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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

        def nextLong(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('long', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('long', jcast('long', jadd(jcast('long', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('long', (jcast('long', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_ClosestPair2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_ClosestPair2.MAXN = jcast('int', 200001)
Code01_ClosestPair2.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code01_ClosestPair2.n = jcast('int', 0)
Code01_ClosestPair2.x = jarray('long', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.y = jarray('long', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.arr = jarray('int', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.root = jcast('int', 0)
Code01_ClosestPair2.ls = jarray('int', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.rs = jarray('int', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.xmin = jarray('long', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.xmax = jarray('long', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.ymin = jarray('long', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.ymax = jarray('long', [Code01_ClosestPair2.MAXN])
Code01_ClosestPair2.ans = jcast('long', 0)
Code01_ClosestPair2.first = jcast('int', 0)
Code01_ClosestPair2.last = jcast('int', 0)

if __name__ == '__main__':
    Code01_ClosestPair2.main([])
