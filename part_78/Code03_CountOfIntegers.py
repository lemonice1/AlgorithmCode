# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 统计整数数目
# 给你两个数字字符串 num1 和 num2 ，以及两个整数max_sum和min_sum
# 如果一个整数 x 满足以下条件，我们称它是一个好整数
# num1 <= x <= num2
# min_sum <= digit_sum(x) <= max_sum
# 请你返回好整数的数目
# 答案可能很大，答案对 1000000007 取模
# 注意，digit_sum(x)表示x各位数字之和
# 测试链接 : https://leetcode.cn/problems/count-of-integers/
class Code03_CountOfIntegers:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'MAXM': 'MAXM', 'dp': 'dp', 'num': 'num', 'min': 'min', 'max': 'max', 'len': 'len'}
    MOD = 0
    MAXN = 0
    MAXM = 0
    dp = None
    @staticmethod
    def build():
        i = jcast('int', 0)
        while (i < Code03_CountOfIntegers.len):
            j = jcast('int', 0)
            while (j <= Code03_CountOfIntegers.max):
                jset(Code03_CountOfIntegers.dp[i][j], 0, jcast('int', (-1)))
                jset(Code03_CountOfIntegers.dp[i][j], 1, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    num = None
    min = 0
    max = 0
    len = 0
    @staticmethod
    def count(num1, num2, min_sum, max_sum):
        min_sum = jcast('int', min_sum)
        max_sum = jcast('int', max_sum)
        Code03_CountOfIntegers.min = jcast('int', min_sum)
        Code03_CountOfIntegers.max = jcast('int', max_sum)
        Code03_CountOfIntegers.num = jcall(num2, 'toCharArray')
        Code03_CountOfIntegers.len = jcast('int', jcall(num2, 'length'))
        Code03_CountOfIntegers.build()
        ans = jcast('int', Code03_CountOfIntegers.f(0, 0, 0))
        Code03_CountOfIntegers.num = jcall(num1, 'toCharArray')
        Code03_CountOfIntegers.len = jcast('int', jcall(num1, 'length'))
        Code03_CountOfIntegers.build()
        ans = jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', (ans - Code03_CountOfIntegers.f(0, 0, 0))), Code03_CountOfIntegers.MOD)), Code03_CountOfIntegers.MOD)))
        if Code03_CountOfIntegers.check():
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, 1)), Code03_CountOfIntegers.MOD)))
        return jcast('int', ans)

    # 注意：
    # 数字，char[] num
    # 数字长度，int len
    # 累加和最小要求，int min
    # 累加和最大要求，int max
    # 这四个变量都是全局静态变量，所以不用带参数，直接访问即可
    # 递归含义：
    # 从num的高位出发，当前来到i位上
    # 之前决定的数字累加和是sum
    # 之前的决定已经比num小，后续可以自由选择数字，那么free == 1
    # 之前的决定和num一样，后续不可以自由选择数字，那么free == 0
    # 返回有多少种可能性
    @staticmethod
    def f(i, sum, free):
        i = jcast('int', i)
        sum = jcast('int', sum)
        free = jcast('int', free)
        if (sum > Code03_CountOfIntegers.max):
            return jcast('int', 0)
        if (jcast('int', jadd(sum, jcast('int', (jcast('int', (Code03_CountOfIntegers.len - i)) * 9)))) < Code03_CountOfIntegers.min):
            return jcast('int', 0)
        if (i == Code03_CountOfIntegers.len):
            return jcast('int', 1)
        if (Code03_CountOfIntegers.dp[i][sum][free] != jcast('int', (-1))):
            return jcast('int', Code03_CountOfIntegers.dp[i][sum][free])
        # cur : num当前位的数字
        cur = jcast('int', jcast('int', (Code03_CountOfIntegers.num[i] - jchar('0'))))
        ans = jcast('int', 0)
        if (free == 0):
            # 还不能自由选择
            pick = jcast('int', 0)
            while (pick < cur):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_CountOfIntegers.f(jcast('int', jadd(i, 1)), jcast('int', jadd(sum, pick)), 1))), Code03_CountOfIntegers.MOD)))
                pick = jcast('int', (pick + 1))
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_CountOfIntegers.f(jcast('int', jadd(i, 1)), jcast('int', jadd(sum, cur)), 0))), Code03_CountOfIntegers.MOD)))
        else:
            # 可以自由选择
            pick = jcast('int', 0)
            while (pick <= 9):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_CountOfIntegers.f(jcast('int', jadd(i, 1)), jcast('int', jadd(sum, pick)), 1))), Code03_CountOfIntegers.MOD)))
                pick = jcast('int', (pick + 1))
        jset(Code03_CountOfIntegers.dp[i][sum], free, ans)
        return jcast('int', ans)

    @staticmethod
    def check():
        sum = jcast('int', 0)
        for cha in Code03_CountOfIntegers.num:
            sum = jcast('int', jcast('int', jadd(sum, jcast('int', (cha - jchar('0'))))))
        return jcast('boolean', ((sum >= Code03_CountOfIntegers.min) and (sum <= Code03_CountOfIntegers.max)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_CountOfIntegers.MOD = jcast('int', 1000000007)
Code03_CountOfIntegers.MAXN = jcast('int', 23)
Code03_CountOfIntegers.MAXM = jcast('int', 401)
Code03_CountOfIntegers.dp = jarray('int', [Code03_CountOfIntegers.MAXN, Code03_CountOfIntegers.MAXM, 2])
Code03_CountOfIntegers.num = None
Code03_CountOfIntegers.min = jcast('int', 0)
Code03_CountOfIntegers.max = jcast('int', 0)
Code03_CountOfIntegers.len = jcast('int', 0)
