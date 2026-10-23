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

# 区间最值和历史最值，Python版
# 给定两个长度都为n的数组A和B，一开始两个数组完全一样
# 任何操作做完，都更新B数组，B[i] = max(B[i],A[i])
# 实现以下五种操作，一共会调用m次
# 操作 1 l r v : A[l..r]范围上每个数加上v
# 操作 2 l r v : A[l..r]范围上每个数A[i]变成min(A[i],v)
# 操作 3 l r   : 返回A[l..r]范围上的累加和
# 操作 4 l r   : 返回A[l..r]范围上的最大值
# 操作 5 l r   : 返回B[l..r]范围上的最大值
# 1 <= n、m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P6242
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_MaximumMinimumHistory2:
    __java_fields__ = {'MAXN': 'MAXN', 'LOWEST': 'LOWEST', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sum': 'sum', 'max': 'max', 'cnt': 'cnt', 'sem': 'sem', 'maxAdd': 'maxAdd', 'otherAdd': 'otherAdd', 'maxHistory': 'maxHistory', 'maxAddTop': 'maxAddTop', 'otherAddTop': 'otherAddTop'}
    MAXN = 0
    LOWEST = 0
    n = 0
    m = 0
    arr = None
    sum = None
    max = None
    cnt = None
    sem = None
    maxAdd = None
    otherAdd = None
    # 历史最大值
    maxHistory = None
    # 最大值达到过的最大提升幅度(懒更新信息)
    maxAddTop = None
    # 除最大值以外的其他数字，达到过的最大提升幅度(懒更新信息)
    otherAddTop = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        jset(Code05_MaximumMinimumHistory2.maxHistory, i, jstatic('Math', 'max', Code05_MaximumMinimumHistory2.maxHistory[l], Code05_MaximumMinimumHistory2.maxHistory[r]))
        Code05_MaximumMinimumHistory2.sum[i] = jcast('long', jcast('long', jadd(Code05_MaximumMinimumHistory2.sum[l], Code05_MaximumMinimumHistory2.sum[r])))
        jset(Code05_MaximumMinimumHistory2.max, i, jstatic('Math', 'max', Code05_MaximumMinimumHistory2.max[l], Code05_MaximumMinimumHistory2.max[r]))
        if (Code05_MaximumMinimumHistory2.max[l] > Code05_MaximumMinimumHistory2.max[r]):
            Code05_MaximumMinimumHistory2.cnt[i] = jcast('int', Code05_MaximumMinimumHistory2.cnt[l])
            jset(Code05_MaximumMinimumHistory2.sem, i, jstatic('Math', 'max', Code05_MaximumMinimumHistory2.sem[l], Code05_MaximumMinimumHistory2.max[r]))
        else:
            if (Code05_MaximumMinimumHistory2.max[l] < Code05_MaximumMinimumHistory2.max[r]):
                Code05_MaximumMinimumHistory2.cnt[i] = jcast('int', Code05_MaximumMinimumHistory2.cnt[r])
                jset(Code05_MaximumMinimumHistory2.sem, i, jstatic('Math', 'max', Code05_MaximumMinimumHistory2.max[l], Code05_MaximumMinimumHistory2.sem[r]))
            else:
                Code05_MaximumMinimumHistory2.cnt[i] = jcast('int', jcast('int', jadd(Code05_MaximumMinimumHistory2.cnt[l], Code05_MaximumMinimumHistory2.cnt[r])))
                jset(Code05_MaximumMinimumHistory2.sem, i, jstatic('Math', 'max', Code05_MaximumMinimumHistory2.sem[l], Code05_MaximumMinimumHistory2.sem[r]))

    # maxAddv   : 最大值增加多少
    # otherAddv : 其他数增加多少
    # maxUpv    : 最大值达到过的最大提升幅度
    # otherUpv  : 其他数达到过的最大提升幅度
    @staticmethod
    def lazy(i, n, maxAddv, otherAddv, maxUpv, otherUpv):
        i = jcast('int', i)
        n = jcast('int', n)
        maxAddv = jcast('long', maxAddv)
        otherAddv = jcast('long', otherAddv)
        maxUpv = jcast('long', maxUpv)
        otherUpv = jcast('long', otherUpv)
        jset(Code05_MaximumMinimumHistory2.maxHistory, i, jstatic('Math', 'max', Code05_MaximumMinimumHistory2.maxHistory[i], jcast('long', jadd(Code05_MaximumMinimumHistory2.max[i], maxUpv))))
        jset(Code05_MaximumMinimumHistory2.maxAddTop, i, jstatic('Math', 'max', Code05_MaximumMinimumHistory2.maxAddTop[i], jcast('long', jadd(Code05_MaximumMinimumHistory2.maxAdd[i], maxUpv))))
        jset(Code05_MaximumMinimumHistory2.otherAddTop, i, jstatic('Math', 'max', Code05_MaximumMinimumHistory2.otherAddTop[i], jcast('long', jadd(Code05_MaximumMinimumHistory2.otherAdd[i], otherUpv))))
        Code05_MaximumMinimumHistory2.sum[i] = jcast('long', jcast('long', jadd(Code05_MaximumMinimumHistory2.sum[i], jcast('long', jadd(jcast('long', (maxAddv * Code05_MaximumMinimumHistory2.cnt[i])), jcast('long', (otherAddv * jcast('int', (n - Code05_MaximumMinimumHistory2.cnt[i])))))))))
        Code05_MaximumMinimumHistory2.max[i] = jcast('long', jcast('long', jadd(Code05_MaximumMinimumHistory2.max[i], maxAddv)))
        Code05_MaximumMinimumHistory2.sem[i] = jcast('long', jcast('long', jadd(Code05_MaximumMinimumHistory2.sem[i], (0 if (Code05_MaximumMinimumHistory2.sem[i] == Code05_MaximumMinimumHistory2.LOWEST) else otherAddv))))
        Code05_MaximumMinimumHistory2.maxAdd[i] = jcast('long', jcast('long', jadd(Code05_MaximumMinimumHistory2.maxAdd[i], maxAddv)))
        Code05_MaximumMinimumHistory2.otherAdd[i] = jcast('long', jcast('long', jadd(Code05_MaximumMinimumHistory2.otherAdd[i], otherAddv)))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        tmp = jcast('long', jstatic('Math', 'max', Code05_MaximumMinimumHistory2.max[l], Code05_MaximumMinimumHistory2.max[r]))
        if (Code05_MaximumMinimumHistory2.max[l] == tmp):
            Code05_MaximumMinimumHistory2.lazy(l, ln, Code05_MaximumMinimumHistory2.maxAdd[i], Code05_MaximumMinimumHistory2.otherAdd[i], Code05_MaximumMinimumHistory2.maxAddTop[i], Code05_MaximumMinimumHistory2.otherAddTop[i])
        else:
            Code05_MaximumMinimumHistory2.lazy(l, ln, Code05_MaximumMinimumHistory2.otherAdd[i], Code05_MaximumMinimumHistory2.otherAdd[i], Code05_MaximumMinimumHistory2.otherAddTop[i], Code05_MaximumMinimumHistory2.otherAddTop[i])
        if (Code05_MaximumMinimumHistory2.max[r] == tmp):
            Code05_MaximumMinimumHistory2.lazy(r, rn, Code05_MaximumMinimumHistory2.maxAdd[i], Code05_MaximumMinimumHistory2.otherAdd[i], Code05_MaximumMinimumHistory2.maxAddTop[i], Code05_MaximumMinimumHistory2.otherAddTop[i])
        else:
            Code05_MaximumMinimumHistory2.lazy(r, rn, Code05_MaximumMinimumHistory2.otherAdd[i], Code05_MaximumMinimumHistory2.otherAdd[i], Code05_MaximumMinimumHistory2.otherAddTop[i], Code05_MaximumMinimumHistory2.otherAddTop[i])
        jset(Code05_MaximumMinimumHistory2.maxAdd, i, jset(Code05_MaximumMinimumHistory2.otherAdd, i, jset(Code05_MaximumMinimumHistory2.maxAddTop, i, jset(Code05_MaximumMinimumHistory2.otherAddTop, i, 0))))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code05_MaximumMinimumHistory2.sum, i, jset(Code05_MaximumMinimumHistory2.max, i, jset(Code05_MaximumMinimumHistory2.maxHistory, i, Code05_MaximumMinimumHistory2.arr[l])))
            Code05_MaximumMinimumHistory2.sem[i] = jcast('long', Code05_MaximumMinimumHistory2.LOWEST)
            Code05_MaximumMinimumHistory2.cnt[i] = jcast('int', 1)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_MaximumMinimumHistory2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code05_MaximumMinimumHistory2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_MaximumMinimumHistory2.up(i)
        jset(Code05_MaximumMinimumHistory2.maxAdd, i, jset(Code05_MaximumMinimumHistory2.otherAdd, i, jset(Code05_MaximumMinimumHistory2.maxAddTop, i, jset(Code05_MaximumMinimumHistory2.otherAddTop, i, 0))))

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_MaximumMinimumHistory2.lazy(i, jcast('int', jadd(jcast('int', (r - l)), 1)), jobv, jobv, jobv, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_MaximumMinimumHistory2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code05_MaximumMinimumHistory2.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_MaximumMinimumHistory2.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_MaximumMinimumHistory2.up(i)

    @staticmethod
    def setMin(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobv >= Code05_MaximumMinimumHistory2.max[i]):
            return
        if (((jobl <= l) and (r <= jobr)) and (Code05_MaximumMinimumHistory2.sem[i] < jobv)):
            Code05_MaximumMinimumHistory2.lazy(i, jcast('int', jadd(jcast('int', (r - l)), 1)), jcast('long', (jobv - Code05_MaximumMinimumHistory2.max[i])), 0, jcast('long', (jobv - Code05_MaximumMinimumHistory2.max[i])), 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_MaximumMinimumHistory2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code05_MaximumMinimumHistory2.setMin(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_MaximumMinimumHistory2.setMin(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_MaximumMinimumHistory2.up(i)

    @staticmethod
    def querySum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code05_MaximumMinimumHistory2.sum[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_MaximumMinimumHistory2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            ans = jcast('long', 0)
            if (jobl <= mid):
                ans = jcast('long', jcast('long', jadd(ans, Code05_MaximumMinimumHistory2.querySum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
            if (jobr > mid):
                ans = jcast('long', jcast('long', jadd(ans, Code05_MaximumMinimumHistory2.querySum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
            return jcast('long', ans)

    @staticmethod
    def queryMax(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code05_MaximumMinimumHistory2.max[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_MaximumMinimumHistory2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            ans = Code05_MaximumMinimumHistory2.LOWEST
            if (jobl <= mid):
                ans = jstatic('Math', 'max', ans, Code05_MaximumMinimumHistory2.queryMax(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))
            if (jobr > mid):
                ans = jstatic('Math', 'max', ans, Code05_MaximumMinimumHistory2.queryMax(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))
            return jcast('long', ans)

    @staticmethod
    def queryHistoryMax(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code05_MaximumMinimumHistory2.maxHistory[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_MaximumMinimumHistory2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            ans = Code05_MaximumMinimumHistory2.LOWEST
            if (jobl <= mid):
                ans = jstatic('Math', 'max', ans, Code05_MaximumMinimumHistory2.queryHistoryMax(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))
            if (jobr > mid):
                ans = jstatic('Math', 'max', ans, Code05_MaximumMinimumHistory2.queryHistoryMax(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))
            return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code05_MaximumMinimumHistory2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_MaximumMinimumHistory2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_MaximumMinimumHistory2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_MaximumMinimumHistory2.n):
            jset(Code05_MaximumMinimumHistory2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code05_MaximumMinimumHistory2.build(1, Code05_MaximumMinimumHistory2.n, 1)
        op = 0
        jobl = 0
        jobr = 0
        jobv = 0
        i = jcast('int', 1)
        while (i <= Code05_MaximumMinimumHistory2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            jobl = jcast('int', jcall(in_, 'nextInt'))
            jobr = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                jobv = jcast('long', jcall(in_, 'nextInt'))
                Code05_MaximumMinimumHistory2.add(jobl, jobr, jobv, 1, Code05_MaximumMinimumHistory2.n, 1)
            else:
                if (op == 2):
                    jobv = jcast('long', jcall(in_, 'nextInt'))
                    Code05_MaximumMinimumHistory2.setMin(jobl, jobr, jobv, 1, Code05_MaximumMinimumHistory2.n, 1)
                else:
                    if (op == 3):
                        jcall(out, 'println', Code05_MaximumMinimumHistory2.querySum(jobl, jobr, 1, Code05_MaximumMinimumHistory2.n, 1))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code05_MaximumMinimumHistory2.queryMax(jobl, jobr, 1, Code05_MaximumMinimumHistory2.n, 1))
                        else:
                            jcall(out, 'println', Code05_MaximumMinimumHistory2.queryHistoryMax(jobl, jobr, 1, Code05_MaximumMinimumHistory2.n, 1))
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
            raise TypeError("No matching overload for Code05_MaximumMinimumHistory2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MaximumMinimumHistory2.MAXN = jcast('int', 500001)
Code05_MaximumMinimumHistory2.LOWEST = jcast('long', jget(Long, 'MIN_VALUE'))
Code05_MaximumMinimumHistory2.n = jcast('int', 0)
Code05_MaximumMinimumHistory2.m = jcast('int', 0)
Code05_MaximumMinimumHistory2.arr = jarray('int', [Code05_MaximumMinimumHistory2.MAXN])
Code05_MaximumMinimumHistory2.sum = jarray('long', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])
Code05_MaximumMinimumHistory2.max = jarray('long', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])
Code05_MaximumMinimumHistory2.cnt = jarray('int', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])
Code05_MaximumMinimumHistory2.sem = jarray('long', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])
Code05_MaximumMinimumHistory2.maxAdd = jarray('long', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])
Code05_MaximumMinimumHistory2.otherAdd = jarray('long', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])
Code05_MaximumMinimumHistory2.maxHistory = jarray('long', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])
Code05_MaximumMinimumHistory2.maxAddTop = jarray('long', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])
Code05_MaximumMinimumHistory2.otherAddTop = jarray('long', [jcast('int', (Code05_MaximumMinimumHistory2.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code05_MaximumMinimumHistory2.main([])
