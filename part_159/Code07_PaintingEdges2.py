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

# 给边涂色，Python版
# 一共有n个点，给定m条无向边，一开始每条边无颜色，一共有k种颜色
# 合法状态的定义为，仅保留染成k种颜色中的任何一种颜色的边，图都是一张二分图
# 一共有q条操作，每条操作格式如下
# 操作 e c : 第e条边，现在要涂成c颜色
# 如果执行此操作之后，整张图还是合法状态，那么执行并打印"YES"
# 如果执行此操作之后，整张图不再是合法状态，那么不执行并打印"NO"
# 1 <= n、m、q <= 5 * 10^5    1 <= k <= 50
# 测试链接 : https://www.luogu.com.cn/problem/CF576E
# 测试链接 : https://codeforces.com/problemset/problem/576/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_PaintingEdges2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'k': 'k', 'q': 'q', 'u': 'u', 'v': 'v', 'e': 'e', 'c': 'c', 'post': 'post', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'head': 'head', 'next': 'next', 'qid': 'qid', 'cnt': 'cnt', 'lastColor': 'lastColor', 'ans': 'ans'}
    MAXN = 0
    MAXK = 0
    MAXT = 0
    n = 0
    m = 0
    k = 0
    q = 0
    u = None
    v = None
    e = None
    c = None
    post = None
    father = None
    siz = None
    rollback = None
    opsize = 0
    # 时间轴线段树的区间上的任务列表
    # 尤其注意qid的设置，课上进行了重点解释
    head = None
    next = None
    qid = None
    cnt = 0
    # lastColor[i] : 第i号边上次成功涂上的颜色
    lastColor = None
    ans = None
    @staticmethod
    def addEdge(i, qi):
        i = jcast('int', i)
        qi = jcast('int', qi)
        jset(Code07_PaintingEdges2.next, ((_java_obj_1 := Code07_PaintingEdges2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_PaintingEdges2.head[i])
        Code07_PaintingEdges2.qid[Code07_PaintingEdges2.cnt] = jcast('int', qi)
        Code07_PaintingEdges2.head[i] = jcast('int', Code07_PaintingEdges2.cnt)

    @staticmethod
    def find(color, i):
        color = jcast('int', color)
        i = jcast('int', i)
        while (i != Code07_PaintingEdges2.father[color][i]):
            i = jcast('int', Code07_PaintingEdges2.father[color][i])
        return jcast('int', i)

    @staticmethod
    def union(color, x, y):
        color = jcast('int', color)
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code07_PaintingEdges2.find(color, x))
        fy = jcast('int', Code07_PaintingEdges2.find(color, y))
        if (Code07_PaintingEdges2.siz[color][fx] < Code07_PaintingEdges2.siz[color][fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        jset(Code07_PaintingEdges2.father[color], fy, fx)
        ((_java_obj_4 := Code07_PaintingEdges2.siz[color]), (_java_key_5 := fx), jset(_java_obj_4, _java_key_5, jcast('int', jadd(jget(_java_obj_4, _java_key_5), Code07_PaintingEdges2.siz[color][fy]))))[2]
        jset(Code07_PaintingEdges2.rollback[((_java_obj_6 := Code07_PaintingEdges2), (_java_key_7 := 'opsize'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3]], 0, color)
        jset(Code07_PaintingEdges2.rollback[Code07_PaintingEdges2.opsize], 1, fx)
        jset(Code07_PaintingEdges2.rollback[Code07_PaintingEdges2.opsize], 2, fy)

    @staticmethod
    def undo():
        color = jcast('int', Code07_PaintingEdges2.rollback[Code07_PaintingEdges2.opsize][0])
        fx = jcast('int', Code07_PaintingEdges2.rollback[Code07_PaintingEdges2.opsize][1])
        fy = jcast('int', Code07_PaintingEdges2.rollback[((_java_obj_9 := Code07_PaintingEdges2), (_java_key_10 := 'opsize'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (-1)))), _java_old_11)[4]][2])
        jset(Code07_PaintingEdges2.father[color], fy, fy)
        ((_java_obj_12 := Code07_PaintingEdges2.siz[color]), (_java_key_13 := fx), jset(_java_obj_12, _java_key_13, jcast('int', (jget(_java_obj_12, _java_key_13) - Code07_PaintingEdges2.siz[color][fy]))))[2]

    @staticmethod
    def add(jobl, jobr, jobq, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobq = jcast('int', jobq)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code07_PaintingEdges2.addEdge(i, jobq)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code07_PaintingEdges2.add(jobl, jobr, jobq, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code07_PaintingEdges2.add(jobl, jobr, jobq, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        unionCnt = jcast('int', 0)
        color = 0
        x = 0
        y = 0
        xn = 0
        yn = 0
        fx = 0
        fy = 0
        fxn = 0
        fyn = 0
        ei = jcast('int', Code07_PaintingEdges2.head[i])
        while (ei > 0):
            color = jcast('int', Code07_PaintingEdges2.c[Code07_PaintingEdges2.qid[ei]])
            x = jcast('int', Code07_PaintingEdges2.u[Code07_PaintingEdges2.e[Code07_PaintingEdges2.qid[ei]]])
            y = jcast('int', Code07_PaintingEdges2.v[Code07_PaintingEdges2.e[Code07_PaintingEdges2.qid[ei]]])
            xn = jcast('int', jcast('int', jadd(x, Code07_PaintingEdges2.n)))
            yn = jcast('int', jcast('int', jadd(y, Code07_PaintingEdges2.n)))
            fx = jcast('int', Code07_PaintingEdges2.find(color, x))
            fy = jcast('int', Code07_PaintingEdges2.find(color, y))
            fxn = jcast('int', Code07_PaintingEdges2.find(color, xn))
            fyn = jcast('int', Code07_PaintingEdges2.find(color, yn))
            if (fx != fyn):
                Code07_PaintingEdges2.union(color, fx, fyn)
                unionCnt = jcast('int', (unionCnt + 1))
            if (fy != fxn):
                Code07_PaintingEdges2.union(color, fy, fxn)
                unionCnt = jcast('int', (unionCnt + 1))
            ei = jcast('int', Code07_PaintingEdges2.next[ei])
        if (l == r):
            if (Code07_PaintingEdges2.find(Code07_PaintingEdges2.c[l], Code07_PaintingEdges2.u[Code07_PaintingEdges2.e[l]]) == Code07_PaintingEdges2.find(Code07_PaintingEdges2.c[l], Code07_PaintingEdges2.v[Code07_PaintingEdges2.e[l]])):
                Code07_PaintingEdges2.ans[l] = jcast('boolean', False)
                Code07_PaintingEdges2.c[l] = jcast('int', Code07_PaintingEdges2.lastColor[Code07_PaintingEdges2.e[l]])
            else:
                Code07_PaintingEdges2.ans[l] = jcast('boolean', True)
                jset(Code07_PaintingEdges2.lastColor, Code07_PaintingEdges2.e[l], Code07_PaintingEdges2.c[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code07_PaintingEdges2.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code07_PaintingEdges2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        j = jcast('int', 1)
        while (j <= unionCnt):
            Code07_PaintingEdges2.undo()
            j = jcast('int', (j + 1))

    @staticmethod
    def prepare():
        color = jcast('int', 1)
        while (color <= Code07_PaintingEdges2.k):
            i = jcast('int', 1)
            while (i <= Code07_PaintingEdges2.n):
                jset(Code07_PaintingEdges2.father[color], i, i)
                jset(Code07_PaintingEdges2.father[color], jcast('int', jadd(i, Code07_PaintingEdges2.n)), jcast('int', jadd(i, Code07_PaintingEdges2.n)))
                jset(Code07_PaintingEdges2.siz[color], i, 1)
                jset(Code07_PaintingEdges2.siz[color], jcast('int', jadd(i, Code07_PaintingEdges2.n)), 1)
                i = jcast('int', (i + 1))
            color = jcast('int', (color + 1))
        i = jcast('int', 1)
        while (i <= Code07_PaintingEdges2.m):
            Code07_PaintingEdges2.post[i] = jcast('int', Code07_PaintingEdges2.q)
            i = jcast('int', (i + 1))
        i = jcast('int', Code07_PaintingEdges2.q)
        while (i >= 1):
            if (jcast('int', jadd(i, 1)) <= Code07_PaintingEdges2.post[Code07_PaintingEdges2.e[i]]):
                Code07_PaintingEdges2.add(jcast('int', jadd(i, 1)), Code07_PaintingEdges2.post[Code07_PaintingEdges2.e[i]], i, 1, Code07_PaintingEdges2.q, 1)
            jset(Code07_PaintingEdges2.post, Code07_PaintingEdges2.e[i], i)
            i = jcast('int', (i - 1))

    @staticmethod
    def main(args):
        io = Code07_PaintingEdges2.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code07_PaintingEdges2.n = jcast('int', jcall(io, 'nextInt'))
        Code07_PaintingEdges2.m = jcast('int', jcall(io, 'nextInt'))
        Code07_PaintingEdges2.k = jcast('int', jcall(io, 'nextInt'))
        Code07_PaintingEdges2.q = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_PaintingEdges2.m):
            jset(Code07_PaintingEdges2.u, i, jcall(io, 'nextInt'))
            jset(Code07_PaintingEdges2.v, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_PaintingEdges2.q):
            jset(Code07_PaintingEdges2.e, i, jcall(io, 'nextInt'))
            jset(Code07_PaintingEdges2.c, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code07_PaintingEdges2.prepare()
        Code07_PaintingEdges2.dfs(1, Code07_PaintingEdges2.q, 1)
        i = jcast('int', 1)
        while (i <= Code07_PaintingEdges2.q):
            if Code07_PaintingEdges2.ans[i]:
                jcall(io, 'write', 'YES\n')
            else:
                jcall(io, 'write', 'NO\n')
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
            raise TypeError("No matching overload for Code07_PaintingEdges2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_PaintingEdges2.MAXN = jcast('int', 500001)
Code07_PaintingEdges2.MAXK = jcast('int', 51)
Code07_PaintingEdges2.MAXT = jcast('int', 10000001)
Code07_PaintingEdges2.n = jcast('int', 0)
Code07_PaintingEdges2.m = jcast('int', 0)
Code07_PaintingEdges2.k = jcast('int', 0)
Code07_PaintingEdges2.q = jcast('int', 0)
Code07_PaintingEdges2.u = jarray('int', [Code07_PaintingEdges2.MAXN])
Code07_PaintingEdges2.v = jarray('int', [Code07_PaintingEdges2.MAXN])
Code07_PaintingEdges2.e = jarray('int', [Code07_PaintingEdges2.MAXN])
Code07_PaintingEdges2.c = jarray('int', [Code07_PaintingEdges2.MAXN])
Code07_PaintingEdges2.post = jarray('int', [Code07_PaintingEdges2.MAXN])
Code07_PaintingEdges2.father = jarray('int', [Code07_PaintingEdges2.MAXK, jcast('int', (Code07_PaintingEdges2.MAXN << (1 & 31)))])
Code07_PaintingEdges2.siz = jarray('int', [Code07_PaintingEdges2.MAXK, jcast('int', (Code07_PaintingEdges2.MAXN << (1 & 31)))])
Code07_PaintingEdges2.rollback = jarray('int', [jcast('int', (Code07_PaintingEdges2.MAXN << (1 & 31))), 3])
Code07_PaintingEdges2.opsize = jcast('int', 0)
Code07_PaintingEdges2.head = jarray('int', [jcast('int', (Code07_PaintingEdges2.MAXN << (2 & 31)))])
Code07_PaintingEdges2.next = jarray('int', [Code07_PaintingEdges2.MAXT])
Code07_PaintingEdges2.qid = jarray('int', [Code07_PaintingEdges2.MAXT])
Code07_PaintingEdges2.cnt = jcast('int', 0)
Code07_PaintingEdges2.lastColor = jarray('int', [Code07_PaintingEdges2.MAXN])
Code07_PaintingEdges2.ans = jarray('boolean', [Code07_PaintingEdges2.MAXN])

if __name__ == '__main__':
    Code07_PaintingEdges2.main([])
