# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 喵了个喵 II，主席树优化建图，Python版
# 给定一个长度为4n的数组arr，1~n每种数字都出现4次
# 从左到右把每个数字划分进序列0或序列1，要求划分出的两个序列完全相等
# 如果能做到，先打印"Yes"，然后从左到右打印每个位置划分进了什么序列
# 如果不能做到，打印"No"
# 1 <= n <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P9139
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Meow_II_java_2:
    __java_fields__ = {'MAXV': 'MAXV', 'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'v': 'v', 'n': 'n', 'cntt': 'cntt', 'vi': 'vi', 'group': 'group', 'cntp': 'cntp', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'rootOut': 'rootOut', 'rootIn': 'rootIn', 'ls': 'ls', 'rs': 'rs', 'ans': 'ans', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXV = 0
    MAXN = 0
    MAXT = 0
    MAXE = 0
    v = 0
    n = 0
    cntt = 0
    vi = None
    group = None
    cntp = 0
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
    rootOut = None
    rootIn = None
    ls = None
    rs = None
    ans = None
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
        Code06_Meow_II_java_2.stau[Code06_Meow_II_java_2.stacksize] = jcast('int', u)
        Code06_Meow_II_java_2.stas[Code06_Meow_II_java_2.stacksize] = jcast('int', status)
        Code06_Meow_II_java_2.stae[Code06_Meow_II_java_2.stacksize] = jcast('int', e)
        Code06_Meow_II_java_2.stacksize = jcast('int', (Code06_Meow_II_java_2.stacksize + 1))

    @staticmethod
    def pop():
        Code06_Meow_II_java_2.stacksize = jcast('int', (Code06_Meow_II_java_2.stacksize - 1))
        Code06_Meow_II_java_2.u = jcast('int', Code06_Meow_II_java_2.stau[Code06_Meow_II_java_2.stacksize])
        Code06_Meow_II_java_2.status = jcast('int', Code06_Meow_II_java_2.stas[Code06_Meow_II_java_2.stacksize])
        Code06_Meow_II_java_2.e = jcast('int', Code06_Meow_II_java_2.stae[Code06_Meow_II_java_2.stacksize])

    @staticmethod
    def addGroup(l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        jset(Code06_Meow_II_java_2.group[((_java_obj_1 := Code06_Meow_II_java_2), (_java_key_2 := 'cntp'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, l)
        jset(Code06_Meow_II_java_2.group[Code06_Meow_II_java_2.cntp], 1, r)
        jset(Code06_Meow_II_java_2.group[Code06_Meow_II_java_2.cntp], 2, x)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_Meow_II_java_2.nxt, ((_java_obj_4 := Code06_Meow_II_java_2), (_java_key_5 := 'cntg'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code06_Meow_II_java_2.head[u])
        Code06_Meow_II_java_2.to[Code06_Meow_II_java_2.cntg] = jcast('int', v)
        Code06_Meow_II_java_2.head[u] = jcast('int', Code06_Meow_II_java_2.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code06_Meow_II_java_2.dfn, u, jset(Code06_Meow_II_java_2.low, u, ((_java_obj_7 := Code06_Meow_II_java_2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code06_Meow_II_java_2.sta, ((_java_obj_10 := Code06_Meow_II_java_2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code06_Meow_II_java_2.head[u])
        while (e > 0):
            v = jcast('int', Code06_Meow_II_java_2.to[e])
            if (Code06_Meow_II_java_2.dfn[v] == 0):
                Code06_Meow_II_java_2.tarjan1(v)
                jset(Code06_Meow_II_java_2.low, u, jstatic('Math', 'min', Code06_Meow_II_java_2.low[u], Code06_Meow_II_java_2.low[v]))
            else:
                if (Code06_Meow_II_java_2.belong[v] == 0):
                    jset(Code06_Meow_II_java_2.low, u, jstatic('Math', 'min', Code06_Meow_II_java_2.low[u], Code06_Meow_II_java_2.dfn[v]))
            e = jcast('int', Code06_Meow_II_java_2.nxt[e])
        if (Code06_Meow_II_java_2.dfn[u] == Code06_Meow_II_java_2.low[u]):
            Code06_Meow_II_java_2.sccCnt = jcast('int', (Code06_Meow_II_java_2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code06_Meow_II_java_2.sta[((_java_obj_13 := Code06_Meow_II_java_2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                Code06_Meow_II_java_2.belong[pop] = jcast('int', Code06_Meow_II_java_2.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code06_Meow_II_java_2.stacksize = jcast('int', 0)
        Code06_Meow_II_java_2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code06_Meow_II_java_2.stacksize > 0):
            Code06_Meow_II_java_2.pop()
            if (Code06_Meow_II_java_2.status == jcast('int', (-1))):
                jset(Code06_Meow_II_java_2.dfn, Code06_Meow_II_java_2.u, jset(Code06_Meow_II_java_2.low, Code06_Meow_II_java_2.u, ((_java_obj_16 := Code06_Meow_II_java_2), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code06_Meow_II_java_2.sta, ((_java_obj_19 := Code06_Meow_II_java_2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code06_Meow_II_java_2.u)
                Code06_Meow_II_java_2.e = jcast('int', Code06_Meow_II_java_2.head[Code06_Meow_II_java_2.u])
            else:
                v = jcast('int', Code06_Meow_II_java_2.to[Code06_Meow_II_java_2.e])
                if (Code06_Meow_II_java_2.status == 0):
                    jset(Code06_Meow_II_java_2.low, Code06_Meow_II_java_2.u, jstatic('Math', 'min', Code06_Meow_II_java_2.low[Code06_Meow_II_java_2.u], Code06_Meow_II_java_2.low[v]))
                if ((Code06_Meow_II_java_2.status == 1) and (Code06_Meow_II_java_2.belong[v] == 0)):
                    jset(Code06_Meow_II_java_2.low, Code06_Meow_II_java_2.u, jstatic('Math', 'min', Code06_Meow_II_java_2.low[Code06_Meow_II_java_2.u], Code06_Meow_II_java_2.dfn[v]))
                Code06_Meow_II_java_2.e = jcast('int', Code06_Meow_II_java_2.nxt[Code06_Meow_II_java_2.e])
            if (Code06_Meow_II_java_2.e != 0):
                v = jcast('int', Code06_Meow_II_java_2.to[Code06_Meow_II_java_2.e])
                if (Code06_Meow_II_java_2.dfn[v] == 0):
                    Code06_Meow_II_java_2.push(Code06_Meow_II_java_2.u, 0, Code06_Meow_II_java_2.e)
                    Code06_Meow_II_java_2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code06_Meow_II_java_2.push(Code06_Meow_II_java_2.u, 1, Code06_Meow_II_java_2.e)
            else:
                if (Code06_Meow_II_java_2.dfn[Code06_Meow_II_java_2.u] == Code06_Meow_II_java_2.low[Code06_Meow_II_java_2.u]):
                    Code06_Meow_II_java_2.sccCnt = jcast('int', (Code06_Meow_II_java_2.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code06_Meow_II_java_2.sta[((_java_obj_22 := Code06_Meow_II_java_2), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                        Code06_Meow_II_java_2.belong[pop] = jcast('int', Code06_Meow_II_java_2.sccCnt)
                        if not ((pop != Code06_Meow_II_java_2.u)):
                            break

    @staticmethod
    def buildOut(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_25 := Code06_Meow_II_java_2), (_java_key_26 := 'cntt'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code06_Meow_II_java_2.ls, rt, Code06_Meow_II_java_2.buildOut(l, mid))
            jset(Code06_Meow_II_java_2.rs, rt, Code06_Meow_II_java_2.buildOut(jcast('int', jadd(mid, 1)), r))
            Code06_Meow_II_java_2.addEdge(Code06_Meow_II_java_2.ls[rt], rt)
            Code06_Meow_II_java_2.addEdge(Code06_Meow_II_java_2.rs[rt], rt)
        return jcast('int', rt)

    @staticmethod
    def buildIn(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_28 := Code06_Meow_II_java_2), (_java_key_29 := 'cntt'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3])
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code06_Meow_II_java_2.ls, rt, Code06_Meow_II_java_2.buildIn(l, mid))
            jset(Code06_Meow_II_java_2.rs, rt, Code06_Meow_II_java_2.buildIn(jcast('int', jadd(mid, 1)), r))
            Code06_Meow_II_java_2.addEdge(rt, Code06_Meow_II_java_2.ls[rt])
            Code06_Meow_II_java_2.addEdge(rt, Code06_Meow_II_java_2.rs[rt])
        return jcast('int', rt)

    @staticmethod
    def addOut(jobi, jobx, l, r, i):
        jobi = jcast('int', jobi)
        jobx = jcast('int', jobx)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_31 := Code06_Meow_II_java_2), (_java_key_32 := 'cntt'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))))[3])
        Code06_Meow_II_java_2.ls[rt] = jcast('int', Code06_Meow_II_java_2.ls[i])
        Code06_Meow_II_java_2.rs[rt] = jcast('int', Code06_Meow_II_java_2.rs[i])
        Code06_Meow_II_java_2.addEdge(i, rt)
        if (l == r):
            Code06_Meow_II_java_2.addEdge(jobx, rt)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code06_Meow_II_java_2.ls, rt, Code06_Meow_II_java_2.addOut(jobi, jobx, l, mid, Code06_Meow_II_java_2.ls[rt]))
                Code06_Meow_II_java_2.addEdge(Code06_Meow_II_java_2.ls[rt], rt)
            else:
                jset(Code06_Meow_II_java_2.rs, rt, Code06_Meow_II_java_2.addOut(jobi, jobx, jcast('int', jadd(mid, 1)), r, Code06_Meow_II_java_2.rs[rt]))
                Code06_Meow_II_java_2.addEdge(Code06_Meow_II_java_2.rs[rt], rt)
        return jcast('int', rt)

    @staticmethod
    def addIn(jobi, jobx, l, r, i):
        jobi = jcast('int', jobi)
        jobx = jcast('int', jobx)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_34 := Code06_Meow_II_java_2), (_java_key_35 := 'cntt'), (_java_old_36 := jget(_java_obj_34, _java_key_35)), jset(_java_obj_34, _java_key_35, jcast('int', (_java_old_36 + (1)))))[3])
        Code06_Meow_II_java_2.ls[rt] = jcast('int', Code06_Meow_II_java_2.ls[i])
        Code06_Meow_II_java_2.rs[rt] = jcast('int', Code06_Meow_II_java_2.rs[i])
        Code06_Meow_II_java_2.addEdge(rt, i)
        if (l == r):
            Code06_Meow_II_java_2.addEdge(rt, jobx)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code06_Meow_II_java_2.ls, rt, Code06_Meow_II_java_2.addIn(jobi, jobx, l, mid, Code06_Meow_II_java_2.ls[rt]))
                Code06_Meow_II_java_2.addEdge(rt, Code06_Meow_II_java_2.ls[rt])
            else:
                jset(Code06_Meow_II_java_2.rs, rt, Code06_Meow_II_java_2.addIn(jobi, jobx, jcast('int', jadd(mid, 1)), r, Code06_Meow_II_java_2.rs[rt]))
                Code06_Meow_II_java_2.addEdge(rt, Code06_Meow_II_java_2.rs[rt])
        return jcast('int', rt)

    @staticmethod
    def xToRange(jobx, jobl, jobr, l, r, i):
        jobx = jcast('int', jobx)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_Meow_II_java_2.addEdge(jobx, i)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code06_Meow_II_java_2.xToRange(jobx, jobl, jobr, l, mid, Code06_Meow_II_java_2.ls[i])
            if (jobr > mid):
                Code06_Meow_II_java_2.xToRange(jobx, jobl, jobr, jcast('int', jadd(mid, 1)), r, Code06_Meow_II_java_2.rs[i])

    @staticmethod
    def rangeToX(jobl, jobr, jobx, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_Meow_II_java_2.addEdge(i, jobx)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code06_Meow_II_java_2.rangeToX(jobl, jobr, jobx, l, mid, Code06_Meow_II_java_2.ls[i])
            if (jobr > mid):
                Code06_Meow_II_java_2.rangeToX(jobl, jobr, jobx, jcast('int', jadd(mid, 1)), r, Code06_Meow_II_java_2.rs[i])

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', jadd(x, Code06_Meow_II_java_2.v)) if (x <= Code06_Meow_II_java_2.v) else jcast('int', (x - Code06_Meow_II_java_2.v))))

    @staticmethod
    def buildGraph():
        jstatic('Arrays', 'sort', Code06_Meow_II_java_2.group, 1, jcast('int', jadd(Code06_Meow_II_java_2.cntp, 1)), (lambda a, b: (a[1] - b[1])))
        Code06_Meow_II_java_2.cntt = jcast('int', jcast('int', (Code06_Meow_II_java_2.v << (1 & 31))))
        jset(Code06_Meow_II_java_2.rootOut, 0, Code06_Meow_II_java_2.buildOut(1, Code06_Meow_II_java_2.n))
        jset(Code06_Meow_II_java_2.rootIn, 0, Code06_Meow_II_java_2.buildIn(1, Code06_Meow_II_java_2.n))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_java_2.cntp):
            l = jcast('int', Code06_Meow_II_java_2.group[i][0])
            r = jcast('int', Code06_Meow_II_java_2.group[i][1])
            x = jcast('int', Code06_Meow_II_java_2.group[i][2])
            Code06_Meow_II_java_2.xToRange(x, l, r, 1, Code06_Meow_II_java_2.n, Code06_Meow_II_java_2.rootIn[jcast('int', (i - 1))])
            Code06_Meow_II_java_2.rangeToX(l, r, Code06_Meow_II_java_2.other(x), 1, Code06_Meow_II_java_2.n, Code06_Meow_II_java_2.rootOut[jcast('int', (i - 1))])
            jset(Code06_Meow_II_java_2.rootIn, i, Code06_Meow_II_java_2.addIn(l, Code06_Meow_II_java_2.other(x), 1, Code06_Meow_II_java_2.n, Code06_Meow_II_java_2.rootIn[jcast('int', (i - 1))]))
            jset(Code06_Meow_II_java_2.rootOut, i, Code06_Meow_II_java_2.addOut(l, x, 1, Code06_Meow_II_java_2.n, Code06_Meow_II_java_2.rootOut[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code06_Meow_II_java_2.vi, 1, jcast('int', jadd(Code06_Meow_II_java_2.n, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_java_2.n):
            x = jcast('int', Code06_Meow_II_java_2.vi[i][0])
            a = jcast('int', Code06_Meow_II_java_2.vi[i][1])
            b = jcast('int', Code06_Meow_II_java_2.vi[jcast('int', jadd(i, 1))][1])
            c = jcast('int', Code06_Meow_II_java_2.vi[jcast('int', jadd(i, 2))][1])
            d = jcast('int', Code06_Meow_II_java_2.vi[jcast('int', jadd(i, 3))][1])
            Code06_Meow_II_java_2.addGroup(a, c, x)
            Code06_Meow_II_java_2.addGroup(b, d, x)
            Code06_Meow_II_java_2.addGroup(a, b, jcast('int', jadd(x, Code06_Meow_II_java_2.v)))
            Code06_Meow_II_java_2.addGroup(c, d, jcast('int', jadd(x, Code06_Meow_II_java_2.v)))
            i = jcast('int', jcast('int', jadd(i, 4)))
        Code06_Meow_II_java_2.buildGraph()
        i = jcast('int', 1)
        while (i <= jcast('int', (Code06_Meow_II_java_2.v << (1 & 31)))):
            if (Code06_Meow_II_java_2.dfn[i] == 0):
                # tarjan1(i);
                Code06_Meow_II_java_2.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_java_2.v):
            try:
                if (Code06_Meow_II_java_2.belong[i] == Code06_Meow_II_java_2.belong[jcast('int', jadd(i, Code06_Meow_II_java_2.v))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_37:
                if _java_control_37.label not in (None,):
                    raise
            except JBreak as _java_control_37:
                if _java_control_37.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if check:
            i = jcast('int', 1)
            while (i <= Code06_Meow_II_java_2.n):
                x = jcast('int', Code06_Meow_II_java_2.vi[i][0])
                a = jcast('int', Code06_Meow_II_java_2.vi[i][1])
                b = jcast('int', Code06_Meow_II_java_2.vi[jcast('int', jadd(i, 1))][1])
                c = jcast('int', Code06_Meow_II_java_2.vi[jcast('int', jadd(i, 2))][1])
                d = jcast('int', Code06_Meow_II_java_2.vi[jcast('int', jadd(i, 3))][1])
                if (Code06_Meow_II_java_2.belong[x] < Code06_Meow_II_java_2.belong[jcast('int', jadd(x, Code06_Meow_II_java_2.v))]):
                    Code06_Meow_II_java_2.ans[a] = jcast('int', 0)
                    Code06_Meow_II_java_2.ans[b] = jcast('int', 0)
                    Code06_Meow_II_java_2.ans[c] = jcast('int', 1)
                    Code06_Meow_II_java_2.ans[d] = jcast('int', 1)
                else:
                    Code06_Meow_II_java_2.ans[a] = jcast('int', 0)
                    Code06_Meow_II_java_2.ans[b] = jcast('int', 1)
                    Code06_Meow_II_java_2.ans[c] = jcast('int', 0)
                    Code06_Meow_II_java_2.ans[d] = jcast('int', 1)
                i = jcast('int', jcast('int', jadd(i, 4)))
        return jcast('boolean', check)

    @staticmethod
    def main(args):
        in_ = Code06_Meow_II_java_2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Meow_II_java_2.v = jcast('int', jcall(in_, 'nextInt'))
        Code06_Meow_II_java_2.n = jcast('int', jcast('int', (Code06_Meow_II_java_2.v << (2 & 31))))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_java_2.n):
            jset(Code06_Meow_II_java_2.vi[i], 0, jcall(in_, 'nextInt'))
            jset(Code06_Meow_II_java_2.vi[i], 1, i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code06_Meow_II_java_2.compute())
        if check:
            jcall(out, 'println', 'Yes')
            i = jcast('int', 1)
            while (i <= Code06_Meow_II_java_2.n):
                jcall(out, 'print', Code06_Meow_II_java_2.ans[i])
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', 'No')
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
            return jcast('int', self.buffer[((_java_obj_38 := self), (_java_key_39 := 'ptr'), (_java_old_40 := jget(_java_obj_38, _java_key_39)), jset(_java_obj_38, _java_key_39, jcast('int', (_java_old_40 + (1)))), _java_old_40)[4]])

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
            raise TypeError("No matching overload for Code06_Meow_II_java_2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Meow_II_java_2.MAXV = jcast('int', 50001)
Code06_Meow_II_java_2.MAXN = jcast('int', 200001)
Code06_Meow_II_java_2.MAXT = jcast('int', 10000001)
Code06_Meow_II_java_2.MAXE = jcast('int', 50000001)
Code06_Meow_II_java_2.v = jcast('int', 0)
Code06_Meow_II_java_2.n = jcast('int', 0)
Code06_Meow_II_java_2.cntt = jcast('int', 0)
Code06_Meow_II_java_2.vi = jarray('int', [Code06_Meow_II_java_2.MAXN, 2])
Code06_Meow_II_java_2.group = jarray('int', [Code06_Meow_II_java_2.MAXN, 3])
Code06_Meow_II_java_2.cntp = jcast('int', 0)
Code06_Meow_II_java_2.head = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.nxt = jarray('int', [Code06_Meow_II_java_2.MAXE])
Code06_Meow_II_java_2.to = jarray('int', [Code06_Meow_II_java_2.MAXE])
Code06_Meow_II_java_2.cntg = jcast('int', 0)
Code06_Meow_II_java_2.dfn = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.low = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.cntd = jcast('int', 0)
Code06_Meow_II_java_2.sta = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.top = jcast('int', 0)
Code06_Meow_II_java_2.belong = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.sccCnt = jcast('int', 0)
Code06_Meow_II_java_2.rootOut = jarray('int', [Code06_Meow_II_java_2.MAXN])
Code06_Meow_II_java_2.rootIn = jarray('int', [Code06_Meow_II_java_2.MAXN])
Code06_Meow_II_java_2.ls = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.rs = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.ans = jarray('int', [Code06_Meow_II_java_2.MAXN])
Code06_Meow_II_java_2.stau = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.stas = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.stae = jarray('int', [Code06_Meow_II_java_2.MAXT])
Code06_Meow_II_java_2.u = jcast('int', 0)
Code06_Meow_II_java_2.status = jcast('int', 0)
Code06_Meow_II_java_2.e = jcast('int', 0)
Code06_Meow_II_java_2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code06_Meow_II_java_2.main([])
