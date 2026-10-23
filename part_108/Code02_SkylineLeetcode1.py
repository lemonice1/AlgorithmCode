# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 天际线问题(Leetcode测试)
# 测试链接 : https://leetcode.cn/problems/the-skyline-problem/
class Code02_SkylineLeetcode1:
    __java_fields__ = {'MAXN': 'MAXN', 'xsort': 'xsort', 'height': 'height'}
    # 堆结构是现成结构
    @staticmethod
    def getSkyline(arr):
        n = jcast('int', jget(arr, 'length'))
        m = jcast('int', Code02_SkylineLeetcode1.prepare(arr, n))
        # 0 : 高度
        # 1 : 影响到的位置
        heap = jnew('PriorityQueue', (lambda a, b: (b[0] - a[0])))
        i = jcast('int', 1)
        j = jcast('int', 0)
        while (i <= m):
            while ((j < n) and (arr[j][0] <= i)):
                jcall(heap, 'add', jarray('int', [None], [arr[j][2], arr[j][1]]))
                j = jcast('int', (j + 1))
            while ((not jcall(heap, 'isEmpty')) and (jcall(heap, 'peek')[1] < i)):
                jcall(heap, 'poll')
            if (not jcall(heap, 'isEmpty')):
                jset(Code02_SkylineLeetcode1.height, i, jcall(heap, 'peek')[0])
            i = jcast('int', (i + 1))
        ans = jnew('ArrayList')
        i = jcast('int', 1)
        pre = jcast('int', 0)
        while (i <= m):
            if (pre != Code02_SkylineLeetcode1.height[i]):
                jcall(ans, 'add', jstatic('Arrays', 'asList', Code02_SkylineLeetcode1.xsort[i], Code02_SkylineLeetcode1.height[i]))
            pre = jcast('int', Code02_SkylineLeetcode1.height[i])
            i = jcast('int', (i + 1))
        return ans

    MAXN = 0
    xsort = None
    height = None
    # 准备工作如下
    # 1) 收集大楼左边界、右边界-1、右边界的值
    # 2) 收集的所有值排序、去重
    # 3) 大楼的左边界和右边界，修改成排名值
    # 4) 大楼根据左边界排序
    # 5) 清空height数组
    # 6) 返回离散值的个数
    @staticmethod
    def prepare(arr, n):
        n = jcast('int', n)
        size = jcast('int', 0)
        # 大楼的左边界、右边界-1、右边界，三个值都去离散化
        i = jcast('int', 0)
        while (i < n):
            jset(Code02_SkylineLeetcode1.xsort, (size := jcast('int', (size + (1)))), arr[i][0])
            jset(Code02_SkylineLeetcode1.xsort, (size := jcast('int', (size + (1)))), jcast('int', (arr[i][1] - 1)))
            jset(Code02_SkylineLeetcode1.xsort, (size := jcast('int', (size + (1)))), arr[i][1])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_SkylineLeetcode1.xsort, 1, jcast('int', jadd(size, 1)))
        # 排序之后去重，去重后的数值有m个
        m = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= size):
            if (Code02_SkylineLeetcode1.xsort[m] != Code02_SkylineLeetcode1.xsort[i]):
                jset(Code02_SkylineLeetcode1.xsort, (m := jcast('int', (m + (1)))), Code02_SkylineLeetcode1.xsort[i])
            i = jcast('int', (i + 1))
        # 修改大楼影响到的左右边界，都变成排名值
        i = jcast('int', 0)
        while (i < n):
            jset(arr[i], 0, Code02_SkylineLeetcode1.rank(m, arr[i][0]))
            # 大楼影响到的右边界，减少1！
            # 课上重点说明的内容
            jset(arr[i], 1, Code02_SkylineLeetcode1.rank(m, jcast('int', (arr[i][1] - 1))))
            i = jcast('int', (i + 1))
        # 所有大楼根据左边界排序
        jstatic('Arrays', 'sort', arr, 0, n, (lambda a, b: (a[0] - b[0])))
        # 高度数组清空
        jstatic('Arrays', 'fill', Code02_SkylineLeetcode1.height, 1, jcast('int', jadd(m, 1)), 0)
        # 返回有多少个不同的离散值
        return jcast('int', m)

    # 查询数值v的排名(离散值)
    @staticmethod
    def rank(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', n)
        mid = 0
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code02_SkylineLeetcode1.xsort[mid] >= v):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SkylineLeetcode1.MAXN = jcast('int', 100001)
Code02_SkylineLeetcode1.xsort = jarray('int', [Code02_SkylineLeetcode1.MAXN])
Code02_SkylineLeetcode1.height = jarray('int', [Code02_SkylineLeetcode1.MAXN])
