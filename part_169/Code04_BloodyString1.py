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

# 大爷的字符串题，Python版
# 给定一个长度为n的数组arr，一共有m条查询，格式如下
# 查询 l r : arr[l..r]范围上，众数出现了几次，打印次数的相反数
# 1 <= n、m <= 2 * 10^5
# 1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3709
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_BloodyString1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sorted': 'sorted', 'query': 'query', 'bi': 'bi', 'cnt1': 'cnt1', 'cnt2': 'cnt2', 'maxCnt': 'maxCnt', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    sorted = None
    query = None
    bi = None
    # cnt1[i] = j，表示窗口内，数字i出现了j次
    # cnt2[i] = j，表示窗口内，出现了i次的数，有j种
    # maxCnt，表示窗口内，众数的次数
    cnt1 = None
    cnt2 = None
    maxCnt = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code04_BloodyString1.bi[a[0]] != Code04_BloodyString1.bi[b[0]]):
                return jcast('int', jcast('int', (Code04_BloodyString1.bi[a[0]] - Code04_BloodyString1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

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
            if (Code04_BloodyString1.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def del_(num):
        num = jcast('int', num)
        if ((Code04_BloodyString1.cnt1[num] == Code04_BloodyString1.maxCnt) and (Code04_BloodyString1.cnt2[Code04_BloodyString1.cnt1[num]] == 1)):
            Code04_BloodyString1.maxCnt = jcast('int', (Code04_BloodyString1.maxCnt - 1))
        ((_java_obj_1 := Code04_BloodyString1.cnt2), (_java_key_2 := Code04_BloodyString1.cnt1[num]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))), _java_old_3)[4]
        Code04_BloodyString1.cnt1[num] = jcast('int', (Code04_BloodyString1.cnt1[num] - 1))
        ((_java_obj_4 := Code04_BloodyString1.cnt2), (_java_key_5 := Code04_BloodyString1.cnt1[num]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]

    @staticmethod
    def add(num):
        num = jcast('int', num)
        ((_java_obj_7 := Code04_BloodyString1.cnt2), (_java_key_8 := Code04_BloodyString1.cnt1[num]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
        Code04_BloodyString1.cnt1[num] = jcast('int', (Code04_BloodyString1.cnt1[num] + 1))
        ((_java_obj_10 := Code04_BloodyString1.cnt2), (_java_key_11 := Code04_BloodyString1.cnt1[num]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
        Code04_BloodyString1.maxCnt = jcast('int', jstatic('Math', 'max', Code04_BloodyString1.maxCnt, Code04_BloodyString1.cnt1[num]))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code04_BloodyString1.n):
            Code04_BloodyString1.sorted[i] = jcast('int', Code04_BloodyString1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_BloodyString1.sorted, 1, jcast('int', jadd(Code04_BloodyString1.n, 1)))
        len = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code04_BloodyString1.n):
            if (Code04_BloodyString1.sorted[len] != Code04_BloodyString1.sorted[i]):
                jset(Code04_BloodyString1.sorted, (len := jcast('int', (len + (1)))), Code04_BloodyString1.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_BloodyString1.n):
            jset(Code04_BloodyString1.arr, i, Code04_BloodyString1.kth(len, Code04_BloodyString1.arr[i]))
            i = jcast('int', (i + 1))
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code04_BloodyString1.n)))
        i = jcast('int', 1)
        while (i <= Code04_BloodyString1.n):
            Code04_BloodyString1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_BloodyString1.query, 1, jcast('int', jadd(Code04_BloodyString1.m, 1)), Code04_BloodyString1.QueryCmp())

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_BloodyString1.m):
            jobl = jcast('int', Code04_BloodyString1.query[i][0])
            jobr = jcast('int', Code04_BloodyString1.query[i][1])
            while (winl > jobl):
                Code04_BloodyString1.add(Code04_BloodyString1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code04_BloodyString1.add(Code04_BloodyString1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code04_BloodyString1.del_(Code04_BloodyString1.arr[((_java_old_13 := winl), (winl := jcast('int', (winl + (1)))), _java_old_13)[2]])
            while (winr > jobr):
                Code04_BloodyString1.del_(Code04_BloodyString1.arr[((_java_old_14 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_14)[2]])
            jset(Code04_BloodyString1.ans, Code04_BloodyString1.query[i][2], Code04_BloodyString1.maxCnt)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code04_BloodyString1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_BloodyString1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_BloodyString1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_BloodyString1.n):
            jset(Code04_BloodyString1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_BloodyString1.m):
            jset(Code04_BloodyString1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code04_BloodyString1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code04_BloodyString1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code04_BloodyString1.prepare()
        Code04_BloodyString1.compute()
        i = jcast('int', 1)
        while (i <= Code04_BloodyString1.m):
            jcall(out, 'println', jcast('int', (-Code04_BloodyString1.ans[i])))
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
            raise TypeError("No matching overload for Code04_BloodyString1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_BloodyString1.MAXN = jcast('int', 200001)
Code04_BloodyString1.n = jcast('int', 0)
Code04_BloodyString1.m = jcast('int', 0)
Code04_BloodyString1.arr = jarray('int', [Code04_BloodyString1.MAXN])
Code04_BloodyString1.sorted = jarray('int', [Code04_BloodyString1.MAXN])
Code04_BloodyString1.query = jarray('int', [Code04_BloodyString1.MAXN, 3])
Code04_BloodyString1.bi = jarray('int', [Code04_BloodyString1.MAXN])
Code04_BloodyString1.cnt1 = jarray('int', [Code04_BloodyString1.MAXN])
Code04_BloodyString1.cnt2 = jarray('int', [Code04_BloodyString1.MAXN])
Code04_BloodyString1.maxCnt = jcast('int', 0)
Code04_BloodyString1.ans = jarray('int', [Code04_BloodyString1.MAXN])

if __name__ == '__main__':
    Code04_BloodyString1.main([])
