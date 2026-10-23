# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 电力，Python版
# 给定一张无向图，一共n个点、m条边，不保证所有点连通
# 点的编号0 ~ n-1，只能删除一个点的话，连通块最多有多少
# 1 <= n <= 10^4
# 1 <= m <= 2 * 10^4
# 测试链接 : https://loj.ac/p/10103
# 测试链接 : http://poj.org/problem?id=2117
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Electricity1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'block': 'block', 'ans': 'ans', 'stack': 'stack', 'u': 'u', 'root': 'root', 'son': 'son', 'cut': 'cut', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    block = 0
    ans = 0
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    root = 0
    son = 0
    cut = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, root, son, cut, status, e):
        u = jcast('int', u)
        root = jcast('int', root)
        son = jcast('int', son)
        cut = jcast('int', cut)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code02_Electricity1.stack[Code02_Electricity1.stacksize], 0, u)
        jset(Code02_Electricity1.stack[Code02_Electricity1.stacksize], 1, root)
        jset(Code02_Electricity1.stack[Code02_Electricity1.stacksize], 2, son)
        jset(Code02_Electricity1.stack[Code02_Electricity1.stacksize], 3, cut)
        jset(Code02_Electricity1.stack[Code02_Electricity1.stacksize], 4, status)
        jset(Code02_Electricity1.stack[Code02_Electricity1.stacksize], 5, e)
        Code02_Electricity1.stacksize = jcast('int', (Code02_Electricity1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_Electricity1.stacksize = jcast('int', (Code02_Electricity1.stacksize - 1))
        Code02_Electricity1.u = jcast('int', Code02_Electricity1.stack[Code02_Electricity1.stacksize][0])
        Code02_Electricity1.root = jcast('int', Code02_Electricity1.stack[Code02_Electricity1.stacksize][1])
        Code02_Electricity1.son = jcast('int', Code02_Electricity1.stack[Code02_Electricity1.stacksize][2])
        Code02_Electricity1.cut = jcast('int', Code02_Electricity1.stack[Code02_Electricity1.stacksize][3])
        Code02_Electricity1.status = jcast('int', Code02_Electricity1.stack[Code02_Electricity1.stacksize][4])
        Code02_Electricity1.e = jcast('int', Code02_Electricity1.stack[Code02_Electricity1.stacksize][5])

    @staticmethod
    def prepare():
        Code02_Electricity1.cntg = jcast('int', jset(Code02_Electricity1, 'cntd', jset(Code02_Electricity1, 'block', jset(Code02_Electricity1, 'ans', 0))))
        i = jcast('int', 1)
        while (i <= Code02_Electricity1.n):
            jset(Code02_Electricity1.head, i, jset(Code02_Electricity1.dfn, i, jset(Code02_Electricity1.low, i, 0)))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_Electricity1.nxt, ((_java_obj_1 := Code02_Electricity1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Electricity1.head[u])
        Code02_Electricity1.to[Code02_Electricity1.cntg] = jcast('int', v)
        Code02_Electricity1.head[u] = jcast('int', Code02_Electricity1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u, root):
        u = jcast('int', u)
        root = jcast('boolean', root)
        jset(Code02_Electricity1.dfn, u, jset(Code02_Electricity1.low, u, ((_java_obj_4 := Code02_Electricity1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        son = jcast('int', 0)
        cut = jcast('int', 0)
        e = jcast('int', Code02_Electricity1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Electricity1.to[e])
            if (Code02_Electricity1.dfn[v] == 0):
                son = jcast('int', (son + 1))
                Code02_Electricity1.tarjan1(v, False)
                jset(Code02_Electricity1.low, u, jstatic('Math', 'min', Code02_Electricity1.low[u], Code02_Electricity1.low[v]))
                if ((Code02_Electricity1.low[v] >= Code02_Electricity1.dfn[u]) and (not root)):
                    cut = jcast('int', (cut + 1))
            else:
                jset(Code02_Electricity1.low, u, jstatic('Math', 'min', Code02_Electricity1.low[u], Code02_Electricity1.dfn[v]))
            e = jcast('int', Code02_Electricity1.nxt[e])
        if root:
            Code02_Electricity1.ans = jcast('int', jstatic('Math', 'max', Code02_Electricity1.ans, son))
        else:
            Code02_Electricity1.ans = jcast('int', jstatic('Math', 'max', Code02_Electricity1.ans, jcast('int', jadd(cut, 1))))

    # 迭代版
    @staticmethod
    def tarjan2(node, rt):
        node = jcast('int', node)
        rt = jcast('boolean', rt)
        Code02_Electricity1.stacksize = jcast('int', 0)
        Code02_Electricity1.push(node, (1 if rt else 0), 0, 0, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code02_Electricity1.stacksize > 0):
            Code02_Electricity1.pop()
            if (Code02_Electricity1.status == jcast('int', (-1))):
                jset(Code02_Electricity1.dfn, Code02_Electricity1.u, jset(Code02_Electricity1.low, Code02_Electricity1.u, ((_java_obj_7 := Code02_Electricity1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
                Code02_Electricity1.e = jcast('int', Code02_Electricity1.head[Code02_Electricity1.u])
            else:
                v = jcast('int', Code02_Electricity1.to[Code02_Electricity1.e])
                if (Code02_Electricity1.status == 0):
                    jset(Code02_Electricity1.low, Code02_Electricity1.u, jstatic('Math', 'min', Code02_Electricity1.low[Code02_Electricity1.u], Code02_Electricity1.low[v]))
                    if ((Code02_Electricity1.low[v] >= Code02_Electricity1.dfn[Code02_Electricity1.u]) and (Code02_Electricity1.root == 0)):
                        Code02_Electricity1.cut = jcast('int', (Code02_Electricity1.cut + 1))
                else:
                    jset(Code02_Electricity1.low, Code02_Electricity1.u, jstatic('Math', 'min', Code02_Electricity1.low[Code02_Electricity1.u], Code02_Electricity1.dfn[v]))
                Code02_Electricity1.e = jcast('int', Code02_Electricity1.nxt[Code02_Electricity1.e])
            if (Code02_Electricity1.e != 0):
                v = jcast('int', Code02_Electricity1.to[Code02_Electricity1.e])
                if (Code02_Electricity1.dfn[v] == 0):
                    Code02_Electricity1.son = jcast('int', (Code02_Electricity1.son + 1))
                    Code02_Electricity1.push(Code02_Electricity1.u, Code02_Electricity1.root, Code02_Electricity1.son, Code02_Electricity1.cut, 0, Code02_Electricity1.e)
                    Code02_Electricity1.push(v, 0, 0, 0, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code02_Electricity1.push(Code02_Electricity1.u, Code02_Electricity1.root, Code02_Electricity1.son, Code02_Electricity1.cut, 1, Code02_Electricity1.e)
            else:
                if (Code02_Electricity1.root == 1):
                    Code02_Electricity1.ans = jcast('int', jstatic('Math', 'max', Code02_Electricity1.ans, Code02_Electricity1.son))
                else:
                    Code02_Electricity1.ans = jcast('int', jstatic('Math', 'max', Code02_Electricity1.ans, jcast('int', jadd(Code02_Electricity1.cut, 1))))

    @staticmethod
    def main(args):
        in_ = Code02_Electricity1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Electricity1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Electricity1.m = jcast('int', jcall(in_, 'nextInt'))
        while ((Code02_Electricity1.n != 0) or (Code02_Electricity1.m != 0)):
            Code02_Electricity1.prepare()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i <= Code02_Electricity1.m):
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                u = jcast('int', (u + 1))
                v = jcast('int', (v + 1))
                Code02_Electricity1.addEdge(u, v)
                Code02_Electricity1.addEdge(v, u)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code02_Electricity1.n):
                if (Code02_Electricity1.dfn[i] == 0):
                    Code02_Electricity1.block = jcast('int', (Code02_Electricity1.block + 1))
                    # tarjan1(i, true);
                    Code02_Electricity1.tarjan2(i, True)
                i = jcast('int', (i + 1))
            jcall(out, 'println', jcast('int', jadd(Code02_Electricity1.block, jcast('int', (Code02_Electricity1.ans - 1)))))
            Code02_Electricity1.n = jcast('int', jcall(in_, 'nextInt'))
            Code02_Electricity1.m = jcast('int', jcall(in_, 'nextInt'))
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
            raise TypeError("No matching overload for Code02_Electricity1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Electricity1.MAXN = jcast('int', 10001)
Code02_Electricity1.MAXM = jcast('int', 20001)
Code02_Electricity1.n = jcast('int', 0)
Code02_Electricity1.m = jcast('int', 0)
Code02_Electricity1.head = jarray('int', [Code02_Electricity1.MAXN])
Code02_Electricity1.nxt = jarray('int', [jcast('int', (Code02_Electricity1.MAXM << (1 & 31)))])
Code02_Electricity1.to = jarray('int', [jcast('int', (Code02_Electricity1.MAXM << (1 & 31)))])
Code02_Electricity1.cntg = jcast('int', 0)
Code02_Electricity1.dfn = jarray('int', [Code02_Electricity1.MAXN])
Code02_Electricity1.low = jarray('int', [Code02_Electricity1.MAXN])
Code02_Electricity1.cntd = jcast('int', 0)
Code02_Electricity1.block = jcast('int', 0)
Code02_Electricity1.ans = jcast('int', 0)
Code02_Electricity1.stack = jarray('int', [Code02_Electricity1.MAXN, 6])
Code02_Electricity1.u = jcast('int', 0)
Code02_Electricity1.root = jcast('int', 0)
Code02_Electricity1.son = jcast('int', 0)
Code02_Electricity1.cut = jcast('int', 0)
Code02_Electricity1.status = jcast('int', 0)
Code02_Electricity1.e = jcast('int', 0)
Code02_Electricity1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code02_Electricity1.main([])
