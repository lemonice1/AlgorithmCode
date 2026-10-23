# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 扰乱字符串
# 使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
# 步骤1 : 如果字符串的长度为 1 ，算法停止
# 步骤2 : 如果字符串的长度 > 1 ，执行下述步骤：
# 在一个随机下标处将字符串分割成两个非空的子字符串
# 已知字符串s，则可以将其分成两个子字符串x和y且满足s=x+y
# 可以决定是要 交换两个子字符串 还是要 保持这两个子字符串的顺序不变
# 即s可能是 s = x + y 或者 s = y + x
# 在x和y这两个子字符串上继续从步骤1开始递归执行此算法
# 给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串
# 如果是，返回true ；否则，返回false
# 测试链接 : https://leetcode.cn/problems/scramble-string/
class Code05_ScrambleString:
    __java_fields__ = {}
    @staticmethod
    def isScramble1(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        return jcast('boolean', Code05_ScrambleString.f1(s1, 0, jcast('int', (n - 1)), s2, 0, jcast('int', (n - 1))))

    # s1[l1....r1]
    # s2[l2....r2]
    # 保证l1....r1与l2....r2
    # 是不是扰乱串的关系
    @staticmethod
    def f1(s1, l1, r1, s2, l2, r2):
        l1 = jcast('int', l1)
        r1 = jcast('int', r1)
        l2 = jcast('int', l2)
        r2 = jcast('int', r2)
        if (l1 == r1):
            # s1[l1..r1]
            # s2[l2..r2]
            return jcast('boolean', (s1[l1] == s2[l2]))
        # s1[l1..i][i+1....r1]
        # s2[l2..j][j+1....r2]
        # 不交错去讨论扰乱关系
        i = jcast('int', l1)
        j = jcast('int', l2)
        while (i < r1):
            if (Code05_ScrambleString.f1(s1, l1, i, s2, l2, j) and Code05_ScrambleString.f1(s1, jcast('int', jadd(i, 1)), r1, s2, jcast('int', jadd(j, 1)), r2)):
                return jcast('boolean', True)
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        # 交错去讨论扰乱关系
        # s1[l1..........i][i+1...r1]
        # s2[l2...j-1][j..........r2]
        i = jcast('int', l1)
        j = jcast('int', r2)
        while (i < r1):
            if (Code05_ScrambleString.f1(s1, l1, i, s2, j, r2) and Code05_ScrambleString.f1(s1, jcast('int', jadd(i, 1)), r1, s2, l2, jcast('int', (j - 1)))):
                return jcast('boolean', True)
            i = jcast('int', (i + 1))
            j = jcast('int', (j - 1))
        return jcast('boolean', False)

    # 依然暴力尝试，只不过四个可变参数，变成了三个
    @staticmethod
    def isScramble2(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        return jcast('boolean', Code05_ScrambleString.f2(s1, s2, 0, 0, n))

    @staticmethod
    def f2(s1, s2, l1, l2, len):
        l1 = jcast('int', l1)
        l2 = jcast('int', l2)
        len = jcast('int', len)
        if (len == 1):
            return jcast('boolean', (s1[l1] == s2[l2]))
        # s1[l1.......]  len
        # s2[l2.......]  len
        # 左 : k个   右: len - k 个
        k = jcast('int', 1)
        while (k < len):
            if (Code05_ScrambleString.f2(s1, s2, l1, l2, k) and Code05_ScrambleString.f2(s1, s2, jcast('int', jadd(l1, k)), jcast('int', jadd(l2, k)), jcast('int', (len - k)))):
                return jcast('boolean', True)
            k = jcast('int', (k + 1))
        # 交错！
        i = jcast('int', jcast('int', jadd(l1, 1)))
        j = jcast('int', jcast('int', (jcast('int', jadd(l2, len)) - 1)))
        k = jcast('int', 1)
        while (k < len):
            if (Code05_ScrambleString.f2(s1, s2, l1, j, k) and Code05_ScrambleString.f2(s1, s2, i, l2, jcast('int', (len - k)))):
                return jcast('boolean', True)
            i = jcast('int', (i + 1))
            j = jcast('int', (j - 1))
            k = jcast('int', (k + 1))
        return jcast('boolean', False)

    @staticmethod
    def isScramble3(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        # dp[l1][l2][len] : int 0 -> 没展开过
        # dp[l1][l2][len] : int -1 -> 展开过，返回的结果是false
        # dp[l1][l2][len] : int 1 -> 展开过，返回的结果是true
        dp = jarray('int', [n, n, jcast('int', jadd(n, 1))])
        return jcast('boolean', Code05_ScrambleString.f3(s1, s2, 0, 0, n, dp))

    @staticmethod
    def f3(s1, s2, l1, l2, len, dp):
        l1 = jcast('int', l1)
        l2 = jcast('int', l2)
        len = jcast('int', len)
        if (len == 1):
            return jcast('boolean', (s1[l1] == s2[l2]))
        if (dp[l1][l2][len] != 0):
            return jcast('boolean', (dp[l1][l2][len] == 1))
        ans = jcast('boolean', False)
        k = jcast('int', 1)
        while (k < len):
            try:
                if (Code05_ScrambleString.f3(s1, s2, l1, l2, k, dp) and Code05_ScrambleString.f3(s1, s2, jcast('int', jadd(l1, k)), jcast('int', jadd(l2, k)), jcast('int', (len - k)), dp)):
                    ans = jcast('boolean', True)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            k = jcast('int', (k + 1))
        if (not ans):
            i = jcast('int', jcast('int', jadd(l1, 1)))
            j = jcast('int', jcast('int', (jcast('int', jadd(l2, len)) - 1)))
            k = jcast('int', 1)
            while (k < len):
                try:
                    if (Code05_ScrambleString.f3(s1, s2, l1, j, k, dp) and Code05_ScrambleString.f3(s1, s2, i, l2, jcast('int', (len - k)), dp)):
                        ans = jcast('boolean', True)
                        raise JBreak(None)
                except JContinue as _java_control_2:
                    if _java_control_2.label not in (None,):
                        raise
                except JBreak as _java_control_2:
                    if _java_control_2.label not in (None,):
                        raise
                    break
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
                k = jcast('int', (k + 1))
        jset(dp[l1][l2], len, (1 if ans else jcast('int', (-1))))
        return jcast('boolean', ans)

    @staticmethod
    def isScramble4(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        dp = jarray('boolean', [n, n, jcast('int', jadd(n, 1))])
        # 填写len=1层，所有的格子
        l1 = jcast('int', 0)
        while (l1 < n):
            l2 = jcast('int', 0)
            while (l2 < n):
                jset(dp[l1][l2], 1, (s1[l1] == s2[l2]))
                l2 = jcast('int', (l2 + 1))
            l1 = jcast('int', (l1 + 1))
        len = jcast('int', 2)
        while (len <= n):
            try:
                # 注意如下的边界条件 : l1 <= n - len l2 <= n - len
                l1 = jcast('int', 0)
                while (l1 <= jcast('int', (n - len))):
                    try:
                        l2 = jcast('int', 0)
                        while (l2 <= jcast('int', (n - len))):
                            try:
                                k = jcast('int', 1)
                                while (k < len):
                                    try:
                                        if (dp[l1][l2][k] and dp[jcast('int', jadd(l1, k))][jcast('int', jadd(l2, k))][jcast('int', (len - k))]):
                                            jset(dp[l1][l2], len, True)
                                            raise JBreak(None)
                                    except JContinue as _java_control_6:
                                        if _java_control_6.label not in (None,):
                                            raise
                                    except JBreak as _java_control_6:
                                        if _java_control_6.label not in (None,):
                                            raise
                                        break
                                    k = jcast('int', (k + 1))
                                if (not dp[l1][l2][len]):
                                    i = jcast('int', jcast('int', jadd(l1, 1)))
                                    j = jcast('int', jcast('int', (jcast('int', jadd(l2, len)) - 1)))
                                    k = jcast('int', 1)
                                    while (k < len):
                                        try:
                                            if (dp[l1][j][k] and dp[i][l2][jcast('int', (len - k))]):
                                                jset(dp[l1][l2], len, True)
                                                raise JBreak(None)
                                        except JContinue as _java_control_7:
                                            if _java_control_7.label not in (None,):
                                                raise
                                        except JBreak as _java_control_7:
                                            if _java_control_7.label not in (None,):
                                                raise
                                            break
                                        i = jcast('int', (i + 1))
                                        j = jcast('int', (j - 1))
                                        k = jcast('int', (k + 1))
                            except JContinue as _java_control_5:
                                if _java_control_5.label not in (None,):
                                    raise
                            except JBreak as _java_control_5:
                                if _java_control_5.label not in (None,):
                                    raise
                                break
                            l2 = jcast('int', (l2 + 1))
                    except JContinue as _java_control_4:
                        if _java_control_4.label not in (None,):
                            raise
                    except JBreak as _java_control_4:
                        if _java_control_4.label not in (None,):
                            raise
                        break
                    l1 = jcast('int', (l1 + 1))
            except JContinue as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
            except JBreak as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
                break
            len = jcast('int', (len + 1))
        return jcast('boolean', dp[0][0][n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


