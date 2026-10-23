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

# 独特事件，Python版
# 一共有n个节点，n-1条无向边，边给定颜色值，所有节点连成一棵树
# 定义f(u, v) : 点u到点v的简单路径上恰好出现一次的颜色的数量
# 打印 ∑(u = 1..n) ∑(v = u + 1..n) f(u, v) 的结果
# 1 <= 颜色值 <= n <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1681F
# 测试链接 : https://codeforces.com/problemset/problem/1681/F
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_UniqueOccurrences2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'v': 'v', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'headc': 'headc', 'nextc': 'nextc', 'xc': 'xc', 'yc': 'yc', 'cntc': 'cntc', 'headt': 'headt', 'nextt': 'nextt', 'xt': 'xt', 'yt': 'yt', 'cntt': 'cntt', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    n = 0
    v = 0
    father = None
    siz = None
    rollback = None
    opsize = 0
    # 每种颜色拥有哪些边的列表
    headc = None
    nextc = None
    xc = None
    yc = None
    cntc = 0
    # 颜色轴线段树的区间任务列表
    headt = None
    nextt = None
    xt = None
    yt = None
    cntt = 0
    ans = 0
    @staticmethod
    def addEdgeC(i, x, y):
        i = jcast('int', i)
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code04_UniqueOccurrences2.nextc, ((_java_obj_1 := Code04_UniqueOccurrences2), (_java_key_2 := 'cntc'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_UniqueOccurrences2.headc[i])
        Code04_UniqueOccurrences2.xc[Code04_UniqueOccurrences2.cntc] = jcast('int', x)
        Code04_UniqueOccurrences2.yc[Code04_UniqueOccurrences2.cntc] = jcast('int', y)
        Code04_UniqueOccurrences2.headc[i] = jcast('int', Code04_UniqueOccurrences2.cntc)

    @staticmethod
    def addEdgeS(i, x, y):
        i = jcast('int', i)
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code04_UniqueOccurrences2.nextt, ((_java_obj_4 := Code04_UniqueOccurrences2), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_UniqueOccurrences2.headt[i])
        Code04_UniqueOccurrences2.xt[Code04_UniqueOccurrences2.cntt] = jcast('int', x)
        Code04_UniqueOccurrences2.yt[Code04_UniqueOccurrences2.cntt] = jcast('int', y)
        Code04_UniqueOccurrences2.headt[i] = jcast('int', Code04_UniqueOccurrences2.cntt)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code04_UniqueOccurrences2.father[i]):
            i = jcast('int', Code04_UniqueOccurrences2.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code04_UniqueOccurrences2.find(x))
        fy = jcast('int', Code04_UniqueOccurrences2.find(y))
        if (Code04_UniqueOccurrences2.siz[fx] < Code04_UniqueOccurrences2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code04_UniqueOccurrences2.father[fy] = jcast('int', fx)
        Code04_UniqueOccurrences2.siz[fx] = jcast('int', jcast('int', jadd(Code04_UniqueOccurrences2.siz[fx], Code04_UniqueOccurrences2.siz[fy])))
        jset(Code04_UniqueOccurrences2.rollback[((_java_obj_7 := Code04_UniqueOccurrences2), (_java_key_8 := 'opsize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]], 0, fx)
        jset(Code04_UniqueOccurrences2.rollback[Code04_UniqueOccurrences2.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code04_UniqueOccurrences2.rollback[Code04_UniqueOccurrences2.opsize][0])
        fy = jcast('int', Code04_UniqueOccurrences2.rollback[((_java_obj_10 := Code04_UniqueOccurrences2), (_java_key_11 := 'opsize'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]][1])
        Code04_UniqueOccurrences2.father[fy] = jcast('int', fy)
        Code04_UniqueOccurrences2.siz[fx] = jcast('int', jcast('int', (Code04_UniqueOccurrences2.siz[fx] - Code04_UniqueOccurrences2.siz[fy])))

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
            Code04_UniqueOccurrences2.addEdgeS(i, jobx, joby)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code04_UniqueOccurrences2.add(jobl, jobr, jobx, joby, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_UniqueOccurrences2.add(jobl, jobr, jobx, joby, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        unionCnt = jcast('int', 0)
        ei = jcast('int', Code04_UniqueOccurrences2.headt[i])
        while (ei > 0):
            Code04_UniqueOccurrences2.union(Code04_UniqueOccurrences2.xt[ei], Code04_UniqueOccurrences2.yt[ei])
            unionCnt = jcast('int', (unionCnt + 1))
            ei = jcast('int', Code04_UniqueOccurrences2.nextt[ei])
        if (l == r):
            ei = jcast('int', Code04_UniqueOccurrences2.headc[l])
            fx = 0
            fy = 0
            while (ei > 0):
                fx = jcast('int', Code04_UniqueOccurrences2.find(Code04_UniqueOccurrences2.xc[ei]))
                fy = jcast('int', Code04_UniqueOccurrences2.find(Code04_UniqueOccurrences2.yc[ei]))
                Code04_UniqueOccurrences2.ans = jcast('long', jcast('long', jadd(Code04_UniqueOccurrences2.ans, jcast('long', (jcast('long', Code04_UniqueOccurrences2.siz[fx]) * Code04_UniqueOccurrences2.siz[fy])))))
                ei = jcast('int', Code04_UniqueOccurrences2.nextc[ei])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_UniqueOccurrences2.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code04_UniqueOccurrences2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        k = jcast('int', 1)
        while (k <= unionCnt):
            Code04_UniqueOccurrences2.undo()
            k = jcast('int', (k + 1))

    @staticmethod
    def main(args):
        io = Code04_UniqueOccurrences2.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code04_UniqueOccurrences2.n = jcast('int', jcall(io, 'nextInt'))
        Code04_UniqueOccurrences2.v = jcast('int', Code04_UniqueOccurrences2.n)
        i = jcast('int', 1)
        x = 0
        y = 0
        c = 0
        while (i < Code04_UniqueOccurrences2.n):
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            c = jcast('int', jcall(io, 'nextInt'))
            Code04_UniqueOccurrences2.addEdgeC(c, x, y)
            if (c > 1):
                Code04_UniqueOccurrences2.add(1, jcast('int', (c - 1)), x, y, 1, Code04_UniqueOccurrences2.v, 1)
            if (c < Code04_UniqueOccurrences2.v):
                Code04_UniqueOccurrences2.add(jcast('int', jadd(c, 1)), Code04_UniqueOccurrences2.v, x, y, 1, Code04_UniqueOccurrences2.v, 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_UniqueOccurrences2.n):
            Code04_UniqueOccurrences2.father[i] = jcast('int', i)
            Code04_UniqueOccurrences2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        Code04_UniqueOccurrences2.dfs(1, Code04_UniqueOccurrences2.v, 1)
        jcall(io, 'writelnLong', Code04_UniqueOccurrences2.ans)
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
                except Exception as _java_exception_13:
                    if jinstanceof(_java_exception_13, 'IOException'):
                        e = _java_exception_13
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_14 := self), (_java_key_15 := 'ptrbuf'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]] & 255)))

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

        def writelnLong(self, x):
            x = jcast('long', x)
            jcall(jcall(self.outBuf, 'append', x), 'append', jchar('\n'))

        def flush(self):
            try:
                jcall(self.os, 'write', jcall(jcall(self.outBuf, 'toString'), 'getBytes'))
                jcall(self.os, 'flush')
                jcall(self.outBuf, 'setLength', 0)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_17:
                if jinstanceof(_java_exception_17, 'IOException'):
                    e = _java_exception_17
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
            raise TypeError("No matching overload for Code04_UniqueOccurrences2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_UniqueOccurrences2.MAXN = jcast('int', 500001)
Code04_UniqueOccurrences2.MAXT = jcast('int', 10000001)
Code04_UniqueOccurrences2.n = jcast('int', 0)
Code04_UniqueOccurrences2.v = jcast('int', 0)
Code04_UniqueOccurrences2.father = jarray('int', [Code04_UniqueOccurrences2.MAXN])
Code04_UniqueOccurrences2.siz = jarray('int', [Code04_UniqueOccurrences2.MAXN])
Code04_UniqueOccurrences2.rollback = jarray('int', [Code04_UniqueOccurrences2.MAXN, 2])
Code04_UniqueOccurrences2.opsize = jcast('int', 0)
Code04_UniqueOccurrences2.headc = jarray('int', [Code04_UniqueOccurrences2.MAXN])
Code04_UniqueOccurrences2.nextc = jarray('int', [Code04_UniqueOccurrences2.MAXN])
Code04_UniqueOccurrences2.xc = jarray('int', [Code04_UniqueOccurrences2.MAXN])
Code04_UniqueOccurrences2.yc = jarray('int', [Code04_UniqueOccurrences2.MAXN])
Code04_UniqueOccurrences2.cntc = jcast('int', 0)
Code04_UniqueOccurrences2.headt = jarray('int', [jcast('int', (Code04_UniqueOccurrences2.MAXN << (2 & 31)))])
Code04_UniqueOccurrences2.nextt = jarray('int', [Code04_UniqueOccurrences2.MAXT])
Code04_UniqueOccurrences2.xt = jarray('int', [Code04_UniqueOccurrences2.MAXT])
Code04_UniqueOccurrences2.yt = jarray('int', [Code04_UniqueOccurrences2.MAXT])
Code04_UniqueOccurrences2.cntt = jcast('int', 0)
Code04_UniqueOccurrences2.ans = jcast('long', 0)

if __name__ == '__main__':
    Code04_UniqueOccurrences2.main([])
