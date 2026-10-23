# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 两个0和1数量相等区间的最大长度
# 给出一个长度为n的01串，现在请你找到两个区间
# 使得这两个区间中，1的个数相等，0的个数也相等
# 这两个区间可以相交，但是不可以完全重叠，即两个区间的左右端点不可以完全一样
# 现在请你找到两个最长的区间，满足以上要求
# 返回区间最大长度
# 来自真实大厂笔试，没有在线测试，对数器验证
class Code06_LongestSameZerosOnes:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    @staticmethod
    def len1(arr):
        map = jnew('HashMap')
        i = jcast('int', 0)
        while (i < jget(arr, 'length')):
            zero = jcast('int', 0)
            one = jcast('int', 0)
            j = jcast('int', i)
            while (j < jget(arr, 'length')):
                zero = jcast('int', jcast('int', jadd(zero, (1 if (arr[j] == 0) else 0))))
                one = jcast('int', jcast('int', jadd(one, (1 if (arr[j] == 1) else 0))))
                jcall(map, 'putIfAbsent', zero, jnew('HashMap'))
                jcall(jcall(map, 'get', zero), 'put', one, jadd(jcall(jcall(map, 'get', zero), 'getOrDefault', one, 0), 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        for zeros in jcall(map, 'keySet'):
            for ones in jcall(jcall(map, 'get', zeros), 'keySet'):
                num = jcast('int', jcall(jcall(map, 'get', zeros), 'get', ones))
                if (num > 1):
                    ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(zeros, ones))))
        return jcast('int', ans)

    # 正式方法
    # 时间复杂度O(n)
    @staticmethod
    def len2(arr):
        leftZero = jcast('int', jcast('int', (-1)))
        rightZero = jcast('int', jcast('int', (-1)))
        leftOne = jcast('int', jcast('int', (-1)))
        rightOne = jcast('int', jcast('int', (-1)))
        i = jcast('int', 0)
        while (i < jget(arr, 'length')):
            try:
                if (arr[i] == 0):
                    leftZero = jcast('int', i)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < jget(arr, 'length')):
            try:
                if (arr[i] == 1):
                    leftOne = jcast('int', i)
                    raise JBreak(None)
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', (jget(arr, 'length') - 1)))
        while (i >= 0):
            try:
                if (arr[i] == 0):
                    rightZero = jcast('int', i)
                    raise JBreak(None)
            except JContinue as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
            except JBreak as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
                break
            i = jcast('int', (i - 1))
        i = jcast('int', jcast('int', (jget(arr, 'length') - 1)))
        while (i >= 0):
            try:
                if (arr[i] == 1):
                    rightOne = jcast('int', i)
                    raise JBreak(None)
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
            i = jcast('int', (i - 1))
        p1 = jcast('int', jcast('int', (rightZero - leftZero)))
        p2 = jcast('int', jcast('int', (rightOne - leftOne)))
        return jcast('int', jstatic('Math', 'max', p1, p2))

    # 为了验证
    @staticmethod
    def randomArray(len):
        len = jcast('int', len)
        ans = jarray('int', [len])
        i = jcast('int', 0)
        while (i < len):
            jset(ans, i, jcast('int', (jstatic('Math', 'random') * 2)))
            i = jcast('int', (i + 1))
        return ans

    # 为了验证
    @staticmethod
    def main(args):
        N = jcast('int', 500)
        testTimes = jcast('int', 2000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 2)))
            arr = Code06_LongestSameZerosOnes.randomArray(n)
            ans1 = jcast('int', Code06_LongestSameZerosOnes.len1(arr))
            ans2 = jcast('int', Code06_LongestSameZerosOnes.len2(arr))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            if (jcast('int', jmod(i, 100)) == 0):
                jprint(jadd(jadd('测试到第', i), '组'), newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code06_LongestSameZerosOnes.main([])
