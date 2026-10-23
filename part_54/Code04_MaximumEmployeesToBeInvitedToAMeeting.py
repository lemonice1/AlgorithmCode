# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 参加会议的最多员工数
# 一个公司准备组织一场会议，邀请名单上有 n 位员工
# 公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工
# 员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工
# 每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议
# 每位员工喜欢的员工 不会 是他自己。给你一个下标从 0 开始的整数数组 favorite
# 其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目
# 测试链接 : https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/
class Code04_MaximumEmployeesToBeInvitedToAMeeting:
    __java_fields__ = {}
    @staticmethod
    def maximumInvitations(favorite):
        # 图 : favorite[a] = b : a -> b
        n = jcast('int', jget(favorite, 'length'))
        indegree = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            ((_java_obj_1 := indegree), (_java_key_2 := favorite[i]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
            i = jcast('int', (i + 1))
        queue = jarray('int', [n])
        l = jcast('int', 0)
        r = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            if (indegree[i] == 0):
                jset(queue, ((_java_old_4 := r), (r := jcast('int', (r + (1)))), _java_old_4)[2], i)
            i = jcast('int', (i + 1))
        # deep[i] : 不包括i在内，i之前的最长链的长度
        deep = jarray('int', [n])
        while (l < r):
            cur = jcast('int', queue[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]])
            next = jcast('int', favorite[cur])
            jset(deep, next, jstatic('Math', 'max', deep[next], jcast('int', jadd(deep[cur], 1))))
            if (((_java_obj_6 := indegree), (_java_key_7 := next), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (-1)))))[3] == 0):
                jset(queue, ((_java_old_9 := r), (r := jcast('int', (r + (1)))), _java_old_9)[2], next)
        # 目前图中的点，不在环上的点，都删除了！ indegree[i] == 0
        # 可能性1 : 所有小环(中心个数 == 2)，算上中心点 + 延伸点，总个数
        sumOfSmallRings = jcast('int', 0)
        # 可能性2 : 所有大环(中心个数 > 2)，只算中心点，最大环的中心点个数
        bigRings = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            # 只关心的环！
            if (indegree[i] > 0):
                ringSize = jcast('int', 1)
                indegree[i] = jcast('int', 0)
                j = jcast('int', favorite[i])
                while (j != i):
                    ringSize = jcast('int', (ringSize + 1))
                    indegree[j] = jcast('int', 0)
                    j = jcast('int', favorite[j])
                if (ringSize == 2):
                    sumOfSmallRings = jcast('int', jcast('int', jadd(sumOfSmallRings, jcast('int', jadd(jcast('int', jadd(2, deep[i])), deep[favorite[i]])))))
                else:
                    bigRings = jcast('int', jstatic('Math', 'max', bigRings, ringSize))
            i = jcast('int', (i + 1))
        return jcast('int', jstatic('Math', 'max', sumOfSmallRings, bigRings))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


