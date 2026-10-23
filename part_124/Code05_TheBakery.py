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

# 划分k段的最大得分
# 给定一个长度为n的数组，最多可以分成k段不重合的子数组
# 每个子数组获得的分值为内部不同数字的个数
# 返回能获得的最大分值
# 1 <= n <= 35000
# 1 <= k <= 50
# k <= n
# 1 <= arr[i] <= n
# 测试链接 : https://www.luogu.com.cn/problem/CF833B
# 测试链接 : https://codeforces.com/problemset/problem/833/B
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_TheBakery:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'arr': 'arr', 'dp': 'dp', 'pre': 'pre', 'max': 'max', 'add': 'add_data'}
    MAXN = 0
    n = 0
    k = 0
    arr = None
    dp = None
    pre = None
    max = None
    add_data = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_TheBakery.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_TheBakery.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code05_TheBakery.n):
            jcall(in_, 'nextToken')
            Code05_TheBakery.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_TheBakery.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 注意本题的线段树范围不是1~n，而是0~n
    # 因为线段树需要维护0号~n号指标
    @staticmethod
    def compute():
        jstatic('Arrays', 'fill', Code05_TheBakery.dp, 1, jcast('int', jadd(Code05_TheBakery.n, 1)), 0)
        t = jcast('int', 1)
        while (t <= Code05_TheBakery.k):
            Code05_TheBakery.build(0, Code05_TheBakery.n, 1)
            jstatic('Arrays', 'fill', Code05_TheBakery.pre, 1, jcast('int', jadd(Code05_TheBakery.n, 1)), 0)
            i = jcast('int', 1)
            while (i <= Code05_TheBakery.n):
                Code05_TheBakery.add(Code05_TheBakery.pre[Code05_TheBakery.arr[i]], jcast('int', (i - 1)), 1, 0, Code05_TheBakery.n, 1)
                if (i >= t):
                    jset(Code05_TheBakery.dp, i, Code05_TheBakery.query(0, jcast('int', (i - 1)), 0, Code05_TheBakery.n, 1))
                jset(Code05_TheBakery.pre, Code05_TheBakery.arr[i], i)
                i = jcast('int', (i + 1))
            t = jcast('int', (t + 1))
        return jcast('int', Code05_TheBakery.dp[Code05_TheBakery.n])

    # 下面所有方法都是线段树维护最大值的模版，没有任何修改
    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code05_TheBakery.max, i, jstatic('Math', 'max', Code05_TheBakery.max[jcast('int', (i << (1 & 31)))], Code05_TheBakery.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code05_TheBakery.add_data[i] != 0):
            Code05_TheBakery.lazy(jcast('int', (i << (1 & 31))), Code05_TheBakery.add_data[i])
            Code05_TheBakery.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code05_TheBakery.add_data[i])
            Code05_TheBakery.add_data[i] = jcast('int', 0)

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code05_TheBakery.max[i] = jcast('int', jcast('int', jadd(Code05_TheBakery.max[i], v)))
        Code05_TheBakery.add_data[i] = jcast('int', jcast('int', jadd(Code05_TheBakery.add_data[i], v)))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            # 用dp[0..n]来build线段树
            Code05_TheBakery.max[i] = jcast('int', Code05_TheBakery.dp[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_TheBakery.build(l, mid, jcast('int', (i << (1 & 31))))
            Code05_TheBakery.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_TheBakery.up(i)
        Code05_TheBakery.add_data[i] = jcast('int', 0)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_TheBakery.lazy(i, jobv)
        else:
            Code05_TheBakery.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code05_TheBakery.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_TheBakery.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_TheBakery.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code05_TheBakery.max[i])
        Code05_TheBakery.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code05_TheBakery.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code05_TheBakery.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_TheBakery.MAXN = jcast('int', 35001)
Code05_TheBakery.n = jcast('int', 0)
Code05_TheBakery.k = jcast('int', 0)
Code05_TheBakery.arr = jarray('int', [Code05_TheBakery.MAXN])
Code05_TheBakery.dp = jarray('int', [Code05_TheBakery.MAXN])
Code05_TheBakery.pre = jarray('int', [Code05_TheBakery.MAXN])
Code05_TheBakery.max = jarray('int', [jcast('int', (Code05_TheBakery.MAXN << (2 & 31)))])
Code05_TheBakery.add_data = jarray('int', [jcast('int', (Code05_TheBakery.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code05_TheBakery.main([])
