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

# 点双连通分量模版题2，Python版
# 给定一张无向图，一共n个点、m条边
# 忽略所有孤立点，打印点双连通分量的个数
# 打印每个点双连通分量内部的节点编号，编号按照从小到大组织
# 内部节点编号是一个序列，序列字典序小的点双连通分量先打印
# 1 <= n <= 5 * 10^4
# 1 <= m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/B3610
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_VBCC1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'vbccArr': 'vbccArr', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    sta = None
    top = 0
    vbccArr = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code05_VBCC1.stack[Code05_VBCC1.stacksize], 0, u)
        jset(Code05_VBCC1.stack[Code05_VBCC1.stacksize], 1, status)
        jset(Code05_VBCC1.stack[Code05_VBCC1.stacksize], 2, e)
        Code05_VBCC1.stacksize = jcast('int', (Code05_VBCC1.stacksize + 1))

    @staticmethod
    def pop():
        Code05_VBCC1.stacksize = jcast('int', (Code05_VBCC1.stacksize - 1))
        Code05_VBCC1.u = jcast('int', Code05_VBCC1.stack[Code05_VBCC1.stacksize][0])
        Code05_VBCC1.status = jcast('int', Code05_VBCC1.stack[Code05_VBCC1.stacksize][1])
        Code05_VBCC1.e = jcast('int', Code05_VBCC1.stack[Code05_VBCC1.stacksize][2])

    class VbccCmp:
        __java_fields__ = {}
        def compare(self, o1, o2):
            size = jcast('int', jstatic('Math', 'min', jcall(o1, 'size'), jcall(o2, 'size')))
            i = jcast('int', 0)
            while (i < size):
                if (not jcall(jcall(o1, 'get', i), 'equals', jcall(o2, 'get', i))):
                    return jcast('int', jcall(jcall(o1, 'get', i), 'compareTo', jcall(o2, 'get', i)))
                i = jcast('int', (i + 1))
            return jcast('int', jcast('int', (jcall(o1, 'size') - jcall(o2, 'size'))))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_VBCC1.nxt, ((_java_obj_1 := Code05_VBCC1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_VBCC1.head[u])
        Code05_VBCC1.to[Code05_VBCC1.cntg] = jcast('int', v)
        Code05_VBCC1.head[u] = jcast('int', Code05_VBCC1.cntg)

    # 递归版，Tarjan算法求解点双连通分量
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code05_VBCC1.dfn, u, jset(Code05_VBCC1.low, u, ((_java_obj_4 := Code05_VBCC1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code05_VBCC1.sta, ((_java_obj_7 := Code05_VBCC1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code05_VBCC1.head[u])
        while (e > 0):
            v = jcast('int', Code05_VBCC1.to[e])
            if (Code05_VBCC1.dfn[v] == 0):
                Code05_VBCC1.tarjan1(v)
                jset(Code05_VBCC1.low, u, jstatic('Math', 'min', Code05_VBCC1.low[u], Code05_VBCC1.low[v]))
                if (Code05_VBCC1.low[v] == Code05_VBCC1.dfn[u]):
                    list = jnew('ArrayList')
                    jcall(list, 'add', u)
                    pop = 0
                    while True:
                        pop = jcast('int', Code05_VBCC1.sta[((_java_obj_10 := Code05_VBCC1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                        jcall(list, 'add', pop)
                        if not ((pop != v)):
                            break
                    jcall(Code05_VBCC1.vbccArr, 'add', list)
            else:
                jset(Code05_VBCC1.low, u, jstatic('Math', 'min', Code05_VBCC1.low[u], Code05_VBCC1.dfn[v]))
            e = jcast('int', Code05_VBCC1.nxt[e])

    # 迭代版，Tarjan算法求解点双连通分量
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code05_VBCC1.stacksize = jcast('int', 0)
        Code05_VBCC1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_VBCC1.stacksize > 0):
            Code05_VBCC1.pop()
            if (Code05_VBCC1.status == jcast('int', (-1))):
                jset(Code05_VBCC1.dfn, Code05_VBCC1.u, jset(Code05_VBCC1.low, Code05_VBCC1.u, ((_java_obj_13 := Code05_VBCC1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code05_VBCC1.sta, ((_java_obj_16 := Code05_VBCC1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code05_VBCC1.u)
                Code05_VBCC1.e = jcast('int', Code05_VBCC1.head[Code05_VBCC1.u])
            else:
                v = jcast('int', Code05_VBCC1.to[Code05_VBCC1.e])
                if (Code05_VBCC1.status == 0):
                    jset(Code05_VBCC1.low, Code05_VBCC1.u, jstatic('Math', 'min', Code05_VBCC1.low[Code05_VBCC1.u], Code05_VBCC1.low[v]))
                    if (Code05_VBCC1.low[v] == Code05_VBCC1.dfn[Code05_VBCC1.u]):
                        list = jnew('ArrayList')
                        jcall(list, 'add', Code05_VBCC1.u)
                        pop = 0
                        while True:
                            pop = jcast('int', Code05_VBCC1.sta[((_java_obj_19 := Code05_VBCC1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                            jcall(list, 'add', pop)
                            if not ((pop != v)):
                                break
                        jcall(Code05_VBCC1.vbccArr, 'add', list)
                else:
                    jset(Code05_VBCC1.low, Code05_VBCC1.u, jstatic('Math', 'min', Code05_VBCC1.low[Code05_VBCC1.u], Code05_VBCC1.dfn[v]))
                Code05_VBCC1.e = jcast('int', Code05_VBCC1.nxt[Code05_VBCC1.e])
            if (Code05_VBCC1.e != 0):
                v = jcast('int', Code05_VBCC1.to[Code05_VBCC1.e])
                if (Code05_VBCC1.dfn[v] == 0):
                    Code05_VBCC1.push(Code05_VBCC1.u, 0, Code05_VBCC1.e)
                    Code05_VBCC1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_VBCC1.push(Code05_VBCC1.u, 1, Code05_VBCC1.e)

    @staticmethod
    def main(args):
        in_ = Code05_VBCC1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_VBCC1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_VBCC1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code05_VBCC1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code05_VBCC1.addEdge(u, v)
            Code05_VBCC1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_VBCC1.n):
            if ((Code05_VBCC1.dfn[i] == 0) and (Code05_VBCC1.head[i] > 0)):
                # tarjan1(i);
                Code05_VBCC1.tarjan2(i)
            i = jcast('int', (i + 1))
        jcall(out, 'println', jcall(Code05_VBCC1.vbccArr, 'size'))
        i = jcast('int', 0)
        while (i < jcall(Code05_VBCC1.vbccArr, 'size')):
            jcall(jcall(Code05_VBCC1.vbccArr, 'get', i), 'sort', (lambda a, b: jcall(a, 'compareTo', b)))
            i = jcast('int', (i + 1))
        jcall(Code05_VBCC1.vbccArr, 'sort', Code05_VBCC1.VbccCmp())
        i = jcast('int', 0)
        while (i < jcall(Code05_VBCC1.vbccArr, 'size')):
            for node in jcall(Code05_VBCC1.vbccArr, 'get', i):
                jcall(out, 'print', jadd(node, ' '))
            jcall(out, 'println')
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
            return jcast('int', self.buffer[((_java_obj_22 := self), (_java_key_23 := 'ptr'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]])

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
            raise TypeError("No matching overload for Code05_VBCC1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_VBCC1.MAXN = jcast('int', 50001)
Code05_VBCC1.MAXM = jcast('int', 300001)
Code05_VBCC1.n = jcast('int', 0)
Code05_VBCC1.m = jcast('int', 0)
Code05_VBCC1.head = jarray('int', [Code05_VBCC1.MAXN])
Code05_VBCC1.nxt = jarray('int', [jcast('int', (Code05_VBCC1.MAXM << (1 & 31)))])
Code05_VBCC1.to = jarray('int', [jcast('int', (Code05_VBCC1.MAXM << (1 & 31)))])
Code05_VBCC1.cntg = jcast('int', 0)
Code05_VBCC1.dfn = jarray('int', [Code05_VBCC1.MAXN])
Code05_VBCC1.low = jarray('int', [Code05_VBCC1.MAXN])
Code05_VBCC1.cntd = jcast('int', 0)
Code05_VBCC1.sta = jarray('int', [Code05_VBCC1.MAXN])
Code05_VBCC1.top = jcast('int', 0)
Code05_VBCC1.vbccArr = jnew('ArrayList')
Code05_VBCC1.stack = jarray('int', [Code05_VBCC1.MAXN, 3])
Code05_VBCC1.u = jcast('int', 0)
Code05_VBCC1.status = jcast('int', 0)
Code05_VBCC1.e = jcast('int', 0)
Code05_VBCC1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code05_VBCC1.main([])
