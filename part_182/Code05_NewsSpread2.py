# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 消息扩散，Python版
# 一共有n个城市，给定m条道路，道路可以传递消息，但道路是单向
# 你有一个消息，需要让所有城市都收到，计算至少要在几个城市发布该消息
# 1 <= n <= 10^5
# 1 <= m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2002
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_NewsSpread2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'indegree': 'indegree', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    a = None
    b = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    indegree = None
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
        jset(Code05_NewsSpread2.stack[Code05_NewsSpread2.stacksize], 0, u)
        jset(Code05_NewsSpread2.stack[Code05_NewsSpread2.stacksize], 1, status)
        jset(Code05_NewsSpread2.stack[Code05_NewsSpread2.stacksize], 2, e)
        Code05_NewsSpread2.stacksize = jcast('int', (Code05_NewsSpread2.stacksize + 1))

    @staticmethod
    def pop():
        Code05_NewsSpread2.stacksize = jcast('int', (Code05_NewsSpread2.stacksize - 1))
        Code05_NewsSpread2.u = jcast('int', Code05_NewsSpread2.stack[Code05_NewsSpread2.stacksize][0])
        Code05_NewsSpread2.status = jcast('int', Code05_NewsSpread2.stack[Code05_NewsSpread2.stacksize][1])
        Code05_NewsSpread2.e = jcast('int', Code05_NewsSpread2.stack[Code05_NewsSpread2.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_NewsSpread2.nxt, ((_java_obj_1 := Code05_NewsSpread2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_NewsSpread2.head[u])
        Code05_NewsSpread2.to[Code05_NewsSpread2.cntg] = jcast('int', v)
        Code05_NewsSpread2.head[u] = jcast('int', Code05_NewsSpread2.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code05_NewsSpread2.dfn, u, jset(Code05_NewsSpread2.low, u, ((_java_obj_4 := Code05_NewsSpread2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code05_NewsSpread2.sta, ((_java_obj_7 := Code05_NewsSpread2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code05_NewsSpread2.head[u])
        while (e > 0):
            v = jcast('int', Code05_NewsSpread2.to[e])
            if (Code05_NewsSpread2.dfn[v] == 0):
                Code05_NewsSpread2.tarjan1(v)
                jset(Code05_NewsSpread2.low, u, jstatic('Math', 'min', Code05_NewsSpread2.low[u], Code05_NewsSpread2.low[v]))
            else:
                if (Code05_NewsSpread2.belong[v] == 0):
                    jset(Code05_NewsSpread2.low, u, jstatic('Math', 'min', Code05_NewsSpread2.low[u], Code05_NewsSpread2.dfn[v]))
            e = jcast('int', Code05_NewsSpread2.nxt[e])
        if (Code05_NewsSpread2.dfn[u] == Code05_NewsSpread2.low[u]):
            Code05_NewsSpread2.sccCnt = jcast('int', (Code05_NewsSpread2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code05_NewsSpread2.sta[((_java_obj_10 := Code05_NewsSpread2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code05_NewsSpread2.belong[pop] = jcast('int', Code05_NewsSpread2.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code05_NewsSpread2.stacksize = jcast('int', 0)
        Code05_NewsSpread2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_NewsSpread2.stacksize > 0):
            Code05_NewsSpread2.pop()
            if (Code05_NewsSpread2.status == jcast('int', (-1))):
                jset(Code05_NewsSpread2.dfn, Code05_NewsSpread2.u, jset(Code05_NewsSpread2.low, Code05_NewsSpread2.u, ((_java_obj_13 := Code05_NewsSpread2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code05_NewsSpread2.sta, ((_java_obj_16 := Code05_NewsSpread2), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code05_NewsSpread2.u)
                Code05_NewsSpread2.e = jcast('int', Code05_NewsSpread2.head[Code05_NewsSpread2.u])
            else:
                v = jcast('int', Code05_NewsSpread2.to[Code05_NewsSpread2.e])
                if (Code05_NewsSpread2.status == 0):
                    jset(Code05_NewsSpread2.low, Code05_NewsSpread2.u, jstatic('Math', 'min', Code05_NewsSpread2.low[Code05_NewsSpread2.u], Code05_NewsSpread2.low[v]))
                if ((Code05_NewsSpread2.status == 1) and (Code05_NewsSpread2.belong[v] == 0)):
                    jset(Code05_NewsSpread2.low, Code05_NewsSpread2.u, jstatic('Math', 'min', Code05_NewsSpread2.low[Code05_NewsSpread2.u], Code05_NewsSpread2.dfn[v]))
                Code05_NewsSpread2.e = jcast('int', Code05_NewsSpread2.nxt[Code05_NewsSpread2.e])
            if (Code05_NewsSpread2.e != 0):
                v = jcast('int', Code05_NewsSpread2.to[Code05_NewsSpread2.e])
                if (Code05_NewsSpread2.dfn[v] == 0):
                    Code05_NewsSpread2.push(Code05_NewsSpread2.u, 0, Code05_NewsSpread2.e)
                    Code05_NewsSpread2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_NewsSpread2.push(Code05_NewsSpread2.u, 1, Code05_NewsSpread2.e)
            else:
                if (Code05_NewsSpread2.dfn[Code05_NewsSpread2.u] == Code05_NewsSpread2.low[Code05_NewsSpread2.u]):
                    Code05_NewsSpread2.sccCnt = jcast('int', (Code05_NewsSpread2.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code05_NewsSpread2.sta[((_java_obj_19 := Code05_NewsSpread2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code05_NewsSpread2.belong[pop] = jcast('int', Code05_NewsSpread2.sccCnt)
                        if not ((pop != Code05_NewsSpread2.u)):
                            break

    @staticmethod
    def main(args):
        in_ = Code05_NewsSpread2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_NewsSpread2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_NewsSpread2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_NewsSpread2.m):
            jset(Code05_NewsSpread2.a, i, jcall(in_, 'nextInt'))
            jset(Code05_NewsSpread2.b, i, jcall(in_, 'nextInt'))
            Code05_NewsSpread2.addEdge(Code05_NewsSpread2.a[i], Code05_NewsSpread2.b[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_NewsSpread2.n):
            if (Code05_NewsSpread2.dfn[i] == 0):
                # tarjan1(i);
                Code05_NewsSpread2.tarjan2(i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_NewsSpread2.m):
            scc1 = jcast('int', Code05_NewsSpread2.belong[Code05_NewsSpread2.a[i]])
            scc2 = jcast('int', Code05_NewsSpread2.belong[Code05_NewsSpread2.b[i]])
            if (scc1 != scc2):
                Code05_NewsSpread2.indegree[scc2] = jcast('int', (Code05_NewsSpread2.indegree[scc2] + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_NewsSpread2.sccCnt):
            if (Code05_NewsSpread2.indegree[i] == 0):
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
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
            raise TypeError("No matching overload for Code05_NewsSpread2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_NewsSpread2.MAXN = jcast('int', 100001)
Code05_NewsSpread2.MAXM = jcast('int', 500001)
Code05_NewsSpread2.n = jcast('int', 0)
Code05_NewsSpread2.m = jcast('int', 0)
Code05_NewsSpread2.a = jarray('int', [Code05_NewsSpread2.MAXM])
Code05_NewsSpread2.b = jarray('int', [Code05_NewsSpread2.MAXM])
Code05_NewsSpread2.head = jarray('int', [Code05_NewsSpread2.MAXN])
Code05_NewsSpread2.nxt = jarray('int', [Code05_NewsSpread2.MAXM])
Code05_NewsSpread2.to = jarray('int', [Code05_NewsSpread2.MAXM])
Code05_NewsSpread2.cntg = jcast('int', 0)
Code05_NewsSpread2.dfn = jarray('int', [Code05_NewsSpread2.MAXN])
Code05_NewsSpread2.low = jarray('int', [Code05_NewsSpread2.MAXN])
Code05_NewsSpread2.cntd = jcast('int', 0)
Code05_NewsSpread2.sta = jarray('int', [Code05_NewsSpread2.MAXN])
Code05_NewsSpread2.top = jcast('int', 0)
Code05_NewsSpread2.belong = jarray('int', [Code05_NewsSpread2.MAXN])
Code05_NewsSpread2.sccCnt = jcast('int', 0)
Code05_NewsSpread2.indegree = jarray('int', [Code05_NewsSpread2.MAXN])
Code05_NewsSpread2.stack = jarray('int', [Code05_NewsSpread2.MAXN, 3])
Code05_NewsSpread2.u = jcast('int', 0)
Code05_NewsSpread2.status = jcast('int', 0)
Code05_NewsSpread2.e = jcast('int', 0)
Code05_NewsSpread2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code05_NewsSpread2.main([])
