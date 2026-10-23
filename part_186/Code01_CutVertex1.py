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

# 割点模版题，Python版
# 给定一张无向图，一共n个点、m条边，不保证所有点连通
# 打印图中割点的数量，然后从小到大打印所有割点的编号
# 1 <= n <= 2 * 10^4
# 1 <= m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3388
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_CutVertex1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'cutVertex': 'cutVertex', 'stack': 'stack', 'u': 'u', 'root': 'root', 'son': 'son', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    cutVertex = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    root = 0
    son = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, root, son, status, e):
        u = jcast('int', u)
        root = jcast('int', root)
        son = jcast('int', son)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code01_CutVertex1.stack[Code01_CutVertex1.stacksize], 0, u)
        jset(Code01_CutVertex1.stack[Code01_CutVertex1.stacksize], 1, root)
        jset(Code01_CutVertex1.stack[Code01_CutVertex1.stacksize], 2, son)
        jset(Code01_CutVertex1.stack[Code01_CutVertex1.stacksize], 3, status)
        jset(Code01_CutVertex1.stack[Code01_CutVertex1.stacksize], 4, e)
        Code01_CutVertex1.stacksize = jcast('int', (Code01_CutVertex1.stacksize + 1))

    @staticmethod
    def pop():
        Code01_CutVertex1.stacksize = jcast('int', (Code01_CutVertex1.stacksize - 1))
        Code01_CutVertex1.u = jcast('int', Code01_CutVertex1.stack[Code01_CutVertex1.stacksize][0])
        Code01_CutVertex1.root = jcast('int', Code01_CutVertex1.stack[Code01_CutVertex1.stacksize][1])
        Code01_CutVertex1.son = jcast('int', Code01_CutVertex1.stack[Code01_CutVertex1.stacksize][2])
        Code01_CutVertex1.status = jcast('int', Code01_CutVertex1.stack[Code01_CutVertex1.stacksize][3])
        Code01_CutVertex1.e = jcast('int', Code01_CutVertex1.stack[Code01_CutVertex1.stacksize][4])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_CutVertex1.nxt, ((_java_obj_1 := Code01_CutVertex1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_CutVertex1.head[u])
        Code01_CutVertex1.to[Code01_CutVertex1.cntg] = jcast('int', v)
        Code01_CutVertex1.head[u] = jcast('int', Code01_CutVertex1.cntg)

    # 递归版，Tarjan算法求解割点
    @staticmethod
    def tarjan1(u, root):
        u = jcast('int', u)
        root = jcast('boolean', root)
        jset(Code01_CutVertex1.dfn, u, jset(Code01_CutVertex1.low, u, ((_java_obj_4 := Code01_CutVertex1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        son = jcast('int', 0)
        e = jcast('int', Code01_CutVertex1.head[u])
        while (e > 0):
            v = jcast('int', Code01_CutVertex1.to[e])
            if (Code01_CutVertex1.dfn[v] == 0):
                son = jcast('int', (son + 1))
                Code01_CutVertex1.tarjan1(v, False)
                jset(Code01_CutVertex1.low, u, jstatic('Math', 'min', Code01_CutVertex1.low[u], Code01_CutVertex1.low[v]))
                if (Code01_CutVertex1.low[v] >= Code01_CutVertex1.dfn[u]):
                    if ((not root) or (son >= 2)):
                        Code01_CutVertex1.cutVertex[u] = jcast('boolean', True)
            else:
                jset(Code01_CutVertex1.low, u, jstatic('Math', 'min', Code01_CutVertex1.low[u], Code01_CutVertex1.dfn[v]))
            e = jcast('int', Code01_CutVertex1.nxt[e])

    # 迭代版，Tarjan算法求解割点
    @staticmethod
    def tarjan2(node, rt):
        node = jcast('int', node)
        rt = jcast('boolean', rt)
        Code01_CutVertex1.stacksize = jcast('int', 0)
        Code01_CutVertex1.push(node, (1 if rt else 0), 0, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code01_CutVertex1.stacksize > 0):
            Code01_CutVertex1.pop()
            if (Code01_CutVertex1.status == jcast('int', (-1))):
                jset(Code01_CutVertex1.dfn, Code01_CutVertex1.u, jset(Code01_CutVertex1.low, Code01_CutVertex1.u, ((_java_obj_7 := Code01_CutVertex1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
                Code01_CutVertex1.e = jcast('int', Code01_CutVertex1.head[Code01_CutVertex1.u])
            else:
                v = jcast('int', Code01_CutVertex1.to[Code01_CutVertex1.e])
                if (Code01_CutVertex1.status == 0):
                    jset(Code01_CutVertex1.low, Code01_CutVertex1.u, jstatic('Math', 'min', Code01_CutVertex1.low[Code01_CutVertex1.u], Code01_CutVertex1.low[v]))
                    if (Code01_CutVertex1.low[v] >= Code01_CutVertex1.dfn[Code01_CutVertex1.u]):
                        if ((Code01_CutVertex1.root == 0) or (Code01_CutVertex1.son >= 2)):
                            Code01_CutVertex1.cutVertex[Code01_CutVertex1.u] = jcast('boolean', True)
                else:
                    jset(Code01_CutVertex1.low, Code01_CutVertex1.u, jstatic('Math', 'min', Code01_CutVertex1.low[Code01_CutVertex1.u], Code01_CutVertex1.dfn[v]))
                Code01_CutVertex1.e = jcast('int', Code01_CutVertex1.nxt[Code01_CutVertex1.e])
            if (Code01_CutVertex1.e != 0):
                v = jcast('int', Code01_CutVertex1.to[Code01_CutVertex1.e])
                if (Code01_CutVertex1.dfn[v] == 0):
                    Code01_CutVertex1.son = jcast('int', (Code01_CutVertex1.son + 1))
                    Code01_CutVertex1.push(Code01_CutVertex1.u, Code01_CutVertex1.root, Code01_CutVertex1.son, 0, Code01_CutVertex1.e)
                    Code01_CutVertex1.push(v, 0, 0, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code01_CutVertex1.push(Code01_CutVertex1.u, Code01_CutVertex1.root, Code01_CutVertex1.son, 1, Code01_CutVertex1.e)

    @staticmethod
    def main(args):
        in_ = Code01_CutVertex1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_CutVertex1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_CutVertex1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code01_CutVertex1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code01_CutVertex1.addEdge(u, v)
            Code01_CutVertex1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CutVertex1.n):
            if (Code01_CutVertex1.dfn[i] == 0):
                # tarjan1(i, true);
                Code01_CutVertex1.tarjan2(i, True)
            i = jcast('int', (i + 1))
        cntCnt = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_CutVertex1.n):
            if Code01_CutVertex1.cutVertex[i]:
                cntCnt = jcast('int', (cntCnt + 1))
            i = jcast('int', (i + 1))
        jcall(out, 'println', cntCnt)
        i = jcast('int', 1)
        while (i <= Code01_CutVertex1.n):
            if Code01_CutVertex1.cutVertex[i]:
                jcall(out, 'print', jadd(i, ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            raise TypeError("No matching overload for Code01_CutVertex1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CutVertex1.MAXN = jcast('int', 20001)
Code01_CutVertex1.MAXM = jcast('int', 100001)
Code01_CutVertex1.n = jcast('int', 0)
Code01_CutVertex1.m = jcast('int', 0)
Code01_CutVertex1.head = jarray('int', [Code01_CutVertex1.MAXN])
Code01_CutVertex1.nxt = jarray('int', [jcast('int', (Code01_CutVertex1.MAXM << (1 & 31)))])
Code01_CutVertex1.to = jarray('int', [jcast('int', (Code01_CutVertex1.MAXM << (1 & 31)))])
Code01_CutVertex1.cntg = jcast('int', 0)
Code01_CutVertex1.dfn = jarray('int', [Code01_CutVertex1.MAXN])
Code01_CutVertex1.low = jarray('int', [Code01_CutVertex1.MAXN])
Code01_CutVertex1.cntd = jcast('int', 0)
Code01_CutVertex1.cutVertex = jarray('boolean', [Code01_CutVertex1.MAXN])
Code01_CutVertex1.stack = jarray('int', [Code01_CutVertex1.MAXN, 5])
Code01_CutVertex1.u = jcast('int', 0)
Code01_CutVertex1.root = jcast('int', 0)
Code01_CutVertex1.son = jcast('int', 0)
Code01_CutVertex1.status = jcast('int', 0)
Code01_CutVertex1.e = jcast('int', 0)
Code01_CutVertex1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code01_CutVertex1.main([])
