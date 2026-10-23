# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 好子集的数目
# 给你一个整数数组 nums，好子集的定义如下：
# nums的某个子集，所有元素的乘积可以表示为一个或多个互不相同质数的乘积
# 比如nums = [1, 2, 3, 4]
# [2, 3]，[1, 2, 3]，[1, 3] 是好子集
# 乘积分别为6=2*3，6=2*3，3=3
# [1, 4]和[4]不是好子集，因为乘积分别为4=2*2和4=2*2
# 返回nums中不同的好子集的数目，答案对 1000000007 取模
# 如果两个子集删除的下标不同，那么它们被视为不同的子集
# 测试链接 : https://leetcode.cn/problems/the-number-of-good-subsets/
class Code03_TheNumberOfGoodSubsets:
    __java_fields__ = {'MAXV': 'MAXV', 'LIMIT': 'LIMIT', 'MOD': 'MOD', 'own': 'own', 'cnt': 'cnt', 'dp': 'dp'}
    MAXV = 0
    LIMIT = 0
    MOD = 0
    # 打个表来加速判断
    # 如果一个数字拥有某一种质数因子不只1个
    # 那么认为这个数字无效，状态全是0，0b0000000000
    # 如果一个数字拥有任何一种质数因子都不超过1个
    # 那么认为这个数字有效，用位信息表示这个数字拥有质数因子的状态
    # 比如12，拥有2这种质数因子不只1个，所以无效，用0b0000000000表示
    # 比如14，拥有2这种质数因子不超过1个，拥有7这种质数因子不超过1个，有效
    # 从高位到低位依次表示：...13 11 7 5 3 2
    # 所以用0b0000001001表示14拥有质数因子的状态
    # 质数: 29 23 19 17 13 11 7 5 3 2
    # 位置: 9 8 7 6 5 4 3 2 1 0
    # 0
    own = None
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    # 11
    # 12
    # 13
    # 14
    # 15
    # 16
    # 17
    # 18
    # 19
    # 20
    # 21
    # 22
    # 23
    # 24
    # 25
    # 26
    # 27
    # 28
    # 29
    # 30
    # 记忆化搜索
    @staticmethod
    def numberOfGoodSubsets1(nums):
        # 1 ~ 30
        cnt = jarray('int', [jcast('int', jadd(Code03_TheNumberOfGoodSubsets.MAXV, 1))])
        for num in nums:
            cnt[num] = jcast('int', (cnt[num] + 1))
        dp = jarray('int', [jcast('int', jadd(Code03_TheNumberOfGoodSubsets.MAXV, 1)), Code03_TheNumberOfGoodSubsets.LIMIT])
        i = jcast('int', 0)
        while (i <= Code03_TheNumberOfGoodSubsets.MAXV):
            jstatic('Arrays', 'fill', dp[i], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        s = jcast('int', 1)
        while (s < Code03_TheNumberOfGoodSubsets.LIMIT):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_TheNumberOfGoodSubsets.f1(Code03_TheNumberOfGoodSubsets.MAXV, s, cnt, dp))), Code03_TheNumberOfGoodSubsets.MOD)))
            s = jcast('int', (s + 1))
        return jcast('int', ans)

    # 1....i范围的数字，每种数字cnt[i]个
    # 最终相乘的结果一定要让质因子的状态为s，且每种质因子只能有1个
    # 请问子集的数量是多少
    # s每一位代表的质因子如下
    # 质数: 29 23 19 17 13 11 7 5 3 2
    # 位置: 9 8 7 6 5 4 3 2 1 0
    @staticmethod
    def f1(i, s, cnt, dp):
        i = jcast('int', i)
        s = jcast('int', s)
        if (dp[i][s] != jcast('int', (-1))):
            return jcast('int', dp[i][s])
        ans = jcast('int', 0)
        if (i == 1):
            if (s == 0):
                ans = jcast('int', 1)
                j = jcast('int', 0)
                while (j < cnt[1]):
                    ans = jcast('int', jcast('int', jmod(jcast('int', (ans << (1 & 31))), Code03_TheNumberOfGoodSubsets.MOD)))
                    j = jcast('int', (j + 1))
        else:
            ans = jcast('int', Code03_TheNumberOfGoodSubsets.f1(jcast('int', (i - 1)), s, cnt, dp))
            cur = jcast('int', Code03_TheNumberOfGoodSubsets.own[i])
            times = jcast('int', cnt[i])
            if (((cur != 0) and (times != 0)) and (jcast('int', (s & cur)) == cur)):
                # 能要i这个数字
                ans = jcast('int', jcast('int', jcast('long', jmod(jcast('long', jadd(jcast('long', (jcast('long', Code03_TheNumberOfGoodSubsets.f1(jcast('int', (i - 1)), jcast('int', (s ^ cur)), cnt, dp)) * times)), ans)), Code03_TheNumberOfGoodSubsets.MOD))))
        jset(dp[i], s, ans)
        return jcast('int', ans)

    # 空间压缩优化
    cnt = None
    dp = None
    @staticmethod
    def numberOfGoodSubsets2(nums):
        jstatic('Arrays', 'fill', Code03_TheNumberOfGoodSubsets.cnt, 0)
        jstatic('Arrays', 'fill', Code03_TheNumberOfGoodSubsets.dp, 0)
        for num in nums:
            Code03_TheNumberOfGoodSubsets.cnt[num] = jcast('int', (Code03_TheNumberOfGoodSubsets.cnt[num] + 1))
        Code03_TheNumberOfGoodSubsets.dp[0] = jcast('int', 1)
        i = jcast('int', 0)
        while (i < Code03_TheNumberOfGoodSubsets.cnt[1]):
            Code03_TheNumberOfGoodSubsets.dp[0] = jcast('int', jcast('int', jmod(jcast('int', (Code03_TheNumberOfGoodSubsets.dp[0] << (1 & 31))), Code03_TheNumberOfGoodSubsets.MOD)))
            i = jcast('int', (i + 1))
        i = jcast('int', 2)
        cur = 0
        times = 0
        while (i <= Code03_TheNumberOfGoodSubsets.MAXV):
            cur = jcast('int', Code03_TheNumberOfGoodSubsets.own[i])
            times = jcast('int', Code03_TheNumberOfGoodSubsets.cnt[i])
            if ((cur != 0) and (times != 0)):
                status = jcast('int', jcast('int', (Code03_TheNumberOfGoodSubsets.LIMIT - 1)))
                while (status >= 0):
                    if (jcast('int', (status & cur)) == cur):
                        Code03_TheNumberOfGoodSubsets.dp[status] = jcast('int', jcast('int', jcast('long', jmod(jcast('long', jadd(jcast('long', (jcast('long', Code03_TheNumberOfGoodSubsets.dp[jcast('int', (status ^ cur))]) * times)), Code03_TheNumberOfGoodSubsets.dp[status])), Code03_TheNumberOfGoodSubsets.MOD))))
                    status = jcast('int', (status - 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        s = jcast('int', 1)
        while (s < Code03_TheNumberOfGoodSubsets.LIMIT):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_TheNumberOfGoodSubsets.dp[s])), Code03_TheNumberOfGoodSubsets.MOD)))
            s = jcast('int', (s + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TheNumberOfGoodSubsets.MAXV = jcast('int', 30)
Code03_TheNumberOfGoodSubsets.LIMIT = jcast('int', jcast('int', (1 << (10 & 31))))
Code03_TheNumberOfGoodSubsets.MOD = jcast('int', 1000000007)
Code03_TheNumberOfGoodSubsets.own = jarray('int', [None], [0, 0, 1, 2, 0, 4, 3, 8, 0, 0, 5, 16, 0, 32, 9, 6, 0, 64, 0, 128, 0, 10, 17, 256, 0, 0, 33, 0, 0, 512, 7])
Code03_TheNumberOfGoodSubsets.cnt = jarray('int', [jcast('int', jadd(Code03_TheNumberOfGoodSubsets.MAXV, 1))])
Code03_TheNumberOfGoodSubsets.dp = jarray('int', [Code03_TheNumberOfGoodSubsets.LIMIT])
