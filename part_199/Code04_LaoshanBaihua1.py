# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 崂山白花蛇草水，Python版
# 网格空间n * n，一共有q条操作，类型如下
# 操作 1 a b v     : 坐标(a, b)，增加一个点，点权为v
# 操作 2 a b c d k : 查询(a, b)为左下角，(c, d)为右上角的矩形中，第k大的点权
# 如果点不够k个，打印 NAIVE!ORZzyz.
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 1 <= n <= 5 * 10^5
# 1 <= q <= 10^5
# 1 <= v <= 10^9
# 本题推荐loj的测试，洛谷的测试让该题变成了卡常竞赛，实在没必要
# 测试链接 : https://loj.ac/p/6016
# 测试链接 : https://www.luogu.com.cn/problem/P4848
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_LaoshanBaihua1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXV': 'MAXV', 'INF': 'INF', 'n': 'n', 'q': 'q', 'cntseg': 'cntseg', 'cntkdt': 'cntkdt', 'rootseg': 'rootseg', 'lseg': 'lseg', 'rseg': 'rseg', 'rootkdt': 'rootkdt', 'x': 'x', 'y': 'y', 'ls': 'ls', 'rs': 'rs', 'siz': 'siz', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'ALPHA': 'ALPHA', 'top': 'top', 'topFather': 'topFather', 'topSide': 'topSide', 'topDimension': 'topDimension', 'arr': 'arr', 'treeSiz': 'treeSiz', 'first': 'first', 'last': 'last'}
    MAXN = 0
    MAXT = 0
    MAXV = 0
    INF = 0
    n = 0
    q = 0
    # 权值线段树节点计数
    cntseg = 0
    # K-D树的节点计数
    cntkdt = 0
    # 外层是权值线段树，开点的设计
    rootseg = 0
    lseg = None
    rseg = None
    # 每个权值线段树的节点，背后是一棵动态kdt
    rootkdt = None
    x = None
    y = None
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
        Code04_LaoshanBaihua1.cntkdt = jcast('int', (Code04_LaoshanBaihua1.cntkdt + 1))
        Code04_LaoshanBaihua1.x[Code04_LaoshanBaihua1.cntkdt] = jcast('int', qx)
        Code04_LaoshanBaihua1.y[Code04_LaoshanBaihua1.cntkdt] = jcast('int', qy)
        jset(Code04_LaoshanBaihua1.ls, Code04_LaoshanBaihua1.cntkdt, jset(Code04_LaoshanBaihua1.rs, Code04_LaoshanBaihua1.cntkdt, 0))
        Code04_LaoshanBaihua1.siz[Code04_LaoshanBaihua1.cntkdt] = jcast('int', 1)
        jset(Code04_LaoshanBaihua1.xmin, Code04_LaoshanBaihua1.cntkdt, jset(Code04_LaoshanBaihua1.xmax, Code04_LaoshanBaihua1.cntkdt, qx))
        jset(Code04_LaoshanBaihua1.ymin, Code04_LaoshanBaihua1.cntkdt, jset(Code04_LaoshanBaihua1.ymax, Code04_LaoshanBaihua1.cntkdt, qy))
        return jcast('int', Code04_LaoshanBaihua1.cntkdt)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        Code04_LaoshanBaihua1.siz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(1, Code04_LaoshanBaihua1.siz[Code04_LaoshanBaihua1.ls[i]])), Code04_LaoshanBaihua1.siz[Code04_LaoshanBaihua1.rs[i]])))
        jset(Code04_LaoshanBaihua1.xmin, i, jstatic('Math', 'min', Code04_LaoshanBaihua1.x[i], jstatic('Math', 'min', Code04_LaoshanBaihua1.xmin[Code04_LaoshanBaihua1.ls[i]], Code04_LaoshanBaihua1.xmin[Code04_LaoshanBaihua1.rs[i]])))
        jset(Code04_LaoshanBaihua1.xmax, i, jstatic('Math', 'max', Code04_LaoshanBaihua1.x[i], jstatic('Math', 'max', Code04_LaoshanBaihua1.xmax[Code04_LaoshanBaihua1.ls[i]], Code04_LaoshanBaihua1.xmax[Code04_LaoshanBaihua1.rs[i]])))
        jset(Code04_LaoshanBaihua1.ymin, i, jstatic('Math', 'min', Code04_LaoshanBaihua1.y[i], jstatic('Math', 'min', Code04_LaoshanBaihua1.ymin[Code04_LaoshanBaihua1.ls[i]], Code04_LaoshanBaihua1.ymin[Code04_LaoshanBaihua1.rs[i]])))
        jset(Code04_LaoshanBaihua1.ymax, i, jstatic('Math', 'max', Code04_LaoshanBaihua1.y[i], jstatic('Math', 'max', Code04_LaoshanBaihua1.ymax[Code04_LaoshanBaihua1.ls[i]], Code04_LaoshanBaihua1.ymax[Code04_LaoshanBaihua1.rs[i]])))

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('int', (Code04_LaoshanBaihua1.x[i] if (dimension == 0) else Code04_LaoshanBaihua1.y[i]))
        v2 = jcast('int', (Code04_LaoshanBaihua1.x[j] if (dimension == 0) else Code04_LaoshanBaihua1.y[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code04_LaoshanBaihua1.arr[i])
        Code04_LaoshanBaihua1.arr[i] = jcast('int', Code04_LaoshanBaihua1.arr[j])
        Code04_LaoshanBaihua1.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code04_LaoshanBaihua1.first = jcast('int', l)
        Code04_LaoshanBaihua1.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code04_LaoshanBaihua1.last):
            cmp = jcast('int', Code04_LaoshanBaihua1.compareNode(Code04_LaoshanBaihua1.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code04_LaoshanBaihua1.swap(((_java_obj_1 := Code04_LaoshanBaihua1), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code04_LaoshanBaihua1.swap(i, ((_java_obj_5 := Code04_LaoshanBaihua1), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code04_LaoshanBaihua1.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code04_LaoshanBaihua1.partition(l, r, pidx, dimension)
                if (i < Code04_LaoshanBaihua1.first):
                    r = jcast('int', jcast('int', (Code04_LaoshanBaihua1.first - 1)))
                else:
                    if (i > Code04_LaoshanBaihua1.last):
                        l = jcast('int', jcast('int', jadd(Code04_LaoshanBaihua1.last, 1)))
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
        Code04_LaoshanBaihua1.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code04_LaoshanBaihua1.arr[mid])
        jset(Code04_LaoshanBaihua1.ls, rt, Code04_LaoshanBaihua1.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code04_LaoshanBaihua1.rs, rt, Code04_LaoshanBaihua1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code04_LaoshanBaihua1.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code04_LaoshanBaihua1.ALPHA * Code04_LaoshanBaihua1.siz[i]) >= jstatic('Math', 'max', Code04_LaoshanBaihua1.siz[Code04_LaoshanBaihua1.ls[i]], Code04_LaoshanBaihua1.siz[Code04_LaoshanBaihua1.rs[i]])))

    @staticmethod
    def dfs(i):
        i = jcast('int', i)
        if (i != 0):
            jset(Code04_LaoshanBaihua1.arr, ((_java_obj_9 := Code04_LaoshanBaihua1), (_java_key_10 := 'treeSiz'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], i)
            Code04_LaoshanBaihua1.dfs(Code04_LaoshanBaihua1.ls[i])
            Code04_LaoshanBaihua1.dfs(Code04_LaoshanBaihua1.rs[i])

    @staticmethod
    def rebuild(version):
        version = jcast('int', version)
        if (Code04_LaoshanBaihua1.top != 0):
            Code04_LaoshanBaihua1.treeSiz = jcast('int', 0)
            Code04_LaoshanBaihua1.dfs(Code04_LaoshanBaihua1.top)
            newRoot = jcast('int', Code04_LaoshanBaihua1.build(1, Code04_LaoshanBaihua1.treeSiz, Code04_LaoshanBaihua1.topDimension))
            if (Code04_LaoshanBaihua1.topFather == 0):
                Code04_LaoshanBaihua1.rootkdt[version] = jcast('int', newRoot)
            else:
                if (Code04_LaoshanBaihua1.topSide == 1):
                    Code04_LaoshanBaihua1.ls[Code04_LaoshanBaihua1.topFather] = jcast('int', newRoot)
                else:
                    Code04_LaoshanBaihua1.rs[Code04_LaoshanBaihua1.topFather] = jcast('int', newRoot)

    @staticmethod
    def _java_addKdt_0(insertNode, u, fa, side, dimension):
        insertNode = jcast('int', insertNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if (u == 0):
            return jcast('int', insertNode)
        if (Code04_LaoshanBaihua1.compareNode(insertNode, u, dimension) <= 0):
            jset(Code04_LaoshanBaihua1.ls, u, Code04_LaoshanBaihua1._java_addKdt_0(insertNode, Code04_LaoshanBaihua1.ls[u], u, 1, jcast('int', (dimension ^ 1))))
        else:
            jset(Code04_LaoshanBaihua1.rs, u, Code04_LaoshanBaihua1._java_addKdt_0(insertNode, Code04_LaoshanBaihua1.rs[u], u, 2, jcast('int', (dimension ^ 1))))
        Code04_LaoshanBaihua1.maintain(u)
        if (not Code04_LaoshanBaihua1.balance(u)):
            Code04_LaoshanBaihua1.top = jcast('int', u)
            Code04_LaoshanBaihua1.topFather = jcast('int', fa)
            Code04_LaoshanBaihua1.topSide = jcast('int', side)
            Code04_LaoshanBaihua1.topDimension = jcast('int', dimension)
        return jcast('int', u)

    @staticmethod
    def _java_addKdt_1(version, qx, qy):
        version = jcast('int', version)
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        Code04_LaoshanBaihua1.top = jcast('int', jset(Code04_LaoshanBaihua1, 'topFather', jset(Code04_LaoshanBaihua1, 'topSide', jset(Code04_LaoshanBaihua1, 'topDimension', 0))))
        insertNode = jcast('int', Code04_LaoshanBaihua1.init(qx, qy))
        jset(Code04_LaoshanBaihua1.rootkdt, version, Code04_LaoshanBaihua1._java_addKdt_0(insertNode, Code04_LaoshanBaihua1.rootkdt[version], 0, 0, 0))
        Code04_LaoshanBaihua1.rebuild(version)

    # 权值线段树上增加点
    @staticmethod
    def add(qx, qy, qv, l, r, i):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        qv = jcast('int', qv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_12 := Code04_LaoshanBaihua1), (_java_key_13 := 'cntseg'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3])
        Code04_LaoshanBaihua1._java_addKdt_1(i, qx, qy)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (qv <= mid):
                jset(Code04_LaoshanBaihua1.lseg, i, Code04_LaoshanBaihua1.add(qx, qy, qv, l, mid, Code04_LaoshanBaihua1.lseg[i]))
            else:
                jset(Code04_LaoshanBaihua1.rseg, i, Code04_LaoshanBaihua1.add(qx, qy, qv, jcast('int', jadd(mid, 1)), r, Code04_LaoshanBaihua1.rseg[i]))
        return jcast('int', i)

    # 查询一棵KDT中，矩形内有多少个点
    @staticmethod
    def queryCount(a, b, c, d, i):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if ((((Code04_LaoshanBaihua1.xmax[i] < a) or (c < Code04_LaoshanBaihua1.xmin[i])) or (Code04_LaoshanBaihua1.ymax[i] < b)) or (d < Code04_LaoshanBaihua1.ymin[i])):
            return jcast('int', 0)
        if ((((a <= Code04_LaoshanBaihua1.xmin[i]) and (Code04_LaoshanBaihua1.xmax[i] <= c)) and (b <= Code04_LaoshanBaihua1.ymin[i])) and (Code04_LaoshanBaihua1.ymax[i] <= d)):
            return jcast('int', Code04_LaoshanBaihua1.siz[i])
        ans = jcast('int', 0)
        if ((((a <= Code04_LaoshanBaihua1.x[i]) and (Code04_LaoshanBaihua1.x[i] <= c)) and (b <= Code04_LaoshanBaihua1.y[i])) and (Code04_LaoshanBaihua1.y[i] <= d)):
            ans = jcast('int', 1)
        ans = jcast('int', jcast('int', jadd(ans, Code04_LaoshanBaihua1.queryCount(a, b, c, d, Code04_LaoshanBaihua1.ls[i]))))
        ans = jcast('int', jcast('int', jadd(ans, Code04_LaoshanBaihua1.queryCount(a, b, c, d, Code04_LaoshanBaihua1.rs[i]))))
        return jcast('int', ans)

    # 查询权值线段树中，矩形内第k大的点权，确定存在
    @staticmethod
    def query(a, b, c, d, k, l, r, i):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        k = jcast('int', k)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', l)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        cnt = jcast('int', Code04_LaoshanBaihua1.queryCount(a, b, c, d, Code04_LaoshanBaihua1.rootkdt[Code04_LaoshanBaihua1.rseg[i]]))
        if (cnt >= k):
            return jcast('int', Code04_LaoshanBaihua1.query(a, b, c, d, k, jcast('int', jadd(mid, 1)), r, Code04_LaoshanBaihua1.rseg[i]))
        else:
            return jcast('int', Code04_LaoshanBaihua1.query(a, b, c, d, jcast('int', (k - cnt)), l, mid, Code04_LaoshanBaihua1.lseg[i]))

    @staticmethod
    def main(args):
        in_ = Code04_LaoshanBaihua1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_LaoshanBaihua1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_LaoshanBaihua1.q = jcast('int', jcall(in_, 'nextInt'))
        jset(Code04_LaoshanBaihua1.xmin, 0, jset(Code04_LaoshanBaihua1.ymin, 0, Code04_LaoshanBaihua1.INF))
        jset(Code04_LaoshanBaihua1.xmax, 0, jset(Code04_LaoshanBaihua1.ymax, 0, jcast('int', (-Code04_LaoshanBaihua1.INF))))
        op = 0
        a = 0
        b = 0
        c = 0
        d = 0
        v = 0
        k = 0
        lastAns = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_LaoshanBaihua1.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                a = jcast('int', jcall(in_, 'nextInt'))
                b = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                a = jcast('int', jcast('int', (a ^ lastAns)))
                b = jcast('int', jcast('int', (b ^ lastAns)))
                v = jcast('int', jcast('int', (v ^ lastAns)))
                Code04_LaoshanBaihua1.rootseg = jcast('int', Code04_LaoshanBaihua1.add(a, b, v, 1, Code04_LaoshanBaihua1.MAXV, Code04_LaoshanBaihua1.rootseg))
            else:
                a = jcast('int', jcall(in_, 'nextInt'))
                b = jcast('int', jcall(in_, 'nextInt'))
                c = jcast('int', jcall(in_, 'nextInt'))
                d = jcast('int', jcall(in_, 'nextInt'))
                k = jcast('int', jcall(in_, 'nextInt'))
                a = jcast('int', jcast('int', (a ^ lastAns)))
                b = jcast('int', jcast('int', (b ^ lastAns)))
                c = jcast('int', jcast('int', (c ^ lastAns)))
                d = jcast('int', jcast('int', (d ^ lastAns)))
                k = jcast('int', jcast('int', (k ^ lastAns)))
                if (Code04_LaoshanBaihua1.queryCount(a, b, c, d, Code04_LaoshanBaihua1.rootkdt[Code04_LaoshanBaihua1.rootseg]) >= k):
                    lastAns = jcast('int', Code04_LaoshanBaihua1.query(a, b, c, d, k, 1, Code04_LaoshanBaihua1.MAXV, Code04_LaoshanBaihua1.rootseg))
                else:
                    lastAns = jcast('int', 0)
                if (lastAns == 0):
                    jcall(out, 'println', 'NAIVE!ORZzyz.')
                else:
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
            raise TypeError("No matching overload for Code04_LaoshanBaihua1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def addKdt(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code04_LaoshanBaihua1._java_addKdt_0(*args)
        if _java_choice == 1:
            return Code04_LaoshanBaihua1._java_addKdt_1(*args)
        raise TypeError("No matching overload for Code04_LaoshanBaihua1.addKdt")


Code04_LaoshanBaihua1.MAXN = jcast('int', 100001)
Code04_LaoshanBaihua1.MAXT = jcast('int', 3100001)
Code04_LaoshanBaihua1.MAXV = jcast('int', 1000000000)
Code04_LaoshanBaihua1.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code04_LaoshanBaihua1.n = jcast('int', 0)
Code04_LaoshanBaihua1.q = jcast('int', 0)
Code04_LaoshanBaihua1.cntseg = jcast('int', 0)
Code04_LaoshanBaihua1.cntkdt = jcast('int', 0)
Code04_LaoshanBaihua1.rootseg = jcast('int', 0)
Code04_LaoshanBaihua1.lseg = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.rseg = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.rootkdt = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.x = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.y = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.ls = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.rs = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.siz = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.xmin = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.xmax = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.ymin = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.ymax = jarray('int', [Code04_LaoshanBaihua1.MAXT])
Code04_LaoshanBaihua1.ALPHA = jcast('double', 0.7)
Code04_LaoshanBaihua1.top = jcast('int', 0)
Code04_LaoshanBaihua1.topFather = jcast('int', 0)
Code04_LaoshanBaihua1.topSide = jcast('int', 0)
Code04_LaoshanBaihua1.topDimension = jcast('int', 0)
Code04_LaoshanBaihua1.arr = jarray('int', [Code04_LaoshanBaihua1.MAXN])
Code04_LaoshanBaihua1.treeSiz = jcast('int', 0)
Code04_LaoshanBaihua1.first = jcast('int', 0)
Code04_LaoshanBaihua1.last = jcast('int', 0)

if __name__ == '__main__':
    Code04_LaoshanBaihua1.main([])
