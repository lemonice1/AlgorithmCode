# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 瓶子里的花朵
# 给定n个瓶子，编号从0~n-1，一开始所有瓶子都是空的
# 每个瓶子最多插入一朵花，实现以下两种类型的操作
# 操作 1 from flower : 一共有flower朵花，从from位置开始依次插入花朵，已经有花的瓶子跳过
# 如果一直到最后的瓶子，花也没有用完，就丢弃剩下的花朵
# 返回这次操作插入的首个空瓶的位置 和 最后空瓶的位置
# 如果从from开始所有瓶子都有花，打印"Can not put any one."
# 操作 2 left right  : 从left位置开始到right位置的瓶子，变回空瓶，返回清理花朵的数量
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=4614
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_VasesAndFlowers:
    __java_fields__ = {'MAXN': 'MAXN', 'sum': 'sum', 'change': 'change', 'update': 'update_data', 'n': 'n'}
    MAXN = 0
    sum = None
    change = None
    update_data = None
    n = 0
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_VasesAndFlowers.sum[i] = jcast('int', jcast('int', jadd(Code02_VasesAndFlowers.sum[jcast('int', (i << (1 & 31)))], Code02_VasesAndFlowers.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if Code02_VasesAndFlowers.update_data[i]:
            Code02_VasesAndFlowers.lazy(jcast('int', (i << (1 & 31))), Code02_VasesAndFlowers.change[i], ln)
            Code02_VasesAndFlowers.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code02_VasesAndFlowers.change[i], rn)
            Code02_VasesAndFlowers.update_data[i] = jcast('boolean', False)

    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('int', v)
        n = jcast('int', n)
        Code02_VasesAndFlowers.sum[i] = jcast('int', jcast('int', (v * n)))
        Code02_VasesAndFlowers.change[i] = jcast('int', v)
        Code02_VasesAndFlowers.update_data[i] = jcast('boolean', True)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_VasesAndFlowers.build(l, mid, jcast('int', (i << (1 & 31))))
            Code02_VasesAndFlowers.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code02_VasesAndFlowers.sum[i] = jcast('int', 0)
        Code02_VasesAndFlowers.update_data[i] = jcast('boolean', False)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code02_VasesAndFlowers.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_VasesAndFlowers.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code02_VasesAndFlowers.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code02_VasesAndFlowers.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_VasesAndFlowers.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code02_VasesAndFlowers.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code02_VasesAndFlowers.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code02_VasesAndFlowers.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code02_VasesAndFlowers.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', ans)

    @staticmethod
    def insert(from_, flowers):
        from_ = jcast('int', from_)
        flowers = jcast('int', flowers)
        # 题目给的位置从0开始
        # 线段树下标从1开始
        from_ = jcast('int', (from_ + 1))
        start = 0
        end = 0
        zeros = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (Code02_VasesAndFlowers.n - from_)), 1)) - Code02_VasesAndFlowers.query(from_, Code02_VasesAndFlowers.n, 1, Code02_VasesAndFlowers.n, 1))))
        if (zeros == 0):
            start = jcast('int', 0)
            end = jcast('int', 0)
        else:
            start = jcast('int', Code02_VasesAndFlowers.findZero(from_, 1))
            end = jcast('int', Code02_VasesAndFlowers.findZero(from_, jstatic('Math', 'min', zeros, flowers)))
            Code02_VasesAndFlowers.update(start, end, 1, 1, Code02_VasesAndFlowers.n, 1)
        # 题目需要从0开始的下标
        start = jcast('int', (start - 1))
        end = jcast('int', (end - 1))
        return jarray('int', [None], [start, end])

    # s~n范围上
    # 返回第k个0的位置
    @staticmethod
    def findZero(s, k):
        s = jcast('int', s)
        k = jcast('int', k)
        l = jcast('int', s)
        r = jcast('int', Code02_VasesAndFlowers.n)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jcast('int', (jcast('int', jadd(jcast('int', (mid - s)), 1)) - Code02_VasesAndFlowers.query(s, mid, 1, Code02_VasesAndFlowers.n, 1))) >= k):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    # 注意题目给的下标从0开始
    # 线段树下标从1开始
    @staticmethod
    def clear(left, right):
        left = jcast('int', left)
        right = jcast('int', right)
        left = jcast('int', (left + 1))
        right = jcast('int', (right + 1))
        ans = jcast('int', Code02_VasesAndFlowers.query(left, right, 1, Code02_VasesAndFlowers.n, 1))
        Code02_VasesAndFlowers.update(left, right, 0, 1, Code02_VasesAndFlowers.n, 1)
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        t = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= t):
            jcall(in_, 'nextToken')
            Code02_VasesAndFlowers.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_VasesAndFlowers.build(1, Code02_VasesAndFlowers.n, 1)
            j = jcast('int', 1)
            while (j <= m):
                jcall(in_, 'nextToken')
                op = jcast('int', jcast('int', jget(in_, 'nval')))
                if (op == 1):
                    jcall(in_, 'nextToken')
                    from_ = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    flowers = jcast('int', jcast('int', jget(in_, 'nval')))
                    ans = Code02_VasesAndFlowers.insert(from_, flowers)
                    if (ans[0] == jcast('int', (-1))):
                        jcall(out, 'println', 'Can not put any one.')
                    else:
                        jcall(out, 'println', jadd(jadd(ans[0], ' '), ans[1]))
                else:
                    jcall(in_, 'nextToken')
                    left = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    right = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(out, 'println', Code02_VasesAndFlowers.clear(left, right))
                j = jcast('int', (j + 1))
            jcall(out, 'println')
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_VasesAndFlowers.MAXN = jcast('int', 50001)
Code02_VasesAndFlowers.sum = jarray('int', [jcast('int', (Code02_VasesAndFlowers.MAXN << (2 & 31)))])
Code02_VasesAndFlowers.change = jarray('int', [jcast('int', (Code02_VasesAndFlowers.MAXN << (2 & 31)))])
Code02_VasesAndFlowers.update_data = jarray('boolean', [jcast('int', (Code02_VasesAndFlowers.MAXN << (2 & 31)))])
Code02_VasesAndFlowers.n = jcast('int', 0)

if __name__ == '__main__':
    Code02_VasesAndFlowers.main([])
