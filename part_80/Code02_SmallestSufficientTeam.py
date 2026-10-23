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

# 最小的必要团队
# 作为项目经理，你规划了一份需求的技能清单req_skills
# 并打算从备选人员名单people中选出些人组成必要团队
# 编号为i的备选人员people[i]含有一份该备选人员掌握的技能列表
# 所谓必要团队，就是在这个团队中
# 对于所需求的技能列表req_skills中列出的每项技能，团队中至少有一名成员已经掌握
# 请你返回规模最小的必要团队，团队成员用人员编号表示
# 你可以按 任意顺序 返回答案，题目数据保证答案存在
# 测试链接 : https://leetcode.cn/problems/smallest-sufficient-team/
class Code02_SmallestSufficientTeam:
    __java_fields__ = {}
    @staticmethod
    def smallestSufficientTeam(skills, people):
        n = jcast('int', jget(skills, 'length'))
        m = jcast('int', jcall(people, 'size'))
        map = jnew('HashMap')
        cnt = jcast('int', 0)
        for s in skills:
            # 把所有必要技能依次编号
            jcall(map, 'put', s, ((_java_old_1 := cnt), (cnt := jcast('int', (cnt + (1)))), _java_old_1)[2])
        # arr[i] : 第i号人掌握必要技能的状况，用位信息表示
        arr = jarray('int', [m])
        i = jcast('int', 0)
        status = 0
        while (i < m):
            status = jcast('int', 0)
            for skill in jcall(people, 'get', i):
                if jcall(map, 'containsKey', skill):
                    # 如果当前技能是必要的
                    # 才设置status
                    status = jcast('int', jcast('int', (status | jcast('int', (1 << (jcall(map, 'get', skill) & 31))))))
            arr[i] = jcast('int', status)
            i = jcast('int', (i + 1))
        dp = jarray('int', [m, jcast('int', (1 << (n & 31)))])
        i = jcast('int', 0)
        while (i < m):
            jstatic('Arrays', 'fill', dp[i], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        size = jcast('int', Code02_SmallestSufficientTeam.f(arr, m, n, 0, 0, dp))
        ans = jarray('int', [size])
        j = jcast('int', 0)
        i = jcast('int', 0)
        s = jcast('int', 0)
        while (s != jcast('int', (jcast('int', (1 << (n & 31))) - 1))):
            # s还没凑齐
            if ((i == jcast('int', (m - 1))) or (dp[i][s] != dp[jcast('int', jadd(i, 1))][s])):
                # 当初的决策是选择了i号人
                jset(ans, ((_java_old_2 := j), (j := jcast('int', (j + (1)))), _java_old_2)[2], i)
                s = jcast('int', jcast('int', (s | arr[i])))
            i = jcast('int', (i + 1))
        return ans

    # arr : 每个人所掌握的必要技能的状态
    # m : 人的总数
    # n : 必要技能的数量
    # i : 当前来到第几号人
    # s : 必要技能覆盖的状态
    # 返回 : i....这些人，把必要技能都凑齐，至少需要几个人
    @staticmethod
    def f(arr, m, n, i, s, dp):
        m = jcast('int', m)
        n = jcast('int', n)
        i = jcast('int', i)
        s = jcast('int', s)
        if (s == jcast('int', (jcast('int', (1 << (n & 31))) - 1))):
            # 所有技能已经凑齐了
            return jcast('int', 0)
        # 没凑齐
        if (i == m):
            # 人已经没了，技能也没凑齐
            # 无效
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (dp[i][s] != jcast('int', (-1))):
            return jcast('int', dp[i][s])
        # 可能性1 : 不要i号人
        p1 = jcast('int', Code02_SmallestSufficientTeam.f(arr, m, n, jcast('int', jadd(i, 1)), s, dp))
        # 可能性2 : 要i号人
        p2 = jcast('int', jget(Integer, 'MAX_VALUE'))
        next2 = jcast('int', Code02_SmallestSufficientTeam.f(arr, m, n, jcast('int', jadd(i, 1)), jcast('int', (s | arr[i])), dp))
        if (next2 != jget(Integer, 'MAX_VALUE')):
            # 后续有效
            p2 = jcast('int', jcast('int', jadd(1, next2)))
        ans = jcast('int', jstatic('Math', 'min', p1, p2))
        jset(dp[i], s, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


