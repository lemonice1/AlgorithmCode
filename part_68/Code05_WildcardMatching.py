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

# 通配符匹配（和题目4高度相似，只是边界条件不同而已，而且更简单）
# 给你字符串s、字符串p
# s中一定不含有'?'、'*'字符，p中可能含有'?'、'*'字符
# '?' 表示可以变成任意字符，数量1个
# '*' 表示可以匹配任何字符串
# 请实现一个支持 '?' 和 '*' 的通配符匹配
# 返回p的整个字符串能不能匹配出s的整个字符串
# 测试链接 : https://leetcode.cn/problems/wildcard-matching/
class Code05_WildcardMatching:
    __java_fields__ = {}
    # 暴力递归
    @staticmethod
    def isMatch1(str, pat):
        s = jcall(str, 'toCharArray')
        p = jcall(pat, 'toCharArray')
        return jcast('boolean', Code05_WildcardMatching.f1(s, p, 0, 0))

    # s[i....]能不能被p[j....]完全匹配出来
    @staticmethod
    def f1(s, p, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if (i == jget(s, 'length')):
            # s没了
            if (j == jget(p, 'length')):
                # 如果p也没了，返回true
                return jcast('boolean', True)
            else:
                # 如果p[j]是*，可以消掉，然后看看p[j+1....]是不是都能消掉
                return jcast('boolean', ((p[j] == jchar('*')) and Code05_WildcardMatching.f1(s, p, i, jcast('int', jadd(j, 1)))))
        else:
            if (j == jget(p, 'length')):
                # s有
                # p没了
                return jcast('boolean', False)
            else:
                if (p[j] != jchar('*')):
                    # s[i....]
                    # p[j....]
                    # 如果p[j]不是*，那么当前的字符必须能匹配：(s[i] == p[j] || p[j] == '?')
                    # 同时，后续也必须匹配上：process1(s, p, i + 1, j + 1);
                    return jcast('boolean', (((s[i] == p[j]) or (p[j] == jchar('?'))) and Code05_WildcardMatching.f1(s, p, jcast('int', jadd(i, 1)), jcast('int', jadd(j, 1)))))
                else:
                    # s[i....]
                    # p[j....]
                    # 如果p[j]是*
                    # 选择1: 反正当前p[j]是*，必然可以搞定s[i]，那么继续 : process1(s, p, i + 1, j)
                    # 选择2: 虽然当前p[j]是*，但就是不让它搞定s[i]，那么继续 : process1(s, p, i, j + 1)
                    # 两种选择有一个能走通，答案就是true；如果都搞不定，答案就是false
                    return jcast('boolean', (Code05_WildcardMatching.f1(s, p, jcast('int', jadd(i, 1)), j) or Code05_WildcardMatching.f1(s, p, i, jcast('int', jadd(j, 1)))))

    # 记忆化搜索
    @staticmethod
    def isMatch2(str, pat):
        s = jcall(str, 'toCharArray')
        p = jcall(pat, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        m = jcast('int', jget(p, 'length'))
        # dp[i][j] == 0，表示没算过
        # dp[i][j] == 1，表示算过，答案是true
        # dp[i][j] == 2，表示算过，答案是false
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        return jcast('boolean', Code05_WildcardMatching.f2(s, p, 0, 0, dp))

    @staticmethod
    def f2(s, p, i, j, dp):
        i = jcast('int', i)
        j = jcast('int', j)
        if (dp[i][j] != 0):
            return jcast('boolean', (dp[i][j] == 1))
        ans = False
        if (i == jget(s, 'length')):
            if (j == jget(p, 'length')):
                ans = jcast('boolean', True)
            else:
                ans = jcast('boolean', ((p[j] == jchar('*')) and Code05_WildcardMatching.f2(s, p, i, jcast('int', jadd(j, 1)), dp)))
        else:
            if (j == jget(p, 'length')):
                ans = jcast('boolean', False)
            else:
                if (p[j] != jchar('*')):
                    ans = jcast('boolean', (((s[i] == p[j]) or (p[j] == jchar('?'))) and Code05_WildcardMatching.f2(s, p, jcast('int', jadd(i, 1)), jcast('int', jadd(j, 1)), dp)))
                else:
                    ans = jcast('boolean', (Code05_WildcardMatching.f2(s, p, jcast('int', jadd(i, 1)), j, dp) or Code05_WildcardMatching.f2(s, p, i, jcast('int', jadd(j, 1)), dp)))
        jset(dp[i], j, (1 if ans else 2))
        return jcast('boolean', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def isMatch3(str, pat):
        s = jcall(str, 'toCharArray')
        p = jcall(pat, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        m = jcast('int', jget(p, 'length'))
        dp = jarray('boolean', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        jset(dp[n], m, True)
        j = jcast('int', jcast('int', (m - 1)))
        while ((j >= 0) and (p[j] == jchar('*'))):
            jset(dp[n], j, True)
            j = jcast('int', (j - 1))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            j = jcast('int', jcast('int', (m - 1)))
            while (j >= 0):
                if (p[j] != jchar('*')):
                    jset(dp[i], j, (((s[i] == p[j]) or (p[j] == jchar('?'))) and dp[jcast('int', jadd(i, 1))][jcast('int', jadd(j, 1))]))
                else:
                    jset(dp[i], j, (dp[jcast('int', jadd(i, 1))][j] or dp[i][jcast('int', jadd(j, 1))]))
                j = jcast('int', (j - 1))
            i = jcast('int', (i - 1))
        return jcast('boolean', dp[0][0])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


