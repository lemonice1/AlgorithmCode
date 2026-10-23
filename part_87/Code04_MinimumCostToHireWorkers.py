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

# 雇佣K名工人的最低成本
# 有n名工人，给定两个数组quality和wage
# 其中quality[i]表示第i名工人的工作质量，其最低期望工资为wage[i]
# 现在我们想雇佣k名工人组成一个工资组
# 在雇佣一组k名工人时，我们必须按照下述规则向他们支付工资：
# 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资
# 工资组中的每名工人至少应当得到他们的最低期望工资
# 给定整数k，返回组成满足上述条件的付费群体所需的最小金额
# 测试链接 : https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/
class Code04_MinimumCostToHireWorkers:
    __java_fields__ = {}
    class Employee:
        __java_fields__ = {'ratio': 'ratio', 'quality': 'quality'}
        # 薪水 / 质量的比例
        # ratio：实例字段，在构造函数中初始化。
        # quality：实例字段，在构造函数中初始化。
        def _java_init_0(self, r, q):
            r = jcast('double', r)
            q = jcast('int', q)
            self.ratio = jcast('double', r)
            self.quality = jcast('int', q)

        def __init__(self, *args, _java_ctor=None):
            self.ratio = jcast('double', 0.0)
            self.quality = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['double', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_MinimumCostToHireWorkers.Employee.Employee")


    @staticmethod
    def mincostToHireWorkers(quality, wage, k):
        k = jcast('int', k)
        n = jcast('int', jget(quality, 'length'))
        employees = jarray('Employee', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(employees, i, Code04_MinimumCostToHireWorkers.Employee(jdiv(jcast('double', wage[i]), quality[i]), quality[i], _java_ctor=0))
            i = jcast('int', (i + 1))
        # 根据比例排序，比例小的在前，比例大的在后
        jstatic('Arrays', 'sort', employees, (lambda a, b: (jcast('int', (-1)) if (jget(a, 'ratio') <= jget(b, 'ratio')) else 1)))
        # 大根堆，用来收集最小的前k个质量数值
        heap = jnew('PriorityQueue', (lambda a, b: (b - a)))
        # 堆里，最小的前k个质量数值，总和是多少
        qualitySum = jcast('int', 0)
        ans = jcast('double', jget(Double, 'MAX_VALUE'))
        i = jcast('int', 0)
        curQuality = 0
        while (i < n):
            curQuality = jcast('int', jget(employees[i], 'quality'))
            # 堆没满
            if (jcall(heap, 'size') < k):
                qualitySum = jcast('int', jcast('int', jadd(qualitySum, curQuality)))
                jcall(heap, 'add', curQuality)
                if (jcall(heap, 'size') == k):
                    ans = jcast('double', jstatic('Math', 'min', ans, (qualitySum * jget(employees[i], 'ratio'))))
                # 堆满了
            else:
                if (jcall(heap, 'peek') > curQuality):
                    qualitySum = jcast('int', jadd(qualitySum, (curQuality - jcall(heap, 'poll'))))
                    jcall(heap, 'add', curQuality)
                    ans = jcast('double', jstatic('Math', 'min', ans, (qualitySum * jget(employees[i], 'ratio'))))
            i = jcast('int', (i + 1))
        return jcast('double', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


