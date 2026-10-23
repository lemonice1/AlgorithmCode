# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 找到所有好字符串
# 给你两个长度为n的字符串s1和s2，以及一个字符串evil
# 好字符串的定义为 : 长度为n，字典序大于等于s1，字典序小于等于s2，且不包含evil字符串
# 返回好字符串的数量
# 由于答案可能很大，答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/find-all-good-strings/
class Code04_FindAllGoodStrings:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'MAXM': 'MAXM', 'dp': 'dp', 'next': 'next'}
    MOD = 0
    MAXN = 0
    MAXM = 0
    dp = None
    next = None
    @staticmethod
    def clear(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                jset(Code04_FindAllGoodStrings.dp[i][j], 0, jcast('int', (-1)))
                jset(Code04_FindAllGoodStrings.dp[i][j], 1, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def findGoodStrings(n, str1, str2, evil):
        n = jcast('int', n)
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        e = jcall(evil, 'toCharArray')
        m = jcast('int', jget(e, 'length'))
        Code04_FindAllGoodStrings.nextArray(e, m)
        Code04_FindAllGoodStrings.clear(n, m)
        # <=s2的好字符串数量
        ans = jcast('int', Code04_FindAllGoodStrings.f(s2, e, n, m, 0, 0, 0))
        Code04_FindAllGoodStrings.clear(n, m)
        # 减去<=s1的好字符串数量
        ans = jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', (ans - Code04_FindAllGoodStrings.f(s1, e, n, m, 0, 0, 0))), Code04_FindAllGoodStrings.MOD)), Code04_FindAllGoodStrings.MOD)))
        if (Code04_FindAllGoodStrings.kmp(s1, e, n, m) == jcast('int', (-1))):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, 1)), Code04_FindAllGoodStrings.MOD)))
        return jcast('int', ans)

    @staticmethod
    def kmp(s, e, n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        x = jcast('int', 0)
        y = jcast('int', 0)
        while ((x < n) and (y < m)):
            if (s[x] == e[y]):
                x = jcast('int', (x + 1))
                y = jcast('int', (y + 1))
            else:
                if (y == 0):
                    x = jcast('int', (x + 1))
                else:
                    y = jcast('int', Code04_FindAllGoodStrings.next[y])
        return jcast('int', (jcast('int', (x - y)) if (y == m) else jcast('int', (-1))))

    @staticmethod
    def nextArray(e, m):
        m = jcast('int', m)
        Code04_FindAllGoodStrings.next[0] = jcast('int', jcast('int', (-1)))
        Code04_FindAllGoodStrings.next[1] = jcast('int', 0)
        i = jcast('int', 2)
        cn = jcast('int', 0)
        while (i < m):
            if (e[jcast('int', (i - 1))] == e[cn]):
                jset(Code04_FindAllGoodStrings.next, ((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2], (cn := jcast('int', (cn + (1)))))
            else:
                if (cn > 0):
                    cn = jcast('int', Code04_FindAllGoodStrings.next[cn])
                else:
                    jset(Code04_FindAllGoodStrings.next, ((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2], 0)

    # 时间复杂度O(n * m * 2 * 26)
    # s、e、n、m都是固定参数
    # 0...i-1已经做了决策，已经匹配了e[0...j-1]这个部分
    # 当前来到s[i]时，最先该考察的匹配位置是e[j]
    # 之前的决策如果已经比s小了，free == 1
    # 之前的决策如果和s[0..i-1]一样，free == 0
    # 返回后续的所有决策中，不含有e字符串且<=s的决策有多少个，同时长度需要为n
    # 核心 : 利用e字符串的next数组加速匹配
    @staticmethod
    def f(s, e, n, m, i, j, free):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', i)
        j = jcast('int', j)
        free = jcast('int', free)
        if (j == m):
            # 一旦配出了e的整体
            # 说明之前的决策已经违规
            # 后续有效决策数量0
            return jcast('int', 0)
        # 能跑如下代码
        # 之前的决策不含有整个e字符串
        if (i == n):
            # 说明所有决策已经做完了
            # 并且不含有e字符串
            # 同时决策的每一步都保证了不会比s大
            # 返回1种有效决策(之前做的所有决定)
            return jcast('int', 1)
        if (Code04_FindAllGoodStrings.dp[i][j][free] != jcast('int', (-1))):
            return jcast('int', Code04_FindAllGoodStrings.dp[i][j][free])
        cur = jcast('char', s[i])
        ans = jcast('int', 0)
        if (free == 0):
            # 之前的决策和s的状况一样
            # 当前尝试比cur小的字符
            pick = jcast('char', jchar('a'))
            while (pick < cur):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code04_FindAllGoodStrings.f(s, e, n, m, jcast('int', jadd(i, 1)), jcast('int', jadd(Code04_FindAllGoodStrings.jump(pick, e, j), 1)), 1))), Code04_FindAllGoodStrings.MOD)))
                pick = jcast('char', (pick + 1))
            # 当前尝试等于cur的字符
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code04_FindAllGoodStrings.f(s, e, n, m, jcast('int', jadd(i, 1)), jcast('int', jadd(Code04_FindAllGoodStrings.jump(cur, e, j), 1)), 0))), Code04_FindAllGoodStrings.MOD)))
        else:
            # 之前的决策已经确定小于s了
            # 当前a~z随便尝试
            pick = jcast('char', jchar('a'))
            while (pick <= jchar('z')):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code04_FindAllGoodStrings.f(s, e, n, m, jcast('int', jadd(i, 1)), jcast('int', jadd(Code04_FindAllGoodStrings.jump(pick, e, j), 1)), 1))), Code04_FindAllGoodStrings.MOD)))
                pick = jcast('char', (pick + 1))
        jset(Code04_FindAllGoodStrings.dp[i][j], free, ans)
        return jcast('int', ans)

    # 当前字符是pick，一开始匹配e[j]
    # 根据next数组加速匹配，返回匹配出来的位置
    # 如果匹配不出来返回-1
    # 单次调用的时间复杂度O(1)
    @staticmethod
    def jump(pick, e, j):
        pick = jcast('char', pick)
        j = jcast('int', j)
        while ((j >= 0) and (pick != e[j])):
            j = jcast('int', Code04_FindAllGoodStrings.next[j])
        return jcast('int', j)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_FindAllGoodStrings.MOD = jcast('int', 1000000007)
Code04_FindAllGoodStrings.MAXN = jcast('int', 501)
Code04_FindAllGoodStrings.MAXM = jcast('int', 51)
Code04_FindAllGoodStrings.dp = jarray('int', [Code04_FindAllGoodStrings.MAXN, Code04_FindAllGoodStrings.MAXM, 2])
Code04_FindAllGoodStrings.next = jarray('int', [Code04_FindAllGoodStrings.MAXM])
