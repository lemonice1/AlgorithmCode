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

# 机器学习，Python版
# 给定一个长度为n的数组arr，一共有m条操作，操作格式如下
# 操作 1 l r     : arr[l..r]范围上，每种数字出现的次数，假设构成一个集合
# 打印这个集合中，没出现过的最小正数
# 操作 2 pos val : 把arr[pos]的值设置成val
# 1 <= n、m <= 10^5
# 1 <= arr[i]、val <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/CF940F
# 测试链接 : https://codeforces.com/problemset/problem/940/F
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_MachineLearning1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sorted': 'sorted', 'bi': 'bi', 'query': 'query', 'update': 'update', 'cntq': 'cntq', 'cntu': 'cntu', 'cnt1': 'cnt1', 'cnt2': 'cnt2', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    sorted = None
    bi = None
    query = None
    update = None
    cntq = 0
    cntu = 0
    # cnt1[i] = j，表示i这种数出现了j次
    # cnt2[i] = j，表示出现次数为i的数有j种
    cnt1 = None
    cnt2 = None
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code08_MachineLearning1.bi[a[0]] != Code08_MachineLearning1.bi[b[0]]):
                return jcast('int', jcast('int', (Code08_MachineLearning1.bi[a[0]] - Code08_MachineLearning1.bi[b[0]])))
            if (Code08_MachineLearning1.bi[a[1]] != Code08_MachineLearning1.bi[b[1]]):
                return jcast('int', jcast('int', (Code08_MachineLearning1.bi[a[1]] - Code08_MachineLearning1.bi[b[1]])))
            return jcast('int', jcast('int', (a[2] - b[2])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def kth(len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', len)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code08_MachineLearning1.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def del_(num):
        num = jcast('int', num)
        ((_java_obj_1 := Code08_MachineLearning1.cnt2), (_java_key_2 := Code08_MachineLearning1.cnt1[num]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))), _java_old_3)[4]
        Code08_MachineLearning1.cnt1[num] = jcast('int', (Code08_MachineLearning1.cnt1[num] - 1))
        ((_java_obj_4 := Code08_MachineLearning1.cnt2), (_java_key_5 := Code08_MachineLearning1.cnt1[num]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]

    @staticmethod
    def add(num):
        num = jcast('int', num)
        ((_java_obj_7 := Code08_MachineLearning1.cnt2), (_java_key_8 := Code08_MachineLearning1.cnt1[num]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
        Code08_MachineLearning1.cnt1[num] = jcast('int', (Code08_MachineLearning1.cnt1[num] + 1))
        ((_java_obj_10 := Code08_MachineLearning1.cnt2), (_java_key_11 := Code08_MachineLearning1.cnt1[num]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]

    @staticmethod
    def moveTime(jobl, jobr, tim):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        tim = jcast('int', tim)
        pos = jcast('int', Code08_MachineLearning1.update[tim][0])
        val = jcast('int', Code08_MachineLearning1.update[tim][1])
        if ((jobl <= pos) and (pos <= jobr)):
            Code08_MachineLearning1.del_(Code08_MachineLearning1.arr[pos])
            Code08_MachineLearning1.add(val)
        tmp = jcast('int', Code08_MachineLearning1.arr[pos])
        Code08_MachineLearning1.arr[pos] = jcast('int', val)
        jset(Code08_MachineLearning1.update[tim], 1, tmp)

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        wint = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code08_MachineLearning1.cntq):
            jobl = jcast('int', Code08_MachineLearning1.query[i][0])
            jobr = jcast('int', Code08_MachineLearning1.query[i][1])
            jobt = jcast('int', Code08_MachineLearning1.query[i][2])
            id = jcast('int', Code08_MachineLearning1.query[i][3])
            while (winl > jobl):
                Code08_MachineLearning1.add(Code08_MachineLearning1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code08_MachineLearning1.add(Code08_MachineLearning1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code08_MachineLearning1.del_(Code08_MachineLearning1.arr[((_java_old_13 := winl), (winl := jcast('int', (winl + (1)))), _java_old_13)[2]])
            while (winr > jobr):
                Code08_MachineLearning1.del_(Code08_MachineLearning1.arr[((_java_old_14 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_14)[2]])
            while (wint < jobt):
                Code08_MachineLearning1.moveTime(jobl, jobr, (wint := jcast('int', (wint + (1)))))
            while (wint > jobt):
                Code08_MachineLearning1.moveTime(jobl, jobr, ((_java_old_15 := wint), (wint := jcast('int', (wint + (-1)))), _java_old_15)[2])
            # 如下枚举看似暴力，其实O(根号n)的复杂度
            ret = jcast('int', 1)
            while ((ret <= Code08_MachineLearning1.n) and (Code08_MachineLearning1.cnt2[ret] > 0)):
                ret = jcast('int', (ret + 1))
            Code08_MachineLearning1.ans[id] = jcast('int', ret)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        len = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code08_MachineLearning1.n):
            jset(Code08_MachineLearning1.sorted, (len := jcast('int', (len + (1)))), Code08_MachineLearning1.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_MachineLearning1.cntu):
            jset(Code08_MachineLearning1.sorted, (len := jcast('int', (len + (1)))), Code08_MachineLearning1.update[i][1])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code08_MachineLearning1.sorted, 1, jcast('int', jadd(len, 1)))
        tmp = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= len):
            if (Code08_MachineLearning1.sorted[tmp] != Code08_MachineLearning1.sorted[i]):
                jset(Code08_MachineLearning1.sorted, (tmp := jcast('int', (tmp + (1)))), Code08_MachineLearning1.sorted[i])
            i = jcast('int', (i + 1))
        len = jcast('int', tmp)
        i = jcast('int', 1)
        while (i <= Code08_MachineLearning1.n):
            jset(Code08_MachineLearning1.arr, i, Code08_MachineLearning1.kth(len, Code08_MachineLearning1.arr[i]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_MachineLearning1.cntu):
            jset(Code08_MachineLearning1.update[i], 1, Code08_MachineLearning1.kth(len, Code08_MachineLearning1.update[i][1]))
            i = jcast('int', (i + 1))
        blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jstatic('Math', 'pow', Code08_MachineLearning1.n, jdiv(2.0, 3)))))
        i = jcast('int', 1)
        while (i <= Code08_MachineLearning1.n):
            Code08_MachineLearning1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code08_MachineLearning1.query, 1, jcast('int', jadd(Code08_MachineLearning1.cntq, 1)), Code08_MachineLearning1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code08_MachineLearning1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_MachineLearning1.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_MachineLearning1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code08_MachineLearning1.n):
            jset(Code08_MachineLearning1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        l = 0
        r = 0
        pos = 0
        val = 0
        while (i <= Code08_MachineLearning1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                l = jcast('int', jcall(in_, 'nextInt'))
                r = jcast('int', jcall(in_, 'nextInt'))
                Code08_MachineLearning1.cntq = jcast('int', (Code08_MachineLearning1.cntq + 1))
                jset(Code08_MachineLearning1.query[Code08_MachineLearning1.cntq], 0, l)
                jset(Code08_MachineLearning1.query[Code08_MachineLearning1.cntq], 1, r)
                jset(Code08_MachineLearning1.query[Code08_MachineLearning1.cntq], 2, Code08_MachineLearning1.cntu)
                jset(Code08_MachineLearning1.query[Code08_MachineLearning1.cntq], 3, Code08_MachineLearning1.cntq)
            else:
                pos = jcast('int', jcall(in_, 'nextInt'))
                val = jcast('int', jcall(in_, 'nextInt'))
                Code08_MachineLearning1.cntu = jcast('int', (Code08_MachineLearning1.cntu + 1))
                jset(Code08_MachineLearning1.update[Code08_MachineLearning1.cntu], 0, pos)
                jset(Code08_MachineLearning1.update[Code08_MachineLearning1.cntu], 1, val)
            i = jcast('int', (i + 1))
        Code08_MachineLearning1.prepare()
        Code08_MachineLearning1.compute()
        i = jcast('int', 1)
        while (i <= Code08_MachineLearning1.cntq):
            jcall(out, 'println', Code08_MachineLearning1.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code08_MachineLearning1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_MachineLearning1.MAXN = jcast('int', 100001)
Code08_MachineLearning1.n = jcast('int', 0)
Code08_MachineLearning1.m = jcast('int', 0)
Code08_MachineLearning1.arr = jarray('int', [Code08_MachineLearning1.MAXN])
Code08_MachineLearning1.sorted = jarray('int', [jcast('int', (Code08_MachineLearning1.MAXN << (1 & 31)))])
Code08_MachineLearning1.bi = jarray('int', [Code08_MachineLearning1.MAXN])
Code08_MachineLearning1.query = jarray('int', [Code08_MachineLearning1.MAXN, 4])
Code08_MachineLearning1.update = jarray('int', [Code08_MachineLearning1.MAXN, 2])
Code08_MachineLearning1.cntq = jcast('int', 0)
Code08_MachineLearning1.cntu = jcast('int', 0)
Code08_MachineLearning1.cnt1 = jarray('int', [jcast('int', (Code08_MachineLearning1.MAXN << (1 & 31)))])
Code08_MachineLearning1.cnt2 = jarray('int', [Code08_MachineLearning1.MAXN])
Code08_MachineLearning1.ans = jarray('int', [Code08_MachineLearning1.MAXN])

if __name__ == '__main__':
    Code08_MachineLearning1.main([])
