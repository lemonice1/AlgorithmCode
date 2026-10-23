# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 连通图，Python版
# 一共有n个点，给定m条边，所有点一开始就连通在一起了
# 一共有k条操作，每条操作格式如下
# 操作 c ... : 操作涉及c条边，这些边的编号 ... 一共c个
# 假设删掉这些边，打印整张图是否联通
# 每条操作都是独立的，相互之间没有任何关系
# 1 <= n、k <= 10^5
# 1 <= m <= 2 * 10^5
# 1 <= c <= 4
# 测试链接 : https://www.luogu.com.cn/problem/P5227
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_ConnectedGraph2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXE': 'MAXE', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'k': 'k', 'u': 'u', 'v': 'v', 'event': 'event', 'ecnt': 'ecnt', 'visit': 'visit', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'head': 'head', 'next': 'next', 'tox': 'tox', 'toy': 'toy', 'cnt': 'cnt', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    MAXE = 0
    MAXT = 0
    n = 0
    m = 0
    k = 0
    u = None
    v = None
    event = None
    ecnt = 0
    visit = None
    father = None
    siz = None
    rollback = None
    opsize = 0
    head = None
    next = None
    tox = None
    toy = None
    cnt = 0
    ans = None
    @staticmethod
    def addEdge(i, x, y):
        i = jcast('int', i)
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code06_ConnectedGraph2.next, ((_java_obj_1 := Code06_ConnectedGraph2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_ConnectedGraph2.head[i])
        Code06_ConnectedGraph2.tox[Code06_ConnectedGraph2.cnt] = jcast('int', x)
        Code06_ConnectedGraph2.toy[Code06_ConnectedGraph2.cnt] = jcast('int', y)
        Code06_ConnectedGraph2.head[i] = jcast('int', Code06_ConnectedGraph2.cnt)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code06_ConnectedGraph2.father[i]):
            i = jcast('int', Code06_ConnectedGraph2.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code06_ConnectedGraph2.find(x))
        fy = jcast('int', Code06_ConnectedGraph2.find(y))
        if (Code06_ConnectedGraph2.siz[fx] < Code06_ConnectedGraph2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code06_ConnectedGraph2.father[fy] = jcast('int', fx)
        Code06_ConnectedGraph2.siz[fx] = jcast('int', jcast('int', jadd(Code06_ConnectedGraph2.siz[fx], Code06_ConnectedGraph2.siz[fy])))
        jset(Code06_ConnectedGraph2.rollback[((_java_obj_4 := Code06_ConnectedGraph2), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, fx)
        jset(Code06_ConnectedGraph2.rollback[Code06_ConnectedGraph2.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code06_ConnectedGraph2.rollback[Code06_ConnectedGraph2.opsize][0])
        fy = jcast('int', Code06_ConnectedGraph2.rollback[((_java_obj_7 := Code06_ConnectedGraph2), (_java_key_8 := 'opsize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]][1])
        Code06_ConnectedGraph2.father[fy] = jcast('int', fy)
        Code06_ConnectedGraph2.siz[fx] = jcast('int', jcast('int', (Code06_ConnectedGraph2.siz[fx] - Code06_ConnectedGraph2.siz[fy])))

    @staticmethod
    def add(jobl, jobr, jobx, joby, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        joby = jcast('int', joby)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_ConnectedGraph2.addEdge(i, jobx, joby)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code06_ConnectedGraph2.add(jobl, jobr, jobx, joby, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_ConnectedGraph2.add(jobl, jobr, jobx, joby, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        check = jcast('boolean', False)
        unionCnt = jcast('int', 0)
        ei = jcast('int', Code06_ConnectedGraph2.head[i])
        while (ei > 0):
            try:
                x = jcast('int', Code06_ConnectedGraph2.tox[ei])
                y = jcast('int', Code06_ConnectedGraph2.toy[ei])
                fx = jcast('int', Code06_ConnectedGraph2.find(x))
                fy = jcast('int', Code06_ConnectedGraph2.find(y))
                if (fx != fy):
                    Code06_ConnectedGraph2.union(fx, fy)
                    unionCnt = jcast('int', (unionCnt + 1))
                if (Code06_ConnectedGraph2.siz[Code06_ConnectedGraph2.find(fx)] == Code06_ConnectedGraph2.n):
                    check = jcast('boolean', True)
                    raise JBreak(None)
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            ei = jcast('int', Code06_ConnectedGraph2.next[ei])
        if check:
            j = jcast('int', l)
            while (j <= r):
                Code06_ConnectedGraph2.ans[j] = jcast('boolean', True)
                j = jcast('int', (j + 1))
        else:
            if (l == r):
                Code06_ConnectedGraph2.ans[l] = jcast('boolean', False)
            else:
                mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
                Code06_ConnectedGraph2.dfs(l, mid, jcast('int', (i << (1 & 31))))
                Code06_ConnectedGraph2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        j = jcast('int', 1)
        while (j <= unionCnt):
            Code06_ConnectedGraph2.undo()
            j = jcast('int', (j + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code06_ConnectedGraph2.n):
            Code06_ConnectedGraph2.father[i] = jcast('int', i)
            Code06_ConnectedGraph2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_ConnectedGraph2.event, 1, jcast('int', jadd(Code06_ConnectedGraph2.ecnt, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        eid = 0
        t = 0
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code06_ConnectedGraph2.ecnt):
            eid = jcast('int', Code06_ConnectedGraph2.event[l][0])
            Code06_ConnectedGraph2.visit[eid] = jcast('boolean', True)
            while ((jcast('int', jadd(r, 1)) <= Code06_ConnectedGraph2.ecnt) and (Code06_ConnectedGraph2.event[jcast('int', jadd(r, 1))][0] == eid)):
                r = jcast('int', (r + 1))
            t = jcast('int', 1)
            i = jcast('int', l)
            while (i <= r):
                if (t <= jcast('int', (Code06_ConnectedGraph2.event[i][1] - 1))):
                    Code06_ConnectedGraph2.add(t, jcast('int', (Code06_ConnectedGraph2.event[i][1] - 1)), Code06_ConnectedGraph2.u[eid], Code06_ConnectedGraph2.v[eid], 1, Code06_ConnectedGraph2.k, 1)
                t = jcast('int', jcast('int', jadd(Code06_ConnectedGraph2.event[i][1], 1)))
                i = jcast('int', (i + 1))
            if (t <= Code06_ConnectedGraph2.k):
                Code06_ConnectedGraph2.add(t, Code06_ConnectedGraph2.k, Code06_ConnectedGraph2.u[eid], Code06_ConnectedGraph2.v[eid], 1, Code06_ConnectedGraph2.k, 1)
            l = jcast('int', (r := jcast('int', (r + (1)))))
        i = jcast('int', 1)
        while (i <= Code06_ConnectedGraph2.m):
            if (not Code06_ConnectedGraph2.visit[i]):
                Code06_ConnectedGraph2.add(1, Code06_ConnectedGraph2.k, Code06_ConnectedGraph2.u[i], Code06_ConnectedGraph2.v[i], 1, Code06_ConnectedGraph2.k, 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        io = Code06_ConnectedGraph2.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code06_ConnectedGraph2.n = jcast('int', jcall(io, 'nextInt'))
        Code06_ConnectedGraph2.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_ConnectedGraph2.m):
            jset(Code06_ConnectedGraph2.u, i, jcall(io, 'nextInt'))
            jset(Code06_ConnectedGraph2.v, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code06_ConnectedGraph2.k = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        c = 0
        while (i <= Code06_ConnectedGraph2.k):
            c = jcast('int', jcall(io, 'nextInt'))
            j = jcast('int', 1)
            while (j <= c):
                jset(Code06_ConnectedGraph2.event[((_java_obj_11 := Code06_ConnectedGraph2), (_java_key_12 := 'ecnt'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3]], 0, jcall(io, 'nextInt'))
                jset(Code06_ConnectedGraph2.event[Code06_ConnectedGraph2.ecnt], 1, i)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code06_ConnectedGraph2.prepare()
        Code06_ConnectedGraph2.dfs(1, Code06_ConnectedGraph2.k, 1)
        i = jcast('int', 1)
        while (i <= Code06_ConnectedGraph2.k):
            if Code06_ConnectedGraph2.ans[i]:
                jcall(io, 'write', 'Connected\n')
            else:
                jcall(io, 'write', 'Disconnected\n')
            i = jcast('int', (i + 1))
        jcall(io, 'flush')

    # 读写工具类
    class FastIO:
        __java_fields__ = {'is': 'is_', 'os': 'os', 'inbuf': 'inbuf', 'lenbuf': 'lenbuf', 'ptrbuf': 'ptrbuf', 'outBuf': 'outBuf'}
        # is_：实例字段，在构造函数中初始化。
        # os：实例字段，在构造函数中初始化。
        # inbuf：实例字段，在构造函数中初始化。
        # lenbuf：实例字段，在构造函数中初始化。
        # ptrbuf：实例字段，在构造函数中初始化。
        # outBuf：实例字段，在构造函数中初始化。
        def _java_init_0(self, is_, os):
            self.is_ = is_
            self.os = os

        def readByte(self):
            if (self.ptrbuf >= self.lenbuf):
                self.ptrbuf = jcast('int', 0)
                try:
                    self.lenbuf = jcast('int', jcall(self.is_, 'read', self.inbuf))
                except (JBreak, JContinue):
                    raise
                except Exception as _java_exception_14:
                    if jinstanceof(_java_exception_14, 'IOException'):
                        e = _java_exception_14
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_15 := self), (_java_key_16 := 'ptrbuf'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))), _java_old_17)[4]] & 255)))

        def skip(self):
            b = 0
            while ((b := self.readByte()) != jcast('int', (-1))):
                if (b > jchar(' ')):
                    return jcast('int', b)
            return jcast('int', jcast('int', (-1)))

        def nextInt(self):
            b = jcast('int', self.skip())
            if (b == jcast('int', (-1))):
                raise jnew('RuntimeException', 'No more integers (EOF)')
            negative = jcast('boolean', False)
            if (b == jchar('-')):
                negative = jcast('boolean', True)
                b = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((b >= jchar('0')) and (b <= jchar('9'))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if negative else val))

        def write(self, s):
            jcall(self.outBuf, 'append', s)

        def writeInt(self, x):
            x = jcast('int', x)
            jcall(self.outBuf, 'append', x)

        def writelnInt(self, x):
            x = jcast('int', x)
            jcall(jcall(self.outBuf, 'append', x), 'append', jchar('\n'))

        def flush(self):
            try:
                jcall(self.os, 'write', jcall(jcall(self.outBuf, 'toString'), 'getBytes'))
                jcall(self.os, 'flush')
                jcall(self.outBuf, 'setLength', 0)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_18:
                if jinstanceof(_java_exception_18, 'IOException'):
                    e = _java_exception_18
                    raise jnew('RuntimeException', e)
                else:
                    raise

        def __init__(self, *args, _java_ctor=None):
            self.is_ = None
            self.os = None
            self.inbuf = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.lenbuf = jcast('int', 0)
            self.ptrbuf = jcast('int', 0)
            self.outBuf = jnew('StringBuilder')
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream', 'OutputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_ConnectedGraph2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_ConnectedGraph2.MAXN = jcast('int', 100001)
Code06_ConnectedGraph2.MAXM = jcast('int', 200001)
Code06_ConnectedGraph2.MAXE = jcast('int', 400001)
Code06_ConnectedGraph2.MAXT = jcast('int', 10000001)
Code06_ConnectedGraph2.n = jcast('int', 0)
Code06_ConnectedGraph2.m = jcast('int', 0)
Code06_ConnectedGraph2.k = jcast('int', 0)
Code06_ConnectedGraph2.u = jarray('int', [Code06_ConnectedGraph2.MAXM])
Code06_ConnectedGraph2.v = jarray('int', [Code06_ConnectedGraph2.MAXM])
Code06_ConnectedGraph2.event = jarray('int', [Code06_ConnectedGraph2.MAXE, 2])
Code06_ConnectedGraph2.ecnt = jcast('int', 0)
Code06_ConnectedGraph2.visit = jarray('boolean', [Code06_ConnectedGraph2.MAXM])
Code06_ConnectedGraph2.father = jarray('int', [Code06_ConnectedGraph2.MAXN])
Code06_ConnectedGraph2.siz = jarray('int', [Code06_ConnectedGraph2.MAXN])
Code06_ConnectedGraph2.rollback = jarray('int', [Code06_ConnectedGraph2.MAXN, 2])
Code06_ConnectedGraph2.opsize = jcast('int', 0)
Code06_ConnectedGraph2.head = jarray('int', [jcast('int', (Code06_ConnectedGraph2.MAXN << (2 & 31)))])
Code06_ConnectedGraph2.next = jarray('int', [Code06_ConnectedGraph2.MAXT])
Code06_ConnectedGraph2.tox = jarray('int', [Code06_ConnectedGraph2.MAXT])
Code06_ConnectedGraph2.toy = jarray('int', [Code06_ConnectedGraph2.MAXT])
Code06_ConnectedGraph2.cnt = jcast('int', 0)
Code06_ConnectedGraph2.ans = jarray('boolean', [Code06_ConnectedGraph2.MAXN])

if __name__ == '__main__':
    Code06_ConnectedGraph2.main([])
