# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 子数组最大变序和
# 给定一个长度为n的数组arr，变序和定义如下
# 数组中每个值都可以减小或者不变，必须把整体变成严格升序的
# 所有方案中，能得到的最大累加和，叫做数组的变序和
# 比如[1,100,7]，变序和14，方案为变成[1,6,7]
# 比如[5,4,9]，变序和16，方案为变成[3,4,9]
# 比如[1,4,2]，变序和3，方案为变成[0,1,2]
# 返回arr所有子数组的变序和中，最大的那个
# 1 <= n、arr[i] <= 10^6
# 来自真实大厂笔试，对数器验证
class Code07_MaximumOrderSum:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    # 时间复杂度O(n * v)
    @staticmethod
    def maxSum1(arr):
        n = jcast('int', jget(arr, 'length'))
        max = jcast('int', 0)
        for num in arr:
            max = jcast('int', jstatic('Math', 'max', max, num))
        ans = jcast('long', 0)
        dp = jarray('long', [n, jcast('int', jadd(max, 1))])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j <= max):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < n):
            ans = jcast('long', jstatic('Math', 'max', ans, Code07_MaximumOrderSum.f1(arr, i, arr[i], dp)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    # 暴力方法
    # 为了验证
    # 子数组一定要以i位置结尾，并且i位置变成的数字不能大于p的情况下
    # 返回子数组的最大变序和
    @staticmethod
    def f1(arr, i, p, dp):
        i = jcast('int', i)
        p = jcast('int', p)
        if ((p <= 0) or (i == jcast('int', (-1)))):
            return jcast('long', 0)
        if (dp[i][p] != jcast('int', (-1))):
            return jcast('long', dp[i][p])
        cur = jcast('int', jstatic('Math', 'min', arr[i], p))
        next = jcast('long', Code07_MaximumOrderSum.f1(arr, jcast('int', (i - 1)), jcast('int', (cur - 1)), dp))
        ans = jcast('long', jcast('long', jadd(jcast('long', cur), next)))
        jset(dp[i], p, ans)
        return jcast('long', jcast('long', jadd(cur, next)))

    # 正式方法
    # 时间复杂度O(n)
    @staticmethod
    def maxSum2(arr):
        n = jcast('int', jget(arr, 'length'))
        stack = jarray('int', [n])
        size = jcast('int', 0)
        dp = jarray('long', [n])
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while (i < n):
            try:
                curIdx = jcast('int', i)
                curVal = jcast('int', arr[curIdx])
                while ((curVal > 0) and (size > 0)):
                    try:
                        topIdx = jcast('int', stack[jcast('int', (size - 1))])
                        topVal = jcast('int', arr[topIdx])
                        if (topVal >= curVal):
                            size = jcast('int', (size - 1))
                        else:
                            idxDiff = jcast('int', jcast('int', (curIdx - topIdx)))
                            valDiff = jcast('int', jcast('int', (curVal - topVal)))
                            if (valDiff >= idxDiff):
                                ((_java_obj_3 := dp), (_java_key_4 := i), jset(_java_obj_3, _java_key_4, jcast('long', jadd(jget(_java_obj_3, _java_key_4), jcast('long', jadd(Code07_MaximumOrderSum.sum(curVal, idxDiff), dp[topIdx]))))))[2]
                                curVal = jcast('int', 0)
                                curIdx = jcast('int', 0)
                                raise JBreak(None)
                            else:
                                ((_java_obj_5 := dp), (_java_key_6 := i), jset(_java_obj_5, _java_key_6, jcast('long', jadd(jget(_java_obj_5, _java_key_6), Code07_MaximumOrderSum.sum(curVal, idxDiff)))))[2]
                                curVal = jcast('int', jcast('int', (curVal - idxDiff)))
                                curIdx = jcast('int', topIdx)
                                size = jcast('int', (size - 1))
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                if (curVal > 0):
                    ((_java_obj_7 := dp), (_java_key_8 := i), jset(_java_obj_7, _java_key_8, jcast('long', jadd(jget(_java_obj_7, _java_key_8), Code07_MaximumOrderSum.sum(curVal, jcast('int', jadd(curIdx, 1)))))))[2]
                jset(stack, ((_java_old_9 := size), (size := jcast('int', (size + (1)))), _java_old_9)[2], i)
                ans = jcast('long', jstatic('Math', 'max', ans, dp[i]))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    # 最大值从max开始，往下一共有n项，只要正数的部分，返回累加和
    @staticmethod
    def sum(max, n):
        max = jcast('int', max)
        n = jcast('int', n)
        n = jcast('int', jstatic('Math', 'min', max, n))
        return jcast('long', jcast('long', jdiv(jcast('long', (jcast('long', jadd(jcast('long', (jcast('long', (jcast('long', max) * 2)) - n)), 1)) * n)), 2)))

    # 为了验证
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', (jstatic('Math', 'random') * v)))
            i = jcast('int', (i + 1))
        return ans

    # 为了验证
    @staticmethod
    def main(args):
        n = jcast('int', 100)
        v = jcast('int', 100)
        testTimes = jcast('int', 50000)
        jprint('功能测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            size = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            arr = Code07_MaximumOrderSum.randomArray(size, v)
            ans1 = jcast('long', Code07_MaximumOrderSum.maxSum1(arr))
            ans2 = jcast('long', Code07_MaximumOrderSum.maxSum2(arr))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('功能测试结束', newline=True)
        jprint('性能测试开始', newline=True)
        n = jcast('int', 1000000)
        v = jcast('int', 1000000)
        jprint(jadd('数组长度 : ', n), newline=True)
        jprint(jadd('数值范围 : ', v), newline=True)
        arr = Code07_MaximumOrderSum.randomArray(n, v)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        Code07_MaximumOrderSum.maxSum2(arr)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        jprint('性能测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code07_MaximumOrderSum.main([])
