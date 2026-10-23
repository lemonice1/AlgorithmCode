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

# 在传球游戏中最大化函数值
# 给定一个长度为n的数组receiver和一个整数k
# 总共有n名玩家，编号0 ~ n-1，这些玩家在玩一个传球游戏
# receiver[i]表示编号为i的玩家会传球给下一个人的编号
# 玩家可以传球给自己，也就是说receiver[i]可能等于i
# 你需要选择一名开始玩家，然后开始传球，球会被传恰好k次
# 如果选择编号为x的玩家作为开始玩家
# 函数f(x)表示从x玩家开始，k次传球内所有接触过球的玩家编号之和
# 如果某位玩家多次触球，则累加多次
# f(x) = x + receiver[x] + receiver[receiver[x]] + ...
# 你的任务时选择开始玩家x，目的是最大化f(x)，返回函数的最大值
# 测试链接 : https://leetcode.cn/problems/maximize-value-of-function-in-a-ball-passing-game/
class Code04_PassingBallMaximizeValue:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'm': 'm', 'kbits': 'kbits', 'stjump': 'stjump', 'stsum': 'stsum'}
    MAXN = 0
    LIMIT = 0
    power = 0
    # 给定k的二进制位上有几个1
    m = 0
    # 收集k的二进制上哪些位有1
    kbits = None
    stjump = None
    stsum = None
    @staticmethod
    def build(k):
        k = jcast('long', k)
        Code04_PassingBallMaximizeValue.power = jcast('int', 0)
        while (jcast('long', (1 << (Code04_PassingBallMaximizeValue.power & 63))) <= jcast('long', (k >> (1 & 63)))):
            Code04_PassingBallMaximizeValue.power = jcast('int', (Code04_PassingBallMaximizeValue.power + 1))
        Code04_PassingBallMaximizeValue.m = jcast('int', 0)
        p = jcast('int', Code04_PassingBallMaximizeValue.power)
        while (p >= 0):
            if (jcast('long', (1 << (p & 63))) <= k):
                jset(Code04_PassingBallMaximizeValue.kbits, ((_java_obj_1 := Code04_PassingBallMaximizeValue), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], p)
                k = jcast('long', jcast('long', (k - jcast('long', (1 << (p & 63))))))
            p = jcast('int', (p - 1))

    # 该方法是树上倍增的解法
    # 打败比例很一般但是非常好想
    # 这个题最优解来自对基环树的分析
    # 后面的课会安排基环树的内容
    @staticmethod
    def getMaxFunctionValue(receiver, k):
        k = jcast('long', k)
        Code04_PassingBallMaximizeValue.build(k)
        n = jcast('int', jcall(receiver, 'size'))
        i = jcast('int', 0)
        while (i < n):
            jset(Code04_PassingBallMaximizeValue.stjump[i], 0, jcall(receiver, 'get', i))
            jset(Code04_PassingBallMaximizeValue.stsum[i], 0, jcall(receiver, 'get', i))
            i = jcast('int', (i + 1))
        p = jcast('int', 1)
        while (p <= Code04_PassingBallMaximizeValue.power):
            i = jcast('int', 0)
            while (i < n):
                jset(Code04_PassingBallMaximizeValue.stjump[i], p, Code04_PassingBallMaximizeValue.stjump[Code04_PassingBallMaximizeValue.stjump[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                jset(Code04_PassingBallMaximizeValue.stsum[i], p, jcast('long', jadd(Code04_PassingBallMaximizeValue.stsum[i][jcast('int', (p - 1))], Code04_PassingBallMaximizeValue.stsum[Code04_PassingBallMaximizeValue.stjump[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])))
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))
        sum = 0
        ans = jcast('long', 0)
        i = jcast('int', 0)
        cur = 0
        while (i < n):
            cur = jcast('int', i)
            sum = jcast('long', i)
            j = jcast('int', 0)
            while (j < Code04_PassingBallMaximizeValue.m):
                sum = jcast('long', jcast('long', jadd(sum, Code04_PassingBallMaximizeValue.stsum[cur][Code04_PassingBallMaximizeValue.kbits[j]])))
                cur = jcast('int', Code04_PassingBallMaximizeValue.stjump[cur][Code04_PassingBallMaximizeValue.kbits[j]])
                j = jcast('int', (j + 1))
            ans = jcast('long', jstatic('Math', 'max', ans, sum))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PassingBallMaximizeValue.MAXN = jcast('int', 100001)
Code04_PassingBallMaximizeValue.LIMIT = jcast('int', 34)
Code04_PassingBallMaximizeValue.power = jcast('int', 0)
Code04_PassingBallMaximizeValue.m = jcast('int', 0)
Code04_PassingBallMaximizeValue.kbits = jarray('int', [Code04_PassingBallMaximizeValue.LIMIT])
Code04_PassingBallMaximizeValue.stjump = jarray('int', [Code04_PassingBallMaximizeValue.MAXN, Code04_PassingBallMaximizeValue.LIMIT])
Code04_PassingBallMaximizeValue.stsum = jarray('long', [Code04_PassingBallMaximizeValue.MAXN, Code04_PassingBallMaximizeValue.LIMIT])
