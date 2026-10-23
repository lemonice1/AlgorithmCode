# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Y的积木，可持久化左偏树实现最优解，Python版
# 一共有n个正数数组，给定每个数组的大小mi，以及每个数组的数字
# 每个数组必须选且只能选一个数字，就可以形成n个数字的挑选方案
# 所有这些方案中，有数字累加和第1小的方案、第2小的方案、第3小的方案...
# 打印，累加和前k小的方案，各自的累加和，要求实现O(k * log k)的解
# 1 <= n、mi <= 100
# 1 <= k <= 10^4
# 1 <= 数字 <= 100
# 测试链接 : https://www.luogu.com.cn/problem/P2409
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Blocks2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXK': 'MAXK', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'k': 'k', 'arr': 'arr', 'start': 'start', 'boundary': 'boundary', 'idx': 'idx', 'jdx': 'jdx', 'cost': 'cost', 'left': 'left', 'right': 'right', 'dist': 'dist', 'pre': 'pre', 'cnt': 'cnt', 'heap': 'heap', 'heapSize': 'heapSize', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    MAXK = 0
    MAXT = 0
    INF = 0
    n = 0
    k = 0
    # 所有数组的所有数字放在arr中
    arr = None
    # start[i] : 第i个数组的第一个数字在arr中的什么位置
    start = None
    # boundary[i] : 第i个数组的越界位置在arr中的什么位置
    boundary = None
    # 左偏树代表基于之前的某个方案，做出行动的可能性
    # 左偏树的头就代表这个最优行动，假设编号为h的节点是头
    # idx[h] : 最优行动来自哪个数组
    idx = None
    # jdx[h] : 最优行动要替换掉idx[h]数组中什么位置的数
    jdx = None
    # cost[h] : 基于之前的某个方案，最优行动会让累加和增加多少
    cost = None
    left = None
    right = None
    dist = None
    # pre[h] : 基于之前的某个方案，这个方案的累加和，标签信息
    pre = None
    cnt = 0
    # heap是经典的小根堆，放着所有版本左偏树的头
    # 哪个左偏树的头节点，所代表方案的累加和最小，谁就放在heap的顶部
    heap = None
    heapSize = 0
    # 收集答案
    ans = None
    @staticmethod
    def init(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        jset(Code04_Blocks2.idx, ((_java_obj_1 := Code04_Blocks2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], i)
        Code04_Blocks2.jdx[Code04_Blocks2.cnt] = jcast('int', j)
        Code04_Blocks2.cost[Code04_Blocks2.cnt] = jcast('int', (jcast('int', (Code04_Blocks2.arr[jcast('int', jadd(j, 1))] - Code04_Blocks2.arr[j])) if (jcast('int', jadd(j, 1)) < Code04_Blocks2.boundary[i]) else Code04_Blocks2.INF))
        jset(Code04_Blocks2.left, Code04_Blocks2.cnt, jset(Code04_Blocks2.right, Code04_Blocks2.cnt, jset(Code04_Blocks2.dist, Code04_Blocks2.cnt, 0)))
        return jcast('int', Code04_Blocks2.cnt)

    @staticmethod
    def clone(i):
        i = jcast('int', i)
        jset(Code04_Blocks2.idx, ((_java_obj_4 := Code04_Blocks2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_Blocks2.idx[i])
        Code04_Blocks2.jdx[Code04_Blocks2.cnt] = jcast('int', Code04_Blocks2.jdx[i])
        Code04_Blocks2.cost[Code04_Blocks2.cnt] = jcast('int', Code04_Blocks2.cost[i])
        Code04_Blocks2.left[Code04_Blocks2.cnt] = jcast('int', Code04_Blocks2.left[i])
        Code04_Blocks2.right[Code04_Blocks2.cnt] = jcast('int', Code04_Blocks2.right[i])
        Code04_Blocks2.dist[Code04_Blocks2.cnt] = jcast('int', Code04_Blocks2.dist[i])
        return jcast('int', Code04_Blocks2.cnt)

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        if (Code04_Blocks2.cost[i] > Code04_Blocks2.cost[j]):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        h = jcast('int', Code04_Blocks2.clone(i))
        jset(Code04_Blocks2.right, h, Code04_Blocks2.merge(Code04_Blocks2.right[h], j))
        if (Code04_Blocks2.dist[Code04_Blocks2.left[h]] < Code04_Blocks2.dist[Code04_Blocks2.right[h]]):
            tmp = jcast('int', Code04_Blocks2.left[h])
            Code04_Blocks2.left[h] = jcast('int', Code04_Blocks2.right[h])
            Code04_Blocks2.right[h] = jcast('int', tmp)
        Code04_Blocks2.dist[h] = jcast('int', jcast('int', jadd(Code04_Blocks2.dist[Code04_Blocks2.right[h]], 1)))
        return jcast('int', h)

    @staticmethod
    def pop(i):
        i = jcast('int', i)
        if ((Code04_Blocks2.left[i] == 0) and (Code04_Blocks2.right[i] == 0)):
            return jcast('int', 0)
        if ((Code04_Blocks2.left[i] == 0) or (Code04_Blocks2.right[i] == 0)):
            return jcast('int', Code04_Blocks2.clone(jcast('int', jadd(Code04_Blocks2.left[i], Code04_Blocks2.right[i]))))
        return jcast('int', Code04_Blocks2.merge(Code04_Blocks2.left[i], Code04_Blocks2.right[i]))

    @staticmethod
    def compare(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        return jcast('boolean', (jcast('int', jadd(Code04_Blocks2.pre[i], Code04_Blocks2.cost[i])) < jcast('int', jadd(Code04_Blocks2.pre[j], Code04_Blocks2.cost[j]))))

    @staticmethod
    def heapAdd(i):
        i = jcast('int', i)
        jset(Code04_Blocks2.heap, ((_java_obj_7 := Code04_Blocks2), (_java_key_8 := 'heapSize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], i)
        cur = jcast('int', Code04_Blocks2.heapSize)
        up = jcast('int', jcast('int', jdiv(cur, 2)))
        tmp = 0
        while ((cur > 1) and Code04_Blocks2.compare(Code04_Blocks2.heap[cur], Code04_Blocks2.heap[up])):
            tmp = jcast('int', Code04_Blocks2.heap[up])
            Code04_Blocks2.heap[up] = jcast('int', Code04_Blocks2.heap[cur])
            Code04_Blocks2.heap[cur] = jcast('int', tmp)
            cur = jcast('int', up)
            up = jcast('int', jcast('int', jdiv(cur, 2)))

    @staticmethod
    def heapPop():
        ans = jcast('int', Code04_Blocks2.heap[1])
        jset(Code04_Blocks2.heap, 1, Code04_Blocks2.heap[((_java_obj_10 := Code04_Blocks2), (_java_key_11 := 'heapSize'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
        cur = jcast('int', 1)
        l = jcast('int', jcast('int', (cur * 2)))
        r = jcast('int', jcast('int', jadd(l, 1)))
        best = 0
        tmp = 0
        while (l <= Code04_Blocks2.heapSize):
            try:
                best = jcast('int', (r if ((r <= Code04_Blocks2.heapSize) and Code04_Blocks2.compare(Code04_Blocks2.heap[r], Code04_Blocks2.heap[l])) else l))
                best = jcast('int', (best if Code04_Blocks2.compare(Code04_Blocks2.heap[best], Code04_Blocks2.heap[cur]) else cur))
                if (best == cur):
                    raise JBreak(None)
                tmp = jcast('int', Code04_Blocks2.heap[best])
                Code04_Blocks2.heap[best] = jcast('int', Code04_Blocks2.heap[cur])
                Code04_Blocks2.heap[cur] = jcast('int', tmp)
                cur = jcast('int', best)
                l = jcast('int', jcast('int', (cur * 2)))
                r = jcast('int', jcast('int', jadd(l, 1)))
            except JContinue as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
            except JBreak as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
                break
        return jcast('int', ans)

    @staticmethod
    def compute():
        first = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Blocks2.n):
            jstatic('Arrays', 'sort', Code04_Blocks2.arr, Code04_Blocks2.start[i], Code04_Blocks2.boundary[i])
            first = jcast('int', jcast('int', jadd(first, Code04_Blocks2.arr[Code04_Blocks2.start[i]])))
            i = jcast('int', (i + 1))
        Code04_Blocks2.dist[0] = jcast('int', jcast('int', (-1)))
        head = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Blocks2.n):
            head = jcast('int', Code04_Blocks2.merge(head, Code04_Blocks2.init(i, Code04_Blocks2.start[i])))
            i = jcast('int', (i + 1))
        Code04_Blocks2.pre[head] = jcast('int', first)
        Code04_Blocks2.ans[1] = jcast('int', first)
        Code04_Blocks2.heapAdd(head)
        ansi = jcast('int', 2)
        h1 = 0
        h2 = 0
        while (ansi <= Code04_Blocks2.k):
            head = jcast('int', Code04_Blocks2.heapPop())
            Code04_Blocks2.ans[ansi] = jcast('int', jcast('int', jadd(Code04_Blocks2.pre[head], Code04_Blocks2.cost[head])))
            h1 = jcast('int', Code04_Blocks2.pop(head))
            if (h1 != 0):
                Code04_Blocks2.pre[h1] = jcast('int', Code04_Blocks2.pre[head])
                Code04_Blocks2.heapAdd(h1)
            if (jcast('int', jadd(Code04_Blocks2.jdx[head], 1)) < Code04_Blocks2.boundary[Code04_Blocks2.idx[head]]):
                h2 = jcast('int', Code04_Blocks2.merge(h1, Code04_Blocks2.init(Code04_Blocks2.idx[head], jcast('int', jadd(Code04_Blocks2.jdx[head], 1)))))
                Code04_Blocks2.pre[h2] = jcast('int', Code04_Blocks2.ans[ansi])
                Code04_Blocks2.heapAdd(h2)
            ansi = jcast('int', (ansi + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_Blocks2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_Blocks2.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        m = 0
        ai = jcast('int', 0)
        while (i <= Code04_Blocks2.n):
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_Blocks2.start[i] = jcast('int', jcast('int', jadd(ai, 1)))
            j = jcast('int', 1)
            while (j <= m):
                jcall(in_, 'nextToken')
                jset(Code04_Blocks2.arr, (ai := jcast('int', (ai + (1)))), jcast('int', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            Code04_Blocks2.boundary[i] = jcast('int', jcast('int', jadd(Code04_Blocks2.start[i], m)))
            i = jcast('int', (i + 1))
        Code04_Blocks2.compute()
        i = jcast('int', 1)
        while (i <= Code04_Blocks2.k):
            jcall(out, 'print', jadd(Code04_Blocks2.ans[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Blocks2.MAXN = jcast('int', 101)
Code04_Blocks2.MAXM = jcast('int', 10001)
Code04_Blocks2.MAXK = jcast('int', 10001)
Code04_Blocks2.MAXT = jcast('int', 1000001)
Code04_Blocks2.INF = jcast('int', 10000001)
Code04_Blocks2.n = jcast('int', 0)
Code04_Blocks2.k = jcast('int', 0)
Code04_Blocks2.arr = jarray('int', [Code04_Blocks2.MAXM])
Code04_Blocks2.start = jarray('int', [Code04_Blocks2.MAXN])
Code04_Blocks2.boundary = jarray('int', [Code04_Blocks2.MAXN])
Code04_Blocks2.idx = jarray('int', [Code04_Blocks2.MAXT])
Code04_Blocks2.jdx = jarray('int', [Code04_Blocks2.MAXT])
Code04_Blocks2.cost = jarray('int', [Code04_Blocks2.MAXT])
Code04_Blocks2.left = jarray('int', [Code04_Blocks2.MAXT])
Code04_Blocks2.right = jarray('int', [Code04_Blocks2.MAXT])
Code04_Blocks2.dist = jarray('int', [Code04_Blocks2.MAXT])
Code04_Blocks2.pre = jarray('int', [Code04_Blocks2.MAXT])
Code04_Blocks2.cnt = jcast('int', 0)
Code04_Blocks2.heap = jarray('int', [Code04_Blocks2.MAXK])
Code04_Blocks2.heapSize = jcast('int', 0)
Code04_Blocks2.ans = jarray('int', [Code04_Blocks2.MAXK])

if __name__ == '__main__':
    Code04_Blocks2.main([])
