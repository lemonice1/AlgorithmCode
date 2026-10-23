# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 数组中两个数的最大异或值
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0<=i<=j<=n
# 1 <= nums.length <= 2 * 10^5
# 0 <= nums[i] <= 2^31 - 1
# 测试链接 : https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/
class Code02_TwoNumbersMaximumXor:
    __java_fields__ = {'MAXN': 'MAXN', 'tree': 'tree', 'cnt': 'cnt', 'high': 'high'}
    # 前缀树的做法
    # 好想
    @staticmethod
    def findMaximumXOR1(nums):
        Code02_TwoNumbersMaximumXor.build(nums)
        ans = jcast('int', 0)
        for num in nums:
            ans = jcast('int', jstatic('Math', 'max', ans, Code02_TwoNumbersMaximumXor.maxXor(num)))
        Code02_TwoNumbersMaximumXor.clear()
        return jcast('int', ans)

    # 准备这么多静态空间就够了，实验出来的
    # 如果测试数据升级了规模，就改大这个值
    MAXN = 0
    tree = None
    # 前缀树目前使用了多少空间
    cnt = 0
    # 数字只需要从哪一位开始考虑
    high = 0
    @staticmethod
    def build(nums):
        Code02_TwoNumbersMaximumXor.cnt = jcast('int', 1)
        # 找个最大值
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        for num in nums:
            max = jcast('int', jstatic('Math', 'max', num, max))
        # 计算数组最大值的二进制状态，有多少个前缀的0
        # 可以忽略这些前置的0，从left位开始考虑
        Code02_TwoNumbersMaximumXor.high = jcast('int', jcast('int', (31 - jstatic('Integer', 'numberOfLeadingZeros', max))))
        for num in nums:
            Code02_TwoNumbersMaximumXor.insert(num)

    @staticmethod
    def insert(num):
        num = jcast('int', num)
        cur = jcast('int', 1)
        i = jcast('int', Code02_TwoNumbersMaximumXor.high)
        path = 0
        while (i >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (i & 31))) & 1)))
            if (Code02_TwoNumbersMaximumXor.tree[cur][path] == 0):
                jset(Code02_TwoNumbersMaximumXor.tree[cur], path, ((_java_obj_1 := Code02_TwoNumbersMaximumXor), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            cur = jcast('int', Code02_TwoNumbersMaximumXor.tree[cur][path])
            i = jcast('int', (i - 1))

    @staticmethod
    def maxXor(num):
        num = jcast('int', num)
        # 最终异或的结果(尽量大)
        ans = jcast('int', 0)
        # 前缀树目前来到的节点编号
        cur = jcast('int', 1)
        i = jcast('int', Code02_TwoNumbersMaximumXor.high)
        status = 0
        want = 0
        while (i >= 0):
            # status : num第i位的状态
            status = jcast('int', jcast('int', (jcast('int', (num >> (i & 31))) & 1)))
            # want : num第i位希望遇到的状态
            want = jcast('int', jcast('int', (status ^ 1)))
            # 询问前缀树，能不能达成
            if (Code02_TwoNumbersMaximumXor.tree[cur][want] == 0):
                # 不能达成
                want = jcast('int', jcast('int', (want ^ 1)))
            # want变成真的往下走的路
            ans = jcast('int', jcast('int', (ans | jcast('int', (jcast('int', (status ^ want)) << (i & 31))))))
            cur = jcast('int', Code02_TwoNumbersMaximumXor.tree[cur][want])
            i = jcast('int', (i - 1))
        return jcast('int', ans)

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code02_TwoNumbersMaximumXor.cnt):
            jset(Code02_TwoNumbersMaximumXor.tree[i], 0, jset(Code02_TwoNumbersMaximumXor.tree[i], 1, 0))
            i = jcast('int', (i + 1))

    # 用哈希表的做法
    # 难想
    def findMaximumXOR2(self, nums):
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        for num in nums:
            max = jcast('int', jstatic('Math', 'max', num, max))
        ans = jcast('int', 0)
        set = jnew('HashSet')
        i = jcast('int', jcast('int', (31 - jstatic('Integer', 'numberOfLeadingZeros', max))))
        while (i >= 0):
            try:
                # ans : 31....i+1 已经达成的目标
                better = jcast('int', jcast('int', (ans | jcast('int', (1 << (i & 31))))))
                jcall(set, 'clear')
                for num in nums:
                    try:
                        # num : 31.....i 这些状态保留，剩下全成0
                        num = jcast('int', jcast('int', (jcast('int', (num >> (i & 31))) << (i & 31))))
                        jcall(set, 'add', num)
                        # num ^ 某状态 是否能 达成better目标，就在set中找 某状态 : better ^ num
                        if jcall(set, 'contains', jcast('int', (better ^ num))):
                            ans = jcast('int', better)
                            raise JBreak(None)
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
            i = jcast('int', (i - 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_TwoNumbersMaximumXor.MAXN = jcast('int', 3000001)
Code02_TwoNumbersMaximumXor.tree = jarray('int', [Code02_TwoNumbersMaximumXor.MAXN, 2])
Code02_TwoNumbersMaximumXor.cnt = jcast('int', 0)
Code02_TwoNumbersMaximumXor.high = jcast('int', 0)
