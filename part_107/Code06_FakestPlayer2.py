# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最假女选手，Python版
# 这道题课上没讲，也是吉司机线段树的经典模版题
# 这道题不涉及历史最值，所以比题目5简单
# 如果理解了题目5，完全可以看懂如下的代码
# 给定一个长度为n的数组arr，然后是m条操作，类型如下
# 操作 1 l r x : arr[l..r]范围内，每个数都加上x
# 操作 2 l r x : arr[l..r]范围内，小于x的数都变成x
# 操作 3 l r x : arr[l..r]范围内，大于x的数都变成x
# 操作 4 l r   : 查询arr[l..r]累加和
# 操作 5 l r   : 查询arr[l..r]最大值
# 操作 6 l r   : 查询arr[l..r]最小值
# 1 <= n、m <= 5 * 10^5    累加和需要long类型
# 测试链接 : https://loj.ac/p/6565
# 测试链接 : https://www.luogu.com.cn/problem/P10639
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_FakestPlayer2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sum': 'sum', 'max': 'max', 'cntMax': 'cntMax', 'sem': 'sem', 'min': 'min', 'cntMin': 'cntMin', 'sim': 'sim', 'addTag': 'addTag'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    arr = None
    sum = None
    max = None
    cntMax = None
    sem = None
    # 区间最小值
    min = None
    # 区间最小值的个数
    cntMin = None
    # 区间严格次小值
    sim = None
    # 整个区间统一增加的懒信息
    addTag = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code06_FakestPlayer2.sum[i] = jcast('long', jcast('long', jadd(Code06_FakestPlayer2.sum[l], Code06_FakestPlayer2.sum[r])))
        if (Code06_FakestPlayer2.max[l] > Code06_FakestPlayer2.max[r]):
            Code06_FakestPlayer2.max[i] = jcast('int', Code06_FakestPlayer2.max[l])
            Code06_FakestPlayer2.cntMax[i] = jcast('int', Code06_FakestPlayer2.cntMax[l])
            jset(Code06_FakestPlayer2.sem, i, jstatic('Math', 'max', Code06_FakestPlayer2.sem[l], Code06_FakestPlayer2.max[r]))
        else:
            if (Code06_FakestPlayer2.max[l] < Code06_FakestPlayer2.max[r]):
                Code06_FakestPlayer2.max[i] = jcast('int', Code06_FakestPlayer2.max[r])
                Code06_FakestPlayer2.cntMax[i] = jcast('int', Code06_FakestPlayer2.cntMax[r])
                jset(Code06_FakestPlayer2.sem, i, jstatic('Math', 'max', Code06_FakestPlayer2.max[l], Code06_FakestPlayer2.sem[r]))
            else:
                Code06_FakestPlayer2.max[i] = jcast('int', Code06_FakestPlayer2.max[l])
                Code06_FakestPlayer2.cntMax[i] = jcast('int', jcast('int', jadd(Code06_FakestPlayer2.cntMax[l], Code06_FakestPlayer2.cntMax[r])))
                jset(Code06_FakestPlayer2.sem, i, jstatic('Math', 'max', Code06_FakestPlayer2.sem[l], Code06_FakestPlayer2.sem[r]))
        if (Code06_FakestPlayer2.min[l] < Code06_FakestPlayer2.min[r]):
            Code06_FakestPlayer2.min[i] = jcast('int', Code06_FakestPlayer2.min[l])
            Code06_FakestPlayer2.cntMin[i] = jcast('int', Code06_FakestPlayer2.cntMin[l])
            jset(Code06_FakestPlayer2.sim, i, jstatic('Math', 'min', Code06_FakestPlayer2.sim[l], Code06_FakestPlayer2.min[r]))
        else:
            if (Code06_FakestPlayer2.min[l] > Code06_FakestPlayer2.min[r]):
                Code06_FakestPlayer2.min[i] = jcast('int', Code06_FakestPlayer2.min[r])
                Code06_FakestPlayer2.cntMin[i] = jcast('int', Code06_FakestPlayer2.cntMin[r])
                jset(Code06_FakestPlayer2.sim, i, jstatic('Math', 'min', Code06_FakestPlayer2.min[l], Code06_FakestPlayer2.sim[r]))
            else:
                Code06_FakestPlayer2.min[i] = jcast('int', Code06_FakestPlayer2.min[l])
                Code06_FakestPlayer2.cntMin[i] = jcast('int', jcast('int', jadd(Code06_FakestPlayer2.cntMin[l], Code06_FakestPlayer2.cntMin[r])))
                jset(Code06_FakestPlayer2.sim, i, jstatic('Math', 'min', Code06_FakestPlayer2.sim[l], Code06_FakestPlayer2.sim[r]))

    @staticmethod
    def lazyAdd(i, n, v):
        i = jcast('int', i)
        n = jcast('int', n)
        v = jcast('int', v)
        Code06_FakestPlayer2.sum[i] = jcast('long', jcast('long', jadd(Code06_FakestPlayer2.sum[i], jcast('long', (jcast('long', (1 * v)) * n)))))
        Code06_FakestPlayer2.max[i] = jcast('int', jcast('int', jadd(Code06_FakestPlayer2.max[i], v)))
        Code06_FakestPlayer2.sem[i] = jcast('int', jcast('int', jadd(Code06_FakestPlayer2.sem[i], (0 if (Code06_FakestPlayer2.sem[i] == jcast('int', (-Code06_FakestPlayer2.INF))) else v))))
        Code06_FakestPlayer2.min[i] = jcast('int', jcast('int', jadd(Code06_FakestPlayer2.min[i], v)))
        Code06_FakestPlayer2.sim[i] = jcast('int', jcast('int', jadd(Code06_FakestPlayer2.sim[i], (0 if (Code06_FakestPlayer2.sim[i] == Code06_FakestPlayer2.INF) else v))))
        Code06_FakestPlayer2.addTag[i] = jcast('int', jcast('int', jadd(Code06_FakestPlayer2.addTag[i], v)))

    # 只把当前区间中的最大值压到v，要求sem[i] < v < max[i]
    @staticmethod
    def lazySetMin(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code06_FakestPlayer2.sum[i] = jcast('long', jcast('long', jadd(Code06_FakestPlayer2.sum[i], jcast('long', (jcast('long', (1 * jcast('int', (v - Code06_FakestPlayer2.max[i])))) * Code06_FakestPlayer2.cntMax[i])))))
        if (Code06_FakestPlayer2.min[i] == Code06_FakestPlayer2.max[i]):
            Code06_FakestPlayer2.min[i] = jcast('int', v)
        else:
            if (Code06_FakestPlayer2.sim[i] == Code06_FakestPlayer2.max[i]):
                Code06_FakestPlayer2.sim[i] = jcast('int', v)
        Code06_FakestPlayer2.max[i] = jcast('int', v)

    # 只把当前区间中的最小值抬到v，要求min[i] < v < sim[i]
    @staticmethod
    def lazySetMax(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code06_FakestPlayer2.sum[i] = jcast('long', jcast('long', jadd(Code06_FakestPlayer2.sum[i], jcast('long', (jcast('long', (1 * jcast('int', (v - Code06_FakestPlayer2.min[i])))) * Code06_FakestPlayer2.cntMin[i])))))
        if (Code06_FakestPlayer2.max[i] == Code06_FakestPlayer2.min[i]):
            Code06_FakestPlayer2.max[i] = jcast('int', v)
        else:
            if (Code06_FakestPlayer2.sem[i] == Code06_FakestPlayer2.min[i]):
                Code06_FakestPlayer2.sem[i] = jcast('int', v)
        Code06_FakestPlayer2.min[i] = jcast('int', v)

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        if (Code06_FakestPlayer2.addTag[i] != 0):
            Code06_FakestPlayer2.lazyAdd(l, ln, Code06_FakestPlayer2.addTag[i])
            Code06_FakestPlayer2.lazyAdd(r, rn, Code06_FakestPlayer2.addTag[i])
            Code06_FakestPlayer2.addTag[i] = jcast('int', 0)
        if (Code06_FakestPlayer2.max[l] > Code06_FakestPlayer2.max[i]):
            Code06_FakestPlayer2.lazySetMin(l, Code06_FakestPlayer2.max[i])
        if (Code06_FakestPlayer2.min[l] < Code06_FakestPlayer2.min[i]):
            Code06_FakestPlayer2.lazySetMax(l, Code06_FakestPlayer2.min[i])
        if (Code06_FakestPlayer2.max[r] > Code06_FakestPlayer2.max[i]):
            Code06_FakestPlayer2.lazySetMin(r, Code06_FakestPlayer2.max[i])
        if (Code06_FakestPlayer2.min[r] < Code06_FakestPlayer2.min[i]):
            Code06_FakestPlayer2.lazySetMax(r, Code06_FakestPlayer2.min[i])

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code06_FakestPlayer2.sum, i, jset(Code06_FakestPlayer2.max, i, jset(Code06_FakestPlayer2.min, i, Code06_FakestPlayer2.arr[l])))
            Code06_FakestPlayer2.sem[i] = jcast('int', jcast('int', (-Code06_FakestPlayer2.INF)))
            Code06_FakestPlayer2.sim[i] = jcast('int', Code06_FakestPlayer2.INF)
            jset(Code06_FakestPlayer2.cntMax, i, jset(Code06_FakestPlayer2.cntMin, i, 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_FakestPlayer2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code06_FakestPlayer2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_FakestPlayer2.up(i)
        Code06_FakestPlayer2.addTag[i] = jcast('int', 0)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_FakestPlayer2.lazyAdd(i, jcast('int', jadd(jcast('int', (r - l)), 1)), jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_FakestPlayer2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code06_FakestPlayer2.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_FakestPlayer2.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_FakestPlayer2.up(i)

    @staticmethod
    def setMax(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobv <= Code06_FakestPlayer2.min[i]):
            return
        if (((jobl <= l) and (r <= jobr)) and (jobv < Code06_FakestPlayer2.sim[i])):
            Code06_FakestPlayer2.lazySetMax(i, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_FakestPlayer2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code06_FakestPlayer2.setMax(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_FakestPlayer2.setMax(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_FakestPlayer2.up(i)

    @staticmethod
    def setMin(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobv >= Code06_FakestPlayer2.max[i]):
            return
        if (((jobl <= l) and (r <= jobr)) and (Code06_FakestPlayer2.sem[i] < jobv)):
            Code06_FakestPlayer2.lazySetMin(i, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_FakestPlayer2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code06_FakestPlayer2.setMin(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_FakestPlayer2.setMin(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_FakestPlayer2.up(i)

    @staticmethod
    def querySum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code06_FakestPlayer2.sum[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_FakestPlayer2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            ans = jcast('long', 0)
            if (jobl <= mid):
                ans = jcast('long', jcast('long', jadd(ans, Code06_FakestPlayer2.querySum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
            if (jobr > mid):
                ans = jcast('long', jcast('long', jadd(ans, Code06_FakestPlayer2.querySum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
            return jcast('long', ans)

    @staticmethod
    def queryMax(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code06_FakestPlayer2.max[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_FakestPlayer2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            ans = jcast('int', jcast('int', (-Code06_FakestPlayer2.INF)))
            if (jobl <= mid):
                ans = jcast('int', jstatic('Math', 'max', ans, Code06_FakestPlayer2.queryMax(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
            if (jobr > mid):
                ans = jcast('int', jstatic('Math', 'max', ans, Code06_FakestPlayer2.queryMax(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
            return jcast('int', ans)

    @staticmethod
    def queryMin(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code06_FakestPlayer2.min[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_FakestPlayer2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            ans = jcast('int', Code06_FakestPlayer2.INF)
            if (jobl <= mid):
                ans = jcast('int', jstatic('Math', 'min', ans, Code06_FakestPlayer2.queryMin(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
            if (jobr > mid):
                ans = jcast('int', jstatic('Math', 'min', ans, Code06_FakestPlayer2.queryMin(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
            return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code06_FakestPlayer2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_FakestPlayer2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_FakestPlayer2.n):
            jset(Code06_FakestPlayer2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code06_FakestPlayer2.build(1, Code06_FakestPlayer2.n, 1)
        Code06_FakestPlayer2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        op = 0
        l = 0
        r = 0
        x = 0
        while (i <= Code06_FakestPlayer2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                x = jcast('int', jcall(in_, 'nextInt'))
                Code06_FakestPlayer2.add(l, r, x, 1, Code06_FakestPlayer2.n, 1)
            else:
                if (op == 2):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    Code06_FakestPlayer2.setMax(l, r, x, 1, Code06_FakestPlayer2.n, 1)
                else:
                    if (op == 3):
                        x = jcast('int', jcall(in_, 'nextInt'))
                        Code06_FakestPlayer2.setMin(l, r, x, 1, Code06_FakestPlayer2.n, 1)
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code06_FakestPlayer2.querySum(l, r, 1, Code06_FakestPlayer2.n, 1))
                        else:
                            if (op == 5):
                                jcall(out, 'println', Code06_FakestPlayer2.queryMax(l, r, 1, Code06_FakestPlayer2.n, 1))
                            else:
                                jcall(out, 'println', Code06_FakestPlayer2.queryMin(l, r, 1, Code06_FakestPlayer2.n, 1))
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
            raise TypeError("No matching overload for Code06_FakestPlayer2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_FakestPlayer2.MAXN = jcast('int', 500001)
Code06_FakestPlayer2.INF = jcast('int', 1000000001)
Code06_FakestPlayer2.n = jcast('int', 0)
Code06_FakestPlayer2.m = jcast('int', 0)
Code06_FakestPlayer2.arr = jarray('int', [Code06_FakestPlayer2.MAXN])
Code06_FakestPlayer2.sum = jarray('long', [jcast('int', (Code06_FakestPlayer2.MAXN << (2 & 31)))])
Code06_FakestPlayer2.max = jarray('int', [jcast('int', (Code06_FakestPlayer2.MAXN << (2 & 31)))])
Code06_FakestPlayer2.cntMax = jarray('int', [jcast('int', (Code06_FakestPlayer2.MAXN << (2 & 31)))])
Code06_FakestPlayer2.sem = jarray('int', [jcast('int', (Code06_FakestPlayer2.MAXN << (2 & 31)))])
Code06_FakestPlayer2.min = jarray('int', [jcast('int', (Code06_FakestPlayer2.MAXN << (2 & 31)))])
Code06_FakestPlayer2.cntMin = jarray('int', [jcast('int', (Code06_FakestPlayer2.MAXN << (2 & 31)))])
Code06_FakestPlayer2.sim = jarray('int', [jcast('int', (Code06_FakestPlayer2.MAXN << (2 & 31)))])
Code06_FakestPlayer2.addTag = jarray('int', [jcast('int', (Code06_FakestPlayer2.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code06_FakestPlayer2.main([])
