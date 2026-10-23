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

# 2-SAT模版题，Python版
# 一共n个变量，变量的编号1~n，每个变量的取值不是0就是1
# 给定m条限制，每条限制的格式 x1 v1 x2 v2，含义如下
# 编号为x1的变量取值为v1 或者 编号为x2的变量取值为v2
# 决定每个变量的值，来满足所有限制，如果无法做到，打印"IMPOSSIBLE"
# 如果可以做到，先打印"POSSIBLE"，然后打印每个变量的值，任何一种方案都可以
# 1 <= n、m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P4782
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_2SAT1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
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
    belong = None
    sccCnt = 0
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
        jset(Code01_2SAT1.stack[Code01_2SAT1.stacksize], 0, u)
        jset(Code01_2SAT1.stack[Code01_2SAT1.stacksize], 1, status)
        jset(Code01_2SAT1.stack[Code01_2SAT1.stacksize], 2, e)
        Code01_2SAT1.stacksize = jcast('int', (Code01_2SAT1.stacksize + 1))

    @staticmethod
    def pop():
        Code01_2SAT1.stacksize = jcast('int', (Code01_2SAT1.stacksize - 1))
        Code01_2SAT1.u = jcast('int', Code01_2SAT1.stack[Code01_2SAT1.stacksize][0])
        Code01_2SAT1.status = jcast('int', Code01_2SAT1.stack[Code01_2SAT1.stacksize][1])
        Code01_2SAT1.e = jcast('int', Code01_2SAT1.stack[Code01_2SAT1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_2SAT1.nxt, ((_java_obj_1 := Code01_2SAT1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_2SAT1.head[u])
        Code01_2SAT1.to[Code01_2SAT1.cntg] = jcast('int', v)
        Code01_2SAT1.head[u] = jcast('int', Code01_2SAT1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code01_2SAT1.dfn, u, jset(Code01_2SAT1.low, u, ((_java_obj_4 := Code01_2SAT1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code01_2SAT1.sta, ((_java_obj_7 := Code01_2SAT1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code01_2SAT1.head[u])
        while (e > 0):
            v = jcast('int', Code01_2SAT1.to[e])
            if (Code01_2SAT1.dfn[v] == 0):
                Code01_2SAT1.tarjan1(v)
                jset(Code01_2SAT1.low, u, jstatic('Math', 'min', Code01_2SAT1.low[u], Code01_2SAT1.low[v]))
            else:
                if (Code01_2SAT1.belong[v] == 0):
                    jset(Code01_2SAT1.low, u, jstatic('Math', 'min', Code01_2SAT1.low[u], Code01_2SAT1.dfn[v]))
            e = jcast('int', Code01_2SAT1.nxt[e])
        if (Code01_2SAT1.dfn[u] == Code01_2SAT1.low[u]):
            Code01_2SAT1.sccCnt = jcast('int', (Code01_2SAT1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code01_2SAT1.sta[((_java_obj_10 := Code01_2SAT1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code01_2SAT1.belong[pop] = jcast('int', Code01_2SAT1.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code01_2SAT1.stacksize = jcast('int', 0)
        Code01_2SAT1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code01_2SAT1.stacksize > 0):
            Code01_2SAT1.pop()
            if (Code01_2SAT1.status == jcast('int', (-1))):
                jset(Code01_2SAT1.dfn, Code01_2SAT1.u, jset(Code01_2SAT1.low, Code01_2SAT1.u, ((_java_obj_13 := Code01_2SAT1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code01_2SAT1.sta, ((_java_obj_16 := Code01_2SAT1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code01_2SAT1.u)
                Code01_2SAT1.e = jcast('int', Code01_2SAT1.head[Code01_2SAT1.u])
            else:
                v = jcast('int', Code01_2SAT1.to[Code01_2SAT1.e])
                if (Code01_2SAT1.status == 0):
                    jset(Code01_2SAT1.low, Code01_2SAT1.u, jstatic('Math', 'min', Code01_2SAT1.low[Code01_2SAT1.u], Code01_2SAT1.low[v]))
                if ((Code01_2SAT1.status == 1) and (Code01_2SAT1.belong[v] == 0)):
                    jset(Code01_2SAT1.low, Code01_2SAT1.u, jstatic('Math', 'min', Code01_2SAT1.low[Code01_2SAT1.u], Code01_2SAT1.dfn[v]))
                Code01_2SAT1.e = jcast('int', Code01_2SAT1.nxt[Code01_2SAT1.e])
            if (Code01_2SAT1.e != 0):
                v = jcast('int', Code01_2SAT1.to[Code01_2SAT1.e])
                if (Code01_2SAT1.dfn[v] == 0):
                    Code01_2SAT1.push(Code01_2SAT1.u, 0, Code01_2SAT1.e)
                    Code01_2SAT1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code01_2SAT1.push(Code01_2SAT1.u, 1, Code01_2SAT1.e)
            else:
                if (Code01_2SAT1.dfn[Code01_2SAT1.u] == Code01_2SAT1.low[Code01_2SAT1.u]):
                    Code01_2SAT1.sccCnt = jcast('int', (Code01_2SAT1.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code01_2SAT1.sta[((_java_obj_19 := Code01_2SAT1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code01_2SAT1.belong[pop] = jcast('int', Code01_2SAT1.sccCnt)
                        if not ((pop != Code01_2SAT1.u)):
                            break

    @staticmethod
    def main(args):
        in_ = Code01_2SAT1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_2SAT1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_2SAT1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x1 = 0
        v1 = 0
        x2 = 0
        v2 = 0
        while (i <= Code01_2SAT1.m):
            x1 = jcast('int', jcall(in_, 'nextInt'))
            v1 = jcast('int', jcall(in_, 'nextInt'))
            x2 = jcast('int', jcall(in_, 'nextInt'))
            v2 = jcast('int', jcall(in_, 'nextInt'))
            if ((v1 == 1) and (v2 == 1)):
                Code01_2SAT1.addEdge(jcast('int', jadd(x1, Code01_2SAT1.n)), x2)
                Code01_2SAT1.addEdge(jcast('int', jadd(x2, Code01_2SAT1.n)), x1)
            else:
                if ((v1 == 0) and (v2 == 1)):
                    Code01_2SAT1.addEdge(x1, x2)
                    Code01_2SAT1.addEdge(jcast('int', jadd(x2, Code01_2SAT1.n)), jcast('int', jadd(x1, Code01_2SAT1.n)))
                else:
                    if ((v1 == 1) and (v2 == 0)):
                        Code01_2SAT1.addEdge(x2, x1)
                        Code01_2SAT1.addEdge(jcast('int', jadd(x1, Code01_2SAT1.n)), jcast('int', jadd(x2, Code01_2SAT1.n)))
                    else:
                        Code01_2SAT1.addEdge(x1, jcast('int', jadd(x2, Code01_2SAT1.n)))
                        Code01_2SAT1.addEdge(x2, jcast('int', jadd(x1, Code01_2SAT1.n)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code01_2SAT1.n << (1 & 31)))):
            if (Code01_2SAT1.dfn[i] == 0):
                # tarjan1(i);
                Code01_2SAT1.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code01_2SAT1.n):
            try:
                if (Code01_2SAT1.belong[i] == Code01_2SAT1.belong[jcast('int', jadd(i, Code01_2SAT1.n))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
            except JBreak as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if check:
            jcall(out, 'println', 'POSSIBLE')
            i = jcast('int', 1)
            while (i <= Code01_2SAT1.n):
                if (Code01_2SAT1.belong[i] < Code01_2SAT1.belong[jcast('int', jadd(i, Code01_2SAT1.n))]):
                    jcall(out, 'print', '1 ')
                else:
                    jcall(out, 'print', '0 ')
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', 'IMPOSSIBLE')
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
            return jcast('int', self.buffer[((_java_obj_23 := self), (_java_key_24 := 'ptr'), (_java_old_25 := jget(_java_obj_23, _java_key_24)), jset(_java_obj_23, _java_key_24, jcast('int', (_java_old_25 + (1)))), _java_old_25)[4]])

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
            raise TypeError("No matching overload for Code01_2SAT1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_2SAT1.MAXN = jcast('int', 2000001)
Code01_2SAT1.n = jcast('int', 0)
Code01_2SAT1.m = jcast('int', 0)
Code01_2SAT1.head = jarray('int', [Code01_2SAT1.MAXN])
Code01_2SAT1.nxt = jarray('int', [Code01_2SAT1.MAXN])
Code01_2SAT1.to = jarray('int', [Code01_2SAT1.MAXN])
Code01_2SAT1.cntg = jcast('int', 0)
Code01_2SAT1.dfn = jarray('int', [Code01_2SAT1.MAXN])
Code01_2SAT1.low = jarray('int', [Code01_2SAT1.MAXN])
Code01_2SAT1.cntd = jcast('int', 0)
Code01_2SAT1.sta = jarray('int', [Code01_2SAT1.MAXN])
Code01_2SAT1.top = jcast('int', 0)
Code01_2SAT1.belong = jarray('int', [Code01_2SAT1.MAXN])
Code01_2SAT1.sccCnt = jcast('int', 0)
Code01_2SAT1.stack = jarray('int', [Code01_2SAT1.MAXN, 3])
Code01_2SAT1.u = jcast('int', 0)
Code01_2SAT1.status = jcast('int', 0)
Code01_2SAT1.e = jcast('int', 0)
Code01_2SAT1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code01_2SAT1.main([])
