# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 线段树分治模版题，Python版
# 一共有n个节点，一共有m条操作，每条操作是如下三种类型中的一种
# 操作 0 x y : 点x和点y之间一定没有边，现在增加一条边
# 操作 1 x y : 点x和点y之间一定存在边，现在删除这条边
# 操作 2 x y : 查询点x和点y是否联通
# 1 <= n <= 5000
# 1 <= m <= 500000
# 不强制在线，可以离线处理
# 测试链接 : https://loj.ac/p/121
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_SegmentTreeDivideConquer1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'op': 'op', 'u': 'u', 'v': 'v', 'last': 'last', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'head': 'head', 'next': 'next', 'tox': 'tox', 'toy': 'toy', 'cnt': 'cnt', 'ans': 'ans'}
    # 点的数量最大值
    MAXN = 0
    # 操作数量最大值
    MAXM = 0
    # 任务数量最大值
    MAXT = 0
    n = 0
    m = 0
    # 操作类型op、端点u、端点v
    op = None
    u = None
    v = None
    # last[x][y] : 点x和点y的边，上次出现的时间点
    last = None
    # 可撤销并查集
    father = None
    siz = None
    rollback = None
    opsize = 0
    # 线段树每个区间拥有哪些任务的列表，链式前向星表示
    head = None
    next = None
    tox = None
    toy = None
    cnt = 0
    # ans[i]为第i条操作的答案，只有查询操作才有答案
    ans = None
    @staticmethod
    def addEdge(i, x, y):
        i = jcast('int', i)
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code01_SegmentTreeDivideConquer1.next, ((_java_obj_1 := Code01_SegmentTreeDivideConquer1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_SegmentTreeDivideConquer1.head[i])
        Code01_SegmentTreeDivideConquer1.tox[Code01_SegmentTreeDivideConquer1.cnt] = jcast('int', x)
        Code01_SegmentTreeDivideConquer1.toy[Code01_SegmentTreeDivideConquer1.cnt] = jcast('int', y)
        Code01_SegmentTreeDivideConquer1.head[i] = jcast('int', Code01_SegmentTreeDivideConquer1.cnt)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code01_SegmentTreeDivideConquer1.father[i]):
            i = jcast('int', Code01_SegmentTreeDivideConquer1.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code01_SegmentTreeDivideConquer1.find(x))
        fy = jcast('int', Code01_SegmentTreeDivideConquer1.find(y))
        if (Code01_SegmentTreeDivideConquer1.siz[fx] < Code01_SegmentTreeDivideConquer1.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code01_SegmentTreeDivideConquer1.father[fy] = jcast('int', fx)
        Code01_SegmentTreeDivideConquer1.siz[fx] = jcast('int', jcast('int', jadd(Code01_SegmentTreeDivideConquer1.siz[fx], Code01_SegmentTreeDivideConquer1.siz[fy])))
        jset(Code01_SegmentTreeDivideConquer1.rollback[((_java_obj_4 := Code01_SegmentTreeDivideConquer1), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, fx)
        jset(Code01_SegmentTreeDivideConquer1.rollback[Code01_SegmentTreeDivideConquer1.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code01_SegmentTreeDivideConquer1.rollback[Code01_SegmentTreeDivideConquer1.opsize][0])
        fy = jcast('int', Code01_SegmentTreeDivideConquer1.rollback[((_java_obj_7 := Code01_SegmentTreeDivideConquer1), (_java_key_8 := 'opsize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]][1])
        Code01_SegmentTreeDivideConquer1.father[fy] = jcast('int', fy)
        Code01_SegmentTreeDivideConquer1.siz[fx] = jcast('int', jcast('int', (Code01_SegmentTreeDivideConquer1.siz[fx] - Code01_SegmentTreeDivideConquer1.siz[fy])))

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
            Code01_SegmentTreeDivideConquer1.addEdge(i, jobx, joby)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code01_SegmentTreeDivideConquer1.add(jobl, jobr, jobx, joby, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_SegmentTreeDivideConquer1.add(jobl, jobr, jobx, joby, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        unionCnt = jcast('int', 0)
        ei = jcast('int', Code01_SegmentTreeDivideConquer1.head[i])
        x = 0
        y = 0
        fx = 0
        fy = 0
        while (ei > 0):
            x = jcast('int', Code01_SegmentTreeDivideConquer1.tox[ei])
            y = jcast('int', Code01_SegmentTreeDivideConquer1.toy[ei])
            fx = jcast('int', Code01_SegmentTreeDivideConquer1.find(x))
            fy = jcast('int', Code01_SegmentTreeDivideConquer1.find(y))
            if (fx != fy):
                Code01_SegmentTreeDivideConquer1.union(fx, fy)
                unionCnt = jcast('int', (unionCnt + 1))
            ei = jcast('int', Code01_SegmentTreeDivideConquer1.next[ei])
        if (l == r):
            if (Code01_SegmentTreeDivideConquer1.op[l] == 2):
                jset(Code01_SegmentTreeDivideConquer1.ans, l, (Code01_SegmentTreeDivideConquer1.find(Code01_SegmentTreeDivideConquer1.u[l]) == Code01_SegmentTreeDivideConquer1.find(Code01_SegmentTreeDivideConquer1.v[l])))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code01_SegmentTreeDivideConquer1.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code01_SegmentTreeDivideConquer1.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        j = jcast('int', 1)
        while (j <= unionCnt):
            Code01_SegmentTreeDivideConquer1.undo()
            j = jcast('int', (j + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code01_SegmentTreeDivideConquer1.n):
            Code01_SegmentTreeDivideConquer1.father[i] = jcast('int', i)
            Code01_SegmentTreeDivideConquer1.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        t = 0
        x = 0
        y = 0
        while (i <= Code01_SegmentTreeDivideConquer1.m):
            t = jcast('int', Code01_SegmentTreeDivideConquer1.op[i])
            x = jcast('int', Code01_SegmentTreeDivideConquer1.u[i])
            y = jcast('int', Code01_SegmentTreeDivideConquer1.v[i])
            if (t == 0):
                jset(Code01_SegmentTreeDivideConquer1.last[x], y, i)
            else:
                if (t == 1):
                    Code01_SegmentTreeDivideConquer1.add(Code01_SegmentTreeDivideConquer1.last[x][y], jcast('int', (i - 1)), x, y, 1, Code01_SegmentTreeDivideConquer1.m, 1)
                    jset(Code01_SegmentTreeDivideConquer1.last[x], y, 0)
            i = jcast('int', (i + 1))
        x = jcast('int', 1)
        while (x <= Code01_SegmentTreeDivideConquer1.n):
            y = jcast('int', jcast('int', jadd(x, 1)))
            while (y <= Code01_SegmentTreeDivideConquer1.n):
                if (Code01_SegmentTreeDivideConquer1.last[x][y] != 0):
                    Code01_SegmentTreeDivideConquer1.add(Code01_SegmentTreeDivideConquer1.last[x][y], Code01_SegmentTreeDivideConquer1.m, x, y, 1, Code01_SegmentTreeDivideConquer1.m, 1)
                y = jcast('int', (y + 1))
            x = jcast('int', (x + 1))

    @staticmethod
    def main(args):
        io = Code01_SegmentTreeDivideConquer1.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code01_SegmentTreeDivideConquer1.n = jcast('int', jcall(io, 'nextInt'))
        Code01_SegmentTreeDivideConquer1.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        t = 0
        x = 0
        y = 0
        while (i <= Code01_SegmentTreeDivideConquer1.m):
            t = jcast('int', jcall(io, 'nextInt'))
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            Code01_SegmentTreeDivideConquer1.op[i] = jcast('int', t)
            jset(Code01_SegmentTreeDivideConquer1.u, i, jstatic('Math', 'min', x, y))
            jset(Code01_SegmentTreeDivideConquer1.v, i, jstatic('Math', 'max', x, y))
            i = jcast('int', (i + 1))
        Code01_SegmentTreeDivideConquer1.prepare()
        Code01_SegmentTreeDivideConquer1.dfs(1, Code01_SegmentTreeDivideConquer1.m, 1)
        i = jcast('int', 1)
        while (i <= Code01_SegmentTreeDivideConquer1.m):
            if (Code01_SegmentTreeDivideConquer1.op[i] == 2):
                if Code01_SegmentTreeDivideConquer1.ans[i]:
                    jcall(io, 'write', 'Y\n')
                else:
                    jcall(io, 'write', 'N\n')
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
            raise TypeError("No matching overload for Code01_SegmentTreeDivideConquer1.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SegmentTreeDivideConquer1.MAXN = jcast('int', 5001)
Code01_SegmentTreeDivideConquer1.MAXM = jcast('int', 500001)
Code01_SegmentTreeDivideConquer1.MAXT = jcast('int', 5000001)
Code01_SegmentTreeDivideConquer1.n = jcast('int', 0)
Code01_SegmentTreeDivideConquer1.m = jcast('int', 0)
Code01_SegmentTreeDivideConquer1.op = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXM])
Code01_SegmentTreeDivideConquer1.u = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXM])
Code01_SegmentTreeDivideConquer1.v = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXM])
Code01_SegmentTreeDivideConquer1.last = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXN, Code01_SegmentTreeDivideConquer1.MAXN])
Code01_SegmentTreeDivideConquer1.father = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXN])
Code01_SegmentTreeDivideConquer1.siz = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXN])
Code01_SegmentTreeDivideConquer1.rollback = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXN, 2])
Code01_SegmentTreeDivideConquer1.opsize = jcast('int', 0)
Code01_SegmentTreeDivideConquer1.head = jarray('int', [jcast('int', (Code01_SegmentTreeDivideConquer1.MAXM << (2 & 31)))])
Code01_SegmentTreeDivideConquer1.next = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXT])
Code01_SegmentTreeDivideConquer1.tox = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXT])
Code01_SegmentTreeDivideConquer1.toy = jarray('int', [Code01_SegmentTreeDivideConquer1.MAXT])
Code01_SegmentTreeDivideConquer1.cnt = jcast('int', 0)
Code01_SegmentTreeDivideConquer1.ans = jarray('boolean', [Code01_SegmentTreeDivideConquer1.MAXM])

if __name__ == '__main__':
    Code01_SegmentTreeDivideConquer1.main([])
