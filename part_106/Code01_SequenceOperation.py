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

# 序列操作
# 给定一个长度为n的数组arr，内部只有01两种值，下标从0开始
# 对于这个序列有五种变换操作和询问操作
# 操作 0 l r : 把l~r范围上所有数字全改成0
# 操作 1 l r : 把l~r范围上所有数字全改成1
# 操作 2 l r : 把l~r范围上所有数字全取反
# 操作 3 l r : 询问l~r范围上有多少个1
# 操作 4 l r : 询问l~r范围上连续1的最长子串长度
# 测试链接 : https://www.luogu.com.cn/problem/P2572
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_SequenceOperation:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum': 'sum', 'len0': 'len0', 'pre0': 'pre0', 'suf0': 'suf0', 'len1': 'len1', 'pre1': 'pre1', 'suf1': 'suf1', 'change': 'change', 'update': 'update_data', 'reverse': 'reverse_data'}
    MAXN = 0
    # 原始数组
    arr = None
    # 累加和用来统计1的数量
    sum = None
    # 连续0的最长子串长度
    len0 = None
    # 连续0的最长前缀长度
    pre0 = None
    # 连续0的最长后缀长度
    suf0 = None
    # 连续1的最长子串长度
    len1 = None
    # 连续1的最长前缀长度
    pre1 = None
    # 连续1的最长后缀长度
    suf1 = None
    # 懒更新信息，范围上所有数字被重置成了什么
    change = None
    # 懒更新信息，范围上有没有重置任务
    update_data = None
    # 懒更新信息，范围上有没有翻转任务
    reverse_data = None
    @staticmethod
    def up(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code01_SequenceOperation.sum[i] = jcast('int', jcast('int', jadd(Code01_SequenceOperation.sum[l], Code01_SequenceOperation.sum[r])))
        jset(Code01_SequenceOperation.len0, i, jstatic('Math', 'max', jstatic('Math', 'max', Code01_SequenceOperation.len0[l], Code01_SequenceOperation.len0[r]), jcast('int', jadd(Code01_SequenceOperation.suf0[l], Code01_SequenceOperation.pre0[r]))))
        Code01_SequenceOperation.pre0[i] = jcast('int', (Code01_SequenceOperation.pre0[l] if (Code01_SequenceOperation.len0[l] < ln) else jcast('int', jadd(Code01_SequenceOperation.pre0[l], Code01_SequenceOperation.pre0[r]))))
        Code01_SequenceOperation.suf0[i] = jcast('int', (Code01_SequenceOperation.suf0[r] if (Code01_SequenceOperation.len0[r] < rn) else jcast('int', jadd(Code01_SequenceOperation.suf0[l], Code01_SequenceOperation.suf0[r]))))
        jset(Code01_SequenceOperation.len1, i, jstatic('Math', 'max', jstatic('Math', 'max', Code01_SequenceOperation.len1[l], Code01_SequenceOperation.len1[r]), jcast('int', jadd(Code01_SequenceOperation.suf1[l], Code01_SequenceOperation.pre1[r]))))
        Code01_SequenceOperation.pre1[i] = jcast('int', (Code01_SequenceOperation.pre1[l] if (Code01_SequenceOperation.len1[l] < ln) else jcast('int', jadd(Code01_SequenceOperation.pre1[l], Code01_SequenceOperation.pre1[r]))))
        Code01_SequenceOperation.suf1[i] = jcast('int', (Code01_SequenceOperation.suf1[r] if (Code01_SequenceOperation.len1[r] < rn) else jcast('int', jadd(Code01_SequenceOperation.suf1[l], Code01_SequenceOperation.suf1[r]))))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if Code01_SequenceOperation.update_data[i]:
            Code01_SequenceOperation.updateLazy(jcast('int', (i << (1 & 31))), Code01_SequenceOperation.change[i], ln)
            Code01_SequenceOperation.updateLazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code01_SequenceOperation.change[i], rn)
            Code01_SequenceOperation.update_data[i] = jcast('boolean', False)
        if Code01_SequenceOperation.reverse_data[i]:
            Code01_SequenceOperation.reverseLazy(jcast('int', (i << (1 & 31))), ln)
            Code01_SequenceOperation.reverseLazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), rn)
            Code01_SequenceOperation.reverse_data[i] = jcast('boolean', False)

    @staticmethod
    def updateLazy(i, v, n):
        i = jcast('int', i)
        v = jcast('int', v)
        n = jcast('int', n)
        Code01_SequenceOperation.sum[i] = jcast('int', jcast('int', (v * n)))
        jset(Code01_SequenceOperation.len0, i, jset(Code01_SequenceOperation.pre0, i, jset(Code01_SequenceOperation.suf0, i, (n if (v == 0) else 0))))
        jset(Code01_SequenceOperation.len1, i, jset(Code01_SequenceOperation.pre1, i, jset(Code01_SequenceOperation.suf1, i, (n if (v == 1) else 0))))
        Code01_SequenceOperation.change[i] = jcast('int', v)
        Code01_SequenceOperation.update_data[i] = jcast('boolean', True)
        Code01_SequenceOperation.reverse_data[i] = jcast('boolean', False)

    @staticmethod
    def reverseLazy(i, n):
        i = jcast('int', i)
        n = jcast('int', n)
        Code01_SequenceOperation.sum[i] = jcast('int', jcast('int', (n - Code01_SequenceOperation.sum[i])))
        tmp = 0
        tmp = jcast('int', Code01_SequenceOperation.len0[i])
        Code01_SequenceOperation.len0[i] = jcast('int', Code01_SequenceOperation.len1[i])
        Code01_SequenceOperation.len1[i] = jcast('int', tmp)
        tmp = jcast('int', Code01_SequenceOperation.pre0[i])
        Code01_SequenceOperation.pre0[i] = jcast('int', Code01_SequenceOperation.pre1[i])
        Code01_SequenceOperation.pre1[i] = jcast('int', tmp)
        tmp = jcast('int', Code01_SequenceOperation.suf0[i])
        Code01_SequenceOperation.suf0[i] = jcast('int', Code01_SequenceOperation.suf1[i])
        Code01_SequenceOperation.suf1[i] = jcast('int', tmp)
        Code01_SequenceOperation.reverse_data[i] = jcast('boolean', (not Code01_SequenceOperation.reverse_data[i]))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code01_SequenceOperation.sum[i] = jcast('int', Code01_SequenceOperation.arr[l])
            jset(Code01_SequenceOperation.len0, i, jset(Code01_SequenceOperation.pre0, i, jset(Code01_SequenceOperation.suf0, i, (1 if (Code01_SequenceOperation.arr[l] == 0) else 0))))
            jset(Code01_SequenceOperation.len1, i, jset(Code01_SequenceOperation.pre1, i, jset(Code01_SequenceOperation.suf1, i, (1 if (Code01_SequenceOperation.arr[l] == 1) else 0))))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_SequenceOperation.build(l, mid, jcast('int', (i << (1 & 31))))
            Code01_SequenceOperation.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_SequenceOperation.up(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        Code01_SequenceOperation.update_data[i] = jcast('boolean', False)
        Code01_SequenceOperation.reverse_data[i] = jcast('boolean', False)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_SequenceOperation.updateLazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_SequenceOperation.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code01_SequenceOperation.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_SequenceOperation.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_SequenceOperation.up(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))

    @staticmethod
    def reverse(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_SequenceOperation.reverseLazy(i, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_SequenceOperation.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code01_SequenceOperation.reverse(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_SequenceOperation.reverse(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_SequenceOperation.up(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))

    # 线段树范围l~r上，被jobl~jobr影响的区域里，返回1的数量
    @staticmethod
    def querySum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code01_SequenceOperation.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code01_SequenceOperation.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code01_SequenceOperation.querySum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code01_SequenceOperation.querySum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', ans)

    # 返回一个长度为3的数组ans，代表结果，具体含义如下：
    # ans[0] : 线段树范围l~r上，被jobl~jobr影响的区域里，连续1的最长子串长度
    # ans[1] : 线段树范围l~r上，被jobl~jobr影响的区域里，连续1的最长前缀长度
    # ans[2] : 线段树范围l~r上，被jobl~jobr影响的区域里，连续1的最长后缀长度
    @staticmethod
    def queryLongest(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jarray('int', [None], [Code01_SequenceOperation.len1[i], Code01_SequenceOperation.pre1[i], Code01_SequenceOperation.suf1[i]])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            ln = jcast('int', jcast('int', jadd(jcast('int', (mid - l)), 1)))
            rn = jcast('int', jcast('int', (r - mid)))
            Code01_SequenceOperation.down(i, ln, rn)
            if (jobr <= mid):
                return Code01_SequenceOperation.queryLongest(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
            if (jobl > mid):
                return Code01_SequenceOperation.queryLongest(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            l3 = Code01_SequenceOperation.queryLongest(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
            r3 = Code01_SequenceOperation.queryLongest(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            llen = jcast('int', l3[0])
            lpre = jcast('int', l3[1])
            lsuf = jcast('int', l3[2])
            rlen = jcast('int', r3[0])
            rpre = jcast('int', r3[1])
            rsuf = jcast('int', r3[2])
            len = jcast('int', jstatic('Math', 'max', jstatic('Math', 'max', llen, rlen), jcast('int', jadd(lsuf, rpre))))
            # 任务实际影响了左侧范围的几个点 -> mid - Math.max(jobl, l) + 1
            pre = jcast('int', (lpre if (llen < jcast('int', jadd(jcast('int', (mid - jstatic('Math', 'max', jobl, l))), 1))) else jcast('int', jadd(lpre, rpre))))
            # 任务实际影响了右侧范围的几个点 -> Math.min(r, jobr) - mid
            suf = jcast('int', (rsuf if (rlen < jcast('int', (jstatic('Math', 'min', r, jobr) - mid))) else jcast('int', jadd(lsuf, rsuf))))
            return jarray('int', [None], [len, pre, suf])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            Code01_SequenceOperation.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_SequenceOperation.build(1, n, 1)
        i = jcast('int', 1)
        op = 0
        jobl = 0
        jobr = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            # 注意题目给的下标从0开始，线段树下标从1开始
            jobl = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
            jcall(in_, 'nextToken')
            # 注意题目给的下标从0开始，线段树下标从1开始
            jobr = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
            if (op == 0):
                Code01_SequenceOperation.update(jobl, jobr, 0, 1, n, 1)
            else:
                if (op == 1):
                    Code01_SequenceOperation.update(jobl, jobr, 1, 1, n, 1)
                else:
                    if (op == 2):
                        Code01_SequenceOperation.reverse(jobl, jobr, 1, n, 1)
                    else:
                        if (op == 3):
                            jcall(out, 'println', Code01_SequenceOperation.querySum(jobl, jobr, 1, n, 1))
                        else:
                            jcall(out, 'println', Code01_SequenceOperation.queryLongest(jobl, jobr, 1, n, 1)[0])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SequenceOperation.MAXN = jcast('int', 100001)
Code01_SequenceOperation.arr = jarray('int', [Code01_SequenceOperation.MAXN])
Code01_SequenceOperation.sum = jarray('int', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.len0 = jarray('int', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.pre0 = jarray('int', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.suf0 = jarray('int', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.len1 = jarray('int', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.pre1 = jarray('int', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.suf1 = jarray('int', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.change = jarray('int', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.update_data = jarray('boolean', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])
Code01_SequenceOperation.reverse_data = jarray('boolean', [jcast('int', (Code01_SequenceOperation.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code01_SequenceOperation.main([])
