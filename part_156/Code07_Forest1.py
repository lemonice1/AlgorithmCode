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

# 森林，Python版
# 一共有n个节点，编号1~n，初始时给定m条边，所有节点可能组成森林结构
# 每个节点都给定非负的点权，一共有t条操作，每条操作是如下两种类型中的一种
# 操作 Q x y k : 点x到点y路径上所有的权值中，打印第k小的权值是多少
# 题目保证x和y联通，并且路径上至少有k个点
# 操作 L x y   : 点x和点y之间连接一条边
# 题目保证操作后，所有节点仍然是森林
# 题目要求强制在线，请不要使用离线算法
# 1 <= n、m、t <= 8 * 10^4    点权 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3302
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Forest1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXP': 'MAXP', 'testcase': 'testcase', 'n': 'n', 'm': 'm', 't': 't', 'arr': 'arr', 'sorted': 'sorted', 'diff': 'diff', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'root': 'root', 'left': 'left', 'right': 'right', 'siz': 'siz', 'cntt': 'cntt', 'dep': 'dep', 'stjump': 'stjump', 'treeHead': 'treeHead', 'setSiz': 'setSiz', 'stack': 'stack', 'stackSize': 'stackSize', 'cur': 'cur', 'father': 'father', 'treehead': 'treehead', 'edge': 'edge'}
    MAXN = 0
    MAXT = 0
    MAXP = 0
    testcase = 0
    n = 0
    m = 0
    t = 0
    arr = None
    sorted = None
    diff = 0
    head = None
    next = None
    to = None
    cntg = 0
    root = None
    left = None
    right = None
    siz = None
    cntt = 0
    dep = None
    stjump = None
    treeHead = None
    setSiz = None
    # 来自讲解158，题目4
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code07_Forest1.diff)
        mid = 0
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code07_Forest1.sorted[mid] == num):
                return jcast('int', mid)
            else:
                if (Code07_Forest1.sorted[mid] < num):
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', jcast('int', (-1)))

    # 来自讲解158，题目4
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_Forest1.next, ((_java_obj_1 := Code07_Forest1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_Forest1.head[u])
        Code07_Forest1.to[Code07_Forest1.cntg] = jcast('int', v)
        Code07_Forest1.head[u] = jcast('int', Code07_Forest1.cntg)

    # 来自讲解158，题目4
    @staticmethod
    def insert(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code07_Forest1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code07_Forest1.left[rt] = jcast('int', Code07_Forest1.left[i])
        Code07_Forest1.right[rt] = jcast('int', Code07_Forest1.right[i])
        Code07_Forest1.siz[rt] = jcast('int', jcast('int', jadd(Code07_Forest1.siz[i], 1)))
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code07_Forest1.left, rt, Code07_Forest1.insert(jobi, l, mid, Code07_Forest1.left[rt]))
            else:
                jset(Code07_Forest1.right, rt, Code07_Forest1.insert(jobi, jcast('int', jadd(mid, 1)), r, Code07_Forest1.right[rt]))
        return jcast('int', rt)

    # 来自讲解158，题目4
    @staticmethod
    def query(jobk, l, r, u, v, lca, lcafa):
        jobk = jcast('int', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        u = jcast('int', u)
        v = jcast('int', v)
        lca = jcast('int', lca)
        lcafa = jcast('int', lcafa)
        if (l == r):
            return jcast('int', l)
        lsize = jcast('int', jcast('int', (jcast('int', (jcast('int', jadd(Code07_Forest1.siz[Code07_Forest1.left[u]], Code07_Forest1.siz[Code07_Forest1.left[v]])) - Code07_Forest1.siz[Code07_Forest1.left[lca]])) - Code07_Forest1.siz[Code07_Forest1.left[lcafa]])))
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (lsize >= jobk):
            return jcast('int', Code07_Forest1.query(jobk, l, mid, Code07_Forest1.left[u], Code07_Forest1.left[v], Code07_Forest1.left[lca], Code07_Forest1.left[lcafa]))
        else:
            return jcast('int', Code07_Forest1.query(jcast('int', (jobk - lsize)), jcast('int', jadd(mid, 1)), r, Code07_Forest1.right[u], Code07_Forest1.right[v], Code07_Forest1.right[lca], Code07_Forest1.right[lcafa]))

    # 来自讲解158，题目4
    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code07_Forest1.dep[a] < Code07_Forest1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code07_Forest1.MAXP - 1)))
        while (p >= 0):
            if (Code07_Forest1.dep[Code07_Forest1.stjump[a][p]] >= Code07_Forest1.dep[b]):
                a = jcast('int', Code07_Forest1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code07_Forest1.MAXP - 1)))
        while (p >= 0):
            if (Code07_Forest1.stjump[a][p] != Code07_Forest1.stjump[b][p]):
                a = jcast('int', Code07_Forest1.stjump[a][p])
                b = jcast('int', Code07_Forest1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code07_Forest1.stjump[a][0])

    # 来自讲解158，题目4
    @staticmethod
    def queryKth(x, y, k):
        x = jcast('int', x)
        y = jcast('int', y)
        k = jcast('int', k)
        xylca = jcast('int', Code07_Forest1.lca(x, y))
        lcafa = jcast('int', Code07_Forest1.stjump[xylca][0])
        i = jcast('int', Code07_Forest1.query(k, 1, Code07_Forest1.diff, Code07_Forest1.root[x], Code07_Forest1.root[y], Code07_Forest1.root[xylca], Code07_Forest1.root[lcafa]))
        return jcast('int', Code07_Forest1.sorted[i])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa, treeh):
        u = jcast('int', u)
        fa = jcast('int', fa)
        treeh = jcast('int', treeh)
        jset(Code07_Forest1.root, u, Code07_Forest1.insert(Code07_Forest1.arr[u], 1, Code07_Forest1.diff, Code07_Forest1.root[fa]))
        Code07_Forest1.dep[u] = jcast('int', jcast('int', jadd(Code07_Forest1.dep[fa], 1)))
        Code07_Forest1.treeHead[u] = jcast('int', treeh)
        Code07_Forest1.setSiz[treeh] = jcast('int', (Code07_Forest1.setSiz[treeh] + 1))
        jset(Code07_Forest1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code07_Forest1.MAXP):
            jset(Code07_Forest1.stjump[u], p, Code07_Forest1.stjump[Code07_Forest1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code07_Forest1.head[u])
        while (e > 0):
            if (Code07_Forest1.to[e] != fa):
                Code07_Forest1.dfs1(Code07_Forest1.to[e], u, treeh)
            e = jcast('int', Code07_Forest1.next[e])

    # 迭代版：使用显式状态保存遍历进度
    # 讲解118，详解了从递归版改迭代版
    stack = None
    stackSize = 0
    cur = 0
    father = 0
    treehead = 0
    edge = 0
    @staticmethod
    def push(cur, father, treehead, edge):
        cur = jcast('int', cur)
        father = jcast('int', father)
        treehead = jcast('int', treehead)
        edge = jcast('int', edge)
        jset(Code07_Forest1.stack[Code07_Forest1.stackSize], 0, cur)
        jset(Code07_Forest1.stack[Code07_Forest1.stackSize], 1, father)
        jset(Code07_Forest1.stack[Code07_Forest1.stackSize], 2, treehead)
        jset(Code07_Forest1.stack[Code07_Forest1.stackSize], 3, edge)
        Code07_Forest1.stackSize = jcast('int', (Code07_Forest1.stackSize + 1))

    @staticmethod
    def pop():
        Code07_Forest1.stackSize = jcast('int', (Code07_Forest1.stackSize - 1))
        Code07_Forest1.cur = jcast('int', Code07_Forest1.stack[Code07_Forest1.stackSize][0])
        Code07_Forest1.father = jcast('int', Code07_Forest1.stack[Code07_Forest1.stackSize][1])
        Code07_Forest1.treehead = jcast('int', Code07_Forest1.stack[Code07_Forest1.stackSize][2])
        Code07_Forest1.edge = jcast('int', Code07_Forest1.stack[Code07_Forest1.stackSize][3])

    # dfs1的迭代版
    @staticmethod
    def dfs2(i, fa, treeh):
        i = jcast('int', i)
        fa = jcast('int', fa)
        treeh = jcast('int', treeh)
        Code07_Forest1.stackSize = jcast('int', 0)
        Code07_Forest1.push(i, fa, treeh, jcast('int', (-1)))
        while (Code07_Forest1.stackSize > 0):
            Code07_Forest1.pop()
            if (Code07_Forest1.edge == jcast('int', (-1))):
                jset(Code07_Forest1.root, Code07_Forest1.cur, Code07_Forest1.insert(Code07_Forest1.arr[Code07_Forest1.cur], 1, Code07_Forest1.diff, Code07_Forest1.root[Code07_Forest1.father]))
                Code07_Forest1.dep[Code07_Forest1.cur] = jcast('int', jcast('int', jadd(Code07_Forest1.dep[Code07_Forest1.father], 1)))
                Code07_Forest1.treeHead[Code07_Forest1.cur] = jcast('int', Code07_Forest1.treehead)
                Code07_Forest1.setSiz[Code07_Forest1.treehead] = jcast('int', (Code07_Forest1.setSiz[Code07_Forest1.treehead] + 1))
                jset(Code07_Forest1.stjump[Code07_Forest1.cur], 0, Code07_Forest1.father)
                p = jcast('int', 1)
                while (p < Code07_Forest1.MAXP):
                    jset(Code07_Forest1.stjump[Code07_Forest1.cur], p, Code07_Forest1.stjump[Code07_Forest1.stjump[Code07_Forest1.cur][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code07_Forest1.edge = jcast('int', Code07_Forest1.head[Code07_Forest1.cur])
            else:
                Code07_Forest1.edge = jcast('int', Code07_Forest1.next[Code07_Forest1.edge])
            if (Code07_Forest1.edge != 0):
                Code07_Forest1.push(Code07_Forest1.cur, Code07_Forest1.father, Code07_Forest1.treehead, Code07_Forest1.edge)
                if (Code07_Forest1.to[Code07_Forest1.edge] != Code07_Forest1.father):
                    Code07_Forest1.push(Code07_Forest1.to[Code07_Forest1.edge], Code07_Forest1.cur, Code07_Forest1.treehead, jcast('int', (-1)))

    # x所在的树和y所在的树，合并成一棵树
    @staticmethod
    def connect(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Forest1.addEdge(x, y)
        Code07_Forest1.addEdge(y, x)
        fx = jcast('int', Code07_Forest1.treeHead[x])
        fy = jcast('int', Code07_Forest1.treeHead[y])
        if (Code07_Forest1.setSiz[fx] >= Code07_Forest1.setSiz[fy]):
            # 调用dfs1的迭代版
            Code07_Forest1.dfs2(y, x, fx)
        else:
            # 调用dfs1的迭代版
            Code07_Forest1.dfs2(x, y, fy)

    # 离散化
    # 每棵子树建立可持久化线段树
    # 记录每个节点的所在子树的头节点
    # 记录每棵子树的大小
    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_Forest1.n):
            Code07_Forest1.sorted[i] = jcast('int', Code07_Forest1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_Forest1.sorted, 1, jcast('int', jadd(Code07_Forest1.n, 1)))
        Code07_Forest1.diff = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code07_Forest1.n):
            if (Code07_Forest1.sorted[Code07_Forest1.diff] != Code07_Forest1.sorted[i]):
                jset(Code07_Forest1.sorted, ((_java_obj_7 := Code07_Forest1), (_java_key_8 := 'diff'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code07_Forest1.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Forest1.n):
            jset(Code07_Forest1.arr, i, Code07_Forest1.kth(Code07_Forest1.arr[i]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Forest1.n):
            if (Code07_Forest1.treeHead[i] == 0):
                # 调用dfs1的迭代版
                Code07_Forest1.dfs2(i, 0, i)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_Forest1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Forest1.testcase = jcast('int', jcall(in_, 'nextInt'))
        Code07_Forest1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Forest1.m = jcast('int', jcall(in_, 'nextInt'))
        Code07_Forest1.t = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_Forest1.n):
            jset(Code07_Forest1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code07_Forest1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code07_Forest1.addEdge(u, v)
            Code07_Forest1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code07_Forest1.prepare()
        op = jchar(0)
        x = 0
        y = 0
        k = 0
        lastAns = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_Forest1.t):
            op = jcast('char', jcall(in_, 'nextChar'))
            x = jcast('int', jcast('int', (jcall(in_, 'nextInt') ^ lastAns)))
            y = jcast('int', jcast('int', (jcall(in_, 'nextInt') ^ lastAns)))
            if (op == jchar('Q')):
                k = jcast('int', jcast('int', (jcall(in_, 'nextInt') ^ lastAns)))
                lastAns = jcast('int', Code07_Forest1.queryKth(x, y, k))
                jcall(out, 'println', lastAns)
            else:
                Code07_Forest1.connect(x, y)
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
            return jcast('byte', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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

        def nextDouble(self):
            num = jcast('double', 0)
            div = jcast('double', 1)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while (((not self.isWhitespace(b)) and (b != jchar('.'))) and (b != jcast('int', (-1)))):
                num = jcast('double', jadd((num * 10), jcast('int', (b - jchar('0')))))
                b = jcast('byte', self.readByte())
            if (b == jchar('.')):
                b = jcast('byte', self.readByte())
                while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                    num = jcast('double', jadd(num, jdiv(jcast('int', (b - jchar('0'))), (div := (div * 10)))))
                    b = jcast('byte', self.readByte())
            return jcast('double', ((-num) if minus else num))

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
            raise TypeError("No matching overload for Code07_Forest1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Forest1.MAXN = jcast('int', 80001)
Code07_Forest1.MAXT = jcast('int', jcast('int', (Code07_Forest1.MAXN * 110)))
Code07_Forest1.MAXP = jcast('int', 20)
Code07_Forest1.testcase = jcast('int', 0)
Code07_Forest1.n = jcast('int', 0)
Code07_Forest1.m = jcast('int', 0)
Code07_Forest1.t = jcast('int', 0)
Code07_Forest1.arr = jarray('int', [Code07_Forest1.MAXN])
Code07_Forest1.sorted = jarray('int', [Code07_Forest1.MAXN])
Code07_Forest1.diff = jcast('int', 0)
Code07_Forest1.head = jarray('int', [Code07_Forest1.MAXN])
Code07_Forest1.next = jarray('int', [jcast('int', (Code07_Forest1.MAXN << (1 & 31)))])
Code07_Forest1.to = jarray('int', [jcast('int', (Code07_Forest1.MAXN << (1 & 31)))])
Code07_Forest1.cntg = jcast('int', 0)
Code07_Forest1.root = jarray('int', [Code07_Forest1.MAXN])
Code07_Forest1.left = jarray('int', [Code07_Forest1.MAXT])
Code07_Forest1.right = jarray('int', [Code07_Forest1.MAXT])
Code07_Forest1.siz = jarray('int', [Code07_Forest1.MAXT])
Code07_Forest1.cntt = jcast('int', 0)
Code07_Forest1.dep = jarray('int', [Code07_Forest1.MAXN])
Code07_Forest1.stjump = jarray('int', [Code07_Forest1.MAXN, Code07_Forest1.MAXP])
Code07_Forest1.treeHead = jarray('int', [Code07_Forest1.MAXN])
Code07_Forest1.setSiz = jarray('int', [Code07_Forest1.MAXN])
Code07_Forest1.stack = jarray('int', [Code07_Forest1.MAXN, 4])
Code07_Forest1.stackSize = jcast('int', 0)
Code07_Forest1.cur = jcast('int', 0)
Code07_Forest1.father = jcast('int', 0)
Code07_Forest1.treehead = jcast('int', 0)
Code07_Forest1.edge = jcast('int', 0)

if __name__ == '__main__':
    Code07_Forest1.main([])
