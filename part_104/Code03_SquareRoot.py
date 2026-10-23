# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 范围上开平方并求累加和
# 给定一个长度为n的数组arr，实现以下两种类型的操作
# 操作 0 l r : 把arr[l..r]范围上的每个数开平方，结果向下取整
# 操作 1 l r : 查询arr[l..r]范围上所有数字的累加和
# 两种操作一共发生m次，数据中有可能l>r，遇到这种情况请交换l和r
# 1 <= n, m <= 10^5，1 <= arr[i] <= 10^12
# 测试链接 : https://www.luogu.com.cn/problem/P4145
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_SquareRoot:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum': 'sum', 'max': 'max'}
    MAXN = 0
    arr = None
    sum = None
    max = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code03_SquareRoot.sum[i] = jcast('long', jcast('long', jadd(Code03_SquareRoot.sum[jcast('int', (i << (1 & 31)))], Code03_SquareRoot.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        jset(Code03_SquareRoot.max, i, jstatic('Math', 'max', Code03_SquareRoot.max[jcast('int', (i << (1 & 31)))], Code03_SquareRoot.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code03_SquareRoot.sum[i] = jcast('long', Code03_SquareRoot.arr[l])
            Code03_SquareRoot.max[i] = jcast('long', Code03_SquareRoot.arr[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_SquareRoot.build(l, mid, jcast('int', (i << (1 & 31))))
            Code03_SquareRoot.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_SquareRoot.up(i)

    # sqrt方法是最核心的
    # 注意和常规线段树不一样，这里没有懒更新，也就不需要有down方法
    # 只有根据范围最大值信息的剪枝
    # 时间复杂度的分析就是课上讲的势能分析
    # 不用纠结单次调用的复杂度
    # 哪怕调用再多次sqrt方法，总的时间复杂度也就是O(n * 6 * logn)
    @staticmethod
    def sqrt(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            sqrt = jcast('long', jcast('long', jstatic('Math', 'sqrt', Code03_SquareRoot.max[i])))
            Code03_SquareRoot.sum[i] = jcast('long', sqrt)
            Code03_SquareRoot.max[i] = jcast('long', sqrt)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if ((jobl <= mid) and (Code03_SquareRoot.max[jcast('int', (i << (1 & 31)))] > 1)):
                Code03_SquareRoot.sqrt(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
            if ((jobr > mid) and (Code03_SquareRoot.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))] > 1)):
                Code03_SquareRoot.sqrt(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_SquareRoot.up(i)

    # 没有懒更新
    # 不需要调用down方法
    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code03_SquareRoot.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_SquareRoot.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_SquareRoot.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            Code03_SquareRoot.arr[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code03_SquareRoot.build(1, n, 1)
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        op = 0
        jobl = 0
        jobr = 0
        tmp = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jobl = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jobr = jcast('int', jcast('int', jget(in_, 'nval')))
            if (jobl > jobr):
                tmp = jcast('int', jobl)
                jobl = jcast('int', jobr)
                jobr = jcast('int', tmp)
            if (op == 0):
                Code03_SquareRoot.sqrt(jobl, jobr, 1, n, 1)
            else:
                jcall(out, 'println', Code03_SquareRoot.query(jobl, jobr, 1, n, 1))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SquareRoot.MAXN = jcast('int', 100001)
Code03_SquareRoot.arr = jarray('long', [Code03_SquareRoot.MAXN])
Code03_SquareRoot.sum = jarray('long', [jcast('int', (Code03_SquareRoot.MAXN << (2 & 31)))])
Code03_SquareRoot.max = jarray('long', [jcast('int', (Code03_SquareRoot.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code03_SquareRoot.main([])
