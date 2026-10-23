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

# 树上分块模版题，随机撒点，Python版
# 一共有n个节点，每个节点有点权，给定n-1条边，所有节点连成一棵树
# 接下来有m条操作，每条操作都要打印两个答案，描述如下
# 操作 k x1 y1 x2 y2 .. (一共k个点对)
# 每个点对(x, y)，在树上都有从x到y的路径，那么k个点对就有k条路径
# 先打印k条路径上不同点权的数量，再打印点权集合中没有出现的最小非负数(mex)
# 1 <= n、点对总数 <= 10^5    点权 <= 30000
# 题目要求强制在线，具体规则可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P3603
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Random2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'MAXV': 'MAXV', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'f': 'f', 'k': 'k', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'dep': 'dep', 'stjump': 'stjump', 'markNum': 'markNum', 'vis': 'vis', 'markNode': 'markNode', 'kthMark': 'kthMark', 'up': 'up', 'downSet': 'downSet', 'ans': 'ans', 'ufe': 'ufe', 'stacksize': 'stacksize', 'cur': 'cur', 'fath': 'fath', 'edge': 'edge'}
    MAXN = 0
    MAXB = 0
    MAXV = 0
    MAXP = 0
    n = 0
    m = 0
    f = 0
    k = 0
    arr = None
    # 链式前向星
    head = None
    next = None
    to = None
    cntg = 0
    # 树上倍增，就只是为了快速求出LCA
    dep = None
    stjump = None
    # 随机撒点
    # markNum表示关键点数量
    markNum = 0
    # vis[i]表示i号节点是否已经是关键点
    vis = None
    # markNode[k] = i 表示第k个关键点是编号为i的节点
    markNode = None
    # kthMark[i] = k 表示i号节点是第k个关键点，kthMark[i] = 0 表示i号节点是非关键点
    kthMark = None
    # up[i] = j，表示i号节点是关键点，它往上跳到最近的关键点是j号节点
    up = None
    # downSet[k]的含义，路径是[第k个的关键点 .. 最近的上方关键点)，沿途所有节点值组成的位图
    downSet = None
    ans = None
    class BitSet:
        __java_fields__ = {'len': 'len', 'set': 'set'}
        # len：实例字段，在构造函数中初始化。
        # set：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.len = jcast('int', jcast('int', jdiv(jcast('int', jadd(Code06_Random2.MAXV, 31)), 32)))
            self.set = jarray('int', [self.len])

        def clear(self):
            i = jcast('int', 0)
            while (i < self.len):
                self.set[i] = jcast('int', 0)
                i = jcast('int', (i + 1))

        def setOne(self, v):
            v = jcast('int', v)
            ((_java_obj_1 := self.set), (_java_key_2 := jcast('int', jdiv(v, 32))), jset(_java_obj_1, _java_key_2, jcast('int', (jget(_java_obj_1, _java_key_2) | jcast('int', (1 << (jcast('int', jmod(v, 32)) & 31)))))))[2]

        def or_(self, obj):
            i = jcast('int', 0)
            while (i < self.len):
                self.set[i] = jcast('int', jcast('int', (self.set[i] | jget(obj, 'set')[i])))
                i = jcast('int', (i + 1))

        def countOnes(self):
            ans = jcast('int', 0)
            for x in self.set:
                ans = jcast('int', jcast('int', jadd(ans, jstatic('Integer', 'bitCount', x))))
            return jcast('int', ans)

        def mex(self):
            i = jcast('int', 0)
            inv = 0
            while (i < self.len):
                inv = jcast('int', jcast('int', (~self.set[i])))
                if (inv != 0):
                    return jcast('int', jcast('int', jadd(jcast('int', (i * 32)), jstatic('Integer', 'numberOfTrailingZeros', inv))))
                i = jcast('int', (i + 1))
            return jcast('int', jcast('int', (-1)))

        def __init__(self, *args, _java_ctor=None):
            self.len = jcast('int', 0)
            self.set = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_Random2.BitSet.BitSet")


    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_Random2.next, ((_java_obj_3 := Code06_Random2), (_java_key_4 := 'cntg'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))))[3], Code06_Random2.head[u])
        Code06_Random2.to[Code06_Random2.cntg] = jcast('int', v)
        Code06_Random2.head[u] = jcast('int', Code06_Random2.cntg)

    # 树上倍增递归版
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code06_Random2.dep[u] = jcast('int', jcast('int', jadd(Code06_Random2.dep[fa], 1)))
        jset(Code06_Random2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code06_Random2.MAXP):
            jset(Code06_Random2.stjump[u], p, Code06_Random2.stjump[Code06_Random2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code06_Random2.head[u])
        while (e != 0):
            if (Code06_Random2.to[e] != fa):
                Code06_Random2.dfs1(Code06_Random2.to[e], u)
            e = jcast('int', Code06_Random2.next[e])

    # 树上倍增迭代版，讲解118进行了详细讲述
    ufe = None
    stacksize = 0
    cur = 0
    fath = 0
    edge = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code06_Random2.ufe[Code06_Random2.stacksize], 0, u)
        jset(Code06_Random2.ufe[Code06_Random2.stacksize], 1, f)
        jset(Code06_Random2.ufe[Code06_Random2.stacksize], 2, e)
        Code06_Random2.stacksize = jcast('int', (Code06_Random2.stacksize + 1))

    @staticmethod
    def pop():
        Code06_Random2.stacksize = jcast('int', (Code06_Random2.stacksize - 1))
        Code06_Random2.cur = jcast('int', Code06_Random2.ufe[Code06_Random2.stacksize][0])
        Code06_Random2.fath = jcast('int', Code06_Random2.ufe[Code06_Random2.stacksize][1])
        Code06_Random2.edge = jcast('int', Code06_Random2.ufe[Code06_Random2.stacksize][2])

    @staticmethod
    def dfs2():
        Code06_Random2.stacksize = jcast('int', 0)
        Code06_Random2.push(1, 0, jcast('int', (-1)))
        while (Code06_Random2.stacksize > 0):
            Code06_Random2.pop()
            if (Code06_Random2.edge == jcast('int', (-1))):
                Code06_Random2.dep[Code06_Random2.cur] = jcast('int', jcast('int', jadd(Code06_Random2.dep[Code06_Random2.fath], 1)))
                jset(Code06_Random2.stjump[Code06_Random2.cur], 0, Code06_Random2.fath)
                p = jcast('int', 1)
                while (p < Code06_Random2.MAXP):
                    jset(Code06_Random2.stjump[Code06_Random2.cur], p, Code06_Random2.stjump[Code06_Random2.stjump[Code06_Random2.cur][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code06_Random2.edge = jcast('int', Code06_Random2.head[Code06_Random2.cur])
            else:
                Code06_Random2.edge = jcast('int', Code06_Random2.next[Code06_Random2.edge])
            if (Code06_Random2.edge != 0):
                Code06_Random2.push(Code06_Random2.cur, Code06_Random2.fath, Code06_Random2.edge)
                if (Code06_Random2.to[Code06_Random2.edge] != Code06_Random2.fath):
                    Code06_Random2.push(Code06_Random2.to[Code06_Random2.edge], Code06_Random2.cur, jcast('int', (-1)))

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code06_Random2.dep[a] < Code06_Random2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code06_Random2.MAXP - 1)))
        while (p >= 0):
            if (Code06_Random2.dep[Code06_Random2.stjump[a][p]] >= Code06_Random2.dep[b]):
                a = jcast('int', Code06_Random2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code06_Random2.MAXP - 1)))
        while (p >= 0):
            if (Code06_Random2.stjump[a][p] != Code06_Random2.stjump[b][p]):
                a = jcast('int', Code06_Random2.stjump[a][p])
                b = jcast('int', Code06_Random2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code06_Random2.stjump[a][0])

    @staticmethod
    def query(x, xylca):
        x = jcast('int', x)
        xylca = jcast('int', xylca)
        while ((Code06_Random2.kthMark[x] == 0) and (x != xylca)):
            jcall(Code06_Random2.ans, 'setOne', Code06_Random2.arr[x])
            x = jcast('int', Code06_Random2.stjump[x][0])
        while ((Code06_Random2.up[x] > 0) and (Code06_Random2.dep[Code06_Random2.up[x]] > Code06_Random2.dep[xylca])):
            jcall(Code06_Random2.ans, 'or_', Code06_Random2.downSet[Code06_Random2.kthMark[x]])
            x = jcast('int', Code06_Random2.up[x])
        while (x != xylca):
            jcall(Code06_Random2.ans, 'setOne', Code06_Random2.arr[x])
            x = jcast('int', Code06_Random2.stjump[x][0])

    @staticmethod
    def updateAns(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        xylca = jcast('int', Code06_Random2.lca(x, y))
        Code06_Random2.query(x, xylca)
        Code06_Random2.query(y, xylca)
        jcall(Code06_Random2.ans, 'setOne', Code06_Random2.arr[xylca])

    @staticmethod
    def prepare():
        Code06_Random2.dfs2()
        len = jcast('int', jcast('int', jstatic('Math', 'sqrt', jcast('int', (Code06_Random2.n * 10)))))
        Code06_Random2.markNum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code06_Random2.n, len)) - 1)), len)))
        b = jcast('int', 1)
        pick = 0
        while (b <= Code06_Random2.markNum):
            while True:
                pick = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * Code06_Random2.n)), 1)))
                if not (Code06_Random2.vis[pick]):
                    break
            Code06_Random2.vis[pick] = jcast('boolean', True)
            Code06_Random2.markNode[b] = jcast('int', pick)
            Code06_Random2.kthMark[pick] = jcast('int', b)
            b = jcast('int', (b + 1))
        b = jcast('int', 1)
        cur = 0
        while (b <= Code06_Random2.markNum):
            try:
                jset(Code06_Random2.downSet, b, Code06_Random2.BitSet(_java_ctor=0))
                jcall(Code06_Random2.downSet[b], 'setOne', Code06_Random2.arr[Code06_Random2.markNode[b]])
                cur = jcast('int', Code06_Random2.stjump[Code06_Random2.markNode[b]][0])
                while (cur != 0):
                    try:
                        if (Code06_Random2.kthMark[cur] > 0):
                            jset(Code06_Random2.up, Code06_Random2.markNode[b], cur)
                            raise JBreak(None)
                        else:
                            jcall(Code06_Random2.downSet[b], 'setOne', Code06_Random2.arr[cur])
                            cur = jcast('int', Code06_Random2.stjump[cur][0])
                    except JContinue as _java_control_7:
                        if _java_control_7.label not in (None,):
                            raise
                    except JBreak as _java_control_7:
                        if _java_control_7.label not in (None,):
                            raise
                        break
            except JContinue as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
            except JBreak as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
                break
            b = jcast('int', (b + 1))

    @staticmethod
    def main(args):
        in_ = Code06_Random2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Random2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_Random2.m = jcast('int', jcall(in_, 'nextInt'))
        Code06_Random2.f = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_Random2.n):
            jset(Code06_Random2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code06_Random2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code06_Random2.addEdge(u, v)
            Code06_Random2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code06_Random2.prepare()
        i = jcast('int', 1)
        lastAns = jcast('int', 0)
        while (i <= Code06_Random2.m):
            jcall(Code06_Random2.ans, 'clear')
            Code06_Random2.k = jcast('int', jcall(in_, 'nextInt'))
            j = jcast('int', 1)
            x = 0
            y = 0
            while (j <= Code06_Random2.k):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                if (Code06_Random2.f > 0):
                    x = jcast('int', jcast('int', (x ^ lastAns)))
                    y = jcast('int', jcast('int', (y ^ lastAns)))
                Code06_Random2.updateAns(x, y)
                j = jcast('int', (j + 1))
            ans1 = jcast('int', jcall(Code06_Random2.ans, 'countOnes'))
            ans2 = jcast('int', jcall(Code06_Random2.ans, 'mex'))
            jcall(out, 'println', jadd(jadd(ans1, ' '), ans2))
            lastAns = jcast('int', jcast('int', jadd(ans1, ans2)))
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
            return jcast('int', self.buffer[((_java_obj_8 := self), (_java_key_9 := 'ptr'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

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
            raise TypeError("No matching overload for Code06_Random2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Random2.MAXN = jcast('int', 100001)
Code06_Random2.MAXB = jcast('int', 401)
Code06_Random2.MAXV = jcast('int', 30001)
Code06_Random2.MAXP = jcast('int', 17)
Code06_Random2.n = jcast('int', 0)
Code06_Random2.m = jcast('int', 0)
Code06_Random2.f = jcast('int', 0)
Code06_Random2.k = jcast('int', 0)
Code06_Random2.arr = jarray('int', [Code06_Random2.MAXN])
Code06_Random2.head = jarray('int', [Code06_Random2.MAXN])
Code06_Random2.next = jarray('int', [jcast('int', (Code06_Random2.MAXN << (1 & 31)))])
Code06_Random2.to = jarray('int', [jcast('int', (Code06_Random2.MAXN << (1 & 31)))])
Code06_Random2.cntg = jcast('int', 0)
Code06_Random2.dep = jarray('int', [Code06_Random2.MAXN])
Code06_Random2.stjump = jarray('int', [Code06_Random2.MAXN, Code06_Random2.MAXP])
Code06_Random2.markNum = jcast('int', 0)
Code06_Random2.vis = jarray('boolean', [Code06_Random2.MAXN])
Code06_Random2.markNode = jarray('int', [Code06_Random2.MAXB])
Code06_Random2.kthMark = jarray('int', [Code06_Random2.MAXN])
Code06_Random2.up = jarray('int', [Code06_Random2.MAXN])
Code06_Random2.downSet = jarray('BitSet', [Code06_Random2.MAXB])
Code06_Random2.ans = Code06_Random2.BitSet(_java_ctor=0)
Code06_Random2.ufe = jarray('int', [Code06_Random2.MAXN, 3])
Code06_Random2.stacksize = jcast('int', 0)
Code06_Random2.cur = jcast('int', 0)
Code06_Random2.fath = jcast('int', 0)
Code06_Random2.edge = jcast('int', 0)

if __name__ == '__main__':
    Code06_Random2.main([])
