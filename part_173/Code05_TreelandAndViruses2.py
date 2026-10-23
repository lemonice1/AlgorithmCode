# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树上病毒传播，Python版
# 一共有n个城市，有n-1条无向边，所有城市组成一棵树，一共有q条查询，每条查询数据如下
# 首先给定k种病毒，每种病毒有初次感染的城市start[i]，还有传播速度speed[i]
# 然后给定m个关键城市，打印每个城市被第几号病毒感染，病毒传播的规则如下
# 病毒的传播按轮次进行，每一轮病毒1先传播，然后是病毒2 .. 直到病毒k，下一轮又从病毒1开始
# 如果第i种病毒已经感染了城市x，当自己传播时，想要感染城市y的条件如下
# 城市x到城市y的路径包含的边数<=speed[i]，城市x到城市y的路径上，除了x所有城市都未被感染
# 一旦城市被某种病毒感染就永久保持，不会再被其他病毒感染，传播一直持续，直到所有城市都被感染
# 1 <= n、q、所有查询病毒总数、所有查询关键城市总数 <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1320E
# 测试链接 : https://codeforces.com/problemset/problem/1320/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_TreelandAndViruses2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'q': 'q', 'k': 'k', 'm': 'm', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headv': 'headv', 'nextv': 'nextv', 'tov': 'tov', 'cntv': 'cntv', 'dep': 'dep', 'dfn': 'dfn', 'stjump': 'stjump', 'cntd': 'cntd', 'start': 'start', 'speed': 'speed', 'query': 'query', 'arr': 'arr', 'tmp': 'tmp', 'len': 'len', 'heap': 'heap', 'vis': 'vis', 'minTime': 'minTime', 'findVirus': 'findVirus'}
    class Node:
        __java_fields__ = {'id': 'id', 'dist': 'dist', 'time': 'time', 'virus': 'virus'}
        # id：实例字段，在构造函数中初始化。
        # dist：实例字段，在构造函数中初始化。
        # time：实例字段，在构造函数中初始化。
        # virus：实例字段，在构造函数中初始化。
        def _java_init_0(self, id_, dist_, time_, virus_):
            id_ = jcast('int', id_)
            dist_ = jcast('int', dist_)
            time_ = jcast('int', time_)
            virus_ = jcast('int', virus_)
            self.id = jcast('int', id_)
            self.dist = jcast('int', dist_)
            self.time = jcast('int', time_)
            self.virus = jcast('int', virus_)

        def __init__(self, *args, _java_ctor=None):
            self.id = jcast('int', 0)
            self.dist = jcast('int', 0)
            self.time = jcast('int', 0)
            self.virus = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int', 'int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_TreelandAndViruses2.Node.Node")


    class NodeCmp:
        __java_fields__ = {}
        def compare(self, o1, o2):
            if (jget(o1, 'time') != jget(o2, 'time')):
                return jcast('int', jcast('int', (jget(o1, 'time') - jget(o2, 'time'))))
            return jcast('int', jcast('int', (jget(o1, 'virus') - jget(o2, 'virus'))))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    MAXN = 0
    MAXP = 0
    n = 0
    q = 0
    k = 0
    m = 0
    headg = None
    nextg = None
    tog = None
    cntg = 0
    headv = None
    nextv = None
    tov = None
    cntv = 0
    dep = None
    dfn = None
    stjump = None
    cntd = 0
    start = None
    speed = None
    query = None
    arr = None
    tmp = None
    len = 0
    heap = None
    vis = None
    minTime = None
    findVirus = None
    @staticmethod
    def addEdgeG(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_TreelandAndViruses2.nextg, ((_java_obj_1 := Code05_TreelandAndViruses2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_TreelandAndViruses2.headg[u])
        Code05_TreelandAndViruses2.tog[Code05_TreelandAndViruses2.cntg] = jcast('int', v)
        Code05_TreelandAndViruses2.headg[u] = jcast('int', Code05_TreelandAndViruses2.cntg)

    @staticmethod
    def addEdgeV(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_TreelandAndViruses2.nextv, ((_java_obj_4 := Code05_TreelandAndViruses2), (_java_key_5 := 'cntv'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code05_TreelandAndViruses2.headv[u])
        Code05_TreelandAndViruses2.tov[Code05_TreelandAndViruses2.cntv] = jcast('int', v)
        Code05_TreelandAndViruses2.headv[u] = jcast('int', Code05_TreelandAndViruses2.cntv)

    @staticmethod
    def sortByDfn(nums, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', nums[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        while (i <= j):
            while (Code05_TreelandAndViruses2.dfn[nums[i]] < Code05_TreelandAndViruses2.dfn[pivot]):
                i = jcast('int', (i + 1))
            while (Code05_TreelandAndViruses2.dfn[nums[j]] > Code05_TreelandAndViruses2.dfn[pivot]):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', nums[i])
                nums[i] = jcast('int', nums[j])
                nums[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code05_TreelandAndViruses2.sortByDfn(nums, l, j)
        Code05_TreelandAndViruses2.sortByDfn(nums, i, r)

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_TreelandAndViruses2.dep[u] = jcast('int', jcast('int', jadd(Code05_TreelandAndViruses2.dep[fa], 1)))
        jset(Code05_TreelandAndViruses2.dfn, u, ((_java_obj_7 := Code05_TreelandAndViruses2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        jset(Code05_TreelandAndViruses2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code05_TreelandAndViruses2.MAXP):
            jset(Code05_TreelandAndViruses2.stjump[u], p, Code05_TreelandAndViruses2.stjump[Code05_TreelandAndViruses2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code05_TreelandAndViruses2.headg[u])
        while (e > 0):
            if (Code05_TreelandAndViruses2.tog[e] != fa):
                Code05_TreelandAndViruses2.dfs(Code05_TreelandAndViruses2.tog[e], u)
            e = jcast('int', Code05_TreelandAndViruses2.nextg[e])

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code05_TreelandAndViruses2.dep[a] < Code05_TreelandAndViruses2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code05_TreelandAndViruses2.MAXP - 1)))
        while (p >= 0):
            if (Code05_TreelandAndViruses2.dep[Code05_TreelandAndViruses2.stjump[a][p]] >= Code05_TreelandAndViruses2.dep[b]):
                a = jcast('int', Code05_TreelandAndViruses2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code05_TreelandAndViruses2.MAXP - 1)))
        while (p >= 0):
            if (Code05_TreelandAndViruses2.stjump[a][p] != Code05_TreelandAndViruses2.stjump[b][p]):
                a = jcast('int', Code05_TreelandAndViruses2.stjump[a][p])
                b = jcast('int', Code05_TreelandAndViruses2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code05_TreelandAndViruses2.stjump[a][0])

    @staticmethod
    def buildVirtualTree():
        tot = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_TreelandAndViruses2.k):
            jset(Code05_TreelandAndViruses2.arr, (tot := jcast('int', (tot + (1)))), Code05_TreelandAndViruses2.start[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_TreelandAndViruses2.m):
            jset(Code05_TreelandAndViruses2.arr, (tot := jcast('int', (tot + (1)))), Code05_TreelandAndViruses2.query[i])
            i = jcast('int', (i + 1))
        Code05_TreelandAndViruses2.sortByDfn(Code05_TreelandAndViruses2.arr, 1, tot)
        Code05_TreelandAndViruses2.len = jcast('int', 0)
        i = jcast('int', 1)
        while (i < tot):
            jset(Code05_TreelandAndViruses2.tmp, ((_java_obj_10 := Code05_TreelandAndViruses2), (_java_key_11 := 'len'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code05_TreelandAndViruses2.arr[i])
            jset(Code05_TreelandAndViruses2.tmp, ((_java_obj_13 := Code05_TreelandAndViruses2), (_java_key_14 := 'len'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code05_TreelandAndViruses2.getLca(Code05_TreelandAndViruses2.arr[i], Code05_TreelandAndViruses2.arr[jcast('int', jadd(i, 1))]))
            i = jcast('int', (i + 1))
        jset(Code05_TreelandAndViruses2.tmp, ((_java_obj_16 := Code05_TreelandAndViruses2), (_java_key_17 := 'len'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code05_TreelandAndViruses2.arr[tot])
        Code05_TreelandAndViruses2.sortByDfn(Code05_TreelandAndViruses2.tmp, 1, Code05_TreelandAndViruses2.len)
        unique = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code05_TreelandAndViruses2.len):
            if (Code05_TreelandAndViruses2.tmp[unique] != Code05_TreelandAndViruses2.tmp[i]):
                jset(Code05_TreelandAndViruses2.tmp, (unique := jcast('int', (unique + (1)))), Code05_TreelandAndViruses2.tmp[i])
            i = jcast('int', (i + 1))
        Code05_TreelandAndViruses2.cntv = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= unique):
            jset(Code05_TreelandAndViruses2.headv, Code05_TreelandAndViruses2.tmp[i], 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < unique):
            # 虚树的边不是单向的，是双向的
            # 因为病毒感染既可以向上也可以向下
            lca = jcast('int', Code05_TreelandAndViruses2.getLca(Code05_TreelandAndViruses2.tmp[i], Code05_TreelandAndViruses2.tmp[jcast('int', jadd(i, 1))]))
            Code05_TreelandAndViruses2.addEdgeV(lca, Code05_TreelandAndViruses2.tmp[jcast('int', jadd(i, 1))])
            Code05_TreelandAndViruses2.addEdgeV(Code05_TreelandAndViruses2.tmp[jcast('int', jadd(i, 1))], lca)
            i = jcast('int', (i + 1))
        Code05_TreelandAndViruses2.len = jcast('int', unique)
        return jcast('int', Code05_TreelandAndViruses2.tmp[1])

    @staticmethod
    def dijkstra():
        i = jcast('int', 1)
        while (i <= Code05_TreelandAndViruses2.len):
            u = jcast('int', Code05_TreelandAndViruses2.tmp[i])
            Code05_TreelandAndViruses2.minTime[u] = jcast('int', jcast('int', jadd(Code05_TreelandAndViruses2.n, 1)))
            Code05_TreelandAndViruses2.findVirus[u] = jcast('int', jcast('int', jadd(Code05_TreelandAndViruses2.k, 1)))
            Code05_TreelandAndViruses2.vis[u] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_TreelandAndViruses2.k):
            s = jcast('int', Code05_TreelandAndViruses2.start[i])
            Code05_TreelandAndViruses2.minTime[s] = jcast('int', 0)
            Code05_TreelandAndViruses2.findVirus[s] = jcast('int', i)
            jcall(Code05_TreelandAndViruses2.heap, 'add', Code05_TreelandAndViruses2.Node(s, 0, 0, i, _java_ctor=0))
            i = jcast('int', (i + 1))
        while (not jcall(Code05_TreelandAndViruses2.heap, 'isEmpty')):
            cur = jcall(Code05_TreelandAndViruses2.heap, 'poll')
            u = jcast('int', jget(cur, 'id'))
            udist = jcast('int', jget(cur, 'dist'))
            uvirus = jcast('int', jget(cur, 'virus'))
            if (not Code05_TreelandAndViruses2.vis[u]):
                Code05_TreelandAndViruses2.vis[u] = jcast('boolean', True)
                e = jcast('int', Code05_TreelandAndViruses2.headv[u])
                while (e > 0):
                    v = jcast('int', Code05_TreelandAndViruses2.tov[e])
                    if (not Code05_TreelandAndViruses2.vis[v]):
                        vdist = jcast('int', jcast('int', jadd(udist, jstatic('Math', 'abs', jcast('int', (Code05_TreelandAndViruses2.dep[u] - Code05_TreelandAndViruses2.dep[v]))))))
                        vtime = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(vdist, Code05_TreelandAndViruses2.speed[uvirus])) - 1)), Code05_TreelandAndViruses2.speed[uvirus])))
                        if ((vtime < Code05_TreelandAndViruses2.minTime[v]) or ((vtime == Code05_TreelandAndViruses2.minTime[v]) and (uvirus < Code05_TreelandAndViruses2.findVirus[v]))):
                            Code05_TreelandAndViruses2.minTime[v] = jcast('int', vtime)
                            Code05_TreelandAndViruses2.findVirus[v] = jcast('int', uvirus)
                            jcall(Code05_TreelandAndViruses2.heap, 'add', Code05_TreelandAndViruses2.Node(v, vdist, vtime, uvirus, _java_ctor=0))
                    e = jcast('int', Code05_TreelandAndViruses2.nextv[e])

    @staticmethod
    def main(args):
        in_ = Code05_TreelandAndViruses2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_TreelandAndViruses2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i < Code05_TreelandAndViruses2.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code05_TreelandAndViruses2.addEdgeG(x, y)
            Code05_TreelandAndViruses2.addEdgeG(y, x)
            i = jcast('int', (i + 1))
        Code05_TreelandAndViruses2.dfs(1, 0)
        Code05_TreelandAndViruses2.q = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', 1)
        while (t <= Code05_TreelandAndViruses2.q):
            Code05_TreelandAndViruses2.k = jcast('int', jcall(in_, 'nextInt'))
            Code05_TreelandAndViruses2.m = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code05_TreelandAndViruses2.k):
                jset(Code05_TreelandAndViruses2.start, i, jcall(in_, 'nextInt'))
                jset(Code05_TreelandAndViruses2.speed, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code05_TreelandAndViruses2.m):
                jset(Code05_TreelandAndViruses2.query, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            Code05_TreelandAndViruses2.buildVirtualTree()
            Code05_TreelandAndViruses2.dijkstra()
            i = jcast('int', 1)
            while (i <= Code05_TreelandAndViruses2.m):
                jcall(out, 'print', jadd(Code05_TreelandAndViruses2.findVirus[Code05_TreelandAndViruses2.query[i]], ' '))
                i = jcast('int', (i + 1))
            jcall(out, 'println')
            t = jcast('int', (t + 1))
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
            raise TypeError("No matching overload for Code05_TreelandAndViruses2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_TreelandAndViruses2.MAXN = jcast('int', 200001)
Code05_TreelandAndViruses2.MAXP = jcast('int', 20)
Code05_TreelandAndViruses2.n = jcast('int', 0)
Code05_TreelandAndViruses2.q = jcast('int', 0)
Code05_TreelandAndViruses2.k = jcast('int', 0)
Code05_TreelandAndViruses2.m = jcast('int', 0)
Code05_TreelandAndViruses2.headg = jarray('int', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.nextg = jarray('int', [jcast('int', (Code05_TreelandAndViruses2.MAXN << (1 & 31)))])
Code05_TreelandAndViruses2.tog = jarray('int', [jcast('int', (Code05_TreelandAndViruses2.MAXN << (1 & 31)))])
Code05_TreelandAndViruses2.cntg = jcast('int', 0)
Code05_TreelandAndViruses2.headv = jarray('int', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.nextv = jarray('int', [jcast('int', (Code05_TreelandAndViruses2.MAXN << (1 & 31)))])
Code05_TreelandAndViruses2.tov = jarray('int', [jcast('int', (Code05_TreelandAndViruses2.MAXN << (1 & 31)))])
Code05_TreelandAndViruses2.cntv = jcast('int', 0)
Code05_TreelandAndViruses2.dep = jarray('int', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.dfn = jarray('int', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.stjump = jarray('int', [Code05_TreelandAndViruses2.MAXN, Code05_TreelandAndViruses2.MAXP])
Code05_TreelandAndViruses2.cntd = jcast('int', 0)
Code05_TreelandAndViruses2.start = jarray('int', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.speed = jarray('int', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.query = jarray('int', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.arr = jarray('int', [jcast('int', (Code05_TreelandAndViruses2.MAXN << (1 & 31)))])
Code05_TreelandAndViruses2.tmp = jarray('int', [jcast('int', (Code05_TreelandAndViruses2.MAXN << (2 & 31)))])
Code05_TreelandAndViruses2.len = jcast('int', 0)
Code05_TreelandAndViruses2.heap = jnew('PriorityQueue', Code05_TreelandAndViruses2.NodeCmp())
Code05_TreelandAndViruses2.vis = jarray('boolean', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.minTime = jarray('int', [Code05_TreelandAndViruses2.MAXN])
Code05_TreelandAndViruses2.findVirus = jarray('int', [Code05_TreelandAndViruses2.MAXN])

if __name__ == '__main__':
    Code05_TreelandAndViruses2.main([])
