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

# 异或最短路，Python版
# 一共有n个节点，m条边，每条边有边权
# 接下来有q条操作，每种操作是如下三种类型中的一种
# 操作 1 x y d : 原图中加入，点x到点y，权值为d的边
# 操作 2 x y   : 原图中删除，点x到点y的边
# 操作 3 x y   : 点x到点y，所有路随便走，沿途边权都异或起来，打印能取得的异或最小值
# 保证x < y，并且任意操作后，图连通、无重边、无自环，所有操作均合法
# 1 <= n、m、q <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF938G
# 测试链接 : https://codeforces.com/problemset/problem/938/G
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_ShortestPathQueries1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'BIT': 'BIT', 'n': 'n', 'm': 'm', 'q': 'q', 'event': 'event', 'eventCnt': 'eventCnt', 'op': 'op', 'x': 'x', 'y': 'y', 'd': 'd', 'basis': 'basis', 'inspos': 'inspos', 'basiz': 'basiz', 'father': 'father', 'siz': 'siz', 'eor': 'eor', 'rollback': 'rollback', 'opsize': 'opsize', 'head': 'head', 'next': 'next', 'tox': 'tox', 'toy': 'toy', 'tow': 'tow', 'cnt': 'cnt', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    BIT = 0
    n = 0
    m = 0
    q = 0
    # 端点x、端点y、时间点t、边权w
    event = None
    eventCnt = 0
    # 操作记录下来
    op = None
    x = None
    y = None
    d = None
    # 可撤销线性基
    basis = None
    inspos = None
    basiz = 0
    # 带权并查集 + 可撤销并查集
    father = None
    siz = None
    eor = None
    rollback = None
    opsize = 0
    # 时间轴线段树上的区间任务列表
    head = None
    next = None
    tox = None
    toy = None
    tow = None
    cnt = 0
    # 查询操作的答案
    ans = None
    # num插入线性基
    @staticmethod
    def insert(num):
        num = jcast('int', num)
        i = jcast('int', Code04_ShortestPathQueries1.BIT)
        while (i >= 0):
            if (jcast('int', (num >> (i & 31))) == 1):
                if (Code04_ShortestPathQueries1.basis[i] == 0):
                    Code04_ShortestPathQueries1.basis[i] = jcast('int', num)
                    jset(Code04_ShortestPathQueries1.inspos, ((_java_obj_1 := Code04_ShortestPathQueries1), (_java_key_2 := 'basiz'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], i)
                    return
                num = jcast('int', jcast('int', (num ^ Code04_ShortestPathQueries1.basis[i])))
            i = jcast('int', (i - 1))

    # num结合线性基，能得到的最小异或值返回
    @staticmethod
    def minEor(num):
        num = jcast('int', num)
        i = jcast('int', Code04_ShortestPathQueries1.BIT)
        while (i >= 0):
            num = jcast('int', jstatic('Math', 'min', num, jcast('int', (num ^ Code04_ShortestPathQueries1.basis[i]))))
            i = jcast('int', (i - 1))
        return jcast('int', num)

    # 线性基的撤销，让空间大小回到之前的规模
    @staticmethod
    def cancel(oldsiz):
        oldsiz = jcast('int', oldsiz)
        while (Code04_ShortestPathQueries1.basiz > oldsiz):
            jset(Code04_ShortestPathQueries1.basis, Code04_ShortestPathQueries1.inspos[((_java_obj_4 := Code04_ShortestPathQueries1), (_java_key_5 := 'basiz'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3]], 0)

    # 可撤销并查集找集合代表点
    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code04_ShortestPathQueries1.father[i]):
            i = jcast('int', Code04_ShortestPathQueries1.father[i])
        return jcast('int', i)

    # 返回i到集合代表点的异或和
    @staticmethod
    def getEor(i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        while (i != Code04_ShortestPathQueries1.father[i]):
            ans = jcast('int', jcast('int', (ans ^ Code04_ShortestPathQueries1.eor[i])))
            i = jcast('int', Code04_ShortestPathQueries1.father[i])
        return jcast('int', ans)

    # 可撤销并查集的合并，增加a和b之间，权值为w的边
    # 集合合并的过程中，还要更新eor数组
    # 更新eor的方式，参考讲解156，带权并查集
    @staticmethod
    def union(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        fu = jcast('int', Code04_ShortestPathQueries1.find(u))
        fv = jcast('int', Code04_ShortestPathQueries1.find(v))
        w = jcast('int', jcast('int', (jcast('int', (Code04_ShortestPathQueries1.getEor(u) ^ Code04_ShortestPathQueries1.getEor(v))) ^ w)))
        if (fu == fv):
            Code04_ShortestPathQueries1.insert(w)
            return jcast('boolean', False)
        if (Code04_ShortestPathQueries1.siz[fu] < Code04_ShortestPathQueries1.siz[fv]):
            tmp = jcast('int', fu)
            fu = jcast('int', fv)
            fv = jcast('int', tmp)
        Code04_ShortestPathQueries1.father[fv] = jcast('int', fu)
        Code04_ShortestPathQueries1.siz[fu] = jcast('int', jcast('int', jadd(Code04_ShortestPathQueries1.siz[fu], Code04_ShortestPathQueries1.siz[fv])))
        Code04_ShortestPathQueries1.eor[fv] = jcast('int', w)
        jset(Code04_ShortestPathQueries1.rollback[((_java_obj_7 := Code04_ShortestPathQueries1), (_java_key_8 := 'opsize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]], 0, fu)
        jset(Code04_ShortestPathQueries1.rollback[Code04_ShortestPathQueries1.opsize], 1, fv)
        return jcast('boolean', True)

    # 并查集的撤销操作
    @staticmethod
    def undo():
        fx = jcast('int', Code04_ShortestPathQueries1.rollback[Code04_ShortestPathQueries1.opsize][0])
        fy = jcast('int', Code04_ShortestPathQueries1.rollback[((_java_obj_10 := Code04_ShortestPathQueries1), (_java_key_11 := 'opsize'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]][1])
        Code04_ShortestPathQueries1.father[fy] = jcast('int', fy)
        Code04_ShortestPathQueries1.eor[fy] = jcast('int', 0)
        Code04_ShortestPathQueries1.siz[fx] = jcast('int', jcast('int', (Code04_ShortestPathQueries1.siz[fx] - Code04_ShortestPathQueries1.siz[fy])))

    # 给某个线段树区间增加任务，点x到点y之间，增加权值为w的边
    @staticmethod
    def addEdge(i, x, y, w):
        i = jcast('int', i)
        x = jcast('int', x)
        y = jcast('int', y)
        w = jcast('int', w)
        jset(Code04_ShortestPathQueries1.next, ((_java_obj_13 := Code04_ShortestPathQueries1), (_java_key_14 := 'cnt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code04_ShortestPathQueries1.head[i])
        Code04_ShortestPathQueries1.tox[Code04_ShortestPathQueries1.cnt] = jcast('int', x)
        Code04_ShortestPathQueries1.toy[Code04_ShortestPathQueries1.cnt] = jcast('int', y)
        Code04_ShortestPathQueries1.tow[Code04_ShortestPathQueries1.cnt] = jcast('int', w)
        Code04_ShortestPathQueries1.head[i] = jcast('int', Code04_ShortestPathQueries1.cnt)

    @staticmethod
    def add(jobl, jobr, jobx, joby, jobw, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        joby = jcast('int', joby)
        jobw = jcast('int', jobw)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code04_ShortestPathQueries1.addEdge(i, jobx, joby, jobw)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code04_ShortestPathQueries1.add(jobl, jobr, jobx, joby, jobw, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_ShortestPathQueries1.add(jobl, jobr, jobx, joby, jobw, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        oldsiz = jcast('int', Code04_ShortestPathQueries1.basiz)
        unionCnt = jcast('int', 0)
        e = jcast('int', Code04_ShortestPathQueries1.head[i])
        while (e > 0):
            if Code04_ShortestPathQueries1.union(Code04_ShortestPathQueries1.tox[e], Code04_ShortestPathQueries1.toy[e], Code04_ShortestPathQueries1.tow[e]):
                unionCnt = jcast('int', (unionCnt + 1))
            e = jcast('int', Code04_ShortestPathQueries1.next[e])
        if (l == r):
            if (Code04_ShortestPathQueries1.op[l] == 3):
                jset(Code04_ShortestPathQueries1.ans, l, Code04_ShortestPathQueries1.minEor(jcast('int', (Code04_ShortestPathQueries1.getEor(Code04_ShortestPathQueries1.x[l]) ^ Code04_ShortestPathQueries1.getEor(Code04_ShortestPathQueries1.y[l])))))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_ShortestPathQueries1.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code04_ShortestPathQueries1.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code04_ShortestPathQueries1.cancel(oldsiz)
        k = jcast('int', 1)
        while (k <= unionCnt):
            Code04_ShortestPathQueries1.undo()
            k = jcast('int', (k + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code04_ShortestPathQueries1.n):
            Code04_ShortestPathQueries1.father[i] = jcast('int', i)
            Code04_ShortestPathQueries1.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_ShortestPathQueries1.event, 1, jcast('int', jadd(Code04_ShortestPathQueries1.eventCnt, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else ((a[1] - b[1]) if (a[1] != b[1]) else (a[2] - b[2])))))
        x = 0
        y = 0
        start = 0
        end = 0
        d = 0
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code04_ShortestPathQueries1.eventCnt):
            x = jcast('int', Code04_ShortestPathQueries1.event[l][0])
            y = jcast('int', Code04_ShortestPathQueries1.event[l][1])
            while (((jcast('int', jadd(r, 1)) <= Code04_ShortestPathQueries1.eventCnt) and (Code04_ShortestPathQueries1.event[jcast('int', jadd(r, 1))][0] == x)) and (Code04_ShortestPathQueries1.event[jcast('int', jadd(r, 1))][1] == y)):
                r = jcast('int', (r + 1))
            i = jcast('int', l)
            while (i <= r):
                start = jcast('int', Code04_ShortestPathQueries1.event[i][2])
                end = jcast('int', (jcast('int', (Code04_ShortestPathQueries1.event[jcast('int', jadd(i, 1))][2] - 1)) if (jcast('int', jadd(i, 1)) <= r) else Code04_ShortestPathQueries1.q))
                d = jcast('int', Code04_ShortestPathQueries1.event[i][3])
                Code04_ShortestPathQueries1.add(start, end, x, y, d, 0, Code04_ShortestPathQueries1.q, 1)
                i = jcast('int', jcast('int', jadd(i, 2)))
            l = jcast('int', (r := jcast('int', (r + (1)))))

    @staticmethod
    def main(args):
        in_ = Code04_ShortestPathQueries1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_ShortestPathQueries1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_ShortestPathQueries1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_ShortestPathQueries1.m):
            jset(Code04_ShortestPathQueries1.event[i], 0, jcall(in_, 'nextInt'))
            jset(Code04_ShortestPathQueries1.event[i], 1, jcall(in_, 'nextInt'))
            jset(Code04_ShortestPathQueries1.event[i], 2, 0)
            jset(Code04_ShortestPathQueries1.event[i], 3, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code04_ShortestPathQueries1.eventCnt = jcast('int', Code04_ShortestPathQueries1.m)
        Code04_ShortestPathQueries1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_ShortestPathQueries1.q):
            jset(Code04_ShortestPathQueries1.op, i, jcall(in_, 'nextInt'))
            jset(Code04_ShortestPathQueries1.x, i, jcall(in_, 'nextInt'))
            jset(Code04_ShortestPathQueries1.y, i, jcall(in_, 'nextInt'))
            if (Code04_ShortestPathQueries1.op[i] == 1):
                jset(Code04_ShortestPathQueries1.d, i, jcall(in_, 'nextInt'))
            if (Code04_ShortestPathQueries1.op[i] != 3):
                jset(Code04_ShortestPathQueries1.event[((_java_obj_16 := Code04_ShortestPathQueries1), (_java_key_17 := 'eventCnt'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]], 0, Code04_ShortestPathQueries1.x[i])
                jset(Code04_ShortestPathQueries1.event[Code04_ShortestPathQueries1.eventCnt], 1, Code04_ShortestPathQueries1.y[i])
                jset(Code04_ShortestPathQueries1.event[Code04_ShortestPathQueries1.eventCnt], 2, i)
                jset(Code04_ShortestPathQueries1.event[Code04_ShortestPathQueries1.eventCnt], 3, Code04_ShortestPathQueries1.d[i])
            i = jcast('int', (i + 1))
        Code04_ShortestPathQueries1.prepare()
        Code04_ShortestPathQueries1.dfs(0, Code04_ShortestPathQueries1.q, 1)
        i = jcast('int', 1)
        while (i <= Code04_ShortestPathQueries1.q):
            if (Code04_ShortestPathQueries1.op[i] == 3):
                jcall(out, 'println', Code04_ShortestPathQueries1.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_19 := self), (_java_key_20 := 'ptr'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_ShortestPathQueries1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_ShortestPathQueries1.MAXN = jcast('int', 200001)
Code04_ShortestPathQueries1.MAXT = jcast('int', 5000001)
Code04_ShortestPathQueries1.BIT = jcast('int', 29)
Code04_ShortestPathQueries1.n = jcast('int', 0)
Code04_ShortestPathQueries1.m = jcast('int', 0)
Code04_ShortestPathQueries1.q = jcast('int', 0)
Code04_ShortestPathQueries1.event = jarray('int', [jcast('int', (Code04_ShortestPathQueries1.MAXN << (1 & 31))), 4])
Code04_ShortestPathQueries1.eventCnt = jcast('int', 0)
Code04_ShortestPathQueries1.op = jarray('int', [Code04_ShortestPathQueries1.MAXN])
Code04_ShortestPathQueries1.x = jarray('int', [Code04_ShortestPathQueries1.MAXN])
Code04_ShortestPathQueries1.y = jarray('int', [Code04_ShortestPathQueries1.MAXN])
Code04_ShortestPathQueries1.d = jarray('int', [Code04_ShortestPathQueries1.MAXN])
Code04_ShortestPathQueries1.basis = jarray('int', [jcast('int', jadd(Code04_ShortestPathQueries1.BIT, 1))])
Code04_ShortestPathQueries1.inspos = jarray('int', [jcast('int', jadd(Code04_ShortestPathQueries1.BIT, 1))])
Code04_ShortestPathQueries1.basiz = jcast('int', 0)
Code04_ShortestPathQueries1.father = jarray('int', [Code04_ShortestPathQueries1.MAXN])
Code04_ShortestPathQueries1.siz = jarray('int', [Code04_ShortestPathQueries1.MAXN])
Code04_ShortestPathQueries1.eor = jarray('int', [Code04_ShortestPathQueries1.MAXN])
Code04_ShortestPathQueries1.rollback = jarray('int', [Code04_ShortestPathQueries1.MAXN, 2])
Code04_ShortestPathQueries1.opsize = jcast('int', 0)
Code04_ShortestPathQueries1.head = jarray('int', [jcast('int', (Code04_ShortestPathQueries1.MAXN << (2 & 31)))])
Code04_ShortestPathQueries1.next = jarray('int', [Code04_ShortestPathQueries1.MAXT])
Code04_ShortestPathQueries1.tox = jarray('int', [Code04_ShortestPathQueries1.MAXT])
Code04_ShortestPathQueries1.toy = jarray('int', [Code04_ShortestPathQueries1.MAXT])
Code04_ShortestPathQueries1.tow = jarray('int', [Code04_ShortestPathQueries1.MAXT])
Code04_ShortestPathQueries1.cnt = jcast('int', 0)
Code04_ShortestPathQueries1.ans = jarray('int', [Code04_ShortestPathQueries1.MAXN])

if __name__ == '__main__':
    Code04_ShortestPathQueries1.main([])
