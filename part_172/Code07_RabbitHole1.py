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

# 掉进兔子洞，Python版
# 三个区间同时出现的数，一个一个删掉，直到无法再删，剩下数字的个数叫做 剩余个数
# A = [1 2 2 3 3 3]    B = [1 2 2 3 3 3]    C = [1 1 2 3 3]
# 删除的过程为，一起删掉一个1、一起删掉一个2、一起删掉2个3，然后状况为
# A = [2 3]    B = [2 3]    C = [1]    剩余个数为5
# 给定一个长度为n的数组arr，下来有m条查询，格式如下
# 查询 l1 r1 l2 r2 l3 r3 : 给定了三个区间，打印剩余个数
# 1 <= n、m <= 10^5
# 1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4688
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_RabbitHole1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'sorted': 'sorted', 'bi': 'bi', 'cnt': 'cnt', 'curSet': 'curSet', 'hasSet': 'hasSet', 'bitSet': 'bitSet', 'ans': 'ans'}
    class BitSet:
        __java_fields__ = {'len': 'len', 'status': 'status'}
        # len：实例字段，在构造函数中初始化。
        # status：实例字段，在构造函数中初始化。
        def _java_init_0(self, siz):
            siz = jcast('int', siz)
            self.len = jcast('int', jcast('int', (jcast('int', jadd(siz, 63)) >> (6 & 31))))
            self.status = jarray('long', [self.len])

        def clear(self):
            i = jcast('int', 0)
            while (i < self.len):
                self.status[i] = jcast('long', 0)
                i = jcast('int', (i + 1))

        def copy(self, obj):
            i = jcast('int', 0)
            while (i < self.len):
                self.status[i] = jcast('long', jget(obj, 'status')[i])
                i = jcast('int', (i + 1))

        def and_(self, obj):
            i = jcast('int', 0)
            while (i < self.len):
                self.status[i] = jcast('long', jcast('long', (self.status[i] & jget(obj, 'status')[i])))
                i = jcast('int', (i + 1))

        def setOne(self, bit):
            bit = jcast('int', bit)
            self.status[jcast('int', (bit >> (6 & 31)))] = jcast('long', jcast('long', (self.status[jcast('int', (bit >> (6 & 31)))] | jcast('long', (1 << (jcast('int', (bit & 63)) & 63))))))

        def setZero(self, bit):
            bit = jcast('int', bit)
            self.status[jcast('int', (bit >> (6 & 31)))] = jcast('long', jcast('long', (self.status[jcast('int', (bit >> (6 & 31)))] & jcast('long', (~jcast('long', (1 << (jcast('int', (bit & 63)) & 63))))))))

        def getOnes(self):
            ret = jcast('int', 0)
            i = jcast('int', 0)
            while (i < self.len):
                ret = jcast('int', jcast('int', jadd(ret, jstatic('Long', 'bitCount', self.status[i]))))
                i = jcast('int', (i + 1))
            return jcast('int', ret)

        def __init__(self, *args, _java_ctor=None):
            self.len = jcast('int', 0)
            self.status = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_RabbitHole1.BitSet.BitSet")


    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    arr = None
    query = None
    # 排序之后不去重
    # 得到每个数字的排名
    sorted = None
    bi = None
    # cnt[v] = c，表示窗口中数字v出现c次
    cnt = None
    # 当前窗口的位图
    curSet = None
    # 问题从来没获得位图就拷贝，问题获得过位图就做&运算
    hasSet = None
    # 每个问题的位图
    bitSet = None
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code07_RabbitHole1.bi[a[0]] != Code07_RabbitHole1.bi[b[0]]):
                return jcast('int', jcast('int', (Code07_RabbitHole1.bi[a[0]] - Code07_RabbitHole1.bi[b[0]])))
            if (jcast('int', (Code07_RabbitHole1.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code07_RabbitHole1.n)
        mid = 0
        ret = jcast('int', jcast('int', (-1)))
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code07_RabbitHole1.sorted[mid] >= num):
                ret = jcast('int', mid)
                right = jcast('int', jcast('int', (mid - 1)))
            else:
                left = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ret)

    @staticmethod
    def add(x):
        x = jcast('int', x)
        Code07_RabbitHole1.cnt[x] = jcast('int', (Code07_RabbitHole1.cnt[x] + 1))
        jcall(Code07_RabbitHole1.curSet, 'setOne', jcast('int', (jcast('int', jadd(x, Code07_RabbitHole1.cnt[x])) - 1)))

    @staticmethod
    def del_(x):
        x = jcast('int', x)
        Code07_RabbitHole1.cnt[x] = jcast('int', (Code07_RabbitHole1.cnt[x] - 1))
        jcall(Code07_RabbitHole1.curSet, 'setZero', jcast('int', jadd(x, Code07_RabbitHole1.cnt[x])))

    @staticmethod
    def compute(q):
        q = jcast('int', q)
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= q):
            jobl = jcast('int', Code07_RabbitHole1.query[i][0])
            jobr = jcast('int', Code07_RabbitHole1.query[i][1])
            id = jcast('int', Code07_RabbitHole1.query[i][2])
            while (winl > jobl):
                Code07_RabbitHole1.add(Code07_RabbitHole1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code07_RabbitHole1.add(Code07_RabbitHole1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code07_RabbitHole1.del_(Code07_RabbitHole1.arr[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]])
            while (winr > jobr):
                Code07_RabbitHole1.del_(Code07_RabbitHole1.arr[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]])
            if (not Code07_RabbitHole1.hasSet[id]):
                Code07_RabbitHole1.hasSet[id] = jcast('boolean', True)
                jcall(Code07_RabbitHole1.bitSet[id], 'copy', Code07_RabbitHole1.curSet)
            else:
                jcall(Code07_RabbitHole1.bitSet[id], 'and_', Code07_RabbitHole1.curSet)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_RabbitHole1.n):
            Code07_RabbitHole1.sorted[i] = jcast('int', Code07_RabbitHole1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_RabbitHole1.sorted, 1, jcast('int', jadd(Code07_RabbitHole1.n, 1)))
        i = jcast('int', 1)
        while (i <= Code07_RabbitHole1.n):
            jset(Code07_RabbitHole1.arr, i, Code07_RabbitHole1.kth(Code07_RabbitHole1.arr[i]))
            i = jcast('int', (i + 1))
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code07_RabbitHole1.n)))
        i = jcast('int', 1)
        while (i <= Code07_RabbitHole1.n):
            Code07_RabbitHole1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < Code07_RabbitHole1.MAXT):
            jset(Code07_RabbitHole1.bitSet, i, Code07_RabbitHole1.BitSet(jcast('int', jadd(Code07_RabbitHole1.n, 1)), _java_ctor=0))
            i = jcast('int', (i + 1))
        Code07_RabbitHole1.curSet = Code07_RabbitHole1.BitSet(jcast('int', jadd(Code07_RabbitHole1.n, 1)), _java_ctor=0)

    @staticmethod
    def main(args):
        in_ = Code07_RabbitHole1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_RabbitHole1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_RabbitHole1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_RabbitHole1.n):
            jset(Code07_RabbitHole1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code07_RabbitHole1.prepare()
        t = jcast('int', jcast('int', (Code07_RabbitHole1.MAXT - 1)))
        while (Code07_RabbitHole1.m > 0):
            k = jcast('int', jstatic('Math', 'min', Code07_RabbitHole1.m, t))
            jstatic('Arrays', 'fill', Code07_RabbitHole1.cnt, 1, jcast('int', jadd(Code07_RabbitHole1.n, 1)), 0)
            jstatic('Arrays', 'fill', Code07_RabbitHole1.hasSet, 1, jcast('int', jadd(k, 1)), False)
            jstatic('Arrays', 'fill', Code07_RabbitHole1.ans, 1, jcast('int', jadd(k, 1)), 0)
            jcall(Code07_RabbitHole1.curSet, 'clear')
            cntq = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= k):
                j = jcast('int', 1)
                while (j <= 3):
                    jset(Code07_RabbitHole1.query[(cntq := jcast('int', (cntq + (1))))], 0, jcall(in_, 'nextInt'))
                    jset(Code07_RabbitHole1.query[cntq], 1, jcall(in_, 'nextInt'))
                    jset(Code07_RabbitHole1.query[cntq], 2, i)
                    Code07_RabbitHole1.ans[i] = jcast('int', jcast('int', jadd(Code07_RabbitHole1.ans[i], jcast('int', jadd(jcast('int', (Code07_RabbitHole1.query[cntq][1] - Code07_RabbitHole1.query[cntq][0])), 1)))))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'sort', Code07_RabbitHole1.query, 1, jcast('int', jadd(cntq, 1)), Code07_RabbitHole1.QueryCmp())
            Code07_RabbitHole1.compute(cntq)
            i = jcast('int', 1)
            while (i <= k):
                ((_java_obj_3 := Code07_RabbitHole1.ans), (_java_key_4 := i), jset(_java_obj_3, _java_key_4, jcast('int', (jget(_java_obj_3, _java_key_4) - jcast('int', (jcall(Code07_RabbitHole1.bitSet[i], 'getOnes') * 3))))))[2]
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= k):
                jcall(out, 'println', Code07_RabbitHole1.ans[i])
                i = jcast('int', (i + 1))
            Code07_RabbitHole1.m = jcast('int', jcast('int', (Code07_RabbitHole1.m - t)))
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
            return jcast('int', self.buffer[((_java_obj_5 := self), (_java_key_6 := 'ptr'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4]])

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
            raise TypeError("No matching overload for Code07_RabbitHole1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_RabbitHole1.MAXN = jcast('int', 100001)
Code07_RabbitHole1.MAXT = jcast('int', 30001)
Code07_RabbitHole1.n = jcast('int', 0)
Code07_RabbitHole1.m = jcast('int', 0)
Code07_RabbitHole1.arr = jarray('int', [Code07_RabbitHole1.MAXN])
Code07_RabbitHole1.query = jarray('int', [jcast('int', (Code07_RabbitHole1.MAXT * 3)), 3])
Code07_RabbitHole1.sorted = jarray('int', [Code07_RabbitHole1.MAXN])
Code07_RabbitHole1.bi = jarray('int', [Code07_RabbitHole1.MAXN])
Code07_RabbitHole1.cnt = jarray('int', [Code07_RabbitHole1.MAXN])
Code07_RabbitHole1.curSet = None
Code07_RabbitHole1.hasSet = jarray('boolean', [Code07_RabbitHole1.MAXT])
Code07_RabbitHole1.bitSet = jarray('BitSet', [Code07_RabbitHole1.MAXT])
Code07_RabbitHole1.ans = jarray('int', [Code07_RabbitHole1.MAXT])

if __name__ == '__main__':
    Code07_RabbitHole1.main([])
