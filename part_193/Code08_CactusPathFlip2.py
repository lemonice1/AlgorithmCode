# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 仙人掌路径翻转，Python版
# 给定n个点、m条边的仙人掌图，没有自环，没有重边，1号节点是仙人掌的根
# 输入保证每个简单环的边数都为奇数，所以点x到根的最短路和最长路都是唯一的
# 以点x为头的子仙人掌，是指删掉根到x路径上的边后，包含x的连通块
# 每个节点只有黑白两种颜色，初始时所有节点为黑，一共有q条操作，类型如下
# 操作 1 x : 点x到根的最短路上所有节点，颜色翻转
# 操作 2 x : 点x到根的最长路上所有节点，颜色翻转
# 操作 3 x : 查询以点x为头的子仙人掌中，黑色节点的数量
# 1 <= n、m、q <= 5 * 10^4
# 测试链接 : https://uoj.ac/problem/158
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_CactusPathFlip2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'q': 'q', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'stasiz': 'stasiz', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'belongCycle': 'belongCycle', 'cycleRoot': 'cycleRoot', 'pos': 'pos', 'cycleSum': 'cycleSum', 'cyclel': 'cyclel', 'cycler': 'cycler', 'treel': 'treel', 'treer': 'treer', 'dfnType': 'dfnType', 'all1': 'all1', 'black1': 'black1', 'lazy1': 'lazy1', 'all2': 'all2', 'black2': 'black2', 'lazy2': 'lazy2', 'all3': 'all3', 'black3': 'black3', 'lazy3': 'lazy3'}
    MAXN = 0
    n = 0
    m = 0
    q = 0
    cntn = 0
    # 原图
    head1 = None
    next1 = None
    to1 = None
    cnt1 = 0
    # 圆方树
    head2 = None
    next2 = None
    to2 = None
    cnt2 = 0
    # tarjan算法
    dfn = None
    low = None
    cntd = 0
    sta = None
    stasiz = 0
    # 树链剖分
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    # 仙人掌中，一个节点可能是多个环的环顶，但不做环顶的话，最多参与一个环
    # belongCycle[x]，表示节点x归属的环，x不是环顶节点
    belongCycle = None
    # 环顶节点，只对方点有意义
    cycleRoot = None
    # 圆点在环中的位置
    pos = None
    # 环的边数
    cycleSum = None
    # 除了环顶和重儿子之外，环中圆点的dfn编号范围，只对方点有意义
    cyclel = None
    cycler = None
    # 子树上，所有后代节点的dfn编号范围，只对圆点有意义
    treel = None
    treer = None
    # dfnType[x] = 0，dfn序号为x的节点是方点
    # dfnType[x] = 1，dfn序号为x的节点是圆点，位于环顶到环中重儿子的短路径侧
    # dfnType[x] = 2，dfn序号为x的节点是圆点，位于环顶到环中重儿子的长路径侧
    # dfnType[x] = 3，dfn序号为x的节点是圆点，如果不是1或2类型，那就是3类型，表示必经点
    # 必经点的情况比较多，可能是环中重儿子 或者 只做环顶 或者 不参与任何环
    # 总之无论短路径还是长路径，通过重链向上必经的点，就算3类型
    dfnType = None
    # 短路径线段树
    all1 = None
    black1 = None
    lazy1 = None
    # 长路径线段树
    all2 = None
    black2 = None
    lazy2 = None
    # 必经点线段树
    all3 = None
    black3 = None
    lazy3 = None
    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_CactusPathFlip2.next1, ((_java_obj_1 := Code08_CactusPathFlip2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_CactusPathFlip2.head1[u])
        Code08_CactusPathFlip2.to1[Code08_CactusPathFlip2.cnt1] = jcast('int', v)
        Code08_CactusPathFlip2.head1[u] = jcast('int', Code08_CactusPathFlip2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_CactusPathFlip2.next2, ((_java_obj_4 := Code08_CactusPathFlip2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code08_CactusPathFlip2.head2[u])
        Code08_CactusPathFlip2.to2[Code08_CactusPathFlip2.cnt2] = jcast('int', v)
        Code08_CactusPathFlip2.head2[u] = jcast('int', Code08_CactusPathFlip2.cnt2)

    @staticmethod
    def cycleLink(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code08_CactusPathFlip2.cntn = jcast('int', (Code08_CactusPathFlip2.cntn + 1))
        Code08_CactusPathFlip2.cycleRoot[Code08_CactusPathFlip2.cntn] = jcast('int', u)
        Code08_CactusPathFlip2.addEdge2(u, Code08_CactusPathFlip2.cntn)
        tmp = jcast('int', Code08_CactusPathFlip2.stasiz)
        pop = 0
        cnt = jcast('int', 0)
        while True:
            pop = jcast('int', Code08_CactusPathFlip2.sta[((_java_old_7 := tmp), (tmp := jcast('int', (tmp + (-1)))), _java_old_7)[2]])
            cnt = jcast('int', (cnt + 1))
            if not ((pop != v)):
                break
        Code08_CactusPathFlip2.cycleSum[Code08_CactusPathFlip2.cntn] = jcast('int', jcast('int', jadd(cnt, 1)))
        while True:
            pop = jcast('int', Code08_CactusPathFlip2.sta[((_java_obj_8 := Code08_CactusPathFlip2), (_java_key_9 := 'stasiz'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))), _java_old_10)[4]])
            Code08_CactusPathFlip2.belongCycle[pop] = jcast('int', Code08_CactusPathFlip2.cntn)
            jset(Code08_CactusPathFlip2.pos, pop, ((_java_old_11 := cnt), (cnt := jcast('int', (cnt + (-1)))), _java_old_11)[2])
            Code08_CactusPathFlip2.addEdge2(Code08_CactusPathFlip2.cntn, pop)
            if not ((pop != v)):
                break

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code08_CactusPathFlip2.dfn, u, jset(Code08_CactusPathFlip2.low, u, ((_java_obj_12 := Code08_CactusPathFlip2), (_java_key_13 := 'cntd'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3]))
        jset(Code08_CactusPathFlip2.sta, ((_java_obj_15 := Code08_CactusPathFlip2), (_java_key_16 := 'stasiz'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))))[3], u)
        e = jcast('int', Code08_CactusPathFlip2.head1[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code08_CactusPathFlip2.to1[e])
                if (Code08_CactusPathFlip2.dfn[v] == 0):
                    Code08_CactusPathFlip2.tarjan(v, e)
                    if (Code08_CactusPathFlip2.low[v] < Code08_CactusPathFlip2.dfn[u]):
                        jset(Code08_CactusPathFlip2.low, u, jstatic('Math', 'min', Code08_CactusPathFlip2.low[u], Code08_CactusPathFlip2.low[v]))
                    else:
                        if (Code08_CactusPathFlip2.low[v] > Code08_CactusPathFlip2.dfn[u]):
                            Code08_CactusPathFlip2.stasiz = jcast('int', (Code08_CactusPathFlip2.stasiz - 1))
                            Code08_CactusPathFlip2.addEdge2(u, v)
                        else:
                            Code08_CactusPathFlip2.cycleLink(u, v)
                else:
                    if (Code08_CactusPathFlip2.dfn[v] < Code08_CactusPathFlip2.dfn[u]):
                        jset(Code08_CactusPathFlip2.low, u, jstatic('Math', 'min', Code08_CactusPathFlip2.low[u], Code08_CactusPathFlip2.dfn[v]))
            except JContinue as _java_control_18:
                if _java_control_18.label not in (None,):
                    raise
            except JBreak as _java_control_18:
                if _java_control_18.label not in (None,):
                    raise
                break
            e = jcast('int', Code08_CactusPathFlip2.next1[e])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code08_CactusPathFlip2.fa[u] = jcast('int', f)
        Code08_CactusPathFlip2.dep[u] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.dep[f], 1)))
        Code08_CactusPathFlip2.siz[u] = jcast('int', 1)
        e = jcast('int', Code08_CactusPathFlip2.head2[u])
        while (e > 0):
            v = jcast('int', Code08_CactusPathFlip2.to2[e])
            if (v != f):
                Code08_CactusPathFlip2.dfs1(v, u)
                Code08_CactusPathFlip2.siz[u] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.siz[u], Code08_CactusPathFlip2.siz[v])))
                if ((Code08_CactusPathFlip2.son[u] == 0) or (Code08_CactusPathFlip2.siz[Code08_CactusPathFlip2.son[u]] < Code08_CactusPathFlip2.siz[v])):
                    Code08_CactusPathFlip2.son[u] = jcast('int', v)
            e = jcast('int', Code08_CactusPathFlip2.next2[e])

    @staticmethod
    def cycleDfn(u):
        u = jcast('int', u)
        h = jcast('int', Code08_CactusPathFlip2.son[u])
        near = jcast('boolean', (jcast('int', (Code08_CactusPathFlip2.pos[h] * 2)) < Code08_CactusPathFlip2.cycleSum[u]))
        Code08_CactusPathFlip2.cyclel[u] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.cntd, 1)))
        e = jcast('int', Code08_CactusPathFlip2.head2[u])
        while (e > 0):
            v = jcast('int', Code08_CactusPathFlip2.to2[e])
            if ((v != Code08_CactusPathFlip2.fa[u]) and (v != h)):
                jset(Code08_CactusPathFlip2.dfn, v, ((_java_obj_19 := Code08_CactusPathFlip2), (_java_key_20 := 'cntd'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3])
                if ((near and (Code08_CactusPathFlip2.pos[v] < Code08_CactusPathFlip2.pos[h])) or ((not near) and (Code08_CactusPathFlip2.pos[v] > Code08_CactusPathFlip2.pos[h]))):
                    Code08_CactusPathFlip2.dfnType[Code08_CactusPathFlip2.cntd] = jcast('int', 1)
                else:
                    Code08_CactusPathFlip2.dfnType[Code08_CactusPathFlip2.cntd] = jcast('int', 2)
            e = jcast('int', Code08_CactusPathFlip2.next2[e])
        Code08_CactusPathFlip2.cycler[u] = jcast('int', Code08_CactusPathFlip2.cntd)
        jset(Code08_CactusPathFlip2.dfn, h, ((_java_obj_22 := Code08_CactusPathFlip2), (_java_key_23 := 'cntd'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code08_CactusPathFlip2.top[u] = jcast('int', t)
        if (Code08_CactusPathFlip2.dfn[u] == 0):
            jset(Code08_CactusPathFlip2.dfn, u, ((_java_obj_25 := Code08_CactusPathFlip2), (_java_key_26 := 'cntd'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
        if (u > Code08_CactusPathFlip2.n):
            Code08_CactusPathFlip2.cycleDfn(u)
        if (u <= Code08_CactusPathFlip2.n):
            Code08_CactusPathFlip2.treel[u] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.cntd, 1)))
        if (Code08_CactusPathFlip2.son[u] != 0):
            Code08_CactusPathFlip2.dfs2(Code08_CactusPathFlip2.son[u], t)
        e = jcast('int', Code08_CactusPathFlip2.head2[u])
        while (e > 0):
            v = jcast('int', Code08_CactusPathFlip2.to2[e])
            if ((v != Code08_CactusPathFlip2.fa[u]) and (v != Code08_CactusPathFlip2.son[u])):
                Code08_CactusPathFlip2.dfs2(v, v)
            e = jcast('int', Code08_CactusPathFlip2.next2[e])
        if (u <= Code08_CactusPathFlip2.n):
            Code08_CactusPathFlip2.treer[u] = jcast('int', Code08_CactusPathFlip2.cntd)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code08_CactusPathFlip2.all1[i] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.all1[jcast('int', (i << (1 & 31)))], Code08_CactusPathFlip2.all1[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        Code08_CactusPathFlip2.all2[i] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.all2[jcast('int', (i << (1 & 31)))], Code08_CactusPathFlip2.all2[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        Code08_CactusPathFlip2.all3[i] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.all3[jcast('int', (i << (1 & 31)))], Code08_CactusPathFlip2.all3[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        Code08_CactusPathFlip2.black1[i] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.black1[jcast('int', (i << (1 & 31)))], Code08_CactusPathFlip2.black1[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        Code08_CactusPathFlip2.black2[i] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.black2[jcast('int', (i << (1 & 31)))], Code08_CactusPathFlip2.black2[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        Code08_CactusPathFlip2.black3[i] = jcast('int', jcast('int', jadd(Code08_CactusPathFlip2.black3[jcast('int', (i << (1 & 31)))], Code08_CactusPathFlip2.black3[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def reverse1(i):
        i = jcast('int', i)
        Code08_CactusPathFlip2.black1[i] = jcast('int', jcast('int', (Code08_CactusPathFlip2.all1[i] - Code08_CactusPathFlip2.black1[i])))
        Code08_CactusPathFlip2.lazy1[i] = jcast('boolean', (not Code08_CactusPathFlip2.lazy1[i]))

    @staticmethod
    def reverse2(i):
        i = jcast('int', i)
        Code08_CactusPathFlip2.black2[i] = jcast('int', jcast('int', (Code08_CactusPathFlip2.all2[i] - Code08_CactusPathFlip2.black2[i])))
        Code08_CactusPathFlip2.lazy2[i] = jcast('boolean', (not Code08_CactusPathFlip2.lazy2[i]))

    @staticmethod
    def reverse3(i):
        i = jcast('int', i)
        Code08_CactusPathFlip2.black3[i] = jcast('int', jcast('int', (Code08_CactusPathFlip2.all3[i] - Code08_CactusPathFlip2.black3[i])))
        Code08_CactusPathFlip2.lazy3[i] = jcast('boolean', (not Code08_CactusPathFlip2.lazy3[i]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code08_CactusPathFlip2.lazy1[i]:
            Code08_CactusPathFlip2.reverse1(jcast('int', (i << (1 & 31))))
            Code08_CactusPathFlip2.reverse1(jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code08_CactusPathFlip2.lazy1[i] = jcast('boolean', False)
        if Code08_CactusPathFlip2.lazy2[i]:
            Code08_CactusPathFlip2.reverse2(jcast('int', (i << (1 & 31))))
            Code08_CactusPathFlip2.reverse2(jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code08_CactusPathFlip2.lazy2[i] = jcast('boolean', False)
        if Code08_CactusPathFlip2.lazy3[i]:
            Code08_CactusPathFlip2.reverse3(jcast('int', (i << (1 & 31))))
            Code08_CactusPathFlip2.reverse3(jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code08_CactusPathFlip2.lazy3[i] = jcast('boolean', False)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            if (Code08_CactusPathFlip2.dfnType[l] == 1):
                jset(Code08_CactusPathFlip2.all1, i, jset(Code08_CactusPathFlip2.black1, i, 1))
            if (Code08_CactusPathFlip2.dfnType[l] == 2):
                jset(Code08_CactusPathFlip2.all2, i, jset(Code08_CactusPathFlip2.black2, i, 1))
            if (Code08_CactusPathFlip2.dfnType[l] == 3):
                jset(Code08_CactusPathFlip2.all3, i, jset(Code08_CactusPathFlip2.black3, i, 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code08_CactusPathFlip2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code08_CactusPathFlip2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code08_CactusPathFlip2.up(i)

    @staticmethod
    def reverse(jobl, jobr, jobt, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobt = jcast('int', jobt)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobl > jobr):
            return
        if ((jobl <= l) and (r <= jobr)):
            if ((jobt == 1) or (jobt == 3)):
                Code08_CactusPathFlip2.reverse1(i)
            if ((jobt == 2) or (jobt == 3)):
                Code08_CactusPathFlip2.reverse2(i)
            Code08_CactusPathFlip2.reverse3(i)
            return
        Code08_CactusPathFlip2.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (jobl <= mid):
            Code08_CactusPathFlip2.reverse(jobl, jobr, jobt, l, mid, jcast('int', (i << (1 & 31))))
        if (mid < jobr):
            Code08_CactusPathFlip2.reverse(jobl, jobr, jobt, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code08_CactusPathFlip2.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobl > jobr):
            return jcast('int', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Code08_CactusPathFlip2.black1[i], Code08_CactusPathFlip2.black2[i])), Code08_CactusPathFlip2.black3[i])))
        Code08_CactusPathFlip2.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code08_CactusPathFlip2.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (mid < jobr):
            ans = jcast('int', jcast('int', jadd(ans, Code08_CactusPathFlip2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', ans)

    @staticmethod
    def flipCycle(u, x, op):
        u = jcast('int', u)
        x = jcast('int', x)
        op = jcast('int', op)
        h = jcast('int', Code08_CactusPathFlip2.son[u])
        near = jcast('boolean', (jcast('int', (Code08_CactusPathFlip2.pos[x] * 2)) < Code08_CactusPathFlip2.cycleSum[u]))
        if ((near and (op == 1)) or ((not near) and (op == 2))):
            Code08_CactusPathFlip2.reverse(Code08_CactusPathFlip2.cyclel[u], Code08_CactusPathFlip2.dfn[x], 3, 1, Code08_CactusPathFlip2.cntn, 1)
            if (Code08_CactusPathFlip2.pos[h] < Code08_CactusPathFlip2.pos[x]):
                Code08_CactusPathFlip2.reverse(Code08_CactusPathFlip2.dfn[h], Code08_CactusPathFlip2.dfn[h], 3, 1, Code08_CactusPathFlip2.cntn, 1)
        else:
            Code08_CactusPathFlip2.reverse(Code08_CactusPathFlip2.dfn[x], Code08_CactusPathFlip2.cycler[u], 3, 1, Code08_CactusPathFlip2.cntn, 1)
            if (Code08_CactusPathFlip2.pos[h] > Code08_CactusPathFlip2.pos[x]):
                Code08_CactusPathFlip2.reverse(Code08_CactusPathFlip2.dfn[h], Code08_CactusPathFlip2.dfn[h], 3, 1, Code08_CactusPathFlip2.cntn, 1)

    @staticmethod
    def flip(x, op):
        x = jcast('int', x)
        op = jcast('int', op)
        while (x != 0):
            xtop = jcast('int', Code08_CactusPathFlip2.top[x])
            if ((xtop > Code08_CactusPathFlip2.n) or (Code08_CactusPathFlip2.belongCycle[xtop] == 0)):
                Code08_CactusPathFlip2.reverse(Code08_CactusPathFlip2.dfn[xtop], Code08_CactusPathFlip2.dfn[x], op, 1, Code08_CactusPathFlip2.cntn, 1)
                x = jcast('int', Code08_CactusPathFlip2.fa[xtop])
            else:
                if (x != xtop):
                    Code08_CactusPathFlip2.reverse(Code08_CactusPathFlip2.dfn[Code08_CactusPathFlip2.son[xtop]], Code08_CactusPathFlip2.dfn[x], op, 1, Code08_CactusPathFlip2.cntn, 1)
                    x = jcast('int', xtop)
                Code08_CactusPathFlip2.flipCycle(Code08_CactusPathFlip2.belongCycle[x], x, op)
                x = jcast('int', Code08_CactusPathFlip2.cycleRoot[Code08_CactusPathFlip2.belongCycle[x]])

    @staticmethod
    def prepare():
        Code08_CactusPathFlip2.tarjan(1, 0)
        Code08_CactusPathFlip2.cntd = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code08_CactusPathFlip2.n):
            Code08_CactusPathFlip2.dfn[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code08_CactusPathFlip2.dfs1(1, 0)
        Code08_CactusPathFlip2.dfs2(1, 1)
        i = jcast('int', 1)
        while (i <= Code08_CactusPathFlip2.n):
            if (Code08_CactusPathFlip2.dfnType[Code08_CactusPathFlip2.dfn[i]] == 0):
                jset(Code08_CactusPathFlip2.dfnType, Code08_CactusPathFlip2.dfn[i], 3)
            i = jcast('int', (i + 1))
        Code08_CactusPathFlip2.build(1, Code08_CactusPathFlip2.cntn, 1)

    @staticmethod
    def main(args):
        in_ = Code08_CactusPathFlip2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_CactusPathFlip2.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_CactusPathFlip2.m = jcast('int', jcall(in_, 'nextInt'))
        Code08_CactusPathFlip2.q = jcast('int', jcall(in_, 'nextInt'))
        Code08_CactusPathFlip2.cntn = jcast('int', Code08_CactusPathFlip2.n)
        Code08_CactusPathFlip2.cnt1 = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code08_CactusPathFlip2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code08_CactusPathFlip2.addEdge1(u, v)
            Code08_CactusPathFlip2.addEdge1(v, u)
            i = jcast('int', (i + 1))
        Code08_CactusPathFlip2.prepare()
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= Code08_CactusPathFlip2.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            if ((op == 1) or (op == 2)):
                Code08_CactusPathFlip2.flip(x, op)
            else:
                ans = jcast('int', Code08_CactusPathFlip2.query(Code08_CactusPathFlip2.dfn[x], Code08_CactusPathFlip2.dfn[x], 1, Code08_CactusPathFlip2.cntn, 1))
                ans = jcast('int', jcast('int', jadd(ans, Code08_CactusPathFlip2.query(Code08_CactusPathFlip2.treel[x], Code08_CactusPathFlip2.treer[x], 1, Code08_CactusPathFlip2.cntn, 1))))
                jcall(out, 'println', ans)
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_28 := self), (_java_key_29 := 'ptr'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))), _java_old_30)[4]])

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
            raise TypeError("No matching overload for Code08_CactusPathFlip2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_CactusPathFlip2.MAXN = jcast('int', 100001)
Code08_CactusPathFlip2.n = jcast('int', 0)
Code08_CactusPathFlip2.m = jcast('int', 0)
Code08_CactusPathFlip2.q = jcast('int', 0)
Code08_CactusPathFlip2.cntn = jcast('int', 0)
Code08_CactusPathFlip2.head1 = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.next1 = jarray('int', [jcast('int', (Code08_CactusPathFlip2.MAXN << (1 & 31)))])
Code08_CactusPathFlip2.to1 = jarray('int', [jcast('int', (Code08_CactusPathFlip2.MAXN << (1 & 31)))])
Code08_CactusPathFlip2.cnt1 = jcast('int', 0)
Code08_CactusPathFlip2.head2 = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.next2 = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.to2 = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.cnt2 = jcast('int', 0)
Code08_CactusPathFlip2.dfn = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.low = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.cntd = jcast('int', 0)
Code08_CactusPathFlip2.sta = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.stasiz = jcast('int', 0)
Code08_CactusPathFlip2.fa = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.dep = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.siz = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.son = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.top = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.belongCycle = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.cycleRoot = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.pos = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.cycleSum = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.cyclel = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.cycler = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.treel = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.treer = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.dfnType = jarray('int', [Code08_CactusPathFlip2.MAXN])
Code08_CactusPathFlip2.all1 = jarray('int', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])
Code08_CactusPathFlip2.black1 = jarray('int', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])
Code08_CactusPathFlip2.lazy1 = jarray('boolean', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])
Code08_CactusPathFlip2.all2 = jarray('int', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])
Code08_CactusPathFlip2.black2 = jarray('int', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])
Code08_CactusPathFlip2.lazy2 = jarray('boolean', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])
Code08_CactusPathFlip2.all3 = jarray('int', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])
Code08_CactusPathFlip2.black3 = jarray('int', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])
Code08_CactusPathFlip2.lazy3 = jarray('boolean', [jcast('int', (Code08_CactusPathFlip2.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code08_CactusPathFlip2.main([])
