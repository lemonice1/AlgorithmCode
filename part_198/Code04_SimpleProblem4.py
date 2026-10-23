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

# 简单题，二进制分组的方式，Python版
# 有一个n * n的平面区域，初始时没有点，有若干条操作，类型如下
# 操作 1 a b c   : 平面里增加一个点，坐标(a, b)，点权为c
# 操作 2 a b c d : 查询(a, b)为左下角、(c, d)为右上角的区域中，所有点的点权和
# 操作 3         : 终止，以后没有操作了
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 1 <= n <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4148
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_SimpleProblem4:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'INF': 'INF', 'n': 'n', 'x': 'x', 'y': 'y', 'v': 'v', 'arr': 'arr', 'cntkdt': 'cntkdt', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'first': 'first', 'last': 'last'}
    MAXN = 0
    MAXP = 0
    INF = 0
    n = 0
    x = None
    y = None
    v = None
    arr = None
    # K-D树的节点计数
    cntkdt = 0
    # root[p]表示大小为2的p次方的K-D树，根节点编号
    root = None
    ls = None
    rs = None
    sum = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        Code04_SimpleProblem4.sum[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_SimpleProblem4.v[i], Code04_SimpleProblem4.sum[Code04_SimpleProblem4.ls[i]])), Code04_SimpleProblem4.sum[Code04_SimpleProblem4.rs[i]])))
        jset(Code04_SimpleProblem4.xmin, i, jstatic('Math', 'min', Code04_SimpleProblem4.x[i], jstatic('Math', 'min', Code04_SimpleProblem4.xmin[Code04_SimpleProblem4.ls[i]], Code04_SimpleProblem4.xmin[Code04_SimpleProblem4.rs[i]])))
        jset(Code04_SimpleProblem4.xmax, i, jstatic('Math', 'max', Code04_SimpleProblem4.x[i], jstatic('Math', 'max', Code04_SimpleProblem4.xmax[Code04_SimpleProblem4.ls[i]], Code04_SimpleProblem4.xmax[Code04_SimpleProblem4.rs[i]])))
        jset(Code04_SimpleProblem4.ymin, i, jstatic('Math', 'min', Code04_SimpleProblem4.y[i], jstatic('Math', 'min', Code04_SimpleProblem4.ymin[Code04_SimpleProblem4.ls[i]], Code04_SimpleProblem4.ymin[Code04_SimpleProblem4.rs[i]])))
        jset(Code04_SimpleProblem4.ymax, i, jstatic('Math', 'max', Code04_SimpleProblem4.y[i], jstatic('Math', 'max', Code04_SimpleProblem4.ymax[Code04_SimpleProblem4.ls[i]], Code04_SimpleProblem4.ymax[Code04_SimpleProblem4.rs[i]])))

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('int', (Code04_SimpleProblem4.x[i] if (dimension == 0) else Code04_SimpleProblem4.y[i]))
        v2 = jcast('int', (Code04_SimpleProblem4.x[j] if (dimension == 0) else Code04_SimpleProblem4.y[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code04_SimpleProblem4.arr[i])
        Code04_SimpleProblem4.arr[i] = jcast('int', Code04_SimpleProblem4.arr[j])
        Code04_SimpleProblem4.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code04_SimpleProblem4.first = jcast('int', l)
        Code04_SimpleProblem4.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code04_SimpleProblem4.last):
            cmp = jcast('int', Code04_SimpleProblem4.compareNode(Code04_SimpleProblem4.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code04_SimpleProblem4.swap(((_java_obj_1 := Code04_SimpleProblem4), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code04_SimpleProblem4.swap(i, ((_java_obj_5 := Code04_SimpleProblem4), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code04_SimpleProblem4.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code04_SimpleProblem4.partition(l, r, pidx, dimension)
                if (i < Code04_SimpleProblem4.first):
                    r = jcast('int', jcast('int', (Code04_SimpleProblem4.first - 1)))
                else:
                    if (i > Code04_SimpleProblem4.last):
                        l = jcast('int', jcast('int', jadd(Code04_SimpleProblem4.last, 1)))
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
        Code04_SimpleProblem4.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code04_SimpleProblem4.arr[mid])
        jset(Code04_SimpleProblem4.ls, rt, Code04_SimpleProblem4.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code04_SimpleProblem4.rs, rt, Code04_SimpleProblem4.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code04_SimpleProblem4.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def add(qx, qy, qv):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        qv = jcast('int', qv)
        Code04_SimpleProblem4.cntkdt = jcast('int', (Code04_SimpleProblem4.cntkdt + 1))
        Code04_SimpleProblem4.x[Code04_SimpleProblem4.cntkdt] = jcast('int', qx)
        Code04_SimpleProblem4.y[Code04_SimpleProblem4.cntkdt] = jcast('int', qy)
        Code04_SimpleProblem4.v[Code04_SimpleProblem4.cntkdt] = jcast('int', qv)
        Code04_SimpleProblem4.arr[Code04_SimpleProblem4.cntkdt] = jcast('int', Code04_SimpleProblem4.cntkdt)
        p = jcast('int', 0)
        while (Code04_SimpleProblem4.root[p] != 0):
            jset(Code04_SimpleProblem4.root, ((_java_old_9 := p), (p := jcast('int', (p + (1)))), _java_old_9)[2], 0)
        jset(Code04_SimpleProblem4.root, p, Code04_SimpleProblem4.build(jcast('int', jadd(jcast('int', (Code04_SimpleProblem4.cntkdt - jcast('int', (1 << (p & 31))))), 1)), Code04_SimpleProblem4.cntkdt, 0))

    @staticmethod
    def _java_query_0(x1, y1, x2, y2, i):
        x1 = jcast('int', x1)
        y1 = jcast('int', y1)
        x2 = jcast('int', x2)
        y2 = jcast('int', y2)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if ((((Code04_SimpleProblem4.xmax[i] < x1) or (x2 < Code04_SimpleProblem4.xmin[i])) or (Code04_SimpleProblem4.ymax[i] < y1)) or (y2 < Code04_SimpleProblem4.ymin[i])):
            return jcast('int', 0)
        if ((((x1 <= Code04_SimpleProblem4.xmin[i]) and (Code04_SimpleProblem4.xmax[i] <= x2)) and (y1 <= Code04_SimpleProblem4.ymin[i])) and (Code04_SimpleProblem4.ymax[i] <= y2)):
            return jcast('int', Code04_SimpleProblem4.sum[i])
        ans = jcast('int', 0)
        if ((((x1 <= Code04_SimpleProblem4.x[i]) and (Code04_SimpleProblem4.x[i] <= x2)) and (y1 <= Code04_SimpleProblem4.y[i])) and (Code04_SimpleProblem4.y[i] <= y2)):
            ans = jcast('int', jcast('int', jadd(ans, Code04_SimpleProblem4.v[i])))
        ans = jcast('int', jcast('int', jadd(ans, Code04_SimpleProblem4._java_query_0(x1, y1, x2, y2, Code04_SimpleProblem4.ls[i]))))
        ans = jcast('int', jcast('int', jadd(ans, Code04_SimpleProblem4._java_query_0(x1, y1, x2, y2, Code04_SimpleProblem4.rs[i]))))
        return jcast('int', ans)

    @staticmethod
    def _java_query_1(x1, y1, x2, y2):
        x1 = jcast('int', x1)
        y1 = jcast('int', y1)
        x2 = jcast('int', x2)
        y2 = jcast('int', y2)
        ans = jcast('int', 0)
        p = jcast('int', 0)
        while (p < Code04_SimpleProblem4.MAXP):
            ans = jcast('int', jcast('int', jadd(ans, Code04_SimpleProblem4._java_query_0(x1, y1, x2, y2, Code04_SimpleProblem4.root[p]))))
            p = jcast('int', (p + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code04_SimpleProblem4.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        # 输入的n没用
        Code04_SimpleProblem4.n = jcast('int', jcall(in_, 'nextInt'))
        jset(Code04_SimpleProblem4.xmin, 0, jset(Code04_SimpleProblem4.ymin, 0, Code04_SimpleProblem4.INF))
        jset(Code04_SimpleProblem4.xmax, 0, jset(Code04_SimpleProblem4.ymax, 0, jcast('int', (-Code04_SimpleProblem4.INF))))
        op = 0
        a = 0
        b = 0
        c = 0
        d = 0
        lastAns = 0
        op = jcast('int', jcall(in_, 'nextInt'))
        lastAns = jcast('int', 0)
        while (op != 3):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            a = jcast('int', jcast('int', (a ^ lastAns)))
            b = jcast('int', jcast('int', (b ^ lastAns)))
            c = jcast('int', jcast('int', (c ^ lastAns)))
            if (op == 1):
                Code04_SimpleProblem4.add(a, b, c)
            else:
                d = jcast('int', jcall(in_, 'nextInt'))
                d = jcast('int', jcast('int', (d ^ lastAns)))
                lastAns = jcast('int', Code04_SimpleProblem4._java_query_1(a, b, c, d))
                jcall(out, 'println', lastAns)
            op = jcast('int', jcall(in_, 'nextInt'))
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

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_SimpleProblem4.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def query(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code04_SimpleProblem4._java_query_0(*args)
        if _java_choice == 1:
            return Code04_SimpleProblem4._java_query_1(*args)
        raise TypeError("No matching overload for Code04_SimpleProblem4.query")


Code04_SimpleProblem4.MAXN = jcast('int', 200001)
Code04_SimpleProblem4.MAXP = jcast('int', 19)
Code04_SimpleProblem4.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code04_SimpleProblem4.n = jcast('int', 0)
Code04_SimpleProblem4.x = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.y = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.v = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.arr = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.cntkdt = jcast('int', 0)
Code04_SimpleProblem4.root = jarray('int', [Code04_SimpleProblem4.MAXP])
Code04_SimpleProblem4.ls = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.rs = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.sum = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.xmin = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.xmax = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.ymin = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.ymax = jarray('int', [Code04_SimpleProblem4.MAXN])
Code04_SimpleProblem4.first = jcast('int', 0)
Code04_SimpleProblem4.last = jcast('int', 0)

if __name__ == '__main__':
    Code04_SimpleProblem4.main([])
