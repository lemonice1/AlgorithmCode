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

# 查询第k远的点，Python版
# 一共n个点，编号1~n，每个点给定坐标(x, y)
# 一共m条查询，格式 qx qy qk，查询距离(qx, qy)第qk远的点，打印该点的编号
# 如果多个点到(qx, qy)的距离相同，那么编号较小的点认为距离更远
# 1 <= n <= 10^5
# 1 <= m <= 10^4
# 1 <= qk <= 20
# -10^9 <= 坐标值 <= +10^9
# 测试链接 : https://www.luogu.com.cn/problem/P2093
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_QueryKthFarthest2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'x': 'x', 'y': 'y', 'arr': 'arr', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'heap': 'heap', 'first': 'first', 'last': 'last'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
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
    # 堆中数据 = (距离、点的编号)
    # 距离一样时，题目规定点的编号越小越远
    # 所以小根堆先看距离，距离小的点先淘汰，距离一样，编号大的点先淘汰
    heap = None
    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('long', (Code02_QueryKthFarthest2.x[i] if (dimension == 0) else Code02_QueryKthFarthest2.y[i]))
        v2 = jcast('long', (Code02_QueryKthFarthest2.x[j] if (dimension == 0) else Code02_QueryKthFarthest2.y[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code02_QueryKthFarthest2.arr[i])
        Code02_QueryKthFarthest2.arr[i] = jcast('int', Code02_QueryKthFarthest2.arr[j])
        Code02_QueryKthFarthest2.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code02_QueryKthFarthest2.first = jcast('int', l)
        Code02_QueryKthFarthest2.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code02_QueryKthFarthest2.last):
            cmp = jcast('int', Code02_QueryKthFarthest2.compareNode(Code02_QueryKthFarthest2.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code02_QueryKthFarthest2.swap(((_java_obj_1 := Code02_QueryKthFarthest2), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code02_QueryKthFarthest2.swap(i, ((_java_obj_5 := Code02_QueryKthFarthest2), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code02_QueryKthFarthest2.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code02_QueryKthFarthest2.partition(l, r, pidx, dimension)
                if (i < Code02_QueryKthFarthest2.first):
                    r = jcast('int', jcast('int', (Code02_QueryKthFarthest2.first - 1)))
                else:
                    if (i > Code02_QueryKthFarthest2.last):
                        l = jcast('int', jcast('int', jadd(Code02_QueryKthFarthest2.last, 1)))
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
        jset(Code02_QueryKthFarthest2.xmin, i, jstatic('Math', 'min', Code02_QueryKthFarthest2.x[i], jstatic('Math', 'min', Code02_QueryKthFarthest2.xmin[Code02_QueryKthFarthest2.ls[i]], Code02_QueryKthFarthest2.xmin[Code02_QueryKthFarthest2.rs[i]])))
        jset(Code02_QueryKthFarthest2.xmax, i, jstatic('Math', 'max', Code02_QueryKthFarthest2.x[i], jstatic('Math', 'max', Code02_QueryKthFarthest2.xmax[Code02_QueryKthFarthest2.ls[i]], Code02_QueryKthFarthest2.xmax[Code02_QueryKthFarthest2.rs[i]])))
        jset(Code02_QueryKthFarthest2.ymin, i, jstatic('Math', 'min', Code02_QueryKthFarthest2.y[i], jstatic('Math', 'min', Code02_QueryKthFarthest2.ymin[Code02_QueryKthFarthest2.ls[i]], Code02_QueryKthFarthest2.ymin[Code02_QueryKthFarthest2.rs[i]])))
        jset(Code02_QueryKthFarthest2.ymax, i, jstatic('Math', 'max', Code02_QueryKthFarthest2.y[i], jstatic('Math', 'max', Code02_QueryKthFarthest2.ymax[Code02_QueryKthFarthest2.ls[i]], Code02_QueryKthFarthest2.ymax[Code02_QueryKthFarthest2.rs[i]])))

    @staticmethod
    def build(l, r, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        dimension = jcast('int', dimension)
        if (l > r):
            return jcast('int', 0)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code02_QueryKthFarthest2.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code02_QueryKthFarthest2.arr[mid])
        jset(Code02_QueryKthFarthest2.ls, rt, Code02_QueryKthFarthest2.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code02_QueryKthFarthest2.rs, rt, Code02_QueryKthFarthest2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code02_QueryKthFarthest2.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def dist(x1, y1, x2, y2):
        x1 = jcast('long', x1)
        y1 = jcast('long', y1)
        x2 = jcast('long', x2)
        y2 = jcast('long', y2)
        dx = jcast('long', jcast('long', (x1 - x2)))
        dy = jcast('long', jcast('long', (y1 - y2)))
        return jcast('long', jcast('long', jadd(jcast('long', (dx * dx)), jcast('long', (dy * dy)))))

    # 估计函数，估计查询点到i子树中所有点的最大距离平方
    @staticmethod
    def guess(qx, qy, i):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        i = jcast('int', i)
        if (i == 0):
            return jcast('long', 0)
        dx = jcast('long', jstatic('Math', 'max', jstatic('Math', 'abs', jcast('long', (qx - Code02_QueryKthFarthest2.xmin[i]))), jstatic('Math', 'abs', jcast('long', (qx - Code02_QueryKthFarthest2.xmax[i])))))
        dy = jcast('long', jstatic('Math', 'max', jstatic('Math', 'abs', jcast('long', (qy - Code02_QueryKthFarthest2.ymin[i]))), jstatic('Math', 'abs', jcast('long', (qy - Code02_QueryKthFarthest2.ymax[i])))))
        return jcast('long', jcast('long', jadd(jcast('long', (dx * dx)), jcast('long', (dy * dy)))))

    @staticmethod
    def updateAns(qx, qy, qk, i):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        qk = jcast('int', qk)
        i = jcast('int', i)
        if (i == 0):
            return
        jcall(Code02_QueryKthFarthest2.heap, 'add', jarray('long', [None], [Code02_QueryKthFarthest2.dist(qx, qy, Code02_QueryKthFarthest2.x[i], Code02_QueryKthFarthest2.y[i]), i]))
        if (jcall(Code02_QueryKthFarthest2.heap, 'size') > qk):
            jcall(Code02_QueryKthFarthest2.heap, 'poll')
        gl = jcast('long', Code02_QueryKthFarthest2.guess(qx, qy, Code02_QueryKthFarthest2.ls[i]))
        gr = jcast('long', Code02_QueryKthFarthest2.guess(qx, qy, Code02_QueryKthFarthest2.rs[i]))
        if (gl > gr):
            # 注意判断必须是 >=
            # 因为距离相同，依然可能存在编号更小的点
            if ((jcall(Code02_QueryKthFarthest2.heap, 'size') < qk) or (gl >= jcall(Code02_QueryKthFarthest2.heap, 'peek')[0])):
                Code02_QueryKthFarthest2.updateAns(qx, qy, qk, Code02_QueryKthFarthest2.ls[i])
            if ((jcall(Code02_QueryKthFarthest2.heap, 'size') < qk) or (gr >= jcall(Code02_QueryKthFarthest2.heap, 'peek')[0])):
                Code02_QueryKthFarthest2.updateAns(qx, qy, qk, Code02_QueryKthFarthest2.rs[i])
        else:
            if ((jcall(Code02_QueryKthFarthest2.heap, 'size') < qk) or (gr >= jcall(Code02_QueryKthFarthest2.heap, 'peek')[0])):
                Code02_QueryKthFarthest2.updateAns(qx, qy, qk, Code02_QueryKthFarthest2.rs[i])
            if ((jcall(Code02_QueryKthFarthest2.heap, 'size') < qk) or (gl >= jcall(Code02_QueryKthFarthest2.heap, 'peek')[0])):
                Code02_QueryKthFarthest2.updateAns(qx, qy, qk, Code02_QueryKthFarthest2.ls[i])

    @staticmethod
    def main(args):
        in_ = Code02_QueryKthFarthest2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_QueryKthFarthest2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_QueryKthFarthest2.n):
            jset(Code02_QueryKthFarthest2.x, i, jcall(in_, 'nextLong'))
            jset(Code02_QueryKthFarthest2.y, i, jcall(in_, 'nextLong'))
            Code02_QueryKthFarthest2.arr[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jset(Code02_QueryKthFarthest2.xmin, 0, jset(Code02_QueryKthFarthest2.ymin, 0, Code02_QueryKthFarthest2.INF))
        jset(Code02_QueryKthFarthest2.xmax, 0, jset(Code02_QueryKthFarthest2.ymax, 0, jcast('long', (-Code02_QueryKthFarthest2.INF))))
        Code02_QueryKthFarthest2.root = jcast('int', Code02_QueryKthFarthest2.build(1, Code02_QueryKthFarthest2.n, 0))
        Code02_QueryKthFarthest2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        qx = 0
        qy = 0
        qk = 0
        while (i <= Code02_QueryKthFarthest2.m):
            qx = jcast('int', jcall(in_, 'nextInt'))
            qy = jcast('int', jcall(in_, 'nextInt'))
            qk = jcast('int', jcall(in_, 'nextInt'))
            jcall(Code02_QueryKthFarthest2.heap, 'clear')
            Code02_QueryKthFarthest2.updateAns(qx, qy, qk, Code02_QueryKthFarthest2.root)
            jcall(out, 'println', jcall(Code02_QueryKthFarthest2.heap, 'peek')[1])
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
            return jcast('int', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

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
            raise TypeError("No matching overload for Code02_QueryKthFarthest2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_QueryKthFarthest2.MAXN = jcast('int', 100001)
Code02_QueryKthFarthest2.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code02_QueryKthFarthest2.n = jcast('int', 0)
Code02_QueryKthFarthest2.m = jcast('int', 0)
Code02_QueryKthFarthest2.x = jarray('long', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.y = jarray('long', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.arr = jarray('int', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.root = jcast('int', 0)
Code02_QueryKthFarthest2.ls = jarray('int', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.rs = jarray('int', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.xmin = jarray('long', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.xmax = jarray('long', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.ymin = jarray('long', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.ymax = jarray('long', [Code02_QueryKthFarthest2.MAXN])
Code02_QueryKthFarthest2.heap = jnew('PriorityQueue', (lambda a, b: (jstatic('Long', 'compare', a[0], b[0]) if (a[0] != b[0]) else jstatic('Long', 'compare', b[1], a[1]))))
Code02_QueryKthFarthest2.first = jcast('int', 0)
Code02_QueryKthFarthest2.last = jcast('int', 0)

if __name__ == '__main__':
    Code02_QueryKthFarthest2.main([])
