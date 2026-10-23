# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 删掉1个数字后长度为k的子数组最大累加和
# 给定一个数组nums，求必须删除一个数字后的新数组中
# 长度为k的子数组最大累加和，删除哪个数字随意
# 对数器验证
class Code06_DeleteOneNumberLengthKMaxSum:
    __java_fields__ = {}
    # 暴力方法
    # 为了测试
    @staticmethod
    def maxSum1(nums, k):
        k = jcast('int', k)
        n = jcast('int', jget(nums, 'length'))
        if (n <= k):
            return jcast('int', 0)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 0)
        while (i < n):
            rest = Code06_DeleteOneNumberLengthKMaxSum.delete(nums, i)
            ans = jcast('int', jstatic('Math', 'max', ans, Code06_DeleteOneNumberLengthKMaxSum.lenKmaxSum(rest, k)))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 暴力方法
    # 为了测试
    # 删掉index位置的元素，然后返回新数组
    @staticmethod
    def delete(nums, index):
        index = jcast('int', index)
        len = jcast('int', jcast('int', (jget(nums, 'length') - 1)))
        ans = jarray('int', [len])
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (j < jget(nums, 'length')):
            if (j != index):
                jset(ans, ((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2], nums[j])
            j = jcast('int', (j + 1))
        return ans

    # 暴力方法
    # 为了测试
    # 枚举每一个子数组找到最大累加和
    @staticmethod
    def lenKmaxSum(nums, k):
        k = jcast('int', k)
        n = jcast('int', jget(nums, 'length'))
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 0)
        while (i <= jcast('int', (n - k))):
            cur = jcast('int', 0)
            j = jcast('int', i)
            cnt = jcast('int', 0)
            while (cnt < k):
                cur = jcast('int', jcast('int', jadd(cur, nums[j])))
                j = jcast('int', (j + 1))
                cnt = jcast('int', (cnt + 1))
            ans = jcast('int', jstatic('Math', 'max', ans, cur))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 正式方法
    # 时间复杂度O(N)
    @staticmethod
    def maxSum2(nums, k):
        k = jcast('int', k)
        n = jcast('int', jget(nums, 'length'))
        if (n <= k):
            return jcast('int', 0)
        # 单调队列 : 维持窗口内最小值的更新结构，讲解054的内容
        window = jarray('int', [n])
        l = jcast('int', 0)
        r = jcast('int', 0)
        # 窗口累加和
        sum = jcast('long', 0)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 0)
        while (i < n):
            # 单调队列 : i位置进入单调队列
            while ((l < r) and (nums[window[jcast('int', (r - 1))]] >= nums[i])):
                r = jcast('int', (r - 1))
            jset(window, ((_java_old_2 := r), (r := jcast('int', (r + (1)))), _java_old_2)[2], i)
            sum = jcast('long', jcast('long', jadd(sum, nums[i])))
            if (i >= k):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jcast('long', (sum - nums[window[l]])))))
                if (window[l] == jcast('int', (i - k))):
                    # 单调队列 : 如果单调队列最左侧的位置过期了，从队列中弹出
                    l = jcast('int', (l + 1))
                sum = jcast('long', jcast('long', (sum - nums[jcast('int', (i - k))])))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 为了测试
    # 生成长度为n，值在[-v, +v]之间的随机数组
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', (jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (2 * v)), 1)))) - v)))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    # 对数器
    @staticmethod
    def main(args):
        n = jcast('int', 200)
        v = jcast('int', 1000)
        testTimes = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            len = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            nums = Code06_DeleteOneNumberLengthKMaxSum.randomArray(len, v)
            k = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            ans1 = jcast('int', Code06_DeleteOneNumberLengthKMaxSum.maxSum1(nums, k))
            ans2 = jcast('int', Code06_DeleteOneNumberLengthKMaxSum.maxSum2(nums, k))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code06_DeleteOneNumberLengthKMaxSum.main([])
