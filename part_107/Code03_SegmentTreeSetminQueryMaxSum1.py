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

# 线段树的区间最值操作
# 给定一个长度为n的数组arr，实现支持以下三种操作的结构
# 操作 0 l r x : 把arr[l..r]范围的每个数v，更新成min(v, x)
# 操作 1 l r   : 查询arr[l..r]范围上的最大值
# 操作 2 l r   : 查询arr[l..r]范围上的累加和
# 三种操作一共调用m次，做到时间复杂度O(n * log n + m * log n)
# 对数器验证
class Code03_SegmentTreeSetminQueryMaxSum1:
    __java_fields__ = {'MAXN': 'MAXN', 'LOWEST': 'LOWEST', 'arr': 'arr', 'sum': 'sum', 'max': 'max', 'cnt': 'cnt', 'sem': 'sem'}
    MAXN = 0
    # 假设初始数组中的值不会出现比LOWEST还小的值
    # 假设更新操作时jobv的数值也不会出现比LOWEST还小的值
    LOWEST = 0
    # 原始数组
    arr = None
    # 累加和
    sum = None
    # 最大值(既是查询信息也是懒更新信息，课上已经讲解了)
    max = None
    # 最大值个数
    cnt = None
    # 严格次大值(second max)
    sem = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code03_SegmentTreeSetminQueryMaxSum1.sum[i] = jcast('long', jcast('long', jadd(Code03_SegmentTreeSetminQueryMaxSum1.sum[l], Code03_SegmentTreeSetminQueryMaxSum1.sum[r])))
        jset(Code03_SegmentTreeSetminQueryMaxSum1.max, i, jstatic('Math', 'max', Code03_SegmentTreeSetminQueryMaxSum1.max[l], Code03_SegmentTreeSetminQueryMaxSum1.max[r]))
        if (Code03_SegmentTreeSetminQueryMaxSum1.max[l] > Code03_SegmentTreeSetminQueryMaxSum1.max[r]):
            Code03_SegmentTreeSetminQueryMaxSum1.cnt[i] = jcast('int', Code03_SegmentTreeSetminQueryMaxSum1.cnt[l])
            jset(Code03_SegmentTreeSetminQueryMaxSum1.sem, i, jstatic('Math', 'max', Code03_SegmentTreeSetminQueryMaxSum1.sem[l], Code03_SegmentTreeSetminQueryMaxSum1.max[r]))
        else:
            if (Code03_SegmentTreeSetminQueryMaxSum1.max[l] < Code03_SegmentTreeSetminQueryMaxSum1.max[r]):
                Code03_SegmentTreeSetminQueryMaxSum1.cnt[i] = jcast('int', Code03_SegmentTreeSetminQueryMaxSum1.cnt[r])
                jset(Code03_SegmentTreeSetminQueryMaxSum1.sem, i, jstatic('Math', 'max', Code03_SegmentTreeSetminQueryMaxSum1.max[l], Code03_SegmentTreeSetminQueryMaxSum1.sem[r]))
            else:
                Code03_SegmentTreeSetminQueryMaxSum1.cnt[i] = jcast('int', jcast('int', jadd(Code03_SegmentTreeSetminQueryMaxSum1.cnt[l], Code03_SegmentTreeSetminQueryMaxSum1.cnt[r])))
                jset(Code03_SegmentTreeSetminQueryMaxSum1.sem, i, jstatic('Math', 'max', Code03_SegmentTreeSetminQueryMaxSum1.sem[l], Code03_SegmentTreeSetminQueryMaxSum1.sem[r]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        Code03_SegmentTreeSetminQueryMaxSum1.lazy(jcast('int', (i << (1 & 31))), Code03_SegmentTreeSetminQueryMaxSum1.max[i])
        Code03_SegmentTreeSetminQueryMaxSum1.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code03_SegmentTreeSetminQueryMaxSum1.max[i])

    # 一定是没有颠覆掉次大值的懒更新信息下发，也就是说：
    # 最大值被压成v，并且v > 严格次大值的情况下
    # sum和max怎么调整
    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        if (v < Code03_SegmentTreeSetminQueryMaxSum1.max[i]):
            Code03_SegmentTreeSetminQueryMaxSum1.sum[i] = jcast('long', jcast('long', (Code03_SegmentTreeSetminQueryMaxSum1.sum[i] - jcast('long', (jcast('long', (jcast('long', Code03_SegmentTreeSetminQueryMaxSum1.max[i]) - v)) * Code03_SegmentTreeSetminQueryMaxSum1.cnt[i])))))
            Code03_SegmentTreeSetminQueryMaxSum1.max[i] = jcast('int', v)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code03_SegmentTreeSetminQueryMaxSum1.sum, i, jset(Code03_SegmentTreeSetminQueryMaxSum1.max, i, Code03_SegmentTreeSetminQueryMaxSum1.arr[l]))
            Code03_SegmentTreeSetminQueryMaxSum1.cnt[i] = jcast('int', 1)
            Code03_SegmentTreeSetminQueryMaxSum1.sem[i] = jcast('int', Code03_SegmentTreeSetminQueryMaxSum1.LOWEST)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_SegmentTreeSetminQueryMaxSum1.build(l, mid, jcast('int', (i << (1 & 31))))
            Code03_SegmentTreeSetminQueryMaxSum1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_SegmentTreeSetminQueryMaxSum1.up(i)

    @staticmethod
    def setMin(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobv >= Code03_SegmentTreeSetminQueryMaxSum1.max[i]):
            return
        if (((jobl <= l) and (r <= jobr)) and (Code03_SegmentTreeSetminQueryMaxSum1.sem[i] < jobv)):
            Code03_SegmentTreeSetminQueryMaxSum1.lazy(i, jobv)
        else:
            # 1) 任务没有全包
            # 2) jobv <= sem[i]
            Code03_SegmentTreeSetminQueryMaxSum1.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code03_SegmentTreeSetminQueryMaxSum1.setMin(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_SegmentTreeSetminQueryMaxSum1.setMin(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_SegmentTreeSetminQueryMaxSum1.up(i)

    @staticmethod
    def queryMax(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code03_SegmentTreeSetminQueryMaxSum1.max[i])
        Code03_SegmentTreeSetminQueryMaxSum1.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_SegmentTreeSetminQueryMaxSum1.queryMax(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_SegmentTreeSetminQueryMaxSum1.queryMax(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def querySum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code03_SegmentTreeSetminQueryMaxSum1.sum[i])
        Code03_SegmentTreeSetminQueryMaxSum1.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_SegmentTreeSetminQueryMaxSum1.querySum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_SegmentTreeSetminQueryMaxSum1.querySum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        n = jcast('int', 2000)
        v = jcast('int', 5000)
        t = jcast('int', 1000000)
        Code03_SegmentTreeSetminQueryMaxSum1.randomArray(n, v)
        check = jarray('int', [jcast('int', jadd(n, 1))])
        i = jcast('int', 1)
        while (i <= n):
            check[i] = jcast('int', Code03_SegmentTreeSetminQueryMaxSum1.arr[i])
            i = jcast('int', (i + 1))
        Code03_SegmentTreeSetminQueryMaxSum1.build(1, n, 1)
        i = jcast('int', 1)
        op = 0
        a = 0
        b = 0
        jobl = 0
        jobr = 0
        jobv = 0
        while (i <= t):
            op = jcast('int', jcast('int', (jstatic('Math', 'random') * 3)))
            a = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            b = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            jobl = jcast('int', jstatic('Math', 'min', a, b))
            jobr = jcast('int', jstatic('Math', 'max', a, b))
            if (op == 0):
                jobv = jcast('int', jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
                Code03_SegmentTreeSetminQueryMaxSum1.setMin(jobl, jobr, jobv, 1, n, 1)
                Code03_SegmentTreeSetminQueryMaxSum1.checkSetMin(check, jobl, jobr, jobv)
            else:
                if (op == 1):
                    ans1 = jcast('int', Code03_SegmentTreeSetminQueryMaxSum1.queryMax(jobl, jobr, 1, n, 1))
                    ans2 = jcast('int', Code03_SegmentTreeSetminQueryMaxSum1.checkQueryMax(check, jobl, jobr))
                    if (ans1 != ans2):
                        jprint('出错了!', newline=True)
                else:
                    ans1 = jcast('long', Code03_SegmentTreeSetminQueryMaxSum1.querySum(jobl, jobr, 1, n, 1))
                    ans2 = jcast('long', Code03_SegmentTreeSetminQueryMaxSum1.checkQuerySum(check, jobl, jobr))
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
            jset(Code03_SegmentTreeSetminQueryMaxSum1.arr, i, jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
            i = jcast('int', (i + 1))

    # 为了验证
    @staticmethod
    def checkSetMin(check, jobl, jobr, jobv):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        i = jcast('int', jobl)
        while (i <= jobr):
            jset(check, i, jstatic('Math', 'min', check[i], jobv))
            i = jcast('int', (i + 1))

    # 为了验证
    @staticmethod
    def checkQueryMax(check, jobl, jobr):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', jobl)
        while (i <= jobr):
            ans = jcast('int', jstatic('Math', 'max', ans, check[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

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


Code03_SegmentTreeSetminQueryMaxSum1.MAXN = jcast('int', 100001)
Code03_SegmentTreeSetminQueryMaxSum1.LOWEST = jcast('int', jcast('int', (-100001)))
Code03_SegmentTreeSetminQueryMaxSum1.arr = jarray('int', [Code03_SegmentTreeSetminQueryMaxSum1.MAXN])
Code03_SegmentTreeSetminQueryMaxSum1.sum = jarray('long', [jcast('int', (Code03_SegmentTreeSetminQueryMaxSum1.MAXN << (2 & 31)))])
Code03_SegmentTreeSetminQueryMaxSum1.max = jarray('int', [jcast('int', (Code03_SegmentTreeSetminQueryMaxSum1.MAXN << (2 & 31)))])
Code03_SegmentTreeSetminQueryMaxSum1.cnt = jarray('int', [jcast('int', (Code03_SegmentTreeSetminQueryMaxSum1.MAXN << (2 & 31)))])
Code03_SegmentTreeSetminQueryMaxSum1.sem = jarray('int', [jcast('int', (Code03_SegmentTreeSetminQueryMaxSum1.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code03_SegmentTreeSetminQueryMaxSum1.main([])
