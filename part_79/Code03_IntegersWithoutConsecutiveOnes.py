# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不含连续1的非负整数
# 给定一个正整数n，请你统计在[0, n]范围的非负整数中
# 有多少个整数的二进制表示中不存在连续的1
# 测试链接 : https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/
class Code03_IntegersWithoutConsecutiveOnes:
    __java_fields__ = {}
    @staticmethod
    def findIntegers1(n):
        n = jcast('int', n)
        cnt = jarray('int', [31])
        cnt[0] = jcast('int', 1)
        cnt[1] = jcast('int', 2)
        len = jcast('int', 2)
        while (len <= 30):
            cnt[len] = jcast('int', jcast('int', jadd(cnt[jcast('int', (len - 1))], cnt[jcast('int', (len - 2))])))
            len = jcast('int', (len + 1))
        return jcast('int', Code03_IntegersWithoutConsecutiveOnes.f(cnt, n, 30))

    # cnt[len] : 二进制如果有len位，所有二进制状态中不存在连续的1的状态有多少个，辅助数组
    # 从num二进制形式的高位开始，当前来到第i位，之前的位完全和num一样
    # 返回<=num且不存在连续的1的状态有多少个
    @staticmethod
    def f(cnt, num, i):
        num = jcast('int', num)
        i = jcast('int', i)
        if (i == jcast('int', (-1))):
            # num自身合法
            return jcast('int', 1)
        ans = jcast('int', 0)
        if (jcast('int', (num & jcast('int', (1 << (i & 31))))) != 0):
            ans = jcast('int', jcast('int', jadd(ans, cnt[i])))
            if (jcast('int', (num & jcast('int', (1 << (jcast('int', jadd(i, 1)) & 31))))) != 0):
                # 如果num二进制状态，前一位是1，当前位也是1
                # 如果前缀保持和num一样，后续一定不合法了
                # 所以提前返回
                return jcast('int', ans)
        # 之前的高位和num一样，且合法，继续去i-1位递归
        ans = jcast('int', jcast('int', jadd(ans, Code03_IntegersWithoutConsecutiveOnes.f(cnt, num, jcast('int', (i - 1))))))
        return jcast('int', ans)

    # 只是把方法1从递归改成迭代而已
    # 完全是等义改写，没有新东西
    @staticmethod
    def findIntegers2(n):
        n = jcast('int', n)
        cnt = jarray('int', [31])
        cnt[0] = jcast('int', 1)
        cnt[1] = jcast('int', 2)
        len = jcast('int', 2)
        while (len <= 30):
            cnt[len] = jcast('int', jcast('int', jadd(cnt[jcast('int', (len - 1))], cnt[jcast('int', (len - 2))])))
            len = jcast('int', (len + 1))
        ans = jcast('int', 0)
        i = jcast('int', 30)
        while (i >= jcast('int', (-1))):
            try:
                if (i == jcast('int', (-1))):
                    ans = jcast('int', (ans + 1))
                    raise JBreak(None)
                if (jcast('int', (n & jcast('int', (1 << (i & 31))))) != 0):
                    ans = jcast('int', jcast('int', jadd(ans, cnt[i])))
                    if (jcast('int', (n & jcast('int', (1 << (jcast('int', jadd(i, 1)) & 31))))) != 0):
                        raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i - 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


