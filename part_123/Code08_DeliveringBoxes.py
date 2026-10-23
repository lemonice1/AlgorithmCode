# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 送箱子到码头的最少行程数
# 一共有m个码头，编号1 ~ m， 给定长度为n的二维数组boxes
# boxes[i][0]表示i号箱子要送往的码头，boxes[i][1]表示i号箱子重量
# 有一辆马车，一次最多能装a个箱子并且箱子总重量不能超过b
# 马车一开始在仓库，可以在0位置，马车每开动一次，认为行程+1
# 箱子必须按照boxes规定的顺序被放上马车，也必须按照顺序被送往各自的码头
# 马车上相邻的箱子如果去往同一个码头，那么认为共享同一趟行程
# 马车可能经过多次送货，每次装货需要回到仓库，认为行程+1，送完所有的货，最终要回到仓库，行程+1
# 返回至少需要几个行程能把所有的货都送完
# 所有数据的范围 <= 10^5
# 测试链接 : https://leetcode.cn/problems/delivering-boxes-from-storage-to-ports/
class Code08_DeliveringBoxes:
    __java_fields__ = {}
    # 贪心分析 + 窗口优化，只用有限几个变量维护窗口信息，无需单调队列/单调栈
    @staticmethod
    def boxDelivering(boxes, m, a, b):
        m = jcast('int', m)
        a = jcast('int', a)
        b = jcast('int', b)
        n = jcast('int', jget(boxes, 'length'))
        # dp[i] : 马车拉完前i个货物并回仓库，需要的最少行程
        # 注意这里的i是指个数，对应的货物是boxes[0...i-1]
        dp = jarray('int', [jcast('int', jadd(n, 1))])
        dp[1] = jcast('int', 2)
        # 马车最后一趟的货物范围[l...r]
        # 最后一趟货物的总重量weight，最后一趟需要的行程trip
        weight = jcast('int', boxes[0][1])
        trip = jcast('int', 2)
        l = jcast('int', 0)
        r = jcast('int', 1)
        while (r < n):
            weight = jcast('int', jcast('int', jadd(weight, boxes[r][1])))
            if (boxes[r][0] != boxes[jcast('int', (r - 1))][0]):
                trip = jcast('int', (trip + 1))
            # 1) 最后一趟货物的个数超了，最后一趟不得不减少货物
            # 2) 最后一趟货物的总重量超了，最后一趟不得不减少货物
            # 3) 最后一趟最左侧的货，分给之前的过程，如果发现之前过程的dp值没变化，那就分出去
            # 最后一趟最左侧的货，分给之前的过程，如果发现之前过程的dp值增加了，一定不要分出去
            # 对于这个逻辑，课上进行了重点图解
            while (((jcast('int', jadd(jcast('int', (r - l)), 1)) > a) or (weight > b)) or (dp[l] == dp[jcast('int', jadd(l, 1))])):
                weight = jcast('int', jcast('int', (weight - boxes[((_java_old_1 := l), (l := jcast('int', (l + (1)))), _java_old_1)[2]][1])))
                if (boxes[l][0] != boxes[jcast('int', (l - 1))][0]):
                    trip = jcast('int', (trip - 1))
            dp[jcast('int', jadd(r, 1))] = jcast('int', jcast('int', jadd(dp[l], trip)))
            r = jcast('int', (r + 1))
        return jcast('int', dp[n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


