# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不用任何算术运算，只用位运算实现加减乘除
# 代码实现中你找不到任何一个算术运算符
# 测试链接 : https://leetcode.cn/problems/divide-two-integers/
# 在线评测时提交题目要求的方法接口，并一并提供使用到的公共辅助模块
class BitOperationAddMinusMultiplyDivide:
    __java_fields__ = {}
    # 在线评测时提交题目要求的方法接口，并一并提供使用到的公共辅助模块
    class Solution:
        __java_fields__ = {'MIN': 'MIN'}
        MIN = 0
        @staticmethod
        def divide(a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            if ((a == BitOperationAddMinusMultiplyDivide.Solution.MIN) and (b == BitOperationAddMinusMultiplyDivide.Solution.MIN)):
                # a和b都是整数最小
                return jcast('int', 1)
            if ((a != BitOperationAddMinusMultiplyDivide.Solution.MIN) and (b != BitOperationAddMinusMultiplyDivide.Solution.MIN)):
                # a和b都不是整数最小，那么正常去除
                return jcast('int', BitOperationAddMinusMultiplyDivide.Solution.div(a, b))
            if (b == BitOperationAddMinusMultiplyDivide.Solution.MIN):
                # a不是整数最小，b是整数最小
                return jcast('int', 0)
            # a是整数最小，b是-1，返回整数最大，因为题目里明确这么说了
            if (b == BitOperationAddMinusMultiplyDivide.Solution.neg(1)):
                return jcast('int', jget(Integer, 'MAX_VALUE'))
            # a是整数最小，b不是整数最小，b也不是-1
            a = jcast('int', BitOperationAddMinusMultiplyDivide.Solution.add(a, (b if (b > 0) else BitOperationAddMinusMultiplyDivide.Solution.neg(b))))
            ans = jcast('int', BitOperationAddMinusMultiplyDivide.Solution.div(a, b))
            offset = jcast('int', (BitOperationAddMinusMultiplyDivide.Solution.neg(1) if (b > 0) else 1))
            return jcast('int', BitOperationAddMinusMultiplyDivide.Solution.add(ans, offset))

        # 必须保证a和b都不是整数最小值，返回a除以b的结果
        @staticmethod
        def div(a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            x = jcast('int', (BitOperationAddMinusMultiplyDivide.Solution.neg(a) if (a < 0) else a))
            y = jcast('int', (BitOperationAddMinusMultiplyDivide.Solution.neg(b) if (b < 0) else b))
            ans = jcast('int', 0)
            i = jcast('int', 30)
            while (i >= 0):
                if (jcast('int', (x >> (i & 31))) >= y):
                    ans = jcast('int', jcast('int', (ans | jcast('int', (1 << (i & 31))))))
                    x = jcast('int', BitOperationAddMinusMultiplyDivide.Solution.minus(x, jcast('int', (y << (i & 31)))))
                i = jcast('int', BitOperationAddMinusMultiplyDivide.Solution.minus(i, 1))
            return jcast('int', (BitOperationAddMinusMultiplyDivide.Solution.neg(ans) if ((a < 0) ^ (b < 0)) else ans))

        @staticmethod
        def add(a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            ans = jcast('int', a)
            while (b != 0):
                # ans : a和b无进位相加的结果
                ans = jcast('int', jcast('int', (a ^ b)))
                # b : a和b相加时的进位信息
                b = jcast('int', jcast('int', (jcast('int', (a & b)) << (1 & 31))))
                a = jcast('int', ans)
            return jcast('int', ans)

        @staticmethod
        def minus(a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            return jcast('int', BitOperationAddMinusMultiplyDivide.Solution.add(a, BitOperationAddMinusMultiplyDivide.Solution.neg(b)))

        @staticmethod
        def neg(n):
            n = jcast('int', n)
            return jcast('int', BitOperationAddMinusMultiplyDivide.Solution.add(jcast('int', (~n)), 1))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 如下的multiply方法，也叫龟速乘，后面的课程有大用处
    # 很多时候，题目要求计算a * b，然后 % mod的结果
    # 过程就是课上讲的，每一步取模即可，后续的课程还会见到
    @staticmethod
    def multiply(a, b, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        mod = jcast('long', mod)
        a = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(a, mod)), mod)), mod)))
        b = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(b, mod)), mod)), mod)))
        ans = jcast('long', 0)
        while (b != 0):
            if (jcast('long', (b & 1)) != 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, a)), mod)))
            a = jcast('long', jcast('long', jmod(jcast('long', jadd(a, a)), mod)))
            b = jcast('long', jcast('long', (b >> (1 & 63))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


BitOperationAddMinusMultiplyDivide.Solution.MIN = jcast('int', jget(Integer, 'MIN_VALUE'))
