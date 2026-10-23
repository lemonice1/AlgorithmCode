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

# 电动车游城市
# 小明的电动车电量充满时可行驶距离为 cnt，每行驶 1 单位距离消耗 1 单位电量，且花费 1 单位时间
# 小明想选择电动车作为代步工具。地图上共有 N 个景点，景点编号为 0 ~ N-1
# 他将地图信息以 [城市 A 编号,城市 B 编号,两城市间距离] 格式整理在在二维数组 paths，
# 表示城市 A、B 间存在双向通路。
# 初始状态，电动车电量为 0。每个城市都设有充电桩，
# charge[i] 表示第 i 个城市每充 1 单位电量需要花费的单位时间。
# 请返回小明最少需要花费多少单位时间从起点城市 start 抵达终点城市 end
# 测试链接 : https://leetcode.cn/problems/DFPeFJ/
class Code05_VisitCityMinCost:
    __java_fields__ = {}
    # 电动车总电量，cnt
    @staticmethod
    def electricCarPlan(paths, cnt, start, end, charge):
        cnt = jcast('int', cnt)
        start = jcast('int', start)
        end = jcast('int', end)
        n = jcast('int', jget(charge, 'length'))
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < n):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        for path in paths:
            jcall(jcall(graph, 'get', path[0]), 'add', jarray('int', [None], [path[1], path[2]]))
            jcall(jcall(graph, 'get', path[1]), 'add', jarray('int', [None], [path[0], path[2]]))
        # n : 0 ~ n-1，不代表图上的点
        # (点，到达这个点的电量)图上的点！
        distance = jarray('int', [n, jcast('int', jadd(cnt, 1))])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j <= cnt):
                jset(distance[i], j, jget(Integer, 'MAX_VALUE'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        jset(distance[start], 0, 0)
        visited = jarray('boolean', [n, jcast('int', jadd(cnt, 1))])
        # 0 : 当前点
        # 1 : 来到当前点的电量
        # 2 : 花费时间
        heap = jnew('PriorityQueue', (lambda a, b: (a[2] - b[2])))
        jcall(heap, 'add', jarray('int', [None], [start, 0, 0]))
        while (not jcall(heap, 'isEmpty')):
            try:
                record = jcall(heap, 'poll')
                cur = jcast('int', record[0])
                power = jcast('int', record[1])
                cost = jcast('int', record[2])
                if visited[cur][power]:
                    raise JContinue(None)
                if (cur == end):
                    # 常见剪枝
                    # 发现终点直接返回
                    # 不用等都结束
                    return jcast('int', cost)
                jset(visited[cur], power, True)
                if (power < cnt):
                    # 充一格电
                    # cur, power+1
                    if ((not visited[cur][jcast('int', jadd(power, 1))]) and (jcast('int', jadd(cost, charge[cur])) < distance[cur][jcast('int', jadd(power, 1))])):
                        jset(distance[cur], jcast('int', jadd(power, 1)), jcast('int', jadd(cost, charge[cur])))
                        jcall(heap, 'add', jarray('int', [None], [cur, jcast('int', jadd(power, 1)), jcast('int', jadd(cost, charge[cur]))]))
                for edge in jcall(graph, 'get', cur):
                    # 不充电去别的城市
                    nextCity = jcast('int', edge[0])
                    restPower = jcast('int', jcast('int', (power - edge[1])))
                    nextCost = jcast('int', jcast('int', jadd(cost, edge[1])))
                    if (((restPower >= 0) and (not visited[nextCity][restPower])) and (nextCost < distance[nextCity][restPower])):
                        jset(distance[nextCity], restPower, nextCost)
                        jcall(heap, 'add', jarray('int', [None], [nextCity, restPower, nextCost]))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


