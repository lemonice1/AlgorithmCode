# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 区间Abbi值，Python版
# 给定一个长度为n的数组arr，区间Abbi值的定义如下
# 如果arr[l..r]包含数字v，并且v是第k小，那么这个数字的Abbi值 = v * k
# 区间Abbi值 = 区间内所有数字Abbi值的累加和
# 比如[1, 2, 2, 3]的Abbi值 = 1 * 1 + 2 * 2 + 2 * 2 + 3 * 4 = 21
# 一共有m条查询，格式为 l r : 打印arr[l..r]的区间Abbi值
# 1 <= n、m <= 5 * 10^5
# 1 <= arr[i] <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5501
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Abbi2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'preSum': 'preSum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'query': 'query', 'headq': 'headq', 'nextq': 'nextq', 'ql': 'ql', 'qr': 'qr', 'qop': 'qop', 'qid': 'qid', 'cntq': 'cntq', 'treeCnt': 'treeCnt', 'treeSum': 'treeSum', 'pre': 'pre', 'blockLessCnt': 'blockLessCnt', 'numLessCnt': 'numLessCnt', 'blockMoreSum': 'blockMoreSum', 'numMoreSum': 'numMoreSum', 'ans': 'ans'}
    MAXN = 0
    MAXV = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    preSum = None
    # 序列分块 + 值域分块
    bi = None
    bl = None
    br = None
    # 莫队任务 + 二次离线任务(x, l, r, op)
    query = None
    headq = None
    nextq = None
    ql = None
    qr = None
    qop = None
    qid = None
    cntq = 0
    # 值域树状数组，统计<x的个数
    treeCnt = None
    # 值域树状数组，统计>x所有数的累加和
    treeSum = None
    # 前缀信息
    pre = None
    # 值域分块，统计<x的个数
    blockLessCnt = None
    numLessCnt = None
    # 值域分块，统计>x所有数的累加和
    blockMoreSum = None
    numMoreSum = None
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code03_Abbi2.bi[a[0]] != Code03_Abbi2.bi[b[0]]):
                return jcast('int', jcast('int', (Code03_Abbi2.bi[a[0]] - Code03_Abbi2.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def addOffline(x, l, r, op, id):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        op = jcast('int', op)
        id = jcast('int', id)
        jset(Code03_Abbi2.nextq, ((_java_obj_1 := Code03_Abbi2), (_java_key_2 := 'cntq'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Abbi2.headq[x])
        Code03_Abbi2.headq[x] = jcast('int', Code03_Abbi2.cntq)
        Code03_Abbi2.ql[Code03_Abbi2.cntq] = jcast('int', l)
        Code03_Abbi2.qr[Code03_Abbi2.cntq] = jcast('int', r)
        Code03_Abbi2.qop[Code03_Abbi2.cntq] = jcast('int', op)
        Code03_Abbi2.qid[Code03_Abbi2.cntq] = jcast('int', id)

    @staticmethod
    def lowbit(x):
        x = jcast('int', x)
        return jcast('int', jcast('int', (x & jcast('int', (-x)))))

    @staticmethod
    def add(tree, x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        while (x <= Code03_Abbi2.MAXV):
            tree[x] = jcast('long', jcast('long', jadd(tree[x], v)))
            x = jcast('int', jcast('int', jadd(x, Code03_Abbi2.lowbit(x))))

    @staticmethod
    def sum(tree, x):
        x = jcast('int', x)
        ret = jcast('long', 0)
        while (x > 0):
            ret = jcast('long', jcast('long', jadd(ret, tree[x])))
            x = jcast('int', jcast('int', (x - Code03_Abbi2.lowbit(x))))
        return jcast('long', ret)

    # 执行二次离线的过程中，加入数字val，修改相关信息
    @staticmethod
    def addVal(val):
        val = jcast('int', val)
        b = jcast('int', jcast('int', jadd(Code03_Abbi2.bi[val], 1)))
        while (b <= Code03_Abbi2.bi[Code03_Abbi2.MAXV]):
            Code03_Abbi2.blockLessCnt[b] = jcast('int', (Code03_Abbi2.blockLessCnt[b] + 1))
            b = jcast('int', (b + 1))
        i = jcast('int', jcast('int', jadd(val, 1)))
        while (i <= Code03_Abbi2.br[Code03_Abbi2.bi[val]]):
            Code03_Abbi2.numLessCnt[i] = jcast('int', (Code03_Abbi2.numLessCnt[i] + 1))
            i = jcast('int', (i + 1))
        b = jcast('int', 1)
        while (b <= jcast('int', (Code03_Abbi2.bi[val] - 1))):
            Code03_Abbi2.blockMoreSum[b] = jcast('long', jcast('long', jadd(Code03_Abbi2.blockMoreSum[b], val)))
            b = jcast('int', (b + 1))
        i = jcast('int', Code03_Abbi2.bl[Code03_Abbi2.bi[val]])
        while (i < val):
            Code03_Abbi2.numMoreSum[i] = jcast('long', jcast('long', jadd(Code03_Abbi2.numMoreSum[i], val)))
            i = jcast('int', (i + 1))

    # 查询<x的个数
    @staticmethod
    def lessCnt(x):
        x = jcast('int', x)
        return jcast('int', jcast('int', jadd(Code03_Abbi2.blockLessCnt[Code03_Abbi2.bi[x]], Code03_Abbi2.numLessCnt[x])))

    # 查询>x的所有数累加和
    @staticmethod
    def moreSum(x):
        x = jcast('int', x)
        return jcast('long', jcast('long', jadd(Code03_Abbi2.blockMoreSum[Code03_Abbi2.bi[x]], Code03_Abbi2.numMoreSum[x])))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code03_Abbi2.n):
            Code03_Abbi2.preSum[i] = jcast('long', jcast('long', jadd(Code03_Abbi2.preSum[jcast('int', (i - 1))], Code03_Abbi2.arr[i])))
            i = jcast('int', (i + 1))
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code03_Abbi2.MAXV)))
        bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code03_Abbi2.MAXV, blen)) - 1)), blen)))
        i = jcast('int', 1)
        while (i <= Code03_Abbi2.MAXV):
            Code03_Abbi2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= bnum):
            Code03_Abbi2.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * blen)), 1)))
            jset(Code03_Abbi2.br, i, jstatic('Math', 'min', jcast('int', (i * blen)), Code03_Abbi2.MAXV))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_Abbi2.query, 1, jcast('int', jadd(Code03_Abbi2.m, 1)), Code03_Abbi2.QueryCmp())

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code03_Abbi2.n):
            jset(Code03_Abbi2.pre, i, jcast('long', (jcast('long', jadd(jcast('long', jadd(Code03_Abbi2.pre[jcast('int', (i - 1))], jcast('long', (Code03_Abbi2.sum(Code03_Abbi2.treeCnt, jcast('int', (Code03_Abbi2.arr[i] - 1))) * Code03_Abbi2.arr[i])))), Code03_Abbi2.sum(Code03_Abbi2.treeSum, Code03_Abbi2.MAXV))) - Code03_Abbi2.sum(Code03_Abbi2.treeSum, Code03_Abbi2.arr[i]))))
            Code03_Abbi2.add(Code03_Abbi2.treeCnt, Code03_Abbi2.arr[i], 1)
            Code03_Abbi2.add(Code03_Abbi2.treeSum, Code03_Abbi2.arr[i], Code03_Abbi2.arr[i])
            i = jcast('int', (i + 1))
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_Abbi2.m):
            jobl = jcast('int', Code03_Abbi2.query[i][0])
            jobr = jcast('int', Code03_Abbi2.query[i][1])
            id = jcast('int', Code03_Abbi2.query[i][2])
            if (winr < jobr):
                Code03_Abbi2.addOffline(jcast('int', (winl - 1)), jcast('int', jadd(winr, 1)), jobr, jcast('int', (-1)), id)
                Code03_Abbi2.ans[id] = jcast('long', jcast('long', jadd(Code03_Abbi2.ans[id], jcast('long', (Code03_Abbi2.pre[jobr] - Code03_Abbi2.pre[winr])))))
            if (winr > jobr):
                Code03_Abbi2.addOffline(jcast('int', (winl - 1)), jcast('int', jadd(jobr, 1)), winr, 1, id)
                Code03_Abbi2.ans[id] = jcast('long', jcast('long', (Code03_Abbi2.ans[id] - jcast('long', (Code03_Abbi2.pre[winr] - Code03_Abbi2.pre[jobr])))))
            winr = jcast('int', jobr)
            if (winl > jobl):
                Code03_Abbi2.addOffline(winr, jobl, jcast('int', (winl - 1)), 1, id)
                Code03_Abbi2.ans[id] = jcast('long', jcast('long', (Code03_Abbi2.ans[id] - jcast('long', (Code03_Abbi2.pre[jcast('int', (winl - 1))] - Code03_Abbi2.pre[jcast('int', (jobl - 1))])))))
            if (winl < jobl):
                Code03_Abbi2.addOffline(winr, winl, jcast('int', (jobl - 1)), jcast('int', (-1)), id)
                Code03_Abbi2.ans[id] = jcast('long', jcast('long', jadd(Code03_Abbi2.ans[id], jcast('long', (Code03_Abbi2.pre[jcast('int', (jobl - 1))] - Code03_Abbi2.pre[jcast('int', (winl - 1))])))))
            winl = jcast('int', jobl)
            i = jcast('int', (i + 1))
        tmp = 0
        x = jcast('int', 0)
        while (x <= Code03_Abbi2.n):
            if (x >= 1):
                Code03_Abbi2.addVal(Code03_Abbi2.arr[x])
            q = jcast('int', Code03_Abbi2.headq[x])
            while (q > 0):
                l = jcast('int', Code03_Abbi2.ql[q])
                r = jcast('int', Code03_Abbi2.qr[q])
                op = jcast('int', Code03_Abbi2.qop[q])
                id = jcast('int', Code03_Abbi2.qid[q])
                j = jcast('int', l)
                while (j <= r):
                    tmp = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', Code03_Abbi2.lessCnt(Code03_Abbi2.arr[j])) * Code03_Abbi2.arr[j])), Code03_Abbi2.moreSum(Code03_Abbi2.arr[j]))))
                    if (op == 1):
                        Code03_Abbi2.ans[id] = jcast('long', jcast('long', jadd(Code03_Abbi2.ans[id], tmp)))
                    else:
                        Code03_Abbi2.ans[id] = jcast('long', jcast('long', (Code03_Abbi2.ans[id] - tmp)))
                    j = jcast('int', (j + 1))
                q = jcast('int', Code03_Abbi2.nextq[q])
            x = jcast('int', (x + 1))

    @staticmethod
    def main(args):
        in_ = Code03_Abbi2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Abbi2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_Abbi2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_Abbi2.n):
            jset(Code03_Abbi2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Abbi2.m):
            jset(Code03_Abbi2.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code03_Abbi2.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code03_Abbi2.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code03_Abbi2.prepare()
        Code03_Abbi2.compute()
        # 加工前缀和
        i = jcast('int', 2)
        while (i <= Code03_Abbi2.m):
            ((_java_obj_4 := Code03_Abbi2.ans), (_java_key_5 := Code03_Abbi2.query[i][2]), jset(_java_obj_4, _java_key_5, jcast('long', jadd(jget(_java_obj_4, _java_key_5), Code03_Abbi2.ans[Code03_Abbi2.query[jcast('int', (i - 1))][2]]))))[2]
            i = jcast('int', (i + 1))
        # 贡献是修正过的概念，现在补偿回来
        i = jcast('int', 1)
        while (i <= Code03_Abbi2.m):
            ((_java_obj_6 := Code03_Abbi2.ans), (_java_key_7 := Code03_Abbi2.query[i][2]), jset(_java_obj_6, _java_key_7, jcast('long', jadd(jget(_java_obj_6, _java_key_7), jcast('long', (Code03_Abbi2.preSum[Code03_Abbi2.query[i][1]] - Code03_Abbi2.preSum[jcast('int', (Code03_Abbi2.query[i][0] - 1))]))))))[2]
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Abbi2.m):
            jcall(out, 'println', Code03_Abbi2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_8 := self), (_java_key_9 := 'ptr'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

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
            raise TypeError("No matching overload for Code03_Abbi2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Abbi2.MAXN = jcast('int', 500001)
Code03_Abbi2.MAXV = jcast('int', 100000)
Code03_Abbi2.MAXB = jcast('int', 401)
Code03_Abbi2.n = jcast('int', 0)
Code03_Abbi2.m = jcast('int', 0)
Code03_Abbi2.arr = jarray('int', [Code03_Abbi2.MAXN])
Code03_Abbi2.preSum = jarray('long', [Code03_Abbi2.MAXN])
Code03_Abbi2.bi = jarray('int', [Code03_Abbi2.MAXN])
Code03_Abbi2.bl = jarray('int', [Code03_Abbi2.MAXB])
Code03_Abbi2.br = jarray('int', [Code03_Abbi2.MAXB])
Code03_Abbi2.query = jarray('int', [Code03_Abbi2.MAXN, 3])
Code03_Abbi2.headq = jarray('int', [Code03_Abbi2.MAXN])
Code03_Abbi2.nextq = jarray('int', [jcast('int', (Code03_Abbi2.MAXN << (1 & 31)))])
Code03_Abbi2.ql = jarray('int', [jcast('int', (Code03_Abbi2.MAXN << (1 & 31)))])
Code03_Abbi2.qr = jarray('int', [jcast('int', (Code03_Abbi2.MAXN << (1 & 31)))])
Code03_Abbi2.qop = jarray('int', [jcast('int', (Code03_Abbi2.MAXN << (1 & 31)))])
Code03_Abbi2.qid = jarray('int', [jcast('int', (Code03_Abbi2.MAXN << (1 & 31)))])
Code03_Abbi2.cntq = jcast('int', 0)
Code03_Abbi2.treeCnt = jarray('long', [jcast('int', jadd(Code03_Abbi2.MAXV, 1))])
Code03_Abbi2.treeSum = jarray('long', [jcast('int', jadd(Code03_Abbi2.MAXV, 1))])
Code03_Abbi2.pre = jarray('long', [Code03_Abbi2.MAXN])
Code03_Abbi2.blockLessCnt = jarray('int', [Code03_Abbi2.MAXB])
Code03_Abbi2.numLessCnt = jarray('int', [Code03_Abbi2.MAXN])
Code03_Abbi2.blockMoreSum = jarray('long', [Code03_Abbi2.MAXB])
Code03_Abbi2.numMoreSum = jarray('long', [Code03_Abbi2.MAXN])
Code03_Abbi2.ans = jarray('long', [Code03_Abbi2.MAXN])

if __name__ == '__main__':
    Code03_Abbi2.main([])
