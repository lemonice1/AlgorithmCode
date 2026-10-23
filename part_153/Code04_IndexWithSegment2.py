# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树状数组套线段树，Python版
# 给定一个长度为n的数组arr，下标1~n，每条操作都是如下5种类型中的一种，一共进行m次操作
# 操作 1 x y z : 查询数字z在arr[x..y]中的排名
# 操作 2 x y z : 查询arr[x..y]中排第z名的数字
# 操作 3 x y   : arr中x位置的数字改成y
# 操作 4 x y z : 查询数字z在arr[x..y]中的前驱，不存在返回-2147483647
# 操作 5 x y z : 查询数字z在arr[x..y]中的后继，不存在返回+2147483647
# 1 <= n、m <= 2 * 10^5
# 数组中的值永远在[0, 10^8]范围内
# 测试链接 : https://www.luogu.com.cn/problem/P3380
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_IndexWithSegment2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'm': 'm', 's': 's', 'arr': 'arr', 'ques': 'ques', 'sorted': 'sorted', 'root': 'root', 'sum': 'sum', 'left': 'left', 'right': 'right', 'cntt': 'cntt', 'addTree': 'addTree', 'minusTree': 'minusTree', 'cntadd': 'cntadd', 'cntminus': 'cntminus'}
    MAXN = 0
    MAXT = 0
    INF = 0
    n = 0
    m = 0
    s = 0
    arr = None
    ques = None
    sorted = None
    root = None
    sum = None
    left = None
    right = None
    cntt = 0
    addTree = None
    minusTree = None
    cntadd = 0
    cntminus = 0
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code04_IndexWithSegment2.s)
        mid = 0
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code04_IndexWithSegment2.sorted[mid] == num):
                return jcast('int', mid)
            else:
                if (Code04_IndexWithSegment2.sorted[mid] < num):
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    # 第jobi小的数字，增加jobv的计数，数字范围l~r，节点编号i，返回头节点编号
    @staticmethod
    def innerAdd(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_1 := Code04_IndexWithSegment2), (_java_key_2 := 'cntt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        if (l == r):
            Code04_IndexWithSegment2.sum[i] = jcast('int', jcast('int', jadd(Code04_IndexWithSegment2.sum[i], jobv)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code04_IndexWithSegment2.left, i, Code04_IndexWithSegment2.innerAdd(jobi, jobv, l, mid, Code04_IndexWithSegment2.left[i]))
            else:
                jset(Code04_IndexWithSegment2.right, i, Code04_IndexWithSegment2.innerAdd(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code04_IndexWithSegment2.right[i]))
            Code04_IndexWithSegment2.sum[i] = jcast('int', jcast('int', jadd(Code04_IndexWithSegment2.sum[Code04_IndexWithSegment2.left[i]], Code04_IndexWithSegment2.sum[Code04_IndexWithSegment2.right[i]])))
        return jcast('int', i)

    # 查询比jobi小的数字个数，数字范围l~r
    # 不需要头节点编号，因为有多棵树，所有的头节点记录在addTree、minusTree
    @staticmethod
    def innerSmall(jobi, l, r):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', 0)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (jobi <= mid):
            i = jcast('int', 1)
            while (i <= Code04_IndexWithSegment2.cntadd):
                Code04_IndexWithSegment2.addTree[i] = jcast('int', Code04_IndexWithSegment2.left[Code04_IndexWithSegment2.addTree[i]])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code04_IndexWithSegment2.cntminus):
                Code04_IndexWithSegment2.minusTree[i] = jcast('int', Code04_IndexWithSegment2.left[Code04_IndexWithSegment2.minusTree[i]])
                i = jcast('int', (i + 1))
            return jcast('int', Code04_IndexWithSegment2.innerSmall(jobi, l, mid))
        else:
            leftsum = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code04_IndexWithSegment2.cntadd):
                leftsum = jcast('int', jcast('int', jadd(leftsum, Code04_IndexWithSegment2.sum[Code04_IndexWithSegment2.left[Code04_IndexWithSegment2.addTree[i]]])))
                Code04_IndexWithSegment2.addTree[i] = jcast('int', Code04_IndexWithSegment2.right[Code04_IndexWithSegment2.addTree[i]])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code04_IndexWithSegment2.cntminus):
                leftsum = jcast('int', jcast('int', (leftsum - Code04_IndexWithSegment2.sum[Code04_IndexWithSegment2.left[Code04_IndexWithSegment2.minusTree[i]]])))
                Code04_IndexWithSegment2.minusTree[i] = jcast('int', Code04_IndexWithSegment2.right[Code04_IndexWithSegment2.minusTree[i]])
                i = jcast('int', (i + 1))
            return jcast('int', jcast('int', jadd(leftsum, Code04_IndexWithSegment2.innerSmall(jobi, jcast('int', jadd(mid, 1)), r))))

    # 查询第jobk小的数字，数字范围l~r
    # 不需要头节点编号，因为有多棵树，所有的头节点记录在addTree、minusTree
    @staticmethod
    def innerQuery(jobk, l, r):
        jobk = jcast('int', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', l)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        leftsum = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_IndexWithSegment2.cntadd):
            leftsum = jcast('int', jcast('int', jadd(leftsum, Code04_IndexWithSegment2.sum[Code04_IndexWithSegment2.left[Code04_IndexWithSegment2.addTree[i]]])))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_IndexWithSegment2.cntminus):
            leftsum = jcast('int', jcast('int', (leftsum - Code04_IndexWithSegment2.sum[Code04_IndexWithSegment2.left[Code04_IndexWithSegment2.minusTree[i]]])))
            i = jcast('int', (i + 1))
        if (jobk <= leftsum):
            i = jcast('int', 1)
            while (i <= Code04_IndexWithSegment2.cntadd):
                Code04_IndexWithSegment2.addTree[i] = jcast('int', Code04_IndexWithSegment2.left[Code04_IndexWithSegment2.addTree[i]])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code04_IndexWithSegment2.cntminus):
                Code04_IndexWithSegment2.minusTree[i] = jcast('int', Code04_IndexWithSegment2.left[Code04_IndexWithSegment2.minusTree[i]])
                i = jcast('int', (i + 1))
            return jcast('int', Code04_IndexWithSegment2.innerQuery(jobk, l, mid))
        else:
            i = jcast('int', 1)
            while (i <= Code04_IndexWithSegment2.cntadd):
                Code04_IndexWithSegment2.addTree[i] = jcast('int', Code04_IndexWithSegment2.right[Code04_IndexWithSegment2.addTree[i]])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code04_IndexWithSegment2.cntminus):
                Code04_IndexWithSegment2.minusTree[i] = jcast('int', Code04_IndexWithSegment2.right[Code04_IndexWithSegment2.minusTree[i]])
                i = jcast('int', (i + 1))
            return jcast('int', Code04_IndexWithSegment2.innerQuery(jcast('int', (jobk - leftsum)), jcast('int', jadd(mid, 1)), r))

    # arr中i下标的数字，增加cnt的计数
    @staticmethod
    def add(i, cnt):
        i = jcast('int', i)
        cnt = jcast('int', cnt)
        j = jcast('int', i)
        while (j <= Code04_IndexWithSegment2.n):
            jset(Code04_IndexWithSegment2.root, j, Code04_IndexWithSegment2.innerAdd(Code04_IndexWithSegment2.arr[i], cnt, 1, Code04_IndexWithSegment2.s, Code04_IndexWithSegment2.root[j]))
            j = jcast('int', jcast('int', jadd(j, Code04_IndexWithSegment2.lowbit(j))))

    # arr中i下标的数字，改成v
    @staticmethod
    def update(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code04_IndexWithSegment2.add(i, jcast('int', (-1)))
        jset(Code04_IndexWithSegment2.arr, i, Code04_IndexWithSegment2.kth(v))
        Code04_IndexWithSegment2.add(i, 1)

    # arr[l..r]范围上，比v小的数字个数
    @staticmethod
    def small(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        Code04_IndexWithSegment2.cntadd = jcast('int', jset(Code04_IndexWithSegment2, 'cntminus', 0))
        i = jcast('int', r)
        while (i > 0):
            jset(Code04_IndexWithSegment2.addTree, ((_java_obj_4 := Code04_IndexWithSegment2), (_java_key_5 := 'cntadd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_IndexWithSegment2.root[i])
            i = jcast('int', jcast('int', (i - Code04_IndexWithSegment2.lowbit(i))))
        i = jcast('int', jcast('int', (l - 1)))
        while (i > 0):
            jset(Code04_IndexWithSegment2.minusTree, ((_java_obj_7 := Code04_IndexWithSegment2), (_java_key_8 := 'cntminus'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code04_IndexWithSegment2.root[i])
            i = jcast('int', jcast('int', (i - Code04_IndexWithSegment2.lowbit(i))))
        return jcast('int', Code04_IndexWithSegment2.innerSmall(v, 1, Code04_IndexWithSegment2.s))

    # arr[l..r]范围上，查询第k小的数字是什么
    @staticmethod
    def number(l, r, k):
        l = jcast('int', l)
        r = jcast('int', r)
        k = jcast('int', k)
        Code04_IndexWithSegment2.cntadd = jcast('int', jset(Code04_IndexWithSegment2, 'cntminus', 0))
        i = jcast('int', r)
        while (i > 0):
            jset(Code04_IndexWithSegment2.addTree, ((_java_obj_10 := Code04_IndexWithSegment2), (_java_key_11 := 'cntadd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code04_IndexWithSegment2.root[i])
            i = jcast('int', jcast('int', (i - Code04_IndexWithSegment2.lowbit(i))))
        i = jcast('int', jcast('int', (l - 1)))
        while (i > 0):
            jset(Code04_IndexWithSegment2.minusTree, ((_java_obj_13 := Code04_IndexWithSegment2), (_java_key_14 := 'cntminus'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code04_IndexWithSegment2.root[i])
            i = jcast('int', jcast('int', (i - Code04_IndexWithSegment2.lowbit(i))))
        return jcast('int', Code04_IndexWithSegment2.sorted[Code04_IndexWithSegment2.innerQuery(k, 1, Code04_IndexWithSegment2.s)])

    # arr[l..r]范围上，查询v的前驱
    @staticmethod
    def pre(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        rank = jcast('int', jcast('int', jadd(Code04_IndexWithSegment2.small(l, r, v), 1)))
        if (rank == 1):
            return jcast('int', jcast('int', (-Code04_IndexWithSegment2.INF)))
        return jcast('int', Code04_IndexWithSegment2.number(l, r, jcast('int', (rank - 1))))

    # arr[l..r]范围上，查询v的后继
    @staticmethod
    def post(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        if (v == Code04_IndexWithSegment2.s):
            return jcast('int', Code04_IndexWithSegment2.INF)
        sml = jcast('int', Code04_IndexWithSegment2.small(l, r, jcast('int', jadd(v, 1))))
        if (sml == jcast('int', jadd(jcast('int', (r - l)), 1))):
            return jcast('int', Code04_IndexWithSegment2.INF)
        return jcast('int', Code04_IndexWithSegment2.number(l, r, jcast('int', jadd(sml, 1))))

    @staticmethod
    def prepare():
        Code04_IndexWithSegment2.s = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_IndexWithSegment2.n):
            jset(Code04_IndexWithSegment2.sorted, ((_java_obj_16 := Code04_IndexWithSegment2), (_java_key_17 := 's'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code04_IndexWithSegment2.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_IndexWithSegment2.m):
            if (Code04_IndexWithSegment2.ques[i][0] == 3):
                jset(Code04_IndexWithSegment2.sorted, ((_java_obj_19 := Code04_IndexWithSegment2), (_java_key_20 := 's'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code04_IndexWithSegment2.ques[i][2])
            else:
                if (Code04_IndexWithSegment2.ques[i][0] != 2):
                    jset(Code04_IndexWithSegment2.sorted, ((_java_obj_22 := Code04_IndexWithSegment2), (_java_key_23 := 's'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], Code04_IndexWithSegment2.ques[i][3])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_IndexWithSegment2.sorted, 1, jcast('int', jadd(Code04_IndexWithSegment2.s, 1)))
        len = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code04_IndexWithSegment2.s):
            if (Code04_IndexWithSegment2.sorted[len] != Code04_IndexWithSegment2.sorted[i]):
                jset(Code04_IndexWithSegment2.sorted, (len := jcast('int', (len + (1)))), Code04_IndexWithSegment2.sorted[i])
            i = jcast('int', (i + 1))
        Code04_IndexWithSegment2.s = jcast('int', len)
        i = jcast('int', 1)
        while (i <= Code04_IndexWithSegment2.n):
            jset(Code04_IndexWithSegment2.arr, i, Code04_IndexWithSegment2.kth(Code04_IndexWithSegment2.arr[i]))
            # arr中i位置的数字，增加1个词频
            Code04_IndexWithSegment2.add(i, 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_IndexWithSegment2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_IndexWithSegment2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code04_IndexWithSegment2.n):
            jcall(in_, 'nextToken')
            Code04_IndexWithSegment2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_IndexWithSegment2.m):
            jcall(in_, 'nextToken')
            jset(Code04_IndexWithSegment2.ques[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_IndexWithSegment2.ques[i], 1, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_IndexWithSegment2.ques[i], 2, jcast('int', jget(in_, 'nval')))
            if (Code04_IndexWithSegment2.ques[i][0] != 3):
                jcall(in_, 'nextToken')
                jset(Code04_IndexWithSegment2.ques[i], 3, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code04_IndexWithSegment2.prepare()
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= Code04_IndexWithSegment2.m):
            op = jcast('int', Code04_IndexWithSegment2.ques[i][0])
            x = jcast('int', Code04_IndexWithSegment2.ques[i][1])
            y = jcast('int', Code04_IndexWithSegment2.ques[i][2])
            if (op == 3):
                Code04_IndexWithSegment2.update(x, y)
            else:
                z = jcast('int', Code04_IndexWithSegment2.ques[i][3])
                if (op == 1):
                    jcall(out, 'println', jcast('int', jadd(Code04_IndexWithSegment2.small(x, y, Code04_IndexWithSegment2.kth(z)), 1)))
                else:
                    if (op == 2):
                        jcall(out, 'println', Code04_IndexWithSegment2.number(x, y, z))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code04_IndexWithSegment2.pre(x, y, Code04_IndexWithSegment2.kth(z)))
                        else:
                            jcall(out, 'println', Code04_IndexWithSegment2.post(x, y, Code04_IndexWithSegment2.kth(z)))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_IndexWithSegment2.MAXN = jcast('int', 200001)
Code04_IndexWithSegment2.MAXT = jcast('int', jcast('int', (Code04_IndexWithSegment2.MAXN * 160)))
Code04_IndexWithSegment2.INF = jcast('int', jget(Integer, 'MAX_VALUE'))
Code04_IndexWithSegment2.n = jcast('int', 0)
Code04_IndexWithSegment2.m = jcast('int', 0)
Code04_IndexWithSegment2.s = jcast('int', 0)
Code04_IndexWithSegment2.arr = jarray('int', [Code04_IndexWithSegment2.MAXN])
Code04_IndexWithSegment2.ques = jarray('int', [Code04_IndexWithSegment2.MAXN, 4])
Code04_IndexWithSegment2.sorted = jarray('int', [jcast('int', (Code04_IndexWithSegment2.MAXN * 2))])
Code04_IndexWithSegment2.root = jarray('int', [Code04_IndexWithSegment2.MAXN])
Code04_IndexWithSegment2.sum = jarray('int', [Code04_IndexWithSegment2.MAXT])
Code04_IndexWithSegment2.left = jarray('int', [Code04_IndexWithSegment2.MAXT])
Code04_IndexWithSegment2.right = jarray('int', [Code04_IndexWithSegment2.MAXT])
Code04_IndexWithSegment2.cntt = jcast('int', 0)
Code04_IndexWithSegment2.addTree = jarray('int', [Code04_IndexWithSegment2.MAXN])
Code04_IndexWithSegment2.minusTree = jarray('int', [Code04_IndexWithSegment2.MAXN])
Code04_IndexWithSegment2.cntadd = jcast('int', 0)
Code04_IndexWithSegment2.cntminus = jcast('int', 0)

if __name__ == '__main__':
    Code04_IndexWithSegment2.main([])
