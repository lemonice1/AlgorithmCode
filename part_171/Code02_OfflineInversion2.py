# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 区间逆序对，Python版
# 给定一个长度为n的数组arr，如果i < j，并且arr[i] > arr[j]，那么(i,j)就是逆序对
# 一共有m条查询，格式为 l r : 打印arr[l..r]范围上，逆序对的数量
# 1 <= n、m <= 10^5
# 0 <= arr[i] <= 10^9
# 本题允许离线，讲解173，题目4，讲了在线查询区间逆序对，但是给定的数组为排列
# 测试链接 : https://www.luogu.com.cn/problem/P5047
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_OfflineInversion2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sorted': 'sorted', 'cntv': 'cntv', 'query': 'query', 'headl': 'headl', 'headr': 'headr', 'nextq': 'nextq', 'ql': 'ql', 'qr': 'qr', 'qop': 'qop', 'qid': 'qid', 'cntq': 'cntq', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'tree': 'tree', 'pre': 'pre', 'suf': 'suf', 'blockCnt': 'blockCnt', 'numCnt': 'numCnt', 'ans': 'ans'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    sorted = None
    cntv = 0
    query = None
    headl = None
    headr = None
    nextq = None
    ql = None
    qr = None
    qop = None
    qid = None
    cntq = 0
    # bi用于序列分块、值域分块，bl和br用于值域分块
    bi = None
    bl = None
    br = None
    # 树状数组
    tree = None
    # 前缀信息
    pre = None
    # 后缀信息
    suf = None
    # 整块增加的词频
    blockCnt = None
    # 单个数值的词频
    numCnt = None
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code02_OfflineInversion2.bi[a[0]] != Code02_OfflineInversion2.bi[b[0]]):
                return jcast('int', jcast('int', (Code02_OfflineInversion2.bi[a[0]] - Code02_OfflineInversion2.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code02_OfflineInversion2.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code02_OfflineInversion2.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code02_OfflineInversion2.cntv):
            Code02_OfflineInversion2.tree[i] = jcast('int', jcast('int', jadd(Code02_OfflineInversion2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code02_OfflineInversion2.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code02_OfflineInversion2.tree[i])))
            i = jcast('int', jcast('int', (i - Code02_OfflineInversion2.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def addLeftOffline(x, l, r, op, id):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        op = jcast('int', op)
        id = jcast('int', id)
        jset(Code02_OfflineInversion2.nextq, ((_java_obj_1 := Code02_OfflineInversion2), (_java_key_2 := 'cntq'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_OfflineInversion2.headl[x])
        Code02_OfflineInversion2.headl[x] = jcast('int', Code02_OfflineInversion2.cntq)
        Code02_OfflineInversion2.ql[Code02_OfflineInversion2.cntq] = jcast('int', l)
        Code02_OfflineInversion2.qr[Code02_OfflineInversion2.cntq] = jcast('int', r)
        Code02_OfflineInversion2.qop[Code02_OfflineInversion2.cntq] = jcast('int', op)
        Code02_OfflineInversion2.qid[Code02_OfflineInversion2.cntq] = jcast('int', id)

    @staticmethod
    def addRightOffline(x, l, r, op, id):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        op = jcast('int', op)
        id = jcast('int', id)
        jset(Code02_OfflineInversion2.nextq, ((_java_obj_4 := Code02_OfflineInversion2), (_java_key_5 := 'cntq'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code02_OfflineInversion2.headr[x])
        Code02_OfflineInversion2.headr[x] = jcast('int', Code02_OfflineInversion2.cntq)
        Code02_OfflineInversion2.ql[Code02_OfflineInversion2.cntq] = jcast('int', l)
        Code02_OfflineInversion2.qr[Code02_OfflineInversion2.cntq] = jcast('int', r)
        Code02_OfflineInversion2.qop[Code02_OfflineInversion2.cntq] = jcast('int', op)
        Code02_OfflineInversion2.qid[Code02_OfflineInversion2.cntq] = jcast('int', id)

    # 增加1 ~ val-1，这些数字的词频
    @staticmethod
    def addLeftCnt(val):
        val = jcast('int', val)
        b = jcast('int', 1)
        while (b <= jcast('int', (Code02_OfflineInversion2.bi[val] - 1))):
            Code02_OfflineInversion2.blockCnt[b] = jcast('long', (Code02_OfflineInversion2.blockCnt[b] + 1))
            b = jcast('int', (b + 1))
        i = jcast('int', Code02_OfflineInversion2.bl[Code02_OfflineInversion2.bi[val]])
        while (i < val):
            Code02_OfflineInversion2.numCnt[i] = jcast('long', (Code02_OfflineInversion2.numCnt[i] + 1))
            i = jcast('int', (i + 1))

    # 增加val+1 ~ cntv，这些数字的词频
    @staticmethod
    def addRightCnt(val):
        val = jcast('int', val)
        b = jcast('int', jcast('int', jadd(Code02_OfflineInversion2.bi[val], 1)))
        while (b <= Code02_OfflineInversion2.bi[Code02_OfflineInversion2.cntv]):
            Code02_OfflineInversion2.blockCnt[b] = jcast('long', (Code02_OfflineInversion2.blockCnt[b] + 1))
            b = jcast('int', (b + 1))
        i = jcast('int', jcast('int', jadd(val, 1)))
        while (i <= Code02_OfflineInversion2.br[Code02_OfflineInversion2.bi[val]]):
            Code02_OfflineInversion2.numCnt[i] = jcast('long', (Code02_OfflineInversion2.numCnt[i] + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def getCnt(val):
        val = jcast('int', val)
        return jcast('long', jcast('long', jadd(Code02_OfflineInversion2.blockCnt[Code02_OfflineInversion2.bi[val]], Code02_OfflineInversion2.numCnt[val])))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code02_OfflineInversion2.n):
            Code02_OfflineInversion2.sorted[i] = jcast('int', Code02_OfflineInversion2.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_OfflineInversion2.sorted, 1, jcast('int', jadd(Code02_OfflineInversion2.n, 1)))
        Code02_OfflineInversion2.cntv = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_OfflineInversion2.n):
            if (Code02_OfflineInversion2.sorted[Code02_OfflineInversion2.cntv] != Code02_OfflineInversion2.sorted[i]):
                jset(Code02_OfflineInversion2.sorted, ((_java_obj_7 := Code02_OfflineInversion2), (_java_key_8 := 'cntv'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code02_OfflineInversion2.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_OfflineInversion2.n):
            jset(Code02_OfflineInversion2.arr, i, Code02_OfflineInversion2.kth(Code02_OfflineInversion2.arr[i]))
            i = jcast('int', (i + 1))
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code02_OfflineInversion2.n)))
        bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code02_OfflineInversion2.n, blen)) - 1)), blen)))
        i = jcast('int', 1)
        while (i <= Code02_OfflineInversion2.n):
            Code02_OfflineInversion2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= bnum):
            Code02_OfflineInversion2.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * blen)), 1)))
            jset(Code02_OfflineInversion2.br, i, jstatic('Math', 'min', jcast('int', (i * blen)), Code02_OfflineInversion2.cntv))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_OfflineInversion2.query, 1, jcast('int', jadd(Code02_OfflineInversion2.m, 1)), Code02_OfflineInversion2.QueryCmp())

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code02_OfflineInversion2.n):
            jset(Code02_OfflineInversion2.pre, i, jcast('long', (jcast('long', jadd(Code02_OfflineInversion2.pre[jcast('int', (i - 1))], Code02_OfflineInversion2.sum(Code02_OfflineInversion2.cntv))) - Code02_OfflineInversion2.sum(Code02_OfflineInversion2.arr[i]))))
            Code02_OfflineInversion2.add(Code02_OfflineInversion2.arr[i], 1)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code02_OfflineInversion2.tree, 1, jcast('int', jadd(Code02_OfflineInversion2.cntv, 1)), 0)
        i = jcast('int', Code02_OfflineInversion2.n)
        while (i >= 1):
            jset(Code02_OfflineInversion2.suf, i, jcast('long', jadd(Code02_OfflineInversion2.suf[jcast('int', jadd(i, 1))], Code02_OfflineInversion2.sum(jcast('int', (Code02_OfflineInversion2.arr[i] - 1))))))
            Code02_OfflineInversion2.add(Code02_OfflineInversion2.arr[i], 1)
            i = jcast('int', (i - 1))
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_OfflineInversion2.m):
            jobl = jcast('int', Code02_OfflineInversion2.query[i][0])
            jobr = jcast('int', Code02_OfflineInversion2.query[i][1])
            id = jcast('int', Code02_OfflineInversion2.query[i][2])
            if (winr < jobr):
                Code02_OfflineInversion2.addLeftOffline(jcast('int', (winl - 1)), jcast('int', jadd(winr, 1)), jobr, jcast('int', (-1)), id)
                Code02_OfflineInversion2.ans[id] = jcast('long', jcast('long', jadd(Code02_OfflineInversion2.ans[id], jcast('long', (Code02_OfflineInversion2.pre[jobr] - Code02_OfflineInversion2.pre[winr])))))
            if (winr > jobr):
                Code02_OfflineInversion2.addLeftOffline(jcast('int', (winl - 1)), jcast('int', jadd(jobr, 1)), winr, 1, id)
                Code02_OfflineInversion2.ans[id] = jcast('long', jcast('long', (Code02_OfflineInversion2.ans[id] - jcast('long', (Code02_OfflineInversion2.pre[winr] - Code02_OfflineInversion2.pre[jobr])))))
            winr = jcast('int', jobr)
            if (winl > jobl):
                Code02_OfflineInversion2.addRightOffline(jcast('int', jadd(winr, 1)), jobl, jcast('int', (winl - 1)), jcast('int', (-1)), id)
                Code02_OfflineInversion2.ans[id] = jcast('long', jcast('long', jadd(Code02_OfflineInversion2.ans[id], jcast('long', (Code02_OfflineInversion2.suf[jobl] - Code02_OfflineInversion2.suf[winl])))))
            if (winl < jobl):
                Code02_OfflineInversion2.addRightOffline(jcast('int', jadd(winr, 1)), winl, jcast('int', (jobl - 1)), 1, id)
                Code02_OfflineInversion2.ans[id] = jcast('long', jcast('long', (Code02_OfflineInversion2.ans[id] - jcast('long', (Code02_OfflineInversion2.suf[winl] - Code02_OfflineInversion2.suf[jobl])))))
            winl = jcast('int', jobl)
            i = jcast('int', (i + 1))
        x = jcast('int', 0)
        while (x <= Code02_OfflineInversion2.n):
            if (x >= 1):
                Code02_OfflineInversion2.addLeftCnt(Code02_OfflineInversion2.arr[x])
            q = jcast('int', Code02_OfflineInversion2.headl[x])
            while (q > 0):
                l = jcast('int', Code02_OfflineInversion2.ql[q])
                r = jcast('int', Code02_OfflineInversion2.qr[q])
                op = jcast('int', Code02_OfflineInversion2.qop[q])
                id = jcast('int', Code02_OfflineInversion2.qid[q])
                ret = jcast('long', 0)
                j = jcast('int', l)
                while (j <= r):
                    ret = jcast('long', jcast('long', jadd(ret, Code02_OfflineInversion2.getCnt(Code02_OfflineInversion2.arr[j]))))
                    j = jcast('int', (j + 1))
                Code02_OfflineInversion2.ans[id] = jcast('long', jcast('long', jadd(Code02_OfflineInversion2.ans[id], jcast('long', (ret * op)))))
                q = jcast('int', Code02_OfflineInversion2.nextq[q])
            x = jcast('int', (x + 1))
        jstatic('Arrays', 'fill', Code02_OfflineInversion2.blockCnt, 0)
        jstatic('Arrays', 'fill', Code02_OfflineInversion2.numCnt, 0)
        x = jcast('int', jcast('int', jadd(Code02_OfflineInversion2.n, 1)))
        while (x >= 1):
            if (x <= Code02_OfflineInversion2.n):
                Code02_OfflineInversion2.addRightCnt(Code02_OfflineInversion2.arr[x])
            q = jcast('int', Code02_OfflineInversion2.headr[x])
            while (q > 0):
                l = jcast('int', Code02_OfflineInversion2.ql[q])
                r = jcast('int', Code02_OfflineInversion2.qr[q])
                op = jcast('int', Code02_OfflineInversion2.qop[q])
                id = jcast('int', Code02_OfflineInversion2.qid[q])
                ret = jcast('long', 0)
                j = jcast('int', l)
                while (j <= r):
                    ret = jcast('long', jcast('long', jadd(ret, Code02_OfflineInversion2.getCnt(Code02_OfflineInversion2.arr[j]))))
                    j = jcast('int', (j + 1))
                Code02_OfflineInversion2.ans[id] = jcast('long', jcast('long', jadd(Code02_OfflineInversion2.ans[id], jcast('long', (ret * op)))))
                q = jcast('int', Code02_OfflineInversion2.nextq[q])
            x = jcast('int', (x - 1))

    @staticmethod
    def main(args):
        in_ = Code02_OfflineInversion2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_OfflineInversion2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_OfflineInversion2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_OfflineInversion2.n):
            jset(Code02_OfflineInversion2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_OfflineInversion2.m):
            jset(Code02_OfflineInversion2.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code02_OfflineInversion2.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code02_OfflineInversion2.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code02_OfflineInversion2.prepare()
        Code02_OfflineInversion2.compute()
        i = jcast('int', 2)
        while (i <= Code02_OfflineInversion2.m):
            ((_java_obj_10 := Code02_OfflineInversion2.ans), (_java_key_11 := Code02_OfflineInversion2.query[i][2]), jset(_java_obj_10, _java_key_11, jcast('long', jadd(jget(_java_obj_10, _java_key_11), Code02_OfflineInversion2.ans[Code02_OfflineInversion2.query[jcast('int', (i - 1))][2]]))))[2]
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_OfflineInversion2.m):
            jcall(out, 'println', Code02_OfflineInversion2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]])

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
            raise TypeError("No matching overload for Code02_OfflineInversion2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_OfflineInversion2.MAXN = jcast('int', 100002)
Code02_OfflineInversion2.MAXB = jcast('int', 401)
Code02_OfflineInversion2.n = jcast('int', 0)
Code02_OfflineInversion2.m = jcast('int', 0)
Code02_OfflineInversion2.arr = jarray('int', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.sorted = jarray('int', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.cntv = jcast('int', 0)
Code02_OfflineInversion2.query = jarray('int', [Code02_OfflineInversion2.MAXN, 3])
Code02_OfflineInversion2.headl = jarray('int', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.headr = jarray('int', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.nextq = jarray('int', [jcast('int', (Code02_OfflineInversion2.MAXN << (1 & 31)))])
Code02_OfflineInversion2.ql = jarray('int', [jcast('int', (Code02_OfflineInversion2.MAXN << (1 & 31)))])
Code02_OfflineInversion2.qr = jarray('int', [jcast('int', (Code02_OfflineInversion2.MAXN << (1 & 31)))])
Code02_OfflineInversion2.qop = jarray('int', [jcast('int', (Code02_OfflineInversion2.MAXN << (1 & 31)))])
Code02_OfflineInversion2.qid = jarray('int', [jcast('int', (Code02_OfflineInversion2.MAXN << (1 & 31)))])
Code02_OfflineInversion2.cntq = jcast('int', 0)
Code02_OfflineInversion2.bi = jarray('int', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.bl = jarray('int', [Code02_OfflineInversion2.MAXB])
Code02_OfflineInversion2.br = jarray('int', [Code02_OfflineInversion2.MAXB])
Code02_OfflineInversion2.tree = jarray('int', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.pre = jarray('long', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.suf = jarray('long', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.blockCnt = jarray('long', [Code02_OfflineInversion2.MAXB])
Code02_OfflineInversion2.numCnt = jarray('long', [Code02_OfflineInversion2.MAXN])
Code02_OfflineInversion2.ans = jarray('long', [Code02_OfflineInversion2.MAXN])

if __name__ == '__main__':
    Code02_OfflineInversion2.main([])
