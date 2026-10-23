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

# 四维偏序最长链，Python版
# 一共n个点，每个点有四维坐标(a, b, c, d)
# 可以任意选择点的排列顺序，每个点最多使用一次
# 点x的后面可以放置点y的条件为，x每个维度的坐标值 <= y对应维度的坐标值
# 希望选择的点尽量多，打印最多能选择几个点
# 1 <= n <= 5 * 10^4
# -10^9 <= 坐标值 <= +10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3769
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_4DPartialOrder1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'abcd': 'abcd', 'bi': 'bi', 'ranking': 'ranking', 'c': 'c', 'd': 'd', 'cntkdt': 'cntkdt', 'rootkdt': 'rootkdt', 'ls': 'ls', 'rs': 'rs', 'siz': 'siz', 'cmin': 'cmin', 'cmax': 'cmax', 'dmin': 'dmin', 'dmax': 'dmax', 'dp': 'dp', 'maxdp': 'maxdp', 'ALPHA': 'ALPHA', 'top': 'top', 'topFather': 'topFather', 'topSide': 'topSide', 'topDimension': 'topDimension', 'arr': 'arr', 'treeSiz': 'treeSiz', 'first': 'first', 'last': 'last', 'queryAns': 'queryAns'}
    MAXN = 0
    MAXT = 0
    INF = 0
    n = 0
    abcd = None
    # b值、点的编号
    bi = None
    # (b值，点编号)的排名
    ranking = None
    # K-D树维护c、d坐标
    c = None
    d = None
    cntkdt = 0
    # 每个树状数组的下标，背后是一棵动态kdt
    rootkdt = None
    ls = None
    rs = None
    siz = None
    cmin = None
    cmax = None
    dmin = None
    dmax = None
    # 单点结尾时的最长偏序链的长度
    dp = None
    # 区域的最大dp值
    maxdp = None
    ALPHA = 0.0
    top = 0
    topFather = 0
    topSide = 0
    topDimension = 0
    arr = None
    treeSiz = 0
    @staticmethod
    def init(qc, qd, qv):
        qc = jcast('int', qc)
        qd = jcast('int', qd)
        qv = jcast('int', qv)
        Code03_4DPartialOrder1.cntkdt = jcast('int', (Code03_4DPartialOrder1.cntkdt + 1))
        Code03_4DPartialOrder1.c[Code03_4DPartialOrder1.cntkdt] = jcast('int', qc)
        Code03_4DPartialOrder1.d[Code03_4DPartialOrder1.cntkdt] = jcast('int', qd)
        jset(Code03_4DPartialOrder1.ls, Code03_4DPartialOrder1.cntkdt, jset(Code03_4DPartialOrder1.rs, Code03_4DPartialOrder1.cntkdt, 0))
        Code03_4DPartialOrder1.siz[Code03_4DPartialOrder1.cntkdt] = jcast('int', 1)
        jset(Code03_4DPartialOrder1.cmin, Code03_4DPartialOrder1.cntkdt, jset(Code03_4DPartialOrder1.cmax, Code03_4DPartialOrder1.cntkdt, qc))
        jset(Code03_4DPartialOrder1.dmin, Code03_4DPartialOrder1.cntkdt, jset(Code03_4DPartialOrder1.dmax, Code03_4DPartialOrder1.cntkdt, qd))
        jset(Code03_4DPartialOrder1.dp, Code03_4DPartialOrder1.cntkdt, jset(Code03_4DPartialOrder1.maxdp, Code03_4DPartialOrder1.cntkdt, qv))
        return jcast('int', Code03_4DPartialOrder1.cntkdt)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        Code03_4DPartialOrder1.siz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(1, Code03_4DPartialOrder1.siz[Code03_4DPartialOrder1.ls[i]])), Code03_4DPartialOrder1.siz[Code03_4DPartialOrder1.rs[i]])))
        jset(Code03_4DPartialOrder1.cmin, i, jstatic('Math', 'min', Code03_4DPartialOrder1.c[i], jstatic('Math', 'min', Code03_4DPartialOrder1.cmin[Code03_4DPartialOrder1.ls[i]], Code03_4DPartialOrder1.cmin[Code03_4DPartialOrder1.rs[i]])))
        jset(Code03_4DPartialOrder1.cmax, i, jstatic('Math', 'max', Code03_4DPartialOrder1.c[i], jstatic('Math', 'max', Code03_4DPartialOrder1.cmax[Code03_4DPartialOrder1.ls[i]], Code03_4DPartialOrder1.cmax[Code03_4DPartialOrder1.rs[i]])))
        jset(Code03_4DPartialOrder1.dmin, i, jstatic('Math', 'min', Code03_4DPartialOrder1.d[i], jstatic('Math', 'min', Code03_4DPartialOrder1.dmin[Code03_4DPartialOrder1.ls[i]], Code03_4DPartialOrder1.dmin[Code03_4DPartialOrder1.rs[i]])))
        jset(Code03_4DPartialOrder1.dmax, i, jstatic('Math', 'max', Code03_4DPartialOrder1.d[i], jstatic('Math', 'max', Code03_4DPartialOrder1.dmax[Code03_4DPartialOrder1.ls[i]], Code03_4DPartialOrder1.dmax[Code03_4DPartialOrder1.rs[i]])))
        jset(Code03_4DPartialOrder1.maxdp, i, jstatic('Math', 'max', Code03_4DPartialOrder1.dp[i], jstatic('Math', 'max', Code03_4DPartialOrder1.maxdp[Code03_4DPartialOrder1.ls[i]], Code03_4DPartialOrder1.maxdp[Code03_4DPartialOrder1.rs[i]])))

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('int', (Code03_4DPartialOrder1.c[i] if (dimension == 0) else Code03_4DPartialOrder1.d[i]))
        v2 = jcast('int', (Code03_4DPartialOrder1.c[j] if (dimension == 0) else Code03_4DPartialOrder1.d[j]))
        return jcast('int', (0 if (v1 == v2) else (jcast('int', (-1)) if (v1 < v2) else 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code03_4DPartialOrder1.arr[i])
        Code03_4DPartialOrder1.arr[i] = jcast('int', Code03_4DPartialOrder1.arr[j])
        Code03_4DPartialOrder1.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code03_4DPartialOrder1.first = jcast('int', l)
        Code03_4DPartialOrder1.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code03_4DPartialOrder1.last):
            cmp = jcast('int', Code03_4DPartialOrder1.compareNode(Code03_4DPartialOrder1.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code03_4DPartialOrder1.swap(((_java_obj_1 := Code03_4DPartialOrder1), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code03_4DPartialOrder1.swap(i, ((_java_obj_5 := Code03_4DPartialOrder1), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, i, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code03_4DPartialOrder1.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code03_4DPartialOrder1.partition(l, r, pidx, dimension)
                if (i < Code03_4DPartialOrder1.first):
                    r = jcast('int', jcast('int', (Code03_4DPartialOrder1.first - 1)))
                else:
                    if (i > Code03_4DPartialOrder1.last):
                        l = jcast('int', jcast('int', jadd(Code03_4DPartialOrder1.last, 1)))
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
        Code03_4DPartialOrder1.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code03_4DPartialOrder1.arr[mid])
        jset(Code03_4DPartialOrder1.ls, rt, Code03_4DPartialOrder1.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code03_4DPartialOrder1.rs, rt, Code03_4DPartialOrder1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code03_4DPartialOrder1.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code03_4DPartialOrder1.ALPHA * Code03_4DPartialOrder1.siz[i]) >= jstatic('Math', 'max', Code03_4DPartialOrder1.siz[Code03_4DPartialOrder1.ls[i]], Code03_4DPartialOrder1.siz[Code03_4DPartialOrder1.rs[i]])))

    @staticmethod
    def dfs(i):
        i = jcast('int', i)
        if (i != 0):
            jset(Code03_4DPartialOrder1.arr, ((_java_obj_9 := Code03_4DPartialOrder1), (_java_key_10 := 'treeSiz'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], i)
            Code03_4DPartialOrder1.dfs(Code03_4DPartialOrder1.ls[i])
            Code03_4DPartialOrder1.dfs(Code03_4DPartialOrder1.rs[i])

    @staticmethod
    def rebuild(version):
        version = jcast('int', version)
        if (Code03_4DPartialOrder1.top != 0):
            Code03_4DPartialOrder1.treeSiz = jcast('int', 0)
            Code03_4DPartialOrder1.dfs(Code03_4DPartialOrder1.top)
            newRoot = jcast('int', Code03_4DPartialOrder1.build(1, Code03_4DPartialOrder1.treeSiz, Code03_4DPartialOrder1.topDimension))
            if (Code03_4DPartialOrder1.topFather == 0):
                Code03_4DPartialOrder1.rootkdt[version] = jcast('int', newRoot)
            else:
                if (Code03_4DPartialOrder1.topSide == 1):
                    Code03_4DPartialOrder1.ls[Code03_4DPartialOrder1.topFather] = jcast('int', newRoot)
                else:
                    Code03_4DPartialOrder1.rs[Code03_4DPartialOrder1.topFather] = jcast('int', newRoot)

    @staticmethod
    def _java_addKdt_0(insertNode, u, fa, side, dimension):
        insertNode = jcast('int', insertNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if (u == 0):
            return jcast('int', insertNode)
        if (Code03_4DPartialOrder1.compareNode(insertNode, u, dimension) <= 0):
            jset(Code03_4DPartialOrder1.ls, u, Code03_4DPartialOrder1._java_addKdt_0(insertNode, Code03_4DPartialOrder1.ls[u], u, 1, jcast('int', (dimension ^ 1))))
        else:
            jset(Code03_4DPartialOrder1.rs, u, Code03_4DPartialOrder1._java_addKdt_0(insertNode, Code03_4DPartialOrder1.rs[u], u, 2, jcast('int', (dimension ^ 1))))
        Code03_4DPartialOrder1.maintain(u)
        if (not Code03_4DPartialOrder1.balance(u)):
            Code03_4DPartialOrder1.top = jcast('int', u)
            Code03_4DPartialOrder1.topFather = jcast('int', fa)
            Code03_4DPartialOrder1.topSide = jcast('int', side)
            Code03_4DPartialOrder1.topDimension = jcast('int', dimension)
        return jcast('int', u)

    @staticmethod
    def _java_addKdt_1(version, qx, qy, qv):
        version = jcast('int', version)
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        qv = jcast('int', qv)
        Code03_4DPartialOrder1.top = jcast('int', jset(Code03_4DPartialOrder1, 'topFather', jset(Code03_4DPartialOrder1, 'topSide', jset(Code03_4DPartialOrder1, 'topDimension', 0))))
        insertNode = jcast('int', Code03_4DPartialOrder1.init(qx, qy, qv))
        jset(Code03_4DPartialOrder1.rootkdt, version, Code03_4DPartialOrder1._java_addKdt_0(insertNode, Code03_4DPartialOrder1.rootkdt[version], 0, 0, 0))
        Code03_4DPartialOrder1.rebuild(version)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    # 新增一个状态，b排名为rank，二维坐标为(qc, qd)，dp值为qv
    @staticmethod
    def add(rank, qc, qd, qv):
        rank = jcast('int', rank)
        qc = jcast('int', qc)
        qd = jcast('int', qd)
        qv = jcast('int', qv)
        i = jcast('int', rank)
        while (i <= Code03_4DPartialOrder1.n):
            Code03_4DPartialOrder1._java_addKdt_1(i, qc, qd, qv)
            i = jcast('int', jcast('int', jadd(i, Code03_4DPartialOrder1.lowbit(i))))

    queryAns = 0
    # 一棵KDT中查询，c坐标 <= qc，d坐标 <= qd，最大的dp值
    @staticmethod
    def updateAns(qc, qd, i):
        qc = jcast('int', qc)
        qd = jcast('int', qd)
        i = jcast('int', i)
        if (i == 0):
            return
        if ((Code03_4DPartialOrder1.cmin[i] > qc) or (Code03_4DPartialOrder1.dmin[i] > qd)):
            return
        if (Code03_4DPartialOrder1.maxdp[i] <= Code03_4DPartialOrder1.queryAns):
            return
        if ((Code03_4DPartialOrder1.cmax[i] <= qc) and (Code03_4DPartialOrder1.dmax[i] <= qd)):
            Code03_4DPartialOrder1.queryAns = jcast('int', jstatic('Math', 'max', Code03_4DPartialOrder1.queryAns, Code03_4DPartialOrder1.maxdp[i]))
            return
        if ((Code03_4DPartialOrder1.c[i] <= qc) and (Code03_4DPartialOrder1.d[i] <= qd)):
            Code03_4DPartialOrder1.queryAns = jcast('int', jstatic('Math', 'max', Code03_4DPartialOrder1.queryAns, Code03_4DPartialOrder1.dp[i]))
        Code03_4DPartialOrder1.updateAns(qc, qd, Code03_4DPartialOrder1.ls[i])
        Code03_4DPartialOrder1.updateAns(qc, qd, Code03_4DPartialOrder1.rs[i])

    # 查询b排名 <= rank，c坐标 <= qc，d坐标 <= qd，最大的dp值
    @staticmethod
    def query(rank, qc, qd):
        rank = jcast('int', rank)
        qc = jcast('int', qc)
        qd = jcast('int', qd)
        Code03_4DPartialOrder1.queryAns = jcast('int', 0)
        i = jcast('int', rank)
        while (i > 0):
            Code03_4DPartialOrder1.updateAns(qc, qd, Code03_4DPartialOrder1.rootkdt[i])
            i = jcast('int', jcast('int', (i - Code03_4DPartialOrder1.lowbit(i))))
        return jcast('int', Code03_4DPartialOrder1.queryAns)

    @staticmethod
    def prepare():
        jstatic('Arrays', 'sort', Code03_4DPartialOrder1.abcd, 1, jcast('int', jadd(Code03_4DPartialOrder1.n, 1)), _java_lambda_12)
        i = jcast('int', 1)
        while (i <= Code03_4DPartialOrder1.n):
            jset(Code03_4DPartialOrder1.bi[i], 0, Code03_4DPartialOrder1.abcd[i][1])
            jset(Code03_4DPartialOrder1.bi[i], 1, i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_4DPartialOrder1.bi, 1, jcast('int', jadd(Code03_4DPartialOrder1.n, 1)), (lambda o1, o2: ((o1[0] - o2[0]) if (o1[0] != o2[0]) else (o1[1] - o2[1]))))
        i = jcast('int', 1)
        while (i <= Code03_4DPartialOrder1.n):
            jset(Code03_4DPartialOrder1.ranking, Code03_4DPartialOrder1.bi[i][1], i)
            i = jcast('int', (i + 1))
        jset(Code03_4DPartialOrder1.cmin, 0, jset(Code03_4DPartialOrder1.dmin, 0, Code03_4DPartialOrder1.INF))
        jset(Code03_4DPartialOrder1.cmax, 0, jset(Code03_4DPartialOrder1.dmax, 0, jcast('int', (-Code03_4DPartialOrder1.INF))))

    @staticmethod
    def main(args):
        in_ = Code03_4DPartialOrder1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_4DPartialOrder1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_4DPartialOrder1.n):
            jset(Code03_4DPartialOrder1.abcd[i], 0, jcall(in_, 'nextInt'))
            jset(Code03_4DPartialOrder1.abcd[i], 1, jcall(in_, 'nextInt'))
            jset(Code03_4DPartialOrder1.abcd[i], 2, jcall(in_, 'nextInt'))
            jset(Code03_4DPartialOrder1.abcd[i], 3, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_4DPartialOrder1.prepare()
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_4DPartialOrder1.n):
            cur = jcast('int', jcast('int', jadd(Code03_4DPartialOrder1.query(Code03_4DPartialOrder1.ranking[i], Code03_4DPartialOrder1.abcd[i][2], Code03_4DPartialOrder1.abcd[i][3]), 1)))
            ans = jcast('int', jstatic('Math', 'max', ans, cur))
            Code03_4DPartialOrder1.add(Code03_4DPartialOrder1.ranking[i], Code03_4DPartialOrder1.abcd[i][2], Code03_4DPartialOrder1.abcd[i][3], cur)
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

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
            raise TypeError("No matching overload for Code03_4DPartialOrder1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def addKdt(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code03_4DPartialOrder1._java_addKdt_0(*args)
        if _java_choice == 1:
            return Code03_4DPartialOrder1._java_addKdt_1(*args)
        raise TypeError("No matching overload for Code03_4DPartialOrder1.addKdt")


def _java_lambda_12(o1, o2):
    i = jcast('int', 0)
    while (i < 4):
        if (o1[i] != o2[i]):
            return (o1[i] - o2[i])
        i = jcast('int', (i + 1))
    return 0

Code03_4DPartialOrder1.MAXN = jcast('int', 50001)
Code03_4DPartialOrder1.MAXT = jcast('int', 500001)
Code03_4DPartialOrder1.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code03_4DPartialOrder1.n = jcast('int', 0)
Code03_4DPartialOrder1.abcd = jarray('int', [Code03_4DPartialOrder1.MAXN, 4])
Code03_4DPartialOrder1.bi = jarray('int', [Code03_4DPartialOrder1.MAXN, 2])
Code03_4DPartialOrder1.ranking = jarray('int', [Code03_4DPartialOrder1.MAXN])
Code03_4DPartialOrder1.c = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.d = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.cntkdt = jcast('int', 0)
Code03_4DPartialOrder1.rootkdt = jarray('int', [Code03_4DPartialOrder1.MAXN])
Code03_4DPartialOrder1.ls = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.rs = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.siz = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.cmin = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.cmax = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.dmin = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.dmax = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.dp = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.maxdp = jarray('int', [Code03_4DPartialOrder1.MAXT])
Code03_4DPartialOrder1.ALPHA = jcast('double', 0.7)
Code03_4DPartialOrder1.top = jcast('int', 0)
Code03_4DPartialOrder1.topFather = jcast('int', 0)
Code03_4DPartialOrder1.topSide = jcast('int', 0)
Code03_4DPartialOrder1.topDimension = jcast('int', 0)
Code03_4DPartialOrder1.arr = jarray('int', [Code03_4DPartialOrder1.MAXN])
Code03_4DPartialOrder1.treeSiz = jcast('int', 0)
Code03_4DPartialOrder1.first = jcast('int', 0)
Code03_4DPartialOrder1.last = jcast('int', 0)
Code03_4DPartialOrder1.queryAns = jcast('int', 0)

if __name__ == '__main__':
    Code03_4DPartialOrder1.main([])
