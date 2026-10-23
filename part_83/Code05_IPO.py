# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# IPO
# 给你n个项目，对于每个项目i
# 它都有一个纯利润profits[i]
# 和启动该项目需要的最小资本capital[i]
# 最初你的资本为w，当你完成一个项目时，你将获得纯利润，添加到你的总资本中
# 总而言之，从给定项目中选择最多k个不同项目的列表
# 以最大化最终资本，并输出最终可获得的最多资本
# 测试链接 : https://leetcode.cn/problems/ipo/
class Code05_IPO:
    __java_fields__ = {}
    class Project:
        __java_fields__ = {'p': 'p', 'c': 'c'}
        # 纯利润
        # p：实例字段，在构造函数中初始化。
        # 需要的启动金
        # c：实例字段，在构造函数中初始化。
        def _java_init_0(self, profit, cost):
            profit = jcast('int', profit)
            cost = jcast('int', cost)
            self.p = jcast('int', profit)
            self.c = jcast('int', cost)

        def __init__(self, *args, _java_ctor=None):
            self.p = jcast('int', 0)
            self.c = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_IPO.Project.Project")


    @staticmethod
    def findMaximizedCapital(k, w, profit, cost):
        k = jcast('int', k)
        w = jcast('int', w)
        n = jcast('int', jget(profit, 'length'))
        # 需要的启动金小根堆
        # 代表被锁住的项目
        heap1 = jnew('PriorityQueue', (lambda a, b: (jget(a, 'c') - jget(b, 'c'))))
        # 利润大根堆
        # 代表被解锁的项目
        heap2 = jnew('PriorityQueue', (lambda a, b: (jget(b, 'p') - jget(a, 'p'))))
        i = jcast('int', 0)
        while (i < n):
            jcall(heap1, 'add', Code05_IPO.Project(profit[i], cost[i], _java_ctor=0))
            i = jcast('int', (i + 1))
        while (k > 0):
            try:
                while ((not jcall(heap1, 'isEmpty')) and (jget(jcall(heap1, 'peek'), 'c') <= w)):
                    jcall(heap2, 'add', jcall(heap1, 'poll'))
                if jcall(heap2, 'isEmpty'):
                    raise JBreak(None)
                w = jcast('int', jadd(w, jget(jcall(heap2, 'poll'), 'p')))
                k = jcast('int', (k - 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        return jcast('int', w)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


