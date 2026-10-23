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

# 所有合法路径的魔力和，Python版
# 一共有n个节点，给定n-1条边，每条边有边权，所有节点组成一棵树
# 给定两个整数l、r，对于点对(x, y)，考虑两点之间的简单路径
# 如果路径的边数在[l, r]范围内，则该路径视为合法
# 一条路径的魔力值 = 该路径上所有边权的最大值
# 计算所有合法路径的魔力值之和
# 本题规定(x, x)不是点对，(x, y)和(y, x)认为是不同的点对
# 1 <= n、边权 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5351
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Maschera2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'l': 'l', 'r': 'r', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'maxvArr': 'maxvArr', 'edgeArr': 'edgeArr', 'cnta': 'cnta', 'tree': 'tree', 'stack': 'stack', 'u': 'u', 'f': 'f', 'maxv': 'maxv', 'edge': 'edge', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    n = 0
    l = 0
    r = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    vis = None
    siz = None
    maxvArr = None
    edgeArr = None
    cnta = 0
    tree = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    maxv = 0
    edge = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, maxv, edge, e):
        u = jcast('int', u)
        f = jcast('int', f)
        maxv = jcast('int', maxv)
        edge = jcast('int', edge)
        e = jcast('int', e)
        jset(Code06_Maschera2.stack[Code06_Maschera2.stacksize], 0, u)
        jset(Code06_Maschera2.stack[Code06_Maschera2.stacksize], 1, f)
        jset(Code06_Maschera2.stack[Code06_Maschera2.stacksize], 2, maxv)
        jset(Code06_Maschera2.stack[Code06_Maschera2.stacksize], 3, edge)
        jset(Code06_Maschera2.stack[Code06_Maschera2.stacksize], 4, e)
        Code06_Maschera2.stacksize = jcast('int', (Code06_Maschera2.stacksize + 1))

    @staticmethod
    def pop():
        Code06_Maschera2.stacksize = jcast('int', (Code06_Maschera2.stacksize - 1))
        Code06_Maschera2.u = jcast('int', Code06_Maschera2.stack[Code06_Maschera2.stacksize][0])
        Code06_Maschera2.f = jcast('int', Code06_Maschera2.stack[Code06_Maschera2.stacksize][1])
        Code06_Maschera2.maxv = jcast('int', Code06_Maschera2.stack[Code06_Maschera2.stacksize][2])
        Code06_Maschera2.edge = jcast('int', Code06_Maschera2.stack[Code06_Maschera2.stacksize][3])
        Code06_Maschera2.e = jcast('int', Code06_Maschera2.stack[Code06_Maschera2.stacksize][4])

    @staticmethod
    def sort(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code06_Maschera2.maxvArr[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (Code06_Maschera2.maxvArr[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code06_Maschera2.maxvArr[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', Code06_Maschera2.maxvArr[i])
                Code06_Maschera2.maxvArr[i] = jcast('int', Code06_Maschera2.maxvArr[j])
                Code06_Maschera2.maxvArr[j] = jcast('int', tmp)
                tmp = jcast('int', Code06_Maschera2.edgeArr[i])
                Code06_Maschera2.edgeArr[i] = jcast('int', Code06_Maschera2.edgeArr[j])
                Code06_Maschera2.edgeArr[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code06_Maschera2.sort(l, j)
        Code06_Maschera2.sort(i, r)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code06_Maschera2.nxt, ((_java_obj_1 := Code06_Maschera2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_Maschera2.head[u])
        Code06_Maschera2.to[Code06_Maschera2.cntg] = jcast('int', v)
        Code06_Maschera2.weight[Code06_Maschera2.cntg] = jcast('int', w)
        Code06_Maschera2.head[u] = jcast('int', Code06_Maschera2.cntg)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        i = jcast('int', (i + 1))
        while (i <= jcast('int', jadd(Code06_Maschera2.r, 1))):
            Code06_Maschera2.tree[i] = jcast('int', jcast('int', jadd(Code06_Maschera2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code06_Maschera2.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        i = jcast('int', (i + 1))
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code06_Maschera2.tree[i])))
            i = jcast('int', jcast('int', (i - Code06_Maschera2.lowbit(i))))
        return jcast('int', ret)

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code06_Maschera2.siz[u] = jcast('int', 1)
        e = jcast('int', Code06_Maschera2.head[u])
        while (e > 0):
            v = jcast('int', Code06_Maschera2.to[e])
            if ((v != fa) and (not Code06_Maschera2.vis[v])):
                Code06_Maschera2.getSize1(v, u)
                Code06_Maschera2.siz[u] = jcast('int', jcast('int', jadd(Code06_Maschera2.siz[u], Code06_Maschera2.siz[v])))
            e = jcast('int', Code06_Maschera2.nxt[e])

    # 得到子树大小迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code06_Maschera2.stacksize = jcast('int', 0)
        Code06_Maschera2.push(cur, fa, 0, 0, jcast('int', (-1)))
        while (Code06_Maschera2.stacksize > 0):
            Code06_Maschera2.pop()
            if (Code06_Maschera2.e == jcast('int', (-1))):
                Code06_Maschera2.siz[Code06_Maschera2.u] = jcast('int', 1)
                Code06_Maschera2.e = jcast('int', Code06_Maschera2.head[Code06_Maschera2.u])
            else:
                Code06_Maschera2.e = jcast('int', Code06_Maschera2.nxt[Code06_Maschera2.e])
            if (Code06_Maschera2.e != 0):
                Code06_Maschera2.push(Code06_Maschera2.u, Code06_Maschera2.f, 0, 0, Code06_Maschera2.e)
                v = jcast('int', Code06_Maschera2.to[Code06_Maschera2.e])
                if ((v != Code06_Maschera2.f) and (not Code06_Maschera2.vis[v])):
                    Code06_Maschera2.push(v, Code06_Maschera2.u, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code06_Maschera2.head[Code06_Maschera2.u])
                while (ei > 0):
                    v = jcast('int', Code06_Maschera2.to[ei])
                    if ((v != Code06_Maschera2.f) and (not Code06_Maschera2.vis[v])):
                        Code06_Maschera2.siz[Code06_Maschera2.u] = jcast('int', jcast('int', jadd(Code06_Maschera2.siz[Code06_Maschera2.u], Code06_Maschera2.siz[v])))
                    ei = jcast('int', Code06_Maschera2.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code06_Maschera2.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code06_Maschera2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code06_Maschera2.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code06_Maschera2.to[e])
                        if (((v != fa) and (not Code06_Maschera2.vis[v])) and (Code06_Maschera2.siz[v] > half)):
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
                    e = jcast('int', Code06_Maschera2.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    # 收集信息递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa, maxv, edge):
        u = jcast('int', u)
        fa = jcast('int', fa)
        maxv = jcast('int', maxv)
        edge = jcast('int', edge)
        if (edge > Code06_Maschera2.r):
            return
        jset(Code06_Maschera2.maxvArr, ((_java_obj_6 := Code06_Maschera2), (_java_key_7 := 'cnta'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3], maxv)
        Code06_Maschera2.edgeArr[Code06_Maschera2.cnta] = jcast('int', edge)
        e = jcast('int', Code06_Maschera2.head[u])
        while (e > 0):
            v = jcast('int', Code06_Maschera2.to[e])
            if ((v != fa) and (not Code06_Maschera2.vis[v])):
                Code06_Maschera2.dfs1(v, u, jstatic('Math', 'max', maxv, Code06_Maschera2.weight[e]), jcast('int', jadd(edge, 1)))
            e = jcast('int', Code06_Maschera2.nxt[e])

    # 收集信息迭代版
    @staticmethod
    def dfs2(cur, fa, pmaxv, pedge):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        pmaxv = jcast('int', pmaxv)
        pedge = jcast('int', pedge)
        Code06_Maschera2.stacksize = jcast('int', 0)
        Code06_Maschera2.push(cur, fa, pmaxv, pedge, jcast('int', (-1)))
        while (Code06_Maschera2.stacksize > 0):
            try:
                Code06_Maschera2.pop()
                if (Code06_Maschera2.e == jcast('int', (-1))):
                    if (Code06_Maschera2.edge > Code06_Maschera2.r):
                        raise JContinue(None)
                    jset(Code06_Maschera2.maxvArr, ((_java_obj_10 := Code06_Maschera2), (_java_key_11 := 'cnta'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code06_Maschera2.maxv)
                    Code06_Maschera2.edgeArr[Code06_Maschera2.cnta] = jcast('int', Code06_Maschera2.edge)
                    Code06_Maschera2.e = jcast('int', Code06_Maschera2.head[Code06_Maschera2.u])
                else:
                    Code06_Maschera2.e = jcast('int', Code06_Maschera2.nxt[Code06_Maschera2.e])
                if (Code06_Maschera2.e != 0):
                    Code06_Maschera2.push(Code06_Maschera2.u, Code06_Maschera2.f, Code06_Maschera2.maxv, Code06_Maschera2.edge, Code06_Maschera2.e)
                    v = jcast('int', Code06_Maschera2.to[Code06_Maschera2.e])
                    if ((v != Code06_Maschera2.f) and (not Code06_Maschera2.vis[v])):
                        Code06_Maschera2.push(Code06_Maschera2.to[Code06_Maschera2.e], Code06_Maschera2.u, jstatic('Math', 'max', Code06_Maschera2.maxv, Code06_Maschera2.weight[Code06_Maschera2.e]), jcast('int', jadd(Code06_Maschera2.edge, 1)), jcast('int', (-1)))
            except JContinue as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
            except JBreak as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
                break

    @staticmethod
    def calc(u, maxv, edge):
        u = jcast('int', u)
        maxv = jcast('int', maxv)
        edge = jcast('int', edge)
        Code06_Maschera2.cnta = jcast('int', 0)
        # dfs1(u, 0, maxv, edge);
        Code06_Maschera2.dfs2(u, 0, maxv, edge)
        Code06_Maschera2.sort(1, Code06_Maschera2.cnta)
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code06_Maschera2.cnta):
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', (1 * Code06_Maschera2.maxvArr[i])) * jcast('int', (Code06_Maschera2.sum(jcast('int', (Code06_Maschera2.r - Code06_Maschera2.edgeArr[i]))) - Code06_Maschera2.sum(jcast('int', (jcast('int', (Code06_Maschera2.l - Code06_Maschera2.edgeArr[i])) - 1))))))))))
            Code06_Maschera2.add(Code06_Maschera2.edgeArr[i], 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_Maschera2.cnta):
            Code06_Maschera2.add(Code06_Maschera2.edgeArr[i], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code06_Maschera2.vis[u] = jcast('boolean', True)
        ans = jcast('long', Code06_Maschera2.calc(u, 0, 0))
        e = jcast('int', Code06_Maschera2.head[u])
        while (e > 0):
            v = jcast('int', Code06_Maschera2.to[e])
            if (not Code06_Maschera2.vis[v]):
                ans = jcast('long', jcast('long', (ans - Code06_Maschera2.calc(v, Code06_Maschera2.weight[e], 1))))
                ans = jcast('long', jcast('long', jadd(ans, Code06_Maschera2.solve(Code06_Maschera2.getCentroid(v, u)))))
            e = jcast('int', Code06_Maschera2.nxt[e])
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code06_Maschera2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Maschera2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_Maschera2.l = jcast('int', jcall(in_, 'nextInt'))
        Code06_Maschera2.r = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code06_Maschera2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code06_Maschera2.addEdge(u, v, w)
            Code06_Maschera2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        ans = jcast('long', Code06_Maschera2.solve(Code06_Maschera2.getCentroid(1, 0)))
        jcall(out, 'println', jcast('long', (ans << (1 & 63))))
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
            return jcast('int', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_Maschera2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Maschera2.MAXN = jcast('int', 100002)
Code06_Maschera2.n = jcast('int', 0)
Code06_Maschera2.l = jcast('int', 0)
Code06_Maschera2.r = jcast('int', 0)
Code06_Maschera2.head = jarray('int', [Code06_Maschera2.MAXN])
Code06_Maschera2.nxt = jarray('int', [jcast('int', (Code06_Maschera2.MAXN << (1 & 31)))])
Code06_Maschera2.to = jarray('int', [jcast('int', (Code06_Maschera2.MAXN << (1 & 31)))])
Code06_Maschera2.weight = jarray('int', [jcast('int', (Code06_Maschera2.MAXN << (1 & 31)))])
Code06_Maschera2.cntg = jcast('int', 0)
Code06_Maschera2.vis = jarray('boolean', [Code06_Maschera2.MAXN])
Code06_Maschera2.siz = jarray('int', [Code06_Maschera2.MAXN])
Code06_Maschera2.maxvArr = jarray('int', [Code06_Maschera2.MAXN])
Code06_Maschera2.edgeArr = jarray('int', [Code06_Maschera2.MAXN])
Code06_Maschera2.cnta = jcast('int', 0)
Code06_Maschera2.tree = jarray('int', [Code06_Maschera2.MAXN])
Code06_Maschera2.stack = jarray('int', [Code06_Maschera2.MAXN, 5])
Code06_Maschera2.u = jcast('int', 0)
Code06_Maschera2.f = jcast('int', 0)
Code06_Maschera2.maxv = jcast('int', 0)
Code06_Maschera2.edge = jcast('int', 0)
Code06_Maschera2.e = jcast('int', 0)
Code06_Maschera2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code06_Maschera2.main([])
