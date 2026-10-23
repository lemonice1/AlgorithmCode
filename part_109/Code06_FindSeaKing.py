# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 子数组里的海王数
# 子数组的海王数首先必须是子数组上出现次数最多的数(水王数)，并且要求出现次数>=t，t是参数
# 设计一个数据结构并实现如下两个方法
# 1) MajorityChecker(int[] arr) : 用数组arr对MajorityChecker初始化
# 2) int query(int l, int r, int t) : 返回arr[l...r]上的海王数，不存在返回-1
# 测试链接 : https://leetcode.cn/problems/online-majority-element-in-subarray/
class Code06_FindSeaKing:
    __java_fields__ = {}
    # 本实现只使用固定数组结构
    # 其他语言的同学很容易改写
    # 时间复杂度也保证了是最优
    class MajorityChecker:
        __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'cand': 'cand', 'hp': 'hp', 'n': 'n'}
        MAXN = 0
        nums = None
        # 维护线段树一段范围，候选是谁
        cand = None
        # 维护线段树一段范围，候选血量
        hp = None
        n = 0
        def _java_init_0(self, arr):
            jset(Code06_FindSeaKing.MajorityChecker, 'n', jget(arr, 'length'))
            self.buildCnt(arr)
            self.buildTree(arr, 1, Code06_FindSeaKing.MajorityChecker.n, 1)

        def query(self, l, r, t):
            l = jcast('int', l)
            r = jcast('int', r)
            t = jcast('int', t)
            ch = self.findCandidate(jcast('int', jadd(l, 1)), jcast('int', jadd(r, 1)), 1, Code06_FindSeaKing.MajorityChecker.n, 1)
            candidate = jcast('int', ch[0])
            return jcast('int', (candidate if (self.cnt(l, r, candidate) >= t) else jcast('int', (-1))))

        def buildCnt(self, arr):
            i = jcast('int', 0)
            while (i < Code06_FindSeaKing.MajorityChecker.n):
                jset(Code06_FindSeaKing.MajorityChecker.nums[i], 0, arr[i])
                jset(Code06_FindSeaKing.MajorityChecker.nums[i], 1, i)
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'sort', Code06_FindSeaKing.MajorityChecker.nums, 0, Code06_FindSeaKing.MajorityChecker.n, (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))

        def cnt(self, l, r, v):
            l = jcast('int', l)
            r = jcast('int', r)
            v = jcast('int', v)
            return jcast('int', jcast('int', (self.bs(v, r) - self.bs(v, jcast('int', (l - 1))))))

        # arr[0 ~ i]范围上
        # (<v的数) + (==v但下标<=i的数)，有几个
        def bs(self, v, i):
            v = jcast('int', v)
            i = jcast('int', i)
            left = jcast('int', 0)
            right = jcast('int', jcast('int', (Code06_FindSeaKing.MajorityChecker.n - 1)))
            mid = 0
            find = jcast('int', jcast('int', (-1)))
            while (left <= right):
                mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
                if ((Code06_FindSeaKing.MajorityChecker.nums[mid][0] < v) or ((Code06_FindSeaKing.MajorityChecker.nums[mid][0] == v) and (Code06_FindSeaKing.MajorityChecker.nums[mid][1] <= i))):
                    find = jcast('int', mid)
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
            return jcast('int', jcast('int', jadd(find, 1)))

        def up(self, i):
            i = jcast('int', i)
            lc = jcast('int', Code06_FindSeaKing.MajorityChecker.cand[jcast('int', (i << (1 & 31)))])
            lh = jcast('int', Code06_FindSeaKing.MajorityChecker.hp[jcast('int', (i << (1 & 31)))])
            rc = jcast('int', Code06_FindSeaKing.MajorityChecker.cand[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])
            rh = jcast('int', Code06_FindSeaKing.MajorityChecker.hp[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])
            jset(Code06_FindSeaKing.MajorityChecker.cand, i, (lc if ((lc == rc) or (lh >= rh)) else rc))
            jset(Code06_FindSeaKing.MajorityChecker.hp, i, (jcast('int', jadd(lh, rh)) if (lc == rc) else jstatic('Math', 'abs', jcast('int', (lh - rh)))))

        def buildTree(self, arr, l, r, i):
            l = jcast('int', l)
            r = jcast('int', r)
            i = jcast('int', i)
            if (l == r):
                jset(Code06_FindSeaKing.MajorityChecker.cand, i, arr[jcast('int', (l - 1))])
                jset(Code06_FindSeaKing.MajorityChecker.hp, i, 1)
            else:
                mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
                self.buildTree(arr, l, mid, jcast('int', (i << (1 & 31))))
                self.buildTree(arr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
                self.up(i)

        def findCandidate(self, jobl, jobr, l, r, i):
            jobl = jcast('int', jobl)
            jobr = jcast('int', jobr)
            l = jcast('int', l)
            r = jcast('int', r)
            i = jcast('int', i)
            if ((jobl <= l) and (r <= jobr)):
                return jarray('int', [None], [Code06_FindSeaKing.MajorityChecker.cand[i], Code06_FindSeaKing.MajorityChecker.hp[i]])
            else:
                mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
                if (jobr <= mid):
                    return self.findCandidate(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
                if (jobl > mid):
                    return self.findCandidate(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
                lch = self.findCandidate(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
                rch = self.findCandidate(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
                lc = jcast('int', lch[0])
                lh = jcast('int', lch[1])
                rc = jcast('int', rch[0])
                rh = jcast('int', rch[1])
                c = jcast('int', (lc if ((lc == rc) or (lh >= rh)) else rc))
                h = jcast('int', (jcast('int', jadd(lh, rh)) if (lc == rc) else jstatic('Math', 'abs', jcast('int', (lh - rh)))))
                return jarray('int', [None], [c, h])

        def __init__(self, *args, _java_ctor=None):
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int[]']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_FindSeaKing.MajorityChecker.MajorityChecker")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_FindSeaKing.MajorityChecker.MAXN = jcast('int', 20001)
Code06_FindSeaKing.MajorityChecker.nums = jarray('int', [Code06_FindSeaKing.MajorityChecker.MAXN, 2])
Code06_FindSeaKing.MajorityChecker.cand = jarray('int', [jcast('int', (Code06_FindSeaKing.MajorityChecker.MAXN << (2 & 31)))])
Code06_FindSeaKing.MajorityChecker.hp = jarray('int', [jcast('int', (Code06_FindSeaKing.MajorityChecker.MAXN << (2 & 31)))])
Code06_FindSeaKing.MajorityChecker.n = jcast('int', 0)
