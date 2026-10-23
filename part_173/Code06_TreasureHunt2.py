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

# 寻宝游戏，Python版
# 一共有n个节点，节点有两种类型，刷宝的点 和 不刷宝的点
# 一共有n-1条无向边，每条边有边权，所有节点组成一棵树
# 开始时所有节点都是不刷宝的点，接下来有m条操作，格式如下
# 操作 x : x号点的类型翻转，刷宝的点 变成 不刷宝的点，不刷宝的点 变成 刷宝的点
# 一次操作后，每个刷宝的点都会产生宝物，你可以瞬移到任何点作为出发点，瞬移是无代价的
# 你需要走路拿到所有的宝物，最后回到出发点，打印最小的行走总路程，一共有m条打印
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3320
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_TreasureHunt2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dep': 'dep', 'dist': 'dist', 'dfn': 'dfn', 'seg': 'seg', 'stjump': 'stjump', 'cntd': 'cntd', 'arr': 'arr', 'treasure': 'treasure', 'set': 'set', 'ans': 'ans', 'ufwe': 'ufwe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'w': 'w', 'e': 'e'}
    MAXN = 0
    MAXP = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    dep = None
    dist = None
    dfn = None
    seg = None
    stjump = None
    cntd = 0
    arr = None
    treasure = None
    # 这里为了方便，使用语言自带的有序表
    set = None
    ans = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code06_TreasureHunt2.nxt, ((_java_obj_1 := Code06_TreasureHunt2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_TreasureHunt2.head[u])
        Code06_TreasureHunt2.to[Code06_TreasureHunt2.cntg] = jcast('int', v)
        Code06_TreasureHunt2.weight[Code06_TreasureHunt2.cntg] = jcast('int', w)
        Code06_TreasureHunt2.head[u] = jcast('int', Code06_TreasureHunt2.cntg)

    # dfs递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa, w):
        u = jcast('int', u)
        fa = jcast('int', fa)
        w = jcast('int', w)
        Code06_TreasureHunt2.dep[u] = jcast('int', jcast('int', jadd(Code06_TreasureHunt2.dep[fa], 1)))
        jset(Code06_TreasureHunt2.dfn, u, ((_java_obj_4 := Code06_TreasureHunt2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code06_TreasureHunt2.seg[Code06_TreasureHunt2.cntd] = jcast('int', u)
        Code06_TreasureHunt2.dist[u] = jcast('long', jcast('long', jadd(Code06_TreasureHunt2.dist[fa], w)))
        jset(Code06_TreasureHunt2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code06_TreasureHunt2.MAXP):
            jset(Code06_TreasureHunt2.stjump[u], p, Code06_TreasureHunt2.stjump[Code06_TreasureHunt2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code06_TreasureHunt2.head[u])
        while (e > 0):
            if (Code06_TreasureHunt2.to[e] != fa):
                Code06_TreasureHunt2.dfs1(Code06_TreasureHunt2.to[e], u, Code06_TreasureHunt2.weight[e])
            e = jcast('int', Code06_TreasureHunt2.nxt[e])

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
    ufwe = None
    stacksize = 0
    u = 0
    f = 0
    w = 0
    e = 0
    @staticmethod
    def push(u, f, w, e):
        u = jcast('int', u)
        f = jcast('int', f)
        w = jcast('int', w)
        e = jcast('int', e)
        jset(Code06_TreasureHunt2.ufwe[Code06_TreasureHunt2.stacksize], 0, u)
        jset(Code06_TreasureHunt2.ufwe[Code06_TreasureHunt2.stacksize], 1, f)
        jset(Code06_TreasureHunt2.ufwe[Code06_TreasureHunt2.stacksize], 2, w)
        jset(Code06_TreasureHunt2.ufwe[Code06_TreasureHunt2.stacksize], 3, e)
        Code06_TreasureHunt2.stacksize = jcast('int', (Code06_TreasureHunt2.stacksize + 1))

    @staticmethod
    def pop():
        Code06_TreasureHunt2.stacksize = jcast('int', (Code06_TreasureHunt2.stacksize - 1))
        Code06_TreasureHunt2.u = jcast('int', Code06_TreasureHunt2.ufwe[Code06_TreasureHunt2.stacksize][0])
        Code06_TreasureHunt2.f = jcast('int', Code06_TreasureHunt2.ufwe[Code06_TreasureHunt2.stacksize][1])
        Code06_TreasureHunt2.w = jcast('int', Code06_TreasureHunt2.ufwe[Code06_TreasureHunt2.stacksize][2])
        Code06_TreasureHunt2.e = jcast('int', Code06_TreasureHunt2.ufwe[Code06_TreasureHunt2.stacksize][3])

    # dfs1的迭代版
    @staticmethod
    def dfs2():
        Code06_TreasureHunt2.stacksize = jcast('int', 0)
        Code06_TreasureHunt2.push(1, 0, 0, jcast('int', (-1)))
        while (Code06_TreasureHunt2.stacksize > 0):
            Code06_TreasureHunt2.pop()
            if (Code06_TreasureHunt2.e == jcast('int', (-1))):
                Code06_TreasureHunt2.dep[Code06_TreasureHunt2.u] = jcast('int', jcast('int', jadd(Code06_TreasureHunt2.dep[Code06_TreasureHunt2.f], 1)))
                jset(Code06_TreasureHunt2.dfn, Code06_TreasureHunt2.u, ((_java_obj_7 := Code06_TreasureHunt2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                Code06_TreasureHunt2.seg[Code06_TreasureHunt2.cntd] = jcast('int', Code06_TreasureHunt2.u)
                Code06_TreasureHunt2.dist[Code06_TreasureHunt2.u] = jcast('long', jcast('long', jadd(Code06_TreasureHunt2.dist[Code06_TreasureHunt2.f], Code06_TreasureHunt2.w)))
                jset(Code06_TreasureHunt2.stjump[Code06_TreasureHunt2.u], 0, Code06_TreasureHunt2.f)
                p = jcast('int', 1)
                while (p < Code06_TreasureHunt2.MAXP):
                    jset(Code06_TreasureHunt2.stjump[Code06_TreasureHunt2.u], p, Code06_TreasureHunt2.stjump[Code06_TreasureHunt2.stjump[Code06_TreasureHunt2.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code06_TreasureHunt2.e = jcast('int', Code06_TreasureHunt2.head[Code06_TreasureHunt2.u])
            else:
                Code06_TreasureHunt2.e = jcast('int', Code06_TreasureHunt2.nxt[Code06_TreasureHunt2.e])
            if (Code06_TreasureHunt2.e != 0):
                Code06_TreasureHunt2.push(Code06_TreasureHunt2.u, Code06_TreasureHunt2.f, Code06_TreasureHunt2.w, Code06_TreasureHunt2.e)
                if (Code06_TreasureHunt2.to[Code06_TreasureHunt2.e] != Code06_TreasureHunt2.f):
                    Code06_TreasureHunt2.push(Code06_TreasureHunt2.to[Code06_TreasureHunt2.e], Code06_TreasureHunt2.u, Code06_TreasureHunt2.weight[Code06_TreasureHunt2.e], jcast('int', (-1)))

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code06_TreasureHunt2.dep[a] < Code06_TreasureHunt2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code06_TreasureHunt2.MAXP - 1)))
        while (p >= 0):
            if (Code06_TreasureHunt2.dep[Code06_TreasureHunt2.stjump[a][p]] >= Code06_TreasureHunt2.dep[b]):
                a = jcast('int', Code06_TreasureHunt2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code06_TreasureHunt2.MAXP - 1)))
        while (p >= 0):
            if (Code06_TreasureHunt2.stjump[a][p] != Code06_TreasureHunt2.stjump[b][p]):
                a = jcast('int', Code06_TreasureHunt2.stjump[a][p])
                b = jcast('int', Code06_TreasureHunt2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code06_TreasureHunt2.stjump[a][0])

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('long', jcast('long', (jcast('long', jadd(Code06_TreasureHunt2.dist[x], Code06_TreasureHunt2.dist[y])) - jcast('long', (2 * Code06_TreasureHunt2.dist[Code06_TreasureHunt2.getLca(x, y)])))))

    @staticmethod
    def compute():
        curAns = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code06_TreasureHunt2.m):
            nodeId = jcast('int', Code06_TreasureHunt2.arr[i])
            dfnId = jcast('int', Code06_TreasureHunt2.dfn[nodeId])
            if (not Code06_TreasureHunt2.treasure[nodeId]):
                Code06_TreasureHunt2.treasure[nodeId] = jcast('boolean', True)
                jcall(Code06_TreasureHunt2.set, 'add', dfnId)
            else:
                Code06_TreasureHunt2.treasure[nodeId] = jcast('boolean', False)
                jcall(Code06_TreasureHunt2.set, 'remove', dfnId)
            if (jcall(Code06_TreasureHunt2.set, 'size') <= 1):
                curAns = jcast('long', 0)
            else:
                low = jcast('int', Code06_TreasureHunt2.seg[(jcall(Code06_TreasureHunt2.set, 'lower', dfnId) if (jcall(Code06_TreasureHunt2.set, 'lower', dfnId) != None) else jcall(Code06_TreasureHunt2.set, 'last'))])
                high = jcast('int', Code06_TreasureHunt2.seg[(jcall(Code06_TreasureHunt2.set, 'higher', dfnId) if (jcall(Code06_TreasureHunt2.set, 'higher', dfnId) != None) else jcall(Code06_TreasureHunt2.set, 'first'))])
                delta = jcast('long', jcast('long', (jcast('long', jadd(Code06_TreasureHunt2.getDist(nodeId, low), Code06_TreasureHunt2.getDist(nodeId, high))) - Code06_TreasureHunt2.getDist(low, high))))
                if Code06_TreasureHunt2.treasure[nodeId]:
                    curAns = jcast('long', jcast('long', jadd(curAns, delta)))
                else:
                    curAns = jcast('long', jcast('long', (curAns - delta)))
            Code06_TreasureHunt2.ans[i] = jcast('long', curAns)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code06_TreasureHunt2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_TreasureHunt2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_TreasureHunt2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code06_TreasureHunt2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code06_TreasureHunt2.addEdge(u, v, w)
            Code06_TreasureHunt2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        # dfs1(1, 0, 0);
        Code06_TreasureHunt2.dfs2()
        i = jcast('int', 1)
        while (i <= Code06_TreasureHunt2.m):
            jset(Code06_TreasureHunt2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code06_TreasureHunt2.compute()
        i = jcast('int', 1)
        while (i <= Code06_TreasureHunt2.m):
            jcall(out, 'println', Code06_TreasureHunt2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code06_TreasureHunt2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_TreasureHunt2.MAXN = jcast('int', 100001)
Code06_TreasureHunt2.MAXP = jcast('int', 20)
Code06_TreasureHunt2.n = jcast('int', 0)
Code06_TreasureHunt2.m = jcast('int', 0)
Code06_TreasureHunt2.head = jarray('int', [Code06_TreasureHunt2.MAXN])
Code06_TreasureHunt2.nxt = jarray('int', [jcast('int', (Code06_TreasureHunt2.MAXN << (1 & 31)))])
Code06_TreasureHunt2.to = jarray('int', [jcast('int', (Code06_TreasureHunt2.MAXN << (1 & 31)))])
Code06_TreasureHunt2.weight = jarray('int', [jcast('int', (Code06_TreasureHunt2.MAXN << (1 & 31)))])
Code06_TreasureHunt2.cntg = jcast('int', 0)
Code06_TreasureHunt2.dep = jarray('int', [Code06_TreasureHunt2.MAXN])
Code06_TreasureHunt2.dist = jarray('long', [Code06_TreasureHunt2.MAXN])
Code06_TreasureHunt2.dfn = jarray('int', [Code06_TreasureHunt2.MAXN])
Code06_TreasureHunt2.seg = jarray('int', [Code06_TreasureHunt2.MAXN])
Code06_TreasureHunt2.stjump = jarray('int', [Code06_TreasureHunt2.MAXN, Code06_TreasureHunt2.MAXP])
Code06_TreasureHunt2.cntd = jcast('int', 0)
Code06_TreasureHunt2.arr = jarray('int', [Code06_TreasureHunt2.MAXN])
Code06_TreasureHunt2.treasure = jarray('boolean', [Code06_TreasureHunt2.MAXN])
Code06_TreasureHunt2.set = jnew('TreeSet')
Code06_TreasureHunt2.ans = jarray('long', [Code06_TreasureHunt2.MAXN])
Code06_TreasureHunt2.ufwe = jarray('int', [Code06_TreasureHunt2.MAXN, 4])
Code06_TreasureHunt2.stacksize = jcast('int', 0)
Code06_TreasureHunt2.u = jcast('int', 0)
Code06_TreasureHunt2.f = jcast('int', 0)
Code06_TreasureHunt2.w = jcast('int', 0)
Code06_TreasureHunt2.e = jcast('int', 0)

if __name__ == '__main__':
    Code06_TreasureHunt2.main([])
