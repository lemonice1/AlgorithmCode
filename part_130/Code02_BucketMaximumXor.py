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

# P哥的桶
# 一共有n个桶，排成一排，编号1~n，每个桶可以装下任意个数字
# 高效的实现如下两个操作
# 操作 1 k v : 把数字v放入k号桶中
# 操作 2 l r : 可以从l..r号桶中随意拿数字，返回异或和最大的结果
# 1 <= n、m <= 5 * 10^4
# 0 <= v <= 2^31 - 1
# 测试链接 : https://www.luogu.com.cn/problem/P4839
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_BucketMaximumXor:
    __java_fields__ = {'MAXN': 'MAXN', 'BIT': 'BIT', 'treeBasis': 'treeBasis', 'basis': 'basis'}
    MAXN = 0
    BIT = 0
    # 线段树的每个范围上维护线性基
    treeBasis = None
    basis = None
    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        Code02_BucketMaximumXor.insert(Code02_BucketMaximumXor.treeBasis[i], jobv)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code02_BucketMaximumXor.add(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code02_BucketMaximumXor.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def insert(basis, num):
        num = jcast('int', num)
        i = jcast('int', Code02_BucketMaximumXor.BIT)
        while (i >= 0):
            if (jcast('int', (num >> (i & 31))) == 1):
                if (basis[i] == 0):
                    basis[i] = jcast('int', num)
                    return jcast('boolean', True)
                num = jcast('int', jcast('int', (num ^ basis[i])))
            i = jcast('int', (i - 1))
        return jcast('boolean', False)

    @staticmethod
    def query(jobl, jobr, m):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        m = jcast('int', m)
        jstatic('Arrays', 'fill', Code02_BucketMaximumXor.basis, 0)
        Code02_BucketMaximumXor.merge(jobl, jobr, 1, m, 1)
        ans = jcast('int', 0)
        j = jcast('int', Code02_BucketMaximumXor.BIT)
        while (j >= 0):
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (ans ^ Code02_BucketMaximumXor.basis[j]))))
            j = jcast('int', (j - 1))
        return jcast('int', ans)

    @staticmethod
    def merge(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            j = jcast('int', Code02_BucketMaximumXor.BIT)
            while (j >= 0):
                if (Code02_BucketMaximumXor.treeBasis[i][j] != 0):
                    Code02_BucketMaximumXor.insert(Code02_BucketMaximumXor.basis, Code02_BucketMaximumXor.treeBasis[i][j])
                j = jcast('int', (j - 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code02_BucketMaximumXor.merge(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code02_BucketMaximumXor.merge(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

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
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                jobi = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobv = jcast('int', jcast('int', jget(in_, 'nval')))
                Code02_BucketMaximumXor.add(jobi, jobv, 1, m, 1)
            else:
                jcall(in_, 'nextToken')
                jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(out, 'println', Code02_BucketMaximumXor.query(jobl, jobr, m))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_BucketMaximumXor.MAXN = jcast('int', 50001)
Code02_BucketMaximumXor.BIT = jcast('int', 30)
Code02_BucketMaximumXor.treeBasis = jarray('int', [jcast('int', (Code02_BucketMaximumXor.MAXN << (2 & 31))), jcast('int', jadd(Code02_BucketMaximumXor.BIT, 1))])
Code02_BucketMaximumXor.basis = jarray('int', [jcast('int', jadd(Code02_BucketMaximumXor.BIT, 1))])

if __name__ == '__main__':
    Code02_BucketMaximumXor.main([])
