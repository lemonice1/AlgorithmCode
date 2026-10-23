# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 划分可重集，主席树优化建图，Python版
# 给定长度为n的数组arr，从左到右把每个数划分进可重集a、b
# 每个数至少要进入a或b中的一个
# arr[i]能进集合a的条件为，i左侧任何 <= arr[i] - k的数字，都没进集合a
# arr[i]能进集合b的条件为，i左侧任何 >= arr[i] + k的数字，都没进集合b
# 然后有m组关系，每组 x y，保证 x < y，表示两个位置的数不能进入同一个集合
# 如果不存在合法划分，打印-1，如果存在方案，打印能划分成功的最小k值
# n、m <= 2 * 10^4
# arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P7477
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Partition_Multiset_cpp_2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'm': 'm', 'cntt': 'cntt', 'v': 'v', 'x': 'x', 'y': 'y', 'rak': 'rak', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'rootOut1': 'rootOut1', 'rootIn1': 'rootIn1', 'rootOut2': 'rootOut2', 'rootIn2': 'rootIn2', 'ls': 'ls', 'rs': 'rs', 'curVersion': 'curVersion', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    MAXT = 0
    MAXE = 0
    n = 0
    m = 0
    cntt = 0
    v = None
    x = None
    y = None
    rak = None
    arr = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    # 主席树
    rootOut1 = None
    rootIn1 = None
    rootOut2 = None
    rootIn2 = None
    ls = None
    rs = None
    curVersion = 0
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stau = None
    stas = None
    stae = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        Code05_Partition_Multiset_cpp_2.stau[Code05_Partition_Multiset_cpp_2.stacksize] = jcast('int', u)
        Code05_Partition_Multiset_cpp_2.stas[Code05_Partition_Multiset_cpp_2.stacksize] = jcast('int', status)
        Code05_Partition_Multiset_cpp_2.stae[Code05_Partition_Multiset_cpp_2.stacksize] = jcast('int', e)
        Code05_Partition_Multiset_cpp_2.stacksize = jcast('int', (Code05_Partition_Multiset_cpp_2.stacksize + 1))

    @staticmethod
    def pop():
        Code05_Partition_Multiset_cpp_2.stacksize = jcast('int', (Code05_Partition_Multiset_cpp_2.stacksize - 1))
        Code05_Partition_Multiset_cpp_2.u = jcast('int', Code05_Partition_Multiset_cpp_2.stau[Code05_Partition_Multiset_cpp_2.stacksize])
        Code05_Partition_Multiset_cpp_2.status = jcast('int', Code05_Partition_Multiset_cpp_2.stas[Code05_Partition_Multiset_cpp_2.stacksize])
        Code05_Partition_Multiset_cpp_2.e = jcast('int', Code05_Partition_Multiset_cpp_2.stae[Code05_Partition_Multiset_cpp_2.stacksize])

    # <= num的范围长度
    @staticmethod
    def small(num):
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', Code05_Partition_Multiset_cpp_2.n)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code05_Partition_Multiset_cpp_2.arr[mid][0] <= num):
                ans = jcast('int', mid)
                l = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                r = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ans)

    # >= num的范围长度
    @staticmethod
    def big(num):
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', Code05_Partition_Multiset_cpp_2.n)
        mid = 0
        ans = jcast('int', jcast('int', jadd(Code05_Partition_Multiset_cpp_2.n, 1)))
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code05_Partition_Multiset_cpp_2.arr[mid][0] >= num):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', jcast('int', jadd(jcast('int', (Code05_Partition_Multiset_cpp_2.n - ans)), 1)))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Partition_Multiset_cpp_2.nxt, ((_java_obj_1 := Code05_Partition_Multiset_cpp_2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Partition_Multiset_cpp_2.head[u])
        Code05_Partition_Multiset_cpp_2.to[Code05_Partition_Multiset_cpp_2.cntg] = jcast('int', v)
        Code05_Partition_Multiset_cpp_2.head[u] = jcast('int', Code05_Partition_Multiset_cpp_2.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code05_Partition_Multiset_cpp_2.dfn, u, jset(Code05_Partition_Multiset_cpp_2.low, u, ((_java_obj_4 := Code05_Partition_Multiset_cpp_2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code05_Partition_Multiset_cpp_2.sta, ((_java_obj_7 := Code05_Partition_Multiset_cpp_2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code05_Partition_Multiset_cpp_2.head[u])
        while (e > 0):
            v = jcast('int', Code05_Partition_Multiset_cpp_2.to[e])
            if (Code05_Partition_Multiset_cpp_2.dfn[v] == 0):
                Code05_Partition_Multiset_cpp_2.tarjan1(v)
                jset(Code05_Partition_Multiset_cpp_2.low, u, jstatic('Math', 'min', Code05_Partition_Multiset_cpp_2.low[u], Code05_Partition_Multiset_cpp_2.low[v]))
            else:
                if (Code05_Partition_Multiset_cpp_2.belong[v] == 0):
                    jset(Code05_Partition_Multiset_cpp_2.low, u, jstatic('Math', 'min', Code05_Partition_Multiset_cpp_2.low[u], Code05_Partition_Multiset_cpp_2.dfn[v]))
            e = jcast('int', Code05_Partition_Multiset_cpp_2.nxt[e])
        if (Code05_Partition_Multiset_cpp_2.dfn[u] == Code05_Partition_Multiset_cpp_2.low[u]):
            Code05_Partition_Multiset_cpp_2.sccCnt = jcast('int', (Code05_Partition_Multiset_cpp_2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code05_Partition_Multiset_cpp_2.sta[((_java_obj_10 := Code05_Partition_Multiset_cpp_2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code05_Partition_Multiset_cpp_2.belong[pop] = jcast('int', Code05_Partition_Multiset_cpp_2.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code05_Partition_Multiset_cpp_2.stacksize = jcast('int', 0)
        Code05_Partition_Multiset_cpp_2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_Partition_Multiset_cpp_2.stacksize > 0):
            Code05_Partition_Multiset_cpp_2.pop()
            if (Code05_Partition_Multiset_cpp_2.status == jcast('int', (-1))):
                jset(Code05_Partition_Multiset_cpp_2.dfn, Code05_Partition_Multiset_cpp_2.u, jset(Code05_Partition_Multiset_cpp_2.low, Code05_Partition_Multiset_cpp_2.u, ((_java_obj_13 := Code05_Partition_Multiset_cpp_2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code05_Partition_Multiset_cpp_2.sta, ((_java_obj_16 := Code05_Partition_Multiset_cpp_2), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code05_Partition_Multiset_cpp_2.u)
                Code05_Partition_Multiset_cpp_2.e = jcast('int', Code05_Partition_Multiset_cpp_2.head[Code05_Partition_Multiset_cpp_2.u])
            else:
                v = jcast('int', Code05_Partition_Multiset_cpp_2.to[Code05_Partition_Multiset_cpp_2.e])
                if (Code05_Partition_Multiset_cpp_2.status == 0):
                    jset(Code05_Partition_Multiset_cpp_2.low, Code05_Partition_Multiset_cpp_2.u, jstatic('Math', 'min', Code05_Partition_Multiset_cpp_2.low[Code05_Partition_Multiset_cpp_2.u], Code05_Partition_Multiset_cpp_2.low[v]))
                if ((Code05_Partition_Multiset_cpp_2.status == 1) and (Code05_Partition_Multiset_cpp_2.belong[v] == 0)):
                    jset(Code05_Partition_Multiset_cpp_2.low, Code05_Partition_Multiset_cpp_2.u, jstatic('Math', 'min', Code05_Partition_Multiset_cpp_2.low[Code05_Partition_Multiset_cpp_2.u], Code05_Partition_Multiset_cpp_2.dfn[v]))
                Code05_Partition_Multiset_cpp_2.e = jcast('int', Code05_Partition_Multiset_cpp_2.nxt[Code05_Partition_Multiset_cpp_2.e])
            if (Code05_Partition_Multiset_cpp_2.e != 0):
                v = jcast('int', Code05_Partition_Multiset_cpp_2.to[Code05_Partition_Multiset_cpp_2.e])
                if (Code05_Partition_Multiset_cpp_2.dfn[v] == 0):
                    Code05_Partition_Multiset_cpp_2.push(Code05_Partition_Multiset_cpp_2.u, 0, Code05_Partition_Multiset_cpp_2.e)
                    Code05_Partition_Multiset_cpp_2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_Partition_Multiset_cpp_2.push(Code05_Partition_Multiset_cpp_2.u, 1, Code05_Partition_Multiset_cpp_2.e)
            else:
                if (Code05_Partition_Multiset_cpp_2.dfn[Code05_Partition_Multiset_cpp_2.u] == Code05_Partition_Multiset_cpp_2.low[Code05_Partition_Multiset_cpp_2.u]):
                    Code05_Partition_Multiset_cpp_2.sccCnt = jcast('int', (Code05_Partition_Multiset_cpp_2.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code05_Partition_Multiset_cpp_2.sta[((_java_obj_19 := Code05_Partition_Multiset_cpp_2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code05_Partition_Multiset_cpp_2.belong[pop] = jcast('int', Code05_Partition_Multiset_cpp_2.sccCnt)
                        if not ((pop != Code05_Partition_Multiset_cpp_2.u)):
                            break

    @staticmethod
    def buildOut(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_22 := Code05_Partition_Multiset_cpp_2), (_java_key_23 := 'cntt'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3])
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code05_Partition_Multiset_cpp_2.ls, rt, Code05_Partition_Multiset_cpp_2.buildOut(l, mid))
            jset(Code05_Partition_Multiset_cpp_2.rs, rt, Code05_Partition_Multiset_cpp_2.buildOut(jcast('int', jadd(mid, 1)), r))
            Code05_Partition_Multiset_cpp_2.addEdge(Code05_Partition_Multiset_cpp_2.ls[rt], rt)
            Code05_Partition_Multiset_cpp_2.addEdge(Code05_Partition_Multiset_cpp_2.rs[rt], rt)
        return jcast('int', rt)

    @staticmethod
    def buildIn(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_25 := Code05_Partition_Multiset_cpp_2), (_java_key_26 := 'cntt'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code05_Partition_Multiset_cpp_2.ls, rt, Code05_Partition_Multiset_cpp_2.buildIn(l, mid))
            jset(Code05_Partition_Multiset_cpp_2.rs, rt, Code05_Partition_Multiset_cpp_2.buildIn(jcast('int', jadd(mid, 1)), r))
            Code05_Partition_Multiset_cpp_2.addEdge(rt, Code05_Partition_Multiset_cpp_2.ls[rt])
            Code05_Partition_Multiset_cpp_2.addEdge(rt, Code05_Partition_Multiset_cpp_2.rs[rt])
        return jcast('int', rt)

    @staticmethod
    def addOut(jobx, jobv, l, r, i):
        jobx = jcast('int', jobx)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_28 := Code05_Partition_Multiset_cpp_2), (_java_key_29 := 'cntt'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3])
        Code05_Partition_Multiset_cpp_2.ls[rt] = jcast('int', Code05_Partition_Multiset_cpp_2.ls[i])
        Code05_Partition_Multiset_cpp_2.rs[rt] = jcast('int', Code05_Partition_Multiset_cpp_2.rs[i])
        Code05_Partition_Multiset_cpp_2.addEdge(i, rt)
        if (l == r):
            Code05_Partition_Multiset_cpp_2.addEdge(jobx, rt)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobv <= mid):
                jset(Code05_Partition_Multiset_cpp_2.ls, rt, Code05_Partition_Multiset_cpp_2.addOut(jobx, jobv, l, mid, Code05_Partition_Multiset_cpp_2.ls[rt]))
                Code05_Partition_Multiset_cpp_2.addEdge(Code05_Partition_Multiset_cpp_2.ls[rt], rt)
            else:
                jset(Code05_Partition_Multiset_cpp_2.rs, rt, Code05_Partition_Multiset_cpp_2.addOut(jobx, jobv, jcast('int', jadd(mid, 1)), r, Code05_Partition_Multiset_cpp_2.rs[rt]))
                Code05_Partition_Multiset_cpp_2.addEdge(Code05_Partition_Multiset_cpp_2.rs[rt], rt)
        return jcast('int', rt)

    @staticmethod
    def addIn(jobx, jobv, l, r, i):
        jobx = jcast('int', jobx)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_31 := Code05_Partition_Multiset_cpp_2), (_java_key_32 := 'cntt'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))))[3])
        Code05_Partition_Multiset_cpp_2.ls[rt] = jcast('int', Code05_Partition_Multiset_cpp_2.ls[i])
        Code05_Partition_Multiset_cpp_2.rs[rt] = jcast('int', Code05_Partition_Multiset_cpp_2.rs[i])
        Code05_Partition_Multiset_cpp_2.addEdge(rt, i)
        if (l == r):
            Code05_Partition_Multiset_cpp_2.addEdge(rt, jobx)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobv <= mid):
                jset(Code05_Partition_Multiset_cpp_2.ls, rt, Code05_Partition_Multiset_cpp_2.addIn(jobx, jobv, l, mid, Code05_Partition_Multiset_cpp_2.ls[rt]))
                Code05_Partition_Multiset_cpp_2.addEdge(rt, Code05_Partition_Multiset_cpp_2.ls[rt])
            else:
                jset(Code05_Partition_Multiset_cpp_2.rs, rt, Code05_Partition_Multiset_cpp_2.addIn(jobx, jobv, jcast('int', jadd(mid, 1)), r, Code05_Partition_Multiset_cpp_2.rs[rt]))
                Code05_Partition_Multiset_cpp_2.addEdge(rt, Code05_Partition_Multiset_cpp_2.rs[rt])
        return jcast('int', rt)

    @staticmethod
    def rangeToX(jobl, jobr, jobx, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_Partition_Multiset_cpp_2.addEdge(i, jobx)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code05_Partition_Multiset_cpp_2.rangeToX(jobl, jobr, jobx, l, mid, Code05_Partition_Multiset_cpp_2.ls[i])
            if (jobr > mid):
                Code05_Partition_Multiset_cpp_2.rangeToX(jobl, jobr, jobx, jcast('int', jadd(mid, 1)), r, Code05_Partition_Multiset_cpp_2.rs[i])

    @staticmethod
    def xToRange(jobx, jobl, jobr, l, r, i):
        jobx = jcast('int', jobx)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_Partition_Multiset_cpp_2.addEdge(jobx, i)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code05_Partition_Multiset_cpp_2.xToRange(jobx, jobl, jobr, l, mid, Code05_Partition_Multiset_cpp_2.ls[i])
            if (jobr > mid):
                Code05_Partition_Multiset_cpp_2.xToRange(jobx, jobl, jobr, jcast('int', jadd(mid, 1)), r, Code05_Partition_Multiset_cpp_2.rs[i])

    @staticmethod
    def add(x, otherx, si, bi):
        x = jcast('int', x)
        otherx = jcast('int', otherx)
        si = jcast('int', si)
        bi = jcast('int', bi)
        Code05_Partition_Multiset_cpp_2.curVersion = jcast('int', (Code05_Partition_Multiset_cpp_2.curVersion + 1))
        jset(Code05_Partition_Multiset_cpp_2.rootOut1, Code05_Partition_Multiset_cpp_2.curVersion, Code05_Partition_Multiset_cpp_2.addOut(x, si, 1, Code05_Partition_Multiset_cpp_2.n, Code05_Partition_Multiset_cpp_2.rootOut1[jcast('int', (Code05_Partition_Multiset_cpp_2.curVersion - 1))]))
        jset(Code05_Partition_Multiset_cpp_2.rootIn1, Code05_Partition_Multiset_cpp_2.curVersion, Code05_Partition_Multiset_cpp_2.addIn(otherx, si, 1, Code05_Partition_Multiset_cpp_2.n, Code05_Partition_Multiset_cpp_2.rootIn1[jcast('int', (Code05_Partition_Multiset_cpp_2.curVersion - 1))]))
        jset(Code05_Partition_Multiset_cpp_2.rootOut2, Code05_Partition_Multiset_cpp_2.curVersion, Code05_Partition_Multiset_cpp_2.addOut(otherx, bi, 1, Code05_Partition_Multiset_cpp_2.n, Code05_Partition_Multiset_cpp_2.rootOut2[jcast('int', (Code05_Partition_Multiset_cpp_2.curVersion - 1))]))
        jset(Code05_Partition_Multiset_cpp_2.rootIn2, Code05_Partition_Multiset_cpp_2.curVersion, Code05_Partition_Multiset_cpp_2.addIn(x, bi, 1, Code05_Partition_Multiset_cpp_2.n, Code05_Partition_Multiset_cpp_2.rootIn2[jcast('int', (Code05_Partition_Multiset_cpp_2.curVersion - 1))]))

    @staticmethod
    def link(x, otherx, lowCnt, hightCnt):
        x = jcast('int', x)
        otherx = jcast('int', otherx)
        lowCnt = jcast('int', lowCnt)
        hightCnt = jcast('int', hightCnt)
        if (lowCnt > 0):
            Code05_Partition_Multiset_cpp_2.xToRange(x, 1, lowCnt, 1, Code05_Partition_Multiset_cpp_2.n, Code05_Partition_Multiset_cpp_2.rootIn1[Code05_Partition_Multiset_cpp_2.curVersion])
            Code05_Partition_Multiset_cpp_2.rangeToX(1, lowCnt, otherx, 1, Code05_Partition_Multiset_cpp_2.n, Code05_Partition_Multiset_cpp_2.rootOut1[Code05_Partition_Multiset_cpp_2.curVersion])
        if (hightCnt > 0):
            Code05_Partition_Multiset_cpp_2.xToRange(otherx, 1, hightCnt, 1, Code05_Partition_Multiset_cpp_2.n, Code05_Partition_Multiset_cpp_2.rootIn2[Code05_Partition_Multiset_cpp_2.curVersion])
            Code05_Partition_Multiset_cpp_2.rangeToX(1, hightCnt, x, 1, Code05_Partition_Multiset_cpp_2.n, Code05_Partition_Multiset_cpp_2.rootOut2[Code05_Partition_Multiset_cpp_2.curVersion])

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', jadd(x, Code05_Partition_Multiset_cpp_2.n)) if (x <= Code05_Partition_Multiset_cpp_2.n) else jcast('int', (x - Code05_Partition_Multiset_cpp_2.n))))

    @staticmethod
    def buildGraph(k):
        k = jcast('int', k)
        Code05_Partition_Multiset_cpp_2.cntt = jcast('int', jcast('int', (Code05_Partition_Multiset_cpp_2.n << (1 & 31))))
        jset(Code05_Partition_Multiset_cpp_2.rootOut1, 0, Code05_Partition_Multiset_cpp_2.buildOut(1, Code05_Partition_Multiset_cpp_2.n))
        jset(Code05_Partition_Multiset_cpp_2.rootIn1, 0, Code05_Partition_Multiset_cpp_2.buildIn(1, Code05_Partition_Multiset_cpp_2.n))
        jset(Code05_Partition_Multiset_cpp_2.rootOut2, 0, Code05_Partition_Multiset_cpp_2.buildOut(1, Code05_Partition_Multiset_cpp_2.n))
        jset(Code05_Partition_Multiset_cpp_2.rootIn2, 0, Code05_Partition_Multiset_cpp_2.buildIn(1, Code05_Partition_Multiset_cpp_2.n))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_cpp_2.m):
            Code05_Partition_Multiset_cpp_2.addEdge(Code05_Partition_Multiset_cpp_2.x[i], Code05_Partition_Multiset_cpp_2.other(Code05_Partition_Multiset_cpp_2.y[i]))
            Code05_Partition_Multiset_cpp_2.addEdge(Code05_Partition_Multiset_cpp_2.y[i], Code05_Partition_Multiset_cpp_2.other(Code05_Partition_Multiset_cpp_2.x[i]))
            Code05_Partition_Multiset_cpp_2.addEdge(Code05_Partition_Multiset_cpp_2.other(Code05_Partition_Multiset_cpp_2.x[i]), Code05_Partition_Multiset_cpp_2.y[i])
            Code05_Partition_Multiset_cpp_2.addEdge(Code05_Partition_Multiset_cpp_2.other(Code05_Partition_Multiset_cpp_2.y[i]), Code05_Partition_Multiset_cpp_2.x[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_cpp_2.n):
            Code05_Partition_Multiset_cpp_2.link(i, Code05_Partition_Multiset_cpp_2.other(i), Code05_Partition_Multiset_cpp_2.small(jcast('int', (Code05_Partition_Multiset_cpp_2.v[i] - k))), Code05_Partition_Multiset_cpp_2.big(jcast('int', jadd(Code05_Partition_Multiset_cpp_2.v[i], k))))
            Code05_Partition_Multiset_cpp_2.add(i, Code05_Partition_Multiset_cpp_2.other(i), Code05_Partition_Multiset_cpp_2.rak[i], jcast('int', jadd(jcast('int', (Code05_Partition_Multiset_cpp_2.n - Code05_Partition_Multiset_cpp_2.rak[i])), 1)))
            i = jcast('int', (i + 1))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_cpp_2.cntt):
            jset(Code05_Partition_Multiset_cpp_2.head, i, jset(Code05_Partition_Multiset_cpp_2.dfn, i, jset(Code05_Partition_Multiset_cpp_2.belong, i, 0)))
            i = jcast('int', (i + 1))
        Code05_Partition_Multiset_cpp_2.cntt = jcast('int', jset(Code05_Partition_Multiset_cpp_2, 'cntg', jset(Code05_Partition_Multiset_cpp_2, 'cntd', jset(Code05_Partition_Multiset_cpp_2, 'top', jset(Code05_Partition_Multiset_cpp_2, 'sccCnt', jset(Code05_Partition_Multiset_cpp_2, 'curVersion', 0))))))

    @staticmethod
    def check(k):
        k = jcast('int', k)
        Code05_Partition_Multiset_cpp_2.buildGraph(k)
        i = jcast('int', 1)
        while (i <= jcast('int', (Code05_Partition_Multiset_cpp_2.n << (1 & 31)))):
            if (Code05_Partition_Multiset_cpp_2.dfn[i] == 0):
                # tarjan1(i);
                Code05_Partition_Multiset_cpp_2.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_cpp_2.n):
            try:
                if (Code05_Partition_Multiset_cpp_2.belong[i] == Code05_Partition_Multiset_cpp_2.belong[jcast('int', jadd(i, Code05_Partition_Multiset_cpp_2.n))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_34:
                if _java_control_34.label not in (None,):
                    raise
            except JBreak as _java_control_34:
                if _java_control_34.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        Code05_Partition_Multiset_cpp_2.clear()
        return jcast('boolean', check)

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_cpp_2.n):
            jset(Code05_Partition_Multiset_cpp_2.arr[i], 0, Code05_Partition_Multiset_cpp_2.v[i])
            jset(Code05_Partition_Multiset_cpp_2.arr[i], 1, i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Partition_Multiset_cpp_2.arr, 1, jcast('int', jadd(Code05_Partition_Multiset_cpp_2.n, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_cpp_2.n):
            jset(Code05_Partition_Multiset_cpp_2.rak, Code05_Partition_Multiset_cpp_2.arr[i][1], i)
            i = jcast('int', (i + 1))
        l = jcast('int', 0)
        r = jcast('int', Code05_Partition_Multiset_cpp_2.arr[Code05_Partition_Multiset_cpp_2.n][0])
        mid = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if Code05_Partition_Multiset_cpp_2.check(mid):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code05_Partition_Multiset_cpp_2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Partition_Multiset_cpp_2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Partition_Multiset_cpp_2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_cpp_2.n):
            jset(Code05_Partition_Multiset_cpp_2.v, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_cpp_2.m):
            jset(Code05_Partition_Multiset_cpp_2.x, i, jcall(in_, 'nextInt'))
            jset(Code05_Partition_Multiset_cpp_2.y, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        ans = jcast('int', Code05_Partition_Multiset_cpp_2.compute())
        jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_35 := self), (_java_key_36 := 'ptr'), (_java_old_37 := jget(_java_obj_35, _java_key_36)), jset(_java_obj_35, _java_key_36, jcast('int', (_java_old_37 + (1)))), _java_old_37)[4]])

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
            raise TypeError("No matching overload for Code05_Partition_Multiset_cpp_2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Partition_Multiset_cpp_2.MAXN = jcast('int', 20001)
Code05_Partition_Multiset_cpp_2.MAXM = jcast('int', 20001)
Code05_Partition_Multiset_cpp_2.MAXT = jcast('int', 2000001)
Code05_Partition_Multiset_cpp_2.MAXE = jcast('int', 5000001)
Code05_Partition_Multiset_cpp_2.n = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.m = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.cntt = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.v = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXN])
Code05_Partition_Multiset_cpp_2.x = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXM])
Code05_Partition_Multiset_cpp_2.y = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXM])
Code05_Partition_Multiset_cpp_2.rak = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXN])
Code05_Partition_Multiset_cpp_2.arr = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXN, 2])
Code05_Partition_Multiset_cpp_2.head = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.nxt = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXE])
Code05_Partition_Multiset_cpp_2.to = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXE])
Code05_Partition_Multiset_cpp_2.cntg = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.dfn = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.low = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.cntd = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.sta = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.top = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.belong = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.sccCnt = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.rootOut1 = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXN])
Code05_Partition_Multiset_cpp_2.rootIn1 = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXN])
Code05_Partition_Multiset_cpp_2.rootOut2 = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXN])
Code05_Partition_Multiset_cpp_2.rootIn2 = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXN])
Code05_Partition_Multiset_cpp_2.ls = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.rs = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.curVersion = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.stau = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.stas = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.stae = jarray('int', [Code05_Partition_Multiset_cpp_2.MAXT])
Code05_Partition_Multiset_cpp_2.u = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.status = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.e = jcast('int', 0)
Code05_Partition_Multiset_cpp_2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code05_Partition_Multiset_cpp_2.main([])
