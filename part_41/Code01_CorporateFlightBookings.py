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

# 航班预订统计
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
# 有一份航班预订表 bookings ，
# 表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi]
# 意味着在从 firsti 到 lasti
# （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
# 请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
# 测试链接 : https://leetcode.cn/problems/corporate-flight-bookings/
class Code01_CorporateFlightBookings:
    __java_fields__ = {}
    # bookings
    # [1,5,6]
    # [2,9,3]
    # ...
    @staticmethod
    def corpFlightBookings(bookings, n):
        n = jcast('int', n)
        cnt = jarray('int', [jcast('int', jadd(n, 2))])
        # 设置差分数组，每一个操作对应两个设置
        for book in bookings:
            ((_java_obj_1 := cnt), (_java_key_2 := book[0]), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), book[2]))))[2]
            ((_java_obj_3 := cnt), (_java_key_4 := jcast('int', jadd(book[1], 1))), jset(_java_obj_3, _java_key_4, jcast('int', (jget(_java_obj_3, _java_key_4) - book[2]))))[2]
        # 加工前缀和
        i = jcast('int', 1)
        while (i < jget(cnt, 'length')):
            cnt[i] = jcast('int', jcast('int', jadd(cnt[i], cnt[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            ans[i] = jcast('int', cnt[jcast('int', jadd(i, 1))])
            i = jcast('int', (i + 1))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


