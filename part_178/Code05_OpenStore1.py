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

# 开店，Python版
# 一共n个人，每个人有年龄，给定n-1条路，每条路有距离，路把人连成一棵树
# 一共m条查询，格式 u l r : 查询年龄范围[l, r]的所有人，到第u号人的距离总和
# 1 <= n <= 1.5 * 10^5    1 <= m <= 2 * 10^5
# 0 <= 年龄值 <= 10^9      1 <= 距离值 <= 1000
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P3241
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_OpenStore1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'n': 'n', 'm': 'm', 'A': 'A', 'age': 'age', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dist': 'dist', 'vis': 'vis', 'centfa': 'centfa', 'curl': 'curl', 'curr': 'curr', 'curAge': 'curAge', 'curSum': 'curSum', 'cntc': 'cntc', 'fal': 'fal', 'far': 'far', 'faAge': 'faAge', 'faSum': 'faSum', 'cntf': 'cntf', 'stack': 'stack', 'u': 'u', 'f': 'f', 'a': 'a', 'b': 'b', 'e': 'e', 'stacksize': 'stacksize', 'nodeCnt': 'nodeCnt', 'pathSum': 'pathSum'}
    MAXN = 0
    MAXK = 0
    n = 0
    m = 0
    A = 0
    age = None
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    dist = None
    vis = None
    centfa = None
    # cur列表(年龄，到当前重心距离)
    curl = None
    curr = None
    curAge = None
    curSum = None
    cntc = 0
    # fa列表(年龄，到上级重心距离)
    fal = None
    far = None
    faAge = None
    faSum = None
    cntf = 0
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    a = 0
    b = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, a, b, e):
        u = jcast('int', u)
        f = jcast('int', f)
        a = jcast('int', a)
        b = jcast('int', b)
        e = jcast('int', e)
        jset(Code05_OpenStore1.stack[Code05_OpenStore1.stacksize], 0, u)
        jset(Code05_OpenStore1.stack[Code05_OpenStore1.stacksize], 1, f)
        jset(Code05_OpenStore1.stack[Code05_OpenStore1.stacksize], 2, a)
        jset(Code05_OpenStore1.stack[Code05_OpenStore1.stacksize], 3, b)
        jset(Code05_OpenStore1.stack[Code05_OpenStore1.stacksize], 4, e)
        Code05_OpenStore1.stacksize = jcast('int', (Code05_OpenStore1.stacksize + 1))

    @staticmethod
    def pop():
        Code05_OpenStore1.stacksize = jcast('int', (Code05_OpenStore1.stacksize - 1))
        Code05_OpenStore1.u = jcast('int', Code05_OpenStore1.stack[Code05_OpenStore1.stacksize][0])
        Code05_OpenStore1.f = jcast('int', Code05_OpenStore1.stack[Code05_OpenStore1.stacksize][1])
        Code05_OpenStore1.a = jcast('int', Code05_OpenStore1.stack[Code05_OpenStore1.stacksize][2])
        Code05_OpenStore1.b = jcast('int', Code05_OpenStore1.stack[Code05_OpenStore1.stacksize][3])
        Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.stack[Code05_OpenStore1.stacksize][4])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code05_OpenStore1.nxt, ((_java_obj_1 := Code05_OpenStore1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_OpenStore1.head[u])
        Code05_OpenStore1.to[Code05_OpenStore1.cntg] = jcast('int', v)
        Code05_OpenStore1.weight[Code05_OpenStore1.cntg] = jcast('int', w)
        Code05_OpenStore1.head[u] = jcast('int', Code05_OpenStore1.cntg)

    @staticmethod
    def dfs1(u, f, dis):
        u = jcast('int', u)
        f = jcast('int', f)
        dis = jcast('int', dis)
        Code05_OpenStore1.fa[u] = jcast('int', f)
        Code05_OpenStore1.dep[u] = jcast('int', jcast('int', jadd(Code05_OpenStore1.dep[f], 1)))
        Code05_OpenStore1.dist[u] = jcast('int', dis)
        Code05_OpenStore1.siz[u] = jcast('int', 1)
        e = jcast('int', Code05_OpenStore1.head[u])
        while (e > 0):
            v = jcast('int', Code05_OpenStore1.to[e])
            w = jcast('int', Code05_OpenStore1.weight[e])
            if (v != f):
                Code05_OpenStore1.dfs1(v, u, jcast('int', jadd(dis, w)))
            e = jcast('int', Code05_OpenStore1.nxt[e])
        ei = jcast('int', Code05_OpenStore1.head[u])
        v = 0
        while (ei > 0):
            v = jcast('int', Code05_OpenStore1.to[ei])
            if (v != f):
                Code05_OpenStore1.siz[u] = jcast('int', jcast('int', jadd(Code05_OpenStore1.siz[u], Code05_OpenStore1.siz[v])))
                if ((Code05_OpenStore1.son[u] == 0) or (Code05_OpenStore1.siz[Code05_OpenStore1.son[u]] < Code05_OpenStore1.siz[v])):
                    Code05_OpenStore1.son[u] = jcast('int', v)
            ei = jcast('int', Code05_OpenStore1.nxt[ei])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code05_OpenStore1.top[u] = jcast('int', t)
        if (Code05_OpenStore1.son[u] == 0):
            return
        Code05_OpenStore1.dfs2(Code05_OpenStore1.son[u], t)
        e = jcast('int', Code05_OpenStore1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_OpenStore1.to[e])
            if ((v != Code05_OpenStore1.fa[u]) and (v != Code05_OpenStore1.son[u])):
                Code05_OpenStore1.dfs2(v, v)
            e = jcast('int', Code05_OpenStore1.nxt[e])

    @staticmethod
    def dfs3(cur, father, distance):
        cur = jcast('int', cur)
        father = jcast('int', father)
        distance = jcast('int', distance)
        Code05_OpenStore1.stacksize = jcast('int', 0)
        Code05_OpenStore1.push(cur, father, distance, 0, jcast('int', (-1)))
        while (Code05_OpenStore1.stacksize > 0):
            Code05_OpenStore1.pop()
            if (Code05_OpenStore1.e == jcast('int', (-1))):
                Code05_OpenStore1.fa[Code05_OpenStore1.u] = jcast('int', Code05_OpenStore1.f)
                Code05_OpenStore1.dep[Code05_OpenStore1.u] = jcast('int', jcast('int', jadd(Code05_OpenStore1.dep[Code05_OpenStore1.f], 1)))
                Code05_OpenStore1.dist[Code05_OpenStore1.u] = jcast('int', Code05_OpenStore1.a)
                Code05_OpenStore1.siz[Code05_OpenStore1.u] = jcast('int', 1)
                Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.head[Code05_OpenStore1.u])
            else:
                Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.nxt[Code05_OpenStore1.e])
            if (Code05_OpenStore1.e != 0):
                Code05_OpenStore1.push(Code05_OpenStore1.u, Code05_OpenStore1.f, Code05_OpenStore1.a, 0, Code05_OpenStore1.e)
                v = jcast('int', Code05_OpenStore1.to[Code05_OpenStore1.e])
                w = jcast('int', Code05_OpenStore1.weight[Code05_OpenStore1.e])
                if (v != Code05_OpenStore1.f):
                    Code05_OpenStore1.push(v, Code05_OpenStore1.u, jcast('int', jadd(Code05_OpenStore1.a, w)), 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code05_OpenStore1.head[Code05_OpenStore1.u])
                while (ei > 0):
                    v = jcast('int', Code05_OpenStore1.to[ei])
                    if (v != Code05_OpenStore1.f):
                        Code05_OpenStore1.siz[Code05_OpenStore1.u] = jcast('int', jcast('int', jadd(Code05_OpenStore1.siz[Code05_OpenStore1.u], Code05_OpenStore1.siz[v])))
                        if ((Code05_OpenStore1.son[Code05_OpenStore1.u] == 0) or (Code05_OpenStore1.siz[Code05_OpenStore1.son[Code05_OpenStore1.u]] < Code05_OpenStore1.siz[v])):
                            Code05_OpenStore1.son[Code05_OpenStore1.u] = jcast('int', v)
                    ei = jcast('int', Code05_OpenStore1.nxt[ei])

    @staticmethod
    def dfs4(cur, tag):
        cur = jcast('int', cur)
        tag = jcast('int', tag)
        Code05_OpenStore1.stacksize = jcast('int', 0)
        Code05_OpenStore1.push(cur, 0, 0, tag, jcast('int', (-1)))
        while (Code05_OpenStore1.stacksize > 0):
            try:
                Code05_OpenStore1.pop()
                if (Code05_OpenStore1.e == jcast('int', (-1))):
                    Code05_OpenStore1.top[Code05_OpenStore1.u] = jcast('int', Code05_OpenStore1.b)
                    if (Code05_OpenStore1.son[Code05_OpenStore1.u] == 0):
                        raise JContinue(None)
                    Code05_OpenStore1.push(Code05_OpenStore1.u, 0, 0, Code05_OpenStore1.b, jcast('int', (-2)))
                    Code05_OpenStore1.push(Code05_OpenStore1.son[Code05_OpenStore1.u], 0, 0, Code05_OpenStore1.b, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code05_OpenStore1.e == jcast('int', (-2))):
                        Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.head[Code05_OpenStore1.u])
                    else:
                        Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.nxt[Code05_OpenStore1.e])
                if (Code05_OpenStore1.e != 0):
                    Code05_OpenStore1.push(Code05_OpenStore1.u, 0, 0, Code05_OpenStore1.b, Code05_OpenStore1.e)
                    v = jcast('int', Code05_OpenStore1.to[Code05_OpenStore1.e])
                    if ((v != Code05_OpenStore1.fa[Code05_OpenStore1.u]) and (v != Code05_OpenStore1.son[Code05_OpenStore1.u])):
                        Code05_OpenStore1.push(v, 0, 0, v, jcast('int', (-1)))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        while (Code05_OpenStore1.top[a] != Code05_OpenStore1.top[b]):
            if (Code05_OpenStore1.dep[Code05_OpenStore1.top[a]] <= Code05_OpenStore1.dep[Code05_OpenStore1.top[b]]):
                b = jcast('int', Code05_OpenStore1.fa[Code05_OpenStore1.top[b]])
            else:
                a = jcast('int', Code05_OpenStore1.fa[Code05_OpenStore1.top[a]])
        return jcast('int', (a if (Code05_OpenStore1.dep[a] <= Code05_OpenStore1.dep[b]) else b))

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code05_OpenStore1.dist[x], Code05_OpenStore1.dist[y])) - jcast('int', (Code05_OpenStore1.dist[Code05_OpenStore1.getLca(x, y)] << (1 & 31))))))

    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_OpenStore1.siz[u] = jcast('int', 1)
        e = jcast('int', Code05_OpenStore1.head[u])
        while (e > 0):
            v = jcast('int', Code05_OpenStore1.to[e])
            if ((v != fa) and (not Code05_OpenStore1.vis[v])):
                Code05_OpenStore1.getSize1(v, u)
                Code05_OpenStore1.siz[u] = jcast('int', jcast('int', jadd(Code05_OpenStore1.siz[u], Code05_OpenStore1.siz[v])))
            e = jcast('int', Code05_OpenStore1.nxt[e])

    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code05_OpenStore1.stacksize = jcast('int', 0)
        Code05_OpenStore1.push(cur, fa, 0, 0, jcast('int', (-1)))
        while (Code05_OpenStore1.stacksize > 0):
            Code05_OpenStore1.pop()
            if (Code05_OpenStore1.e == jcast('int', (-1))):
                Code05_OpenStore1.siz[Code05_OpenStore1.u] = jcast('int', 1)
                Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.head[Code05_OpenStore1.u])
            else:
                Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.nxt[Code05_OpenStore1.e])
            if (Code05_OpenStore1.e != 0):
                Code05_OpenStore1.push(Code05_OpenStore1.u, Code05_OpenStore1.f, 0, 0, Code05_OpenStore1.e)
                v = jcast('int', Code05_OpenStore1.to[Code05_OpenStore1.e])
                if ((v != Code05_OpenStore1.f) and (not Code05_OpenStore1.vis[v])):
                    Code05_OpenStore1.push(v, Code05_OpenStore1.u, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code05_OpenStore1.head[Code05_OpenStore1.u])
                while (ei > 0):
                    v = jcast('int', Code05_OpenStore1.to[ei])
                    if ((v != Code05_OpenStore1.f) and (not Code05_OpenStore1.vis[v])):
                        Code05_OpenStore1.siz[Code05_OpenStore1.u] = jcast('int', jcast('int', jadd(Code05_OpenStore1.siz[Code05_OpenStore1.u], Code05_OpenStore1.siz[v])))
                    ei = jcast('int', Code05_OpenStore1.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code05_OpenStore1.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code05_OpenStore1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code05_OpenStore1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code05_OpenStore1.to[e])
                        if (((v != fa) and (not Code05_OpenStore1.vis[v])) and (Code05_OpenStore1.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                    except JBreak as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code05_OpenStore1.nxt[e])
            except JContinue as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
            except JBreak as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
                break
        return jcast('int', u)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    # 来到了一片连通区，当前重心是rt，上级重心是centfa[rt]
    # 生成两个列表，距离到当前重心的列表，距离到上级重心的列表
    @staticmethod
    def getList1(u, fa, sum, rt):
        u = jcast('int', u)
        fa = jcast('int', fa)
        sum = jcast('int', sum)
        rt = jcast('int', rt)
        jset(Code05_OpenStore1.curAge, ((_java_obj_7 := Code05_OpenStore1), (_java_key_8 := 'cntc'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code05_OpenStore1.age[u])
        Code05_OpenStore1.curSum[Code05_OpenStore1.cntc] = jcast('long', sum)
        if (Code05_OpenStore1.centfa[rt] > 0):
            jset(Code05_OpenStore1.faAge, ((_java_obj_10 := Code05_OpenStore1), (_java_key_11 := 'cntf'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code05_OpenStore1.age[u])
            jset(Code05_OpenStore1.faSum, Code05_OpenStore1.cntf, Code05_OpenStore1.getDist(u, Code05_OpenStore1.centfa[rt]))
        e = jcast('int', Code05_OpenStore1.head[u])
        while (e > 0):
            v = jcast('int', Code05_OpenStore1.to[e])
            w = jcast('int', Code05_OpenStore1.weight[e])
            if ((v != fa) and (not Code05_OpenStore1.vis[v])):
                Code05_OpenStore1.getList1(v, u, jcast('int', jadd(sum, w)), rt)
            e = jcast('int', Code05_OpenStore1.nxt[e])

    # getList1的迭代版
    @staticmethod
    def getList2(cur, father, psum, cen):
        cur = jcast('int', cur)
        father = jcast('int', father)
        psum = jcast('int', psum)
        cen = jcast('int', cen)
        Code05_OpenStore1.stacksize = jcast('int', 0)
        Code05_OpenStore1.push(cur, father, psum, cen, jcast('int', (-1)))
        while (Code05_OpenStore1.stacksize > 0):
            Code05_OpenStore1.pop()
            if (Code05_OpenStore1.e == jcast('int', (-1))):
                jset(Code05_OpenStore1.curAge, ((_java_obj_13 := Code05_OpenStore1), (_java_key_14 := 'cntc'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code05_OpenStore1.age[Code05_OpenStore1.u])
                Code05_OpenStore1.curSum[Code05_OpenStore1.cntc] = jcast('long', Code05_OpenStore1.a)
                if (Code05_OpenStore1.centfa[Code05_OpenStore1.b] > 0):
                    jset(Code05_OpenStore1.faAge, ((_java_obj_16 := Code05_OpenStore1), (_java_key_17 := 'cntf'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code05_OpenStore1.age[Code05_OpenStore1.u])
                    jset(Code05_OpenStore1.faSum, Code05_OpenStore1.cntf, Code05_OpenStore1.getDist(Code05_OpenStore1.u, Code05_OpenStore1.centfa[Code05_OpenStore1.b]))
                Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.head[Code05_OpenStore1.u])
            else:
                Code05_OpenStore1.e = jcast('int', Code05_OpenStore1.nxt[Code05_OpenStore1.e])
            if (Code05_OpenStore1.e != 0):
                Code05_OpenStore1.push(Code05_OpenStore1.u, Code05_OpenStore1.f, Code05_OpenStore1.a, Code05_OpenStore1.b, Code05_OpenStore1.e)
                v = jcast('int', Code05_OpenStore1.to[Code05_OpenStore1.e])
                w = jcast('int', Code05_OpenStore1.weight[Code05_OpenStore1.e])
                if ((v != Code05_OpenStore1.f) and (not Code05_OpenStore1.vis[v])):
                    Code05_OpenStore1.push(v, Code05_OpenStore1.u, jcast('int', jadd(Code05_OpenStore1.a, w)), Code05_OpenStore1.b, jcast('int', (-1)))

    @staticmethod
    def centroidTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_OpenStore1.centfa[u] = jcast('int', fa)
        Code05_OpenStore1.vis[u] = jcast('boolean', True)
        Code05_OpenStore1.curl[u] = jcast('int', jcast('int', jadd(Code05_OpenStore1.cntc, 1)))
        Code05_OpenStore1.fal[u] = jcast('int', jcast('int', jadd(Code05_OpenStore1.cntf, 1)))
        # getList1(u, 0, 0, u);
        Code05_OpenStore1.getList2(u, 0, 0, u)
        Code05_OpenStore1.curr[u] = jcast('int', Code05_OpenStore1.cntc)
        Code05_OpenStore1.far[u] = jcast('int', Code05_OpenStore1.cntf)
        e = jcast('int', Code05_OpenStore1.head[u])
        while (e > 0):
            v = jcast('int', Code05_OpenStore1.to[e])
            if (not Code05_OpenStore1.vis[v]):
                Code05_OpenStore1.centroidTree(Code05_OpenStore1.getCentroid(v, u), u)
            e = jcast('int', Code05_OpenStore1.nxt[e])

    # 查询x在有序数组arr中的排名
    @staticmethod
    def kth(arr, l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        ans = jcast('int', jcast('int', jadd(r, 1)))
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (arr[mid] >= x):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    # 每个对象两个属性(age, sum)，所有对象根据年龄排序
    # 这里使用双指针快排完成排序
    @staticmethod
    def sort(age, sum, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', age[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp1 = 0
        tmp2 = 0
        while (i <= j):
            while (age[i] < pivot):
                i = jcast('int', (i + 1))
            while (age[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp1 = jcast('int', age[i])
                age[i] = jcast('int', age[j])
                age[j] = jcast('int', tmp1)
                tmp2 = jcast('long', sum[i])
                sum[i] = jcast('long', sum[j])
                sum[j] = jcast('long', tmp2)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code05_OpenStore1.sort(age, sum, l, j)
        Code05_OpenStore1.sort(age, sum, i, r)

    nodeCnt = 0
    pathSum = 0
    # 下标范围[l...r]代表当前节点的列表，找到年龄范围[agel, ager]的人
    # 查到的人数设置给nodeCnt，查到的距离总和设置给pathSum
    @staticmethod
    def query(age, sum, l, r, agel, ager):
        l = jcast('int', l)
        r = jcast('int', r)
        agel = jcast('int', agel)
        ager = jcast('int', ager)
        Code05_OpenStore1.nodeCnt = jcast('long', jset(Code05_OpenStore1, 'pathSum', 0))
        if (l <= r):
            a = jcast('int', Code05_OpenStore1.kth(age, l, r, agel))
            b = jcast('int', jcast('int', (Code05_OpenStore1.kth(age, l, r, jcast('int', jadd(ager, 1))) - 1)))
            if (a <= b):
                Code05_OpenStore1.nodeCnt = jcast('long', jcast('int', jadd(jcast('int', (b - a)), 1)))
                Code05_OpenStore1.pathSum = jcast('long', jcast('long', (sum[b] - (0 if (a == l) else sum[jcast('int', (a - 1))]))))

    @staticmethod
    def compute(x, agel, ager):
        x = jcast('int', x)
        agel = jcast('int', agel)
        ager = jcast('int', ager)
        Code05_OpenStore1.query(Code05_OpenStore1.curAge, Code05_OpenStore1.curSum, Code05_OpenStore1.curl[x], Code05_OpenStore1.curr[x], agel, ager)
        ans = jcast('long', Code05_OpenStore1.pathSum)
        cnt1 = 0
        sum1 = 0
        cnt2 = 0
        sum2 = 0
        cur = jcast('int', x)
        fa = jcast('int', Code05_OpenStore1.centfa[cur])
        while (fa > 0):
            Code05_OpenStore1.query(Code05_OpenStore1.curAge, Code05_OpenStore1.curSum, Code05_OpenStore1.curl[fa], Code05_OpenStore1.curr[fa], agel, ager)
            cnt1 = jcast('long', Code05_OpenStore1.nodeCnt)
            sum1 = jcast('long', Code05_OpenStore1.pathSum)
            Code05_OpenStore1.query(Code05_OpenStore1.faAge, Code05_OpenStore1.faSum, Code05_OpenStore1.fal[cur], Code05_OpenStore1.far[cur], agel, ager)
            cnt2 = jcast('long', Code05_OpenStore1.nodeCnt)
            sum2 = jcast('long', Code05_OpenStore1.pathSum)
            ans = jcast('long', jcast('long', jadd(ans, sum1)))
            ans = jcast('long', jcast('long', (ans - sum2)))
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', (cnt1 - cnt2)) * Code05_OpenStore1.getDist(x, fa))))))
            cur = jcast('int', fa)
            fa = jcast('int', Code05_OpenStore1.centfa[cur])
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code05_OpenStore1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_OpenStore1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_OpenStore1.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_OpenStore1.A = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_OpenStore1.n):
            jset(Code05_OpenStore1.age, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code05_OpenStore1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code05_OpenStore1.addEdge(u, v, w)
            Code05_OpenStore1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        # dfs1(1, 0, 0);
        # dfs2(1, 1);
        Code05_OpenStore1.dfs3(1, 0, 0)
        Code05_OpenStore1.dfs4(1, 1)
        Code05_OpenStore1.centroidTree(Code05_OpenStore1.getCentroid(1, 0), 0)
        i = jcast('int', 1)
        while (i <= Code05_OpenStore1.n):
            Code05_OpenStore1.sort(Code05_OpenStore1.curAge, Code05_OpenStore1.curSum, Code05_OpenStore1.curl[i], Code05_OpenStore1.curr[i])
            j = jcast('int', jcast('int', jadd(Code05_OpenStore1.curl[i], 1)))
            while (j <= Code05_OpenStore1.curr[i]):
                Code05_OpenStore1.curSum[j] = jcast('long', jcast('long', jadd(Code05_OpenStore1.curSum[j], Code05_OpenStore1.curSum[jcast('int', (j - 1))])))
                j = jcast('int', (j + 1))
            Code05_OpenStore1.sort(Code05_OpenStore1.faAge, Code05_OpenStore1.faSum, Code05_OpenStore1.fal[i], Code05_OpenStore1.far[i])
            j = jcast('int', jcast('int', jadd(Code05_OpenStore1.fal[i], 1)))
            while (j <= Code05_OpenStore1.far[i]):
                Code05_OpenStore1.faSum[j] = jcast('long', jcast('long', jadd(Code05_OpenStore1.faSum[j], Code05_OpenStore1.faSum[jcast('int', (j - 1))])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        lastAns = jcast('long', 0)
        i = jcast('int', 1)
        u = 0
        l = 0
        r = 0
        while (i <= Code05_OpenStore1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            l = jcast('int', jcast('int', jcast('long', jmod(jcast('long', jadd(lastAns, l)), Code05_OpenStore1.A))))
            r = jcast('int', jcast('int', jcast('long', jmod(jcast('long', jadd(lastAns, r)), Code05_OpenStore1.A))))
            if (l > r):
                tmp = jcast('int', l)
                l = jcast('int', r)
                r = jcast('int', tmp)
            lastAns = jcast('long', Code05_OpenStore1.compute(u, l, r))
            jcall(out, 'println', lastAns)
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
            return jcast('int', self.buffer[((_java_obj_19 := self), (_java_key_20 := 'ptr'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]])

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
            raise TypeError("No matching overload for Code05_OpenStore1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_OpenStore1.MAXN = jcast('int', 200001)
Code05_OpenStore1.MAXK = jcast('int', 4000001)
Code05_OpenStore1.n = jcast('int', 0)
Code05_OpenStore1.m = jcast('int', 0)
Code05_OpenStore1.A = jcast('int', 0)
Code05_OpenStore1.age = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.head = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.nxt = jarray('int', [jcast('int', (Code05_OpenStore1.MAXN << (1 & 31)))])
Code05_OpenStore1.to = jarray('int', [jcast('int', (Code05_OpenStore1.MAXN << (1 & 31)))])
Code05_OpenStore1.weight = jarray('int', [jcast('int', (Code05_OpenStore1.MAXN << (1 & 31)))])
Code05_OpenStore1.cntg = jcast('int', 0)
Code05_OpenStore1.fa = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.dep = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.siz = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.son = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.top = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.dist = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.vis = jarray('boolean', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.centfa = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.curl = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.curr = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.curAge = jarray('int', [Code05_OpenStore1.MAXK])
Code05_OpenStore1.curSum = jarray('long', [Code05_OpenStore1.MAXK])
Code05_OpenStore1.cntc = jcast('int', 0)
Code05_OpenStore1.fal = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.far = jarray('int', [Code05_OpenStore1.MAXN])
Code05_OpenStore1.faAge = jarray('int', [Code05_OpenStore1.MAXK])
Code05_OpenStore1.faSum = jarray('long', [Code05_OpenStore1.MAXK])
Code05_OpenStore1.cntf = jcast('int', 0)
Code05_OpenStore1.stack = jarray('int', [Code05_OpenStore1.MAXN, 5])
Code05_OpenStore1.u = jcast('int', 0)
Code05_OpenStore1.f = jcast('int', 0)
Code05_OpenStore1.a = jcast('int', 0)
Code05_OpenStore1.b = jcast('int', 0)
Code05_OpenStore1.e = jcast('int', 0)
Code05_OpenStore1.stacksize = jcast('int', 0)
Code05_OpenStore1.nodeCnt = jcast('long', 0)
Code05_OpenStore1.pathSum = jcast('long', 0)

if __name__ == '__main__':
    Code05_OpenStore1.main([])
