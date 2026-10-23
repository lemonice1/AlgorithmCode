# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 感谢热心的同学，找到了题目5的在线测试
# 最大平均值和中位数
# 给定一个长度为n的数组arr，现在要选出一些数
# 满足 任意两个相邻的数中至少有一个数被选择
# 被选中的数字平均值的最大值，打印的答案为double类型，误差在0.001以内
# 被选中的数字中位数的最大值，打印的答案为int类型，中位数认为是上中位数
# 2 <= n <= 10^5
# 1 <= arr[i] <= 10^9
# 测试链接 : https://atcoder.jp/contests/abc236/tasks/abc236_e
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_MaximizeMedian2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'arr': 'arr', 'help1': 'help1', 'dp1': 'dp1', 'sorted': 'sorted', 'help2': 'help2', 'dp2': 'dp2'}
    MAXN = 0
    n = 0
    arr = None
    # 求最大平均数需要
    help1 = None
    dp1 = None
    # 求最大上中位数需要
    sorted = None
    help2 = None
    dp2 = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_MaximizeMedian2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code05_MaximizeMedian2.n):
            jcall(in_, 'nextToken')
            Code05_MaximizeMedian2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_MaximizeMedian2.average())
        jcall(out, 'println', Code05_MaximizeMedian2.median())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 最大平均数
    # 课上没有讲，但是很好理解，也是二分答案
    # 假设arr中最小值为l，最大值为r
    # 那么最大平均值必然在[l, r]范围上
    # 假设平均值设为中点m，arr中所有的数字都减去m
    # 如果此时，任意两个相邻的数中至少有一个数被选择
    # 最后得到的结果 >= 0，说明最大平均值至少是m，去右侧二分
    # 否则去左侧二分
    @staticmethod
    def average():
        l = jcast('double', jget(Double, 'MAX_VALUE'))
        r = jcast('double', jget(Double, 'MIN_VALUE'))
        m = 0.0
        i = jcast('int', 1)
        while (i <= Code05_MaximizeMedian2.n):
            l = jcast('double', jstatic('Math', 'min', l, Code05_MaximizeMedian2.arr[i]))
            r = jcast('double', jstatic('Math', 'max', r, Code05_MaximizeMedian2.arr[i]))
            i = jcast('int', (i + 1))
        # 二分60次，足够让误差小于0.001
        i = jcast('int', 1)
        while (i <= 60):
            m = jcast('double', jdiv(jadd(l, r), 2))
            if Code05_MaximizeMedian2.check1(m):
                l = jcast('double', m)
            else:
                r = jcast('double', m)
            i = jcast('int', (i + 1))
        return jcast('double', l)

    @staticmethod
    def check1(x):
        x = jcast('double', x)
        # arr中所有的数字都减去x，得到的数字填入help1
        i = jcast('int', 1)
        while (i <= Code05_MaximizeMedian2.n):
            Code05_MaximizeMedian2.help1[i] = jcast('double', (jcast('double', Code05_MaximizeMedian2.arr[i]) - x))
            i = jcast('int', (i + 1))
        # 和课上讲的一样的逻辑
        # 任意两个相邻的数中至少有一个数被选择，去得到dp表
        jset(Code05_MaximizeMedian2.dp1[jcast('int', jadd(Code05_MaximizeMedian2.n, 1))], 0, jset(Code05_MaximizeMedian2.dp1[jcast('int', jadd(Code05_MaximizeMedian2.n, 1))], 1, 0))
        i = jcast('int', Code05_MaximizeMedian2.n)
        while (i >= 1):
            jset(Code05_MaximizeMedian2.dp1[i], 0, jstatic('Math', 'max', jadd(Code05_MaximizeMedian2.help1[i], Code05_MaximizeMedian2.dp1[jcast('int', jadd(i, 1))][0]), Code05_MaximizeMedian2.dp1[jcast('int', jadd(i, 1))][1]))
            jset(Code05_MaximizeMedian2.dp1[i], 1, jadd(Code05_MaximizeMedian2.help1[i], Code05_MaximizeMedian2.dp1[jcast('int', jadd(i, 1))][0]))
            i = jcast('int', (i - 1))
        return jcast('boolean', (Code05_MaximizeMedian2.dp1[1][0] >= 0))

    # 最大上中位数，就和课上讲的一样了
    @staticmethod
    def median():
        i = jcast('int', 1)
        while (i <= Code05_MaximizeMedian2.n):
            Code05_MaximizeMedian2.sorted[i] = jcast('int', Code05_MaximizeMedian2.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_MaximizeMedian2.sorted, 1, jcast('int', jadd(Code05_MaximizeMedian2.n, 1)))
        l = jcast('int', 1)
        r = jcast('int', Code05_MaximizeMedian2.n)
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if Code05_MaximizeMedian2.check2(Code05_MaximizeMedian2.sorted[m]):
                ans = jcast('int', Code05_MaximizeMedian2.sorted[m])
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('int', ans)

    @staticmethod
    def check2(x):
        x = jcast('int', x)
        i = jcast('int', 1)
        while (i <= Code05_MaximizeMedian2.n):
            Code05_MaximizeMedian2.help2[i] = jcast('int', (1 if (Code05_MaximizeMedian2.arr[i] >= x) else jcast('int', (-1))))
            i = jcast('int', (i + 1))
        jset(Code05_MaximizeMedian2.dp2[jcast('int', jadd(Code05_MaximizeMedian2.n, 1))], 0, jset(Code05_MaximizeMedian2.dp2[jcast('int', jadd(Code05_MaximizeMedian2.n, 1))], 1, 0))
        i = jcast('int', Code05_MaximizeMedian2.n)
        while (i >= 1):
            jset(Code05_MaximizeMedian2.dp2[i], 0, jstatic('Math', 'max', jcast('int', jadd(Code05_MaximizeMedian2.help2[i], Code05_MaximizeMedian2.dp2[jcast('int', jadd(i, 1))][0])), Code05_MaximizeMedian2.dp2[jcast('int', jadd(i, 1))][1]))
            jset(Code05_MaximizeMedian2.dp2[i], 1, jcast('int', jadd(Code05_MaximizeMedian2.help2[i], Code05_MaximizeMedian2.dp2[jcast('int', jadd(i, 1))][0])))
            i = jcast('int', (i - 1))
        return jcast('boolean', (Code05_MaximizeMedian2.dp2[1][0] > 0))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MaximizeMedian2.MAXN = jcast('int', 100005)
Code05_MaximizeMedian2.n = jcast('int', 0)
Code05_MaximizeMedian2.arr = jarray('int', [Code05_MaximizeMedian2.MAXN])
Code05_MaximizeMedian2.help1 = jarray('double', [Code05_MaximizeMedian2.MAXN])
Code05_MaximizeMedian2.dp1 = jarray('double', [Code05_MaximizeMedian2.MAXN, 2])
Code05_MaximizeMedian2.sorted = jarray('int', [Code05_MaximizeMedian2.MAXN])
Code05_MaximizeMedian2.help2 = jarray('int', [Code05_MaximizeMedian2.MAXN])
Code05_MaximizeMedian2.dp2 = jarray('int', [Code05_MaximizeMedian2.MAXN, 2])

if __name__ == '__main__':
    Code05_MaximizeMedian2.main([])
