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

# 相近点对的数量，Python版
# 一共有n个节点，所有节点组成一棵树，1号节点是树头
# 从2号点开始，给定每个点的父节点编号、与父节点之间无向边的边权
# 给定两个整数limitl、limitw，要求两点之间的简单路径满足如下关系
# 路径权值和 <= limitw、路径边数 <= limitl，求出这样的点对数量
# 本题规定(x, x)不是点对，(x, y)和(y, x)认为是同一个点对
# 1 <= limitl <= n <= 10^5    0 <= limitw <= 10^9    0 <= 边权 <= 10^4
# 测试链接 : https://www.luogu.com.cn/problem/CF293E
# 测试链接 : https://codeforces.com/problemset/problem/293/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_CloseVertices2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'limitl': 'limitl', 'limitw': 'limitw', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'disArr': 'disArr', 'edgeArr': 'edgeArr', 'cnta': 'cnta', 'tree': 'tree'}
    MAXN = 0
    n = 0
    limitl = 0
    limitw = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    vis = None
    siz = None
    disArr = None
    edgeArr = None
    cnta = 0
    # 树状数组
    # 下标是边数，统计节点个数
    # 但是注意，边数从0开始，而树状数组的下标从1开始
    # 所以每次的入参i，需要i++进行平移
    tree = None
    @staticmethod
    def sort(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code05_CloseVertices2.disArr[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (Code05_CloseVertices2.disArr[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code05_CloseVertices2.disArr[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', Code05_CloseVertices2.disArr[i])
                Code05_CloseVertices2.disArr[i] = jcast('int', Code05_CloseVertices2.disArr[j])
                Code05_CloseVertices2.disArr[j] = jcast('int', tmp)
                tmp = jcast('int', Code05_CloseVertices2.edgeArr[i])
                Code05_CloseVertices2.edgeArr[i] = jcast('int', Code05_CloseVertices2.edgeArr[j])
                Code05_CloseVertices2.edgeArr[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code05_CloseVertices2.sort(l, j)
        Code05_CloseVertices2.sort(i, r)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code05_CloseVertices2.nxt, ((_java_obj_1 := Code05_CloseVertices2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_CloseVertices2.head[u])
        Code05_CloseVertices2.to[Code05_CloseVertices2.cntg] = jcast('int', v)
        Code05_CloseVertices2.weight[Code05_CloseVertices2.cntg] = jcast('int', w)
        Code05_CloseVertices2.head[u] = jcast('int', Code05_CloseVertices2.cntg)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        # 平移
        i = jcast('int', (i + 1))
        while (i <= jcast('int', jadd(Code05_CloseVertices2.limitl, 1))):
            Code05_CloseVertices2.tree[i] = jcast('int', jcast('int', jadd(Code05_CloseVertices2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code05_CloseVertices2.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        # 平移
        i = jcast('int', (i + 1))
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code05_CloseVertices2.tree[i])))
            i = jcast('int', jcast('int', (i - Code05_CloseVertices2.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_CloseVertices2.siz[u] = jcast('int', 1)
        e = jcast('int', Code05_CloseVertices2.head[u])
        while (e > 0):
            v = jcast('int', Code05_CloseVertices2.to[e])
            if ((v != fa) and (not Code05_CloseVertices2.vis[v])):
                Code05_CloseVertices2.getSize(v, u)
                Code05_CloseVertices2.siz[u] = jcast('int', jcast('int', jadd(Code05_CloseVertices2.siz[u], Code05_CloseVertices2.siz[v])))
            e = jcast('int', Code05_CloseVertices2.nxt[e])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_CloseVertices2.getSize(u, fa)
        half = jcast('int', jcast('int', (Code05_CloseVertices2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code05_CloseVertices2.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code05_CloseVertices2.to[e])
                        if (((v != fa) and (not Code05_CloseVertices2.vis[v])) and (Code05_CloseVertices2.siz[v] > half)):
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
                    e = jcast('int', Code05_CloseVertices2.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def dfs(u, fa, dis, edge):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dis = jcast('int', dis)
        edge = jcast('int', edge)
        if ((dis > Code05_CloseVertices2.limitw) or (edge > Code05_CloseVertices2.limitl)):
            return
        jset(Code05_CloseVertices2.disArr, ((_java_obj_6 := Code05_CloseVertices2), (_java_key_7 := 'cnta'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3], dis)
        Code05_CloseVertices2.edgeArr[Code05_CloseVertices2.cnta] = jcast('int', edge)
        e = jcast('int', Code05_CloseVertices2.head[u])
        while (e > 0):
            v = jcast('int', Code05_CloseVertices2.to[e])
            if ((v != fa) and (not Code05_CloseVertices2.vis[v])):
                Code05_CloseVertices2.dfs(v, u, jcast('int', jadd(dis, Code05_CloseVertices2.weight[e])), jcast('int', jadd(edge, 1)))
            e = jcast('int', Code05_CloseVertices2.nxt[e])

    # 从真正的头来到u时，路径权值和为dis，边的数量为edge
    # 子树u上的点对(x, y)，需要走过，x -> 真正的头 -> y
    # 返回 路径权值和<=limitw、路径边数<=limitwl 的点对数量
    @staticmethod
    def calc(u, dis, edge):
        u = jcast('int', u)
        dis = jcast('int', dis)
        edge = jcast('int', edge)
        Code05_CloseVertices2.cnta = jcast('int', 0)
        Code05_CloseVertices2.dfs(u, 0, dis, edge)
        Code05_CloseVertices2.sort(1, Code05_CloseVertices2.cnta)
        i = jcast('int', 1)
        while (i <= Code05_CloseVertices2.cnta):
            Code05_CloseVertices2.add(Code05_CloseVertices2.edgeArr[i], 1)
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        l = jcast('int', 1)
        r = jcast('int', Code05_CloseVertices2.cnta)
        while (l <= r):
            if (jcast('int', jadd(Code05_CloseVertices2.disArr[l], Code05_CloseVertices2.disArr[r])) <= Code05_CloseVertices2.limitw):
                Code05_CloseVertices2.add(Code05_CloseVertices2.edgeArr[l], jcast('int', (-1)))
                ans = jcast('long', jcast('long', jadd(ans, Code05_CloseVertices2.sum(jcast('int', (Code05_CloseVertices2.limitl - Code05_CloseVertices2.edgeArr[l]))))))
                l = jcast('int', (l + 1))
            else:
                Code05_CloseVertices2.add(Code05_CloseVertices2.edgeArr[r], jcast('int', (-1)))
                r = jcast('int', (r - 1))
        return jcast('long', ans)

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code05_CloseVertices2.vis[u] = jcast('boolean', True)
        ans = jcast('long', Code05_CloseVertices2.calc(u, 0, 0))
        e = jcast('int', Code05_CloseVertices2.head[u])
        while (e > 0):
            v = jcast('int', Code05_CloseVertices2.to[e])
            if (not Code05_CloseVertices2.vis[v]):
                ans = jcast('long', jcast('long', (ans - Code05_CloseVertices2.calc(v, Code05_CloseVertices2.weight[e], 1))))
                ans = jcast('long', jcast('long', jadd(ans, Code05_CloseVertices2.solve(Code05_CloseVertices2.getCentroid(v, u)))))
            e = jcast('int', Code05_CloseVertices2.nxt[e])
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code05_CloseVertices2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_CloseVertices2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_CloseVertices2.limitl = jcast('int', jcall(in_, 'nextInt'))
        Code05_CloseVertices2.limitw = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 2)
        fa = 0
        w = 0
        while (i <= Code05_CloseVertices2.n):
            fa = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code05_CloseVertices2.addEdge(i, fa, w)
            Code05_CloseVertices2.addEdge(fa, i, w)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_CloseVertices2.solve(Code05_CloseVertices2.getCentroid(1, 0)))
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
            raise TypeError("No matching overload for Code05_CloseVertices2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_CloseVertices2.MAXN = jcast('int', 100002)
Code05_CloseVertices2.n = jcast('int', 0)
Code05_CloseVertices2.limitl = jcast('int', 0)
Code05_CloseVertices2.limitw = jcast('int', 0)
Code05_CloseVertices2.head = jarray('int', [Code05_CloseVertices2.MAXN])
Code05_CloseVertices2.nxt = jarray('int', [jcast('int', (Code05_CloseVertices2.MAXN << (1 & 31)))])
Code05_CloseVertices2.to = jarray('int', [jcast('int', (Code05_CloseVertices2.MAXN << (1 & 31)))])
Code05_CloseVertices2.weight = jarray('int', [jcast('int', (Code05_CloseVertices2.MAXN << (1 & 31)))])
Code05_CloseVertices2.cntg = jcast('int', 0)
Code05_CloseVertices2.vis = jarray('boolean', [Code05_CloseVertices2.MAXN])
Code05_CloseVertices2.siz = jarray('int', [Code05_CloseVertices2.MAXN])
Code05_CloseVertices2.disArr = jarray('int', [Code05_CloseVertices2.MAXN])
Code05_CloseVertices2.edgeArr = jarray('int', [Code05_CloseVertices2.MAXN])
Code05_CloseVertices2.cnta = jcast('int', 0)
Code05_CloseVertices2.tree = jarray('int', [Code05_CloseVertices2.MAXN])

if __name__ == '__main__':
    Code05_CloseVertices2.main([])
