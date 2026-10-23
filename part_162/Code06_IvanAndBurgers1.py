# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 范围最大异或和，Python版
# 给定一个长度为n的数组arr，下标1~n，接下来有q条查询，格式如下
# 查询 l r : arr[l..r]中选若干个数，打印最大的异或和
# 1 <= n、q <= 5 * 10^5
# 0 <= arr[i] <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/CF1100F
# 测试链接 : https://codeforces.com/problemset/problem/1100/F
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_IvanAndBurgers1:
    __java_fields__ = {'MAXN': 'MAXN', 'BIT': 'BIT', 'n': 'n', 'q': 'q', 'arr': 'arr', 'qid': 'qid', 'l': 'l', 'r': 'r', 'baset': 'baset', 'tmp': 'tmp', 'lset': 'lset', 'rset': 'rset', 'ans': 'ans'}
    MAXN = 0
    BIT = 0
    n = 0
    q = 0
    arr = None
    qid = None
    l = None
    r = None
    baset = None
    tmp = None
    lset = None
    rset = None
    ans = None
    @staticmethod
    def insert(basis, num):
        num = jcast('int', num)
        i = jcast('int', Code06_IvanAndBurgers1.BIT)
        while (i >= 0):
            if (jcast('int', (num >> (i & 31))) == 1):
                if (basis[i] == 0):
                    basis[i] = jcast('int', num)
                    return
                num = jcast('int', jcast('int', (num ^ basis[i])))
            i = jcast('int', (i - 1))

    @staticmethod
    def clear(basis):
        i = jcast('int', 0)
        while (i <= Code06_IvanAndBurgers1.BIT):
            basis[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def maxEor(basis):
        ret = jcast('int', 0)
        i = jcast('int', Code06_IvanAndBurgers1.BIT)
        while (i >= 0):
            ret = jcast('int', jstatic('Math', 'max', ret, jcast('int', (ret ^ basis[i]))))
            i = jcast('int', (i - 1))
        return jcast('int', ret)

    @staticmethod
    def clone(b1, b2):
        i = jcast('int', 0)
        while (i <= Code06_IvanAndBurgers1.BIT):
            b1[i] = jcast('int', b2[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def merge(b1, b2):
        Code06_IvanAndBurgers1.clone(Code06_IvanAndBurgers1.tmp, b1)
        i = jcast('int', 0)
        while (i <= Code06_IvanAndBurgers1.BIT):
            Code06_IvanAndBurgers1.insert(Code06_IvanAndBurgers1.tmp, b2[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def compute(ql, qr, vl, vr):
        ql = jcast('int', ql)
        qr = jcast('int', qr)
        vl = jcast('int', vl)
        vr = jcast('int', vr)
        if (ql > qr):
            return
        if (vl == vr):
            i = jcast('int', ql)
            while (i <= qr):
                jset(Code06_IvanAndBurgers1.ans, Code06_IvanAndBurgers1.qid[i], Code06_IvanAndBurgers1.arr[vl])
                i = jcast('int', (i + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(vl, vr)) >> (1 & 31))))
            Code06_IvanAndBurgers1.clear(Code06_IvanAndBurgers1.baset[mid])
            Code06_IvanAndBurgers1.insert(Code06_IvanAndBurgers1.baset[mid], Code06_IvanAndBurgers1.arr[mid])
            i = jcast('int', jcast('int', (mid - 1)))
            while (i >= vl):
                Code06_IvanAndBurgers1.clone(Code06_IvanAndBurgers1.baset[i], Code06_IvanAndBurgers1.baset[jcast('int', jadd(i, 1))])
                Code06_IvanAndBurgers1.insert(Code06_IvanAndBurgers1.baset[i], Code06_IvanAndBurgers1.arr[i])
                i = jcast('int', (i - 1))
            i = jcast('int', jcast('int', jadd(mid, 1)))
            while (i <= vr):
                Code06_IvanAndBurgers1.clone(Code06_IvanAndBurgers1.baset[i], Code06_IvanAndBurgers1.baset[jcast('int', (i - 1))])
                Code06_IvanAndBurgers1.insert(Code06_IvanAndBurgers1.baset[i], Code06_IvanAndBurgers1.arr[i])
                i = jcast('int', (i + 1))
            lsiz = jcast('int', 0)
            rsiz = jcast('int', 0)
            id = 0
            i = jcast('int', ql)
            while (i <= qr):
                id = jcast('int', Code06_IvanAndBurgers1.qid[i])
                if (Code06_IvanAndBurgers1.r[id] < mid):
                    jset(Code06_IvanAndBurgers1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                else:
                    if (Code06_IvanAndBurgers1.l[id] > mid):
                        jset(Code06_IvanAndBurgers1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                    else:
                        Code06_IvanAndBurgers1.merge(Code06_IvanAndBurgers1.baset[Code06_IvanAndBurgers1.l[id]], Code06_IvanAndBurgers1.baset[Code06_IvanAndBurgers1.r[id]])
                        jset(Code06_IvanAndBurgers1.ans, id, Code06_IvanAndBurgers1.maxEor(Code06_IvanAndBurgers1.tmp))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= lsiz):
                Code06_IvanAndBurgers1.qid[jcast('int', (jcast('int', jadd(ql, i)) - 1))] = jcast('int', Code06_IvanAndBurgers1.lset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                Code06_IvanAndBurgers1.qid[jcast('int', (jcast('int', jadd(jcast('int', jadd(ql, lsiz)), i)) - 1))] = jcast('int', Code06_IvanAndBurgers1.rset[i])
                i = jcast('int', (i + 1))
            Code06_IvanAndBurgers1.compute(ql, jcast('int', (jcast('int', jadd(ql, lsiz)) - 1)), vl, mid)
            Code06_IvanAndBurgers1.compute(jcast('int', jadd(ql, lsiz)), jcast('int', (jcast('int', jadd(jcast('int', jadd(ql, lsiz)), rsiz)) - 1)), jcast('int', jadd(mid, 1)), vr)

    @staticmethod
    def main(args):
        in_ = Code06_IvanAndBurgers1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_IvanAndBurgers1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_IvanAndBurgers1.n):
            jset(Code06_IvanAndBurgers1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code06_IvanAndBurgers1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_IvanAndBurgers1.q):
            Code06_IvanAndBurgers1.qid[i] = jcast('int', i)
            jset(Code06_IvanAndBurgers1.l, i, jcall(in_, 'nextInt'))
            jset(Code06_IvanAndBurgers1.r, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code06_IvanAndBurgers1.compute(1, Code06_IvanAndBurgers1.q, 1, Code06_IvanAndBurgers1.n)
        i = jcast('int', 1)
        while (i <= Code06_IvanAndBurgers1.q):
            jcall(out, 'println', Code06_IvanAndBurgers1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

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
            raise TypeError("No matching overload for Code06_IvanAndBurgers1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_IvanAndBurgers1.MAXN = jcast('int', 500001)
Code06_IvanAndBurgers1.BIT = jcast('int', 21)
Code06_IvanAndBurgers1.n = jcast('int', 0)
Code06_IvanAndBurgers1.q = jcast('int', 0)
Code06_IvanAndBurgers1.arr = jarray('int', [Code06_IvanAndBurgers1.MAXN])
Code06_IvanAndBurgers1.qid = jarray('int', [Code06_IvanAndBurgers1.MAXN])
Code06_IvanAndBurgers1.l = jarray('int', [Code06_IvanAndBurgers1.MAXN])
Code06_IvanAndBurgers1.r = jarray('int', [Code06_IvanAndBurgers1.MAXN])
Code06_IvanAndBurgers1.baset = jarray('int', [Code06_IvanAndBurgers1.MAXN, jcast('int', jadd(Code06_IvanAndBurgers1.BIT, 1))])
Code06_IvanAndBurgers1.tmp = jarray('int', [jcast('int', jadd(Code06_IvanAndBurgers1.BIT, 1))])
Code06_IvanAndBurgers1.lset = jarray('int', [Code06_IvanAndBurgers1.MAXN])
Code06_IvanAndBurgers1.rset = jarray('int', [Code06_IvanAndBurgers1.MAXN])
Code06_IvanAndBurgers1.ans = jarray('int', [Code06_IvanAndBurgers1.MAXN])

if __name__ == '__main__':
    Code06_IvanAndBurgers1.main([])
