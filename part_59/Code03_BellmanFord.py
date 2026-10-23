# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Bellman-Ford算法应用（不是模版）
# k站中转内最便宜的航班
# 有 n 个城市通过一些航班连接。给你一个数组 flights
# 其中 flights[i] = [fromi, toi, pricei]
# 表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线
# 使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。
# 测试链接 : https://leetcode.cn/problems/cheapest-flights-within-k-stops/
class Code03_BellmanFord:
    __java_fields__ = {}
    # Bellman-Ford算法
    # 针对此题改写了松弛逻辑，课上讲了细节
    @staticmethod
    def findCheapestPrice(n, flights, start, target, k):
        n = jcast('int', n)
        start = jcast('int', start)
        target = jcast('int', target)
        k = jcast('int', k)
        cur = jarray('int', [n])
        jstatic('Arrays', 'fill', cur, jget(Integer, 'MAX_VALUE'))
        cur[start] = jcast('int', 0)
        i = jcast('int', 0)
        while (i <= k):
            next = jstatic('Arrays', 'copyOf', cur, n)
            for edge in flights:
                # a -> b , w
                if (cur[edge[0]] != jget(Integer, 'MAX_VALUE')):
                    jset(next, edge[1], jstatic('Math', 'min', next[edge[1]], jcast('int', jadd(cur[edge[0]], edge[2]))))
            cur = next
            i = jcast('int', (i + 1))
        return jcast('int', (jcast('int', (-1)) if (cur[target] == jget(Integer, 'MAX_VALUE')) else cur[target]))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


