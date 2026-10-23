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

# 第一次出现位置的序列，Python版
# 给定一个长度为n的数组arr，下标1~n，一共有m条查询，每条查询格式如下
# l r : arr[l..r]范围上，每个数第一次出现的位置，把这些位置组成一个序列
# 假设该范围有s种不同的数，那么序列长度为s
# 打印该序列第s/2个位置(向上取整)，对应arr的什么位置
# 题目有强制在线的要求，上一次打印的答案为lastAns，初始时lastAns = 0
# 每次给定的l和r，按照如下方式得到真实的l和r，查询完成后更新lastAns
# a = (给定l + lastAns) % n + 1
# b = (给定r + lastAns) % n + 1
# 真实l = min(a, b)
# 真实r = max(a, b)
# 1 <= n、m <= 2 * 10^5    0 <= arr[i] <= 2 * 10^5
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=5919
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_FirstTimeSequence1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'cases': 'cases', 'n': 'n', 'm': 'm', 'arr': 'arr', 'pos': 'pos', 'root': 'root', 'left': 'left', 'right': 'right', 'firstSize': 'firstSize', 'cnt': 'cnt'}
    MAXN = 0
    MAXT = 0
    cases = 0
    n = 0
    m = 0
    arr = None
    # pos[v] : v这个数字上次出现的位置
    pos = None
    # 可持久化线段树需要
    root = None
    left = None
    right = None
    # 数组范围上只记录每种数第一次出现的位置，这样的位置有多少个
    firstSize = None
    cnt = 0
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code01_FirstTimeSequence1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code01_FirstTimeSequence1.left, rt, Code01_FirstTimeSequence1.build(l, mid))
            jset(Code01_FirstTimeSequence1.right, rt, Code01_FirstTimeSequence1.build(jcast('int', jadd(mid, 1)), r))
        Code01_FirstTimeSequence1.firstSize[rt] = jcast('int', 0)
        return jcast('int', rt)

    # 数组范围l~r，信息在i号节点
    # 如果jobv = -1，意味着jobi位置减少一个计数
    # 如果jobv = +1，意味着jobi位置增加一个计数
    # 返回新的头节点编号
    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code01_FirstTimeSequence1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code01_FirstTimeSequence1.left[rt] = jcast('int', Code01_FirstTimeSequence1.left[i])
        Code01_FirstTimeSequence1.right[rt] = jcast('int', Code01_FirstTimeSequence1.right[i])
        Code01_FirstTimeSequence1.firstSize[rt] = jcast('int', jcast('int', jadd(Code01_FirstTimeSequence1.firstSize[i], jobv)))
        if (l == r):
            return jcast('int', rt)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (jobi <= mid):
            jset(Code01_FirstTimeSequence1.left, rt, Code01_FirstTimeSequence1.update(jobi, jobv, l, mid, Code01_FirstTimeSequence1.left[rt]))
        else:
            jset(Code01_FirstTimeSequence1.right, rt, Code01_FirstTimeSequence1.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code01_FirstTimeSequence1.right[rt]))
        return jcast('int', rt)

    # 数组范围l~r，信息在i号节点
    # jobl ~ jobr范围上，一共有几种不同的数字，也就是这个范围上，有多少个位置有1
    @staticmethod
    def querySize(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code01_FirstTimeSequence1.firstSize[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code01_FirstTimeSequence1.querySize(jobl, jobr, l, mid, Code01_FirstTimeSequence1.left[i]))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code01_FirstTimeSequence1.querySize(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code01_FirstTimeSequence1.right[i]))))
        return jcast('int', ans)

    # 数组范围l~r，信息在i号节点
    # 查询这个范围上，第jobk个1在哪
    @staticmethod
    def queryKth(jobk, l, r, i):
        jobk = jcast('int', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', l)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        lsize = jcast('int', Code01_FirstTimeSequence1.firstSize[Code01_FirstTimeSequence1.left[i]])
        if (lsize >= jobk):
            return jcast('int', Code01_FirstTimeSequence1.queryKth(jobk, l, mid, Code01_FirstTimeSequence1.left[i]))
        else:
            return jcast('int', Code01_FirstTimeSequence1.queryKth(jcast('int', (jobk - lsize)), jcast('int', jadd(mid, 1)), r, Code01_FirstTimeSequence1.right[i]))

    # 从右往左建立各个版本的线段树
    @staticmethod
    def prepare():
        Code01_FirstTimeSequence1.cnt = jcast('int', 0)
        jstatic('Arrays', 'fill', Code01_FirstTimeSequence1.pos, 0)
        jset(Code01_FirstTimeSequence1.root, jcast('int', jadd(Code01_FirstTimeSequence1.n, 1)), Code01_FirstTimeSequence1.build(1, Code01_FirstTimeSequence1.n))
        i = jcast('int', Code01_FirstTimeSequence1.n)
        while (i >= 1):
            if (Code01_FirstTimeSequence1.pos[Code01_FirstTimeSequence1.arr[i]] == 0):
                jset(Code01_FirstTimeSequence1.root, i, Code01_FirstTimeSequence1.update(i, 1, 1, Code01_FirstTimeSequence1.n, Code01_FirstTimeSequence1.root[jcast('int', jadd(i, 1))]))
            else:
                jset(Code01_FirstTimeSequence1.root, i, Code01_FirstTimeSequence1.update(Code01_FirstTimeSequence1.pos[Code01_FirstTimeSequence1.arr[i]], jcast('int', (-1)), 1, Code01_FirstTimeSequence1.n, Code01_FirstTimeSequence1.root[jcast('int', jadd(i, 1))]))
                jset(Code01_FirstTimeSequence1.root, i, Code01_FirstTimeSequence1.update(i, 1, 1, Code01_FirstTimeSequence1.n, Code01_FirstTimeSequence1.root[i]))
            jset(Code01_FirstTimeSequence1.pos, Code01_FirstTimeSequence1.arr[i], i)
            i = jcast('int', (i - 1))

    @staticmethod
    def main(args):
        io = Code01_FirstTimeSequence1.ReaderWriter(_java_ctor=0)
        Code01_FirstTimeSequence1.cases = jcast('int', jcall(io, 'nextInt'))
        t = jcast('int', 1)
        while (t <= Code01_FirstTimeSequence1.cases):
            Code01_FirstTimeSequence1.n = jcast('int', jcall(io, 'nextInt'))
            Code01_FirstTimeSequence1.m = jcast('int', jcall(io, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code01_FirstTimeSequence1.n):
                jset(Code01_FirstTimeSequence1.arr, i, jcall(io, 'nextInt'))
                i = jcast('int', (i + 1))
            Code01_FirstTimeSequence1.prepare()
            jcall(io, 'write', 'Case #')
            jcall(io, 'writeInt', t)
            jcall(io, 'write', ':')
            i = jcast('int', 1)
            a = 0
            b = 0
            l = 0
            r = 0
            k = 0
            lastAns = jcast('int', 0)
            while (i <= Code01_FirstTimeSequence1.m):
                a = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcall(io, 'nextInt'), lastAns)), Code01_FirstTimeSequence1.n)), 1)))
                b = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcall(io, 'nextInt'), lastAns)), Code01_FirstTimeSequence1.n)), 1)))
                l = jcast('int', jstatic('Math', 'min', a, b))
                r = jcast('int', jstatic('Math', 'max', a, b))
                k = jcast('int', jcast('int', jdiv(jcast('int', jadd(Code01_FirstTimeSequence1.querySize(l, r, 1, Code01_FirstTimeSequence1.n, Code01_FirstTimeSequence1.root[l]), 1)), 2)))
                lastAns = jcast('int', Code01_FirstTimeSequence1.queryKth(k, 1, Code01_FirstTimeSequence1.n, Code01_FirstTimeSequence1.root[l]))
                jcall(io, 'write', ' ')
                jcall(io, 'writeInt', lastAns)
                i = jcast('int', (i + 1))
            jcall(io, 'write', '\n')
            t = jcast('int', (t + 1))
        jcall(io, 'flush')

    # 读写工具类
    class ReaderWriter:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'inBuf': 'inBuf', 'bId': 'bId', 'bSize': 'bSize', 'in': 'in_', 'outBuf': 'outBuf', 'oId': 'oId', 'out': 'out'}
        BUFFER_SIZE = 0
        # inBuf：实例字段，在构造函数中初始化。
        # bId：实例字段，在构造函数中初始化。
        # bSize：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # outBuf：实例字段，在构造函数中初始化。
        # oId：实例字段，在构造函数中初始化。
        # out：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.out = jget(System, 'out')

        def read(self):
            if (self.bId == self.bSize):
                self.bSize = jcast('int', jcall(self.in_, 'read', self.inBuf))
                self.bId = jcast('int', 0)
                if (self.bSize == jcast('int', (-1))):
                    return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.inBuf[((_java_obj_7 := self), (_java_key_8 := 'bId'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

        def nextInt(self):
            s = jcast('int', 0)
            c = jcast('byte', self.read())
            while (c <= jchar(' ')):
                if (c == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
                c = jcast('byte', self.read())
            neg = jcast('boolean', (c == jchar('-')))
            if neg:
                c = jcast('byte', self.read())
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                s = jcast('int', jcast('int', jadd(jcast('int', (s * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('byte', self.read())
            return jcast('int', (jcast('int', (-s)) if neg else s))

        def write(self, s):
            i = jcast('int', 0)
            while (i < jcall(s, 'length')):
                self.writeByte(jcast('byte', jcall(s, 'charAt', i)))
                i = jcast('int', (i + 1))

        def writeInt(self, x):
            x = jcast('int', x)
            if (x == 0):
                self.writeByte(jcast('byte', jchar('0')))
                return
            if (x < 0):
                self.writeByte(jcast('byte', jchar('-')))
                x = jcast('int', jcast('int', (-x)))
            len = jcast('int', 0)
            tmp = jarray('byte', [12])
            while (x > 0):
                jset(tmp, ((_java_old_10 := len), (len := jcast('int', (len + (1)))), _java_old_10)[2], jcast('byte', jcast('int', jadd(jcast('int', jmod(x, 10)), jchar('0')))))
                x = jcast('int', jcast('int', jdiv(x, 10)))
            while (((_java_old_11 := len), (len := jcast('int', (len + (-1)))), _java_old_11)[2] > 0):
                self.writeByte(tmp[len])

        def writeByte(self, b):
            b = jcast('byte', b)
            if (self.oId == Code01_FirstTimeSequence1.ReaderWriter.BUFFER_SIZE):
                self.flush()
            jset(self.outBuf, ((_java_obj_12 := self), (_java_key_13 := 'oId'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4], b)

        def flush(self):
            if (self.oId > 0):
                jcall(self.out, 'write', self.outBuf, 0, self.oId)
                self.oId = jcast('int', 0)

        def __init__(self, *args, _java_ctor=None):
            self.inBuf = jarray('byte', [Code01_FirstTimeSequence1.ReaderWriter.BUFFER_SIZE])
            self.bId = jcast('int', 0)
            self.bSize = jcast('int', 0)
            self.in_ = None
            self.outBuf = jarray('byte', [Code01_FirstTimeSequence1.ReaderWriter.BUFFER_SIZE])
            self.oId = jcast('int', 0)
            self.out = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_FirstTimeSequence1.ReaderWriter.ReaderWriter")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_FirstTimeSequence1.MAXN = jcast('int', 200002)
Code01_FirstTimeSequence1.MAXT = jcast('int', jcast('int', (Code01_FirstTimeSequence1.MAXN * 37)))
Code01_FirstTimeSequence1.cases = jcast('int', 0)
Code01_FirstTimeSequence1.n = jcast('int', 0)
Code01_FirstTimeSequence1.m = jcast('int', 0)
Code01_FirstTimeSequence1.arr = jarray('int', [Code01_FirstTimeSequence1.MAXN])
Code01_FirstTimeSequence1.pos = jarray('int', [Code01_FirstTimeSequence1.MAXN])
Code01_FirstTimeSequence1.root = jarray('int', [Code01_FirstTimeSequence1.MAXN])
Code01_FirstTimeSequence1.left = jarray('int', [Code01_FirstTimeSequence1.MAXT])
Code01_FirstTimeSequence1.right = jarray('int', [Code01_FirstTimeSequence1.MAXT])
Code01_FirstTimeSequence1.firstSize = jarray('int', [Code01_FirstTimeSequence1.MAXT])
Code01_FirstTimeSequence1.cnt = jcast('int', 0)
Code01_FirstTimeSequence1.ReaderWriter.BUFFER_SIZE = jcast('int', jcast('int', (1 << (9 & 31))))

if __name__ == '__main__':
    Code01_FirstTimeSequence1.main([])
