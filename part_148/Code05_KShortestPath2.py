# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# k短路问题，可持久化左偏树实现最优解，Python版
# 有n个点编号1~n，有m条边，每条边都是正数边权，组成有向带权图
# 从1号点走到n号点，就认为是一次旅行
# 一次旅行中，边不能重复选，点可以重复经过，如果到达了n号点，那么旅行立刻停止
# 从1号点走到n号点，会有很多通路方案，通路方案的路费为选择边的边权累加和
# 虽然每次旅行都是从1号点到n号点，但是你希望每次旅行的通路方案都是不同的
# 任何两次旅行，只要选择的边稍有不同，就认为是不同的通路方案
# 你的钱数为money，用来支付路费，打印你一共能进行几次旅行
# 测试链接 : https://www.luogu.com.cn/problem/P2483
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_KShortestPath2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXT': 'MAXT', 'MAXH': 'MAXH', 'INF': 'INF', 'n': 'n', 'm': 'm', 'money': 'money', 'headg': 'headg', 'tog': 'tog', 'nextg': 'nextg', 'weightg': 'weightg', 'cntg': 'cntg', 'headr': 'headr', 'tor': 'tor', 'nextr': 'nextr', 'weightr': 'weightr', 'cntr': 'cntr', 'to': 'to', 'cost': 'cost', 'left': 'left', 'right': 'right', 'dist': 'dist', 'cntt': 'cntt', 'rt': 'rt', 'key': 'key', 'val': 'val', 'heap': 'heap', 'cntd': 'cntd', 'cnth': 'cnth', 'vis': 'vis', 'path': 'path', 'dis': 'dis'}
    MAXN = 0
    MAXM = 0
    MAXT = 0
    MAXH = 0
    INF = 0.0
    n = 0
    m = 0
    money = 0.0
    # 关于正反图有一个非常值得注意的地方
    # 如果正图中，a到b的边，编号为x
    # 那么反图中，b到a的边，编号也是x
    # 因为每一条边，正图建立的同时，反图也同步建立
    # 所以正反图中这条边分配的编号也是一样的
    # 正图
    headg = None
    tog = None
    nextg = None
    weightg = None
    cntg = 0
    # 反图
    headr = None
    tor = None
    nextr = None
    weightr = None
    cntr = 0
    # 左偏树代表基于之前的通路方案，选择非树边的可能性
    # 左偏树的头就代表最优的选择，假设编号为h的节点是头
    # to[h] : 选择最优非树边，这个非树边在正图里指向哪个节点
    to = None
    # cost[h] : 基于之前的通路方案，最优选择会让路费增加多少
    cost = None
    left = None
    right = None
    dist = None
    cntt = 0
    # rt[u] : 在最短路树上，节点u及其所有祖先节点，所拥有的全部非树边，组成的左偏树
    rt = None
    # heap是经典的小根堆，放着很多(key, val)数据，根据val来组织小根堆
    key = None
    val = None
    heap = None
    cntd = 0
    cnth = 0
    # dijkstra算法需要，根据反图跑dijkstra，生成从节点n开始的最短路树
    # vis[u] : 节点u到节点n的最短距离，是否已经计算过了
    vis = None
    # path[u] : 最短路树上，到达节点u的树边，编号是什么，也代表正图上，所对应的边
    path = None
    # dis[u] : 最短路树上，节点n到节点u的最短距离
    dis = None
    @staticmethod
    def addEdgeG(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('double', w)
        jset(Code05_KShortestPath2.nextg, ((_java_obj_1 := Code05_KShortestPath2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_KShortestPath2.headg[u])
        Code05_KShortestPath2.tog[Code05_KShortestPath2.cntg] = jcast('int', v)
        Code05_KShortestPath2.weightg[Code05_KShortestPath2.cntg] = jcast('double', w)
        Code05_KShortestPath2.headg[u] = jcast('int', Code05_KShortestPath2.cntg)

    @staticmethod
    def addEdgeR(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('double', w)
        jset(Code05_KShortestPath2.nextr, ((_java_obj_4 := Code05_KShortestPath2), (_java_key_5 := 'cntr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code05_KShortestPath2.headr[u])
        Code05_KShortestPath2.tor[Code05_KShortestPath2.cntr] = jcast('int', v)
        Code05_KShortestPath2.weightr[Code05_KShortestPath2.cntr] = jcast('double', w)
        Code05_KShortestPath2.headr[u] = jcast('int', Code05_KShortestPath2.cntr)

    @staticmethod
    def init(t, c):
        t = jcast('int', t)
        c = jcast('double', c)
        jset(Code05_KShortestPath2.to, ((_java_obj_7 := Code05_KShortestPath2), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], t)
        Code05_KShortestPath2.cost[Code05_KShortestPath2.cntt] = jcast('double', c)
        jset(Code05_KShortestPath2.left, Code05_KShortestPath2.cntt, jset(Code05_KShortestPath2.right, Code05_KShortestPath2.cntt, jset(Code05_KShortestPath2.dist, Code05_KShortestPath2.cntt, 0)))
        return jcast('int', Code05_KShortestPath2.cntt)

    @staticmethod
    def clone(i):
        i = jcast('int', i)
        jset(Code05_KShortestPath2.to, ((_java_obj_10 := Code05_KShortestPath2), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code05_KShortestPath2.to[i])
        Code05_KShortestPath2.cost[Code05_KShortestPath2.cntt] = jcast('double', Code05_KShortestPath2.cost[i])
        Code05_KShortestPath2.left[Code05_KShortestPath2.cntt] = jcast('int', Code05_KShortestPath2.left[i])
        Code05_KShortestPath2.right[Code05_KShortestPath2.cntt] = jcast('int', Code05_KShortestPath2.right[i])
        Code05_KShortestPath2.dist[Code05_KShortestPath2.cntt] = jcast('int', Code05_KShortestPath2.dist[i])
        return jcast('int', Code05_KShortestPath2.cntt)

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        if (Code05_KShortestPath2.cost[i] > Code05_KShortestPath2.cost[j]):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        h = jcast('int', Code05_KShortestPath2.clone(i))
        jset(Code05_KShortestPath2.right, h, Code05_KShortestPath2.merge(Code05_KShortestPath2.right[h], j))
        if (Code05_KShortestPath2.dist[Code05_KShortestPath2.left[h]] < Code05_KShortestPath2.dist[Code05_KShortestPath2.right[h]]):
            tmp = jcast('int', Code05_KShortestPath2.left[h])
            Code05_KShortestPath2.left[h] = jcast('int', Code05_KShortestPath2.right[h])
            Code05_KShortestPath2.right[h] = jcast('int', tmp)
        Code05_KShortestPath2.dist[h] = jcast('int', jcast('int', jadd(Code05_KShortestPath2.dist[Code05_KShortestPath2.right[h]], 1)))
        return jcast('int', h)

    # (k, v)组成一个数据，放到堆上，根据v来组织小根堆
    @staticmethod
    def heapAdd(k, v):
        k = jcast('int', k)
        v = jcast('double', v)
        jset(Code05_KShortestPath2.key, ((_java_obj_13 := Code05_KShortestPath2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], k)
        Code05_KShortestPath2.val[Code05_KShortestPath2.cntd] = jcast('double', v)
        jset(Code05_KShortestPath2.heap, ((_java_obj_16 := Code05_KShortestPath2), (_java_key_17 := 'cnth'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code05_KShortestPath2.cntd)
        cur = jcast('int', Code05_KShortestPath2.cnth)
        father = jcast('int', jcast('int', jdiv(cur, 2)))
        tmp = 0
        while ((cur > 1) and (Code05_KShortestPath2.val[Code05_KShortestPath2.heap[father]] > Code05_KShortestPath2.val[Code05_KShortestPath2.heap[cur]])):
            tmp = jcast('int', Code05_KShortestPath2.heap[father])
            Code05_KShortestPath2.heap[father] = jcast('int', Code05_KShortestPath2.heap[cur])
            Code05_KShortestPath2.heap[cur] = jcast('int', tmp)
            cur = jcast('int', father)
            father = jcast('int', jcast('int', jdiv(cur, 2)))

    # 小根堆上，堆顶的数据(k, v)弹出，并返回数据所在的下标ans
    # 根据返回值ans，key[ans]得到k，val[ans]得到v
    @staticmethod
    def heapPop():
        ans = jcast('int', Code05_KShortestPath2.heap[1])
        jset(Code05_KShortestPath2.heap, 1, Code05_KShortestPath2.heap[((_java_obj_19 := Code05_KShortestPath2), (_java_key_20 := 'cnth'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
        cur = jcast('int', 1)
        l = jcast('int', jcast('int', (cur * 2)))
        r = jcast('int', jcast('int', jadd(l, 1)))
        best = 0
        tmp = 0
        while (l <= Code05_KShortestPath2.cnth):
            try:
                best = jcast('int', (r if ((r <= Code05_KShortestPath2.cnth) and (Code05_KShortestPath2.val[Code05_KShortestPath2.heap[r]] < Code05_KShortestPath2.val[Code05_KShortestPath2.heap[l]])) else l))
                best = jcast('int', (best if (Code05_KShortestPath2.val[Code05_KShortestPath2.heap[best]] < Code05_KShortestPath2.val[Code05_KShortestPath2.heap[cur]]) else cur))
                if (best == cur):
                    raise JBreak(None)
                tmp = jcast('int', Code05_KShortestPath2.heap[best])
                Code05_KShortestPath2.heap[best] = jcast('int', Code05_KShortestPath2.heap[cur])
                Code05_KShortestPath2.heap[cur] = jcast('int', tmp)
                cur = jcast('int', best)
                l = jcast('int', jcast('int', (cur * 2)))
                r = jcast('int', jcast('int', jadd(l, 1)))
            except JContinue as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
            except JBreak as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
                break
        return jcast('int', ans)

    @staticmethod
    def heapEmpty():
        return jcast('boolean', (Code05_KShortestPath2.cnth == 0))

    # 根据反图跑dijkstra算法
    # 得到从节点n出发的最短路树、每个节点到节点n的最短距离信息
    # 最短路树如果有多个，找到任何一个即可
    @staticmethod
    def dijkstra():
        Code05_KShortestPath2.dis[Code05_KShortestPath2.n] = jcast('double', 0)
        jstatic('Arrays', 'fill', Code05_KShortestPath2.dis, 1, Code05_KShortestPath2.n, Code05_KShortestPath2.INF)
        Code05_KShortestPath2.cntd = jcast('int', jset(Code05_KShortestPath2, 'cnth', 0))
        Code05_KShortestPath2.heapAdd(Code05_KShortestPath2.n, 0)
        while (not Code05_KShortestPath2.heapEmpty()):
            top = jcast('int', Code05_KShortestPath2.heapPop())
            u = jcast('int', Code05_KShortestPath2.key[top])
            w = jcast('double', Code05_KShortestPath2.val[top])
            if (not Code05_KShortestPath2.vis[u]):
                Code05_KShortestPath2.vis[u] = jcast('boolean', True)
                e = jcast('int', Code05_KShortestPath2.headr[u])
                v = 0
                while (e > 0):
                    v = jcast('int', Code05_KShortestPath2.tor[e])
                    if (Code05_KShortestPath2.dis[v] > jadd(w, Code05_KShortestPath2.weightr[e])):
                        Code05_KShortestPath2.dis[v] = jcast('double', jadd(w, Code05_KShortestPath2.weightr[e]))
                        Code05_KShortestPath2.path[v] = jcast('int', e)
                        Code05_KShortestPath2.heapAdd(v, Code05_KShortestPath2.dis[v])
                    e = jcast('int', Code05_KShortestPath2.nextr[e])

    # 在最短路树上的每个节点，生成自己的左偏树
    # 节点u的左偏树 = 节点u自己的非树边左偏树 + 节点u在最短路树上的父亲的左偏树
    # 课上重点解释了这么做的意义
    @staticmethod
    def mergeRoad():
        Code05_KShortestPath2.cntd = jcast('int', jset(Code05_KShortestPath2, 'cnth', 0))
        i = jcast('int', 1)
        while (i <= Code05_KShortestPath2.n):
            Code05_KShortestPath2.heapAdd(i, Code05_KShortestPath2.dis[i])
            i = jcast('int', (i + 1))
        Code05_KShortestPath2.dist[0] = jcast('int', jcast('int', (-1)))
        while (not Code05_KShortestPath2.heapEmpty()):
            top = jcast('int', Code05_KShortestPath2.heapPop())
            u = jcast('int', Code05_KShortestPath2.key[top])
            e = jcast('int', Code05_KShortestPath2.headg[u])
            v = 0
            while (e > 0):
                v = jcast('int', Code05_KShortestPath2.tog[e])
                # path[u]既是边在反图中的编号，也是边在正图中的编号
                # 因为正反图同步建立，边的正图编号 == 边的反图编号
                if (e != Code05_KShortestPath2.path[u]):
                    jset(Code05_KShortestPath2.rt, u, Code05_KShortestPath2.merge(Code05_KShortestPath2.rt[u], Code05_KShortestPath2.init(v, (jadd(Code05_KShortestPath2.weightg[e], Code05_KShortestPath2.dis[v]) - Code05_KShortestPath2.dis[u]))))
                e = jcast('int', Code05_KShortestPath2.nextg[e])
            if (Code05_KShortestPath2.path[u] != 0):
                jset(Code05_KShortestPath2.rt, u, Code05_KShortestPath2.merge(Code05_KShortestPath2.rt[u], Code05_KShortestPath2.rt[Code05_KShortestPath2.tog[Code05_KShortestPath2.path[u]]]))

    # 从路费第1小的方案开始，逐渐找到第2小、第3小...
    # 看看money能够覆盖几次旅行，返回旅行的次数
    @staticmethod
    def expand():
        ans = jcast('int', 0)
        Code05_KShortestPath2.money = jcast('double', (Code05_KShortestPath2.money - Code05_KShortestPath2.dis[1]))
        if (Code05_KShortestPath2.money >= 0):
            ans = jcast('int', (ans + 1))
            Code05_KShortestPath2.cntd = jcast('int', jset(Code05_KShortestPath2, 'cnth', 0))
            if (Code05_KShortestPath2.rt[1] != 0):
                # 开始阶段
                # 1号节点左偏树的堆顶，代表增加代价最小的非树边，放入决策堆
                # 目前路通方案的路费，同步放入
                Code05_KShortestPath2.heapAdd(Code05_KShortestPath2.rt[1], jadd(Code05_KShortestPath2.dis[1], Code05_KShortestPath2.cost[Code05_KShortestPath2.rt[1]]))
            while (not Code05_KShortestPath2.heapEmpty()):
                try:
                    top = jcast('int', Code05_KShortestPath2.heapPop())
                    h = jcast('int', Code05_KShortestPath2.key[top])
                    w = jcast('double', Code05_KShortestPath2.val[top])
                    Code05_KShortestPath2.money = jcast('double', (Code05_KShortestPath2.money - w))
                    if (Code05_KShortestPath2.money < 0):
                        raise JBreak(None)
                    ans = jcast('int', (ans + 1))
                    # 当前选择的非树边，被左偏树上的左儿子替换
                    if (Code05_KShortestPath2.left[h] != 0):
                        Code05_KShortestPath2.heapAdd(Code05_KShortestPath2.left[h], jadd((w - Code05_KShortestPath2.cost[h]), Code05_KShortestPath2.cost[Code05_KShortestPath2.left[h]]))
                    # 当前选择的非树边，被左偏树上的右儿子替换
                    if (Code05_KShortestPath2.right[h] != 0):
                        Code05_KShortestPath2.heapAdd(Code05_KShortestPath2.right[h], jadd((w - Code05_KShortestPath2.cost[h]), Code05_KShortestPath2.cost[Code05_KShortestPath2.right[h]]))
                    # 当前选择的非树边，指向节点to[h]，那么从to[h]的左偏树里，新增一个最优的非树边
                    if ((Code05_KShortestPath2.to[h] != 0) and (Code05_KShortestPath2.rt[Code05_KShortestPath2.to[h]] != 0)):
                        Code05_KShortestPath2.heapAdd(Code05_KShortestPath2.rt[Code05_KShortestPath2.to[h]], jadd(w, Code05_KShortestPath2.cost[Code05_KShortestPath2.rt[Code05_KShortestPath2.to[h]]]))
                except JContinue as _java_control_23:
                    if _java_control_23.label not in (None,):
                        raise
                except JBreak as _java_control_23:
                    if _java_control_23.label not in (None,):
                        raise
                    break
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code05_KShortestPath2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_KShortestPath2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_KShortestPath2.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_KShortestPath2.money = jcast('double', jcall(in_, 'nextDouble'))
        u = 0
        v = 0
        w = 0.0
        i = jcast('int', 1)
        while (i <= Code05_KShortestPath2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('double', jcall(in_, 'nextDouble'))
            # 题目说了，一旦到达节点n，旅行立刻停止
            # 所以从节点n出发的边，一律忽略
            if (u != Code05_KShortestPath2.n):
                # 建立正图
                Code05_KShortestPath2.addEdgeG(u, v, w)
                # 建立反图
                Code05_KShortestPath2.addEdgeR(v, u, w)
            i = jcast('int', (i + 1))
        Code05_KShortestPath2.dijkstra()
        Code05_KShortestPath2.mergeRoad()
        ans = jcast('int', Code05_KShortestPath2.expand())
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_24 := self), (_java_key_25 := 'ptr'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))), _java_old_26)[4]])

        def hasNext(self):
            while self.hasNextByte():
                b = jcast('byte', self.buffer[self.ptr])
                if (not self.isWhitespace(b)):
                    return jcast('boolean', True)
                self.ptr = jcast('int', (self.ptr + 1))
            return jcast('boolean', False)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def nextDouble(self):
            num = jcast('double', 0)
            div = jcast('double', 1)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while (((not self.isWhitespace(b)) and (b != jchar('.'))) and (b != jcast('int', (-1)))):
                num = jcast('double', jadd((num * 10), jcast('int', (b - jchar('0')))))
                b = jcast('byte', self.readByte())
            if (b == jchar('.')):
                b = jcast('byte', self.readByte())
                while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                    num = jcast('double', jadd(num, jdiv(jcast('int', (b - jchar('0'))), (div := (div * 10)))))
                    b = jcast('byte', self.readByte())
            return jcast('double', ((-num) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_KShortestPath2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_KShortestPath2.MAXN = jcast('int', 5001)
Code05_KShortestPath2.MAXM = jcast('int', 200001)
Code05_KShortestPath2.MAXT = jcast('int', 1000001)
Code05_KShortestPath2.MAXH = jcast('int', 4200001)
Code05_KShortestPath2.INF = jcast('double', 1e+18)
Code05_KShortestPath2.n = jcast('int', 0)
Code05_KShortestPath2.m = jcast('int', 0)
Code05_KShortestPath2.money = jcast('double', 0.0)
Code05_KShortestPath2.headg = jarray('int', [Code05_KShortestPath2.MAXN])
Code05_KShortestPath2.tog = jarray('int', [Code05_KShortestPath2.MAXM])
Code05_KShortestPath2.nextg = jarray('int', [Code05_KShortestPath2.MAXM])
Code05_KShortestPath2.weightg = jarray('double', [Code05_KShortestPath2.MAXM])
Code05_KShortestPath2.cntg = jcast('int', 0)
Code05_KShortestPath2.headr = jarray('int', [Code05_KShortestPath2.MAXN])
Code05_KShortestPath2.tor = jarray('int', [Code05_KShortestPath2.MAXM])
Code05_KShortestPath2.nextr = jarray('int', [Code05_KShortestPath2.MAXM])
Code05_KShortestPath2.weightr = jarray('double', [Code05_KShortestPath2.MAXM])
Code05_KShortestPath2.cntr = jcast('int', 0)
Code05_KShortestPath2.to = jarray('int', [Code05_KShortestPath2.MAXT])
Code05_KShortestPath2.cost = jarray('double', [Code05_KShortestPath2.MAXT])
Code05_KShortestPath2.left = jarray('int', [Code05_KShortestPath2.MAXT])
Code05_KShortestPath2.right = jarray('int', [Code05_KShortestPath2.MAXT])
Code05_KShortestPath2.dist = jarray('int', [Code05_KShortestPath2.MAXT])
Code05_KShortestPath2.cntt = jcast('int', 0)
Code05_KShortestPath2.rt = jarray('int', [Code05_KShortestPath2.MAXN])
Code05_KShortestPath2.key = jarray('int', [Code05_KShortestPath2.MAXH])
Code05_KShortestPath2.val = jarray('double', [Code05_KShortestPath2.MAXH])
Code05_KShortestPath2.heap = jarray('int', [Code05_KShortestPath2.MAXH])
Code05_KShortestPath2.cntd = jcast('int', 0)
Code05_KShortestPath2.cnth = jcast('int', 0)
Code05_KShortestPath2.vis = jarray('boolean', [Code05_KShortestPath2.MAXN])
Code05_KShortestPath2.path = jarray('int', [Code05_KShortestPath2.MAXN])
Code05_KShortestPath2.dis = jarray('double', [Code05_KShortestPath2.MAXN])

if __name__ == '__main__':
    Code05_KShortestPath2.main([])
