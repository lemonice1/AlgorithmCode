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

# 增加限制的最长公共子序列问题
# 给定两个字符串s1和s2，s1长度为n，s2长度为m
# 返回s1和s2的最长公共子序列长度
# 注意：
# 两个字符串都只由小写字母组成
# 1 <= n <= 10^6
# 1 <= m <= 10^3
# 状态设计优化的经典题，对数器验证
class Code03_AddLimitLcs:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 's1': 's1', 's2': 's2', 'n': 'n', 'm': 'm', 'right': 'right', 'next': 'next', 'dp': 'dp', 'NA': 'NA'}
    # 为了测试
    @staticmethod
    def main(args):
        n = jcast('int', 100)
        m = jcast('int', 100)
        testTime = jcast('int', 10000)
        jprint('功能测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            size1 = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            size2 = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * m)), 1)))
            str1 = Code03_AddLimitLcs.randomString(size1)
            str2 = Code03_AddLimitLcs.randomString(size2)
            ans1 = jcast('int', Code03_AddLimitLcs.lcs1(str1, str2))
            ans2 = jcast('int', Code03_AddLimitLcs.lcs2(str1, str2))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('功能测试结束', newline=True)
        jprint(newline=True)
        jprint('性能测试开始', newline=True)
        n = jcast('int', 1000000)
        m = jcast('int', 1000)
        jprint(jadd('n = ', n), newline=True)
        jprint(jadd('m = ', m), newline=True)
        str1 = Code03_AddLimitLcs.randomString(n)
        str2 = Code03_AddLimitLcs.randomString(m)
        start = 0
        end = 0
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        Code03_AddLimitLcs.lcs1(str1, str2)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('lcs1方法运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        Code03_AddLimitLcs.lcs2(str1, str2)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('lcs2方法运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        jprint('性能测试结束', newline=True)

    # 为了测试
    # 随机生成长度为n只有小写字母构成的字符串
    @staticmethod
    def randomString(n):
        n = jcast('int', n)
        ans = jarray('char', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('char', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * 26)), jchar('a')))))
            i = jcast('int', (i + 1))
        return jstatic('String', 'valueOf', ans)

    # 经典动态规划的版本
    # 来自讲解067，题目3，最经典的方法4
    # 不利用任何限制，时间复杂度O(n*m)
    @staticmethod
    def lcs1(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= m):
                if (s1[jcast('int', (i - 1))] == s2[jcast('int', (j - 1))]):
                    jset(dp[i], j, jcast('int', jadd(1, dp[jcast('int', (i - 1))][jcast('int', (j - 1))])))
                else:
                    jset(dp[i], j, jstatic('Math', 'max', dp[jcast('int', (i - 1))][j], dp[i][jcast('int', (j - 1))]))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n][m])

    # 利用限制条件做优化的版本
    # 时间复杂度O(26*n + m^2)
    MAXN = 0
    MAXM = 0
    s1 = None
    s2 = None
    n = 0
    m = 0
    right = None
    next = None
    dp = None
    NA = 0
    @staticmethod
    def lcs2(str1, str2):
        Code03_AddLimitLcs.s1 = jcall(str1, 'toCharArray')
        Code03_AddLimitLcs.s2 = jcall(str2, 'toCharArray')
        Code03_AddLimitLcs.n = jcast('int', jget(Code03_AddLimitLcs.s1, 'length'))
        Code03_AddLimitLcs.m = jcast('int', jget(Code03_AddLimitLcs.s2, 'length'))
        Code03_AddLimitLcs.build()
        ans = jcast('int', 0)
        j = jcast('int', Code03_AddLimitLcs.m)
        while (j >= 1):
            try:
                if (Code03_AddLimitLcs.f(Code03_AddLimitLcs.m, j) != Code03_AddLimitLcs.NA):
                    ans = jcast('int', j)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            j = jcast('int', (j - 1))
        return jcast('int', ans)

    @staticmethod
    def build():
        j = jcast('int', 0)
        while (j < 26):
            Code03_AddLimitLcs.right[j] = jcast('int', Code03_AddLimitLcs.NA)
            j = jcast('int', (j + 1))
        i = jcast('int', Code03_AddLimitLcs.n)
        while (i >= 0):
            j = jcast('int', 0)
            while (j < 26):
                jset(Code03_AddLimitLcs.next[i], j, Code03_AddLimitLcs.right[j])
                j = jcast('int', (j + 1))
            if (i > 0):
                # s1的i长度，对应的字符是s1[i-1]
                jset(Code03_AddLimitLcs.right, jcast('int', (Code03_AddLimitLcs.s1[jcast('int', (i - 1))] - jchar('a'))), i)
            i = jcast('int', (i - 1))
        i = jcast('int', 0)
        while (i <= Code03_AddLimitLcs.m):
            j = jcast('int', 0)
            while (j <= Code03_AddLimitLcs.m):
                jset(Code03_AddLimitLcs.dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    # 长度为i的s2前缀串，想和s1字符串形成长度为j的公共子序列
    # 返回至少需要多长的s1前缀串才能做到
    # 如果怎么都做不到，返回NA
    @staticmethod
    def f(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if (i < j):
            return jcast('int', Code03_AddLimitLcs.NA)
        if (j == 0):
            return jcast('int', 0)
        if (Code03_AddLimitLcs.dp[i][j] != jcast('int', (-1))):
            return jcast('int', Code03_AddLimitLcs.dp[i][j])
        # s2前缀串长度为i，最后字符s2[i-1]
        cha = jcast('int', jcast('int', (Code03_AddLimitLcs.s2[jcast('int', (i - 1))] - jchar('a'))))
        ans = jcast('int', Code03_AddLimitLcs.f(jcast('int', (i - 1)), j))
        pre = jcast('int', Code03_AddLimitLcs.f(jcast('int', (i - 1)), jcast('int', (j - 1))))
        if (pre != Code03_AddLimitLcs.NA):
            ans = jcast('int', jstatic('Math', 'min', ans, Code03_AddLimitLcs.next[pre][cha]))
        jset(Code03_AddLimitLcs.dp[i], j, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_AddLimitLcs.MAXN = jcast('int', 1000005)
Code03_AddLimitLcs.MAXM = jcast('int', 1005)
Code03_AddLimitLcs.s1 = None
Code03_AddLimitLcs.s2 = None
Code03_AddLimitLcs.n = jcast('int', 0)
Code03_AddLimitLcs.m = jcast('int', 0)
Code03_AddLimitLcs.right = jarray('int', [26])
Code03_AddLimitLcs.next = jarray('int', [Code03_AddLimitLcs.MAXN, 26])
Code03_AddLimitLcs.dp = jarray('int', [Code03_AddLimitLcs.MAXM, Code03_AddLimitLcs.MAXM])
Code03_AddLimitLcs.NA = jcast('int', jget(Integer, 'MAX_VALUE'))

if __name__ == '__main__':
    Code03_AddLimitLcs.main([])
