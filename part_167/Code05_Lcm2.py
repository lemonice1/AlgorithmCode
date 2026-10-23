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

# 最小公倍数，Python版
# 有n个点组成的无向图，依次给出m条无向边，每条边都有边权，并且边权很特殊
# u v a b : u到v的边，边权 = 2的a次方 * 3的b次方
# 接下来有q条查询，每条查询的格式如下
# u v a b : 从u出发可以随意选择边到达v，打印是否存在一条路径，满足如下条件
# 路径上所有边权的最小公倍数 = 2的a次方 * 3的b次方
# 1 <= n、q <= 5 * 10^4
# 1 <= m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3247
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Lcm2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXQ': 'MAXQ', 'n': 'n', 'm': 'm', 'q': 'q', 'blen': 'blen', 'bnum': 'bnum', 'eu': 'eu', 'ev': 'ev', 'ea': 'ea', 'eb': 'eb', 'qu': 'qu', 'qv': 'qv', 'qa': 'qa', 'qb': 'qb', 'edge': 'edge', 'query': 'query', 'cur': 'cur', 'cursiz': 'cursiz', 'fa': 'fa', 'siz': 'siz', 'maxa': 'maxa', 'maxb': 'maxb', 'rollback': 'rollback', 'opsize': 'opsize', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    MAXQ = 0
    n = 0
    m = 0
    q = 0
    blen = 0
    bnum = 0
    eu = None
    ev = None
    ea = None
    eb = None
    qu = None
    qv = None
    qa = None
    qb = None
    edge = None
    query = None
    cur = None
    cursiz = 0
    fa = None
    siz = None
    maxa = None
    maxb = None
    rollback = None
    opsize = 0
    ans = None
    @staticmethod
    def sort(idx, val, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', val[idx[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))]])
        tmp = 0
        while (i <= j):
            while (val[idx[i]] < pivot):
                i = jcast('int', (i + 1))
            while (val[idx[j]] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', idx[i])
                idx[i] = jcast('int', idx[j])
                idx[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code05_Lcm2.sort(idx, val, l, j)
        Code05_Lcm2.sort(idx, val, i, r)

    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code05_Lcm2.n):
            Code05_Lcm2.fa[i] = jcast('int', i)
            Code05_Lcm2.siz[i] = jcast('int', 1)
            Code05_Lcm2.maxa[i] = jcast('int', jcast('int', (-1)))
            Code05_Lcm2.maxb[i] = jcast('int', jcast('int', (-1)))
            i = jcast('int', (i + 1))

    @staticmethod
    def find(x):
        x = jcast('int', x)
        while (x != Code05_Lcm2.fa[x]):
            x = jcast('int', Code05_Lcm2.fa[x])
        return jcast('int', x)

    @staticmethod
    def union(x, y, a, b):
        x = jcast('int', x)
        y = jcast('int', y)
        a = jcast('int', a)
        b = jcast('int', b)
        fx = jcast('int', Code05_Lcm2.find(x))
        fy = jcast('int', Code05_Lcm2.find(y))
        if (Code05_Lcm2.siz[fx] < Code05_Lcm2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        jset(Code05_Lcm2.rollback[((_java_obj_1 := Code05_Lcm2), (_java_key_2 := 'opsize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, fx)
        jset(Code05_Lcm2.rollback[Code05_Lcm2.opsize], 1, fy)
        jset(Code05_Lcm2.rollback[Code05_Lcm2.opsize], 2, Code05_Lcm2.siz[fx])
        jset(Code05_Lcm2.rollback[Code05_Lcm2.opsize], 3, Code05_Lcm2.maxa[fx])
        jset(Code05_Lcm2.rollback[Code05_Lcm2.opsize], 4, Code05_Lcm2.maxb[fx])
        if (fx != fy):
            Code05_Lcm2.fa[fy] = jcast('int', fx)
            Code05_Lcm2.siz[fx] = jcast('int', jcast('int', jadd(Code05_Lcm2.siz[fx], Code05_Lcm2.siz[fy])))
        jset(Code05_Lcm2.maxa, fx, jstatic('Math', 'max', jstatic('Math', 'max', Code05_Lcm2.maxa[fx], Code05_Lcm2.maxa[fy]), a))
        jset(Code05_Lcm2.maxb, fx, jstatic('Math', 'max', jstatic('Math', 'max', Code05_Lcm2.maxb[fx], Code05_Lcm2.maxb[fy]), b))

    @staticmethod
    def undo():
        fx = 0
        fy = 0
        while (Code05_Lcm2.opsize > 0):
            fx = jcast('int', Code05_Lcm2.rollback[Code05_Lcm2.opsize][0])
            fy = jcast('int', Code05_Lcm2.rollback[Code05_Lcm2.opsize][1])
            Code05_Lcm2.fa[fy] = jcast('int', fy)
            Code05_Lcm2.siz[fx] = jcast('int', Code05_Lcm2.rollback[Code05_Lcm2.opsize][2])
            Code05_Lcm2.maxa[fx] = jcast('int', Code05_Lcm2.rollback[Code05_Lcm2.opsize][3])
            Code05_Lcm2.maxb[fx] = jcast('int', Code05_Lcm2.rollback[Code05_Lcm2.opsize][4])
            Code05_Lcm2.opsize = jcast('int', (Code05_Lcm2.opsize - 1))

    @staticmethod
    def check(x, y, a, b):
        x = jcast('int', x)
        y = jcast('int', y)
        a = jcast('int', a)
        b = jcast('int', b)
        fx = jcast('int', Code05_Lcm2.find(x))
        fy = jcast('int', Code05_Lcm2.find(y))
        return jcast('boolean', (((fx == fy) and (Code05_Lcm2.maxa[fx] == a)) and (Code05_Lcm2.maxb[fx] == b)))

    @staticmethod
    def compute(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        # 重要剪枝
        # 保证每条查询只在一个边的序列块中处理
        Code05_Lcm2.cursiz = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_Lcm2.q):
            if ((Code05_Lcm2.ea[Code05_Lcm2.edge[l]] <= Code05_Lcm2.qa[Code05_Lcm2.query[i]]) and ((jcast('int', jadd(r, 1)) > Code05_Lcm2.m) or (Code05_Lcm2.qa[Code05_Lcm2.query[i]] < Code05_Lcm2.ea[Code05_Lcm2.edge[jcast('int', jadd(r, 1))]]))):
                jset(Code05_Lcm2.cur, ((_java_obj_4 := Code05_Lcm2), (_java_key_5 := 'cursiz'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code05_Lcm2.query[i])
            i = jcast('int', (i + 1))
        if (Code05_Lcm2.cursiz > 0):
            # 重建并查集，目前没有任何连通性
            Code05_Lcm2.build()
            # 本版本直接排序，不另行实现归并过程
            Code05_Lcm2.sort(Code05_Lcm2.edge, Code05_Lcm2.eb, 1, jcast('int', (l - 1)))
            i = jcast('int', 1)
            j = jcast('int', 1)
            while (i <= Code05_Lcm2.cursiz):
                while ((j < l) and (Code05_Lcm2.eb[Code05_Lcm2.edge[j]] <= Code05_Lcm2.qb[Code05_Lcm2.cur[i]])):
                    Code05_Lcm2.union(Code05_Lcm2.eu[Code05_Lcm2.edge[j]], Code05_Lcm2.ev[Code05_Lcm2.edge[j]], Code05_Lcm2.ea[Code05_Lcm2.edge[j]], Code05_Lcm2.eb[Code05_Lcm2.edge[j]])
                    j = jcast('int', (j + 1))
                Code05_Lcm2.opsize = jcast('int', 0)
                k = jcast('int', l)
                while (k <= r):
                    if ((Code05_Lcm2.ea[Code05_Lcm2.edge[k]] <= Code05_Lcm2.qa[Code05_Lcm2.cur[i]]) and (Code05_Lcm2.eb[Code05_Lcm2.edge[k]] <= Code05_Lcm2.qb[Code05_Lcm2.cur[i]])):
                        Code05_Lcm2.union(Code05_Lcm2.eu[Code05_Lcm2.edge[k]], Code05_Lcm2.ev[Code05_Lcm2.edge[k]], Code05_Lcm2.ea[Code05_Lcm2.edge[k]], Code05_Lcm2.eb[Code05_Lcm2.edge[k]])
                    k = jcast('int', (k + 1))
                jset(Code05_Lcm2.ans, Code05_Lcm2.cur[i], Code05_Lcm2.check(Code05_Lcm2.qu[Code05_Lcm2.cur[i]], Code05_Lcm2.qv[Code05_Lcm2.cur[i]], Code05_Lcm2.qa[Code05_Lcm2.cur[i]], Code05_Lcm2.qb[Code05_Lcm2.cur[i]]))
                Code05_Lcm2.undo()
                i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        log2n = jcast('int', 0)
        while (jcast('int', (1 << (log2n & 31))) <= jcast('int', (Code05_Lcm2.n >> (1 & 31)))):
            log2n = jcast('int', (log2n + 1))
        Code05_Lcm2.blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jstatic('Math', 'sqrt', jcast('int', (Code05_Lcm2.m * log2n))))))
        Code05_Lcm2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code05_Lcm2.m, Code05_Lcm2.blen)) - 1)), Code05_Lcm2.blen)))
        Code05_Lcm2.sort(Code05_Lcm2.edge, Code05_Lcm2.ea, 1, Code05_Lcm2.m)
        Code05_Lcm2.sort(Code05_Lcm2.query, Code05_Lcm2.qb, 1, Code05_Lcm2.q)

    @staticmethod
    def main(args):
        in_ = Code05_Lcm2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Lcm2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Lcm2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Lcm2.m):
            jset(Code05_Lcm2.eu, i, jcall(in_, 'nextInt'))
            jset(Code05_Lcm2.ev, i, jcall(in_, 'nextInt'))
            jset(Code05_Lcm2.ea, i, jcall(in_, 'nextInt'))
            jset(Code05_Lcm2.eb, i, jcall(in_, 'nextInt'))
            Code05_Lcm2.edge[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code05_Lcm2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Lcm2.q):
            jset(Code05_Lcm2.qu, i, jcall(in_, 'nextInt'))
            jset(Code05_Lcm2.qv, i, jcall(in_, 'nextInt'))
            jset(Code05_Lcm2.qa, i, jcall(in_, 'nextInt'))
            jset(Code05_Lcm2.qb, i, jcall(in_, 'nextInt'))
            Code05_Lcm2.query[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code05_Lcm2.prepare()
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= Code05_Lcm2.bnum):
            l = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code05_Lcm2.blen)), 1)))
            r = jcast('int', jstatic('Math', 'min', jcast('int', (i * Code05_Lcm2.blen)), Code05_Lcm2.m))
            Code05_Lcm2.compute(l, r)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Lcm2.q):
            jcall(out, 'println', ('Yes' if Code05_Lcm2.ans[i] else 'No'))
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_Lcm2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Lcm2.MAXN = jcast('int', 50001)
Code05_Lcm2.MAXM = jcast('int', 100001)
Code05_Lcm2.MAXQ = jcast('int', 50001)
Code05_Lcm2.n = jcast('int', 0)
Code05_Lcm2.m = jcast('int', 0)
Code05_Lcm2.q = jcast('int', 0)
Code05_Lcm2.blen = jcast('int', 0)
Code05_Lcm2.bnum = jcast('int', 0)
Code05_Lcm2.eu = jarray('int', [Code05_Lcm2.MAXM])
Code05_Lcm2.ev = jarray('int', [Code05_Lcm2.MAXM])
Code05_Lcm2.ea = jarray('int', [Code05_Lcm2.MAXM])
Code05_Lcm2.eb = jarray('int', [Code05_Lcm2.MAXM])
Code05_Lcm2.qu = jarray('int', [Code05_Lcm2.MAXQ])
Code05_Lcm2.qv = jarray('int', [Code05_Lcm2.MAXQ])
Code05_Lcm2.qa = jarray('int', [Code05_Lcm2.MAXQ])
Code05_Lcm2.qb = jarray('int', [Code05_Lcm2.MAXQ])
Code05_Lcm2.edge = jarray('int', [Code05_Lcm2.MAXM])
Code05_Lcm2.query = jarray('int', [Code05_Lcm2.MAXQ])
Code05_Lcm2.cur = jarray('int', [Code05_Lcm2.MAXQ])
Code05_Lcm2.cursiz = jcast('int', 0)
Code05_Lcm2.fa = jarray('int', [Code05_Lcm2.MAXN])
Code05_Lcm2.siz = jarray('int', [Code05_Lcm2.MAXN])
Code05_Lcm2.maxa = jarray('int', [Code05_Lcm2.MAXN])
Code05_Lcm2.maxb = jarray('int', [Code05_Lcm2.MAXN])
Code05_Lcm2.rollback = jarray('int', [Code05_Lcm2.MAXN, 5])
Code05_Lcm2.opsize = jcast('int', 0)
Code05_Lcm2.ans = jarray('boolean', [Code05_Lcm2.MAXQ])

if __name__ == '__main__':
    Code05_Lcm2.main([])
