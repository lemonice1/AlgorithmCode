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

# 浮动区间的最大上中位数，Python版
# 为了方便理解，我改写了题意，但是改写的题意和原始题意等效
# 给定一个长度为n的数组arr，下标1~n，一共有m条查询
# 每条查询 a b c d : 左端点在[a,b]之间、右端点在[c,d]之间，保证a<b<c<d
# 哪个区间有最大的上中位数，打印最大的上中位数
# 题目有强制在线的要求，上一次打印的答案为lastAns，初始时lastAns = 0
# 每次给定四个参数，按照如下方式得到a、b、c、d，查询完成后更新lastAns
# (给定的每个参数 + lastAns) % n + 1，得到四个值，从小到大对应a、b、c、d
# 1 <= n <= 20000
# 1 <= m <= 25000
# 1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P2839
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_LargestUpMedian1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'm': 'm', 'arr': 'arr', 'root': 'root', 'left': 'left', 'right': 'right', 'pre': 'pre', 'suf': 'suf', 'sum': 'sum', 'cnt': 'cnt', 'ques': 'ques', 'info': 'info'}
    MAXN = 0
    MAXT = 0
    INF = 0
    n = 0
    m = 0
    # 原始位置、数值
    arr = None
    # 可持久化线段树需要
    root = None
    left = None
    right = None
    # 区间内最大前缀和，前缀不能为空
    pre = None
    # 区间内最大后缀和，后缀不能为空
    suf = None
    # 区间内累加和
    sum = None
    cnt = 0
    # 查询的问题，a、b、c、d
    ques = None
    # 收集区间信息，pre、suf、sum
    info = None
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code03_LargestUpMedian1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        jset(Code03_LargestUpMedian1.pre, rt, jset(Code03_LargestUpMedian1.suf, rt, jset(Code03_LargestUpMedian1.sum, rt, jcast('int', jadd(jcast('int', (r - l)), 1)))))
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code03_LargestUpMedian1.left, rt, Code03_LargestUpMedian1.build(l, mid))
            jset(Code03_LargestUpMedian1.right, rt, Code03_LargestUpMedian1.build(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code03_LargestUpMedian1.pre, i, jstatic('Math', 'max', Code03_LargestUpMedian1.pre[Code03_LargestUpMedian1.left[i]], jcast('int', jadd(Code03_LargestUpMedian1.sum[Code03_LargestUpMedian1.left[i]], Code03_LargestUpMedian1.pre[Code03_LargestUpMedian1.right[i]]))))
        jset(Code03_LargestUpMedian1.suf, i, jstatic('Math', 'max', Code03_LargestUpMedian1.suf[Code03_LargestUpMedian1.right[i]], jcast('int', jadd(Code03_LargestUpMedian1.suf[Code03_LargestUpMedian1.left[i]], Code03_LargestUpMedian1.sum[Code03_LargestUpMedian1.right[i]]))))
        Code03_LargestUpMedian1.sum[i] = jcast('int', jcast('int', jadd(Code03_LargestUpMedian1.sum[Code03_LargestUpMedian1.left[i]], Code03_LargestUpMedian1.sum[Code03_LargestUpMedian1.right[i]])))

    # jobi位置，原来是1，现在改为-1
    @staticmethod
    def update(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code03_LargestUpMedian1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code03_LargestUpMedian1.left[rt] = jcast('int', Code03_LargestUpMedian1.left[i])
        Code03_LargestUpMedian1.right[rt] = jcast('int', Code03_LargestUpMedian1.right[i])
        Code03_LargestUpMedian1.pre[rt] = jcast('int', Code03_LargestUpMedian1.pre[i])
        Code03_LargestUpMedian1.suf[rt] = jcast('int', Code03_LargestUpMedian1.suf[i])
        Code03_LargestUpMedian1.sum[rt] = jcast('int', Code03_LargestUpMedian1.sum[i])
        if (l == r):
            jset(Code03_LargestUpMedian1.pre, rt, jset(Code03_LargestUpMedian1.suf, rt, jset(Code03_LargestUpMedian1.sum, rt, jcast('int', (-1)))))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code03_LargestUpMedian1.left, rt, Code03_LargestUpMedian1.update(jobi, l, mid, Code03_LargestUpMedian1.left[rt]))
            else:
                jset(Code03_LargestUpMedian1.right, rt, Code03_LargestUpMedian1.update(jobi, jcast('int', jadd(mid, 1)), r, Code03_LargestUpMedian1.right[rt]))
            Code03_LargestUpMedian1.up(rt)
        return jcast('int', rt)

    @staticmethod
    def initInfo():
        jset(Code03_LargestUpMedian1.info, 0, jset(Code03_LargestUpMedian1.info, 1, jcast('int', (-Code03_LargestUpMedian1.INF))))
        Code03_LargestUpMedian1.info[2] = jcast('int', 0)

    @staticmethod
    def mergeRight(r):
        r = jcast('int', r)
        jset(Code03_LargestUpMedian1.info, 0, jstatic('Math', 'max', Code03_LargestUpMedian1.info[0], jcast('int', jadd(Code03_LargestUpMedian1.info[2], Code03_LargestUpMedian1.pre[r]))))
        jset(Code03_LargestUpMedian1.info, 1, jstatic('Math', 'max', Code03_LargestUpMedian1.suf[r], jcast('int', jadd(Code03_LargestUpMedian1.info[1], Code03_LargestUpMedian1.sum[r]))))
        Code03_LargestUpMedian1.info[2] = jcast('int', jcast('int', jadd(Code03_LargestUpMedian1.info[2], Code03_LargestUpMedian1.sum[r])))

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code03_LargestUpMedian1.mergeRight(i)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code03_LargestUpMedian1.query(jobl, jobr, l, mid, Code03_LargestUpMedian1.left[i])
            if (jobr > mid):
                Code03_LargestUpMedian1.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code03_LargestUpMedian1.right[i])

    @staticmethod
    def prepare():
        jstatic('Arrays', 'sort', Code03_LargestUpMedian1.arr, 1, jcast('int', jadd(Code03_LargestUpMedian1.n, 1)), (lambda a, b: (a[1] - b[1])))
        Code03_LargestUpMedian1.cnt = jcast('int', 0)
        jset(Code03_LargestUpMedian1.root, 1, Code03_LargestUpMedian1.build(1, Code03_LargestUpMedian1.n))
        i = jcast('int', 2)
        while (i <= Code03_LargestUpMedian1.n):
            jset(Code03_LargestUpMedian1.root, i, Code03_LargestUpMedian1.update(Code03_LargestUpMedian1.arr[jcast('int', (i - 1))][0], 1, Code03_LargestUpMedian1.n, Code03_LargestUpMedian1.root[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))

    @staticmethod
    def check(a, b, c, d, v):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        v = jcast('int', v)
        Code03_LargestUpMedian1.initInfo()
        Code03_LargestUpMedian1.query(a, b, 1, Code03_LargestUpMedian1.n, Code03_LargestUpMedian1.root[v])
        best = jcast('int', Code03_LargestUpMedian1.info[1])
        Code03_LargestUpMedian1.initInfo()
        Code03_LargestUpMedian1.query(c, d, 1, Code03_LargestUpMedian1.n, Code03_LargestUpMedian1.root[v])
        best = jcast('int', jcast('int', jadd(best, Code03_LargestUpMedian1.info[0])))
        if (jcast('int', jadd(b, 1)) <= jcast('int', (c - 1))):
            Code03_LargestUpMedian1.initInfo()
            Code03_LargestUpMedian1.query(jcast('int', jadd(b, 1)), jcast('int', (c - 1)), 1, Code03_LargestUpMedian1.n, Code03_LargestUpMedian1.root[v])
            best = jcast('int', jcast('int', jadd(best, Code03_LargestUpMedian1.info[2])))
        return jcast('boolean', (best >= 0))

    @staticmethod
    def compute(a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        left = jcast('int', 1)
        right = jcast('int', Code03_LargestUpMedian1.n)
        mid = 0
        ans = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if Code03_LargestUpMedian1.check(a, b, c, d, mid):
                ans = jcast('int', Code03_LargestUpMedian1.arr[mid][1])
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_LargestUpMedian1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_LargestUpMedian1.n):
            jset(Code03_LargestUpMedian1.arr[i], 0, i)
            jcall(in_, 'nextToken')
            jset(Code03_LargestUpMedian1.arr[i], 1, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code03_LargestUpMedian1.prepare()
        jcall(in_, 'nextToken')
        Code03_LargestUpMedian1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        lastAns = jcast('int', 0)
        while (i <= Code03_LargestUpMedian1.m):
            jcall(in_, 'nextToken')
            Code03_LargestUpMedian1.ques[0] = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcast('int', jget(in_, 'nval')), lastAns)), Code03_LargestUpMedian1.n)), 1)))
            jcall(in_, 'nextToken')
            Code03_LargestUpMedian1.ques[1] = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcast('int', jget(in_, 'nval')), lastAns)), Code03_LargestUpMedian1.n)), 1)))
            jcall(in_, 'nextToken')
            Code03_LargestUpMedian1.ques[2] = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcast('int', jget(in_, 'nval')), lastAns)), Code03_LargestUpMedian1.n)), 1)))
            jcall(in_, 'nextToken')
            Code03_LargestUpMedian1.ques[3] = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcast('int', jget(in_, 'nval')), lastAns)), Code03_LargestUpMedian1.n)), 1)))
            jstatic('Arrays', 'sort', Code03_LargestUpMedian1.ques)
            lastAns = jcast('int', Code03_LargestUpMedian1.compute(Code03_LargestUpMedian1.ques[0], Code03_LargestUpMedian1.ques[1], Code03_LargestUpMedian1.ques[2], Code03_LargestUpMedian1.ques[3]))
            jcall(out, 'println', lastAns)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_LargestUpMedian1.MAXN = jcast('int', 20001)
Code03_LargestUpMedian1.MAXT = jcast('int', jcast('int', (Code03_LargestUpMedian1.MAXN * 20)))
Code03_LargestUpMedian1.INF = jcast('int', 10000001)
Code03_LargestUpMedian1.n = jcast('int', 0)
Code03_LargestUpMedian1.m = jcast('int', 0)
Code03_LargestUpMedian1.arr = jarray('int', [Code03_LargestUpMedian1.MAXN, 2])
Code03_LargestUpMedian1.root = jarray('int', [Code03_LargestUpMedian1.MAXN])
Code03_LargestUpMedian1.left = jarray('int', [Code03_LargestUpMedian1.MAXT])
Code03_LargestUpMedian1.right = jarray('int', [Code03_LargestUpMedian1.MAXT])
Code03_LargestUpMedian1.pre = jarray('int', [Code03_LargestUpMedian1.MAXT])
Code03_LargestUpMedian1.suf = jarray('int', [Code03_LargestUpMedian1.MAXT])
Code03_LargestUpMedian1.sum = jarray('int', [Code03_LargestUpMedian1.MAXT])
Code03_LargestUpMedian1.cnt = jcast('int', 0)
Code03_LargestUpMedian1.ques = jarray('int', [4])
Code03_LargestUpMedian1.info = jarray('int', [3])

if __name__ == '__main__':
    Code03_LargestUpMedian1.main([])
