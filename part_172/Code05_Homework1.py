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

# 作业，Python版
# 给定一个长度为n的数组arr，接下来有m条查询，格式如下
# 查询 l r a b : 打印arr[l..r]范围上的两个答案
# 答案1，数值范围在[a, b]的数字个数
# 答案2，数值范围在[a, b]的数字种数
# 1 <= 所有数据 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4396
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Homework1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'numCnt': 'numCnt', 'blockCnt': 'blockCnt', 'blockKind': 'blockKind', 'ans1': 'ans1', 'ans2': 'ans2'}
    MAXN = 0
    MAXV = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    # 查询任务，l、r、a、b、id
    query = None
    bi = None
    bl = None
    br = None
    numCnt = None
    blockCnt = None
    blockKind = None
    ans1 = None
    ans2 = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code05_Homework1.bi[a[0]] != Code05_Homework1.bi[b[0]]):
                return jcast('int', jcast('int', (Code05_Homework1.bi[a[0]] - Code05_Homework1.bi[b[0]])))
            if (jcast('int', (Code05_Homework1.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def add(x):
        x = jcast('int', x)
        Code05_Homework1.numCnt[x] = jcast('int', (Code05_Homework1.numCnt[x] + 1))
        ((_java_obj_1 := Code05_Homework1.blockCnt), (_java_key_2 := Code05_Homework1.bi[x]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
        if (Code05_Homework1.numCnt[x] == 1):
            ((_java_obj_4 := Code05_Homework1.blockKind), (_java_key_5 := Code05_Homework1.bi[x]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]

    @staticmethod
    def del_(x):
        x = jcast('int', x)
        Code05_Homework1.numCnt[x] = jcast('int', (Code05_Homework1.numCnt[x] - 1))
        ((_java_obj_7 := Code05_Homework1.blockCnt), (_java_key_8 := Code05_Homework1.bi[x]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
        if (Code05_Homework1.numCnt[x] == 0):
            ((_java_obj_10 := Code05_Homework1.blockKind), (_java_key_11 := Code05_Homework1.bi[x]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]

    @staticmethod
    def setAns(a, b, id):
        a = jcast('int', a)
        b = jcast('int', b)
        id = jcast('int', id)
        if (Code05_Homework1.bi[a] == Code05_Homework1.bi[b]):
            i = jcast('int', a)
            while (i <= b):
                if (Code05_Homework1.numCnt[i] > 0):
                    Code05_Homework1.ans1[id] = jcast('int', jcast('int', jadd(Code05_Homework1.ans1[id], Code05_Homework1.numCnt[i])))
                    Code05_Homework1.ans2[id] = jcast('int', (Code05_Homework1.ans2[id] + 1))
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', a)
            while (i <= Code05_Homework1.br[Code05_Homework1.bi[a]]):
                if (Code05_Homework1.numCnt[i] > 0):
                    Code05_Homework1.ans1[id] = jcast('int', jcast('int', jadd(Code05_Homework1.ans1[id], Code05_Homework1.numCnt[i])))
                    Code05_Homework1.ans2[id] = jcast('int', (Code05_Homework1.ans2[id] + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', Code05_Homework1.bl[Code05_Homework1.bi[b]])
            while (i <= b):
                if (Code05_Homework1.numCnt[i] > 0):
                    Code05_Homework1.ans1[id] = jcast('int', jcast('int', jadd(Code05_Homework1.ans1[id], Code05_Homework1.numCnt[i])))
                    Code05_Homework1.ans2[id] = jcast('int', (Code05_Homework1.ans2[id] + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', jadd(Code05_Homework1.bi[a], 1)))
            while (i <= jcast('int', (Code05_Homework1.bi[b] - 1))):
                Code05_Homework1.ans1[id] = jcast('int', jcast('int', jadd(Code05_Homework1.ans1[id], Code05_Homework1.blockCnt[i])))
                Code05_Homework1.ans2[id] = jcast('int', jcast('int', jadd(Code05_Homework1.ans2[id], Code05_Homework1.blockKind[i])))
                i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_Homework1.m):
            jobl = jcast('int', Code05_Homework1.query[i][0])
            jobr = jcast('int', Code05_Homework1.query[i][1])
            joba = jcast('int', Code05_Homework1.query[i][2])
            jobb = jcast('int', Code05_Homework1.query[i][3])
            id = jcast('int', Code05_Homework1.query[i][4])
            while (winl > jobl):
                Code05_Homework1.add(Code05_Homework1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code05_Homework1.add(Code05_Homework1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code05_Homework1.del_(Code05_Homework1.arr[((_java_old_13 := winl), (winl := jcast('int', (winl + (1)))), _java_old_13)[2]])
            while (winr > jobr):
                Code05_Homework1.del_(Code05_Homework1.arr[((_java_old_14 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_14)[2]])
            Code05_Homework1.setAns(joba, jobb, id)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code05_Homework1.MAXV)))
        bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code05_Homework1.MAXV, blen)) - 1)), blen)))
        i = jcast('int', 1)
        while (i <= Code05_Homework1.MAXV):
            Code05_Homework1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= bnum):
            Code05_Homework1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * blen)), 1)))
            jset(Code05_Homework1.br, i, jstatic('Math', 'min', jcast('int', (i * blen)), Code05_Homework1.MAXV))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Homework1.query, 1, jcast('int', jadd(Code05_Homework1.m, 1)), Code05_Homework1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code05_Homework1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Homework1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Homework1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Homework1.n):
            jset(Code05_Homework1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Homework1.m):
            jset(Code05_Homework1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code05_Homework1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code05_Homework1.query[i], 2, jcall(in_, 'nextInt'))
            jset(Code05_Homework1.query[i], 3, jcall(in_, 'nextInt'))
            jset(Code05_Homework1.query[i], 4, i)
            i = jcast('int', (i + 1))
        Code05_Homework1.prepare()
        Code05_Homework1.compute()
        i = jcast('int', 1)
        while (i <= Code05_Homework1.m):
            jcall(out, 'println', jadd(jadd(Code05_Homework1.ans1[i], ' '), Code05_Homework1.ans2[i]))
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
            return jcast('int', self.buffer[((_java_obj_15 := self), (_java_key_16 := 'ptr'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))), _java_old_17)[4]])

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
            raise TypeError("No matching overload for Code05_Homework1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Homework1.MAXN = jcast('int', 100001)
Code05_Homework1.MAXV = jcast('int', 100000)
Code05_Homework1.MAXB = jcast('int', 401)
Code05_Homework1.n = jcast('int', 0)
Code05_Homework1.m = jcast('int', 0)
Code05_Homework1.arr = jarray('int', [Code05_Homework1.MAXN])
Code05_Homework1.query = jarray('int', [Code05_Homework1.MAXN, 5])
Code05_Homework1.bi = jarray('int', [Code05_Homework1.MAXN])
Code05_Homework1.bl = jarray('int', [Code05_Homework1.MAXB])
Code05_Homework1.br = jarray('int', [Code05_Homework1.MAXB])
Code05_Homework1.numCnt = jarray('int', [Code05_Homework1.MAXN])
Code05_Homework1.blockCnt = jarray('int', [Code05_Homework1.MAXB])
Code05_Homework1.blockKind = jarray('int', [Code05_Homework1.MAXB])
Code05_Homework1.ans1 = jarray('int', [Code05_Homework1.MAXN])
Code05_Homework1.ans2 = jarray('int', [Code05_Homework1.MAXN])

if __name__ == '__main__':
    Code05_Homework1.main([])
