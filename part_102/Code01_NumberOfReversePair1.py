# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 逆序对数量(归并分治)
# 给定一个长度为n的数组arr
# 如果 i < j 且 arr[i] > arr[j]
# 那么(i,j)就是一个逆序对
# 求arr中逆序对的数量
# 1 <= n <= 5 * 10^5
# 1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1908
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_NumberOfReversePair1:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'help': 'help', 'n': 'n'}
    MAXN = 0
    arr = None
    help = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_NumberOfReversePair1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_NumberOfReversePair1.n):
            jcall(in_, 'nextToken')
            Code01_NumberOfReversePair1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_NumberOfReversePair1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        return jcast('long', Code01_NumberOfReversePair1.f(1, Code01_NumberOfReversePair1.n))

    # 归并分治
    # 1) 统计i、j来自l~r范围的情况下，逆序对数量
    # 2) 统计完成后，让arr[l...r]变成有序的
    @staticmethod
    def f(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('long', 0)
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        return jcast('long', jcast('long', jadd(jcast('long', jadd(Code01_NumberOfReversePair1.f(l, m), Code01_NumberOfReversePair1.f(jcast('int', jadd(m, 1)), r))), Code01_NumberOfReversePair1.merge(l, m, r))))

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        # i来自l.....m
        # j来自m+1...r
        # 统计有多少逆序对
        ans = jcast('long', 0)
        i = jcast('int', m)
        j = jcast('int', r)
        while (i >= l):
            while ((j >= jcast('int', jadd(m, 1))) and (Code01_NumberOfReversePair1.arr[i] <= Code01_NumberOfReversePair1.arr[j])):
                j = jcast('int', (j - 1))
            ans = jcast('long', jcast('long', jadd(ans, jcast('int', (j - m)))))
            i = jcast('int', (i - 1))
        # 左右部分合并，整体变有序，归并排序的过程
        i = jcast('int', l)
        a = jcast('int', l)
        b = jcast('int', jcast('int', jadd(m, 1)))
        while ((a <= m) and (b <= r)):
            jset(Code01_NumberOfReversePair1.help, ((_java_old_3 := i), (i := jcast('int', (i + (1)))), _java_old_3)[2], (Code01_NumberOfReversePair1.arr[((_java_old_1 := a), (a := jcast('int', (a + (1)))), _java_old_1)[2]] if (Code01_NumberOfReversePair1.arr[a] <= Code01_NumberOfReversePair1.arr[b]) else Code01_NumberOfReversePair1.arr[((_java_old_2 := b), (b := jcast('int', (b + (1)))), _java_old_2)[2]]))
        while (a <= m):
            jset(Code01_NumberOfReversePair1.help, ((_java_old_5 := i), (i := jcast('int', (i + (1)))), _java_old_5)[2], Code01_NumberOfReversePair1.arr[((_java_old_4 := a), (a := jcast('int', (a + (1)))), _java_old_4)[2]])
        while (b <= r):
            jset(Code01_NumberOfReversePair1.help, ((_java_old_7 := i), (i := jcast('int', (i + (1)))), _java_old_7)[2], Code01_NumberOfReversePair1.arr[((_java_old_6 := b), (b := jcast('int', (b + (1)))), _java_old_6)[2]])
        i = jcast('int', l)
        while (i <= r):
            Code01_NumberOfReversePair1.arr[i] = jcast('int', Code01_NumberOfReversePair1.help[i])
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_NumberOfReversePair1.MAXN = jcast('int', 500001)
Code01_NumberOfReversePair1.arr = jarray('int', [Code01_NumberOfReversePair1.MAXN])
Code01_NumberOfReversePair1.help = jarray('int', [Code01_NumberOfReversePair1.MAXN])
Code01_NumberOfReversePair1.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_NumberOfReversePair1.main([])
