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

# 巧克力王国，Python版
# 一共n个点，每个点有坐标(x, y)，还有点权v
# 一共m条查询，格式 a b c，含义如下
# 满足 a * x + b * y < c 的所有点，打印点权累加和
# 1 <= n、m <= 5 * 10^4
# -10^9 <= a、b、x、y <= +10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4475
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_ChocolateKingdom2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'x': 'x', 'y': 'y', 'v': 'v', 'arr': 'arr', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'first': 'first', 'last': 'last'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    x = None
    y = None
    v = None
    arr = None
    root = 0
    ls = None
    rs = None
    # 区域点权和
    sum = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('long', (Code03_ChocolateKingdom2.x[i] if (dimension == 0) else Code03_ChocolateKingdom2.y[i]))
        v2 = jcast('long', (Code03_ChocolateKingdom2.x[j] if (dimension == 0) else Code03_ChocolateKingdom2.y[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code03_ChocolateKingdom2.arr[i])
        Code03_ChocolateKingdom2.arr[i] = jcast('int', Code03_ChocolateKingdom2.arr[j])
        Code03_ChocolateKingdom2.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code03_ChocolateKingdom2.first = jcast('int', l)
        Code03_ChocolateKingdom2.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code03_ChocolateKingdom2.last):
            cmp = jcast('int', Code03_ChocolateKingdom2.compareNode(Code03_ChocolateKingdom2.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code03_ChocolateKingdom2.swap(((_java_obj_1 := Code03_ChocolateKingdom2), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code03_ChocolateKingdom2.swap(i, ((_java_obj_5 := Code03_ChocolateKingdom2), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code03_ChocolateKingdom2.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code03_ChocolateKingdom2.partition(l, r, pidx, dimension)
                if (i < Code03_ChocolateKingdom2.first):
                    r = jcast('int', jcast('int', (Code03_ChocolateKingdom2.first - 1)))
                else:
                    if (i > Code03_ChocolateKingdom2.last):
                        l = jcast('int', jcast('int', jadd(Code03_ChocolateKingdom2.last, 1)))
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
        Code03_ChocolateKingdom2.sum[i] = jcast('long', jcast('long', jadd(jcast('long', jadd(Code03_ChocolateKingdom2.v[i], Code03_ChocolateKingdom2.sum[Code03_ChocolateKingdom2.ls[i]])), Code03_ChocolateKingdom2.sum[Code03_ChocolateKingdom2.rs[i]])))
        jset(Code03_ChocolateKingdom2.xmin, i, jstatic('Math', 'min', Code03_ChocolateKingdom2.x[i], jstatic('Math', 'min', Code03_ChocolateKingdom2.xmin[Code03_ChocolateKingdom2.ls[i]], Code03_ChocolateKingdom2.xmin[Code03_ChocolateKingdom2.rs[i]])))
        jset(Code03_ChocolateKingdom2.xmax, i, jstatic('Math', 'max', Code03_ChocolateKingdom2.x[i], jstatic('Math', 'max', Code03_ChocolateKingdom2.xmax[Code03_ChocolateKingdom2.ls[i]], Code03_ChocolateKingdom2.xmax[Code03_ChocolateKingdom2.rs[i]])))
        jset(Code03_ChocolateKingdom2.ymin, i, jstatic('Math', 'min', Code03_ChocolateKingdom2.y[i], jstatic('Math', 'min', Code03_ChocolateKingdom2.ymin[Code03_ChocolateKingdom2.ls[i]], Code03_ChocolateKingdom2.ymin[Code03_ChocolateKingdom2.rs[i]])))
        jset(Code03_ChocolateKingdom2.ymax, i, jstatic('Math', 'max', Code03_ChocolateKingdom2.y[i], jstatic('Math', 'max', Code03_ChocolateKingdom2.ymax[Code03_ChocolateKingdom2.ls[i]], Code03_ChocolateKingdom2.ymax[Code03_ChocolateKingdom2.rs[i]])))

    @staticmethod
    def build(l, r, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        dimension = jcast('int', dimension)
        if (l > r):
            return jcast('int', 0)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code03_ChocolateKingdom2.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code03_ChocolateKingdom2.arr[mid])
        jset(Code03_ChocolateKingdom2.ls, rt, Code03_ChocolateKingdom2.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code03_ChocolateKingdom2.rs, rt, Code03_ChocolateKingdom2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code03_ChocolateKingdom2.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def query(a, b, c, i):
        a = jcast('long', a)
        b = jcast('long', b)
        c = jcast('long', c)
        i = jcast('int', i)
        if (i == 0):
            return jcast('long', 0)
        # a、b、x、y，可能是正或者负，最值的可能性要考虑完整
        ax1 = jcast('long', jcast('long', (Code03_ChocolateKingdom2.xmin[i] * a)))
        ax2 = jcast('long', jcast('long', (Code03_ChocolateKingdom2.xmax[i] * a)))
        by1 = jcast('long', jcast('long', (Code03_ChocolateKingdom2.ymin[i] * b)))
        by2 = jcast('long', jcast('long', (Code03_ChocolateKingdom2.ymax[i] * b)))
        minv = jcast('long', jcast('long', jadd(jstatic('Math', 'min', ax1, ax2), jstatic('Math', 'min', by1, by2))))
        maxv = jcast('long', jcast('long', jadd(jstatic('Math', 'max', ax1, ax2), jstatic('Math', 'max', by1, by2))))
        if (minv >= c):
            return jcast('long', 0)
        if (maxv < c):
            return jcast('long', Code03_ChocolateKingdom2.sum[i])
        ans = jcast('long', 0)
        if (jcast('long', jadd(jcast('long', (a * Code03_ChocolateKingdom2.x[i])), jcast('long', (b * Code03_ChocolateKingdom2.y[i])))) < c):
            ans = jcast('long', jcast('long', jadd(ans, Code03_ChocolateKingdom2.v[i])))
        ans = jcast('long', jcast('long', jadd(ans, Code03_ChocolateKingdom2.query(a, b, c, Code03_ChocolateKingdom2.ls[i]))))
        ans = jcast('long', jcast('long', jadd(ans, Code03_ChocolateKingdom2.query(a, b, c, Code03_ChocolateKingdom2.rs[i]))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code03_ChocolateKingdom2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_ChocolateKingdom2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_ChocolateKingdom2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_ChocolateKingdom2.n):
            jset(Code03_ChocolateKingdom2.x, i, jcall(in_, 'nextLong'))
            jset(Code03_ChocolateKingdom2.y, i, jcall(in_, 'nextLong'))
            jset(Code03_ChocolateKingdom2.v, i, jcall(in_, 'nextLong'))
            Code03_ChocolateKingdom2.arr[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jset(Code03_ChocolateKingdom2.xmin, 0, jset(Code03_ChocolateKingdom2.ymin, 0, Code03_ChocolateKingdom2.INF))
        jset(Code03_ChocolateKingdom2.xmax, 0, jset(Code03_ChocolateKingdom2.ymax, 0, jcast('long', (-Code03_ChocolateKingdom2.INF))))
        Code03_ChocolateKingdom2.root = jcast('int', Code03_ChocolateKingdom2.build(1, Code03_ChocolateKingdom2.n, 0))
        a = 0
        b = 0
        c = 0
        i = jcast('int', 1)
        while (i <= Code03_ChocolateKingdom2.m):
            a = jcast('long', jcall(in_, 'nextLong'))
            b = jcast('long', jcall(in_, 'nextLong'))
            c = jcast('long', jcall(in_, 'nextLong'))
            jcall(out, 'println', Code03_ChocolateKingdom2.query(a, b, c, Code03_ChocolateKingdom2.root))
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
            raise TypeError("No matching overload for Code03_ChocolateKingdom2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_ChocolateKingdom2.MAXN = jcast('int', 50001)
Code03_ChocolateKingdom2.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code03_ChocolateKingdom2.n = jcast('int', 0)
Code03_ChocolateKingdom2.m = jcast('int', 0)
Code03_ChocolateKingdom2.x = jarray('long', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.y = jarray('long', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.v = jarray('long', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.arr = jarray('int', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.root = jcast('int', 0)
Code03_ChocolateKingdom2.ls = jarray('int', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.rs = jarray('int', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.sum = jarray('long', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.xmin = jarray('long', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.xmax = jarray('long', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.ymin = jarray('long', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.ymax = jarray('long', [Code03_ChocolateKingdom2.MAXN])
Code03_ChocolateKingdom2.first = jcast('int', 0)
Code03_ChocolateKingdom2.last = jcast('int', 0)

if __name__ == '__main__':
    Code03_ChocolateKingdom2.main([])
