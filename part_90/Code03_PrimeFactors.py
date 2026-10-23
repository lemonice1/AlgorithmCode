# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 数字n拆分质数因子
class Code03_PrimeFactors:
    __java_fields__ = {'MAXV': 'MAXV', 'factors': 'factors', 'MAXN': 'MAXN', 'father': 'father', 'size': 'size', 'n': 'n'}
    # 展示分解质因子过程
    @staticmethod
    def main(args):
        n = jcast('int', 4012100)
        Code03_PrimeFactors.f(n)

    # 打印所有n的质因子，时间复杂度O(根号n)
    @staticmethod
    def f(n):
        n = jcast('int', n)
        i = jcast('int', 2)
        while (jcast('int', (i * i)) <= n):
            if (jcast('int', jmod(n, i)) == 0):
                jprint(i, newline=True)
                while (jcast('int', jmod(n, i)) == 0):
                    n = jcast('int', jcast('int', jdiv(n, i)))
            i = jcast('int', (i + 1))
        if (n > 1):
            jprint(n, newline=True)

    # 按公因数计算最大组件大小
    # 给定一个由不同正整数的组成的非空数组 nums
    # 如果 nums[i] 和 nums[j] 有一个大于1的公因子，那么这两个数之间有一条无向边
    # 返回 nums中最大连通组件的大小。
    # 测试链接 : https://leetcode.cn/problems/largest-component-size-by-common-factor/
    # Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
    MAXV = 0
    # factors[a] = b
    # a这个质数因子，最早被下标b的数字拥有
    factors = None
    # 讲解056、讲解057 - 并查集模版
    MAXN = 0
    father = None
    size = None
    n = 0
    @staticmethod
    def build():
        i = jcast('int', 0)
        while (i < Code03_PrimeFactors.n):
            Code03_PrimeFactors.father[i] = jcast('int', i)
            Code03_PrimeFactors.size[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code03_PrimeFactors.factors, jcast('int', (-1)))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_PrimeFactors.father[i]):
            jset(Code03_PrimeFactors.father, i, Code03_PrimeFactors.find(Code03_PrimeFactors.father[i]))
        return jcast('int', Code03_PrimeFactors.father[i])

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code03_PrimeFactors.find(x))
        fy = jcast('int', Code03_PrimeFactors.find(y))
        if (fx != fy):
            Code03_PrimeFactors.father[fx] = jcast('int', fy)
            Code03_PrimeFactors.size[fy] = jcast('int', jcast('int', jadd(Code03_PrimeFactors.size[fy], Code03_PrimeFactors.size[fx])))

    @staticmethod
    def maxSize():
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code03_PrimeFactors.n):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_PrimeFactors.size[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 正式方法
    # 时间复杂度O(n * 根号v)
    @staticmethod
    def largestComponentSize(arr):
        Code03_PrimeFactors.n = jcast('int', jget(arr, 'length'))
        Code03_PrimeFactors.build()
        i = jcast('int', 0)
        x = 0
        while (i < Code03_PrimeFactors.n):
            x = jcast('int', arr[i])
            j = jcast('int', 2)
            while (jcast('int', (j * j)) <= x):
                if (jcast('int', jmod(x, j)) == 0):
                    if (Code03_PrimeFactors.factors[j] == jcast('int', (-1))):
                        Code03_PrimeFactors.factors[j] = jcast('int', i)
                    else:
                        Code03_PrimeFactors.union(Code03_PrimeFactors.factors[j], i)
                    while (jcast('int', jmod(x, j)) == 0):
                        x = jcast('int', jcast('int', jdiv(x, j)))
                j = jcast('int', (j + 1))
            if (x > 1):
                if (Code03_PrimeFactors.factors[x] == jcast('int', (-1))):
                    Code03_PrimeFactors.factors[x] = jcast('int', i)
                else:
                    Code03_PrimeFactors.union(Code03_PrimeFactors.factors[x], i)
            i = jcast('int', (i + 1))
        return jcast('int', Code03_PrimeFactors.maxSize())

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_PrimeFactors.MAXV = jcast('int', 100001)
Code03_PrimeFactors.factors = jarray('int', [Code03_PrimeFactors.MAXV])
Code03_PrimeFactors.MAXN = jcast('int', 20001)
Code03_PrimeFactors.father = jarray('int', [Code03_PrimeFactors.MAXN])
Code03_PrimeFactors.size = jarray('int', [Code03_PrimeFactors.MAXN])
Code03_PrimeFactors.n = jcast('int', 0)

if __name__ == '__main__':
    Code03_PrimeFactors.main([])
