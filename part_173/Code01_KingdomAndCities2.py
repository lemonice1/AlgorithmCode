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

# 王国和城市，Python版
# 一共有n个节点，给定n-1条无向边，所有节点组成一棵树
# 一共有q条查询，每条查询格式如下
# 查询 k a1 a2 ... ak : 给出了k个不同的重要点，其他点是非重要点
# 你可以攻占非重要点，被攻占的点无法通行
# 要让重要点两两之间不再连通，打印至少需要攻占几个非重要点
# 如果攻占非重要点无法达成目标，打印-1
# 1 <= n、q <= 10^5
# 1 <= 所有查询给出的点的总数 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF613D
# 测试链接 : https://codeforces.com/problemset/problem/613/D
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_KingdomAndCities2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'q': 'q', 'k': 'k', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headv': 'headv', 'nextv': 'nextv', 'tov': 'tov', 'cntv': 'cntv', 'dep': 'dep', 'dfn': 'dfn', 'stjump': 'stjump', 'cntd': 'cntd', 'arr': 'arr', 'isKey': 'isKey', 'tmp': 'tmp', 'stk': 'stk', 'siz': 'siz', 'cost': 'cost'}
    MAXN = 0
    MAXP = 0
    n = 0
    q = 0
    k = 0
    # 原始树
    headg = None
    nextg = None
    tog = None
    cntg = 0
    # 虚树
    headv = None
    nextv = None
    tov = None
    cntv = 0
    # 树上倍增求LCA + 生成dfn序
    dep = None
    dfn = None
    stjump = None
    cntd = 0
    # 关键点数组
    arr = None
    # 标记节点是否是关键点
    isKey = None
    # 第一种建树方式
    tmp = None
    # 第二种建树方式
    stk = None
    # 动态规划相关
    # siz[u]，还有几个重要点没和u断开，值为0或者1
    # cost[u]，表示节点u的子树中，做到不违规，至少需要攻占几个非重要点
    siz = None
    cost = None
    # 原始树连边
    @staticmethod
    def addEdgeG(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_KingdomAndCities2.nextg, ((_java_obj_1 := Code01_KingdomAndCities2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_KingdomAndCities2.headg[u])
        Code01_KingdomAndCities2.tog[Code01_KingdomAndCities2.cntg] = jcast('int', v)
        Code01_KingdomAndCities2.headg[u] = jcast('int', Code01_KingdomAndCities2.cntg)

    # 虚树连边
    @staticmethod
    def addEdgeV(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_KingdomAndCities2.nextv, ((_java_obj_4 := Code01_KingdomAndCities2), (_java_key_5 := 'cntv'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code01_KingdomAndCities2.headv[u])
        Code01_KingdomAndCities2.tov[Code01_KingdomAndCities2.cntv] = jcast('int', v)
        Code01_KingdomAndCities2.headv[u] = jcast('int', Code01_KingdomAndCities2.cntv)

    # nums中的数，根据dfn的大小排序，手撸双指针快排
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
            while (Code01_KingdomAndCities2.dfn[nums[i]] < Code01_KingdomAndCities2.dfn[pivot]):
                i = jcast('int', (i + 1))
            while (Code01_KingdomAndCities2.dfn[nums[j]] > Code01_KingdomAndCities2.dfn[pivot]):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', nums[i])
                nums[i] = jcast('int', nums[j])
                nums[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code01_KingdomAndCities2.sortByDfn(nums, l, j)
        Code01_KingdomAndCities2.sortByDfn(nums, i, r)

    # 树上倍增的dfs过程
    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code01_KingdomAndCities2.dep[u] = jcast('int', jcast('int', jadd(Code01_KingdomAndCities2.dep[fa], 1)))
        jset(Code01_KingdomAndCities2.dfn, u, ((_java_obj_7 := Code01_KingdomAndCities2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        jset(Code01_KingdomAndCities2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code01_KingdomAndCities2.MAXP):
            jset(Code01_KingdomAndCities2.stjump[u], p, Code01_KingdomAndCities2.stjump[Code01_KingdomAndCities2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code01_KingdomAndCities2.headg[u])
        while (e > 0):
            if (Code01_KingdomAndCities2.tog[e] != fa):
                Code01_KingdomAndCities2.dfs(Code01_KingdomAndCities2.tog[e], u)
            e = jcast('int', Code01_KingdomAndCities2.nextg[e])

    # 返回a和b的最低公共祖先
    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code01_KingdomAndCities2.dep[a] < Code01_KingdomAndCities2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code01_KingdomAndCities2.MAXP - 1)))
        while (p >= 0):
            if (Code01_KingdomAndCities2.dep[Code01_KingdomAndCities2.stjump[a][p]] >= Code01_KingdomAndCities2.dep[b]):
                a = jcast('int', Code01_KingdomAndCities2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code01_KingdomAndCities2.MAXP - 1)))
        while (p >= 0):
            if (Code01_KingdomAndCities2.stjump[a][p] != Code01_KingdomAndCities2.stjump[b][p]):
                a = jcast('int', Code01_KingdomAndCities2.stjump[a][p])
                b = jcast('int', Code01_KingdomAndCities2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code01_KingdomAndCities2.stjump[a][0])

    # 二次排序 + LCA连边的方式建立虚树
    @staticmethod
    def buildVirtualTree1():
        Code01_KingdomAndCities2.sortByDfn(Code01_KingdomAndCities2.arr, 1, Code01_KingdomAndCities2.k)
        len = jcast('int', 0)
        i = jcast('int', 1)
        while (i < Code01_KingdomAndCities2.k):
            jset(Code01_KingdomAndCities2.tmp, (len := jcast('int', (len + (1)))), Code01_KingdomAndCities2.arr[i])
            jset(Code01_KingdomAndCities2.tmp, (len := jcast('int', (len + (1)))), Code01_KingdomAndCities2.getLca(Code01_KingdomAndCities2.arr[i], Code01_KingdomAndCities2.arr[jcast('int', jadd(i, 1))]))
            i = jcast('int', (i + 1))
        jset(Code01_KingdomAndCities2.tmp, (len := jcast('int', (len + (1)))), Code01_KingdomAndCities2.arr[Code01_KingdomAndCities2.k])
        Code01_KingdomAndCities2.sortByDfn(Code01_KingdomAndCities2.tmp, 1, len)
        unique = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= len):
            if (Code01_KingdomAndCities2.tmp[unique] != Code01_KingdomAndCities2.tmp[i]):
                jset(Code01_KingdomAndCities2.tmp, (unique := jcast('int', (unique + (1)))), Code01_KingdomAndCities2.tmp[i])
            i = jcast('int', (i + 1))
        Code01_KingdomAndCities2.cntv = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= unique):
            jset(Code01_KingdomAndCities2.headv, Code01_KingdomAndCities2.tmp[i], 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < unique):
            Code01_KingdomAndCities2.addEdgeV(Code01_KingdomAndCities2.getLca(Code01_KingdomAndCities2.tmp[i], Code01_KingdomAndCities2.tmp[jcast('int', jadd(i, 1))]), Code01_KingdomAndCities2.tmp[jcast('int', jadd(i, 1))])
            i = jcast('int', (i + 1))
        return jcast('int', Code01_KingdomAndCities2.tmp[1])

    # 单调栈的方式建立虚树
    @staticmethod
    def buildVirtualTree2():
        Code01_KingdomAndCities2.sortByDfn(Code01_KingdomAndCities2.arr, 1, Code01_KingdomAndCities2.k)
        Code01_KingdomAndCities2.cntv = jcast('int', 0)
        jset(Code01_KingdomAndCities2.headv, Code01_KingdomAndCities2.arr[1], 0)
        top = jcast('int', 0)
        jset(Code01_KingdomAndCities2.stk, (top := jcast('int', (top + (1)))), Code01_KingdomAndCities2.arr[1])
        i = jcast('int', 2)
        while (i <= Code01_KingdomAndCities2.k):
            x = jcast('int', Code01_KingdomAndCities2.arr[i])
            y = jcast('int', Code01_KingdomAndCities2.stk[top])
            lca = jcast('int', Code01_KingdomAndCities2.getLca(x, y))
            while ((top > 1) and (Code01_KingdomAndCities2.dfn[Code01_KingdomAndCities2.stk[jcast('int', (top - 1))]] >= Code01_KingdomAndCities2.dfn[lca])):
                Code01_KingdomAndCities2.addEdgeV(Code01_KingdomAndCities2.stk[jcast('int', (top - 1))], Code01_KingdomAndCities2.stk[top])
                top = jcast('int', (top - 1))
            if (lca != Code01_KingdomAndCities2.stk[top]):
                Code01_KingdomAndCities2.headv[lca] = jcast('int', 0)
                Code01_KingdomAndCities2.addEdgeV(lca, Code01_KingdomAndCities2.stk[top])
                Code01_KingdomAndCities2.stk[top] = jcast('int', lca)
            Code01_KingdomAndCities2.headv[x] = jcast('int', 0)
            jset(Code01_KingdomAndCities2.stk, (top := jcast('int', (top + (1)))), x)
            i = jcast('int', (i + 1))
        while (top > 1):
            Code01_KingdomAndCities2.addEdgeV(Code01_KingdomAndCities2.stk[jcast('int', (top - 1))], Code01_KingdomAndCities2.stk[top])
            top = jcast('int', (top - 1))
        return jcast('int', Code01_KingdomAndCities2.stk[1])

    # 树型dp的过程
    @staticmethod
    def dp(u):
        u = jcast('int', u)
        jset(Code01_KingdomAndCities2.cost, u, jset(Code01_KingdomAndCities2.siz, u, 0))
        e = jcast('int', Code01_KingdomAndCities2.headv[u])
        while (e > 0):
            v = jcast('int', Code01_KingdomAndCities2.tov[e])
            Code01_KingdomAndCities2.dp(v)
            Code01_KingdomAndCities2.cost[u] = jcast('int', jcast('int', jadd(Code01_KingdomAndCities2.cost[u], Code01_KingdomAndCities2.cost[v])))
            Code01_KingdomAndCities2.siz[u] = jcast('int', jcast('int', jadd(Code01_KingdomAndCities2.siz[u], Code01_KingdomAndCities2.siz[v])))
            e = jcast('int', Code01_KingdomAndCities2.nextv[e])
        if Code01_KingdomAndCities2.isKey[u]:
            Code01_KingdomAndCities2.cost[u] = jcast('int', jcast('int', jadd(Code01_KingdomAndCities2.cost[u], Code01_KingdomAndCities2.siz[u])))
            Code01_KingdomAndCities2.siz[u] = jcast('int', 1)
        else:
            if (Code01_KingdomAndCities2.siz[u] > 1):
                Code01_KingdomAndCities2.cost[u] = jcast('int', (Code01_KingdomAndCities2.cost[u] + 1))
                Code01_KingdomAndCities2.siz[u] = jcast('int', 0)

    @staticmethod
    def compute():
        # 节点标记关键点信息
        i = jcast('int', 1)
        while (i <= Code01_KingdomAndCities2.k):
            jset(Code01_KingdomAndCities2.isKey, Code01_KingdomAndCities2.arr[i], True)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code01_KingdomAndCities2.k):
            try:
                # 只能通过攻占非关键点的方式，来隔开关键点
                # 所以如果 a 和 a的父节点 都是关键点，这是怎么也隔不开的
                # 直接返回-1即可
                if Code01_KingdomAndCities2.isKey[Code01_KingdomAndCities2.stjump[Code01_KingdomAndCities2.arr[i]][0]]:
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        ans = jcast('int', jcast('int', (-1)))
        if check:
            tree = jcast('int', Code01_KingdomAndCities2.buildVirtualTree1())
            # int tree = buildVirtualTree2();
            Code01_KingdomAndCities2.dp(tree)
            ans = jcast('int', Code01_KingdomAndCities2.cost[tree])
        # 节点撤销关键点信息
        i = jcast('int', 1)
        while (i <= Code01_KingdomAndCities2.k):
            jset(Code01_KingdomAndCities2.isKey, Code01_KingdomAndCities2.arr[i], False)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code01_KingdomAndCities2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_KingdomAndCities2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_KingdomAndCities2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code01_KingdomAndCities2.addEdgeG(u, v)
            Code01_KingdomAndCities2.addEdgeG(v, u)
            i = jcast('int', (i + 1))
        Code01_KingdomAndCities2.dfs(1, 0)
        Code01_KingdomAndCities2.q = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', 1)
        while (t <= Code01_KingdomAndCities2.q):
            Code01_KingdomAndCities2.k = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code01_KingdomAndCities2.k):
                jset(Code01_KingdomAndCities2.arr, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code01_KingdomAndCities2.compute())
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code01_KingdomAndCities2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_KingdomAndCities2.MAXN = jcast('int', 100001)
Code01_KingdomAndCities2.MAXP = jcast('int', 20)
Code01_KingdomAndCities2.n = jcast('int', 0)
Code01_KingdomAndCities2.q = jcast('int', 0)
Code01_KingdomAndCities2.k = jcast('int', 0)
Code01_KingdomAndCities2.headg = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.nextg = jarray('int', [jcast('int', (Code01_KingdomAndCities2.MAXN << (1 & 31)))])
Code01_KingdomAndCities2.tog = jarray('int', [jcast('int', (Code01_KingdomAndCities2.MAXN << (1 & 31)))])
Code01_KingdomAndCities2.cntg = jcast('int', 0)
Code01_KingdomAndCities2.headv = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.nextv = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.tov = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.cntv = jcast('int', 0)
Code01_KingdomAndCities2.dep = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.dfn = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.stjump = jarray('int', [Code01_KingdomAndCities2.MAXN, Code01_KingdomAndCities2.MAXP])
Code01_KingdomAndCities2.cntd = jcast('int', 0)
Code01_KingdomAndCities2.arr = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.isKey = jarray('boolean', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.tmp = jarray('int', [jcast('int', (Code01_KingdomAndCities2.MAXN << (1 & 31)))])
Code01_KingdomAndCities2.stk = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.siz = jarray('int', [Code01_KingdomAndCities2.MAXN])
Code01_KingdomAndCities2.cost = jarray('int', [Code01_KingdomAndCities2.MAXN])

if __name__ == '__main__':
    Code01_KingdomAndCities2.main([])
