# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大平均通过率
# 一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试
# 给你一个二维数组classes，其中classes[i]=[passi, totali]
# 表示你提前知道了第i个班级总共有totali个学生
# 其中只有 passi 个学生可以通过考试
# 给你一个整数extraStudents，表示额外有extraStudents个聪明的学生，一定能通过期末考
# 你需要给这extraStudents个学生每人都安排一个班级，使得所有班级的平均通过率最大
# 一个班级的 通过率 等于这个班级通过考试的学生人数除以这个班级的总人数
# 平均通过率 是所有班级的通过率之和除以班级数目
# 请你返回在安排这extraStudents个学生去对应班级后的最大平均通过率
# 测试链接 : https://leetcode.cn/problems/maximum-average-pass-ratio/
class Code03_MaximumAveragePassRatio:
    __java_fields__ = {}
    @staticmethod
    def maxAverageRatio(classes, m):
        m = jcast('int', m)
        n = jcast('int', jget(classes, 'length'))
        # double[] c1 : {a, b, c}
        # a : c1班级有多少人通过
        # b : c1班级总人数
        # c : 如果再来一人，c1班级通过率提升多少，(a+1)/(b+1) - a/b
        # 通过率提升的大根堆
        heap = jnew('PriorityQueue', (lambda c1, c2: (jcast('int', (-1)) if (c1[2] >= c2[2]) else 1)))
        # n * logn
        for c in classes:
            a = jcast('double', c[0])
            b = jcast('double', c[1])
            jcall(heap, 'add', jarray('double', [None], [a, b, (jdiv(jadd(a, 1), jadd(b, 1)) - jdiv(a, b))]))
        # 天才一个一个分配
        # m * logn
        while (((_java_old_1 := m), (m := jcast('int', (m + (-1)))), _java_old_1)[2] > 0):
            cur = jcall(heap, 'poll')
            a = jcast('double', jadd(cur[0], 1))
            b = jcast('double', jadd(cur[1], 1))
            jcall(heap, 'add', jarray('double', [None], [a, b, (jdiv(jadd(a, 1), jadd(b, 1)) - jdiv(a, b))]))
        # 计算通过率累加和
        ans = jcast('double', 0)
        while (not jcall(heap, 'isEmpty')):
            cur = jcall(heap, 'poll')
            ans = jcast('double', jadd(ans, jdiv(cur[0], cur[1])))
        # 返回最大平均通过率
        return jcast('double', jdiv(ans, n))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


