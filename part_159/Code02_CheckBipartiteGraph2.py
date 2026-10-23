# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 判断二分图，Python版
# 一共有n个节点，时刻的范围0~k，一共有m条操作，每条操作含义如下
# 操作 x y l r : 点x到点y之间连一条边，该边在l时刻出现，在r时刻消失
# 分别打印1时刻以内、2时刻以内..k时刻以内，图是不是二分图
# 注意i时刻以内是0~i-1时间段的意思
# 1 <= n、k <= 10^5    1 <= m <= 2 * 10^5
# 1 <= x、y <= n       0 <= l、r <= k
# 测试链接 : https://www.luogu.com.cn/problem/P5787
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_CheckBipartiteGraph2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'k': 'k', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'head': 'head', 'next': 'next', 'tox': 'tox', 'toy': 'toy', 'cnt': 'cnt', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    k = 0
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
        jset(Code02_CheckBipartiteGraph2.next, ((_java_obj_1 := Code02_CheckBipartiteGraph2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_CheckBipartiteGraph2.head[i])
        Code02_CheckBipartiteGraph2.tox[Code02_CheckBipartiteGraph2.cnt] = jcast('int', x)
        Code02_CheckBipartiteGraph2.toy[Code02_CheckBipartiteGraph2.cnt] = jcast('int', y)
        Code02_CheckBipartiteGraph2.head[i] = jcast('int', Code02_CheckBipartiteGraph2.cnt)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code02_CheckBipartiteGraph2.father[i]):
            i = jcast('int', Code02_CheckBipartiteGraph2.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code02_CheckBipartiteGraph2.find(x))
        fy = jcast('int', Code02_CheckBipartiteGraph2.find(y))
        if (Code02_CheckBipartiteGraph2.siz[fx] < Code02_CheckBipartiteGraph2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code02_CheckBipartiteGraph2.father[fy] = jcast('int', fx)
        Code02_CheckBipartiteGraph2.siz[fx] = jcast('int', jcast('int', jadd(Code02_CheckBipartiteGraph2.siz[fx], Code02_CheckBipartiteGraph2.siz[fy])))
        jset(Code02_CheckBipartiteGraph2.rollback[((_java_obj_4 := Code02_CheckBipartiteGraph2), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, fx)
        jset(Code02_CheckBipartiteGraph2.rollback[Code02_CheckBipartiteGraph2.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code02_CheckBipartiteGraph2.rollback[Code02_CheckBipartiteGraph2.opsize][0])
        fy = jcast('int', Code02_CheckBipartiteGraph2.rollback[((_java_obj_7 := Code02_CheckBipartiteGraph2), (_java_key_8 := 'opsize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]][1])
        Code02_CheckBipartiteGraph2.father[fy] = jcast('int', fy)
        Code02_CheckBipartiteGraph2.siz[fx] = jcast('int', jcast('int', (Code02_CheckBipartiteGraph2.siz[fx] - Code02_CheckBipartiteGraph2.siz[fy])))

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
            Code02_CheckBipartiteGraph2.addEdge(i, jobx, joby)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code02_CheckBipartiteGraph2.add(jobl, jobr, jobx, joby, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code02_CheckBipartiteGraph2.add(jobl, jobr, jobx, joby, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        check = jcast('boolean', True)
        unionCnt = jcast('int', 0)
        ei = jcast('int', Code02_CheckBipartiteGraph2.head[i])
        while (ei > 0):
            try:
                x = jcast('int', Code02_CheckBipartiteGraph2.tox[ei])
                y = jcast('int', Code02_CheckBipartiteGraph2.toy[ei])
                fx = jcast('int', Code02_CheckBipartiteGraph2.find(x))
                fy = jcast('int', Code02_CheckBipartiteGraph2.find(y))
                if (fx == fy):
                    check = jcast('boolean', False)
                    raise JBreak(None)
                else:
                    Code02_CheckBipartiteGraph2.union(x, jcast('int', jadd(y, Code02_CheckBipartiteGraph2.n)))
                    Code02_CheckBipartiteGraph2.union(y, jcast('int', jadd(x, Code02_CheckBipartiteGraph2.n)))
                    unionCnt = jcast('int', jcast('int', jadd(unionCnt, 2)))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            ei = jcast('int', Code02_CheckBipartiteGraph2.next[ei])
        if check:
            if (l == r):
                Code02_CheckBipartiteGraph2.ans[l] = jcast('boolean', True)
            else:
                mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
                Code02_CheckBipartiteGraph2.dfs(l, mid, jcast('int', (i << (1 & 31))))
                Code02_CheckBipartiteGraph2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        else:
            k = jcast('int', l)
            while (k <= r):
                Code02_CheckBipartiteGraph2.ans[k] = jcast('boolean', False)
                k = jcast('int', (k + 1))
        k = jcast('int', 1)
        while (k <= unionCnt):
            Code02_CheckBipartiteGraph2.undo()
            k = jcast('int', (k + 1))

    @staticmethod
    def main(args):
        io = Code02_CheckBipartiteGraph2.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code02_CheckBipartiteGraph2.n = jcast('int', jcall(io, 'nextInt'))
        Code02_CheckBipartiteGraph2.m = jcast('int', jcall(io, 'nextInt'))
        Code02_CheckBipartiteGraph2.k = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code02_CheckBipartiteGraph2.n * 2))):
            Code02_CheckBipartiteGraph2.father[i] = jcast('int', i)
            Code02_CheckBipartiteGraph2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        l = 0
        r = 0
        while (i <= Code02_CheckBipartiteGraph2.m):
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            l = jcast('int', jcall(io, 'nextInt'))
            r = jcast('int', jcall(io, 'nextInt'))
            Code02_CheckBipartiteGraph2.add(jcast('int', jadd(l, 1)), r, x, y, 1, Code02_CheckBipartiteGraph2.k, 1)
            i = jcast('int', (i + 1))
        Code02_CheckBipartiteGraph2.dfs(1, Code02_CheckBipartiteGraph2.k, 1)
        i = jcast('int', 1)
        while (i <= Code02_CheckBipartiteGraph2.k):
            if Code02_CheckBipartiteGraph2.ans[i]:
                jcall(io, 'write', 'Yes\n')
            else:
                jcall(io, 'write', 'No\n')
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
                except Exception as _java_exception_11:
                    if jinstanceof(_java_exception_11, 'IOException'):
                        e = _java_exception_11
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_12 := self), (_java_key_13 := 'ptrbuf'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]] & 255)))

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
            except Exception as _java_exception_15:
                if jinstanceof(_java_exception_15, 'IOException'):
                    e = _java_exception_15
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
            raise TypeError("No matching overload for Code02_CheckBipartiteGraph2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CheckBipartiteGraph2.MAXN = jcast('int', 100001)
Code02_CheckBipartiteGraph2.MAXT = jcast('int', 3000001)
Code02_CheckBipartiteGraph2.n = jcast('int', 0)
Code02_CheckBipartiteGraph2.m = jcast('int', 0)
Code02_CheckBipartiteGraph2.k = jcast('int', 0)
Code02_CheckBipartiteGraph2.father = jarray('int', [jcast('int', (Code02_CheckBipartiteGraph2.MAXN << (1 & 31)))])
Code02_CheckBipartiteGraph2.siz = jarray('int', [jcast('int', (Code02_CheckBipartiteGraph2.MAXN << (1 & 31)))])
Code02_CheckBipartiteGraph2.rollback = jarray('int', [jcast('int', (Code02_CheckBipartiteGraph2.MAXN << (1 & 31))), 2])
Code02_CheckBipartiteGraph2.opsize = jcast('int', 0)
Code02_CheckBipartiteGraph2.head = jarray('int', [jcast('int', (Code02_CheckBipartiteGraph2.MAXN << (2 & 31)))])
Code02_CheckBipartiteGraph2.next = jarray('int', [Code02_CheckBipartiteGraph2.MAXT])
Code02_CheckBipartiteGraph2.tox = jarray('int', [Code02_CheckBipartiteGraph2.MAXT])
Code02_CheckBipartiteGraph2.toy = jarray('int', [Code02_CheckBipartiteGraph2.MAXT])
Code02_CheckBipartiteGraph2.cnt = jcast('int', 0)
Code02_CheckBipartiteGraph2.ans = jarray('boolean', [Code02_CheckBipartiteGraph2.MAXN])

if __name__ == '__main__':
    Code02_CheckBipartiteGraph2.main([])
