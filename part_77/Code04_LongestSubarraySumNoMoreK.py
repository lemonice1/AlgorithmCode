# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 累加和不大于k的最长子数组
# 给定一个无序数组arr，长度为n，其中元素可能是正、负、0
# 给定一个整数k，求arr所有的子数组中累加和不大于k的最长子数组长度
# 要求时间复杂度为O(n)
# 测试链接 : https://www.nowcoder.com/practice/3473e545d6924077a4f7cbc850408ade
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 至今的最优解，全网题解几乎都是我几年前讲的方法
class Code04_LongestSubarraySumNoMoreK:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'minSums': 'minSums', 'minSumEnds': 'minSumEnds', 'n': 'n', 'k': 'k'}
    MAXN = 0
    nums = None
    minSums = None
    minSumEnds = None
    n = 0
    k = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_LongestSubarraySumNoMoreK.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code04_LongestSubarraySumNoMoreK.k = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code04_LongestSubarraySumNoMoreK.n):
                jcall(in_, 'nextToken')
                Code04_LongestSubarraySumNoMoreK.nums[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_LongestSubarraySumNoMoreK.compute2())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute1():
        sums = jarray('int', [jcast('int', jadd(Code04_LongestSubarraySumNoMoreK.n, 1))])
        i = jcast('int', 0)
        sum = jcast('int', 0)
        while (i < Code04_LongestSubarraySumNoMoreK.n):
            # sum : 0...i范围上，这前i+1个数字的累加和
            sum = jcast('int', jcast('int', jadd(sum, Code04_LongestSubarraySumNoMoreK.nums[i])))
            # sums[i + 1] : 前i+1个，包括一个数字也没有的时候，所有前缀和中的最大值
            jset(sums, jcast('int', jadd(i, 1)), jstatic('Math', 'max', sum, sums[i]))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        sum = jcast('int', 0)
        pre = 0
        len = 0
        while (i < Code04_LongestSubarraySumNoMoreK.n):
            sum = jcast('int', jcast('int', jadd(sum, Code04_LongestSubarraySumNoMoreK.nums[i])))
            pre = jcast('int', Code04_LongestSubarraySumNoMoreK.find(sums, jcast('int', (sum - Code04_LongestSubarraySumNoMoreK.k))))
            len = jcast('int', (0 if (pre == jcast('int', (-1))) else jcast('int', jadd(jcast('int', (i - pre)), 1))))
            ans = jcast('int', jstatic('Math', 'max', ans, len))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def find(sums, num):
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', Code04_LongestSubarraySumNoMoreK.n)
        m = jcast('int', 0)
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (sums[m] >= num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def compute2():
        Code04_LongestSubarraySumNoMoreK.minSums[jcast('int', (Code04_LongestSubarraySumNoMoreK.n - 1))] = jcast('int', Code04_LongestSubarraySumNoMoreK.nums[jcast('int', (Code04_LongestSubarraySumNoMoreK.n - 1))])
        Code04_LongestSubarraySumNoMoreK.minSumEnds[jcast('int', (Code04_LongestSubarraySumNoMoreK.n - 1))] = jcast('int', jcast('int', (Code04_LongestSubarraySumNoMoreK.n - 1)))
        i = jcast('int', jcast('int', (Code04_LongestSubarraySumNoMoreK.n - 2)))
        while (i >= 0):
            if (Code04_LongestSubarraySumNoMoreK.minSums[jcast('int', jadd(i, 1))] < 0):
                Code04_LongestSubarraySumNoMoreK.minSums[i] = jcast('int', jcast('int', jadd(Code04_LongestSubarraySumNoMoreK.nums[i], Code04_LongestSubarraySumNoMoreK.minSums[jcast('int', jadd(i, 1))])))
                Code04_LongestSubarraySumNoMoreK.minSumEnds[i] = jcast('int', Code04_LongestSubarraySumNoMoreK.minSumEnds[jcast('int', jadd(i, 1))])
            else:
                Code04_LongestSubarraySumNoMoreK.minSums[i] = jcast('int', Code04_LongestSubarraySumNoMoreK.nums[i])
                Code04_LongestSubarraySumNoMoreK.minSumEnds[i] = jcast('int', i)
            i = jcast('int', (i - 1))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        sum = jcast('int', 0)
        end = jcast('int', 0)
        while (i < Code04_LongestSubarraySumNoMoreK.n):
            while ((end < Code04_LongestSubarraySumNoMoreK.n) and (jcast('int', jadd(sum, Code04_LongestSubarraySumNoMoreK.minSums[end])) <= Code04_LongestSubarraySumNoMoreK.k)):
                sum = jcast('int', jcast('int', jadd(sum, Code04_LongestSubarraySumNoMoreK.minSums[end])))
                end = jcast('int', jcast('int', jadd(Code04_LongestSubarraySumNoMoreK.minSumEnds[end], 1)))
            if (end > i):
                # 如果end > i，
                # 窗口范围：i...end-1，那么窗口有效
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (end - i))))
                sum = jcast('int', jcast('int', (sum - Code04_LongestSubarraySumNoMoreK.nums[i])))
            else:
                # 如果end == i，那么说明窗口根本没扩出来，代表窗口无效
                # end来到i+1位置，然后i++了
                # 继续以新的i位置做开头去扩窗口
                end = jcast('int', jcast('int', jadd(i, 1)))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_LongestSubarraySumNoMoreK.MAXN = jcast('int', 100001)
Code04_LongestSubarraySumNoMoreK.nums = jarray('int', [Code04_LongestSubarraySumNoMoreK.MAXN])
Code04_LongestSubarraySumNoMoreK.minSums = jarray('int', [Code04_LongestSubarraySumNoMoreK.MAXN])
Code04_LongestSubarraySumNoMoreK.minSumEnds = jarray('int', [Code04_LongestSubarraySumNoMoreK.MAXN])
Code04_LongestSubarraySumNoMoreK.n = jcast('int', 0)
Code04_LongestSubarraySumNoMoreK.k = jcast('int', 0)

if __name__ == '__main__':
    Code04_LongestSubarraySumNoMoreK.main([])
