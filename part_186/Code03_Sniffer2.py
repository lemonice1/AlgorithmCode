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

# 嗅探器，Python版
# 给定一张n个点、m条边的无向图，所有节点属于一个连通区
# 给定点a和点b，如果删掉别的点能让a和b不再连通，这个点叫关键点
# 打印编号最小的关键点，不存在打印"No solution"
# 1 <= n <= 2 * 10^5
# 1 <= m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5058
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Sniffer2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'isKey': 'isKey', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    a = 0
    b = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    isKey = None
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
        jset(Code03_Sniffer2.stack[Code03_Sniffer2.stacksize], 0, u)
        jset(Code03_Sniffer2.stack[Code03_Sniffer2.stacksize], 1, status)
        jset(Code03_Sniffer2.stack[Code03_Sniffer2.stacksize], 2, e)
        Code03_Sniffer2.stacksize = jcast('int', (Code03_Sniffer2.stacksize + 1))

    @staticmethod
    def pop():
        Code03_Sniffer2.stacksize = jcast('int', (Code03_Sniffer2.stacksize - 1))
        Code03_Sniffer2.u = jcast('int', Code03_Sniffer2.stack[Code03_Sniffer2.stacksize][0])
        Code03_Sniffer2.status = jcast('int', Code03_Sniffer2.stack[Code03_Sniffer2.stacksize][1])
        Code03_Sniffer2.e = jcast('int', Code03_Sniffer2.stack[Code03_Sniffer2.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_Sniffer2.nxt, ((_java_obj_1 := Code03_Sniffer2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Sniffer2.head[u])
        Code03_Sniffer2.to[Code03_Sniffer2.cntg] = jcast('int', v)
        Code03_Sniffer2.head[u] = jcast('int', Code03_Sniffer2.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code03_Sniffer2.dfn, u, jset(Code03_Sniffer2.low, u, ((_java_obj_4 := Code03_Sniffer2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        e = jcast('int', Code03_Sniffer2.head[u])
        while (e > 0):
            v = jcast('int', Code03_Sniffer2.to[e])
            if (Code03_Sniffer2.dfn[v] == 0):
                Code03_Sniffer2.tarjan1(v)
                jset(Code03_Sniffer2.low, u, jstatic('Math', 'min', Code03_Sniffer2.low[u], Code03_Sniffer2.low[v]))
                if ((((Code03_Sniffer2.low[v] >= Code03_Sniffer2.dfn[u]) and (u != Code03_Sniffer2.a)) and (u != Code03_Sniffer2.b)) and (Code03_Sniffer2.dfn[Code03_Sniffer2.b] >= Code03_Sniffer2.dfn[v])):
                    Code03_Sniffer2.isKey[u] = jcast('boolean', True)
            else:
                jset(Code03_Sniffer2.low, u, jstatic('Math', 'min', Code03_Sniffer2.low[u], Code03_Sniffer2.dfn[v]))
            e = jcast('int', Code03_Sniffer2.nxt[e])

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code03_Sniffer2.stacksize = jcast('int', 0)
        Code03_Sniffer2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code03_Sniffer2.stacksize > 0):
            Code03_Sniffer2.pop()
            if (Code03_Sniffer2.status == jcast('int', (-1))):
                jset(Code03_Sniffer2.dfn, Code03_Sniffer2.u, jset(Code03_Sniffer2.low, Code03_Sniffer2.u, ((_java_obj_7 := Code03_Sniffer2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
                Code03_Sniffer2.e = jcast('int', Code03_Sniffer2.head[Code03_Sniffer2.u])
            else:
                v = jcast('int', Code03_Sniffer2.to[Code03_Sniffer2.e])
                if (Code03_Sniffer2.status == 0):
                    jset(Code03_Sniffer2.low, Code03_Sniffer2.u, jstatic('Math', 'min', Code03_Sniffer2.low[Code03_Sniffer2.u], Code03_Sniffer2.low[v]))
                    if ((((Code03_Sniffer2.low[v] >= Code03_Sniffer2.dfn[Code03_Sniffer2.u]) and (Code03_Sniffer2.u != Code03_Sniffer2.a)) and (Code03_Sniffer2.u != Code03_Sniffer2.b)) and (Code03_Sniffer2.dfn[Code03_Sniffer2.b] >= Code03_Sniffer2.dfn[v])):
                        Code03_Sniffer2.isKey[Code03_Sniffer2.u] = jcast('boolean', True)
                else:
                    jset(Code03_Sniffer2.low, Code03_Sniffer2.u, jstatic('Math', 'min', Code03_Sniffer2.low[Code03_Sniffer2.u], Code03_Sniffer2.dfn[v]))
                Code03_Sniffer2.e = jcast('int', Code03_Sniffer2.nxt[Code03_Sniffer2.e])
            if (Code03_Sniffer2.e != 0):
                v = jcast('int', Code03_Sniffer2.to[Code03_Sniffer2.e])
                if (Code03_Sniffer2.dfn[v] == 0):
                    Code03_Sniffer2.push(Code03_Sniffer2.u, 0, Code03_Sniffer2.e)
                    Code03_Sniffer2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code03_Sniffer2.push(Code03_Sniffer2.u, 1, Code03_Sniffer2.e)

    @staticmethod
    def main(args):
        in_ = Code03_Sniffer2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Sniffer2.n = jcast('int', jcall(in_, 'nextInt'))
        u = jcast('int', jcall(in_, 'nextInt'))
        v = jcast('int', jcall(in_, 'nextInt'))
        while ((u != 0) or (v != 0)):
            Code03_Sniffer2.addEdge(u, v)
            Code03_Sniffer2.addEdge(v, u)
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
        Code03_Sniffer2.a = jcast('int', jcall(in_, 'nextInt'))
        Code03_Sniffer2.b = jcast('int', jcall(in_, 'nextInt'))
        # tarjan1(a);
        Code03_Sniffer2.tarjan2(Code03_Sniffer2.a)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_Sniffer2.n):
            try:
                if Code03_Sniffer2.isKey[i]:
                    ans = jcast('int', i)
                    raise JBreak(None)
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if (ans == 0):
            jcall(out, 'println', 'No solution')
        else:
            jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code03_Sniffer2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Sniffer2.MAXN = jcast('int', 200001)
Code03_Sniffer2.MAXM = jcast('int', 500001)
Code03_Sniffer2.n = jcast('int', 0)
Code03_Sniffer2.a = jcast('int', 0)
Code03_Sniffer2.b = jcast('int', 0)
Code03_Sniffer2.head = jarray('int', [Code03_Sniffer2.MAXN])
Code03_Sniffer2.nxt = jarray('int', [jcast('int', (Code03_Sniffer2.MAXM << (1 & 31)))])
Code03_Sniffer2.to = jarray('int', [jcast('int', (Code03_Sniffer2.MAXM << (1 & 31)))])
Code03_Sniffer2.cntg = jcast('int', 0)
Code03_Sniffer2.dfn = jarray('int', [Code03_Sniffer2.MAXN])
Code03_Sniffer2.low = jarray('int', [Code03_Sniffer2.MAXN])
Code03_Sniffer2.cntd = jcast('int', 0)
Code03_Sniffer2.isKey = jarray('boolean', [Code03_Sniffer2.MAXN])
Code03_Sniffer2.stack = jarray('int', [Code03_Sniffer2.MAXN, 3])
Code03_Sniffer2.u = jcast('int', 0)
Code03_Sniffer2.status = jcast('int', 0)
Code03_Sniffer2.e = jcast('int', 0)
Code03_Sniffer2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code03_Sniffer2.main([])
