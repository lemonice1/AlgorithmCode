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

# 好路径的数目
# 给你一棵 n 个节点的树（连通无向无环的图）
# 节点编号从0到n-1，且恰好有n-1条边
# 给你一个长度为 n 下标从 0 开始的整数数组 vals
# 分别表示每个节点的值。同时给你一个二维整数数组 edges
# 其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边
# 好路径需要满足以下条件：开始和结束节点的值相同、 路径中所有值都小于等于开始的值
# 请你返回不同好路径的数目
# 注意，一条路径和它反向的路径算作 同一 路径
# 比方说， 0 -> 1 与 1 -> 0 视为同一条路径。单个节点也视为一条合法路径
# 测试链接 : https://leetcode.cn/problems/number-of-good-paths/
class Code03_NumberOfGoodPaths:
    __java_fields__ = {'MAXN': 'MAXN', 'father': 'father', 'maxcnt': 'maxcnt'}
    MAXN = 0
    # 需要保证集合中，代表节点的值，一定是整个集合的最大值
    father = None
    # 集合中最大值的次数，也就是 集合中代表节点的值有几个
    maxcnt = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        i = jcast('int', 0)
        while (i < n):
            Code03_NumberOfGoodPaths.father[i] = jcast('int', i)
            Code03_NumberOfGoodPaths.maxcnt[i] = jcast('int', 1)
            i = jcast('int', (i + 1))

    # 这个并查集的优化只来自扁平化
    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_NumberOfGoodPaths.father[i]):
            jset(Code03_NumberOfGoodPaths.father, i, Code03_NumberOfGoodPaths.find(Code03_NumberOfGoodPaths.father[i]))
        return jcast('int', Code03_NumberOfGoodPaths.father[i])

    # 核心！
    # 注意以下的写法！
    # 谁的值大，谁做代表节点
    # 同时注意 maxcnt 的更新
    @staticmethod
    def union(x, y, vals):
        x = jcast('int', x)
        y = jcast('int', y)
        # fx : x所在集团的代表节点，同时也是x所在集团的最大值下标
        fx = jcast('int', Code03_NumberOfGoodPaths.find(x))
        # fy : y所在集团的代表节点，同时也是y所在集团的最大值下标
        fy = jcast('int', Code03_NumberOfGoodPaths.find(y))
        path = jcast('int', 0)
        if (vals[fx] > vals[fy]):
            Code03_NumberOfGoodPaths.father[fy] = jcast('int', fx)
        else:
            if (vals[fx] < vals[fy]):
                Code03_NumberOfGoodPaths.father[fx] = jcast('int', fy)
            else:
                # 两个集团最大值一样！
                path = jcast('int', jcast('int', (Code03_NumberOfGoodPaths.maxcnt[fx] * Code03_NumberOfGoodPaths.maxcnt[fy])))
                Code03_NumberOfGoodPaths.father[fy] = jcast('int', fx)
                Code03_NumberOfGoodPaths.maxcnt[fx] = jcast('int', jcast('int', jadd(Code03_NumberOfGoodPaths.maxcnt[fx], Code03_NumberOfGoodPaths.maxcnt[fy])))
        return jcast('int', path)

    @staticmethod
    def numberOfGoodPaths(vals, edges):
        n = jcast('int', jget(vals, 'length'))
        Code03_NumberOfGoodPaths.build(n)
        ans = jcast('int', n)
        # 课上重点讲这个核心排序！
        # 处理边的时候，依次从小节点往大节点处理
        jstatic('Arrays', 'sort', edges, (lambda e1, e2: jcast('int', (jstatic('Math', 'max', vals[e1[0]], vals[e1[1]]) - jstatic('Math', 'max', vals[e2[0]], vals[e2[1]])))))
        for edge in edges:
            ans = jcast('int', jcast('int', jadd(ans, Code03_NumberOfGoodPaths.union(edge[0], edge[1], vals))))
        return jcast('int', ans)

    # 课上讲解的例子1和例子2
    @staticmethod
    def main(args):
        # 课上例子1
        # 0  1  2  3  4  5  6  7
        vals1 = jarray('int', [None], [2, 1, 1, 2, 2, 1, 1, 2])
        edges1 = jarray('int', [None, None], [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [5, 6], [6, 7]])
        jprint(Code03_NumberOfGoodPaths.numberOfGoodPaths(vals1, edges1), newline=True)
        # 课上例子2
        # 0  1  2  3  4  5  6  7  8  9 10 11 12
        vals2 = jarray('int', [None], [1, 2, 2, 3, 1, 2, 2, 1, 1, 3, 3, 3, 3])
        edges2 = jarray('int', [None, None], [[0, 1], [0, 2], [0, 3], [1, 4], [4, 7], [4, 8], [3, 5], [3, 6], [6, 9], [6, 10], [6, 11], [9, 12]])
        jprint(Code03_NumberOfGoodPaths.numberOfGoodPaths(vals2, edges2), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_NumberOfGoodPaths.MAXN = jcast('int', 30001)
Code03_NumberOfGoodPaths.father = jarray('int', [Code03_NumberOfGoodPaths.MAXN])
Code03_NumberOfGoodPaths.maxcnt = jarray('int', [Code03_NumberOfGoodPaths.MAXN])

if __name__ == '__main__':
    Code03_NumberOfGoodPaths.main([])
