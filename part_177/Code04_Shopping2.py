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

# 树上购物，Python版
# 一共有n个商店，有n-1条路构成一棵树，第i个商店只卖第i种物品
# 给定每种物品三个属性，价值v[i]、单价c[i]、数量d[i]
# 你逛商店可能会购买物品，要求所有买过东西的商店，在树上必须连通
# 你有m元，打印能获得的最大价值总和
# 1 <= n <= 500    1 <= m <= 4000    1 <= d[i] <= 2000
# 测试链接 : https://www.luogu.com.cn/problem/P6326
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Shopping2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 't': 't', 'n': 'n', 'm': 'm', 'v': 'v', 'c': 'c', 'd': 'd', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'nodeArr': 'nodeArr', 'endDfn': 'endDfn', 'cntd': 'cntd', 'val': 'val', 'cost': 'cost', 'dp': 'dp'}
    MAXN = 0
    MAXM = 0
    t = 0
    n = 0
    m = 0
    v = None
    c = None
    d = None
    head = None
    nxt = None
    to = None
    cntg = 0
    vis = None
    siz = None
    nodeArr = None
    endDfn = None
    cntd = 0
    val = None
    cost = None
    dp = None
    @staticmethod
    def prepare():
        Code04_Shopping2.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Shopping2.n):
            Code04_Shopping2.head[i] = jcast('int', 0)
            Code04_Shopping2.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_Shopping2.nxt, ((_java_obj_1 := Code04_Shopping2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Shopping2.head[u])
        Code04_Shopping2.to[Code04_Shopping2.cntg] = jcast('int', v)
        Code04_Shopping2.head[u] = jcast('int', Code04_Shopping2.cntg)

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_Shopping2.siz[u] = jcast('int', 1)
        e = jcast('int', Code04_Shopping2.head[u])
        while (e > 0):
            v = jcast('int', Code04_Shopping2.to[e])
            if ((v != fa) and (not Code04_Shopping2.vis[v])):
                Code04_Shopping2.getSize(v, u)
                Code04_Shopping2.siz[u] = jcast('int', jcast('int', jadd(Code04_Shopping2.siz[u], Code04_Shopping2.siz[v])))
            e = jcast('int', Code04_Shopping2.nxt[e])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_Shopping2.getSize(u, fa)
        half = jcast('int', jcast('int', (Code04_Shopping2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code04_Shopping2.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code04_Shopping2.to[e])
                        if (((v != fa) and (not Code04_Shopping2.vis[v])) and (Code04_Shopping2.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code04_Shopping2.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code04_Shopping2.nodeArr, ((_java_obj_6 := Code04_Shopping2), (_java_key_7 := 'cntd'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3], u)
        e = jcast('int', Code04_Shopping2.head[u])
        while (e > 0):
            v = jcast('int', Code04_Shopping2.to[e])
            if ((v != fa) and (not Code04_Shopping2.vis[v])):
                Code04_Shopping2.dfs(v, u)
            e = jcast('int', Code04_Shopping2.nxt[e])
        Code04_Shopping2.endDfn[u] = jcast('int', Code04_Shopping2.cntd)

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        Code04_Shopping2.cntd = jcast('int', 0)
        Code04_Shopping2.dfs(u, 0)
        i = jcast('int', Code04_Shopping2.cntd)
        while (i > 0):
            cur = jcast('int', Code04_Shopping2.nodeArr[i])
            # 二进制分组优化，注意物品量-1，然后二进制分组
            # 先必选一件，然后考虑更多件，课上解释了为什么
            cnt = jcast('int', jcast('int', (Code04_Shopping2.d[cur] - 1)))
            num = jcast('int', 0)
            k = jcast('int', 1)
            while (k <= cnt):
                jset(Code04_Shopping2.val, (num := jcast('int', (num + (1)))), jcast('int', (Code04_Shopping2.v[cur] * k)))
                Code04_Shopping2.cost[num] = jcast('int', jcast('int', (Code04_Shopping2.c[cur] * k)))
                cnt = jcast('int', jcast('int', (cnt - k)))
                k = jcast('int', jcast('int', (k << (1 & 31))))
            if (cnt > 0):
                jset(Code04_Shopping2.val, (num := jcast('int', (num + (1)))), jcast('int', (Code04_Shopping2.v[cur] * cnt)))
                Code04_Shopping2.cost[num] = jcast('int', jcast('int', (Code04_Shopping2.c[cur] * cnt)))
            # 必选cur的情况，先必选一件
            j = jcast('int', Code04_Shopping2.m)
            while (j >= Code04_Shopping2.c[cur]):
                jset(Code04_Shopping2.dp[i], j, jcast('int', jadd(Code04_Shopping2.dp[jcast('int', jadd(i, 1))][jcast('int', (j - Code04_Shopping2.c[cur]))], Code04_Shopping2.v[cur])))
                j = jcast('int', (j - 1))
            # 然后用二进制分组，拼出可能的更多件
            k = jcast('int', 1)
            while (k <= num):
                j = jcast('int', Code04_Shopping2.m)
                while (j >= Code04_Shopping2.cost[k]):
                    jset(Code04_Shopping2.dp[i], j, jstatic('Math', 'max', Code04_Shopping2.dp[i][j], jcast('int', jadd(Code04_Shopping2.dp[i][jcast('int', (j - Code04_Shopping2.cost[k]))], Code04_Shopping2.val[k]))))
                    j = jcast('int', (j - 1))
                k = jcast('int', (k + 1))
            # 不选cur的情况，那么cur的子树都跳过，直接跳到endDfn[cur] + 1
            j = jcast('int', 0)
            while (j <= Code04_Shopping2.m):
                jset(Code04_Shopping2.dp[i], j, jstatic('Math', 'max', Code04_Shopping2.dp[i][j], Code04_Shopping2.dp[jcast('int', jadd(Code04_Shopping2.endDfn[cur], 1))][j]))
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        ans = jcast('int', Code04_Shopping2.dp[1][Code04_Shopping2.m])
        # 返回之前清空
        i = jcast('int', 1)
        while (i <= Code04_Shopping2.cntd):
            j = jcast('int', 0)
            while (j <= Code04_Shopping2.m):
                jset(Code04_Shopping2.dp[i], j, 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code04_Shopping2.vis[u] = jcast('boolean', True)
        ans = jcast('int', Code04_Shopping2.calc(u))
        e = jcast('int', Code04_Shopping2.head[u])
        while (e > 0):
            v = jcast('int', Code04_Shopping2.to[e])
            if (not Code04_Shopping2.vis[v]):
                ans = jcast('int', jstatic('Math', 'max', ans, Code04_Shopping2.solve(Code04_Shopping2.getCentroid(v, u))))
            e = jcast('int', Code04_Shopping2.nxt[e])
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code04_Shopping2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Shopping2.t = jcast('int', jcall(in_, 'nextInt'))
        k = jcast('int', 1)
        while (k <= Code04_Shopping2.t):
            Code04_Shopping2.n = jcast('int', jcall(in_, 'nextInt'))
            Code04_Shopping2.m = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code04_Shopping2.n):
                jset(Code04_Shopping2.v, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code04_Shopping2.n):
                jset(Code04_Shopping2.c, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code04_Shopping2.n):
                jset(Code04_Shopping2.d, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            Code04_Shopping2.prepare()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i < Code04_Shopping2.n):
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code04_Shopping2.addEdge(u, v)
                Code04_Shopping2.addEdge(v, u)
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_Shopping2.solve(Code04_Shopping2.getCentroid(1, 0)))
            k = jcast('int', (k + 1))
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
            return jcast('int', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

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
            raise TypeError("No matching overload for Code04_Shopping2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Shopping2.MAXN = jcast('int', 501)
Code04_Shopping2.MAXM = jcast('int', 4001)
Code04_Shopping2.t = jcast('int', 0)
Code04_Shopping2.n = jcast('int', 0)
Code04_Shopping2.m = jcast('int', 0)
Code04_Shopping2.v = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.c = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.d = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.head = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.nxt = jarray('int', [jcast('int', (Code04_Shopping2.MAXN << (1 & 31)))])
Code04_Shopping2.to = jarray('int', [jcast('int', (Code04_Shopping2.MAXN << (1 & 31)))])
Code04_Shopping2.cntg = jcast('int', 0)
Code04_Shopping2.vis = jarray('boolean', [Code04_Shopping2.MAXN])
Code04_Shopping2.siz = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.nodeArr = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.endDfn = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.cntd = jcast('int', 0)
Code04_Shopping2.val = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.cost = jarray('int', [Code04_Shopping2.MAXN])
Code04_Shopping2.dp = jarray('int', [jcast('int', jadd(Code04_Shopping2.MAXN, 1)), Code04_Shopping2.MAXM])

if __name__ == '__main__':
    Code04_Shopping2.main([])
