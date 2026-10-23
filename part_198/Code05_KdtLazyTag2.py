# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# K-D树结合懒更新，替罪羊树的方式，Python版
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
class Code05_KdtLazyTag2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'INF': 'INF', 'k': 'k', 'm': 'm', 'pos': 'pos', 'val': 'val', 'qx': 'qx', 'qy': 'qy', 'qv': 'qv', 'cntkdt': 'cntkdt', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'siz': 'siz', 'sum': 'sum', 'minv': 'minv', 'maxv': 'maxv', 'addTag': 'addTag', 'ALPHA': 'ALPHA', 'top': 'top', 'topFather': 'topFather', 'topSide': 'topSide', 'topDimension': 'topDimension', 'arr': 'arr', 'treeSiz': 'treeSiz', 'first': 'first', 'last': 'last'}
    MAXN = 0
    MAXK = 0
    INF = 0
    k = 0
    m = 0
    # 每个点有k个坐标值
    pos = None
    # 每个点有点权
    val = None
    # 每次操作给定的参数
    qx = None
    qy = None
    qv = 0
    # 动态K-D树，替罪羊树的方式
    cntkdt = 0
    root = 0
    ls = None
    rs = None
    siz = None
    sum = None
    # 每个点掌管的区域内，每个维度都有范围，最小值、最大值
    minv = None
    maxv = None
    # 懒更新标记
    addTag = None
    # 重构
    ALPHA = 0.0
    top = 0
    topFather = 0
    topSide = 0
    topDimension = 0
    arr = None
    treeSiz = 0
    @staticmethod
    def init():
        Code05_KdtLazyTag2.cntkdt = jcast('int', (Code05_KdtLazyTag2.cntkdt + 1))
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag2.k):
            jset(Code05_KdtLazyTag2.pos[Code05_KdtLazyTag2.cntkdt], d, Code05_KdtLazyTag2.qx[d])
            jset(Code05_KdtLazyTag2.minv[Code05_KdtLazyTag2.cntkdt], d, jset(Code05_KdtLazyTag2.maxv[Code05_KdtLazyTag2.cntkdt], d, Code05_KdtLazyTag2.qx[d]))
            d = jcast('int', (d + 1))
        Code05_KdtLazyTag2.val[Code05_KdtLazyTag2.cntkdt] = jcast('long', Code05_KdtLazyTag2.qv)
        jset(Code05_KdtLazyTag2.ls, Code05_KdtLazyTag2.cntkdt, jset(Code05_KdtLazyTag2.rs, Code05_KdtLazyTag2.cntkdt, 0))
        Code05_KdtLazyTag2.siz[Code05_KdtLazyTag2.cntkdt] = jcast('int', 1)
        Code05_KdtLazyTag2.sum[Code05_KdtLazyTag2.cntkdt] = jcast('long', Code05_KdtLazyTag2.qv)
        Code05_KdtLazyTag2.addTag[Code05_KdtLazyTag2.cntkdt] = jcast('long', 0)
        return jcast('int', Code05_KdtLazyTag2.cntkdt)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        Code05_KdtLazyTag2.siz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(1, Code05_KdtLazyTag2.siz[Code05_KdtLazyTag2.ls[i]])), Code05_KdtLazyTag2.siz[Code05_KdtLazyTag2.rs[i]])))
        Code05_KdtLazyTag2.sum[i] = jcast('long', jcast('long', jadd(jcast('long', jadd(Code05_KdtLazyTag2.val[i], Code05_KdtLazyTag2.sum[Code05_KdtLazyTag2.ls[i]])), Code05_KdtLazyTag2.sum[Code05_KdtLazyTag2.rs[i]])))
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag2.k):
            jset(Code05_KdtLazyTag2.minv[i], d, jstatic('Math', 'min', Code05_KdtLazyTag2.pos[i][d], jstatic('Math', 'min', Code05_KdtLazyTag2.minv[Code05_KdtLazyTag2.ls[i]][d], Code05_KdtLazyTag2.minv[Code05_KdtLazyTag2.rs[i]][d])))
            jset(Code05_KdtLazyTag2.maxv[i], d, jstatic('Math', 'max', Code05_KdtLazyTag2.pos[i][d], jstatic('Math', 'max', Code05_KdtLazyTag2.maxv[Code05_KdtLazyTag2.ls[i]][d], Code05_KdtLazyTag2.maxv[Code05_KdtLazyTag2.rs[i]][d])))
            d = jcast('int', (d + 1))

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        if (i != 0):
            Code05_KdtLazyTag2.val[i] = jcast('long', jcast('long', jadd(Code05_KdtLazyTag2.val[i], v)))
            Code05_KdtLazyTag2.sum[i] = jcast('long', jcast('long', jadd(Code05_KdtLazyTag2.sum[i], jcast('long', (v * Code05_KdtLazyTag2.siz[i])))))
            Code05_KdtLazyTag2.addTag[i] = jcast('long', jcast('long', jadd(Code05_KdtLazyTag2.addTag[i], v)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code05_KdtLazyTag2.addTag[i] != 0):
            Code05_KdtLazyTag2.lazy(Code05_KdtLazyTag2.ls[i], Code05_KdtLazyTag2.addTag[i])
            Code05_KdtLazyTag2.lazy(Code05_KdtLazyTag2.rs[i], Code05_KdtLazyTag2.addTag[i])
            Code05_KdtLazyTag2.addTag[i] = jcast('long', 0)

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('long', Code05_KdtLazyTag2.pos[i][dimension])
        v2 = jcast('long', Code05_KdtLazyTag2.pos[j][dimension])
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code05_KdtLazyTag2.arr[i])
        Code05_KdtLazyTag2.arr[i] = jcast('int', Code05_KdtLazyTag2.arr[j])
        Code05_KdtLazyTag2.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code05_KdtLazyTag2.first = jcast('int', l)
        Code05_KdtLazyTag2.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code05_KdtLazyTag2.last):
            cmp = jcast('int', Code05_KdtLazyTag2.compareNode(Code05_KdtLazyTag2.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code05_KdtLazyTag2.swap(((_java_obj_1 := Code05_KdtLazyTag2), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code05_KdtLazyTag2.swap(i, ((_java_obj_5 := Code05_KdtLazyTag2), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code05_KdtLazyTag2.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code05_KdtLazyTag2.partition(l, r, pidx, dimension)
                if (i < Code05_KdtLazyTag2.first):
                    r = jcast('int', jcast('int', (Code05_KdtLazyTag2.first - 1)))
                else:
                    if (i > Code05_KdtLazyTag2.last):
                        l = jcast('int', jcast('int', jadd(Code05_KdtLazyTag2.last, 1)))
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
        Code05_KdtLazyTag2.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code05_KdtLazyTag2.arr[mid])
        jset(Code05_KdtLazyTag2.ls, rt, Code05_KdtLazyTag2.build(l, jcast('int', (mid - 1)), jcast('int', jmod(jcast('int', jadd(dimension, 1)), Code05_KdtLazyTag2.k))))
        jset(Code05_KdtLazyTag2.rs, rt, Code05_KdtLazyTag2.build(jcast('int', jadd(mid, 1)), r, jcast('int', jmod(jcast('int', jadd(dimension, 1)), Code05_KdtLazyTag2.k))))
        Code05_KdtLazyTag2.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code05_KdtLazyTag2.ALPHA * Code05_KdtLazyTag2.siz[i]) >= jstatic('Math', 'max', Code05_KdtLazyTag2.siz[Code05_KdtLazyTag2.ls[i]], Code05_KdtLazyTag2.siz[Code05_KdtLazyTag2.rs[i]])))

    @staticmethod
    def dfs(i):
        i = jcast('int', i)
        if (i != 0):
            # 懒更新信息下发
            Code05_KdtLazyTag2.down(i)
            jset(Code05_KdtLazyTag2.arr, ((_java_obj_9 := Code05_KdtLazyTag2), (_java_key_10 := 'treeSiz'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], i)
            Code05_KdtLazyTag2.dfs(Code05_KdtLazyTag2.ls[i])
            Code05_KdtLazyTag2.dfs(Code05_KdtLazyTag2.rs[i])

    @staticmethod
    def rebuild():
        if (Code05_KdtLazyTag2.top != 0):
            Code05_KdtLazyTag2.treeSiz = jcast('int', 0)
            Code05_KdtLazyTag2.dfs(Code05_KdtLazyTag2.top)
            newRoot = jcast('int', Code05_KdtLazyTag2.build(1, Code05_KdtLazyTag2.treeSiz, Code05_KdtLazyTag2.topDimension))
            if (Code05_KdtLazyTag2.topFather == 0):
                Code05_KdtLazyTag2.root = jcast('int', newRoot)
            else:
                if (Code05_KdtLazyTag2.topSide == 1):
                    Code05_KdtLazyTag2.ls[Code05_KdtLazyTag2.topFather] = jcast('int', newRoot)
                else:
                    Code05_KdtLazyTag2.rs[Code05_KdtLazyTag2.topFather] = jcast('int', newRoot)

    @staticmethod
    def add(insertNode, u, fa, side, dimension):
        insertNode = jcast('int', insertNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if (u == 0):
            return jcast('int', insertNode)
        # 懒更新信息下发
        Code05_KdtLazyTag2.down(u)
        if (Code05_KdtLazyTag2.compareNode(insertNode, u, dimension) <= 0):
            jset(Code05_KdtLazyTag2.ls, u, Code05_KdtLazyTag2.add(insertNode, Code05_KdtLazyTag2.ls[u], u, 1, jcast('int', jmod(jcast('int', jadd(dimension, 1)), Code05_KdtLazyTag2.k))))
        else:
            jset(Code05_KdtLazyTag2.rs, u, Code05_KdtLazyTag2.add(insertNode, Code05_KdtLazyTag2.rs[u], u, 2, jcast('int', jmod(jcast('int', jadd(dimension, 1)), Code05_KdtLazyTag2.k))))
        Code05_KdtLazyTag2.maintain(u)
        if (not Code05_KdtLazyTag2.balance(u)):
            Code05_KdtLazyTag2.top = jcast('int', u)
            Code05_KdtLazyTag2.topFather = jcast('int', fa)
            Code05_KdtLazyTag2.topSide = jcast('int', side)
            Code05_KdtLazyTag2.topDimension = jcast('int', dimension)
        return jcast('int', u)

    @staticmethod
    def addNode():
        Code05_KdtLazyTag2.top = jcast('int', jset(Code05_KdtLazyTag2, 'topFather', jset(Code05_KdtLazyTag2, 'topSide', jset(Code05_KdtLazyTag2, 'topDimension', 0))))
        insertNode = jcast('int', Code05_KdtLazyTag2.init())
        Code05_KdtLazyTag2.root = jcast('int', Code05_KdtLazyTag2.add(insertNode, Code05_KdtLazyTag2.root, 0, 0, 0))
        Code05_KdtLazyTag2.rebuild()

    # 判断操作区域是否和节点i的区域无交集
    @staticmethod
    def outside(i):
        i = jcast('int', i)
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag2.k):
            if ((Code05_KdtLazyTag2.maxv[i][d] < Code05_KdtLazyTag2.qx[d]) or (Code05_KdtLazyTag2.qy[d] < Code05_KdtLazyTag2.minv[i][d])):
                return jcast('boolean', True)
            d = jcast('int', (d + 1))
        return jcast('boolean', False)

    # 判断操作区域是否完全包住节点i的区域
    @staticmethod
    def covered(i):
        i = jcast('int', i)
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag2.k):
            if ((Code05_KdtLazyTag2.qx[d] > Code05_KdtLazyTag2.minv[i][d]) or (Code05_KdtLazyTag2.qy[d] < Code05_KdtLazyTag2.maxv[i][d])):
                return jcast('boolean', False)
            d = jcast('int', (d + 1))
        return jcast('boolean', True)

    # 判断操作区域是否包含节点i这个单点
    @staticmethod
    def pointIn(i):
        i = jcast('int', i)
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag2.k):
            if ((Code05_KdtLazyTag2.qx[d] > Code05_KdtLazyTag2.pos[i][d]) or (Code05_KdtLazyTag2.qy[d] < Code05_KdtLazyTag2.pos[i][d])):
                return jcast('boolean', False)
            d = jcast('int', (d + 1))
        return jcast('boolean', True)

    @staticmethod
    def addValue(i):
        i = jcast('int', i)
        if (i == 0):
            return
        if Code05_KdtLazyTag2.outside(i):
            return
        if Code05_KdtLazyTag2.covered(i):
            Code05_KdtLazyTag2.lazy(i, Code05_KdtLazyTag2.qv)
            return
        if Code05_KdtLazyTag2.pointIn(i):
            Code05_KdtLazyTag2.val[i] = jcast('long', jcast('long', jadd(Code05_KdtLazyTag2.val[i], Code05_KdtLazyTag2.qv)))
        # 懒更新信息下发
        Code05_KdtLazyTag2.down(i)
        Code05_KdtLazyTag2.addValue(Code05_KdtLazyTag2.ls[i])
        Code05_KdtLazyTag2.addValue(Code05_KdtLazyTag2.rs[i])
        Code05_KdtLazyTag2.maintain(i)

    @staticmethod
    def querySum(i):
        i = jcast('int', i)
        if (i == 0):
            return jcast('long', 0)
        if Code05_KdtLazyTag2.outside(i):
            return jcast('long', 0)
        if Code05_KdtLazyTag2.covered(i):
            return jcast('long', Code05_KdtLazyTag2.sum[i])
        ans = jcast('long', 0)
        if Code05_KdtLazyTag2.pointIn(i):
            ans = jcast('long', jcast('long', jadd(ans, Code05_KdtLazyTag2.val[i])))
        # 懒更新信息下发
        Code05_KdtLazyTag2.down(i)
        ans = jcast('long', jcast('long', jadd(ans, Code05_KdtLazyTag2.querySum(Code05_KdtLazyTag2.ls[i]))))
        ans = jcast('long', jcast('long', jadd(ans, Code05_KdtLazyTag2.querySum(Code05_KdtLazyTag2.rs[i]))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code05_KdtLazyTag2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_KdtLazyTag2.k = jcast('int', jcall(in_, 'nextInt'))
        Code05_KdtLazyTag2.m = jcast('int', jcall(in_, 'nextInt'))
        d = jcast('int', 0)
        while (d < Code05_KdtLazyTag2.k):
            jset(Code05_KdtLazyTag2.minv[0], d, Code05_KdtLazyTag2.INF)
            jset(Code05_KdtLazyTag2.maxv[0], d, jcast('long', (-Code05_KdtLazyTag2.INF)))
            d = jcast('int', (d + 1))
        lastAns = jcast('long', 0)
        i = jcast('int', 1)
        op = 0
        while (i <= Code05_KdtLazyTag2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                d = jcast('int', 0)
                while (d < Code05_KdtLazyTag2.k):
                    jset(Code05_KdtLazyTag2.qx, d, jcall(in_, 'nextLong'))
                    Code05_KdtLazyTag2.qx[d] = jcast('long', jcast('long', (Code05_KdtLazyTag2.qx[d] ^ lastAns)))
                    d = jcast('int', (d + 1))
                Code05_KdtLazyTag2.qv = jcast('long', jcall(in_, 'nextLong'))
                Code05_KdtLazyTag2.qv = jcast('long', jcast('long', (Code05_KdtLazyTag2.qv ^ lastAns)))
                Code05_KdtLazyTag2.addNode()
            else:
                d = jcast('int', 0)
                while (d < Code05_KdtLazyTag2.k):
                    jset(Code05_KdtLazyTag2.qx, d, jcall(in_, 'nextLong'))
                    Code05_KdtLazyTag2.qx[d] = jcast('long', jcast('long', (Code05_KdtLazyTag2.qx[d] ^ lastAns)))
                    d = jcast('int', (d + 1))
                d = jcast('int', 0)
                while (d < Code05_KdtLazyTag2.k):
                    jset(Code05_KdtLazyTag2.qy, d, jcall(in_, 'nextLong'))
                    Code05_KdtLazyTag2.qy[d] = jcast('long', jcast('long', (Code05_KdtLazyTag2.qy[d] ^ lastAns)))
                    d = jcast('int', (d + 1))
                if (op == 2):
                    Code05_KdtLazyTag2.qv = jcast('long', jcall(in_, 'nextLong'))
                    Code05_KdtLazyTag2.qv = jcast('long', jcast('long', (Code05_KdtLazyTag2.qv ^ lastAns)))
                    Code05_KdtLazyTag2.addValue(Code05_KdtLazyTag2.root)
                else:
                    lastAns = jcast('long', Code05_KdtLazyTag2.querySum(Code05_KdtLazyTag2.root))
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
            raise TypeError("No matching overload for Code05_KdtLazyTag2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_KdtLazyTag2.MAXN = jcast('int', 200001)
Code05_KdtLazyTag2.MAXK = jcast('int', 3)
Code05_KdtLazyTag2.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code05_KdtLazyTag2.k = jcast('int', 0)
Code05_KdtLazyTag2.m = jcast('int', 0)
Code05_KdtLazyTag2.pos = jarray('long', [Code05_KdtLazyTag2.MAXN, Code05_KdtLazyTag2.MAXK])
Code05_KdtLazyTag2.val = jarray('long', [Code05_KdtLazyTag2.MAXN])
Code05_KdtLazyTag2.qx = jarray('long', [Code05_KdtLazyTag2.MAXK])
Code05_KdtLazyTag2.qy = jarray('long', [Code05_KdtLazyTag2.MAXK])
Code05_KdtLazyTag2.qv = jcast('long', 0)
Code05_KdtLazyTag2.cntkdt = jcast('int', 0)
Code05_KdtLazyTag2.root = jcast('int', 0)
Code05_KdtLazyTag2.ls = jarray('int', [Code05_KdtLazyTag2.MAXN])
Code05_KdtLazyTag2.rs = jarray('int', [Code05_KdtLazyTag2.MAXN])
Code05_KdtLazyTag2.siz = jarray('int', [Code05_KdtLazyTag2.MAXN])
Code05_KdtLazyTag2.sum = jarray('long', [Code05_KdtLazyTag2.MAXN])
Code05_KdtLazyTag2.minv = jarray('long', [Code05_KdtLazyTag2.MAXN, Code05_KdtLazyTag2.MAXK])
Code05_KdtLazyTag2.maxv = jarray('long', [Code05_KdtLazyTag2.MAXN, Code05_KdtLazyTag2.MAXK])
Code05_KdtLazyTag2.addTag = jarray('long', [Code05_KdtLazyTag2.MAXN])
Code05_KdtLazyTag2.ALPHA = jcast('double', 0.7)
Code05_KdtLazyTag2.top = jcast('int', 0)
Code05_KdtLazyTag2.topFather = jcast('int', 0)
Code05_KdtLazyTag2.topSide = jcast('int', 0)
Code05_KdtLazyTag2.topDimension = jcast('int', 0)
Code05_KdtLazyTag2.arr = jarray('int', [Code05_KdtLazyTag2.MAXN])
Code05_KdtLazyTag2.treeSiz = jcast('int', 0)
Code05_KdtLazyTag2.first = jcast('int', 0)
Code05_KdtLazyTag2.last = jcast('int', 0)

if __name__ == '__main__':
    Code05_KdtLazyTag2.main([])
