# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 计数质数
# 给定整数n，返回小于非负整数n的质数的数量
# 测试链接 : https://leetcode.cn/problems/count-primes/
class Code04_EhrlichAndEuler:
    __java_fields__ = {}
    @staticmethod
    def countPrimes(n):
        n = jcast('int', n)
        return jcast('int', Code04_EhrlichAndEuler.ehrlich(jcast('int', (n - 1))))

    # 埃氏筛统计0 ~ n范围内的质数个数
    # 时间复杂度O(n * log(logn))
    @staticmethod
    def ehrlich(n):
        n = jcast('int', n)
        # visit[i] = true，代表i是合数
        # visit[i] = false，代表i是质数
        # 初始时认为0~n所有数都是质数
        visit = jarray('boolean', [jcast('int', jadd(n, 1))])
        i = jcast('int', 2)
        while (jcast('int', (i * i)) <= n):
            if (not visit[i]):
                j = jcast('int', jcast('int', (i * i)))
                while (j <= n):
                    visit[j] = jcast('boolean', True)
                    j = jcast('int', jcast('int', jadd(j, i)))
            i = jcast('int', (i + 1))
        cnt = jcast('int', 0)
        i = jcast('int', 2)
        while (i <= n):
            if (not visit[i]):
                # 此时i就是质数，可以收集，也可以计数
                cnt = jcast('int', (cnt + 1))
            i = jcast('int', (i + 1))
        return jcast('int', cnt)

    # 欧拉筛统计0 ~ n范围内的质数个数
    # 时间复杂度O(n)
    @staticmethod
    def euler(n):
        n = jcast('int', n)
        # visit[i] = true，代表i是合数
        # visit[i] = false，代表i是质数
        # 初始时认为0~n所有数都是质数
        visit = jarray('boolean', [jcast('int', jadd(n, 1))])
        # prime收集所有的质数，收集的个数是cnt
        prime = jarray('int', [jcast('int', jadd(jcast('int', jdiv(n, 2)), 1))])
        cnt = jcast('int', 0)
        i = jcast('int', 2)
        while (i <= n):
            try:
                if (not visit[i]):
                    jset(prime, ((_java_old_2 := cnt), (cnt := jcast('int', (cnt + (1)))), _java_old_2)[2], i)
                j = jcast('int', 0)
                while (j < cnt):
                    try:
                        if (jcast('int', (i * prime[j])) > n):
                            raise JBreak(None)
                        jset(visit, jcast('int', (i * prime[j])), True)
                        if (jcast('int', jmod(i, prime[j])) == 0):
                            raise JBreak(None)
                    except JContinue as _java_control_3:
                        if _java_control_3.label not in (None,):
                            raise
                    except JBreak as _java_control_3:
                        if _java_control_3.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        return jcast('int', cnt)

    # 只是计数的话
    # 埃氏筛还能改进
    @staticmethod
    def ehrlich2(n):
        n = jcast('int', n)
        if (n <= 1):
            return jcast('int', 0)
        # visit[i] = true，代表i是合数
        # visit[i] = false，代表i是质数
        # 初始时认为0~n所有数都是质数
        visit = jarray('boolean', [jcast('int', jadd(n, 1))])
        # 先把所有的偶数去掉，但是算上2
        # 估计的质数数量，如果发现更多合数，那么cnt--
        cnt = jcast('int', jcast('int', jdiv(jcast('int', jadd(n, 1)), 2)))
        i = jcast('int', 3)
        while (jcast('int', (i * i)) <= n):
            if (not visit[i]):
                j = jcast('int', jcast('int', (i * i)))
                while (j <= n):
                    if (not visit[j]):
                        visit[j] = jcast('boolean', True)
                        cnt = jcast('int', (cnt - 1))
                    j = jcast('int', jcast('int', jadd(j, jcast('int', (2 * i)))))
            i = jcast('int', jcast('int', jadd(i, 2)))
        return jcast('int', cnt)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


