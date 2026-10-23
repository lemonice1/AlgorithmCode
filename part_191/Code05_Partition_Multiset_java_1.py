# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 划分可重集，树状数组优化建图，Python版
# 给定长度为n的数组arr，从左到右把每个数划分进可重集a、b
# 每个数至少要进入a或b中的一个
# arr[i]能进集合a的条件为，i左侧任何 <= arr[i] - k的数字，都没进集合a
# arr[i]能进集合b的条件为，i左侧任何 >= arr[i] + k的数字，都没进集合b
# 然后有m组关系，每组 x y，保证 x < y，表示两个位置的数不能进入同一个集合
# 如果不存在合法划分，打印-1，如果存在方案，打印能划分成功的最小k值
# n、m <= 2 * 10^4
# arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P7477
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Partition_Multiset_java_1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'm': 'm', 'cntt': 'cntt', 'v': 'v', 'x': 'x', 'y': 'y', 'rak': 'rak', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'outTree1': 'outTree1', 'inTree1': 'inTree1', 'outTree2': 'outTree2', 'inTree2': 'inTree2', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    # 树状数组
    outTree1 = None
    inTree1 = None
    outTree2 = None
    inTree2 = None
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
        Code05_Partition_Multiset_java_1.stau[Code05_Partition_Multiset_java_1.stacksize] = jcast('int', u)
        Code05_Partition_Multiset_java_1.stas[Code05_Partition_Multiset_java_1.stacksize] = jcast('int', status)
        Code05_Partition_Multiset_java_1.stae[Code05_Partition_Multiset_java_1.stacksize] = jcast('int', e)
        Code05_Partition_Multiset_java_1.stacksize = jcast('int', (Code05_Partition_Multiset_java_1.stacksize + 1))

    @staticmethod
    def pop():
        Code05_Partition_Multiset_java_1.stacksize = jcast('int', (Code05_Partition_Multiset_java_1.stacksize - 1))
        Code05_Partition_Multiset_java_1.u = jcast('int', Code05_Partition_Multiset_java_1.stau[Code05_Partition_Multiset_java_1.stacksize])
        Code05_Partition_Multiset_java_1.status = jcast('int', Code05_Partition_Multiset_java_1.stas[Code05_Partition_Multiset_java_1.stacksize])
        Code05_Partition_Multiset_java_1.e = jcast('int', Code05_Partition_Multiset_java_1.stae[Code05_Partition_Multiset_java_1.stacksize])

    # <= num的范围长度
    @staticmethod
    def small(num):
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', Code05_Partition_Multiset_java_1.n)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code05_Partition_Multiset_java_1.arr[mid][0] <= num):
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
        r = jcast('int', Code05_Partition_Multiset_java_1.n)
        mid = 0
        ans = jcast('int', jcast('int', jadd(Code05_Partition_Multiset_java_1.n, 1)))
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code05_Partition_Multiset_java_1.arr[mid][0] >= num):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', jcast('int', jadd(jcast('int', (Code05_Partition_Multiset_java_1.n - ans)), 1)))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Partition_Multiset_java_1.nxt, ((_java_obj_1 := Code05_Partition_Multiset_java_1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Partition_Multiset_java_1.head[u])
        Code05_Partition_Multiset_java_1.to[Code05_Partition_Multiset_java_1.cntg] = jcast('int', v)
        Code05_Partition_Multiset_java_1.head[u] = jcast('int', Code05_Partition_Multiset_java_1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code05_Partition_Multiset_java_1.dfn, u, jset(Code05_Partition_Multiset_java_1.low, u, ((_java_obj_4 := Code05_Partition_Multiset_java_1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code05_Partition_Multiset_java_1.sta, ((_java_obj_7 := Code05_Partition_Multiset_java_1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code05_Partition_Multiset_java_1.head[u])
        while (e > 0):
            v = jcast('int', Code05_Partition_Multiset_java_1.to[e])
            if (Code05_Partition_Multiset_java_1.dfn[v] == 0):
                Code05_Partition_Multiset_java_1.tarjan1(v)
                jset(Code05_Partition_Multiset_java_1.low, u, jstatic('Math', 'min', Code05_Partition_Multiset_java_1.low[u], Code05_Partition_Multiset_java_1.low[v]))
            else:
                if (Code05_Partition_Multiset_java_1.belong[v] == 0):
                    jset(Code05_Partition_Multiset_java_1.low, u, jstatic('Math', 'min', Code05_Partition_Multiset_java_1.low[u], Code05_Partition_Multiset_java_1.dfn[v]))
            e = jcast('int', Code05_Partition_Multiset_java_1.nxt[e])
        if (Code05_Partition_Multiset_java_1.dfn[u] == Code05_Partition_Multiset_java_1.low[u]):
            Code05_Partition_Multiset_java_1.sccCnt = jcast('int', (Code05_Partition_Multiset_java_1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code05_Partition_Multiset_java_1.sta[((_java_obj_10 := Code05_Partition_Multiset_java_1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code05_Partition_Multiset_java_1.belong[pop] = jcast('int', Code05_Partition_Multiset_java_1.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code05_Partition_Multiset_java_1.stacksize = jcast('int', 0)
        Code05_Partition_Multiset_java_1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_Partition_Multiset_java_1.stacksize > 0):
            Code05_Partition_Multiset_java_1.pop()
            if (Code05_Partition_Multiset_java_1.status == jcast('int', (-1))):
                jset(Code05_Partition_Multiset_java_1.dfn, Code05_Partition_Multiset_java_1.u, jset(Code05_Partition_Multiset_java_1.low, Code05_Partition_Multiset_java_1.u, ((_java_obj_13 := Code05_Partition_Multiset_java_1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code05_Partition_Multiset_java_1.sta, ((_java_obj_16 := Code05_Partition_Multiset_java_1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code05_Partition_Multiset_java_1.u)
                Code05_Partition_Multiset_java_1.e = jcast('int', Code05_Partition_Multiset_java_1.head[Code05_Partition_Multiset_java_1.u])
            else:
                v = jcast('int', Code05_Partition_Multiset_java_1.to[Code05_Partition_Multiset_java_1.e])
                if (Code05_Partition_Multiset_java_1.status == 0):
                    jset(Code05_Partition_Multiset_java_1.low, Code05_Partition_Multiset_java_1.u, jstatic('Math', 'min', Code05_Partition_Multiset_java_1.low[Code05_Partition_Multiset_java_1.u], Code05_Partition_Multiset_java_1.low[v]))
                if ((Code05_Partition_Multiset_java_1.status == 1) and (Code05_Partition_Multiset_java_1.belong[v] == 0)):
                    jset(Code05_Partition_Multiset_java_1.low, Code05_Partition_Multiset_java_1.u, jstatic('Math', 'min', Code05_Partition_Multiset_java_1.low[Code05_Partition_Multiset_java_1.u], Code05_Partition_Multiset_java_1.dfn[v]))
                Code05_Partition_Multiset_java_1.e = jcast('int', Code05_Partition_Multiset_java_1.nxt[Code05_Partition_Multiset_java_1.e])
            if (Code05_Partition_Multiset_java_1.e != 0):
                v = jcast('int', Code05_Partition_Multiset_java_1.to[Code05_Partition_Multiset_java_1.e])
                if (Code05_Partition_Multiset_java_1.dfn[v] == 0):
                    Code05_Partition_Multiset_java_1.push(Code05_Partition_Multiset_java_1.u, 0, Code05_Partition_Multiset_java_1.e)
                    Code05_Partition_Multiset_java_1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_Partition_Multiset_java_1.push(Code05_Partition_Multiset_java_1.u, 1, Code05_Partition_Multiset_java_1.e)
            else:
                if (Code05_Partition_Multiset_java_1.dfn[Code05_Partition_Multiset_java_1.u] == Code05_Partition_Multiset_java_1.low[Code05_Partition_Multiset_java_1.u]):
                    Code05_Partition_Multiset_java_1.sccCnt = jcast('int', (Code05_Partition_Multiset_java_1.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code05_Partition_Multiset_java_1.sta[((_java_obj_19 := Code05_Partition_Multiset_java_1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code05_Partition_Multiset_java_1.belong[pop] = jcast('int', Code05_Partition_Multiset_java_1.sccCnt)
                        if not ((pop != Code05_Partition_Multiset_java_1.u)):
                            break

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def addOut(outTree, i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        while (i <= Code05_Partition_Multiset_java_1.n):
            preo = jcast('int', outTree[i])
            curo = jcast('int', ((_java_obj_22 := Code05_Partition_Multiset_java_1), (_java_key_23 := 'cntt'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3])
            if (preo > 0):
                Code05_Partition_Multiset_java_1.addEdge(preo, curo)
            Code05_Partition_Multiset_java_1.addEdge(x, curo)
            outTree[i] = jcast('int', curo)
            i = jcast('int', jcast('int', jadd(i, Code05_Partition_Multiset_java_1.lowbit(i))))

    @staticmethod
    def addIn(inTree, i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        while (i <= Code05_Partition_Multiset_java_1.n):
            prei = jcast('int', inTree[i])
            curi = jcast('int', ((_java_obj_25 := Code05_Partition_Multiset_java_1), (_java_key_26 := 'cntt'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
            if (prei > 0):
                Code05_Partition_Multiset_java_1.addEdge(curi, prei)
            Code05_Partition_Multiset_java_1.addEdge(curi, x)
            inTree[i] = jcast('int', curi)
            i = jcast('int', jcast('int', jadd(i, Code05_Partition_Multiset_java_1.lowbit(i))))

    @staticmethod
    def rangeToX(outTree, i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        while (i > 0):
            if (outTree[i] > 0):
                Code05_Partition_Multiset_java_1.addEdge(outTree[i], x)
            i = jcast('int', jcast('int', (i - Code05_Partition_Multiset_java_1.lowbit(i))))

    @staticmethod
    def xToRange(inTree, x, i):
        x = jcast('int', x)
        i = jcast('int', i)
        while (i > 0):
            if (inTree[i] > 0):
                Code05_Partition_Multiset_java_1.addEdge(x, inTree[i])
            i = jcast('int', jcast('int', (i - Code05_Partition_Multiset_java_1.lowbit(i))))

    @staticmethod
    def add(x, otherx, si, bi):
        x = jcast('int', x)
        otherx = jcast('int', otherx)
        si = jcast('int', si)
        bi = jcast('int', bi)
        Code05_Partition_Multiset_java_1.addOut(Code05_Partition_Multiset_java_1.outTree1, si, x)
        Code05_Partition_Multiset_java_1.addIn(Code05_Partition_Multiset_java_1.inTree1, si, otherx)
        Code05_Partition_Multiset_java_1.addOut(Code05_Partition_Multiset_java_1.outTree2, bi, otherx)
        Code05_Partition_Multiset_java_1.addIn(Code05_Partition_Multiset_java_1.inTree2, bi, x)

    @staticmethod
    def link(x, otherx, lowCnt, highCnt):
        x = jcast('int', x)
        otherx = jcast('int', otherx)
        lowCnt = jcast('int', lowCnt)
        highCnt = jcast('int', highCnt)
        Code05_Partition_Multiset_java_1.xToRange(Code05_Partition_Multiset_java_1.inTree1, x, lowCnt)
        Code05_Partition_Multiset_java_1.rangeToX(Code05_Partition_Multiset_java_1.outTree1, lowCnt, otherx)
        Code05_Partition_Multiset_java_1.xToRange(Code05_Partition_Multiset_java_1.inTree2, otherx, highCnt)
        Code05_Partition_Multiset_java_1.rangeToX(Code05_Partition_Multiset_java_1.outTree2, highCnt, x)

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', jadd(x, Code05_Partition_Multiset_java_1.n)) if (x <= Code05_Partition_Multiset_java_1.n) else jcast('int', (x - Code05_Partition_Multiset_java_1.n))))

    @staticmethod
    def buildGraph(k):
        k = jcast('int', k)
        Code05_Partition_Multiset_java_1.cntt = jcast('int', jcast('int', (Code05_Partition_Multiset_java_1.n << (1 & 31))))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.m):
            Code05_Partition_Multiset_java_1.addEdge(Code05_Partition_Multiset_java_1.x[i], Code05_Partition_Multiset_java_1.other(Code05_Partition_Multiset_java_1.y[i]))
            Code05_Partition_Multiset_java_1.addEdge(Code05_Partition_Multiset_java_1.y[i], Code05_Partition_Multiset_java_1.other(Code05_Partition_Multiset_java_1.x[i]))
            Code05_Partition_Multiset_java_1.addEdge(Code05_Partition_Multiset_java_1.other(Code05_Partition_Multiset_java_1.x[i]), Code05_Partition_Multiset_java_1.y[i])
            Code05_Partition_Multiset_java_1.addEdge(Code05_Partition_Multiset_java_1.other(Code05_Partition_Multiset_java_1.y[i]), Code05_Partition_Multiset_java_1.x[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.n):
            Code05_Partition_Multiset_java_1.link(i, Code05_Partition_Multiset_java_1.other(i), Code05_Partition_Multiset_java_1.small(jcast('int', (Code05_Partition_Multiset_java_1.v[i] - k))), Code05_Partition_Multiset_java_1.big(jcast('int', jadd(Code05_Partition_Multiset_java_1.v[i], k))))
            Code05_Partition_Multiset_java_1.add(i, Code05_Partition_Multiset_java_1.other(i), Code05_Partition_Multiset_java_1.rak[i], jcast('int', jadd(jcast('int', (Code05_Partition_Multiset_java_1.n - Code05_Partition_Multiset_java_1.rak[i])), 1)))
            i = jcast('int', (i + 1))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.cntt):
            jset(Code05_Partition_Multiset_java_1.head, i, jset(Code05_Partition_Multiset_java_1.dfn, i, jset(Code05_Partition_Multiset_java_1.belong, i, 0)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.n):
            jset(Code05_Partition_Multiset_java_1.inTree1, i, jset(Code05_Partition_Multiset_java_1.outTree1, i, jset(Code05_Partition_Multiset_java_1.inTree2, i, jset(Code05_Partition_Multiset_java_1.outTree2, i, 0))))
            i = jcast('int', (i + 1))
        Code05_Partition_Multiset_java_1.cntt = jcast('int', jset(Code05_Partition_Multiset_java_1, 'cntg', jset(Code05_Partition_Multiset_java_1, 'cntd', jset(Code05_Partition_Multiset_java_1, 'top', jset(Code05_Partition_Multiset_java_1, 'sccCnt', 0)))))

    @staticmethod
    def check(k):
        k = jcast('int', k)
        Code05_Partition_Multiset_java_1.buildGraph(k)
        i = jcast('int', 1)
        while (i <= jcast('int', (Code05_Partition_Multiset_java_1.n << (1 & 31)))):
            if (Code05_Partition_Multiset_java_1.dfn[i] == 0):
                # tarjan1(i);
                Code05_Partition_Multiset_java_1.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.n):
            try:
                if (Code05_Partition_Multiset_java_1.belong[i] == Code05_Partition_Multiset_java_1.belong[jcast('int', jadd(i, Code05_Partition_Multiset_java_1.n))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_28:
                if _java_control_28.label not in (None,):
                    raise
            except JBreak as _java_control_28:
                if _java_control_28.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        Code05_Partition_Multiset_java_1.clear()
        return jcast('boolean', check)

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.n):
            jset(Code05_Partition_Multiset_java_1.arr[i], 0, Code05_Partition_Multiset_java_1.v[i])
            jset(Code05_Partition_Multiset_java_1.arr[i], 1, i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Partition_Multiset_java_1.arr, 1, jcast('int', jadd(Code05_Partition_Multiset_java_1.n, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.n):
            jset(Code05_Partition_Multiset_java_1.rak, Code05_Partition_Multiset_java_1.arr[i][1], i)
            i = jcast('int', (i + 1))
        l = jcast('int', 0)
        r = jcast('int', Code05_Partition_Multiset_java_1.arr[Code05_Partition_Multiset_java_1.n][0])
        mid = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if Code05_Partition_Multiset_java_1.check(mid):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code05_Partition_Multiset_java_1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Partition_Multiset_java_1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Partition_Multiset_java_1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.n):
            jset(Code05_Partition_Multiset_java_1.v, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Partition_Multiset_java_1.m):
            jset(Code05_Partition_Multiset_java_1.x, i, jcall(in_, 'nextInt'))
            jset(Code05_Partition_Multiset_java_1.y, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        ans = jcast('int', Code05_Partition_Multiset_java_1.compute())
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
            return jcast('int', self.buffer[((_java_obj_29 := self), (_java_key_30 := 'ptr'), (_java_old_31 := jget(_java_obj_29, _java_key_30)), jset(_java_obj_29, _java_key_30, jcast('int', (_java_old_31 + (1)))), _java_old_31)[4]])

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
            raise TypeError("No matching overload for Code05_Partition_Multiset_java_1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Partition_Multiset_java_1.MAXN = jcast('int', 20001)
Code05_Partition_Multiset_java_1.MAXM = jcast('int', 20001)
Code05_Partition_Multiset_java_1.MAXT = jcast('int', 1000001)
Code05_Partition_Multiset_java_1.MAXE = jcast('int', 2000001)
Code05_Partition_Multiset_java_1.n = jcast('int', 0)
Code05_Partition_Multiset_java_1.m = jcast('int', 0)
Code05_Partition_Multiset_java_1.cntt = jcast('int', 0)
Code05_Partition_Multiset_java_1.v = jarray('int', [Code05_Partition_Multiset_java_1.MAXN])
Code05_Partition_Multiset_java_1.x = jarray('int', [Code05_Partition_Multiset_java_1.MAXM])
Code05_Partition_Multiset_java_1.y = jarray('int', [Code05_Partition_Multiset_java_1.MAXM])
Code05_Partition_Multiset_java_1.rak = jarray('int', [Code05_Partition_Multiset_java_1.MAXN])
Code05_Partition_Multiset_java_1.arr = jarray('int', [Code05_Partition_Multiset_java_1.MAXN, 2])
Code05_Partition_Multiset_java_1.head = jarray('int', [Code05_Partition_Multiset_java_1.MAXT])
Code05_Partition_Multiset_java_1.nxt = jarray('int', [Code05_Partition_Multiset_java_1.MAXE])
Code05_Partition_Multiset_java_1.to = jarray('int', [Code05_Partition_Multiset_java_1.MAXE])
Code05_Partition_Multiset_java_1.cntg = jcast('int', 0)
Code05_Partition_Multiset_java_1.dfn = jarray('int', [Code05_Partition_Multiset_java_1.MAXT])
Code05_Partition_Multiset_java_1.low = jarray('int', [Code05_Partition_Multiset_java_1.MAXT])
Code05_Partition_Multiset_java_1.cntd = jcast('int', 0)
Code05_Partition_Multiset_java_1.sta = jarray('int', [Code05_Partition_Multiset_java_1.MAXT])
Code05_Partition_Multiset_java_1.top = jcast('int', 0)
Code05_Partition_Multiset_java_1.belong = jarray('int', [Code05_Partition_Multiset_java_1.MAXT])
Code05_Partition_Multiset_java_1.sccCnt = jcast('int', 0)
Code05_Partition_Multiset_java_1.outTree1 = jarray('int', [Code05_Partition_Multiset_java_1.MAXN])
Code05_Partition_Multiset_java_1.inTree1 = jarray('int', [Code05_Partition_Multiset_java_1.MAXN])
Code05_Partition_Multiset_java_1.outTree2 = jarray('int', [Code05_Partition_Multiset_java_1.MAXN])
Code05_Partition_Multiset_java_1.inTree2 = jarray('int', [Code05_Partition_Multiset_java_1.MAXN])
Code05_Partition_Multiset_java_1.stau = jarray('int', [Code05_Partition_Multiset_java_1.MAXT])
Code05_Partition_Multiset_java_1.stas = jarray('int', [Code05_Partition_Multiset_java_1.MAXT])
Code05_Partition_Multiset_java_1.stae = jarray('int', [Code05_Partition_Multiset_java_1.MAXT])
Code05_Partition_Multiset_java_1.u = jcast('int', 0)
Code05_Partition_Multiset_java_1.status = jcast('int', 0)
Code05_Partition_Multiset_java_1.e = jcast('int', 0)
Code05_Partition_Multiset_java_1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code05_Partition_Multiset_java_1.main([])
