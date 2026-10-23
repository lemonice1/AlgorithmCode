# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 线段树范围增加操作 + 区间最值操作
# 给定一个长度为n的数组arr，实现支持以下四种操作的结构
# 操作 0 l r x : 把arr[l..r]范围的每个数v，增加x
# 操作 1 l r x : 把arr[l..r]范围的每个数v，更新成min(v, x)
# 操作 2 l r   : 查询arr[l..r]范围上的最大值
# 操作 3 l r   : 查询arr[l..r]范围上的累加和
# 对数器验证
class Code04_SegmentTreeAddSetminQueryMaxSum:
    __java_fields__ = {'MAXN': 'MAXN', 'LOWEST': 'LOWEST', 'arr': 'arr', 'sum': 'sum', 'max': 'max', 'cnt': 'cnt', 'sem': 'sem', 'maxAdd': 'maxAdd', 'otherAdd': 'otherAdd'}
    MAXN = 0
    LOWEST = 0
    # 原始数组
    arr = None
    # 累加和信息(查询信息)
    sum = None
    # 最大值信息(只是查询信息，不再是懒更新信息，懒更新功能被maxAdd数组替代了)
    max = None
    # 最大值个数(查询信息)
    cnt = None
    # 严格次大值(查询信息)
    sem = None
    # 最大值的增加幅度(懒更新信息)
    maxAdd = None
    # 除最大值以外其他数字的增加幅度(懒更新信息)
    otherAdd = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code04_SegmentTreeAddSetminQueryMaxSum.sum[i] = jcast('long', jcast('long', jadd(Code04_SegmentTreeAddSetminQueryMaxSum.sum[l], Code04_SegmentTreeAddSetminQueryMaxSum.sum[r])))
        jset(Code04_SegmentTreeAddSetminQueryMaxSum.max, i, jstatic('Math', 'max', Code04_SegmentTreeAddSetminQueryMaxSum.max[l], Code04_SegmentTreeAddSetminQueryMaxSum.max[r]))
        if (Code04_SegmentTreeAddSetminQueryMaxSum.max[l] > Code04_SegmentTreeAddSetminQueryMaxSum.max[r]):
            Code04_SegmentTreeAddSetminQueryMaxSum.cnt[i] = jcast('int', Code04_SegmentTreeAddSetminQueryMaxSum.cnt[l])
            jset(Code04_SegmentTreeAddSetminQueryMaxSum.sem, i, jstatic('Math', 'max', Code04_SegmentTreeAddSetminQueryMaxSum.sem[l], Code04_SegmentTreeAddSetminQueryMaxSum.max[r]))
        else:
            if (Code04_SegmentTreeAddSetminQueryMaxSum.max[l] < Code04_SegmentTreeAddSetminQueryMaxSum.max[r]):
                Code04_SegmentTreeAddSetminQueryMaxSum.cnt[i] = jcast('int', Code04_SegmentTreeAddSetminQueryMaxSum.cnt[r])
                jset(Code04_SegmentTreeAddSetminQueryMaxSum.sem, i, jstatic('Math', 'max', Code04_SegmentTreeAddSetminQueryMaxSum.max[l], Code04_SegmentTreeAddSetminQueryMaxSum.sem[r]))
            else:
                Code04_SegmentTreeAddSetminQueryMaxSum.cnt[i] = jcast('int', jcast('int', jadd(Code04_SegmentTreeAddSetminQueryMaxSum.cnt[l], Code04_SegmentTreeAddSetminQueryMaxSum.cnt[r])))
                jset(Code04_SegmentTreeAddSetminQueryMaxSum.sem, i, jstatic('Math', 'max', Code04_SegmentTreeAddSetminQueryMaxSum.sem[l], Code04_SegmentTreeAddSetminQueryMaxSum.sem[r]))

    @staticmethod
    def lazy(i, n, maxAddv, otherAddv):
        i = jcast('int', i)
        n = jcast('int', n)
        maxAddv = jcast('long', maxAddv)
        otherAddv = jcast('long', otherAddv)
        Code04_SegmentTreeAddSetminQueryMaxSum.sum[i] = jcast('long', jcast('long', jadd(Code04_SegmentTreeAddSetminQueryMaxSum.sum[i], jcast('long', jadd(jcast('long', (maxAddv * Code04_SegmentTreeAddSetminQueryMaxSum.cnt[i])), jcast('long', (otherAddv * jcast('int', (n - Code04_SegmentTreeAddSetminQueryMaxSum.cnt[i])))))))))
        Code04_SegmentTreeAddSetminQueryMaxSum.max[i] = jcast('long', jcast('long', jadd(Code04_SegmentTreeAddSetminQueryMaxSum.max[i], maxAddv)))
        Code04_SegmentTreeAddSetminQueryMaxSum.sem[i] = jcast('long', jcast('long', jadd(Code04_SegmentTreeAddSetminQueryMaxSum.sem[i], (0 if (Code04_SegmentTreeAddSetminQueryMaxSum.sem[i] == Code04_SegmentTreeAddSetminQueryMaxSum.LOWEST) else otherAddv))))
        Code04_SegmentTreeAddSetminQueryMaxSum.maxAdd[i] = jcast('long', jcast('long', jadd(Code04_SegmentTreeAddSetminQueryMaxSum.maxAdd[i], maxAddv)))
        Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd[i] = jcast('long', jcast('long', jadd(Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd[i], otherAddv)))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        # 为什么拿全局最大值不写成 : tmp = max[i]
        # 因为父亲范围的最大值可能已经被懒更新任务修改过了
        # 现在希望拿的是懒更新之前的最大值
        # 子范围的max值没有修改过，所以写成 : tmp = Math.max(max[l], max[r])
        tmp = jcast('long', jstatic('Math', 'max', Code04_SegmentTreeAddSetminQueryMaxSum.max[l], Code04_SegmentTreeAddSetminQueryMaxSum.max[r]))
        if (Code04_SegmentTreeAddSetminQueryMaxSum.max[l] == tmp):
            Code04_SegmentTreeAddSetminQueryMaxSum.lazy(l, ln, Code04_SegmentTreeAddSetminQueryMaxSum.maxAdd[i], Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd[i])
        else:
            Code04_SegmentTreeAddSetminQueryMaxSum.lazy(l, ln, Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd[i], Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd[i])
        if (Code04_SegmentTreeAddSetminQueryMaxSum.max[r] == tmp):
            Code04_SegmentTreeAddSetminQueryMaxSum.lazy(r, rn, Code04_SegmentTreeAddSetminQueryMaxSum.maxAdd[i], Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd[i])
        else:
            Code04_SegmentTreeAddSetminQueryMaxSum.lazy(r, rn, Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd[i], Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd[i])
        jset(Code04_SegmentTreeAddSetminQueryMaxSum.maxAdd, i, jset(Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd, i, 0))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code04_SegmentTreeAddSetminQueryMaxSum.sum, i, jset(Code04_SegmentTreeAddSetminQueryMaxSum.max, i, Code04_SegmentTreeAddSetminQueryMaxSum.arr[l]))
            Code04_SegmentTreeAddSetminQueryMaxSum.sem[i] = jcast('long', Code04_SegmentTreeAddSetminQueryMaxSum.LOWEST)
            Code04_SegmentTreeAddSetminQueryMaxSum.cnt[i] = jcast('int', 1)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_SegmentTreeAddSetminQueryMaxSum.build(l, mid, jcast('int', (i << (1 & 31))))
            Code04_SegmentTreeAddSetminQueryMaxSum.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_SegmentTreeAddSetminQueryMaxSum.up(i)
        jset(Code04_SegmentTreeAddSetminQueryMaxSum.maxAdd, i, jset(Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd, i, 0))

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code04_SegmentTreeAddSetminQueryMaxSum.lazy(i, jcast('int', jadd(jcast('int', (r - l)), 1)), jobv, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_SegmentTreeAddSetminQueryMaxSum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code04_SegmentTreeAddSetminQueryMaxSum.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_SegmentTreeAddSetminQueryMaxSum.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_SegmentTreeAddSetminQueryMaxSum.up(i)

    @staticmethod
    def setMin(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobv >= Code04_SegmentTreeAddSetminQueryMaxSum.max[i]):
            return
        if (((jobl <= l) and (r <= jobr)) and (Code04_SegmentTreeAddSetminQueryMaxSum.sem[i] < jobv)):
            Code04_SegmentTreeAddSetminQueryMaxSum.lazy(i, jcast('int', jadd(jcast('int', (r - l)), 1)), jcast('long', (jobv - Code04_SegmentTreeAddSetminQueryMaxSum.max[i])), 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_SegmentTreeAddSetminQueryMaxSum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code04_SegmentTreeAddSetminQueryMaxSum.setMin(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_SegmentTreeAddSetminQueryMaxSum.setMin(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_SegmentTreeAddSetminQueryMaxSum.up(i)

    @staticmethod
    def querySum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code04_SegmentTreeAddSetminQueryMaxSum.sum[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_SegmentTreeAddSetminQueryMaxSum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            ans = jcast('long', 0)
            if (jobl <= mid):
                ans = jcast('long', jcast('long', jadd(ans, Code04_SegmentTreeAddSetminQueryMaxSum.querySum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
            if (jobr > mid):
                ans = jcast('long', jcast('long', jadd(ans, Code04_SegmentTreeAddSetminQueryMaxSum.querySum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
            return jcast('long', ans)

    @staticmethod
    def queryMax(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code04_SegmentTreeAddSetminQueryMaxSum.max[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_SegmentTreeAddSetminQueryMaxSum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            ans = jget(Long, 'MIN_VALUE')
            if (jobl <= mid):
                ans = jstatic('Math', 'max', ans, Code04_SegmentTreeAddSetminQueryMaxSum.queryMax(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))
            if (jobr > mid):
                ans = jstatic('Math', 'max', ans, Code04_SegmentTreeAddSetminQueryMaxSum.queryMax(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))
            return jcast('long', ans)

    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        n = jcast('int', 2000)
        v = jcast('int', 5000)
        t = jcast('int', 1000000)
        Code04_SegmentTreeAddSetminQueryMaxSum.randomArray(n, v)
        check = jarray('long', [jcast('int', jadd(n, 1))])
        i = jcast('int', 1)
        while (i <= n):
            check[i] = jcast('long', Code04_SegmentTreeAddSetminQueryMaxSum.arr[i])
            i = jcast('int', (i + 1))
        Code04_SegmentTreeAddSetminQueryMaxSum.build(1, n, 1)
        i = jcast('int', 1)
        op = 0
        a = 0
        b = 0
        jobl = 0
        jobr = 0
        jobv = 0
        while (i <= t):
            op = jcast('int', jcast('int', (jstatic('Math', 'random') * 4)))
            a = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            b = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            jobl = jcast('int', jstatic('Math', 'min', a, b))
            jobr = jcast('int', jstatic('Math', 'max', a, b))
            if (op == 0):
                jobv = jcast('int', jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
                Code04_SegmentTreeAddSetminQueryMaxSum.add(jobl, jobr, jobv, 1, n, 1)
                Code04_SegmentTreeAddSetminQueryMaxSum.checkAdd(check, jobl, jobr, jobv)
            else:
                if (op == 1):
                    jobv = jcast('int', jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
                    Code04_SegmentTreeAddSetminQueryMaxSum.setMin(jobl, jobr, jobv, 1, n, 1)
                    Code04_SegmentTreeAddSetminQueryMaxSum.checkSetMin(check, jobl, jobr, jobv)
                else:
                    if (op == 2):
                        ans1 = jcast('long', Code04_SegmentTreeAddSetminQueryMaxSum.queryMax(jobl, jobr, 1, n, 1))
                        ans2 = jcast('long', Code04_SegmentTreeAddSetminQueryMaxSum.checkQueryMax(check, jobl, jobr))
                        if (ans1 != ans2):
                            jprint('出错了!', newline=True)
                    else:
                        ans1 = jcast('long', Code04_SegmentTreeAddSetminQueryMaxSum.querySum(jobl, jobr, 1, n, 1))
                        ans2 = jcast('long', Code04_SegmentTreeAddSetminQueryMaxSum.checkQuerySum(check, jobl, jobr))
                        if (ans1 != ans2):
                            jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    # 为了验证
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        i = jcast('int', 1)
        while (i <= n):
            jset(Code04_SegmentTreeAddSetminQueryMaxSum.arr, i, jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
            i = jcast('int', (i + 1))

    # 为了验证
    @staticmethod
    def checkAdd(check, jobl, jobr, jobv):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        i = jcast('int', jobl)
        while (i <= jobr):
            check[i] = jcast('long', jcast('long', jadd(check[i], jobv)))
            i = jcast('int', (i + 1))

    # 为了验证
    @staticmethod
    def checkSetMin(check, jobl, jobr, jobv):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        i = jcast('int', jobl)
        while (i <= jobr):
            jset(check, i, jstatic('Math', 'min', check[i], jobv))
            i = jcast('int', (i + 1))

    # 为了验证
    @staticmethod
    def checkQueryMax(check, jobl, jobr):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        ans = jcast('long', jget(Long, 'MIN_VALUE'))
        i = jcast('int', jobl)
        while (i <= jobr):
            ans = jcast('long', jstatic('Math', 'max', ans, check[i]))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    # 为了验证
    @staticmethod
    def checkQuerySum(check, jobl, jobr):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        ans = jcast('long', 0)
        i = jcast('int', jobl)
        while (i <= jobr):
            ans = jcast('long', jcast('long', jadd(ans, check[i])))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_SegmentTreeAddSetminQueryMaxSum.MAXN = jcast('int', 500001)
Code04_SegmentTreeAddSetminQueryMaxSum.LOWEST = jcast('long', jget(Long, 'MIN_VALUE'))
Code04_SegmentTreeAddSetminQueryMaxSum.arr = jarray('int', [Code04_SegmentTreeAddSetminQueryMaxSum.MAXN])
Code04_SegmentTreeAddSetminQueryMaxSum.sum = jarray('long', [jcast('int', (Code04_SegmentTreeAddSetminQueryMaxSum.MAXN << (2 & 31)))])
Code04_SegmentTreeAddSetminQueryMaxSum.max = jarray('long', [jcast('int', (Code04_SegmentTreeAddSetminQueryMaxSum.MAXN << (2 & 31)))])
Code04_SegmentTreeAddSetminQueryMaxSum.cnt = jarray('int', [jcast('int', (Code04_SegmentTreeAddSetminQueryMaxSum.MAXN << (2 & 31)))])
Code04_SegmentTreeAddSetminQueryMaxSum.sem = jarray('long', [jcast('int', (Code04_SegmentTreeAddSetminQueryMaxSum.MAXN << (2 & 31)))])
Code04_SegmentTreeAddSetminQueryMaxSum.maxAdd = jarray('long', [jcast('int', (Code04_SegmentTreeAddSetminQueryMaxSum.MAXN << (2 & 31)))])
Code04_SegmentTreeAddSetminQueryMaxSum.otherAdd = jarray('long', [jcast('int', (Code04_SegmentTreeAddSetminQueryMaxSum.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code04_SegmentTreeAddSetminQueryMaxSum.main([])
