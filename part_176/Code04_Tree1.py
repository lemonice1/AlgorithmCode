# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 距离<=k的点对数量，Python版
# 一共有n个节点，给定n-1条边，每条边有边权，所有节点组成一棵树
# 给定数字k，求出树上两点距离<=k的点对数量
# 本题规定(x, x)不是点对，(x, y)和(y, x)认为是同一个点对
# 1 <= n <= 4 * 10^4
# 0 <= 边权 <= 10^3
# 0 <= k <= 2 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P4178
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Tree1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'disArr': 'disArr', 'cnta': 'cnta'}
    MAXN = 0
    n = 0
    k = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    vis = None
    siz = None
    disArr = None
    cnta = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_Tree1.nxt, ((_java_obj_1 := Code04_Tree1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Tree1.head[u])
        Code04_Tree1.to[Code04_Tree1.cntg] = jcast('int', v)
        Code04_Tree1.weight[Code04_Tree1.cntg] = jcast('int', w)
        Code04_Tree1.head[u] = jcast('int', Code04_Tree1.cntg)

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_Tree1.siz[u] = jcast('int', 1)
        e = jcast('int', Code04_Tree1.head[u])
        while (e > 0):
            v = jcast('int', Code04_Tree1.to[e])
            if ((v != fa) and (not Code04_Tree1.vis[v])):
                Code04_Tree1.getSize(v, u)
                Code04_Tree1.siz[u] = jcast('int', jcast('int', jadd(Code04_Tree1.siz[u], Code04_Tree1.siz[v])))
            e = jcast('int', Code04_Tree1.nxt[e])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_Tree1.getSize(u, fa)
        half = jcast('int', jcast('int', (Code04_Tree1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code04_Tree1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code04_Tree1.to[e])
                        if (((v != fa) and (not Code04_Tree1.vis[v])) and (Code04_Tree1.siz[v] > half)):
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
                    e = jcast('int', Code04_Tree1.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def dfs(u, fa, dis):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dis = jcast('int', dis)
        if (dis > Code04_Tree1.k):
            return
        jset(Code04_Tree1.disArr, ((_java_obj_6 := Code04_Tree1), (_java_key_7 := 'cnta'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3], dis)
        e = jcast('int', Code04_Tree1.head[u])
        while (e > 0):
            v = jcast('int', Code04_Tree1.to[e])
            if ((v != fa) and (not Code04_Tree1.vis[v])):
                Code04_Tree1.dfs(v, u, jcast('int', jadd(dis, Code04_Tree1.weight[e])))
            e = jcast('int', Code04_Tree1.nxt[e])

    # 从真正的头来到u时，路径权值和为dis
    # 子树u上的点对(x, y)，需要走过，x -> 真正的头 -> y
    # 返回距离<=k的点对数量
    @staticmethod
    def calc(u, dis):
        u = jcast('int', u)
        dis = jcast('int', dis)
        Code04_Tree1.cnta = jcast('int', 0)
        Code04_Tree1.dfs(u, 0, dis)
        ans = jcast('long', 0)
        jstatic('Arrays', 'sort', Code04_Tree1.disArr, 1, jcast('int', jadd(Code04_Tree1.cnta, 1)))
        l = jcast('int', 1)
        r = jcast('int', Code04_Tree1.cnta)
        while (l <= r):
            if (jcast('int', jadd(Code04_Tree1.disArr[l], Code04_Tree1.disArr[r])) <= Code04_Tree1.k):
                ans = jcast('long', jcast('long', jadd(ans, jcast('int', (r - l)))))
                l = jcast('int', (l + 1))
            else:
                r = jcast('int', (r - 1))
        return jcast('long', ans)

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code04_Tree1.vis[u] = jcast('boolean', True)
        ans = jcast('long', Code04_Tree1.calc(u, 0))
        e = jcast('int', Code04_Tree1.head[u])
        while (e > 0):
            v = jcast('int', Code04_Tree1.to[e])
            if (not Code04_Tree1.vis[v]):
                ans = jcast('long', jcast('long', (ans - Code04_Tree1.calc(v, Code04_Tree1.weight[e]))))
                ans = jcast('long', jcast('long', jadd(ans, Code04_Tree1.solve(Code04_Tree1.getCentroid(v, u)))))
            e = jcast('int', Code04_Tree1.nxt[e])
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code04_Tree1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Tree1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code04_Tree1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code04_Tree1.addEdge(u, v, w)
            Code04_Tree1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code04_Tree1.k = jcast('int', jcall(in_, 'nextInt'))
        jcall(out, 'println', Code04_Tree1.solve(Code04_Tree1.getCentroid(1, 0)))
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
            raise TypeError("No matching overload for Code04_Tree1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Tree1.MAXN = jcast('int', 50001)
Code04_Tree1.n = jcast('int', 0)
Code04_Tree1.k = jcast('int', 0)
Code04_Tree1.head = jarray('int', [Code04_Tree1.MAXN])
Code04_Tree1.nxt = jarray('int', [jcast('int', (Code04_Tree1.MAXN << (1 & 31)))])
Code04_Tree1.to = jarray('int', [jcast('int', (Code04_Tree1.MAXN << (1 & 31)))])
Code04_Tree1.weight = jarray('int', [jcast('int', (Code04_Tree1.MAXN << (1 & 31)))])
Code04_Tree1.cntg = jcast('int', 0)
Code04_Tree1.vis = jarray('boolean', [Code04_Tree1.MAXN])
Code04_Tree1.siz = jarray('int', [Code04_Tree1.MAXN])
Code04_Tree1.disArr = jarray('int', [Code04_Tree1.MAXN])
Code04_Tree1.cnta = jcast('int', 0)

if __name__ == '__main__':
    Code04_Tree1.main([])
