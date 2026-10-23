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

# 解码方法 II
# 一条包含字母 A-Z 的消息通过以下的方式进行了 编码 ：
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 一条已编码的消息，所有的数字都必须分组
# 然后按原来的编码方案反向映射回字母（可能存在多种方式）
# 例如，"11106" 可以映射为："AAJF"、"KJF"
# 注意，像 (1 11 06) 这样的分组是无效的，"06"不可以映射为'F'
# 除了上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符
# 可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）
# 例如，"1*" 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19"
# 对 "1*" 进行解码，相当于解码该字符串可以表示的任何编码消息
# 给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目
# 由于答案数目可能非常大，答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/decode-ways-ii/
class Code04_DecodeWaysII:
    __java_fields__ = {'mod': 'mod'}
    # 没有取模逻辑
    # 最自然的暴力尝试
    @staticmethod
    def numDecodings1(str):
        return jcast('int', Code04_DecodeWaysII.f1(jcall(str, 'toCharArray'), 0))

    # s[i....] 有多少种有效转化
    @staticmethod
    def f1(s, i):
        i = jcast('int', i)
        if (i == jget(s, 'length')):
            return jcast('int', 1)
        if (s[i] == jchar('0')):
            return jcast('int', 0)
        # s[i] != '0'
        # 2) i想单独转
        ans = jcast('int', jcast('int', (Code04_DecodeWaysII.f1(s, jcast('int', jadd(i, 1))) * (9 if (s[i] == jchar('*')) else 1))))
        # 3) i i+1 一起转化 <= 26
        if (jcast('int', jadd(i, 1)) < jget(s, 'length')):
            # 有i+1位置
            if (s[i] != jchar('*')):
                if (s[jcast('int', jadd(i, 1))] != jchar('*')):
                    # num num
                    # i  i+1
                    if (jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (s[i] - jchar('0'))) * 10)), s[jcast('int', jadd(i, 1))])) - jchar('0'))) <= 26):
                        ans = jcast('int', jcast('int', jadd(ans, Code04_DecodeWaysII.f1(s, jcast('int', jadd(i, 2))))))
                else:
                    # num  *
                    # i  i+1
                    if (s[i] == jchar('1')):
                        ans = jcast('int', jcast('int', jadd(ans, jcast('int', (Code04_DecodeWaysII.f1(s, jcast('int', jadd(i, 2))) * 9)))))
                    if (s[i] == jchar('2')):
                        ans = jcast('int', jcast('int', jadd(ans, jcast('int', (Code04_DecodeWaysII.f1(s, jcast('int', jadd(i, 2))) * 6)))))
            else:
                if (s[jcast('int', jadd(i, 1))] != jchar('*')):
                    # *  num
                    # i  i+1
                    if (s[jcast('int', jadd(i, 1))] <= jchar('6')):
                        ans = jcast('int', jcast('int', jadd(ans, jcast('int', (Code04_DecodeWaysII.f1(s, jcast('int', jadd(i, 2))) * 2)))))
                    else:
                        ans = jcast('int', jcast('int', jadd(ans, Code04_DecodeWaysII.f1(s, jcast('int', jadd(i, 2))))))
                else:
                    # *  *
                    # i  i+1
                    # 11 12 ... 19 21 22 ... 26 -> 一共15种可能
                    # 没有10、20，因为*只能变1~9，并不包括0
                    ans = jcast('int', jcast('int', jadd(ans, jcast('int', (Code04_DecodeWaysII.f1(s, jcast('int', jadd(i, 2))) * 15)))))
        return jcast('int', ans)

    mod = 0
    @staticmethod
    def numDecodings2(str):
        s = jcall(str, 'toCharArray')
        dp = jarray('long', [jget(s, 'length')])
        jstatic('Arrays', 'fill', dp, jcast('int', (-1)))
        return jcast('int', jcast('int', Code04_DecodeWaysII.f2(s, 0, dp)))

    @staticmethod
    def f2(s, i, dp):
        i = jcast('int', i)
        if (i == jget(s, 'length')):
            return jcast('long', 1)
        if (s[i] == jchar('0')):
            return jcast('long', 0)
        if (dp[i] != jcast('int', (-1))):
            return jcast('long', dp[i])
        ans = jcast('long', jcast('long', (Code04_DecodeWaysII.f2(s, jcast('int', jadd(i, 1)), dp) * (9 if (s[i] == jchar('*')) else 1))))
        if (jcast('int', jadd(i, 1)) < jget(s, 'length')):
            if (s[i] != jchar('*')):
                if (s[jcast('int', jadd(i, 1))] != jchar('*')):
                    if (jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (s[i] - jchar('0'))) * 10)), s[jcast('int', jadd(i, 1))])) - jchar('0'))) <= 26):
                        ans = jcast('long', jcast('long', jadd(ans, Code04_DecodeWaysII.f2(s, jcast('int', jadd(i, 2)), dp))))
                else:
                    if (s[i] == jchar('1')):
                        ans = jcast('long', jcast('long', jadd(ans, jcast('long', (Code04_DecodeWaysII.f2(s, jcast('int', jadd(i, 2)), dp) * 9)))))
                    if (s[i] == jchar('2')):
                        ans = jcast('long', jcast('long', jadd(ans, jcast('long', (Code04_DecodeWaysII.f2(s, jcast('int', jadd(i, 2)), dp) * 6)))))
            else:
                if (s[jcast('int', jadd(i, 1))] != jchar('*')):
                    if (s[jcast('int', jadd(i, 1))] <= jchar('6')):
                        ans = jcast('long', jcast('long', jadd(ans, jcast('long', (Code04_DecodeWaysII.f2(s, jcast('int', jadd(i, 2)), dp) * 2)))))
                    else:
                        ans = jcast('long', jcast('long', jadd(ans, Code04_DecodeWaysII.f2(s, jcast('int', jadd(i, 2)), dp))))
                else:
                    ans = jcast('long', jcast('long', jadd(ans, jcast('long', (Code04_DecodeWaysII.f2(s, jcast('int', jadd(i, 2)), dp) * 15)))))
        ans = jcast('long', jcast('long', jmod(ans, Code04_DecodeWaysII.mod)))
        dp[i] = jcast('long', ans)
        return jcast('long', ans)

    @staticmethod
    def numDecodings3(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('long', [jcast('int', jadd(n, 1))])
        dp[n] = jcast('long', 1)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            if (s[i] != jchar('0')):
                dp[i] = jcast('long', jcast('long', ((9 if (s[i] == jchar('*')) else 1) * dp[jcast('int', jadd(i, 1))])))
                if (jcast('int', jadd(i, 1)) < n):
                    if (s[i] != jchar('*')):
                        if (s[jcast('int', jadd(i, 1))] != jchar('*')):
                            if (jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (s[i] - jchar('0'))) * 10)), s[jcast('int', jadd(i, 1))])) - jchar('0'))) <= 26):
                                dp[i] = jcast('long', jcast('long', jadd(dp[i], dp[jcast('int', jadd(i, 2))])))
                        else:
                            if (s[i] == jchar('1')):
                                dp[i] = jcast('long', jcast('long', jadd(dp[i], jcast('long', (dp[jcast('int', jadd(i, 2))] * 9)))))
                            if (s[i] == jchar('2')):
                                dp[i] = jcast('long', jcast('long', jadd(dp[i], jcast('long', (dp[jcast('int', jadd(i, 2))] * 6)))))
                    else:
                        if (s[jcast('int', jadd(i, 1))] != jchar('*')):
                            if (s[jcast('int', jadd(i, 1))] <= jchar('6')):
                                dp[i] = jcast('long', jcast('long', jadd(dp[i], jcast('long', (dp[jcast('int', jadd(i, 2))] * 2)))))
                            else:
                                dp[i] = jcast('long', jcast('long', jadd(dp[i], dp[jcast('int', jadd(i, 2))])))
                        else:
                            dp[i] = jcast('long', jcast('long', jadd(dp[i], jcast('long', (dp[jcast('int', jadd(i, 2))] * 15)))))
                dp[i] = jcast('long', jcast('long', jmod(dp[i], Code04_DecodeWaysII.mod)))
            i = jcast('int', (i - 1))
        return jcast('int', jcast('int', dp[0]))

    @staticmethod
    def numDecodings4(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        cur = jcast('long', 0)
        next = jcast('long', 1)
        nextNext = jcast('long', 0)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            if (s[i] != jchar('0')):
                cur = jcast('long', jcast('long', ((9 if (s[i] == jchar('*')) else 1) * next)))
                if (jcast('int', jadd(i, 1)) < n):
                    if (s[i] != jchar('*')):
                        if (s[jcast('int', jadd(i, 1))] != jchar('*')):
                            if (jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (s[i] - jchar('0'))) * 10)), s[jcast('int', jadd(i, 1))])) - jchar('0'))) <= 26):
                                cur = jcast('long', jcast('long', jadd(cur, nextNext)))
                        else:
                            if (s[i] == jchar('1')):
                                cur = jcast('long', jcast('long', jadd(cur, jcast('long', (nextNext * 9)))))
                            if (s[i] == jchar('2')):
                                cur = jcast('long', jcast('long', jadd(cur, jcast('long', (nextNext * 6)))))
                    else:
                        if (s[jcast('int', jadd(i, 1))] != jchar('*')):
                            if (s[jcast('int', jadd(i, 1))] <= jchar('6')):
                                cur = jcast('long', jcast('long', jadd(cur, jcast('long', (nextNext * 2)))))
                            else:
                                cur = jcast('long', jcast('long', jadd(cur, nextNext)))
                        else:
                            cur = jcast('long', jcast('long', jadd(cur, jcast('long', (nextNext * 15)))))
                cur = jcast('long', jcast('long', jmod(cur, Code04_DecodeWaysII.mod)))
            nextNext = jcast('long', next)
            next = jcast('long', cur)
            cur = jcast('long', 0)
            i = jcast('int', (i - 1))
        return jcast('int', jcast('int', next))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_DecodeWaysII.mod = jcast('long', 1000000007)
