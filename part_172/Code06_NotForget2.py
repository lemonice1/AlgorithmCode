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

# 盼君勿忘，Python版
# 一个序列中每种数字只保留一个，得到的累加和，叫做去重累加和
# 给定一个长度为n的数组arr，接下来是m条查询，查询格式如下
# 查询 l r p : arr[l..r]范围上，每个子序列的去重累加和，都累加起来 % p 的结果打印
# 1 <= n、m、arr[i] <= 10^5
# 1 <= p <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P5072
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_NotForget2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'bi': 'bi', 'head': 'head', 'last': 'last', 'next': 'next', 'cnt': 'cnt', 'sum': 'sum', 'smlPower': 'smlPower', 'bigPower': 'bigPower', 'ans': 'ans'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    # 查询任务，l、r、p、id
    query = None
    bi = None
    # 有效次数桶组成的双向链表
    # 有数字进入次数桶，该次数桶才进入链表，链表内部不需要有序组织
    head = 0
    last = None
    next = None
    # cnt[v] = c，表示v这个数出现了c次，也可以说v在c次桶里
    # sum[c] = x，表示c次桶内的数字，每种数字只统计一次，累加和为x
    cnt = None
    sum = None
    # 光速幂
    # 假设[l..r]范围长度len，blockLen为块的长度，blockNum为块的数量
    # smlPower[i]，表示p的i次方的值，i <= blockLen
    # bigPower[i]，表示p的(i * blockLen)次方的值，i <= blockNum
    smlPower = None
    bigPower = None
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code06_NotForget2.bi[a[0]] != Code06_NotForget2.bi[b[0]]):
                return jcast('int', jcast('int', (Code06_NotForget2.bi[a[0]] - Code06_NotForget2.bi[b[0]])))
            if (jcast('int', (Code06_NotForget2.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def addNode(x):
        x = jcast('int', x)
        Code06_NotForget2.last[Code06_NotForget2.head] = jcast('int', x)
        Code06_NotForget2.next[x] = jcast('int', Code06_NotForget2.head)
        Code06_NotForget2.head = jcast('int', x)

    @staticmethod
    def delNode(x):
        x = jcast('int', x)
        if (x == Code06_NotForget2.head):
            Code06_NotForget2.head = jcast('int', Code06_NotForget2.next[Code06_NotForget2.head])
            jset(Code06_NotForget2.last, Code06_NotForget2.head, jset(Code06_NotForget2.next, x, 0))
        else:
            jset(Code06_NotForget2.next, Code06_NotForget2.last[x], Code06_NotForget2.next[x])
            jset(Code06_NotForget2.last, Code06_NotForget2.next[x], Code06_NotForget2.last[x])
            jset(Code06_NotForget2.last, x, jset(Code06_NotForget2.next, x, 0))

    @staticmethod
    def add(num):
        num = jcast('int', num)
        if (Code06_NotForget2.cnt[num] > 0):
            ((_java_obj_1 := Code06_NotForget2.sum), (_java_key_2 := Code06_NotForget2.cnt[num]), jset(_java_obj_1, _java_key_2, jcast('long', (jget(_java_obj_1, _java_key_2) - num))))[2]
        if ((Code06_NotForget2.cnt[num] > 0) and (Code06_NotForget2.sum[Code06_NotForget2.cnt[num]] == 0)):
            Code06_NotForget2.delNode(Code06_NotForget2.cnt[num])
        Code06_NotForget2.cnt[num] = jcast('int', (Code06_NotForget2.cnt[num] + 1))
        if ((Code06_NotForget2.cnt[num] > 0) and (Code06_NotForget2.sum[Code06_NotForget2.cnt[num]] == 0)):
            Code06_NotForget2.addNode(Code06_NotForget2.cnt[num])
        if (Code06_NotForget2.cnt[num] > 0):
            ((_java_obj_3 := Code06_NotForget2.sum), (_java_key_4 := Code06_NotForget2.cnt[num]), jset(_java_obj_3, _java_key_4, jcast('long', jadd(jget(_java_obj_3, _java_key_4), num))))[2]

    @staticmethod
    def del_(num):
        num = jcast('int', num)
        if (Code06_NotForget2.cnt[num] > 0):
            ((_java_obj_5 := Code06_NotForget2.sum), (_java_key_6 := Code06_NotForget2.cnt[num]), jset(_java_obj_5, _java_key_6, jcast('long', (jget(_java_obj_5, _java_key_6) - num))))[2]
        if ((Code06_NotForget2.cnt[num] > 0) and (Code06_NotForget2.sum[Code06_NotForget2.cnt[num]] == 0)):
            Code06_NotForget2.delNode(Code06_NotForget2.cnt[num])
        Code06_NotForget2.cnt[num] = jcast('int', (Code06_NotForget2.cnt[num] - 1))
        if ((Code06_NotForget2.cnt[num] > 0) and (Code06_NotForget2.sum[Code06_NotForget2.cnt[num]] == 0)):
            Code06_NotForget2.addNode(Code06_NotForget2.cnt[num])
        if (Code06_NotForget2.cnt[num] > 0):
            ((_java_obj_7 := Code06_NotForget2.sum), (_java_key_8 := Code06_NotForget2.cnt[num]), jset(_java_obj_7, _java_key_8, jcast('long', jadd(jget(_java_obj_7, _java_key_8), num))))[2]

    @staticmethod
    def setAns(len, p, id):
        len = jcast('int', len)
        p = jcast('int', p)
        id = jcast('int', id)
        # 光速幂
        # 构建smlPower和bigPower
        blockLen = jcast('int', jcast('int', jstatic('Math', 'sqrt', len)))
        blockNum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(len, blockLen)) - 1)), blockLen)))
        Code06_NotForget2.smlPower[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= blockLen):
            Code06_NotForget2.smlPower[i] = jcast('long', jcast('long', jmod(jcast('long', (Code06_NotForget2.smlPower[jcast('int', (i - 1))] << (1 & 63))), p)))
            i = jcast('int', (i + 1))
        Code06_NotForget2.bigPower[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= blockNum):
            Code06_NotForget2.bigPower[i] = jcast('long', jcast('long', jmod(jcast('long', (Code06_NotForget2.bigPower[jcast('int', (i - 1))] * Code06_NotForget2.smlPower[blockLen])), p)))
            i = jcast('int', (i + 1))
        # t次桶的贡献 = [2的len次方 - 2的(len-t)次方] * sum[t]
        res = jcast('long', 0)
        p1 = 0
        p2 = 0
        tmp = 0
        p1 = jcast('long', jcast('long', jmod(jcast('long', (Code06_NotForget2.bigPower[jcast('int', jdiv(len, blockLen))] * Code06_NotForget2.smlPower[jcast('int', jmod(len, blockLen))])), p)))
        t = jcast('int', Code06_NotForget2.head)
        while (t > 0):
            p2 = jcast('long', jcast('long', jmod(jcast('long', (Code06_NotForget2.bigPower[jcast('int', jdiv(jcast('int', (len - t)), blockLen))] * Code06_NotForget2.smlPower[jcast('int', jmod(jcast('int', (len - t)), blockLen))])), p)))
            tmp = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', (p1 - p2)) * Code06_NotForget2.sum[t])), p)))
            res = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(jcast('long', jadd(res, tmp)), p)), p)), p)))
            t = jcast('int', Code06_NotForget2.next[t])
        Code06_NotForget2.ans[id] = jcast('long', res)

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_NotForget2.m):
            jobl = jcast('int', Code06_NotForget2.query[i][0])
            jobr = jcast('int', Code06_NotForget2.query[i][1])
            jobp = jcast('int', Code06_NotForget2.query[i][2])
            id = jcast('int', Code06_NotForget2.query[i][3])
            while (winl > jobl):
                Code06_NotForget2.add(Code06_NotForget2.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code06_NotForget2.add(Code06_NotForget2.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code06_NotForget2.del_(Code06_NotForget2.arr[((_java_old_9 := winl), (winl := jcast('int', (winl + (1)))), _java_old_9)[2]])
            while (winr > jobr):
                Code06_NotForget2.del_(Code06_NotForget2.arr[((_java_old_10 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_10)[2]])
            Code06_NotForget2.setAns(jcast('int', jadd(jcast('int', (jobr - jobl)), 1)), jobp, id)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code06_NotForget2.n)))
        i = jcast('int', 1)
        while (i <= Code06_NotForget2.n):
            Code06_NotForget2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_NotForget2.query, 1, jcast('int', jadd(Code06_NotForget2.m, 1)), Code06_NotForget2.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code06_NotForget2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_NotForget2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_NotForget2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_NotForget2.n):
            jset(Code06_NotForget2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_NotForget2.m):
            jset(Code06_NotForget2.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code06_NotForget2.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code06_NotForget2.query[i], 2, jcall(in_, 'nextInt'))
            jset(Code06_NotForget2.query[i], 3, i)
            i = jcast('int', (i + 1))
        Code06_NotForget2.prepare()
        Code06_NotForget2.compute()
        i = jcast('int', 1)
        while (i <= Code06_NotForget2.m):
            jcall(out, 'println', Code06_NotForget2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code06_NotForget2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_NotForget2.MAXN = jcast('int', 100001)
Code06_NotForget2.MAXB = jcast('int', 401)
Code06_NotForget2.n = jcast('int', 0)
Code06_NotForget2.m = jcast('int', 0)
Code06_NotForget2.arr = jarray('int', [Code06_NotForget2.MAXN])
Code06_NotForget2.query = jarray('int', [Code06_NotForget2.MAXN, 4])
Code06_NotForget2.bi = jarray('int', [Code06_NotForget2.MAXN])
Code06_NotForget2.head = jcast('int', 0)
Code06_NotForget2.last = jarray('int', [Code06_NotForget2.MAXN])
Code06_NotForget2.next = jarray('int', [Code06_NotForget2.MAXN])
Code06_NotForget2.cnt = jarray('int', [Code06_NotForget2.MAXN])
Code06_NotForget2.sum = jarray('long', [Code06_NotForget2.MAXN])
Code06_NotForget2.smlPower = jarray('long', [Code06_NotForget2.MAXB])
Code06_NotForget2.bigPower = jarray('long', [Code06_NotForget2.MAXB])
Code06_NotForget2.ans = jarray('long', [Code06_NotForget2.MAXN])

if __name__ == '__main__':
    Code06_NotForget2.main([])
