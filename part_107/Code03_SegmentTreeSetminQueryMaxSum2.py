# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 线段树的区间最值操作(hdu测试)
# 给定一个长度为n的数组arr，实现支持以下三种操作的结构
# 操作 0 l r x : 把arr[l..r]范围的每个数v，更新成min(v, x)
# 操作 1 l r   : 查询arr[l..r]范围上的最大值
# 操作 2 l r   : 查询arr[l..r]范围上的累加和
# 三种操作一共调用m次，做到时间复杂度O(n * log n + m * log n)
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=5306
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_SegmentTreeSetminQueryMaxSum2:
    __java_fields__ = {'MAXN': 'MAXN', 'LOWEST': 'LOWEST', 'sum': 'sum', 'max': 'max', 'cnt': 'cnt', 'sem': 'sem', 'br': 'br', 'in': 'in_', 'out': 'out'}
    MAXN = 0
    LOWEST = 0
    sum = None
    max = None
    cnt = None
    sem = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code03_SegmentTreeSetminQueryMaxSum2.sum[i] = jcast('long', jcast('long', jadd(Code03_SegmentTreeSetminQueryMaxSum2.sum[l], Code03_SegmentTreeSetminQueryMaxSum2.sum[r])))
        jset(Code03_SegmentTreeSetminQueryMaxSum2.max, i, jstatic('Math', 'max', Code03_SegmentTreeSetminQueryMaxSum2.max[l], Code03_SegmentTreeSetminQueryMaxSum2.max[r]))
        if (Code03_SegmentTreeSetminQueryMaxSum2.max[l] > Code03_SegmentTreeSetminQueryMaxSum2.max[r]):
            Code03_SegmentTreeSetminQueryMaxSum2.cnt[i] = jcast('int', Code03_SegmentTreeSetminQueryMaxSum2.cnt[l])
            jset(Code03_SegmentTreeSetminQueryMaxSum2.sem, i, jstatic('Math', 'max', Code03_SegmentTreeSetminQueryMaxSum2.sem[l], Code03_SegmentTreeSetminQueryMaxSum2.max[r]))
        else:
            if (Code03_SegmentTreeSetminQueryMaxSum2.max[l] < Code03_SegmentTreeSetminQueryMaxSum2.max[r]):
                Code03_SegmentTreeSetminQueryMaxSum2.cnt[i] = jcast('int', Code03_SegmentTreeSetminQueryMaxSum2.cnt[r])
                jset(Code03_SegmentTreeSetminQueryMaxSum2.sem, i, jstatic('Math', 'max', Code03_SegmentTreeSetminQueryMaxSum2.max[l], Code03_SegmentTreeSetminQueryMaxSum2.sem[r]))
            else:
                Code03_SegmentTreeSetminQueryMaxSum2.cnt[i] = jcast('int', jcast('int', jadd(Code03_SegmentTreeSetminQueryMaxSum2.cnt[l], Code03_SegmentTreeSetminQueryMaxSum2.cnt[r])))
                jset(Code03_SegmentTreeSetminQueryMaxSum2.sem, i, jstatic('Math', 'max', Code03_SegmentTreeSetminQueryMaxSum2.sem[l], Code03_SegmentTreeSetminQueryMaxSum2.sem[r]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        Code03_SegmentTreeSetminQueryMaxSum2.lazy(jcast('int', (i << (1 & 31))), Code03_SegmentTreeSetminQueryMaxSum2.max[i])
        Code03_SegmentTreeSetminQueryMaxSum2.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code03_SegmentTreeSetminQueryMaxSum2.max[i])

    # 一定是没有颠覆掉次大值的懒更新信息下发，也就是说：
    # 最大值被压成v，并且v > 严格次大值的情况下
    # sum和max怎么调整
    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        if (v < Code03_SegmentTreeSetminQueryMaxSum2.max[i]):
            Code03_SegmentTreeSetminQueryMaxSum2.sum[i] = jcast('long', jcast('long', (Code03_SegmentTreeSetminQueryMaxSum2.sum[i] - jcast('long', (jcast('long', (jcast('long', Code03_SegmentTreeSetminQueryMaxSum2.max[i]) - v)) * Code03_SegmentTreeSetminQueryMaxSum2.cnt[i])))))
            Code03_SegmentTreeSetminQueryMaxSum2.max[i] = jcast('int', v)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            # 不能生成原始数组然后build
            # 因为这道题空间非常极限
            # 生成原始数组然后build
            # 空间就是会超过限制
            # 所以build的过程直接从输入流读入
            # 一般情况下不会这么极限的
            jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
            jset(Code03_SegmentTreeSetminQueryMaxSum2.sum, i, jset(Code03_SegmentTreeSetminQueryMaxSum2.max, i, jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval'))))
            Code03_SegmentTreeSetminQueryMaxSum2.cnt[i] = jcast('int', 1)
            Code03_SegmentTreeSetminQueryMaxSum2.sem[i] = jcast('int', Code03_SegmentTreeSetminQueryMaxSum2.LOWEST)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_SegmentTreeSetminQueryMaxSum2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code03_SegmentTreeSetminQueryMaxSum2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_SegmentTreeSetminQueryMaxSum2.up(i)

    @staticmethod
    def setMin(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobv >= Code03_SegmentTreeSetminQueryMaxSum2.max[i]):
            return
        if (((jobl <= l) and (r <= jobr)) and (Code03_SegmentTreeSetminQueryMaxSum2.sem[i] < jobv)):
            Code03_SegmentTreeSetminQueryMaxSum2.lazy(i, jobv)
        else:
            Code03_SegmentTreeSetminQueryMaxSum2.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code03_SegmentTreeSetminQueryMaxSum2.setMin(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_SegmentTreeSetminQueryMaxSum2.setMin(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_SegmentTreeSetminQueryMaxSum2.up(i)

    @staticmethod
    def queryMax(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code03_SegmentTreeSetminQueryMaxSum2.max[i])
        Code03_SegmentTreeSetminQueryMaxSum2.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_SegmentTreeSetminQueryMaxSum2.queryMax(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_SegmentTreeSetminQueryMaxSum2.queryMax(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def querySum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code03_SegmentTreeSetminQueryMaxSum2.sum[i])
        Code03_SegmentTreeSetminQueryMaxSum2.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_SegmentTreeSetminQueryMaxSum2.querySum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_SegmentTreeSetminQueryMaxSum2.querySum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('long', ans)

    # 为了不生成原始数组
    # 让build函数可以直接从输入流拿数据
    # 所以把输入输出流定义成全局静态变量
    br = None
    in_ = None
    out = None
    @staticmethod
    def main(args):
        jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
        testCases = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
        t = jcast('int', 1)
        while (t <= testCases):
            jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
            n = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
            jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
            m = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
            Code03_SegmentTreeSetminQueryMaxSum2.build(1, n, 1)
            i = jcast('int', 1)
            op = 0
            jobl = 0
            jobr = 0
            jobv = 0
            while (i <= m):
                jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
                op = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
                if (op == 0):
                    jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
                    jobl = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
                    jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
                    jobr = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
                    jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
                    jobv = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
                    Code03_SegmentTreeSetminQueryMaxSum2.setMin(jobl, jobr, jobv, 1, n, 1)
                else:
                    if (op == 1):
                        jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
                        jobl = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
                        jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
                        jobr = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
                        jcall(Code03_SegmentTreeSetminQueryMaxSum2.out, 'println', Code03_SegmentTreeSetminQueryMaxSum2.queryMax(jobl, jobr, 1, n, 1))
                    else:
                        jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
                        jobl = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
                        jcall(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nextToken')
                        jobr = jcast('int', jcast('int', jget(Code03_SegmentTreeSetminQueryMaxSum2.in_, 'nval')))
                        jcall(Code03_SegmentTreeSetminQueryMaxSum2.out, 'println', Code03_SegmentTreeSetminQueryMaxSum2.querySum(jobl, jobr, 1, n, 1))
                i = jcast('int', (i + 1))
            t = jcast('int', (t + 1))
        jcall(Code03_SegmentTreeSetminQueryMaxSum2.out, 'flush')
        jcall(Code03_SegmentTreeSetminQueryMaxSum2.out, 'close')
        jcall(Code03_SegmentTreeSetminQueryMaxSum2.br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SegmentTreeSetminQueryMaxSum2.MAXN = jcast('int', 1000001)
Code03_SegmentTreeSetminQueryMaxSum2.LOWEST = jcast('int', jcast('int', (-1)))
Code03_SegmentTreeSetminQueryMaxSum2.sum = jarray('long', [jcast('int', (Code03_SegmentTreeSetminQueryMaxSum2.MAXN << (2 & 31)))])
Code03_SegmentTreeSetminQueryMaxSum2.max = jarray('int', [jcast('int', (Code03_SegmentTreeSetminQueryMaxSum2.MAXN << (2 & 31)))])
Code03_SegmentTreeSetminQueryMaxSum2.cnt = jarray('int', [jcast('int', (Code03_SegmentTreeSetminQueryMaxSum2.MAXN << (2 & 31)))])
Code03_SegmentTreeSetminQueryMaxSum2.sem = jarray('int', [jcast('int', (Code03_SegmentTreeSetminQueryMaxSum2.MAXN << (2 & 31)))])
Code03_SegmentTreeSetminQueryMaxSum2.br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
Code03_SegmentTreeSetminQueryMaxSum2.in_ = jnew('StreamTokenizer', Code03_SegmentTreeSetminQueryMaxSum2.br)
Code03_SegmentTreeSetminQueryMaxSum2.out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))

if __name__ == '__main__':
    Code03_SegmentTreeSetminQueryMaxSum2.main([])
