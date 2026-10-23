# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 学生出勤记录II
# 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）
# 记录中只含下面三种字符：
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
# 按 总出勤 计，学生缺勤（'A'）严格 少于两天
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 给你一个整数n，表示出勤记录的长度（次数）
# 请你返回记录长度为n时，可能获得出勤奖励的记录情况数量
# 答案可能很大，结果对1000000007取模
# 测试链接 : https://leetcode.cn/problems/student-attendance-record-ii/
class Code07_StudentAttendanceRecordII:
    __java_fields__ = {'MOD': 'MOD'}
    # 正式方法
    # 矩阵快速幂
    # 时间复杂度O(logn)
    MOD = 0
    @staticmethod
    def checkRecord(n):
        n = jcast('int', n)
        # 1天的情况下，各种状态的合法数量
        start = jarray('int', [None, None], [[1, 1, 0, 1, 0, 0]])
        base = jarray('int', [None, None], [[1, 1, 0, 1, 0, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0]])
        ans = Code07_StudentAttendanceRecordII.multiply(start, Code07_StudentAttendanceRecordII.power(base, jcast('int', (n - 1))))
        ret = jcast('int', 0)
        for a in ans[0]:
            ret = jcast('int', jcast('int', jmod(jcast('int', jadd(ret, a)), Code07_StudentAttendanceRecordII.MOD)))
        return jcast('int', ret)

    # 矩阵相乘 + 乘法取模
    # a的列数一定要等于b的行数
    @staticmethod
    def multiply(a, b):
        n = jcast('int', jget(a, 'length'))
        m = jcast('int', jget(b[0], 'length'))
        k = jcast('int', jget(a[0], 'length'))
        ans = jarray('int', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                c = jcast('int', 0)
                while (c < k):
                    jset(ans[i], j, jcast('int', jcast('long', jmod(jcast('long', jadd(jcast('long', (jcast('long', a[i][c]) * b[c][j])), ans[i][j])), Code07_StudentAttendanceRecordII.MOD))))
                    c = jcast('int', (c + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return ans

    # 矩阵快速幂
    @staticmethod
    def power(m, p):
        p = jcast('int', p)
        n = jcast('int', jget(m, 'length'))
        ans = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans[i], i, 1)
            i = jcast('int', (i + 1))
        while (p != 0):
            if (jcast('int', (p & 1)) != 0):
                ans = Code07_StudentAttendanceRecordII.multiply(ans, m)
            m = Code07_StudentAttendanceRecordII.multiply(m, m)
            p = jcast('int', jcast('int', (p >> (1 & 31))))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_StudentAttendanceRecordII.MOD = jcast('int', 1000000007)
