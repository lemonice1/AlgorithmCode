# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 正则表达式匹配
# 给你字符串s、字符串p
# s中一定不含有'.'、'*'字符，p中可能含有'.'、'*'字符
# '.' 表示可以变成任意字符，数量1个
# '*' 表示可以让 '*' 前面那个字符数量任意(甚至可以是0个)
# p中即便有'*'，一定不会出现以'*'开头的情况，也一定不会出现多个'*'相邻的情况(无意义)
# 请实现一个支持 '.' 和 '*' 的正则表达式匹配
# 返回p的整个字符串能不能匹配出s的整个字符串
# 测试链接 : https://leetcode.cn/problems/regular-expression-matching/
class Code04_RegularExpressionMatching:
    __java_fields__ = {}
    @staticmethod
    def isMatch1(str, pat):
        s = jcall(str, 'toCharArray')
        p = jcall(pat, 'toCharArray')
        return jcast('boolean', Code04_RegularExpressionMatching.f1(s, p, 0, 0))

    # s[i....]能不能被p[j....]完全匹配出来
    # p[j]这个字符，一定不是'*'
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
                # p还剩下一些后缀
                # 如果p[j+1]是*，那么p[j..j+1]可以消掉，然后看看p[j+2....]是不是都能消掉
                return jcast('boolean', (((jcast('int', jadd(j, 1)) < jget(p, 'length')) and (p[jcast('int', jadd(j, 1))] == jchar('*'))) and Code04_RegularExpressionMatching.f1(s, p, i, jcast('int', jadd(j, 2)))))
        else:
            if (j == jget(p, 'length')):
                # s有后缀
                # p没后缀了
                return jcast('boolean', False)
            else:
                # s有后缀
                # p有后缀
                if ((jcast('int', jadd(j, 1)) == jget(p, 'length')) or (p[jcast('int', jadd(j, 1))] != jchar('*'))):
                    # s[i....]
                    # p[j....]
                    # 如果p[j+1]不是*，那么当前的字符必须能匹配：(s[i] == p[j] || p[j] == '?')
                    # 同时，后续也必须匹配上：process1(s, p, i + 1, j + 1);
                    return jcast('boolean', (((s[i] == p[j]) or (p[j] == jchar('.'))) and Code04_RegularExpressionMatching.f1(s, p, jcast('int', jadd(i, 1)), jcast('int', jadd(j, 1)))))
                else:
                    # 如果p[j+1]是*
                    # 完全背包！
                    # s[i....]
                    # p[j....]
                    # 选择1: 当前p[j..j+1]是x*，就是不让它搞定s[i]，那么继续 : process1(s, p, i, j + 2)
                    p1 = jcast('boolean', Code04_RegularExpressionMatching.f1(s, p, i, jcast('int', jadd(j, 2))))
                    # 选择2: 当前p[j..j+1]是x*，如果可以搞定s[i]，那么继续 : process1(s, p, i + 1, j)
                    # 如果可以搞定s[i] : (s[i] == p[j] || p[j] == '.')
                    # 继续匹配 : process1(s, p, i + 1, j)
                    p2 = jcast('boolean', (((s[i] == p[j]) or (p[j] == jchar('.'))) and Code04_RegularExpressionMatching.f1(s, p, jcast('int', jadd(i, 1)), j)))
                    # 两个选择，有一个可以搞定就返回true，都无法搞定返回false
                    return jcast('boolean', (p1 or p2))

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
        return jcast('boolean', Code04_RegularExpressionMatching.f2(s, p, 0, 0, dp))

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
                ans = jcast('boolean', (((jcast('int', jadd(j, 1)) < jget(p, 'length')) and (p[jcast('int', jadd(j, 1))] == jchar('*'))) and Code04_RegularExpressionMatching.f2(s, p, i, jcast('int', jadd(j, 2)), dp)))
        else:
            if (j == jget(p, 'length')):
                ans = jcast('boolean', False)
            else:
                if ((jcast('int', jadd(j, 1)) == jget(p, 'length')) or (p[jcast('int', jadd(j, 1))] != jchar('*'))):
                    ans = jcast('boolean', (((s[i] == p[j]) or (p[j] == jchar('.'))) and Code04_RegularExpressionMatching.f2(s, p, jcast('int', jadd(i, 1)), jcast('int', jadd(j, 1)), dp)))
                else:
                    ans = jcast('boolean', (Code04_RegularExpressionMatching.f2(s, p, i, jcast('int', jadd(j, 2)), dp) or (((s[i] == p[j]) or (p[j] == jchar('.'))) and Code04_RegularExpressionMatching.f2(s, p, jcast('int', jadd(i, 1)), j, dp))))
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
        while (j >= 0):
            jset(dp[n], j, (((jcast('int', jadd(j, 1)) < m) and (p[jcast('int', jadd(j, 1))] == jchar('*'))) and dp[n][jcast('int', jadd(j, 2))]))
            j = jcast('int', (j - 1))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            j = jcast('int', jcast('int', (m - 1)))
            while (j >= 0):
                if ((jcast('int', jadd(j, 1)) == m) or (p[jcast('int', jadd(j, 1))] != jchar('*'))):
                    jset(dp[i], j, (((s[i] == p[j]) or (p[j] == jchar('.'))) and dp[jcast('int', jadd(i, 1))][jcast('int', jadd(j, 1))]))
                else:
                    jset(dp[i], j, (dp[i][jcast('int', jadd(j, 2))] or (((s[i] == p[j]) or (p[j] == jchar('.'))) and dp[jcast('int', jadd(i, 1))][j])))
                j = jcast('int', (j - 1))
            i = jcast('int', (i - 1))
        return jcast('boolean', dp[0][0])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


