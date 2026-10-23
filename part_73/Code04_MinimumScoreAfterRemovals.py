# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 从树中删除边的最小分数
# 存在一棵无向连通树，树中有编号从0到n-1的n个节点，以及n-1条边
# 给你一个下标从0开始的整数数组nums长度为n，其中nums[i]表示第i个节点的值
# 另给你一个二维整数数组edges长度为n-1
# 其中 edges[i] = [ai, bi] 表示树中存在一条位于节点 ai 和 bi 之间的边
# 删除树中两条不同的边以形成三个连通组件，对于一种删除边方案，定义如下步骤以计算其分数：
# 分别获取三个组件每个组件中所有节点值的异或值
# 最大 异或值和 最小 异或值的 差值 就是这种删除边方案的分数
# 返回可能的最小分数
# 测试链接 : https://leetcode.cn/problems/minimum-score-after-removals-on-a-tree/
class Code04_MinimumScoreAfterRemovals:
    __java_fields__ = {'MAXN': 'MAXN', 'dfn': 'dfn', 'xor': 'xor', 'size': 'size', 'dfnCnt': 'dfnCnt'}
    MAXN = 0
    # 下标为原始节点编号
    dfn = None
    # 下标为dfn序号
    xor = None
    # 下标为dfn序号
    size = None
    dfnCnt = 0
    @staticmethod
    def minimumScore(nums, edges):
        n = jcast('int', jget(nums, 'length'))
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < n):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        for edge in edges:
            jcall(jcall(graph, 'get', edge[0]), 'add', edge[1])
            jcall(jcall(graph, 'get', edge[1]), 'add', edge[0])
        jstatic('Arrays', 'fill', Code04_MinimumScoreAfterRemovals.dfn, 0, n, 0)
        Code04_MinimumScoreAfterRemovals.dfnCnt = jcast('int', 0)
        Code04_MinimumScoreAfterRemovals.f(nums, graph, 0)
        m = jcast('int', jget(edges, 'length'))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        i = jcast('int', 0)
        a = 0
        b = 0
        pre = 0
        pos = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        while (i < m):
            a = jcast('int', jstatic('Math', 'max', Code04_MinimumScoreAfterRemovals.dfn[edges[i][0]], Code04_MinimumScoreAfterRemovals.dfn[edges[i][1]]))
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j < m):
                b = jcast('int', jstatic('Math', 'max', Code04_MinimumScoreAfterRemovals.dfn[edges[j][0]], Code04_MinimumScoreAfterRemovals.dfn[edges[j][1]]))
                if (a < b):
                    pre = jcast('int', a)
                    pos = jcast('int', b)
                else:
                    pre = jcast('int', b)
                    pos = jcast('int', a)
                sum1 = jcast('int', Code04_MinimumScoreAfterRemovals.xor[pos])
                # xor[1] : 整棵树的异或和
                # 因为头节点是0，一定拥有最小的dfn序号1
                # f函数调用的时候，也是从0节点开始的
                if (pos < jcast('int', jadd(pre, Code04_MinimumScoreAfterRemovals.size[pre]))):
                    sum2 = jcast('int', jcast('int', (Code04_MinimumScoreAfterRemovals.xor[pre] ^ Code04_MinimumScoreAfterRemovals.xor[pos])))
                    sum3 = jcast('int', jcast('int', (Code04_MinimumScoreAfterRemovals.xor[1] ^ Code04_MinimumScoreAfterRemovals.xor[pre])))
                else:
                    sum2 = jcast('int', Code04_MinimumScoreAfterRemovals.xor[pre])
                    sum3 = jcast('int', jcast('int', (jcast('int', (Code04_MinimumScoreAfterRemovals.xor[1] ^ sum1)) ^ sum2)))
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', (jstatic('Math', 'max', jstatic('Math', 'max', sum1, sum2), sum3) - jstatic('Math', 'min', jstatic('Math', 'min', sum1, sum2), sum3)))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 当前来到原始编号u，遍历u的整棵树
    @staticmethod
    def f(nums, graph, u):
        u = jcast('int', u)
        i = jcast('int', ((_java_obj_1 := Code04_MinimumScoreAfterRemovals), (_java_key_2 := 'dfnCnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        Code04_MinimumScoreAfterRemovals.dfn[u] = jcast('int', i)
        Code04_MinimumScoreAfterRemovals.xor[i] = jcast('int', nums[u])
        Code04_MinimumScoreAfterRemovals.size[i] = jcast('int', 1)
        for v in jcall(graph, 'get', u):
            if (Code04_MinimumScoreAfterRemovals.dfn[v] == 0):
                Code04_MinimumScoreAfterRemovals.f(nums, graph, v)
                Code04_MinimumScoreAfterRemovals.xor[i] = jcast('int', jcast('int', (Code04_MinimumScoreAfterRemovals.xor[i] ^ Code04_MinimumScoreAfterRemovals.xor[Code04_MinimumScoreAfterRemovals.dfn[v]])))
                Code04_MinimumScoreAfterRemovals.size[i] = jcast('int', jcast('int', jadd(Code04_MinimumScoreAfterRemovals.size[i], Code04_MinimumScoreAfterRemovals.size[Code04_MinimumScoreAfterRemovals.dfn[v]])))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MinimumScoreAfterRemovals.MAXN = jcast('int', 1001)
Code04_MinimumScoreAfterRemovals.dfn = jarray('int', [Code04_MinimumScoreAfterRemovals.MAXN])
Code04_MinimumScoreAfterRemovals.xor = jarray('int', [Code04_MinimumScoreAfterRemovals.MAXN])
Code04_MinimumScoreAfterRemovals.size = jarray('int', [Code04_MinimumScoreAfterRemovals.MAXN])
Code04_MinimumScoreAfterRemovals.dfnCnt = jcast('int', 0)
