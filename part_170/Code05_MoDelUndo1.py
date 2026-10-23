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

# 只删回滚莫队入门题，Python版
# 本题最优解为主席树，讲解158，题目2，已经讲述
# 给定一个长度为n的数组arr，一共有m条查询，格式如下
# 查询 l r : 打印arr[l..r]内没有出现过的最小自然数，注意0是自然数
# 0 <= n、m、arr[i] <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4137
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_MoDelUndo1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'cnt': 'cnt', 'mex': 'mex', 'ans': 'ans'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    query = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    cnt = None
    mex = 0
    ans = None
    # 只删回滚莫队经典排序
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code05_MoDelUndo1.bi[a[0]] != Code05_MoDelUndo1.bi[b[0]]):
                return jcast('int', jcast('int', (Code05_MoDelUndo1.bi[a[0]] - Code05_MoDelUndo1.bi[b[0]])))
            return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def del_(num):
        num = jcast('int', num)
        if (((_java_obj_1 := Code05_MoDelUndo1.cnt), (_java_key_2 := num), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3] == 0):
            Code05_MoDelUndo1.mex = jcast('int', jstatic('Math', 'min', Code05_MoDelUndo1.mex, num))

    @staticmethod
    def add(num):
        num = jcast('int', num)
        Code05_MoDelUndo1.cnt[num] = jcast('int', (Code05_MoDelUndo1.cnt[num] + 1))

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code05_MoDelUndo1.n):
            ((_java_obj_4 := Code05_MoDelUndo1.cnt), (_java_key_5 := Code05_MoDelUndo1.arr[i]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
            i = jcast('int', (i + 1))
        Code05_MoDelUndo1.mex = jcast('int', 0)
        while (Code05_MoDelUndo1.cnt[Code05_MoDelUndo1.mex] != 0):
            Code05_MoDelUndo1.mex = jcast('int', (Code05_MoDelUndo1.mex + 1))
        winl = jcast('int', 1)
        winr = jcast('int', Code05_MoDelUndo1.n)
        block = jcast('int', 1)
        qi = jcast('int', 1)
        while ((block <= Code05_MoDelUndo1.bnum) and (qi <= Code05_MoDelUndo1.m)):
            while (winl < Code05_MoDelUndo1.bl[block]):
                Code05_MoDelUndo1.del_(Code05_MoDelUndo1.arr[((_java_old_7 := winl), (winl := jcast('int', (winl + (1)))), _java_old_7)[2]])
            beforeJob = jcast('int', Code05_MoDelUndo1.mex)
            while ((qi <= Code05_MoDelUndo1.m) and (Code05_MoDelUndo1.bi[Code05_MoDelUndo1.query[qi][0]] == block)):
                jobl = jcast('int', Code05_MoDelUndo1.query[qi][0])
                jobr = jcast('int', Code05_MoDelUndo1.query[qi][1])
                id = jcast('int', Code05_MoDelUndo1.query[qi][2])
                while (winr > jobr):
                    Code05_MoDelUndo1.del_(Code05_MoDelUndo1.arr[((_java_old_8 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_8)[2]])
                backup = jcast('int', Code05_MoDelUndo1.mex)
                while (winl < jobl):
                    Code05_MoDelUndo1.del_(Code05_MoDelUndo1.arr[((_java_old_9 := winl), (winl := jcast('int', (winl + (1)))), _java_old_9)[2]])
                Code05_MoDelUndo1.ans[id] = jcast('int', Code05_MoDelUndo1.mex)
                Code05_MoDelUndo1.mex = jcast('int', backup)
                while (winl > Code05_MoDelUndo1.bl[block]):
                    Code05_MoDelUndo1.add(Code05_MoDelUndo1.arr[(winl := jcast('int', (winl + (-1))))])
                qi = jcast('int', (qi + 1))
            while (winr < Code05_MoDelUndo1.n):
                Code05_MoDelUndo1.add(Code05_MoDelUndo1.arr[(winr := jcast('int', (winr + (1))))])
            Code05_MoDelUndo1.mex = jcast('int', beforeJob)
            block = jcast('int', (block + 1))

    @staticmethod
    def prepare():
        Code05_MoDelUndo1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code05_MoDelUndo1.n)))
        Code05_MoDelUndo1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code05_MoDelUndo1.n, Code05_MoDelUndo1.blen)) - 1)), Code05_MoDelUndo1.blen)))
        i = jcast('int', 1)
        while (i <= Code05_MoDelUndo1.n):
            Code05_MoDelUndo1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code05_MoDelUndo1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_MoDelUndo1.bnum):
            Code05_MoDelUndo1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code05_MoDelUndo1.blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_MoDelUndo1.query, 1, jcast('int', jadd(Code05_MoDelUndo1.m, 1)), Code05_MoDelUndo1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code05_MoDelUndo1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_MoDelUndo1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_MoDelUndo1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_MoDelUndo1.n):
            jset(Code05_MoDelUndo1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_MoDelUndo1.m):
            jset(Code05_MoDelUndo1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code05_MoDelUndo1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code05_MoDelUndo1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code05_MoDelUndo1.prepare()
        Code05_MoDelUndo1.compute()
        i = jcast('int', 1)
        while (i <= Code05_MoDelUndo1.m):
            jcall(out, 'println', Code05_MoDelUndo1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code05_MoDelUndo1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MoDelUndo1.MAXN = jcast('int', 200001)
Code05_MoDelUndo1.MAXB = jcast('int', 501)
Code05_MoDelUndo1.n = jcast('int', 0)
Code05_MoDelUndo1.m = jcast('int', 0)
Code05_MoDelUndo1.arr = jarray('int', [Code05_MoDelUndo1.MAXN])
Code05_MoDelUndo1.query = jarray('int', [Code05_MoDelUndo1.MAXN, 3])
Code05_MoDelUndo1.blen = jcast('int', 0)
Code05_MoDelUndo1.bnum = jcast('int', 0)
Code05_MoDelUndo1.bi = jarray('int', [Code05_MoDelUndo1.MAXN])
Code05_MoDelUndo1.bl = jarray('int', [Code05_MoDelUndo1.MAXB])
Code05_MoDelUndo1.cnt = jarray('int', [Code05_MoDelUndo1.MAXN])
Code05_MoDelUndo1.mex = jcast('int', 0)
Code05_MoDelUndo1.ans = jarray('int', [Code05_MoDelUndo1.MAXN])

if __name__ == '__main__':
    Code05_MoDelUndo1.main([])
