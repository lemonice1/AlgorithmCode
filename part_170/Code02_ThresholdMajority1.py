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

# 达到阈值的最小众数，Python版
# 给定一个长度为n的数组arr，一共有m条查询，格式如下
# 查询 l r k : arr[l..r]范围上，如果所有数字的出现次数 < k，打印-1
# 如果有些数字的出现次数 >= k，打印其中的最小众数
# 1 <= n <= 10^4
# 1 <= m <= 5 * 10^4
# 1 <= arr[i] <= 10^9
# 测试链接 : https://leetcode.cn/problems/threshold-majority-queries/
# 在线评测时提交题目要求的方法接口，并一并提供使用到的公共辅助模块
class Code02_ThresholdMajority1:
    __java_fields__ = {}
    class Solution:
        __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'sorted': 'sorted', 'cntv': 'cntv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'br': 'br', 'cnt': 'cnt', 'maxCnt': 'maxCnt', 'minMode': 'minMode', 'ans': 'ans'}
        MAXN = 0
        MAXM = 0
        MAXB = 0
        n = 0
        m = 0
        arr = None
        query = None
        sorted = None
        cntv = 0
        blen = 0
        bnum = 0
        bi = None
        br = None
        cnt = None
        maxCnt = 0
        minMode = 0
        ans = None
        class QueryCmp:
            __java_fields__ = {}
            def compare(self, a, b):
                if (Code02_ThresholdMajority1.Solution.bi[a[0]] != Code02_ThresholdMajority1.Solution.bi[b[0]]):
                    return jcast('int', jcast('int', (Code02_ThresholdMajority1.Solution.bi[a[0]] - Code02_ThresholdMajority1.Solution.bi[b[0]])))
                return jcast('int', jcast('int', (a[1] - b[1])))

            def __init__(self, *args, _java_ctor=None):
                if args:
                    raise TypeError('This class has a no-argument constructor')


        @staticmethod
        def kth(num):
            num = jcast('int', num)
            left = jcast('int', 1)
            right = jcast('int', Code02_ThresholdMajority1.Solution.cntv)
            mid = 0
            ret = jcast('int', 0)
            while (left <= right):
                mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
                if (Code02_ThresholdMajority1.Solution.sorted[mid] <= num):
                    ret = jcast('int', mid)
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
            return jcast('int', ret)

        @staticmethod
        def force(l, r, k):
            l = jcast('int', l)
            r = jcast('int', r)
            k = jcast('int', k)
            mx = jcast('int', 0)
            who = jcast('int', 0)
            i = jcast('int', l)
            while (i <= r):
                ((_java_obj_1 := Code02_ThresholdMajority1.Solution.cnt), (_java_key_2 := Code02_ThresholdMajority1.Solution.arr[i]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= r):
                num = jcast('int', Code02_ThresholdMajority1.Solution.arr[i])
                if ((Code02_ThresholdMajority1.Solution.cnt[num] > mx) or ((Code02_ThresholdMajority1.Solution.cnt[num] == mx) and (num < who))):
                    mx = jcast('int', Code02_ThresholdMajority1.Solution.cnt[num])
                    who = jcast('int', num)
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= r):
                ((_java_obj_4 := Code02_ThresholdMajority1.Solution.cnt), (_java_key_5 := Code02_ThresholdMajority1.Solution.arr[i]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]
                i = jcast('int', (i + 1))
            return jcast('int', (Code02_ThresholdMajority1.Solution.sorted[who] if (mx >= k) else jcast('int', (-1))))

        @staticmethod
        def add(num):
            num = jcast('int', num)
            ((_java_obj_7 := Code02_ThresholdMajority1.Solution.cnt), (_java_key_8 := num), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]
            if ((Code02_ThresholdMajority1.Solution.cnt[num] > Code02_ThresholdMajority1.Solution.maxCnt) or ((Code02_ThresholdMajority1.Solution.cnt[num] == Code02_ThresholdMajority1.Solution.maxCnt) and (num < Code02_ThresholdMajority1.Solution.minMode))):
                jset(Code02_ThresholdMajority1.Solution, 'maxCnt', Code02_ThresholdMajority1.Solution.cnt[num])
                jset(Code02_ThresholdMajority1.Solution, 'minMode', num)

        @staticmethod
        def del_(num):
            num = jcast('int', num)
            ((_java_obj_10 := Code02_ThresholdMajority1.Solution.cnt), (_java_key_11 := num), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]

        @staticmethod
        def compute():
            block = jcast('int', 1)
            qi = jcast('int', 1)
            while ((block <= Code02_ThresholdMajority1.Solution.bnum) and (qi <= Code02_ThresholdMajority1.Solution.m)):
                jset(Code02_ThresholdMajority1.Solution, 'maxCnt', 0)
                jset(Code02_ThresholdMajority1.Solution, 'minMode', 0)
                jstatic('Arrays', 'fill', Code02_ThresholdMajority1.Solution.cnt, 1, jcast('int', jadd(Code02_ThresholdMajority1.Solution.cntv, 1)), 0)
                winl = jcast('int', jcast('int', jadd(Code02_ThresholdMajority1.Solution.br[block], 1)))
                winr = jcast('int', Code02_ThresholdMajority1.Solution.br[block])
                while ((qi <= Code02_ThresholdMajority1.Solution.m) and (Code02_ThresholdMajority1.Solution.bi[Code02_ThresholdMajority1.Solution.query[qi][0]] == block)):
                    jobl = jcast('int', Code02_ThresholdMajority1.Solution.query[qi][0])
                    jobr = jcast('int', Code02_ThresholdMajority1.Solution.query[qi][1])
                    jobk = jcast('int', Code02_ThresholdMajority1.Solution.query[qi][2])
                    id = jcast('int', Code02_ThresholdMajority1.Solution.query[qi][3])
                    if (jobr <= Code02_ThresholdMajority1.Solution.br[block]):
                        jset(Code02_ThresholdMajority1.Solution.ans, id, Code02_ThresholdMajority1.Solution.force(jobl, jobr, jobk))
                    else:
                        while (winr < jobr):
                            Code02_ThresholdMajority1.Solution.add(Code02_ThresholdMajority1.Solution.arr[(winr := jcast('int', (winr + (1))))])
                        backupCnt = jcast('int', Code02_ThresholdMajority1.Solution.maxCnt)
                        backupNum = jcast('int', Code02_ThresholdMajority1.Solution.minMode)
                        while (winl > jobl):
                            Code02_ThresholdMajority1.Solution.add(Code02_ThresholdMajority1.Solution.arr[(winl := jcast('int', (winl + (-1))))])
                        if (Code02_ThresholdMajority1.Solution.maxCnt >= jobk):
                            jset(Code02_ThresholdMajority1.Solution.ans, id, Code02_ThresholdMajority1.Solution.sorted[Code02_ThresholdMajority1.Solution.minMode])
                        else:
                            jset(Code02_ThresholdMajority1.Solution.ans, id, jcast('int', (-1)))
                        jset(Code02_ThresholdMajority1.Solution, 'maxCnt', backupCnt)
                        jset(Code02_ThresholdMajority1.Solution, 'minMode', backupNum)
                        while (winl <= Code02_ThresholdMajority1.Solution.br[block]):
                            Code02_ThresholdMajority1.Solution.del_(Code02_ThresholdMajority1.Solution.arr[((_java_old_13 := winl), (winl := jcast('int', (winl + (1)))), _java_old_13)[2]])
                    qi = jcast('int', (qi + 1))
                block = jcast('int', (block + 1))

        @staticmethod
        def prepare():
            i = jcast('int', 1)
            while (i <= Code02_ThresholdMajority1.Solution.n):
                jset(Code02_ThresholdMajority1.Solution.sorted, i, Code02_ThresholdMajority1.Solution.arr[i])
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'sort', Code02_ThresholdMajority1.Solution.sorted, 1, jcast('int', jadd(Code02_ThresholdMajority1.Solution.n, 1)))
            jset(Code02_ThresholdMajority1.Solution, 'cntv', 1)
            i = jcast('int', 2)
            while (i <= Code02_ThresholdMajority1.Solution.n):
                if (Code02_ThresholdMajority1.Solution.sorted[Code02_ThresholdMajority1.Solution.cntv] != Code02_ThresholdMajority1.Solution.sorted[i]):
                    jset(Code02_ThresholdMajority1.Solution.sorted, ((_java_obj_14 := Code02_ThresholdMajority1.Solution), (_java_key_15 := 'cntv'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3], Code02_ThresholdMajority1.Solution.sorted[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code02_ThresholdMajority1.Solution.n):
                jset(Code02_ThresholdMajority1.Solution.arr, i, Code02_ThresholdMajority1.Solution.kth(Code02_ThresholdMajority1.Solution.arr[i]))
                i = jcast('int', (i + 1))
            jset(Code02_ThresholdMajority1.Solution, 'blen', jcast('int', jstatic('Math', 'sqrt', Code02_ThresholdMajority1.Solution.n)))
            jset(Code02_ThresholdMajority1.Solution, 'bnum', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code02_ThresholdMajority1.Solution.n, Code02_ThresholdMajority1.Solution.blen)) - 1)), Code02_ThresholdMajority1.Solution.blen)))
            i = jcast('int', 1)
            while (i <= Code02_ThresholdMajority1.Solution.n):
                jset(Code02_ThresholdMajority1.Solution.bi, i, jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code02_ThresholdMajority1.Solution.blen)), 1)))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code02_ThresholdMajority1.Solution.bnum):
                jset(Code02_ThresholdMajority1.Solution.br, i, jstatic('Math', 'min', jcast('int', (i * Code02_ThresholdMajority1.Solution.blen)), Code02_ThresholdMajority1.Solution.n))
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'sort', Code02_ThresholdMajority1.Solution.query, 1, jcast('int', jadd(Code02_ThresholdMajority1.Solution.m, 1)), Code02_ThresholdMajority1.Solution.QueryCmp())

        @staticmethod
        def subarrayMajority(nums, queries):
            jset(Code02_ThresholdMajority1.Solution, 'n', jget(nums, 'length'))
            jset(Code02_ThresholdMajority1.Solution, 'm', jget(queries, 'length'))
            i = jcast('int', 1)
            j = jcast('int', 0)
            while (i <= Code02_ThresholdMajority1.Solution.n):
                jset(Code02_ThresholdMajority1.Solution.arr, i, nums[j])
                i = jcast('int', (i + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', 1)
            j = jcast('int', 0)
            while (i <= Code02_ThresholdMajority1.Solution.m):
                jset(Code02_ThresholdMajority1.Solution.query[i], 0, jcast('int', jadd(queries[j][0], 1)))
                jset(Code02_ThresholdMajority1.Solution.query[i], 1, jcast('int', jadd(queries[j][1], 1)))
                jset(Code02_ThresholdMajority1.Solution.query[i], 2, queries[j][2])
                jset(Code02_ThresholdMajority1.Solution.query[i], 3, i)
                i = jcast('int', (i + 1))
                j = jcast('int', (j + 1))
            Code02_ThresholdMajority1.Solution.prepare()
            Code02_ThresholdMajority1.Solution.compute()
            ret = jarray('int', [Code02_ThresholdMajority1.Solution.m])
            i = jcast('int', 1)
            j = jcast('int', 0)
            while (i <= Code02_ThresholdMajority1.Solution.m):
                ret[j] = jcast('int', Code02_ThresholdMajority1.Solution.ans[i])
                i = jcast('int', (i + 1))
                j = jcast('int', (j + 1))
            return ret

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ThresholdMajority1.Solution.MAXN = jcast('int', 10001)
Code02_ThresholdMajority1.Solution.MAXM = jcast('int', 50001)
Code02_ThresholdMajority1.Solution.MAXB = jcast('int', 301)
Code02_ThresholdMajority1.Solution.n = jcast('int', 0)
Code02_ThresholdMajority1.Solution.m = jcast('int', 0)
Code02_ThresholdMajority1.Solution.arr = jarray('int', [Code02_ThresholdMajority1.Solution.MAXN])
Code02_ThresholdMajority1.Solution.query = jarray('int', [Code02_ThresholdMajority1.Solution.MAXM, 4])
Code02_ThresholdMajority1.Solution.sorted = jarray('int', [Code02_ThresholdMajority1.Solution.MAXN])
Code02_ThresholdMajority1.Solution.cntv = jcast('int', 0)
Code02_ThresholdMajority1.Solution.blen = jcast('int', 0)
Code02_ThresholdMajority1.Solution.bnum = jcast('int', 0)
Code02_ThresholdMajority1.Solution.bi = jarray('int', [Code02_ThresholdMajority1.Solution.MAXN])
Code02_ThresholdMajority1.Solution.br = jarray('int', [Code02_ThresholdMajority1.Solution.MAXB])
Code02_ThresholdMajority1.Solution.cnt = jarray('int', [Code02_ThresholdMajority1.Solution.MAXN])
Code02_ThresholdMajority1.Solution.maxCnt = jcast('int', 0)
Code02_ThresholdMajority1.Solution.minMode = jcast('int', 0)
Code02_ThresholdMajority1.Solution.ans = jarray('int', [Code02_ThresholdMajority1.Solution.MAXM])
