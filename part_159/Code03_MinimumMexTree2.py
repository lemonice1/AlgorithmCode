# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最小mex生成树，Python版
# 给定n个点，m条边的无向连通图，边有边权
# 自然数集合S的mex含义为：最小的、没有出现在S中的自然数
# 现在你要求出一个这个图的生成树，使得其边权集合的mex尽可能小
# 对本题来说，注意0是自然数
# 1 <= n <= 10^6
# 1 <= m <= 2 * 10^6
# 0 <= 边权 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5631
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_MinimumMexTree2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'v': 'v', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'head': 'head', 'next': 'next', 'tox': 'tox', 'toy': 'toy', 'cnt': 'cnt', 'part': 'part'}
    MAXN = 0
    MAXV = 0
    MAXT = 0
    n = 0
    m = 0
    v = 0
    father = None
    siz = None
    rollback = None
    opsize = 0
    head = None
    next = None
    tox = None
    toy = None
    cnt = 0
    part = 0
    @staticmethod
    def addEdge(i, x, y):
        i = jcast('int', i)
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code03_MinimumMexTree2.next, ((_java_obj_1 := Code03_MinimumMexTree2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_MinimumMexTree2.head[i])
        Code03_MinimumMexTree2.tox[Code03_MinimumMexTree2.cnt] = jcast('int', x)
        Code03_MinimumMexTree2.toy[Code03_MinimumMexTree2.cnt] = jcast('int', y)
        Code03_MinimumMexTree2.head[i] = jcast('int', Code03_MinimumMexTree2.cnt)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code03_MinimumMexTree2.father[i]):
            i = jcast('int', Code03_MinimumMexTree2.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code03_MinimumMexTree2.find(x))
        fy = jcast('int', Code03_MinimumMexTree2.find(y))
        if (Code03_MinimumMexTree2.siz[fx] < Code03_MinimumMexTree2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code03_MinimumMexTree2.father[fy] = jcast('int', fx)
        Code03_MinimumMexTree2.siz[fx] = jcast('int', jcast('int', jadd(Code03_MinimumMexTree2.siz[fx], Code03_MinimumMexTree2.siz[fy])))
        jset(Code03_MinimumMexTree2.rollback[((_java_obj_4 := Code03_MinimumMexTree2), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, fx)
        jset(Code03_MinimumMexTree2.rollback[Code03_MinimumMexTree2.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code03_MinimumMexTree2.rollback[Code03_MinimumMexTree2.opsize][0])
        fy = jcast('int', Code03_MinimumMexTree2.rollback[((_java_obj_7 := Code03_MinimumMexTree2), (_java_key_8 := 'opsize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]][1])
        Code03_MinimumMexTree2.father[fy] = jcast('int', fy)
        Code03_MinimumMexTree2.siz[fx] = jcast('int', jcast('int', (Code03_MinimumMexTree2.siz[fx] - Code03_MinimumMexTree2.siz[fy])))

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
            Code03_MinimumMexTree2.addEdge(i, jobx, joby)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code03_MinimumMexTree2.add(jobl, jobr, jobx, joby, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_MinimumMexTree2.add(jobl, jobr, jobx, joby, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        unionCnt = jcast('int', 0)
        ei = jcast('int', Code03_MinimumMexTree2.head[i])
        fx = 0
        fy = 0
        while (ei > 0):
            fx = jcast('int', Code03_MinimumMexTree2.find(Code03_MinimumMexTree2.tox[ei]))
            fy = jcast('int', Code03_MinimumMexTree2.find(Code03_MinimumMexTree2.toy[ei]))
            if (fx != fy):
                Code03_MinimumMexTree2.union(fx, fy)
                Code03_MinimumMexTree2.part = jcast('int', (Code03_MinimumMexTree2.part - 1))
                unionCnt = jcast('int', (unionCnt + 1))
            ei = jcast('int', Code03_MinimumMexTree2.next[ei])
        ans = jcast('int', jcast('int', (-1)))
        if (l == r):
            if (Code03_MinimumMexTree2.part == 1):
                ans = jcast('int', l)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            ans = jcast('int', Code03_MinimumMexTree2.dfs(l, mid, jcast('int', (i << (1 & 31)))))
            if (ans == jcast('int', (-1))):
                ans = jcast('int', Code03_MinimumMexTree2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))
        k = jcast('int', 1)
        while (k <= unionCnt):
            Code03_MinimumMexTree2.undo()
            Code03_MinimumMexTree2.part = jcast('int', (Code03_MinimumMexTree2.part + 1))
            k = jcast('int', (k + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        io = Code03_MinimumMexTree2.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code03_MinimumMexTree2.n = jcast('int', jcall(io, 'nextInt'))
        Code03_MinimumMexTree2.m = jcast('int', jcall(io, 'nextInt'))
        Code03_MinimumMexTree2.v = jcast('int', Code03_MinimumMexTree2.MAXV)
        i = jcast('int', 1)
        while (i <= Code03_MinimumMexTree2.n):
            Code03_MinimumMexTree2.father[i] = jcast('int', i)
            Code03_MinimumMexTree2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        w = 0
        while (i <= Code03_MinimumMexTree2.m):
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            w = jcast('int', jcall(io, 'nextInt'))
            if (w > 0):
                Code03_MinimumMexTree2.add(0, jcast('int', (w - 1)), x, y, 0, Code03_MinimumMexTree2.v, 1)
            Code03_MinimumMexTree2.add(jcast('int', jadd(w, 1)), Code03_MinimumMexTree2.v, x, y, 0, Code03_MinimumMexTree2.v, 1)
            i = jcast('int', (i + 1))
        Code03_MinimumMexTree2.part = jcast('int', Code03_MinimumMexTree2.n)
        jcall(io, 'writelnInt', Code03_MinimumMexTree2.dfs(0, Code03_MinimumMexTree2.v, 1))
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
                except Exception as _java_exception_10:
                    if jinstanceof(_java_exception_10, 'IOException'):
                        e = _java_exception_10
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_11 := self), (_java_key_12 := 'ptrbuf'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]] & 255)))

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
            except Exception as _java_exception_14:
                if jinstanceof(_java_exception_14, 'IOException'):
                    e = _java_exception_14
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
            raise TypeError("No matching overload for Code03_MinimumMexTree2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MinimumMexTree2.MAXN = jcast('int', 1000001)
Code03_MinimumMexTree2.MAXV = jcast('int', 100001)
Code03_MinimumMexTree2.MAXT = jcast('int', 30000001)
Code03_MinimumMexTree2.n = jcast('int', 0)
Code03_MinimumMexTree2.m = jcast('int', 0)
Code03_MinimumMexTree2.v = jcast('int', 0)
Code03_MinimumMexTree2.father = jarray('int', [Code03_MinimumMexTree2.MAXN])
Code03_MinimumMexTree2.siz = jarray('int', [Code03_MinimumMexTree2.MAXN])
Code03_MinimumMexTree2.rollback = jarray('int', [Code03_MinimumMexTree2.MAXN, 2])
Code03_MinimumMexTree2.opsize = jcast('int', 0)
Code03_MinimumMexTree2.head = jarray('int', [jcast('int', (Code03_MinimumMexTree2.MAXV << (2 & 31)))])
Code03_MinimumMexTree2.next = jarray('int', [Code03_MinimumMexTree2.MAXT])
Code03_MinimumMexTree2.tox = jarray('int', [Code03_MinimumMexTree2.MAXT])
Code03_MinimumMexTree2.toy = jarray('int', [Code03_MinimumMexTree2.MAXT])
Code03_MinimumMexTree2.cnt = jcast('int', 0)
Code03_MinimumMexTree2.part = jcast('int', 0)

if __name__ == '__main__':
    Code03_MinimumMexTree2.main([])
