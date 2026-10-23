# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 烁烁的游戏，Python版
# 树上有n个点，每个点的初始点权是0，给定n-1条边，边权都是1
# 接下来有m条操作，每条操作是如下两种类型中的一种
# 操作 M x k v : 点x出发，距离<=k的所有点，点权都加上v
# 操作 Q x     : 打印点x的点权
# 1 <= n、m <= 10^5
# -10000 <= v <= +10000
# 测试链接 : https://www.luogu.com.cn/problem/P10603
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Game1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dep': 'dep', 'stjump': 'stjump', 'vis': 'vis', 'siz': 'siz', 'centfa': 'centfa', 'addTree': 'addTree', 'minusTree': 'minusTree', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'cntt': 'cntt', 'stack': 'stack', 'u': 'u', 'f': 'f', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXP = 0
    MAXT = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dep = None
    stjump = None
    vis = None
    siz = None
    centfa = None
    addTree = None
    minusTree = None
    ls = None
    rs = None
    sum = None
    cntt = 0
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code02_Game1.stack[Code02_Game1.stacksize], 0, u)
        jset(Code02_Game1.stack[Code02_Game1.stacksize], 1, f)
        jset(Code02_Game1.stack[Code02_Game1.stacksize], 2, e)
        Code02_Game1.stacksize = jcast('int', (Code02_Game1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_Game1.stacksize = jcast('int', (Code02_Game1.stacksize - 1))
        Code02_Game1.u = jcast('int', Code02_Game1.stack[Code02_Game1.stacksize][0])
        Code02_Game1.f = jcast('int', Code02_Game1.stack[Code02_Game1.stacksize][1])
        Code02_Game1.e = jcast('int', Code02_Game1.stack[Code02_Game1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_Game1.nxt, ((_java_obj_1 := Code02_Game1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Game1.head[u])
        Code02_Game1.to[Code02_Game1.cntg] = jcast('int', v)
        Code02_Game1.head[u] = jcast('int', Code02_Game1.cntg)

    # 树上倍增收集信息递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Game1.dep[u] = jcast('int', jcast('int', jadd(Code02_Game1.dep[fa], 1)))
        jset(Code02_Game1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code02_Game1.MAXP):
            jset(Code02_Game1.stjump[u], p, Code02_Game1.stjump[Code02_Game1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code02_Game1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Game1.to[e])
            if (v != fa):
                Code02_Game1.dfs1(v, u)
            e = jcast('int', Code02_Game1.nxt[e])

    # dfs1的迭代版
    @staticmethod
    def dfs2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code02_Game1.stacksize = jcast('int', 0)
        Code02_Game1.push(cur, fa, jcast('int', (-1)))
        while (Code02_Game1.stacksize > 0):
            Code02_Game1.pop()
            if (Code02_Game1.e == jcast('int', (-1))):
                Code02_Game1.dep[Code02_Game1.u] = jcast('int', jcast('int', jadd(Code02_Game1.dep[Code02_Game1.f], 1)))
                jset(Code02_Game1.stjump[Code02_Game1.u], 0, Code02_Game1.f)
                p = jcast('int', 1)
                while (p < Code02_Game1.MAXP):
                    jset(Code02_Game1.stjump[Code02_Game1.u], p, Code02_Game1.stjump[Code02_Game1.stjump[Code02_Game1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code02_Game1.e = jcast('int', Code02_Game1.head[Code02_Game1.u])
            else:
                Code02_Game1.e = jcast('int', Code02_Game1.nxt[Code02_Game1.e])
            if (Code02_Game1.e != 0):
                Code02_Game1.push(Code02_Game1.u, Code02_Game1.f, Code02_Game1.e)
                v = jcast('int', Code02_Game1.to[Code02_Game1.e])
                if (v != Code02_Game1.f):
                    Code02_Game1.push(v, Code02_Game1.u, jcast('int', (-1)))

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code02_Game1.dep[a] < Code02_Game1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code02_Game1.MAXP - 1)))
        while (p >= 0):
            if (Code02_Game1.dep[Code02_Game1.stjump[a][p]] >= Code02_Game1.dep[b]):
                a = jcast('int', Code02_Game1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code02_Game1.MAXP - 1)))
        while (p >= 0):
            if (Code02_Game1.stjump[a][p] != Code02_Game1.stjump[b][p]):
                a = jcast('int', Code02_Game1.stjump[a][p])
                b = jcast('int', Code02_Game1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code02_Game1.stjump[a][0])

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code02_Game1.dep[x], Code02_Game1.dep[y])) - jcast('int', (Code02_Game1.dep[Code02_Game1.getLca(x, y)] << (1 & 31))))))

    # 找重心需要计算子树大小的递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Game1.siz[u] = jcast('int', 1)
        e = jcast('int', Code02_Game1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Game1.to[e])
            if ((v != fa) and (not Code02_Game1.vis[v])):
                Code02_Game1.getSize1(v, u)
                Code02_Game1.siz[u] = jcast('int', jcast('int', jadd(Code02_Game1.siz[u], Code02_Game1.siz[v])))
            e = jcast('int', Code02_Game1.nxt[e])

    # getSize1的迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code02_Game1.stacksize = jcast('int', 0)
        Code02_Game1.push(cur, fa, jcast('int', (-1)))
        while (Code02_Game1.stacksize > 0):
            Code02_Game1.pop()
            if (Code02_Game1.e == jcast('int', (-1))):
                Code02_Game1.siz[Code02_Game1.u] = jcast('int', 1)
                Code02_Game1.e = jcast('int', Code02_Game1.head[Code02_Game1.u])
            else:
                Code02_Game1.e = jcast('int', Code02_Game1.nxt[Code02_Game1.e])
            if (Code02_Game1.e != 0):
                Code02_Game1.push(Code02_Game1.u, Code02_Game1.f, Code02_Game1.e)
                v = jcast('int', Code02_Game1.to[Code02_Game1.e])
                if ((v != Code02_Game1.f) and (not Code02_Game1.vis[v])):
                    Code02_Game1.push(v, Code02_Game1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code02_Game1.head[Code02_Game1.u])
                while (ei > 0):
                    v = jcast('int', Code02_Game1.to[ei])
                    if ((v != Code02_Game1.f) and (not Code02_Game1.vis[v])):
                        Code02_Game1.siz[Code02_Game1.u] = jcast('int', jcast('int', jadd(Code02_Game1.siz[Code02_Game1.u], Code02_Game1.siz[v])))
                    ei = jcast('int', Code02_Game1.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code02_Game1.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code02_Game1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code02_Game1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code02_Game1.to[e])
                        if (((v != fa) and (not Code02_Game1.vis[v])) and (Code02_Game1.siz[v] > half)):
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
                    e = jcast('int', Code02_Game1.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def centroidTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Game1.centfa[u] = jcast('int', fa)
        Code02_Game1.vis[u] = jcast('boolean', True)
        e = jcast('int', Code02_Game1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Game1.to[e])
            if (not Code02_Game1.vis[v]):
                Code02_Game1.centroidTree(Code02_Game1.getCentroid(v, u), u)
            e = jcast('int', Code02_Game1.nxt[e])

    @staticmethod
    def _java_add_0(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_6 := Code02_Game1), (_java_key_7 := 'cntt'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3])
        if (l == r):
            Code02_Game1.sum[i] = jcast('int', jcast('int', jadd(Code02_Game1.sum[i], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code02_Game1.ls, i, Code02_Game1._java_add_0(jobi, jobv, l, mid, Code02_Game1.ls[i]))
            else:
                jset(Code02_Game1.rs, i, Code02_Game1._java_add_0(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code02_Game1.rs[i]))
            Code02_Game1.sum[i] = jcast('int', jcast('int', jadd(Code02_Game1.sum[Code02_Game1.ls[i]], Code02_Game1.sum[Code02_Game1.rs[i]])))
        return jcast('int', i)

    @staticmethod
    def _java_query_0(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code02_Game1.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code02_Game1._java_query_0(jobl, jobr, l, mid, Code02_Game1.ls[i]))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code02_Game1._java_query_0(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code02_Game1.rs[i]))))
        return jcast('int', ans)

    @staticmethod
    def _java_add_1(x, k, v):
        x = jcast('int', x)
        k = jcast('int', k)
        v = jcast('int', v)
        jset(Code02_Game1.addTree, x, Code02_Game1._java_add_0(k, v, 0, jcast('int', (Code02_Game1.n - 1)), Code02_Game1.addTree[x]))
        cur = jcast('int', x)
        fa = jcast('int', Code02_Game1.centfa[cur])
        while (fa > 0):
            dist = jcast('int', Code02_Game1.getDist(x, fa))
            if (jcast('int', (k - dist)) >= 0):
                jset(Code02_Game1.addTree, fa, Code02_Game1._java_add_0(jcast('int', (k - dist)), v, 0, jcast('int', (Code02_Game1.n - 1)), Code02_Game1.addTree[fa]))
                jset(Code02_Game1.minusTree, cur, Code02_Game1._java_add_0(jcast('int', (k - dist)), v, 0, jcast('int', (Code02_Game1.n - 1)), Code02_Game1.minusTree[cur]))
            cur = jcast('int', fa)
            fa = jcast('int', Code02_Game1.centfa[cur])

    @staticmethod
    def _java_query_1(x):
        x = jcast('int', x)
        ans = jcast('int', Code02_Game1._java_query_0(0, jcast('int', (Code02_Game1.n - 1)), 0, jcast('int', (Code02_Game1.n - 1)), Code02_Game1.addTree[x]))
        cur = jcast('int', x)
        fa = jcast('int', Code02_Game1.centfa[cur])
        while (fa > 0):
            dist = jcast('int', Code02_Game1.getDist(x, fa))
            ans = jcast('int', jcast('int', jadd(ans, Code02_Game1._java_query_0(dist, jcast('int', (Code02_Game1.n - 1)), 0, jcast('int', (Code02_Game1.n - 1)), Code02_Game1.addTree[fa]))))
            ans = jcast('int', jcast('int', (ans - Code02_Game1._java_query_0(dist, jcast('int', (Code02_Game1.n - 1)), 0, jcast('int', (Code02_Game1.n - 1)), Code02_Game1.minusTree[cur]))))
            cur = jcast('int', fa)
            fa = jcast('int', Code02_Game1.centfa[cur])
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code02_Game1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Game1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Game1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code02_Game1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code02_Game1.addEdge(u, v)
            Code02_Game1.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        Code02_Game1.dfs2(1, 0)
        Code02_Game1.centroidTree(Code02_Game1.getCentroid(1, 0), 0)
        op = jchar(0)
        x = 0
        k = 0
        v = 0
        i = jcast('int', 1)
        while (i <= Code02_Game1.m):
            op = jcast('char', jcall(in_, 'nextChar'))
            if (op == jchar('M')):
                x = jcast('int', jcall(in_, 'nextInt'))
                k = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code02_Game1._java_add_1(x, k, v)
            else:
                x = jcast('int', jcall(in_, 'nextInt'))
                jcall(out, 'println', Code02_Game1._java_query_1(x))
            i = jcast('int', (i + 1))
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
            return jcast('byte', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

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
            raise TypeError("No matching overload for Code02_Game1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code02_Game1._java_add_0(*args)
        if _java_choice == 1:
            return Code02_Game1._java_add_1(*args)
        raise TypeError("No matching overload for Code02_Game1.add")

    @staticmethod
    def query(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code02_Game1._java_query_0(*args)
        if _java_choice == 1:
            return Code02_Game1._java_query_1(*args)
        raise TypeError("No matching overload for Code02_Game1.query")


Code02_Game1.MAXN = jcast('int', 100001)
Code02_Game1.MAXP = jcast('int', 18)
Code02_Game1.MAXT = jcast('int', 20000001)
Code02_Game1.n = jcast('int', 0)
Code02_Game1.m = jcast('int', 0)
Code02_Game1.head = jarray('int', [Code02_Game1.MAXN])
Code02_Game1.nxt = jarray('int', [jcast('int', (Code02_Game1.MAXN << (1 & 31)))])
Code02_Game1.to = jarray('int', [jcast('int', (Code02_Game1.MAXN << (1 & 31)))])
Code02_Game1.cntg = jcast('int', 0)
Code02_Game1.dep = jarray('int', [Code02_Game1.MAXN])
Code02_Game1.stjump = jarray('int', [Code02_Game1.MAXN, Code02_Game1.MAXP])
Code02_Game1.vis = jarray('boolean', [Code02_Game1.MAXN])
Code02_Game1.siz = jarray('int', [Code02_Game1.MAXN])
Code02_Game1.centfa = jarray('int', [Code02_Game1.MAXN])
Code02_Game1.addTree = jarray('int', [Code02_Game1.MAXN])
Code02_Game1.minusTree = jarray('int', [Code02_Game1.MAXN])
Code02_Game1.ls = jarray('int', [Code02_Game1.MAXT])
Code02_Game1.rs = jarray('int', [Code02_Game1.MAXT])
Code02_Game1.sum = jarray('int', [Code02_Game1.MAXT])
Code02_Game1.cntt = jcast('int', 0)
Code02_Game1.stack = jarray('int', [Code02_Game1.MAXN, 3])
Code02_Game1.u = jcast('int', 0)
Code02_Game1.f = jcast('int', 0)
Code02_Game1.e = jcast('int', 0)
Code02_Game1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code02_Game1.main([])
