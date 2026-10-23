# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 一和零(多维费用背包)
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n
# 请你找出并返回 strs 的最大子集的长度
# 该子集中 最多 有 m 个 0 和 n 个 1
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集
# 测试链接 : https://leetcode.cn/problems/ones-and-zeroes/
class Code01_OnesAndZeroes:
    __java_fields__ = {'zeros': 'zeros', 'ones': 'ones'}
    zeros = 0
    ones = 0
    # 统计一个字符串中0的1的数量
    # 0的数量赋值给全局变量zeros
    # 1的数量赋值给全局变量ones
    @staticmethod
    def zerosAndOnes(str):
        Code01_OnesAndZeroes.zeros = jcast('int', 0)
        Code01_OnesAndZeroes.ones = jcast('int', 0)
        i = jcast('int', 0)
        while (i < jcall(str, 'length')):
            if (jcall(str, 'charAt', i) == jchar('0')):
                Code01_OnesAndZeroes.zeros = jcast('int', (Code01_OnesAndZeroes.zeros + 1))
            else:
                Code01_OnesAndZeroes.ones = jcast('int', (Code01_OnesAndZeroes.ones + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def findMaxForm1(strs, m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        return jcast('int', Code01_OnesAndZeroes.f1(strs, 0, m, n))

    # strs[i....]自由选择，希望零的数量不超过z、一的数量不超过o
    # 最多能选多少个字符串
    @staticmethod
    def f1(strs, i, z, o):
        i = jcast('int', i)
        z = jcast('int', z)
        o = jcast('int', o)
        if (i == jget(strs, 'length')):
            # 没有字符串了
            return jcast('int', 0)
        # 不使用当前的strs[i]字符串
        p1 = jcast('int', Code01_OnesAndZeroes.f1(strs, jcast('int', jadd(i, 1)), z, o))
        # 使用当前的strs[i]字符串
        p2 = jcast('int', 0)
        Code01_OnesAndZeroes.zerosAndOnes(strs[i])
        if ((Code01_OnesAndZeroes.zeros <= z) and (Code01_OnesAndZeroes.ones <= o)):
            p2 = jcast('int', jcast('int', jadd(1, Code01_OnesAndZeroes.f1(strs, jcast('int', jadd(i, 1)), jcast('int', (z - Code01_OnesAndZeroes.zeros)), jcast('int', (o - Code01_OnesAndZeroes.ones))))))
        return jcast('int', jstatic('Math', 'max', p1, p2))

    # 记忆化搜索
    @staticmethod
    def findMaxForm2(strs, m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        dp = jarray('int', [jget(strs, 'length'), jcast('int', jadd(m, 1)), jcast('int', jadd(n, 1))])
        i = jcast('int', 0)
        while (i < jget(strs, 'length')):
            z = jcast('int', 0)
            while (z <= m):
                o = jcast('int', 0)
                while (o <= n):
                    jset(dp[i][z], o, jcast('int', (-1)))
                    o = jcast('int', (o + 1))
                z = jcast('int', (z + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_OnesAndZeroes.f2(strs, 0, m, n, dp))

    @staticmethod
    def f2(strs, i, z, o, dp):
        i = jcast('int', i)
        z = jcast('int', z)
        o = jcast('int', o)
        if (i == jget(strs, 'length')):
            return jcast('int', 0)
        if (dp[i][z][o] != jcast('int', (-1))):
            return jcast('int', dp[i][z][o])
        p1 = jcast('int', Code01_OnesAndZeroes.f2(strs, jcast('int', jadd(i, 1)), z, o, dp))
        p2 = jcast('int', 0)
        Code01_OnesAndZeroes.zerosAndOnes(strs[i])
        if ((Code01_OnesAndZeroes.zeros <= z) and (Code01_OnesAndZeroes.ones <= o)):
            p2 = jcast('int', jcast('int', jadd(1, Code01_OnesAndZeroes.f2(strs, jcast('int', jadd(i, 1)), jcast('int', (z - Code01_OnesAndZeroes.zeros)), jcast('int', (o - Code01_OnesAndZeroes.ones)), dp))))
        ans = jcast('int', jstatic('Math', 'max', p1, p2))
        jset(dp[i][z], o, ans)
        return jcast('int', ans)

    @staticmethod
    def findMaxForm3(strs, m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        len = jcast('int', jget(strs, 'length'))
        dp = jarray('int', [jcast('int', jadd(len, 1)), jcast('int', jadd(m, 1)), jcast('int', jadd(n, 1))])
        i = jcast('int', jcast('int', (len - 1)))
        while (i >= 0):
            Code01_OnesAndZeroes.zerosAndOnes(strs[i])
            z = jcast('int', 0)
            p1 = 0
            p2 = 0
            while (z <= m):
                o = jcast('int', 0)
                while (o <= n):
                    p1 = jcast('int', dp[jcast('int', jadd(i, 1))][z][o])
                    p2 = jcast('int', 0)
                    if ((Code01_OnesAndZeroes.zeros <= z) and (Code01_OnesAndZeroes.ones <= o)):
                        p2 = jcast('int', jcast('int', jadd(1, dp[jcast('int', jadd(i, 1))][jcast('int', (z - Code01_OnesAndZeroes.zeros))][jcast('int', (o - Code01_OnesAndZeroes.ones))])))
                    jset(dp[i][z], o, jstatic('Math', 'max', p1, p2))
                    o = jcast('int', (o + 1))
                z = jcast('int', (z + 1))
            i = jcast('int', (i - 1))
        return jcast('int', dp[0][m][n])

    @staticmethod
    def findMaxForm4(strs, m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        # 代表i == len
        dp = jarray('int', [jcast('int', jadd(m, 1)), jcast('int', jadd(n, 1))])
        for s in strs:
            # 每个字符串逐渐遍历即可
            # 更新每一层的表
            # 和之前的遍历没有区别
            Code01_OnesAndZeroes.zerosAndOnes(s)
            z = jcast('int', m)
            while (z >= Code01_OnesAndZeroes.zeros):
                o = jcast('int', n)
                while (o >= Code01_OnesAndZeroes.ones):
                    jset(dp[z], o, jstatic('Math', 'max', dp[z][o], jcast('int', jadd(1, dp[jcast('int', (z - Code01_OnesAndZeroes.zeros))][jcast('int', (o - Code01_OnesAndZeroes.ones))]))))
                    o = jcast('int', (o - 1))
                z = jcast('int', (z - 1))
        return jcast('int', dp[m][n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_OnesAndZeroes.zeros = jcast('int', 0)
Code01_OnesAndZeroes.ones = jcast('int', 0)
