# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# K-D树结合懒更新，二进制分组的方式，Python版
# 点的坐标有k维，点还有点权，k维空间中的轴对齐区域，可以用两个对角点表示
# 一共有m条操作，类型如下
# 操作 1 qx qv    : 空间里增加一个点，qx是k个值表示点的坐标，qv表示点权
# 操作 2 qx qy qv : 区域的两个对角点qx和qy，各自有k个值的坐标，该区域所有点的点权增加qv
# 操作 3 qx qy    : 区域的两个对角点qx和qy，各自有k个值的坐标，打印该区域所有点的点权和
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 2 <= k <= 3
# 1 <= m <= 10^5
# 坐标、点权、答案都需要long类型
# 测试链接 : https://www.luogu.com.cn/problem/P14312
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_KdtLazyTag4:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'MAXK': 'MAXK', 'INF': 'INF', 'k': 'k', 'm': 'm', 'pos': 'pos', 'val': 'val', 'arr': 'arr', 'qx': 'qx', 'qy': 'qy', 'qv': 'qv', 'cntkdt': 'cntkdt', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'siz': 'siz', 'sum': 'sum', 'minv': 'minv', 'maxv': 'maxv', 'addTag': 'addTag', 'first': 'first', 'last': 'last'}
    MAXN = 0
    MAXP = 0
    MAXK = 0
    INF = 0
    k = 0
    m = 0
    pos = None
    val = None
    arr = None
    qx = None
    qy = None
    qv = 0
    cntkdt = 0
    root = None
    ls = None
    rs = None
    siz = None
    sum = None
    minv = None
    maxv = None
    addTag = None
    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        Code05_KdtLazyTag4.siz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(1, Code05_KdtLazyTag4.siz[Code05_KdtLazyTag4.ls[i]])), Code05_KdtLazyTag4.siz[Code05_KdtLazyTag4.rs[i]])))
        Code05_KdtLazyTag4.sum[i] = jcast('long', jcast('long', jadd(jcast('long', jadd(Code05_KdtLazyTag4.val[i], Code05_KdtLazyTag4.sum[Code05_KdtLazyTag4.ls[i]])), Code05_KdtLazyTag4.sum[Code05_KdtLazyTag4.rs[i]])))
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag4.k):
            jset(Code05_KdtLazyTag4.minv[i], d, jstatic('Math', 'min', Code05_KdtLazyTag4.pos[i][d], jstatic('Math', 'min', Code05_KdtLazyTag4.minv[Code05_KdtLazyTag4.ls[i]][d], Code05_KdtLazyTag4.minv[Code05_KdtLazyTag4.rs[i]][d])))
            jset(Code05_KdtLazyTag4.maxv[i], d, jstatic('Math', 'max', Code05_KdtLazyTag4.pos[i][d], jstatic('Math', 'max', Code05_KdtLazyTag4.maxv[Code05_KdtLazyTag4.ls[i]][d], Code05_KdtLazyTag4.maxv[Code05_KdtLazyTag4.rs[i]][d])))
            d = jcast('int', (d + 1))

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        if (i != 0):
            Code05_KdtLazyTag4.val[i] = jcast('long', jcast('long', jadd(Code05_KdtLazyTag4.val[i], v)))
            Code05_KdtLazyTag4.sum[i] = jcast('long', jcast('long', jadd(Code05_KdtLazyTag4.sum[i], jcast('long', (v * Code05_KdtLazyTag4.siz[i])))))
            Code05_KdtLazyTag4.addTag[i] = jcast('long', jcast('long', jadd(Code05_KdtLazyTag4.addTag[i], v)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code05_KdtLazyTag4.addTag[i] != 0):
            Code05_KdtLazyTag4.lazy(Code05_KdtLazyTag4.ls[i], Code05_KdtLazyTag4.addTag[i])
            Code05_KdtLazyTag4.lazy(Code05_KdtLazyTag4.rs[i], Code05_KdtLazyTag4.addTag[i])
            Code05_KdtLazyTag4.addTag[i] = jcast('long', 0)

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('long', Code05_KdtLazyTag4.pos[i][dimension])
        v2 = jcast('long', Code05_KdtLazyTag4.pos[j][dimension])
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code05_KdtLazyTag4.arr[i])
        Code05_KdtLazyTag4.arr[i] = jcast('int', Code05_KdtLazyTag4.arr[j])
        Code05_KdtLazyTag4.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code05_KdtLazyTag4.first = jcast('int', l)
        Code05_KdtLazyTag4.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code05_KdtLazyTag4.last):
            cmp = jcast('int', Code05_KdtLazyTag4.compareNode(Code05_KdtLazyTag4.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code05_KdtLazyTag4.swap(((_java_obj_1 := Code05_KdtLazyTag4), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code05_KdtLazyTag4.swap(i, ((_java_obj_5 := Code05_KdtLazyTag4), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code05_KdtLazyTag4.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code05_KdtLazyTag4.partition(l, r, pidx, dimension)
                if (i < Code05_KdtLazyTag4.first):
                    r = jcast('int', jcast('int', (Code05_KdtLazyTag4.first - 1)))
                else:
                    if (i > Code05_KdtLazyTag4.last):
                        l = jcast('int', jcast('int', jadd(Code05_KdtLazyTag4.last, 1)))
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
        Code05_KdtLazyTag4.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code05_KdtLazyTag4.arr[mid])
        jset(Code05_KdtLazyTag4.ls, rt, Code05_KdtLazyTag4.build(l, jcast('int', (mid - 1)), jcast('int', jmod(jcast('int', jadd(dimension, 1)), Code05_KdtLazyTag4.k))))
        jset(Code05_KdtLazyTag4.rs, rt, Code05_KdtLazyTag4.build(jcast('int', jadd(mid, 1)), r, jcast('int', jmod(jcast('int', jadd(dimension, 1)), Code05_KdtLazyTag4.k))))
        Code05_KdtLazyTag4.maintain(rt)
        return jcast('int', rt)

    # 分组的树中，懒更新全部下发到底
    @staticmethod
    def dfs(i):
        i = jcast('int', i)
        if (i != 0):
            Code05_KdtLazyTag4.down(i)
            Code05_KdtLazyTag4.dfs(Code05_KdtLazyTag4.ls[i])
            Code05_KdtLazyTag4.dfs(Code05_KdtLazyTag4.rs[i])

    # 二进制分组的方式加入节点
    @staticmethod
    def addNode():
        Code05_KdtLazyTag4.cntkdt = jcast('int', (Code05_KdtLazyTag4.cntkdt + 1))
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag4.k):
            jset(Code05_KdtLazyTag4.pos[Code05_KdtLazyTag4.cntkdt], d, Code05_KdtLazyTag4.qx[d])
            d = jcast('int', (d + 1))
        Code05_KdtLazyTag4.val[Code05_KdtLazyTag4.cntkdt] = jcast('long', Code05_KdtLazyTag4.qv)
        Code05_KdtLazyTag4.arr[Code05_KdtLazyTag4.cntkdt] = jcast('int', Code05_KdtLazyTag4.cntkdt)
        p = jcast('int', 0)
        while (Code05_KdtLazyTag4.root[p] != 0):
            # 合并更大的分组之前，需要先处理懒更新
            Code05_KdtLazyTag4.dfs(Code05_KdtLazyTag4.root[p])
            jset(Code05_KdtLazyTag4.root, ((_java_old_9 := p), (p := jcast('int', (p + (1)))), _java_old_9)[2], 0)
        jset(Code05_KdtLazyTag4.root, p, Code05_KdtLazyTag4.build(jcast('int', jadd(jcast('int', (Code05_KdtLazyTag4.cntkdt - jcast('int', (1 << (p & 31))))), 1)), Code05_KdtLazyTag4.cntkdt, 0))

    @staticmethod
    def outside(i):
        i = jcast('int', i)
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag4.k):
            if ((Code05_KdtLazyTag4.maxv[i][d] < Code05_KdtLazyTag4.qx[d]) or (Code05_KdtLazyTag4.qy[d] < Code05_KdtLazyTag4.minv[i][d])):
                return jcast('boolean', True)
            d = jcast('int', (d + 1))
        return jcast('boolean', False)

    @staticmethod
    def covered(i):
        i = jcast('int', i)
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag4.k):
            if ((Code05_KdtLazyTag4.qx[d] > Code05_KdtLazyTag4.minv[i][d]) or (Code05_KdtLazyTag4.qy[d] < Code05_KdtLazyTag4.maxv[i][d])):
                return jcast('boolean', False)
            d = jcast('int', (d + 1))
        return jcast('boolean', True)

    @staticmethod
    def pointIn(i):
        i = jcast('int', i)
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag4.k):
            if ((Code05_KdtLazyTag4.qx[d] > Code05_KdtLazyTag4.pos[i][d]) or (Code05_KdtLazyTag4.qy[d] < Code05_KdtLazyTag4.pos[i][d])):
                return jcast('boolean', False)
            d = jcast('int', (d + 1))
        return jcast('boolean', True)

    @staticmethod
    def _java_addValue_0(i):
        i = jcast('int', i)
        if (i == 0):
            return
        if Code05_KdtLazyTag4.outside(i):
            return
        if Code05_KdtLazyTag4.covered(i):
            Code05_KdtLazyTag4.lazy(i, Code05_KdtLazyTag4.qv)
            return
        if Code05_KdtLazyTag4.pointIn(i):
            Code05_KdtLazyTag4.val[i] = jcast('long', jcast('long', jadd(Code05_KdtLazyTag4.val[i], Code05_KdtLazyTag4.qv)))
        Code05_KdtLazyTag4.down(i)
        Code05_KdtLazyTag4._java_addValue_0(Code05_KdtLazyTag4.ls[i])
        Code05_KdtLazyTag4._java_addValue_0(Code05_KdtLazyTag4.rs[i])
        Code05_KdtLazyTag4.maintain(i)

    # 每棵分树都要修改
    @staticmethod
    def _java_addValue_1():
        p = jcast('int', 0)
        while (p < Code05_KdtLazyTag4.MAXP):
            Code05_KdtLazyTag4._java_addValue_0(Code05_KdtLazyTag4.root[p])
            p = jcast('int', (p + 1))

    @staticmethod
    def _java_querySum_0(i):
        i = jcast('int', i)
        if (i == 0):
            return jcast('long', 0)
        if Code05_KdtLazyTag4.outside(i):
            return jcast('long', 0)
        if Code05_KdtLazyTag4.covered(i):
            return jcast('long', Code05_KdtLazyTag4.sum[i])
        ans = jcast('long', 0)
        if Code05_KdtLazyTag4.pointIn(i):
            ans = jcast('long', jcast('long', jadd(ans, Code05_KdtLazyTag4.val[i])))
        Code05_KdtLazyTag4.down(i)
        ans = jcast('long', jcast('long', jadd(ans, Code05_KdtLazyTag4._java_querySum_0(Code05_KdtLazyTag4.ls[i]))))
        ans = jcast('long', jcast('long', jadd(ans, Code05_KdtLazyTag4._java_querySum_0(Code05_KdtLazyTag4.rs[i]))))
        return jcast('long', ans)

    # 每棵分树都要查询
    @staticmethod
    def _java_querySum_1():
        ans = jcast('long', 0)
        p = jcast('int', 0)
        while (p < Code05_KdtLazyTag4.MAXP):
            ans = jcast('long', jcast('long', jadd(ans, Code05_KdtLazyTag4._java_querySum_0(Code05_KdtLazyTag4.root[p]))))
            p = jcast('int', (p + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code05_KdtLazyTag4.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_KdtLazyTag4.k = jcast('int', jcall(in_, 'nextInt'))
        Code05_KdtLazyTag4.m = jcast('int', jcall(in_, 'nextInt'))
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag4.k):
            jset(Code05_KdtLazyTag4.minv[0], d, Code05_KdtLazyTag4.INF)
            jset(Code05_KdtLazyTag4.maxv[0], d, jcast('long', (-Code05_KdtLazyTag4.INF)))
            d = jcast('int', (d + 1))
        lastAns = jcast('long', 0)
        i = jcast('int', 1)
        op = 0
        while (i <= Code05_KdtLazyTag4.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                d = jcast('int', 0)
                while (d < Code05_KdtLazyTag4.k):
                    jset(Code05_KdtLazyTag4.qx, d, jcall(in_, 'nextLong'))
                    Code05_KdtLazyTag4.qx[d] = jcast('long', jcast('long', (Code05_KdtLazyTag4.qx[d] ^ lastAns)))
                    d = jcast('int', (d + 1))
                Code05_KdtLazyTag4.qv = jcast('long', jcall(in_, 'nextLong'))
                Code05_KdtLazyTag4.qv = jcast('long', jcast('long', (Code05_KdtLazyTag4.qv ^ lastAns)))
                Code05_KdtLazyTag4.addNode()
            else:
                d = jcast('int', 0)
                while (d < Code05_KdtLazyTag4.k):
                    jset(Code05_KdtLazyTag4.qx, d, jcall(in_, 'nextLong'))
                    Code05_KdtLazyTag4.qx[d] = jcast('long', jcast('long', (Code05_KdtLazyTag4.qx[d] ^ lastAns)))
                    d = jcast('int', (d + 1))
                d = jcast('int', 0)
                while (d < Code05_KdtLazyTag4.k):
                    jset(Code05_KdtLazyTag4.qy, d, jcall(in_, 'nextLong'))
                    Code05_KdtLazyTag4.qy[d] = jcast('long', jcast('long', (Code05_KdtLazyTag4.qy[d] ^ lastAns)))
                    d = jcast('int', (d + 1))
                if (op == 2):
                    Code05_KdtLazyTag4.qv = jcast('long', jcall(in_, 'nextLong'))
                    Code05_KdtLazyTag4.qv = jcast('long', jcast('long', (Code05_KdtLazyTag4.qv ^ lastAns)))
                    Code05_KdtLazyTag4._java_addValue_1()
                else:
                    lastAns = jcast('long', Code05_KdtLazyTag4._java_querySum_1())
                    jcall(out, 'println', lastAns)
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
            raise TypeError("No matching overload for Code05_KdtLazyTag4.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def addValue(*args):
        _java_choice = jselect(args, [['int'], []], [False, False])
        if _java_choice == 0:
            return Code05_KdtLazyTag4._java_addValue_0(*args)
        if _java_choice == 1:
            return Code05_KdtLazyTag4._java_addValue_1(*args)
        raise TypeError("No matching overload for Code05_KdtLazyTag4.addValue")

    @staticmethod
    def querySum(*args):
        _java_choice = jselect(args, [['int'], []], [False, False])
        if _java_choice == 0:
            return Code05_KdtLazyTag4._java_querySum_0(*args)
        if _java_choice == 1:
            return Code05_KdtLazyTag4._java_querySum_1(*args)
        raise TypeError("No matching overload for Code05_KdtLazyTag4.querySum")


Code05_KdtLazyTag4.MAXN = jcast('int', 200001)
Code05_KdtLazyTag4.MAXP = jcast('int', 19)
Code05_KdtLazyTag4.MAXK = jcast('int', 3)
Code05_KdtLazyTag4.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code05_KdtLazyTag4.k = jcast('int', 0)
Code05_KdtLazyTag4.m = jcast('int', 0)
Code05_KdtLazyTag4.pos = jarray('long', [Code05_KdtLazyTag4.MAXN, Code05_KdtLazyTag4.MAXK])
Code05_KdtLazyTag4.val = jarray('long', [Code05_KdtLazyTag4.MAXN])
Code05_KdtLazyTag4.arr = jarray('int', [Code05_KdtLazyTag4.MAXN])
Code05_KdtLazyTag4.qx = jarray('long', [Code05_KdtLazyTag4.MAXK])
Code05_KdtLazyTag4.qy = jarray('long', [Code05_KdtLazyTag4.MAXK])
Code05_KdtLazyTag4.qv = jcast('long', 0)
Code05_KdtLazyTag4.cntkdt = jcast('int', 0)
Code05_KdtLazyTag4.root = jarray('int', [Code05_KdtLazyTag4.MAXP])
Code05_KdtLazyTag4.ls = jarray('int', [Code05_KdtLazyTag4.MAXN])
Code05_KdtLazyTag4.rs = jarray('int', [Code05_KdtLazyTag4.MAXN])
Code05_KdtLazyTag4.siz = jarray('int', [Code05_KdtLazyTag4.MAXN])
Code05_KdtLazyTag4.sum = jarray('long', [Code05_KdtLazyTag4.MAXN])
Code05_KdtLazyTag4.minv = jarray('long', [Code05_KdtLazyTag4.MAXN, Code05_KdtLazyTag4.MAXK])
Code05_KdtLazyTag4.maxv = jarray('long', [Code05_KdtLazyTag4.MAXN, Code05_KdtLazyTag4.MAXK])
Code05_KdtLazyTag4.addTag = jarray('long', [Code05_KdtLazyTag4.MAXN])
Code05_KdtLazyTag4.first = jcast('int', 0)
Code05_KdtLazyTag4.last = jcast('int', 0)

if __name__ == '__main__':
    Code05_KdtLazyTag4.main([])
