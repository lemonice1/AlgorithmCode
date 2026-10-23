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

# 世界树，Python版
# 一共有n个节点，给定n-1条无向边，所有节点组成一棵树
# 一共有q条查询，每条查询格式如下
# 查询 k a1 a2 ... ak : 给出了k个不同的管理点，树上每个点都找最近的管理点来管理自己
# 如果某个节点的最近管理点有多个，选择编号最小的管理点
# 打印每个管理点，管理的节点数量
# 1 <= n、q <= 3 * 10^5
# 1 <= 所有查询给出的点的总数 <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3233
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本题递归函数较多：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 下面继续减少状态存储和常数开销
# 对应实现可参考 Code04_WorldTree2.py
# 两个版本保留相同的算法逻辑
class Code04_WorldTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'q': 'q', 'k': 'k', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headv': 'headv', 'nextv': 'nextv', 'tov': 'tov', 'cntv': 'cntv', 'dep': 'dep', 'siz': 'siz', 'dfn': 'dfn', 'stjump': 'stjump', 'cntd': 'cntd', 'order': 'order', 'arr': 'arr', 'isKey': 'isKey', 'tmp': 'tmp', 'manager': 'manager', 'dist': 'dist', 'ans': 'ans'}
    MAXN = 0
    MAXP = 0
    n = 0
    q = 0
    k = 0
    headg = None
    nextg = None
    tog = None
    cntg = 0
    headv = None
    nextv = None
    tov = None
    cntv = 0
    dep = None
    # 注意siz[u]表示在原树里，子树u有几个节点
    siz = None
    dfn = None
    stjump = None
    cntd = 0
    order = None
    arr = None
    isKey = None
    tmp = None
    # manager[u]表示u节点找到的最近管理点
    manager = None
    # dist[u]表示u节点到最近管理点的距离
    dist = None
    # ans[i]表示i这个管理点，管理了几个点
    ans = None
    @staticmethod
    def addEdgeG(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_WorldTree1.nextg, ((_java_obj_1 := Code04_WorldTree1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_WorldTree1.headg[u])
        Code04_WorldTree1.tog[Code04_WorldTree1.cntg] = jcast('int', v)
        Code04_WorldTree1.headg[u] = jcast('int', Code04_WorldTree1.cntg)

    @staticmethod
    def addEdgeV(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_WorldTree1.nextv, ((_java_obj_4 := Code04_WorldTree1), (_java_key_5 := 'cntv'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_WorldTree1.headv[u])
        Code04_WorldTree1.tov[Code04_WorldTree1.cntv] = jcast('int', v)
        Code04_WorldTree1.headv[u] = jcast('int', Code04_WorldTree1.cntv)

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
            while (Code04_WorldTree1.dfn[nums[i]] < Code04_WorldTree1.dfn[pivot]):
                i = jcast('int', (i + 1))
            while (Code04_WorldTree1.dfn[nums[j]] > Code04_WorldTree1.dfn[pivot]):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', nums[i])
                nums[i] = jcast('int', nums[j])
                nums[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code04_WorldTree1.sortByDfn(nums, l, j)
        Code04_WorldTree1.sortByDfn(nums, i, r)

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_WorldTree1.dep[u] = jcast('int', jcast('int', jadd(Code04_WorldTree1.dep[fa], 1)))
        Code04_WorldTree1.siz[u] = jcast('int', 1)
        jset(Code04_WorldTree1.dfn, u, ((_java_obj_7 := Code04_WorldTree1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        jset(Code04_WorldTree1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code04_WorldTree1.MAXP):
            jset(Code04_WorldTree1.stjump[u], p, Code04_WorldTree1.stjump[Code04_WorldTree1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code04_WorldTree1.headg[u])
        while (e > 0):
            v = jcast('int', Code04_WorldTree1.tog[e])
            if (v != fa):
                Code04_WorldTree1.dfs(v, u)
                Code04_WorldTree1.siz[u] = jcast('int', jcast('int', jadd(Code04_WorldTree1.siz[u], Code04_WorldTree1.siz[v])))
            e = jcast('int', Code04_WorldTree1.nextg[e])

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code04_WorldTree1.dep[a] < Code04_WorldTree1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code04_WorldTree1.MAXP - 1)))
        while (p >= 0):
            if (Code04_WorldTree1.dep[Code04_WorldTree1.stjump[a][p]] >= Code04_WorldTree1.dep[b]):
                a = jcast('int', Code04_WorldTree1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code04_WorldTree1.MAXP - 1)))
        while (p >= 0):
            if (Code04_WorldTree1.stjump[a][p] != Code04_WorldTree1.stjump[b][p]):
                a = jcast('int', Code04_WorldTree1.stjump[a][p])
                b = jcast('int', Code04_WorldTree1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code04_WorldTree1.stjump[a][0])

    @staticmethod
    def buildVirtualTree():
        Code04_WorldTree1.sortByDfn(Code04_WorldTree1.arr, 1, Code04_WorldTree1.k)
        # 一定要加入1号点
        # 因为题目问的是所有节点的归属问题
        len = jcast('int', 0)
        jset(Code04_WorldTree1.tmp, (len := jcast('int', (len + (1)))), 1)
        i = jcast('int', 1)
        while (i < Code04_WorldTree1.k):
            jset(Code04_WorldTree1.tmp, (len := jcast('int', (len + (1)))), Code04_WorldTree1.arr[i])
            jset(Code04_WorldTree1.tmp, (len := jcast('int', (len + (1)))), Code04_WorldTree1.getLca(Code04_WorldTree1.arr[i], Code04_WorldTree1.arr[jcast('int', jadd(i, 1))]))
            i = jcast('int', (i + 1))
        jset(Code04_WorldTree1.tmp, (len := jcast('int', (len + (1)))), Code04_WorldTree1.arr[Code04_WorldTree1.k])
        Code04_WorldTree1.sortByDfn(Code04_WorldTree1.tmp, 1, len)
        unique = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= len):
            if (Code04_WorldTree1.tmp[unique] != Code04_WorldTree1.tmp[i]):
                jset(Code04_WorldTree1.tmp, (unique := jcast('int', (unique + (1)))), Code04_WorldTree1.tmp[i])
            i = jcast('int', (i + 1))
        Code04_WorldTree1.cntv = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= unique):
            jset(Code04_WorldTree1.headv, Code04_WorldTree1.tmp[i], 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < unique):
            Code04_WorldTree1.addEdgeV(Code04_WorldTree1.getLca(Code04_WorldTree1.tmp[i], Code04_WorldTree1.tmp[jcast('int', jadd(i, 1))]), Code04_WorldTree1.tmp[jcast('int', jadd(i, 1))])
            i = jcast('int', (i + 1))
        return jcast('int', Code04_WorldTree1.tmp[1])

    # 下方找最近管理点，节点u根据孩子的管理点，找到离u最近的管理点
    @staticmethod
    def dp1(u):
        u = jcast('int', u)
        Code04_WorldTree1.dist[u] = jcast('int', 1000000001)
        e = jcast('int', Code04_WorldTree1.headv[u])
        while (e > 0):
            v = jcast('int', Code04_WorldTree1.tov[e])
            Code04_WorldTree1.dp1(v)
            w = jcast('int', jcast('int', (Code04_WorldTree1.dep[v] - Code04_WorldTree1.dep[u])))
            if ((jcast('int', jadd(Code04_WorldTree1.dist[v], w)) < Code04_WorldTree1.dist[u]) or ((jcast('int', jadd(Code04_WorldTree1.dist[v], w)) == Code04_WorldTree1.dist[u]) and (Code04_WorldTree1.manager[v] < Code04_WorldTree1.manager[u]))):
                Code04_WorldTree1.dist[u] = jcast('int', jcast('int', jadd(Code04_WorldTree1.dist[v], w)))
                Code04_WorldTree1.manager[u] = jcast('int', Code04_WorldTree1.manager[v])
            e = jcast('int', Code04_WorldTree1.nextv[e])
        if Code04_WorldTree1.isKey[u]:
            Code04_WorldTree1.dist[u] = jcast('int', 0)
            Code04_WorldTree1.manager[u] = jcast('int', u)

    # 上方找最近管理点，根据u找到的最近管理点，更新每个孩子节点v的最近管理点
    @staticmethod
    def dp2(u):
        u = jcast('int', u)
        e = jcast('int', Code04_WorldTree1.headv[u])
        while (e > 0):
            v = jcast('int', Code04_WorldTree1.tov[e])
            w = jcast('int', jcast('int', (Code04_WorldTree1.dep[v] - Code04_WorldTree1.dep[u])))
            if ((jcast('int', jadd(Code04_WorldTree1.dist[u], w)) < Code04_WorldTree1.dist[v]) or ((jcast('int', jadd(Code04_WorldTree1.dist[u], w)) == Code04_WorldTree1.dist[v]) and (Code04_WorldTree1.manager[u] < Code04_WorldTree1.manager[v]))):
                Code04_WorldTree1.dist[v] = jcast('int', jcast('int', jadd(Code04_WorldTree1.dist[u], w)))
                Code04_WorldTree1.manager[v] = jcast('int', Code04_WorldTree1.manager[u])
            Code04_WorldTree1.dp2(v)
            e = jcast('int', Code04_WorldTree1.nextv[e])

    # 已知u一定是v的祖先节点，u到v之间的大量节点没有被纳入到虚树
    # 这部分节点之前都分配给了manager[u]，现在根据最近距离做重新分配
    # 可能若干节点会重新分配给manager[v]，修正相关的计数
    @staticmethod
    def amend(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        if (Code04_WorldTree1.manager[u] == Code04_WorldTree1.manager[v]):
            return
        x = jcast('int', v)
        p = jcast('int', jcast('int', (Code04_WorldTree1.MAXP - 1)))
        while (p >= 0):
            jump = jcast('int', Code04_WorldTree1.stjump[x][p])
            if (Code04_WorldTree1.dep[u] < Code04_WorldTree1.dep[jump]):
                tou = jcast('int', jcast('int', jadd(jcast('int', (Code04_WorldTree1.dep[jump] - Code04_WorldTree1.dep[u])), Code04_WorldTree1.dist[u])))
                tov = jcast('int', jcast('int', jadd(jcast('int', (Code04_WorldTree1.dep[v] - Code04_WorldTree1.dep[jump])), Code04_WorldTree1.dist[v])))
                if ((tov < tou) or ((tov == tou) and (Code04_WorldTree1.manager[v] < Code04_WorldTree1.manager[u]))):
                    x = jcast('int', jump)
            p = jcast('int', (p - 1))
        delta = jcast('int', jcast('int', (Code04_WorldTree1.siz[x] - Code04_WorldTree1.siz[v])))
        ((_java_obj_10 := Code04_WorldTree1.ans), (_java_key_11 := Code04_WorldTree1.manager[u]), jset(_java_obj_10, _java_key_11, jcast('int', (jget(_java_obj_10, _java_key_11) - delta))))[2]
        ((_java_obj_12 := Code04_WorldTree1.ans), (_java_key_13 := Code04_WorldTree1.manager[v]), jset(_java_obj_12, _java_key_13, jcast('int', jadd(jget(_java_obj_12, _java_key_13), delta))))[2]

    # 每个点都有了最近的管理点，更新相关管理点的管理节点计数
    @staticmethod
    def dp3(u):
        u = jcast('int', u)
        # u的管理节点，先获得原树里子树u的所有节点
        # 然后经历修正的过程，把管理节点的数量更新正确
        ((_java_obj_14 := Code04_WorldTree1.ans), (_java_key_15 := Code04_WorldTree1.manager[u]), jset(_java_obj_14, _java_key_15, jcast('int', jadd(jget(_java_obj_14, _java_key_15), Code04_WorldTree1.siz[u]))))[2]
        e = jcast('int', Code04_WorldTree1.headv[u])
        while (e > 0):
            v = jcast('int', Code04_WorldTree1.tov[e])
            # 修正的过程
            Code04_WorldTree1.amend(u, v)
            # 马上要执行dp3(v)，所以子树v的节点现在扣除
            ((_java_obj_16 := Code04_WorldTree1.ans), (_java_key_17 := Code04_WorldTree1.manager[u]), jset(_java_obj_16, _java_key_17, jcast('int', (jget(_java_obj_16, _java_key_17) - Code04_WorldTree1.siz[v]))))[2]
            # 子树v怎么分配节点，那是后续dp3(v)的事情
            Code04_WorldTree1.dp3(v)
            e = jcast('int', Code04_WorldTree1.nextv[e])

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code04_WorldTree1.k):
            Code04_WorldTree1.arr[i] = jcast('int', Code04_WorldTree1.order[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_WorldTree1.k):
            jset(Code04_WorldTree1.isKey, Code04_WorldTree1.arr[i], True)
            jset(Code04_WorldTree1.ans, Code04_WorldTree1.arr[i], 0)
            i = jcast('int', (i + 1))
        tree = jcast('int', Code04_WorldTree1.buildVirtualTree())
        Code04_WorldTree1.dp1(tree)
        Code04_WorldTree1.dp2(tree)
        Code04_WorldTree1.dp3(tree)
        i = jcast('int', 1)
        while (i <= Code04_WorldTree1.k):
            jset(Code04_WorldTree1.isKey, Code04_WorldTree1.arr[i], False)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code04_WorldTree1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_WorldTree1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code04_WorldTree1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_WorldTree1.addEdgeG(u, v)
            Code04_WorldTree1.addEdgeG(v, u)
            i = jcast('int', (i + 1))
        Code04_WorldTree1.dfs(1, 0)
        Code04_WorldTree1.q = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', 1)
        while (t <= Code04_WorldTree1.q):
            Code04_WorldTree1.k = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code04_WorldTree1.k):
                jset(Code04_WorldTree1.order, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            Code04_WorldTree1.compute()
            i = jcast('int', 1)
            while (i <= Code04_WorldTree1.k):
                jcall(out, 'print', jadd(Code04_WorldTree1.ans[Code04_WorldTree1.order[i]], ' '))
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
            return jcast('int', self.buffer[((_java_obj_18 := self), (_java_key_19 := 'ptr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))), _java_old_20)[4]])

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
            raise TypeError("No matching overload for Code04_WorldTree1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_WorldTree1.MAXN = jcast('int', 300001)
Code04_WorldTree1.MAXP = jcast('int', 20)
Code04_WorldTree1.n = jcast('int', 0)
Code04_WorldTree1.q = jcast('int', 0)
Code04_WorldTree1.k = jcast('int', 0)
Code04_WorldTree1.headg = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.nextg = jarray('int', [jcast('int', (Code04_WorldTree1.MAXN << (1 & 31)))])
Code04_WorldTree1.tog = jarray('int', [jcast('int', (Code04_WorldTree1.MAXN << (1 & 31)))])
Code04_WorldTree1.cntg = jcast('int', 0)
Code04_WorldTree1.headv = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.nextv = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.tov = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.cntv = jcast('int', 0)
Code04_WorldTree1.dep = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.siz = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.dfn = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.stjump = jarray('int', [Code04_WorldTree1.MAXN, Code04_WorldTree1.MAXP])
Code04_WorldTree1.cntd = jcast('int', 0)
Code04_WorldTree1.order = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.arr = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.isKey = jarray('boolean', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.tmp = jarray('int', [jcast('int', (Code04_WorldTree1.MAXN << (1 & 31)))])
Code04_WorldTree1.manager = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.dist = jarray('int', [Code04_WorldTree1.MAXN])
Code04_WorldTree1.ans = jarray('int', [Code04_WorldTree1.MAXN])

if __name__ == '__main__':
    Code04_WorldTree1.main([])
