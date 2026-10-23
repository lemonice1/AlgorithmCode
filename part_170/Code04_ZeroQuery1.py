# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 累加和为0的最长子数组，Python版
# 给定一个长度为n的数组arr，其中只有1和-1两种值
# 一共有m条查询，格式 l r : 打印arr[l..r]范围上，累加和为0的最长子数组长度
# 1 <= n、m <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/SP20644
# 测试链接 : https://www.spoj.com/problems/ZQUERY/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_ZeroQuery1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'sorted': 'sorted', 'cntv': 'cntv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'br': 'br', 'first': 'first', 'mostRight': 'mostRight', 'maxDist': 'maxDist', 'ans': 'ans'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    query = None
    sorted = None
    cntv = 0
    blen = 0
    bnum = 0
    bi = None
    br = None
    first = None
    mostRight = None
    maxDist = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code04_ZeroQuery1.bi[a[0]] != Code04_ZeroQuery1.bi[b[0]]):
                return jcast('int', jcast('int', (Code04_ZeroQuery1.bi[a[0]] - Code04_ZeroQuery1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code04_ZeroQuery1.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code04_ZeroQuery1.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def force(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ret = jcast('int', 0)
        i = jcast('int', l)
        while (i <= r):
            if (Code04_ZeroQuery1.first[Code04_ZeroQuery1.arr[i]] == 0):
                jset(Code04_ZeroQuery1.first, Code04_ZeroQuery1.arr[i], i)
            else:
                ret = jcast('int', jstatic('Math', 'max', ret, jcast('int', (i - Code04_ZeroQuery1.first[Code04_ZeroQuery1.arr[i]]))))
            i = jcast('int', (i + 1))
        i = jcast('int', l)
        while (i <= r):
            jset(Code04_ZeroQuery1.first, Code04_ZeroQuery1.arr[i], 0)
            i = jcast('int', (i + 1))
        return jcast('int', ret)

    @staticmethod
    def addRight(idx):
        idx = jcast('int', idx)
        num = jcast('int', Code04_ZeroQuery1.arr[idx])
        Code04_ZeroQuery1.mostRight[num] = jcast('int', idx)
        if (Code04_ZeroQuery1.first[num] == 0):
            Code04_ZeroQuery1.first[num] = jcast('int', idx)
        Code04_ZeroQuery1.maxDist = jcast('int', jstatic('Math', 'max', Code04_ZeroQuery1.maxDist, jcast('int', (idx - Code04_ZeroQuery1.first[num]))))

    @staticmethod
    def addLeft(idx):
        idx = jcast('int', idx)
        num = jcast('int', Code04_ZeroQuery1.arr[idx])
        if (Code04_ZeroQuery1.mostRight[num] == 0):
            Code04_ZeroQuery1.mostRight[num] = jcast('int', idx)
        else:
            Code04_ZeroQuery1.maxDist = jcast('int', jstatic('Math', 'max', Code04_ZeroQuery1.maxDist, jcast('int', (Code04_ZeroQuery1.mostRight[num] - idx))))

    @staticmethod
    def delLeft(idx):
        idx = jcast('int', idx)
        num = jcast('int', Code04_ZeroQuery1.arr[idx])
        if (Code04_ZeroQuery1.mostRight[num] == idx):
            Code04_ZeroQuery1.mostRight[num] = jcast('int', 0)

    @staticmethod
    def compute():
        block = jcast('int', 1)
        qi = jcast('int', 1)
        while ((block <= Code04_ZeroQuery1.bnum) and (qi <= Code04_ZeroQuery1.m)):
            Code04_ZeroQuery1.maxDist = jcast('int', 0)
            jstatic('Arrays', 'fill', Code04_ZeroQuery1.first, 1, jcast('int', jadd(Code04_ZeroQuery1.cntv, 1)), 0)
            jstatic('Arrays', 'fill', Code04_ZeroQuery1.mostRight, 1, jcast('int', jadd(Code04_ZeroQuery1.cntv, 1)), 0)
            winl = jcast('int', jcast('int', jadd(Code04_ZeroQuery1.br[block], 1)))
            winr = jcast('int', Code04_ZeroQuery1.br[block])
            while ((qi <= Code04_ZeroQuery1.m) and (Code04_ZeroQuery1.bi[Code04_ZeroQuery1.query[qi][0]] == block)):
                jobl = jcast('int', Code04_ZeroQuery1.query[qi][0])
                jobr = jcast('int', Code04_ZeroQuery1.query[qi][1])
                id = jcast('int', Code04_ZeroQuery1.query[qi][2])
                if (jobr <= Code04_ZeroQuery1.br[block]):
                    jset(Code04_ZeroQuery1.ans, id, Code04_ZeroQuery1.force(jobl, jobr))
                else:
                    while (winr < jobr):
                        Code04_ZeroQuery1.addRight((winr := jcast('int', (winr + (1)))))
                    backup = jcast('int', Code04_ZeroQuery1.maxDist)
                    while (winl > jobl):
                        Code04_ZeroQuery1.addLeft((winl := jcast('int', (winl + (-1)))))
                    Code04_ZeroQuery1.ans[id] = jcast('int', Code04_ZeroQuery1.maxDist)
                    Code04_ZeroQuery1.maxDist = jcast('int', backup)
                    while (winl <= Code04_ZeroQuery1.br[block]):
                        Code04_ZeroQuery1.delLeft(((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2])
                qi = jcast('int', (qi + 1))
            block = jcast('int', (block + 1))

    @staticmethod
    def prepare():
        # 生成前缀和数组，下标从1开始，补充一个前缀长度为0的前缀和
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.n):
            Code04_ZeroQuery1.arr[i] = jcast('int', jcast('int', jadd(Code04_ZeroQuery1.arr[i], Code04_ZeroQuery1.arr[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        i = jcast('int', Code04_ZeroQuery1.n)
        while (i >= 0):
            Code04_ZeroQuery1.arr[jcast('int', jadd(i, 1))] = jcast('int', Code04_ZeroQuery1.arr[i])
            i = jcast('int', (i - 1))
        Code04_ZeroQuery1.n = jcast('int', (Code04_ZeroQuery1.n + 1))
        # 原来查询范围 l..r，对应前缀和查询范围 l-1..r
        # 现在前缀和平移了，所以对应前缀查询范围 l..r+1
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.m):
            ((_java_obj_2 := Code04_ZeroQuery1.query[i]), (_java_key_3 := 1), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4]
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.n):
            Code04_ZeroQuery1.sorted[i] = jcast('int', Code04_ZeroQuery1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_ZeroQuery1.sorted, 1, jcast('int', jadd(Code04_ZeroQuery1.n, 1)))
        Code04_ZeroQuery1.cntv = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code04_ZeroQuery1.n):
            if (Code04_ZeroQuery1.sorted[Code04_ZeroQuery1.cntv] != Code04_ZeroQuery1.sorted[i]):
                jset(Code04_ZeroQuery1.sorted, ((_java_obj_5 := Code04_ZeroQuery1), (_java_key_6 := 'cntv'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3], Code04_ZeroQuery1.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.n):
            jset(Code04_ZeroQuery1.arr, i, Code04_ZeroQuery1.kth(Code04_ZeroQuery1.arr[i]))
            i = jcast('int', (i + 1))
        Code04_ZeroQuery1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code04_ZeroQuery1.n)))
        Code04_ZeroQuery1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code04_ZeroQuery1.n, Code04_ZeroQuery1.blen)) - 1)), Code04_ZeroQuery1.blen)))
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.n):
            Code04_ZeroQuery1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code04_ZeroQuery1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.bnum):
            jset(Code04_ZeroQuery1.br, i, jstatic('Math', 'min', jcast('int', (i * Code04_ZeroQuery1.blen)), Code04_ZeroQuery1.n))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_ZeroQuery1.query, 1, jcast('int', jadd(Code04_ZeroQuery1.m, 1)), Code04_ZeroQuery1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code04_ZeroQuery1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_ZeroQuery1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_ZeroQuery1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.n):
            jset(Code04_ZeroQuery1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.m):
            jset(Code04_ZeroQuery1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code04_ZeroQuery1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code04_ZeroQuery1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code04_ZeroQuery1.prepare()
        Code04_ZeroQuery1.compute()
        i = jcast('int', 1)
        while (i <= Code04_ZeroQuery1.m):
            jcall(out, 'println', Code04_ZeroQuery1.ans[i])
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
            raise TypeError("No matching overload for Code04_ZeroQuery1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_ZeroQuery1.MAXN = jcast('int', 50002)
Code04_ZeroQuery1.MAXB = jcast('int', 301)
Code04_ZeroQuery1.n = jcast('int', 0)
Code04_ZeroQuery1.m = jcast('int', 0)
Code04_ZeroQuery1.arr = jarray('int', [Code04_ZeroQuery1.MAXN])
Code04_ZeroQuery1.query = jarray('int', [Code04_ZeroQuery1.MAXN, 3])
Code04_ZeroQuery1.sorted = jarray('int', [Code04_ZeroQuery1.MAXN])
Code04_ZeroQuery1.cntv = jcast('int', 0)
Code04_ZeroQuery1.blen = jcast('int', 0)
Code04_ZeroQuery1.bnum = jcast('int', 0)
Code04_ZeroQuery1.bi = jarray('int', [Code04_ZeroQuery1.MAXN])
Code04_ZeroQuery1.br = jarray('int', [Code04_ZeroQuery1.MAXB])
Code04_ZeroQuery1.first = jarray('int', [Code04_ZeroQuery1.MAXN])
Code04_ZeroQuery1.mostRight = jarray('int', [Code04_ZeroQuery1.MAXN])
Code04_ZeroQuery1.maxDist = jcast('int', 0)
Code04_ZeroQuery1.ans = jarray('int', [Code04_ZeroQuery1.MAXN])

if __name__ == '__main__':
    Code04_ZeroQuery1.main([])
