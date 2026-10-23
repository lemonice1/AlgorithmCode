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

# 使数组严格递增的最小操作数
# 给你两个整数数组 arr1 和 arr2
# 返回使 arr1 严格递增所需要的最小操作数（可能为0）
# 每一步操作中，你可以分别从 arr1 和 arr2 中各选出一个索引
# 分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length
# 然后进行赋值运算 arr1[i] = arr2[j]
# 如果无法让 arr1 严格递增，请返回-1
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9
# 测试链接 : https://leetcode.cn/problems/make-array-strictly-increasing/
class Code04_MakeArrayStrictlyIncreasing:
    __java_fields__ = {}
    @staticmethod
    def makeArrayIncreasing1(arr1, arr2):
        jstatic('Arrays', 'sort', arr2)
        m = jcast('int', 1)
        i = jcast('int', 1)
        while (i < jget(arr2, 'length')):
            if (arr2[i] != arr2[jcast('int', (m - 1))]):
                jset(arr2, ((_java_old_1 := m), (m := jcast('int', (m + (1)))), _java_old_1)[2], arr2[i])
            i = jcast('int', (i + 1))
        n = jcast('int', jget(arr1, 'length'))
        dp = jarray('int', [n])
        jstatic('Arrays', 'fill', dp, jcast('int', (-1)))
        ans = jcast('int', Code04_MakeArrayStrictlyIncreasing.f1(arr1, arr2, n, m, 0, dp))
        return jcast('int', (jcast('int', (-1)) if (ans == jget(Integer, 'MAX_VALUE')) else ans))

    # arr1长度为n，arr2有效部分长度为m
    # arr2有效部分可以替换arr1中的数字
    # arr1[0..i-1]已经严格递增且arr1[i-1]一定没有替换
    # 返回让arr1整体都严格递增，arr1[i...]范围上还需要几次替换
    # 如果做不到，返回无穷大
    @staticmethod
    def f1(arr1, arr2, n, m, i, dp):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', i)
        if (i == n):
            return jcast('int', 0)
        if (dp[i] != jcast('int', (-1))):
            return jcast('int', dp[i])
        # ans : 遍历所有的分支，所得到的最少的操作次数
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        # pre : 前一位的数字
        pre = jcast('int', (jget(Integer, 'MIN_VALUE') if (i == 0) else arr1[jcast('int', (i - 1))]))
        # find : arr2有效长度m的范围上，找到刚比pre大的位置
        find = jcast('int', Code04_MakeArrayStrictlyIncreasing.bs(arr2, m, pre))
        # 枚举arr1[i...]范围上，第一个不需要替换的位置j
        j = jcast('int', i)
        k = jcast('int', 0)
        next = 0
        while (j <= n):
            try:
                if (j == n):
                    ans = jcast('int', jstatic('Math', 'min', ans, k))
                else:
                    # pre : 被arr2替换的前一位数字
                    if (pre < arr1[j]):
                        next = jcast('int', Code04_MakeArrayStrictlyIncreasing.f1(arr1, arr2, n, m, jcast('int', jadd(j, 1)), dp))
                        if (next != jget(Integer, 'MAX_VALUE')):
                            ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(k, next))))
                    if ((find != jcast('int', (-1))) and (find < m)):
                        pre = jcast('int', arr2[((_java_old_3 := find), (find := jcast('int', (find + (1)))), _java_old_3)[2]])
                    else:
                        raise JBreak(None)
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
            j = jcast('int', (j + 1))
            k = jcast('int', (k + 1))
        dp[i] = jcast('int', ans)
        return jcast('int', ans)

    # arr2[0..size-1]范围上是严格递增的
    # 找到这个范围上>num的最左位置
    # 不存在返回-1
    @staticmethod
    def bs(arr2, size, num):
        size = jcast('int', size)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (size - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (arr2[m] > num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    # 和方法1的思路没有区别
    # 甚至填写dp表的逻辑都保持一致
    @staticmethod
    def makeArrayIncreasing2(arr1, arr2):
        jstatic('Arrays', 'sort', arr2)
        m = jcast('int', 1)
        i = jcast('int', 1)
        while (i < jget(arr2, 'length')):
            if (arr2[i] != arr2[jcast('int', (m - 1))]):
                jset(arr2, ((_java_old_4 := m), (m := jcast('int', (m + (1)))), _java_old_4)[2], arr2[i])
            i = jcast('int', (i + 1))
        n = jcast('int', jget(arr1, 'length'))
        dp = jarray('int', [jcast('int', jadd(n, 1))])
        i = jcast('int', jcast('int', (n - 1)))
        ans = 0
        pre = 0
        find = 0
        while (i >= 0):
            try:
                ans = jcast('int', jget(Integer, 'MAX_VALUE'))
                pre = jcast('int', (jget(Integer, 'MIN_VALUE') if (i == 0) else arr1[jcast('int', (i - 1))]))
                find = jcast('int', Code04_MakeArrayStrictlyIncreasing.bs(arr2, m, pre))
                j = jcast('int', i)
                k = jcast('int', 0)
                next = 0
                while (j <= n):
                    try:
                        if (j == n):
                            ans = jcast('int', jstatic('Math', 'min', ans, k))
                        else:
                            if (pre < arr1[j]):
                                next = jcast('int', dp[jcast('int', jadd(j, 1))])
                                if (next != jget(Integer, 'MAX_VALUE')):
                                    ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(k, next))))
                            if ((find != jcast('int', (-1))) and (find < m)):
                                pre = jcast('int', arr2[((_java_old_7 := find), (find := jcast('int', (find + (1)))), _java_old_7)[2]])
                            else:
                                raise JBreak(None)
                    except JContinue as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                    except JBreak as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                    k = jcast('int', (k + 1))
                dp[i] = jcast('int', ans)
            except JContinue as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
            except JBreak as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
                break
            i = jcast('int', (i - 1))
        return jcast('int', (jcast('int', (-1)) if (dp[0] == jget(Integer, 'MAX_VALUE')) else dp[0]))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


