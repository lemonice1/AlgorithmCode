# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 拦截导弹，Python版
# 一共有n个导弹，编号1~n，表示导弹从早到晚依次到达，每个导弹给定，高度h、速度v
# 你有导弹拦截系统，第1次可以拦截任意参数的导弹
# 但是之后拦截的导弹，高度和速度都不能比前一次拦截的导弹大
# 你的目的是尽可能多的拦截导弹，如果有多个最优方案，会随机选一个执行
# 打印最多能拦截几个导弹，并且打印每个导弹被拦截的概率
# 1 <= n <= 5 * 10^4
# 1 <= h、v <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P2487
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Interceptor1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 's': 's', 'h': 'h', 'v': 'v', 'sortv': 'sortv', 'arr': 'arr', 'treeVal': 'treeVal', 'treeCnt': 'treeCnt', 'len1': 'len1', 'cnt1': 'cnt1', 'len2': 'len2', 'cnt2': 'cnt2', 'queryVal': 'queryVal', 'queryCnt': 'queryCnt'}
    MAXN = 0
    n = 0
    s = 0
    h = None
    v = None
    sortv = None
    # 位置i、高度h、速度v
    arr = None
    # 树状数组维护前缀最大值、最大值出现的次数
    treeVal = None
    treeCnt = None
    # i位置结尾的情况下，最长不上升子序列的长度 及其 子序列个数
    len1 = None
    cnt1 = None
    # i位置开头的情况下，最长不上升子序列的长度 及其 子序列个数
    len2 = None
    cnt2 = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def more(i, val, cnt):
        i = jcast('int', i)
        val = jcast('int', val)
        cnt = jcast('double', cnt)
        while (i <= Code04_Interceptor1.s):
            if (val > Code04_Interceptor1.treeVal[i]):
                Code04_Interceptor1.treeVal[i] = jcast('int', val)
                Code04_Interceptor1.treeCnt[i] = jcast('double', cnt)
            else:
                if (val == Code04_Interceptor1.treeVal[i]):
                    Code04_Interceptor1.treeCnt[i] = jcast('double', jadd(Code04_Interceptor1.treeCnt[i], cnt))
            i = jcast('int', jcast('int', jadd(i, Code04_Interceptor1.lowbit(i))))

    queryVal = 0
    queryCnt = 0.0
    @staticmethod
    def query(i):
        i = jcast('int', i)
        Code04_Interceptor1.queryVal = jcast('int', 0)
        Code04_Interceptor1.queryCnt = jcast('double', 0)
        while (i > 0):
            if (Code04_Interceptor1.treeVal[i] > Code04_Interceptor1.queryVal):
                Code04_Interceptor1.queryVal = jcast('int', Code04_Interceptor1.treeVal[i])
                Code04_Interceptor1.queryCnt = jcast('double', Code04_Interceptor1.treeCnt[i])
            else:
                if (Code04_Interceptor1.treeVal[i] == Code04_Interceptor1.queryVal):
                    Code04_Interceptor1.queryCnt = jcast('double', jadd(Code04_Interceptor1.queryCnt, Code04_Interceptor1.treeCnt[i]))
            i = jcast('int', jcast('int', (i - Code04_Interceptor1.lowbit(i))))

    @staticmethod
    def clear(i):
        i = jcast('int', i)
        while (i <= Code04_Interceptor1.s):
            Code04_Interceptor1.treeVal[i] = jcast('int', 0)
            Code04_Interceptor1.treeCnt[i] = jcast('double', 0)
            i = jcast('int', jcast('int', jadd(i, Code04_Interceptor1.lowbit(i))))

    @staticmethod
    def merge1(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        i = jcast('int', l)
        while (i <= r):
            jset(Code04_Interceptor1.arr[i], 0, i)
            jset(Code04_Interceptor1.arr[i], 1, Code04_Interceptor1.h[i])
            jset(Code04_Interceptor1.arr[i], 2, Code04_Interceptor1.v[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_Interceptor1.arr, l, jcast('int', jadd(m, 1)), (lambda a, b: (b[1] - a[1])))
        jstatic('Arrays', 'sort', Code04_Interceptor1.arr, jcast('int', jadd(m, 1)), jcast('int', jadd(r, 1)), (lambda a, b: (b[1] - a[1])))
        p1 = 0
        p2 = 0
        # 为了防止出现0下标，(s - v + 1)是树状数组的下标
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code04_Interceptor1.arr[jcast('int', jadd(p1, 1))][1] >= Code04_Interceptor1.arr[p2][1])):
                p1 = jcast('int', (p1 + 1))
                Code04_Interceptor1.more(jcast('int', jadd(jcast('int', (Code04_Interceptor1.s - Code04_Interceptor1.arr[p1][2])), 1)), Code04_Interceptor1.len1[Code04_Interceptor1.arr[p1][0]], Code04_Interceptor1.cnt1[Code04_Interceptor1.arr[p1][0]])
            Code04_Interceptor1.query(jcast('int', jadd(jcast('int', (Code04_Interceptor1.s - Code04_Interceptor1.arr[p2][2])), 1)))
            if (jcast('int', jadd(Code04_Interceptor1.queryVal, 1)) > Code04_Interceptor1.len1[Code04_Interceptor1.arr[p2][0]]):
                jset(Code04_Interceptor1.len1, Code04_Interceptor1.arr[p2][0], jcast('int', jadd(Code04_Interceptor1.queryVal, 1)))
                jset(Code04_Interceptor1.cnt1, Code04_Interceptor1.arr[p2][0], Code04_Interceptor1.queryCnt)
            else:
                if (jcast('int', jadd(Code04_Interceptor1.queryVal, 1)) == Code04_Interceptor1.len1[Code04_Interceptor1.arr[p2][0]]):
                    ((_java_obj_1 := Code04_Interceptor1.cnt1), (_java_key_2 := Code04_Interceptor1.arr[p2][0]), jset(_java_obj_1, _java_key_2, jadd(jget(_java_obj_1, _java_key_2), Code04_Interceptor1.queryCnt)))[2]
            p2 = jcast('int', (p2 + 1))
        i = jcast('int', l)
        while (i <= p1):
            Code04_Interceptor1.clear(jcast('int', jadd(jcast('int', (Code04_Interceptor1.s - Code04_Interceptor1.arr[i][2])), 1)))
            i = jcast('int', (i + 1))

    # 最长不上升子序列的长度 及其 个数
    @staticmethod
    def cdq1(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code04_Interceptor1.cdq1(l, mid)
        Code04_Interceptor1.merge1(l, mid, r)
        Code04_Interceptor1.cdq1(jcast('int', jadd(mid, 1)), r)

    @staticmethod
    def merge2(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        i = jcast('int', l)
        while (i <= r):
            jset(Code04_Interceptor1.arr[i], 0, i)
            jset(Code04_Interceptor1.arr[i], 1, Code04_Interceptor1.h[i])
            jset(Code04_Interceptor1.arr[i], 2, Code04_Interceptor1.v[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_Interceptor1.arr, l, jcast('int', jadd(m, 1)), (lambda a, b: (a[1] - b[1])))
        jstatic('Arrays', 'sort', Code04_Interceptor1.arr, jcast('int', jadd(m, 1)), jcast('int', jadd(r, 1)), (lambda a, b: (a[1] - b[1])))
        p1 = 0
        p2 = 0
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code04_Interceptor1.arr[jcast('int', jadd(p1, 1))][1] <= Code04_Interceptor1.arr[p2][1])):
                p1 = jcast('int', (p1 + 1))
                Code04_Interceptor1.more(Code04_Interceptor1.arr[p1][2], Code04_Interceptor1.len2[Code04_Interceptor1.arr[p1][0]], Code04_Interceptor1.cnt2[Code04_Interceptor1.arr[p1][0]])
            Code04_Interceptor1.query(Code04_Interceptor1.arr[p2][2])
            if (jcast('int', jadd(Code04_Interceptor1.queryVal, 1)) > Code04_Interceptor1.len2[Code04_Interceptor1.arr[p2][0]]):
                jset(Code04_Interceptor1.len2, Code04_Interceptor1.arr[p2][0], jcast('int', jadd(Code04_Interceptor1.queryVal, 1)))
                jset(Code04_Interceptor1.cnt2, Code04_Interceptor1.arr[p2][0], Code04_Interceptor1.queryCnt)
            else:
                if (jcast('int', jadd(Code04_Interceptor1.queryVal, 1)) == Code04_Interceptor1.len2[Code04_Interceptor1.arr[p2][0]]):
                    ((_java_obj_3 := Code04_Interceptor1.cnt2), (_java_key_4 := Code04_Interceptor1.arr[p2][0]), jset(_java_obj_3, _java_key_4, jadd(jget(_java_obj_3, _java_key_4), Code04_Interceptor1.queryCnt)))[2]
            p2 = jcast('int', (p2 + 1))
        i = jcast('int', l)
        while (i <= p1):
            Code04_Interceptor1.clear(Code04_Interceptor1.arr[i][2])
            i = jcast('int', (i + 1))

    # 最长不下降子序列的长度 及其 个数
    @staticmethod
    def cdq2(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code04_Interceptor1.cdq2(l, m)
        Code04_Interceptor1.merge2(l, m, r)
        Code04_Interceptor1.cdq2(jcast('int', jadd(m, 1)), r)

    @staticmethod
    def lower(num):
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', Code04_Interceptor1.s)
        ans = jcast('int', 1)
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code04_Interceptor1.sortv[mid] >= num):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code04_Interceptor1.n):
            Code04_Interceptor1.sortv[i] = jcast('int', Code04_Interceptor1.v[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_Interceptor1.sortv, 1, jcast('int', jadd(Code04_Interceptor1.n, 1)))
        Code04_Interceptor1.s = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code04_Interceptor1.n):
            if (Code04_Interceptor1.sortv[Code04_Interceptor1.s] != Code04_Interceptor1.sortv[i]):
                jset(Code04_Interceptor1.sortv, ((_java_obj_5 := Code04_Interceptor1), (_java_key_6 := 's'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3], Code04_Interceptor1.sortv[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Interceptor1.n):
            jset(Code04_Interceptor1.v, i, Code04_Interceptor1.lower(Code04_Interceptor1.v[i]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Interceptor1.n):
            jset(Code04_Interceptor1.len1, i, jset(Code04_Interceptor1.len2, i, 1))
            jset(Code04_Interceptor1.cnt1, i, jset(Code04_Interceptor1.cnt2, i, 1.0))
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        Code04_Interceptor1.cdq1(1, Code04_Interceptor1.n)
        l = jcast('int', 1)
        r = jcast('int', Code04_Interceptor1.n)
        while (l < r):
            a = jcast('int', Code04_Interceptor1.h[l])
            Code04_Interceptor1.h[l] = jcast('int', Code04_Interceptor1.h[r])
            Code04_Interceptor1.h[r] = jcast('int', a)
            b = jcast('int', Code04_Interceptor1.v[l])
            Code04_Interceptor1.v[l] = jcast('int', Code04_Interceptor1.v[r])
            Code04_Interceptor1.v[r] = jcast('int', b)
            l = jcast('int', (l + 1))
            r = jcast('int', (r - 1))
        Code04_Interceptor1.cdq2(1, Code04_Interceptor1.n)
        l = jcast('int', 1)
        r = jcast('int', Code04_Interceptor1.n)
        while (l < r):
            a = jcast('int', Code04_Interceptor1.len2[l])
            Code04_Interceptor1.len2[l] = jcast('int', Code04_Interceptor1.len2[r])
            Code04_Interceptor1.len2[r] = jcast('int', a)
            b = jcast('double', Code04_Interceptor1.cnt2[l])
            Code04_Interceptor1.cnt2[l] = jcast('double', Code04_Interceptor1.cnt2[r])
            Code04_Interceptor1.cnt2[r] = jcast('double', b)
            l = jcast('int', (l + 1))
            r = jcast('int', (r - 1))

    @staticmethod
    def main(args):
        in_ = Code04_Interceptor1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Interceptor1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Interceptor1.n):
            jset(Code04_Interceptor1.h, i, jcall(in_, 'nextInt'))
            jset(Code04_Interceptor1.v, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code04_Interceptor1.prepare()
        Code04_Interceptor1.compute()
        len = jcast('int', 0)
        cnt = jcast('double', 0)
        i = jcast('int', 1)
        while (i <= Code04_Interceptor1.n):
            len = jcast('int', jstatic('Math', 'max', len, Code04_Interceptor1.len1[i]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Interceptor1.n):
            if (Code04_Interceptor1.len1[i] == len):
                cnt = jcast('double', jadd(cnt, Code04_Interceptor1.cnt1[i]))
            i = jcast('int', (i + 1))
        jcall(out, 'println', len)
        i = jcast('int', 1)
        while (i <= Code04_Interceptor1.n):
            if (jcast('int', (jcast('int', jadd(Code04_Interceptor1.len1[i], Code04_Interceptor1.len2[i])) - 1)) < len):
                jcall(out, 'print', '0 ')
            else:
                jcall(out, 'printf', '%.5f ', jdiv((Code04_Interceptor1.cnt1[i] * Code04_Interceptor1.cnt2[i]), cnt))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_Interceptor1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Interceptor1.MAXN = jcast('int', 50001)
Code04_Interceptor1.n = jcast('int', 0)
Code04_Interceptor1.s = jcast('int', 0)
Code04_Interceptor1.h = jarray('int', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.v = jarray('int', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.sortv = jarray('int', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.arr = jarray('int', [Code04_Interceptor1.MAXN, 3])
Code04_Interceptor1.treeVal = jarray('int', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.treeCnt = jarray('double', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.len1 = jarray('int', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.cnt1 = jarray('double', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.len2 = jarray('int', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.cnt2 = jarray('double', [Code04_Interceptor1.MAXN])
Code04_Interceptor1.queryVal = jcast('int', 0)
Code04_Interceptor1.queryCnt = jcast('double', 0.0)

if __name__ == '__main__':
    Code04_Interceptor1.main([])
