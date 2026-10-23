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

# 标记永久化，范围增加 + 查询累加和，Python版
# 给定一个长度为n的数组arr，下标1~n，一共有m条操作，操作类型如下
# 1 x y k : 将区间[x, y]每个数加上k
# 2 x y   : 打印区间[x, y]的累加和
# 这就是普通线段树，请用标记永久化的方式实现
# 测试链接 : https://www.luogu.com.cn/problem/P3372
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_TagPermanentization2:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum': 'sum', 'addTag': 'addTag'}
    MAXN = 0
    arr = None
    # 不是真实累加和，而是之前的任务中
    # 不考虑被上方范围截住的任务，只考虑来到当前范围 或者 往下走的任务
    # 累加和变成了什么
    sum = None
    # 不再是懒更新信息，变成标记信息
    addTag = None
    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code04_TagPermanentization2.sum[i] = jcast('long', Code04_TagPermanentization2.arr[l])
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code04_TagPermanentization2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code04_TagPermanentization2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_TagPermanentization2.sum[i] = jcast('long', jcast('long', jadd(Code04_TagPermanentization2.sum[jcast('int', (i << (1 & 31)))], Code04_TagPermanentization2.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        Code04_TagPermanentization2.addTag[i] = jcast('long', 0)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        a = jcast('int', jstatic('Math', 'max', jobl, l))
        b = jcast('int', jstatic('Math', 'min', jobr, r))
        Code04_TagPermanentization2.sum[i] = jcast('long', jcast('long', jadd(Code04_TagPermanentization2.sum[i], jcast('long', (jobv * jcast('int', jadd(jcast('int', (b - a)), 1)))))))
        if ((jobl <= l) and (r <= jobr)):
            Code04_TagPermanentization2.addTag[i] = jcast('long', jcast('long', jadd(Code04_TagPermanentization2.addTag[i], jobv)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code04_TagPermanentization2.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_TagPermanentization2.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def query(jobl, jobr, addHistory, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        addHistory = jcast('long', addHistory)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', jcast('long', jadd(Code04_TagPermanentization2.sum[i], jcast('long', (addHistory * jcast('int', jadd(jcast('int', (r - l)), 1)))))))
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code04_TagPermanentization2.query(jobl, jobr, jcast('long', jadd(addHistory, Code04_TagPermanentization2.addTag[i])), l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code04_TagPermanentization2.query(jobl, jobr, jcast('long', jadd(addHistory, Code04_TagPermanentization2.addTag[i])), jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('long', ans)

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
            Code04_TagPermanentization2.arr[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code04_TagPermanentization2.build(1, n, 1)
        op = 0
        jobl = 0
        jobr = 0
        jobv = 0
        i = jcast('int', 1)
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobv = jcast('long', jcast('long', jget(in_, 'nval')))
                Code04_TagPermanentization2.add(jobl, jobr, jobv, 1, n, 1)
            else:
                jcall(in_, 'nextToken')
                jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(out, 'println', Code04_TagPermanentization2.query(jobl, jobr, 0, 1, n, 1))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_TagPermanentization2.MAXN = jcast('int', 100001)
Code04_TagPermanentization2.arr = jarray('long', [Code04_TagPermanentization2.MAXN])
Code04_TagPermanentization2.sum = jarray('long', [jcast('int', (Code04_TagPermanentization2.MAXN << (2 & 31)))])
Code04_TagPermanentization2.addTag = jarray('long', [jcast('int', (Code04_TagPermanentization2.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code04_TagPermanentization2.main([])
