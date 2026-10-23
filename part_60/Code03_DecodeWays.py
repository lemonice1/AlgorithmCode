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

# 解码方法
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）
# 例如，"11106" 可以映射为："AAJF"、"KJF"
# 注意，消息不能分组为(1 11 06)，因为 "06" 不能映射为 "F"
# 这是由于 "6" 和 "06" 在映射中并不等价
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数
# 题目数据保证答案肯定是一个 32位 的整数
# 测试链接 : https://leetcode.cn/problems/decode-ways/
class Code03_DecodeWays:
    __java_fields__ = {}
    # 暴力尝试
    @staticmethod
    def numDecodings1(s):
        return jcast('int', Code03_DecodeWays.f1(jcall(s, 'toCharArray'), 0))

    # s : 数字字符串
    # s[i....]有多少种有效的转化方案
    @staticmethod
    def f1(s, i):
        i = jcast('int', i)
        if (i == jget(s, 'length')):
            return jcast('int', 1)
        ans = 0
        if (s[i] == jchar('0')):
            ans = jcast('int', 0)
        else:
            ans = jcast('int', Code03_DecodeWays.f1(s, jcast('int', jadd(i, 1))))
            if ((jcast('int', jadd(i, 1)) < jget(s, 'length')) and (jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (s[i] - jchar('0'))) * 10)), s[jcast('int', jadd(i, 1))])) - jchar('0'))) <= 26)):
                ans = jcast('int', jcast('int', jadd(ans, Code03_DecodeWays.f1(s, jcast('int', jadd(i, 2))))))
        return jcast('int', ans)

    # 暴力尝试改记忆化搜索
    @staticmethod
    def numDecodings2(s):
        dp = jarray('int', [jcall(s, 'length')])
        jstatic('Arrays', 'fill', dp, jcast('int', (-1)))
        return jcast('int', Code03_DecodeWays.f2(jcall(s, 'toCharArray'), 0, dp))

    @staticmethod
    def f2(s, i, dp):
        i = jcast('int', i)
        if (i == jget(s, 'length')):
            return jcast('int', 1)
        if (dp[i] != jcast('int', (-1))):
            return jcast('int', dp[i])
        ans = 0
        if (s[i] == jchar('0')):
            ans = jcast('int', 0)
        else:
            ans = jcast('int', Code03_DecodeWays.f2(s, jcast('int', jadd(i, 1)), dp))
            if ((jcast('int', jadd(i, 1)) < jget(s, 'length')) and (jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (s[i] - jchar('0'))) * 10)), s[jcast('int', jadd(i, 1))])) - jchar('0'))) <= 26)):
                ans = jcast('int', jcast('int', jadd(ans, Code03_DecodeWays.f2(s, jcast('int', jadd(i, 2)), dp))))
        dp[i] = jcast('int', ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def numDecodings3(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [jcast('int', jadd(n, 1))])
        dp[n] = jcast('int', 1)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            if (s[i] == jchar('0')):
                dp[i] = jcast('int', 0)
            else:
                dp[i] = jcast('int', dp[jcast('int', jadd(i, 1))])
                if ((jcast('int', jadd(i, 1)) < jget(s, 'length')) and (jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (s[i] - jchar('0'))) * 10)), s[jcast('int', jadd(i, 1))])) - jchar('0'))) <= 26)):
                    dp[i] = jcast('int', jcast('int', jadd(dp[i], dp[jcast('int', jadd(i, 2))])))
            i = jcast('int', (i - 1))
        return jcast('int', dp[0])

    # 严格位置依赖的动态规划 + 空间压缩
    @staticmethod
    def numDecodings4(s):
        # dp[i+1]
        next = jcast('int', 1)
        # dp[i+2]
        nextNext = jcast('int', 0)
        i = jcast('int', jcast('int', (jcall(s, 'length') - 1)))
        cur = 0
        while (i >= 0):
            if (jcall(s, 'charAt', i) == jchar('0')):
                cur = jcast('int', 0)
            else:
                cur = jcast('int', next)
                if ((jcast('int', jadd(i, 1)) < jcall(s, 'length')) and (jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (jcall(s, 'charAt', i) - jchar('0'))) * 10)), jcall(s, 'charAt', jcast('int', jadd(i, 1))))) - jchar('0'))) <= 26)):
                    cur = jcast('int', jcast('int', jadd(cur, nextNext)))
            nextNext = jcast('int', next)
            next = jcast('int', cur)
            i = jcast('int', (i - 1))
        return jcast('int', next)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


