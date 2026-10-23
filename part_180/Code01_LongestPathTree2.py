# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最长道路tree，Python版
# 一共n个节点，每个点给定点权，给定n-1条边，所有节点组成一棵树
# 树上任何一条链的指标 = 链的节点数 * 链上节点的最小值
# 打印这个指标的最大值
# 1 <= n <= 5 * 10^4
# 测试链接 : https://hydro.ac/p/bzoj-P2870
# 测试链接 : https://darkbzoj.cc/problem/2870
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_LongestPathTree2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'cntn': 'cntn', 'arr': 'arr', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'weight1': 'weight1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'weight2': 'weight2', 'cnt2': 'cnt2', 'vis': 'vis', 'siz': 'siz', 'ledge': 'ledge', 'lminv': 'lminv', 'cntl': 'cntl', 'redge': 'redge', 'rminv': 'rminv', 'cntr': 'cntr', 'ans': 'ans', 'stack': 'stack', 'u': 'u', 'f': 'f', 'edge': 'edge', 'minv': 'minv', 'op': 'op', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    n = 0
    cntn = 0
    arr = None
    head1 = None
    next1 = None
    to1 = None
    weight1 = None
    cnt1 = 0
    head2 = None
    next2 = None
    to2 = None
    weight2 = None
    cnt2 = 0
    vis = None
    siz = None
    ledge = None
    lminv = None
    cntl = 0
    redge = None
    rminv = None
    cntr = 0
    ans = 0
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    edge = 0
    minv = 0
    op = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, edge, minv, op, e):
        u = jcast('int', u)
        f = jcast('int', f)
        edge = jcast('int', edge)
        minv = jcast('int', minv)
        op = jcast('int', op)
        e = jcast('int', e)
        jset(Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize], 0, u)
        jset(Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize], 1, f)
        jset(Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize], 2, edge)
        jset(Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize], 3, minv)
        jset(Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize], 4, op)
        jset(Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize], 5, e)
        Code01_LongestPathTree2.stacksize = jcast('int', (Code01_LongestPathTree2.stacksize + 1))

    @staticmethod
    def pop():
        Code01_LongestPathTree2.stacksize = jcast('int', (Code01_LongestPathTree2.stacksize - 1))
        Code01_LongestPathTree2.u = jcast('int', Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize][0])
        Code01_LongestPathTree2.f = jcast('int', Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize][1])
        Code01_LongestPathTree2.edge = jcast('int', Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize][2])
        Code01_LongestPathTree2.minv = jcast('int', Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize][3])
        Code01_LongestPathTree2.op = jcast('int', Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize][4])
        Code01_LongestPathTree2.e = jcast('int', Code01_LongestPathTree2.stack[Code01_LongestPathTree2.stacksize][5])

    @staticmethod
    def addEdge1(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code01_LongestPathTree2.next1, ((_java_obj_1 := Code01_LongestPathTree2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_LongestPathTree2.head1[u])
        Code01_LongestPathTree2.to1[Code01_LongestPathTree2.cnt1] = jcast('int', v)
        Code01_LongestPathTree2.weight1[Code01_LongestPathTree2.cnt1] = jcast('int', w)
        Code01_LongestPathTree2.head1[u] = jcast('int', Code01_LongestPathTree2.cnt1)

    @staticmethod
    def addEdge2(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code01_LongestPathTree2.next2, ((_java_obj_4 := Code01_LongestPathTree2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code01_LongestPathTree2.head2[u])
        Code01_LongestPathTree2.to2[Code01_LongestPathTree2.cnt2] = jcast('int', v)
        Code01_LongestPathTree2.weight2[Code01_LongestPathTree2.cnt2] = jcast('int', w)
        Code01_LongestPathTree2.head2[u] = jcast('int', Code01_LongestPathTree2.cnt2)

    # 普通树进行三度化的重构递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def rebuild1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        last = jcast('int', 0)
        e = jcast('int', Code01_LongestPathTree2.head1[u])
        while (e > 0):
            v = jcast('int', Code01_LongestPathTree2.to1[e])
            w = jcast('int', Code01_LongestPathTree2.weight1[e])
            if (v != fa):
                if (last == 0):
                    last = jcast('int', u)
                    Code01_LongestPathTree2.addEdge2(u, v, w)
                    Code01_LongestPathTree2.addEdge2(v, u, w)
                else:
                    add = jcast('int', ((_java_obj_7 := Code01_LongestPathTree2), (_java_key_8 := 'cntn'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                    Code01_LongestPathTree2.arr[add] = jcast('int', Code01_LongestPathTree2.arr[u])
                    Code01_LongestPathTree2.addEdge2(last, add, 0)
                    Code01_LongestPathTree2.addEdge2(add, last, 0)
                    Code01_LongestPathTree2.addEdge2(add, v, w)
                    Code01_LongestPathTree2.addEdge2(v, add, w)
                    last = jcast('int', add)
                Code01_LongestPathTree2.rebuild1(v, u)
            e = jcast('int', Code01_LongestPathTree2.next1[e])

    # rebuild1迭代版
    @staticmethod
    def rebuild2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code01_LongestPathTree2.stacksize = jcast('int', 0)
        Code01_LongestPathTree2.push(cur, fa, 0, 0, 0, jcast('int', (-1)))
        while (Code01_LongestPathTree2.stacksize > 0):
            Code01_LongestPathTree2.pop()
            if (Code01_LongestPathTree2.e == jcast('int', (-1))):
                last = jcast('int', 0)
                ei = jcast('int', Code01_LongestPathTree2.head1[Code01_LongestPathTree2.u])
                while (ei > 0):
                    v = jcast('int', Code01_LongestPathTree2.to1[ei])
                    w = jcast('int', Code01_LongestPathTree2.weight1[ei])
                    if (v != Code01_LongestPathTree2.f):
                        if (last == 0):
                            last = jcast('int', Code01_LongestPathTree2.u)
                            Code01_LongestPathTree2.addEdge2(Code01_LongestPathTree2.u, v, w)
                            Code01_LongestPathTree2.addEdge2(v, Code01_LongestPathTree2.u, w)
                        else:
                            add = jcast('int', ((_java_obj_10 := Code01_LongestPathTree2), (_java_key_11 := 'cntn'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
                            Code01_LongestPathTree2.arr[add] = jcast('int', Code01_LongestPathTree2.arr[Code01_LongestPathTree2.u])
                            Code01_LongestPathTree2.addEdge2(last, add, 0)
                            Code01_LongestPathTree2.addEdge2(add, last, 0)
                            Code01_LongestPathTree2.addEdge2(add, v, w)
                            Code01_LongestPathTree2.addEdge2(v, add, w)
                            last = jcast('int', add)
                    ei = jcast('int', Code01_LongestPathTree2.next1[ei])
                Code01_LongestPathTree2.e = jcast('int', Code01_LongestPathTree2.head1[Code01_LongestPathTree2.u])
            else:
                Code01_LongestPathTree2.e = jcast('int', Code01_LongestPathTree2.next1[Code01_LongestPathTree2.e])
            if (Code01_LongestPathTree2.e != 0):
                Code01_LongestPathTree2.push(Code01_LongestPathTree2.u, Code01_LongestPathTree2.f, 0, 0, 0, Code01_LongestPathTree2.e)
                v = jcast('int', Code01_LongestPathTree2.to1[Code01_LongestPathTree2.e])
                if (v != Code01_LongestPathTree2.f):
                    Code01_LongestPathTree2.push(v, Code01_LongestPathTree2.u, 0, 0, 0, jcast('int', (-1)))

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code01_LongestPathTree2.siz[u] = jcast('int', 1)
        e = jcast('int', Code01_LongestPathTree2.head2[u])
        while (e > 0):
            v = jcast('int', Code01_LongestPathTree2.to2[e])
            if ((v != fa) and (not Code01_LongestPathTree2.vis[jcast('int', (e >> (1 & 31)))])):
                Code01_LongestPathTree2.getSize1(v, u)
                Code01_LongestPathTree2.siz[u] = jcast('int', jcast('int', jadd(Code01_LongestPathTree2.siz[u], Code01_LongestPathTree2.siz[v])))
            e = jcast('int', Code01_LongestPathTree2.next2[e])

    # getSize1的迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code01_LongestPathTree2.stacksize = jcast('int', 0)
        Code01_LongestPathTree2.push(cur, fa, 0, 0, 0, jcast('int', (-1)))
        while (Code01_LongestPathTree2.stacksize > 0):
            Code01_LongestPathTree2.pop()
            if (Code01_LongestPathTree2.e == jcast('int', (-1))):
                Code01_LongestPathTree2.siz[Code01_LongestPathTree2.u] = jcast('int', 1)
                Code01_LongestPathTree2.e = jcast('int', Code01_LongestPathTree2.head2[Code01_LongestPathTree2.u])
            else:
                Code01_LongestPathTree2.e = jcast('int', Code01_LongestPathTree2.next2[Code01_LongestPathTree2.e])
            if (Code01_LongestPathTree2.e != 0):
                Code01_LongestPathTree2.push(Code01_LongestPathTree2.u, Code01_LongestPathTree2.f, 0, 0, 0, Code01_LongestPathTree2.e)
                v = jcast('int', Code01_LongestPathTree2.to2[Code01_LongestPathTree2.e])
                if ((v != Code01_LongestPathTree2.f) and (not Code01_LongestPathTree2.vis[jcast('int', (Code01_LongestPathTree2.e >> (1 & 31)))])):
                    Code01_LongestPathTree2.push(v, Code01_LongestPathTree2.u, 0, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code01_LongestPathTree2.head2[Code01_LongestPathTree2.u])
                while (ei > 0):
                    v = jcast('int', Code01_LongestPathTree2.to2[ei])
                    if ((v != Code01_LongestPathTree2.f) and (not Code01_LongestPathTree2.vis[jcast('int', (ei >> (1 & 31)))])):
                        Code01_LongestPathTree2.siz[Code01_LongestPathTree2.u] = jcast('int', jcast('int', jadd(Code01_LongestPathTree2.siz[Code01_LongestPathTree2.u], Code01_LongestPathTree2.siz[v])))
                    ei = jcast('int', Code01_LongestPathTree2.next2[ei])

    # 找寻重心边，重心边的序号返回
    @staticmethod
    def getCentroidEdge(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code01_LongestPathTree2.getSize2(u, fa)
        total = jcast('int', Code01_LongestPathTree2.siz[u])
        half = jcast('int', jcast('int', (total >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code01_LongestPathTree2.head2[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code01_LongestPathTree2.to2[e])
                        if (((v != fa) and (not Code01_LongestPathTree2.vis[jcast('int', (e >> (1 & 31)))])) and (Code01_LongestPathTree2.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_14:
                        if _java_control_14.label not in (None,):
                            raise
                    except JBreak as _java_control_14:
                        if _java_control_14.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code01_LongestPathTree2.next2[e])
            except JContinue as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
            except JBreak as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
                break
        best = jcast('int', 0)
        edge = jcast('int', 0)
        e = jcast('int', Code01_LongestPathTree2.head2[u])
        while (e > 0):
            if (not Code01_LongestPathTree2.vis[jcast('int', (e >> (1 & 31)))]):
                v = jcast('int', Code01_LongestPathTree2.to2[e])
                sub = jcast('int', (jcast('int', (total - Code01_LongestPathTree2.siz[u])) if (v == fa) else Code01_LongestPathTree2.siz[v]))
                if (sub > best):
                    best = jcast('int', sub)
                    edge = jcast('int', e)
            e = jcast('int', Code01_LongestPathTree2.next2[e])
        return jcast('int', edge)

    # 收集信息递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa, edge, minv, op):
        u = jcast('int', u)
        fa = jcast('int', fa)
        edge = jcast('int', edge)
        minv = jcast('int', minv)
        op = jcast('int', op)
        if (op == 0):
            jset(Code01_LongestPathTree2.ledge, ((_java_obj_15 := Code01_LongestPathTree2), (_java_key_16 := 'cntl'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))))[3], edge)
            Code01_LongestPathTree2.lminv[Code01_LongestPathTree2.cntl] = jcast('int', minv)
        else:
            jset(Code01_LongestPathTree2.redge, ((_java_obj_18 := Code01_LongestPathTree2), (_java_key_19 := 'cntr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))))[3], edge)
            Code01_LongestPathTree2.rminv[Code01_LongestPathTree2.cntr] = jcast('int', minv)
        e = jcast('int', Code01_LongestPathTree2.head2[u])
        while (e > 0):
            v = jcast('int', Code01_LongestPathTree2.to2[e])
            if ((v != fa) and (not Code01_LongestPathTree2.vis[jcast('int', (e >> (1 & 31)))])):
                Code01_LongestPathTree2.dfs1(v, u, jcast('int', jadd(edge, Code01_LongestPathTree2.weight2[e])), jstatic('Math', 'min', minv, Code01_LongestPathTree2.arr[v]), op)
            e = jcast('int', Code01_LongestPathTree2.next2[e])

    # dfs1的迭代版
    @staticmethod
    def dfs2(cur, fa, pedge, pminv, opt):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        pedge = jcast('int', pedge)
        pminv = jcast('int', pminv)
        opt = jcast('int', opt)
        Code01_LongestPathTree2.stacksize = jcast('int', 0)
        Code01_LongestPathTree2.push(cur, fa, pedge, pminv, opt, jcast('int', (-1)))
        while (Code01_LongestPathTree2.stacksize > 0):
            Code01_LongestPathTree2.pop()
            if (Code01_LongestPathTree2.e == jcast('int', (-1))):
                if (Code01_LongestPathTree2.op == 0):
                    jset(Code01_LongestPathTree2.ledge, ((_java_obj_21 := Code01_LongestPathTree2), (_java_key_22 := 'cntl'), (_java_old_23 := jget(_java_obj_21, _java_key_22)), jset(_java_obj_21, _java_key_22, jcast('int', (_java_old_23 + (1)))))[3], Code01_LongestPathTree2.edge)
                    Code01_LongestPathTree2.lminv[Code01_LongestPathTree2.cntl] = jcast('int', Code01_LongestPathTree2.minv)
                else:
                    jset(Code01_LongestPathTree2.redge, ((_java_obj_24 := Code01_LongestPathTree2), (_java_key_25 := 'cntr'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))))[3], Code01_LongestPathTree2.edge)
                    Code01_LongestPathTree2.rminv[Code01_LongestPathTree2.cntr] = jcast('int', Code01_LongestPathTree2.minv)
                Code01_LongestPathTree2.e = jcast('int', Code01_LongestPathTree2.head2[Code01_LongestPathTree2.u])
            else:
                Code01_LongestPathTree2.e = jcast('int', Code01_LongestPathTree2.next2[Code01_LongestPathTree2.e])
            if (Code01_LongestPathTree2.e != 0):
                Code01_LongestPathTree2.push(Code01_LongestPathTree2.u, Code01_LongestPathTree2.f, Code01_LongestPathTree2.edge, Code01_LongestPathTree2.minv, Code01_LongestPathTree2.op, Code01_LongestPathTree2.e)
                v = jcast('int', Code01_LongestPathTree2.to2[Code01_LongestPathTree2.e])
                if ((v != Code01_LongestPathTree2.f) and (not Code01_LongestPathTree2.vis[jcast('int', (Code01_LongestPathTree2.e >> (1 & 31)))])):
                    Code01_LongestPathTree2.push(v, Code01_LongestPathTree2.u, jcast('int', jadd(Code01_LongestPathTree2.edge, Code01_LongestPathTree2.weight2[Code01_LongestPathTree2.e])), jstatic('Math', 'min', Code01_LongestPathTree2.minv, Code01_LongestPathTree2.arr[v]), Code01_LongestPathTree2.op, jcast('int', (-1)))

    # 根据minv的值从小到大排序
    # 这里使用双指针快排完成排序
    @staticmethod
    def sort(edge, minv, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', minv[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (minv[i] < pivot):
                i = jcast('int', (i + 1))
            while (minv[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', edge[i])
                edge[i] = jcast('int', edge[j])
                edge[j] = jcast('int', tmp)
                tmp = jcast('int', minv[i])
                minv[i] = jcast('int', minv[j])
                minv[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code01_LongestPathTree2.sort(edge, minv, l, j)
        Code01_LongestPathTree2.sort(edge, minv, i, r)

    @staticmethod
    def calc(edge):
        edge = jcast('int', edge)
        Code01_LongestPathTree2.cntl = jcast('int', jset(Code01_LongestPathTree2, 'cntr', 0))
        v1 = jcast('int', Code01_LongestPathTree2.to2[edge])
        v2 = jcast('int', Code01_LongestPathTree2.to2[jcast('int', (edge ^ 1))])
        # dfs1(v1, 0, 0, arr[v1], 0);
        # dfs1(v2, 0, weight2[edge], arr[v2], 1);
        Code01_LongestPathTree2.dfs2(v1, 0, 0, Code01_LongestPathTree2.arr[v1], 0)
        Code01_LongestPathTree2.dfs2(v2, 0, Code01_LongestPathTree2.weight2[edge], Code01_LongestPathTree2.arr[v2], 1)
        Code01_LongestPathTree2.sort(Code01_LongestPathTree2.ledge, Code01_LongestPathTree2.lminv, 1, Code01_LongestPathTree2.cntl)
        Code01_LongestPathTree2.sort(Code01_LongestPathTree2.redge, Code01_LongestPathTree2.rminv, 1, Code01_LongestPathTree2.cntr)
        maxEdge = jcast('long', 0)
        i = jcast('int', Code01_LongestPathTree2.cntl)
        j = jcast('int', Code01_LongestPathTree2.cntr)
        while (i >= 1):
            while ((j >= 1) and (Code01_LongestPathTree2.rminv[j] >= Code01_LongestPathTree2.lminv[i])):
                maxEdge = jcast('long', jstatic('Math', 'max', maxEdge, Code01_LongestPathTree2.redge[j]))
                j = jcast('int', (j - 1))
            if (j < Code01_LongestPathTree2.cntr):
                Code01_LongestPathTree2.ans = jcast('long', jstatic('Math', 'max', Code01_LongestPathTree2.ans, jcast('long', (jcast('long', (1 * Code01_LongestPathTree2.lminv[i])) * jcast('long', jadd(jcast('long', jadd(maxEdge, Code01_LongestPathTree2.ledge[i])), 1))))))
            i = jcast('int', (i - 1))
        maxEdge = jcast('long', 0)
        i = jcast('int', Code01_LongestPathTree2.cntr)
        j = jcast('int', Code01_LongestPathTree2.cntl)
        while (i >= 1):
            while ((j >= 1) and (Code01_LongestPathTree2.lminv[j] >= Code01_LongestPathTree2.rminv[i])):
                maxEdge = jcast('long', jstatic('Math', 'max', maxEdge, Code01_LongestPathTree2.ledge[j]))
                j = jcast('int', (j - 1))
            if (j < Code01_LongestPathTree2.cntl):
                Code01_LongestPathTree2.ans = jcast('long', jstatic('Math', 'max', Code01_LongestPathTree2.ans, jcast('long', (jcast('long', (1 * Code01_LongestPathTree2.rminv[i])) * jcast('long', jadd(jcast('long', jadd(maxEdge, Code01_LongestPathTree2.redge[i])), 1))))))
            i = jcast('int', (i - 1))

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        edge = jcast('int', Code01_LongestPathTree2.getCentroidEdge(u, 0))
        if (edge > 0):
            Code01_LongestPathTree2.vis[jcast('int', (edge >> (1 & 31)))] = jcast('boolean', True)
            Code01_LongestPathTree2.calc(edge)
            Code01_LongestPathTree2.solve(Code01_LongestPathTree2.to2[edge])
            Code01_LongestPathTree2.solve(Code01_LongestPathTree2.to2[jcast('int', (edge ^ 1))])

    @staticmethod
    def main(args):
        in_ = Code01_LongestPathTree2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_LongestPathTree2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_LongestPathTree2.n):
            jset(Code01_LongestPathTree2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_LongestPathTree2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code01_LongestPathTree2.addEdge1(u, v, 1)
            Code01_LongestPathTree2.addEdge1(v, u, 1)
            i = jcast('int', (i + 1))
        Code01_LongestPathTree2.cntn = jcast('int', Code01_LongestPathTree2.n)
        Code01_LongestPathTree2.cnt2 = jcast('int', 1)
        # rebuild1(1, 0);
        Code01_LongestPathTree2.rebuild2(1, 0)
        Code01_LongestPathTree2.solve(1)
        jcall(out, 'println', Code01_LongestPathTree2.ans)
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_27 := self), (_java_key_28 := 'ptr'), (_java_old_29 := jget(_java_obj_27, _java_key_28)), jset(_java_obj_27, _java_key_28, jcast('int', (_java_old_29 + (1)))), _java_old_29)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_LongestPathTree2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_LongestPathTree2.MAXN = jcast('int', 100001)
Code01_LongestPathTree2.n = jcast('int', 0)
Code01_LongestPathTree2.cntn = jcast('int', 0)
Code01_LongestPathTree2.arr = jarray('int', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.head1 = jarray('int', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.next1 = jarray('int', [jcast('int', (Code01_LongestPathTree2.MAXN << (1 & 31)))])
Code01_LongestPathTree2.to1 = jarray('int', [jcast('int', (Code01_LongestPathTree2.MAXN << (1 & 31)))])
Code01_LongestPathTree2.weight1 = jarray('int', [jcast('int', (Code01_LongestPathTree2.MAXN << (1 & 31)))])
Code01_LongestPathTree2.cnt1 = jcast('int', 0)
Code01_LongestPathTree2.head2 = jarray('int', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.next2 = jarray('int', [jcast('int', (Code01_LongestPathTree2.MAXN << (1 & 31)))])
Code01_LongestPathTree2.to2 = jarray('int', [jcast('int', (Code01_LongestPathTree2.MAXN << (1 & 31)))])
Code01_LongestPathTree2.weight2 = jarray('int', [jcast('int', (Code01_LongestPathTree2.MAXN << (1 & 31)))])
Code01_LongestPathTree2.cnt2 = jcast('int', 0)
Code01_LongestPathTree2.vis = jarray('boolean', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.siz = jarray('int', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.ledge = jarray('int', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.lminv = jarray('int', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.cntl = jcast('int', 0)
Code01_LongestPathTree2.redge = jarray('int', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.rminv = jarray('int', [Code01_LongestPathTree2.MAXN])
Code01_LongestPathTree2.cntr = jcast('int', 0)
Code01_LongestPathTree2.ans = jcast('long', 0)
Code01_LongestPathTree2.stack = jarray('int', [Code01_LongestPathTree2.MAXN, 6])
Code01_LongestPathTree2.u = jcast('int', 0)
Code01_LongestPathTree2.f = jcast('int', 0)
Code01_LongestPathTree2.edge = jcast('int', 0)
Code01_LongestPathTree2.minv = jcast('int', 0)
Code01_LongestPathTree2.op = jcast('int', 0)
Code01_LongestPathTree2.e = jcast('int', 0)
Code01_LongestPathTree2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code01_LongestPathTree2.main([])
