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

# 网络管理，Python版
# 一共有n个点，编号1~n，每个点给定点权，给定n-1条边，所有点连成一棵树
# 实现如下类型的操作，操作一共发生m次
# 操作 0 x y : x号点的点权变成y
# 操作 k x y : 保证k > 0，点x到点y的路径上，打印第k大的值
# 如果路径上不够k个点，打印"invalid request!"
# 1 <= n、m <= 8 * 10^4
# 点权 <= 10^8
# 测试链接 : https://www.luogu.com.cn/problem/P4175
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_NetworkManagement2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 's': 's', 'arr': 'arr', 'ques': 'ques', 'sorted': 'sorted', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'root': 'root', 'left': 'left', 'right': 'right', 'sum': 'sum', 'cntt': 'cntt', 'deep': 'deep', 'size': 'size', 'dfn': 'dfn', 'stjump': 'stjump', 'cntd': 'cntd', 'addTree': 'addTree', 'minusTree': 'minusTree', 'cntadd': 'cntadd', 'cntminus': 'cntminus', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXT = 0
    MAXP = 0
    n = 0
    m = 0
    s = 0
    arr = None
    ques = None
    sorted = None
    # 链式前向星需要
    head = None
    next = None
    to = None
    cntg = 0
    # 外层的树状数组
    root = None
    left = None
    right = None
    sum = None
    cntt = 0
    # 树上倍增需要
    deep = None
    size = None
    dfn = None
    stjump = None
    cntd = 0
    addTree = None
    minusTree = None
    cntadd = 0
    cntminus = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_NetworkManagement2.next, ((_java_obj_1 := Code07_NetworkManagement2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_NetworkManagement2.head[u])
        Code07_NetworkManagement2.to[Code07_NetworkManagement2.cntg] = jcast('int', v)
        Code07_NetworkManagement2.head[u] = jcast('int', Code07_NetworkManagement2.cntg)

    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code07_NetworkManagement2.s)
        mid = 0
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code07_NetworkManagement2.sorted[mid] == num):
                return jcast('int', mid)
            else:
                if (Code07_NetworkManagement2.sorted[mid] < num):
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    # dfs1是递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code07_NetworkManagement2.deep[u] = jcast('int', jcast('int', jadd(Code07_NetworkManagement2.deep[fa], 1)))
        Code07_NetworkManagement2.size[u] = jcast('int', 1)
        jset(Code07_NetworkManagement2.dfn, u, ((_java_obj_4 := Code07_NetworkManagement2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        jset(Code07_NetworkManagement2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code07_NetworkManagement2.MAXP):
            jset(Code07_NetworkManagement2.stjump[u], p, Code07_NetworkManagement2.stjump[Code07_NetworkManagement2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code07_NetworkManagement2.head[u])
        while (e > 0):
            if (Code07_NetworkManagement2.to[e] != fa):
                Code07_NetworkManagement2.dfs1(Code07_NetworkManagement2.to[e], u)
            e = jcast('int', Code07_NetworkManagement2.next[e])
        e = jcast('int', Code07_NetworkManagement2.head[u])
        while (e > 0):
            if (Code07_NetworkManagement2.to[e] != fa):
                Code07_NetworkManagement2.size[u] = jcast('int', jcast('int', jadd(Code07_NetworkManagement2.size[u], Code07_NetworkManagement2.size[Code07_NetworkManagement2.to[e]])))
            e = jcast('int', Code07_NetworkManagement2.next[e])

    # dfs 迭代版：使用显式状态保存遍历进度
    # 讲解118，详解了从递归版改迭代版
    ufe = None
    stackSize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code07_NetworkManagement2.ufe[Code07_NetworkManagement2.stackSize], 0, u)
        jset(Code07_NetworkManagement2.ufe[Code07_NetworkManagement2.stackSize], 1, f)
        jset(Code07_NetworkManagement2.ufe[Code07_NetworkManagement2.stackSize], 2, e)
        Code07_NetworkManagement2.stackSize = jcast('int', (Code07_NetworkManagement2.stackSize + 1))

    @staticmethod
    def pop():
        Code07_NetworkManagement2.stackSize = jcast('int', (Code07_NetworkManagement2.stackSize - 1))
        Code07_NetworkManagement2.u = jcast('int', Code07_NetworkManagement2.ufe[Code07_NetworkManagement2.stackSize][0])
        Code07_NetworkManagement2.f = jcast('int', Code07_NetworkManagement2.ufe[Code07_NetworkManagement2.stackSize][1])
        Code07_NetworkManagement2.e = jcast('int', Code07_NetworkManagement2.ufe[Code07_NetworkManagement2.stackSize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs2():
        Code07_NetworkManagement2.stackSize = jcast('int', 0)
        Code07_NetworkManagement2.push(1, 0, jcast('int', (-1)))
        while (Code07_NetworkManagement2.stackSize > 0):
            Code07_NetworkManagement2.pop()
            if (Code07_NetworkManagement2.e == jcast('int', (-1))):
                Code07_NetworkManagement2.deep[Code07_NetworkManagement2.u] = jcast('int', jcast('int', jadd(Code07_NetworkManagement2.deep[Code07_NetworkManagement2.f], 1)))
                Code07_NetworkManagement2.size[Code07_NetworkManagement2.u] = jcast('int', 1)
                jset(Code07_NetworkManagement2.dfn, Code07_NetworkManagement2.u, ((_java_obj_7 := Code07_NetworkManagement2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                jset(Code07_NetworkManagement2.stjump[Code07_NetworkManagement2.u], 0, Code07_NetworkManagement2.f)
                p = jcast('int', 1)
                while (p < Code07_NetworkManagement2.MAXP):
                    jset(Code07_NetworkManagement2.stjump[Code07_NetworkManagement2.u], p, Code07_NetworkManagement2.stjump[Code07_NetworkManagement2.stjump[Code07_NetworkManagement2.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code07_NetworkManagement2.e = jcast('int', Code07_NetworkManagement2.head[Code07_NetworkManagement2.u])
            else:
                Code07_NetworkManagement2.e = jcast('int', Code07_NetworkManagement2.next[Code07_NetworkManagement2.e])
            if (Code07_NetworkManagement2.e != 0):
                Code07_NetworkManagement2.push(Code07_NetworkManagement2.u, Code07_NetworkManagement2.f, Code07_NetworkManagement2.e)
                if (Code07_NetworkManagement2.to[Code07_NetworkManagement2.e] != Code07_NetworkManagement2.f):
                    Code07_NetworkManagement2.push(Code07_NetworkManagement2.to[Code07_NetworkManagement2.e], Code07_NetworkManagement2.u, jcast('int', (-1)))
            else:
                e = jcast('int', Code07_NetworkManagement2.head[Code07_NetworkManagement2.u])
                while (e > 0):
                    if (Code07_NetworkManagement2.to[e] != Code07_NetworkManagement2.f):
                        Code07_NetworkManagement2.size[Code07_NetworkManagement2.u] = jcast('int', jcast('int', jadd(Code07_NetworkManagement2.size[Code07_NetworkManagement2.u], Code07_NetworkManagement2.size[Code07_NetworkManagement2.to[e]])))
                    e = jcast('int', Code07_NetworkManagement2.next[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code07_NetworkManagement2.deep[a] < Code07_NetworkManagement2.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code07_NetworkManagement2.MAXP - 1)))
        while (p >= 0):
            if (Code07_NetworkManagement2.deep[Code07_NetworkManagement2.stjump[a][p]] >= Code07_NetworkManagement2.deep[b]):
                a = jcast('int', Code07_NetworkManagement2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code07_NetworkManagement2.MAXP - 1)))
        while (p >= 0):
            if (Code07_NetworkManagement2.stjump[a][p] != Code07_NetworkManagement2.stjump[b][p]):
                a = jcast('int', Code07_NetworkManagement2.stjump[a][p])
                b = jcast('int', Code07_NetworkManagement2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code07_NetworkManagement2.stjump[a][0])

    @staticmethod
    def innerAdd(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_10 := Code07_NetworkManagement2), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        if (l == r):
            Code07_NetworkManagement2.sum[i] = jcast('int', jcast('int', jadd(Code07_NetworkManagement2.sum[i], jobv)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code07_NetworkManagement2.left, i, Code07_NetworkManagement2.innerAdd(jobi, jobv, l, mid, Code07_NetworkManagement2.left[i]))
            else:
                jset(Code07_NetworkManagement2.right, i, Code07_NetworkManagement2.innerAdd(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code07_NetworkManagement2.right[i]))
            Code07_NetworkManagement2.sum[i] = jcast('int', jcast('int', jadd(Code07_NetworkManagement2.sum[Code07_NetworkManagement2.left[i]], Code07_NetworkManagement2.sum[Code07_NetworkManagement2.right[i]])))
        return jcast('int', i)

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
        while (i <= Code07_NetworkManagement2.cntadd):
            leftsum = jcast('int', jcast('int', jadd(leftsum, Code07_NetworkManagement2.sum[Code07_NetworkManagement2.left[Code07_NetworkManagement2.addTree[i]]])))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_NetworkManagement2.cntminus):
            leftsum = jcast('int', jcast('int', (leftsum - Code07_NetworkManagement2.sum[Code07_NetworkManagement2.left[Code07_NetworkManagement2.minusTree[i]]])))
            i = jcast('int', (i + 1))
        if (jobk <= leftsum):
            i = jcast('int', 1)
            while (i <= Code07_NetworkManagement2.cntadd):
                Code07_NetworkManagement2.addTree[i] = jcast('int', Code07_NetworkManagement2.left[Code07_NetworkManagement2.addTree[i]])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code07_NetworkManagement2.cntminus):
                Code07_NetworkManagement2.minusTree[i] = jcast('int', Code07_NetworkManagement2.left[Code07_NetworkManagement2.minusTree[i]])
                i = jcast('int', (i + 1))
            return jcast('int', Code07_NetworkManagement2.innerQuery(jobk, l, mid))
        else:
            i = jcast('int', 1)
            while (i <= Code07_NetworkManagement2.cntadd):
                Code07_NetworkManagement2.addTree[i] = jcast('int', Code07_NetworkManagement2.right[Code07_NetworkManagement2.addTree[i]])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code07_NetworkManagement2.cntminus):
                Code07_NetworkManagement2.minusTree[i] = jcast('int', Code07_NetworkManagement2.right[Code07_NetworkManagement2.minusTree[i]])
                i = jcast('int', (i + 1))
            return jcast('int', Code07_NetworkManagement2.innerQuery(jcast('int', (jobk - leftsum)), jcast('int', jadd(mid, 1)), r))

    # i是dfn序号，val这是值，增加cnt的计数
    @staticmethod
    def add(i, val, cnt):
        i = jcast('int', i)
        val = jcast('int', val)
        cnt = jcast('int', cnt)
        while (i <= Code07_NetworkManagement2.n):
            jset(Code07_NetworkManagement2.root, i, Code07_NetworkManagement2.innerAdd(val, cnt, 1, Code07_NetworkManagement2.s, Code07_NetworkManagement2.root[i]))
            i = jcast('int', jcast('int', jadd(i, Code07_NetworkManagement2.lowbit(i))))

    @staticmethod
    def update(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code07_NetworkManagement2.add(Code07_NetworkManagement2.dfn[i], Code07_NetworkManagement2.arr[i], jcast('int', (-1)))
        Code07_NetworkManagement2.add(jcast('int', jadd(Code07_NetworkManagement2.dfn[i], Code07_NetworkManagement2.size[i])), Code07_NetworkManagement2.arr[i], 1)
        jset(Code07_NetworkManagement2.arr, i, Code07_NetworkManagement2.kth(v))
        Code07_NetworkManagement2.add(Code07_NetworkManagement2.dfn[i], Code07_NetworkManagement2.arr[i], 1)
        Code07_NetworkManagement2.add(jcast('int', jadd(Code07_NetworkManagement2.dfn[i], Code07_NetworkManagement2.size[i])), Code07_NetworkManagement2.arr[i], jcast('int', (-1)))

    @staticmethod
    def query(x, y, k):
        x = jcast('int', x)
        y = jcast('int', y)
        k = jcast('int', k)
        lca = jcast('int', Code07_NetworkManagement2.lca(x, y))
        lcafa = jcast('int', Code07_NetworkManagement2.stjump[lca][0])
        num = jcast('int', jcast('int', (jcast('int', (jcast('int', jadd(Code07_NetworkManagement2.deep[x], Code07_NetworkManagement2.deep[y])) - Code07_NetworkManagement2.deep[lca])) - Code07_NetworkManagement2.deep[lcafa])))
        if (num < k):
            return jcast('int', jcast('int', (-1)))
        Code07_NetworkManagement2.cntadd = jcast('int', jset(Code07_NetworkManagement2, 'cntminus', 0))
        i = jcast('int', Code07_NetworkManagement2.dfn[x])
        while (i > 0):
            jset(Code07_NetworkManagement2.addTree, ((_java_obj_13 := Code07_NetworkManagement2), (_java_key_14 := 'cntadd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code07_NetworkManagement2.root[i])
            i = jcast('int', jcast('int', (i - Code07_NetworkManagement2.lowbit(i))))
        i = jcast('int', Code07_NetworkManagement2.dfn[y])
        while (i > 0):
            jset(Code07_NetworkManagement2.addTree, ((_java_obj_16 := Code07_NetworkManagement2), (_java_key_17 := 'cntadd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code07_NetworkManagement2.root[i])
            i = jcast('int', jcast('int', (i - Code07_NetworkManagement2.lowbit(i))))
        i = jcast('int', Code07_NetworkManagement2.dfn[lca])
        while (i > 0):
            jset(Code07_NetworkManagement2.minusTree, ((_java_obj_19 := Code07_NetworkManagement2), (_java_key_20 := 'cntminus'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code07_NetworkManagement2.root[i])
            i = jcast('int', jcast('int', (i - Code07_NetworkManagement2.lowbit(i))))
        i = jcast('int', Code07_NetworkManagement2.dfn[lcafa])
        while (i > 0):
            jset(Code07_NetworkManagement2.minusTree, ((_java_obj_22 := Code07_NetworkManagement2), (_java_key_23 := 'cntminus'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], Code07_NetworkManagement2.root[i])
            i = jcast('int', jcast('int', (i - Code07_NetworkManagement2.lowbit(i))))
        return jcast('int', Code07_NetworkManagement2.sorted[Code07_NetworkManagement2.innerQuery(jcast('int', jadd(jcast('int', (num - k)), 1)), 1, Code07_NetworkManagement2.s)])

    @staticmethod
    def prepare():
        Code07_NetworkManagement2.s = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_NetworkManagement2.n):
            jset(Code07_NetworkManagement2.sorted, ((_java_obj_25 := Code07_NetworkManagement2), (_java_key_26 := 's'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3], Code07_NetworkManagement2.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_NetworkManagement2.m):
            if (Code07_NetworkManagement2.ques[i][0] == 0):
                jset(Code07_NetworkManagement2.sorted, ((_java_obj_28 := Code07_NetworkManagement2), (_java_key_29 := 's'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3], Code07_NetworkManagement2.ques[i][2])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_NetworkManagement2.sorted, 1, jcast('int', jadd(Code07_NetworkManagement2.s, 1)))
        len = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code07_NetworkManagement2.s):
            if (Code07_NetworkManagement2.sorted[len] != Code07_NetworkManagement2.sorted[i]):
                jset(Code07_NetworkManagement2.sorted, (len := jcast('int', (len + (1)))), Code07_NetworkManagement2.sorted[i])
            i = jcast('int', (i + 1))
        Code07_NetworkManagement2.s = jcast('int', len)
        i = jcast('int', 1)
        while (i <= Code07_NetworkManagement2.n):
            jset(Code07_NetworkManagement2.arr, i, Code07_NetworkManagement2.kth(Code07_NetworkManagement2.arr[i]))
            i = jcast('int', (i + 1))
        Code07_NetworkManagement2.dfs2()
        i = jcast('int', 1)
        while (i <= Code07_NetworkManagement2.n):
            Code07_NetworkManagement2.add(Code07_NetworkManagement2.dfn[i], Code07_NetworkManagement2.arr[i], 1)
            Code07_NetworkManagement2.add(jcast('int', jadd(Code07_NetworkManagement2.dfn[i], Code07_NetworkManagement2.size[i])), Code07_NetworkManagement2.arr[i], jcast('int', (-1)))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code07_NetworkManagement2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code07_NetworkManagement2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code07_NetworkManagement2.n):
            jcall(in_, 'nextToken')
            Code07_NetworkManagement2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_NetworkManagement2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code07_NetworkManagement2.addEdge(u, v)
            Code07_NetworkManagement2.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_NetworkManagement2.m):
            jcall(in_, 'nextToken')
            jset(Code07_NetworkManagement2.ques[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code07_NetworkManagement2.ques[i], 1, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code07_NetworkManagement2.ques[i], 2, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code07_NetworkManagement2.prepare()
        i = jcast('int', 1)
        k = 0
        x = 0
        y = 0
        while (i <= Code07_NetworkManagement2.m):
            k = jcast('int', Code07_NetworkManagement2.ques[i][0])
            x = jcast('int', Code07_NetworkManagement2.ques[i][1])
            y = jcast('int', Code07_NetworkManagement2.ques[i][2])
            if (k == 0):
                Code07_NetworkManagement2.update(x, y)
            else:
                ans = jcast('int', Code07_NetworkManagement2.query(x, y, k))
                if (ans == jcast('int', (-1))):
                    jcall(out, 'println', 'invalid request!')
                else:
                    jcall(out, 'println', ans)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_NetworkManagement2.MAXN = jcast('int', 80001)
Code07_NetworkManagement2.MAXT = jcast('int', jcast('int', (Code07_NetworkManagement2.MAXN * 110)))
Code07_NetworkManagement2.MAXP = jcast('int', 18)
Code07_NetworkManagement2.n = jcast('int', 0)
Code07_NetworkManagement2.m = jcast('int', 0)
Code07_NetworkManagement2.s = jcast('int', 0)
Code07_NetworkManagement2.arr = jarray('int', [Code07_NetworkManagement2.MAXN])
Code07_NetworkManagement2.ques = jarray('int', [Code07_NetworkManagement2.MAXN, 3])
Code07_NetworkManagement2.sorted = jarray('int', [jcast('int', (Code07_NetworkManagement2.MAXN << (1 & 31)))])
Code07_NetworkManagement2.head = jarray('int', [Code07_NetworkManagement2.MAXN])
Code07_NetworkManagement2.next = jarray('int', [jcast('int', (Code07_NetworkManagement2.MAXN << (1 & 31)))])
Code07_NetworkManagement2.to = jarray('int', [jcast('int', (Code07_NetworkManagement2.MAXN << (1 & 31)))])
Code07_NetworkManagement2.cntg = jcast('int', 0)
Code07_NetworkManagement2.root = jarray('int', [Code07_NetworkManagement2.MAXN])
Code07_NetworkManagement2.left = jarray('int', [Code07_NetworkManagement2.MAXT])
Code07_NetworkManagement2.right = jarray('int', [Code07_NetworkManagement2.MAXT])
Code07_NetworkManagement2.sum = jarray('int', [Code07_NetworkManagement2.MAXT])
Code07_NetworkManagement2.cntt = jcast('int', 0)
Code07_NetworkManagement2.deep = jarray('int', [Code07_NetworkManagement2.MAXN])
Code07_NetworkManagement2.size = jarray('int', [Code07_NetworkManagement2.MAXN])
Code07_NetworkManagement2.dfn = jarray('int', [Code07_NetworkManagement2.MAXN])
Code07_NetworkManagement2.stjump = jarray('int', [Code07_NetworkManagement2.MAXN, Code07_NetworkManagement2.MAXP])
Code07_NetworkManagement2.cntd = jcast('int', 0)
Code07_NetworkManagement2.addTree = jarray('int', [Code07_NetworkManagement2.MAXN])
Code07_NetworkManagement2.minusTree = jarray('int', [Code07_NetworkManagement2.MAXN])
Code07_NetworkManagement2.cntadd = jcast('int', 0)
Code07_NetworkManagement2.cntminus = jcast('int', 0)
Code07_NetworkManagement2.ufe = jarray('int', [Code07_NetworkManagement2.MAXN, 3])
Code07_NetworkManagement2.stackSize = jcast('int', 0)
Code07_NetworkManagement2.u = jcast('int', 0)
Code07_NetworkManagement2.f = jcast('int', 0)
Code07_NetworkManagement2.e = jcast('int', 0)

if __name__ == '__main__':
    Code07_NetworkManagement2.main([])
