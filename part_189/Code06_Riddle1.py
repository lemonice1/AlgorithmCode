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

# 谜语，Python版
# 无向图中有n个点、m条边，一共有k个阵营，每个阵营拥有一些点
# 给定每个阵营拥有的节点列表，每个点都会进入且只进一个阵营
# 选择一些点成为关键点，要求每个阵营必须有一个点成为关键点
# 同时要求每条边的两个端点中，至少有一个端点成为关键点
# 如果存在选择方案，打印"TAK"，否则打印"NIE"
# 1 <= n、m、k <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P6378
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Riddle1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'k': 'k', 'w': 'w', 'cntt': 'cntt', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    k = 0
    w = 0
    cntt = 0
    arr = None
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
        jset(Code06_Riddle1.stack[Code06_Riddle1.stacksize], 0, u)
        jset(Code06_Riddle1.stack[Code06_Riddle1.stacksize], 1, status)
        jset(Code06_Riddle1.stack[Code06_Riddle1.stacksize], 2, e)
        Code06_Riddle1.stacksize = jcast('int', (Code06_Riddle1.stacksize + 1))

    @staticmethod
    def pop():
        Code06_Riddle1.stacksize = jcast('int', (Code06_Riddle1.stacksize - 1))
        Code06_Riddle1.u = jcast('int', Code06_Riddle1.stack[Code06_Riddle1.stacksize][0])
        Code06_Riddle1.status = jcast('int', Code06_Riddle1.stack[Code06_Riddle1.stacksize][1])
        Code06_Riddle1.e = jcast('int', Code06_Riddle1.stack[Code06_Riddle1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_Riddle1.nxt, ((_java_obj_1 := Code06_Riddle1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_Riddle1.head[u])
        Code06_Riddle1.to[Code06_Riddle1.cntg] = jcast('int', v)
        Code06_Riddle1.head[u] = jcast('int', Code06_Riddle1.cntg)

    # 前后缀优化建图
    @staticmethod
    def link():
        Code06_Riddle1.cntt = jcast('int', (Code06_Riddle1.cntt + 1))
        Code06_Riddle1.addEdge(Code06_Riddle1.cntt, jcast('int', jadd(Code06_Riddle1.arr[1], Code06_Riddle1.n)))
        i = jcast('int', 2)
        while (i <= Code06_Riddle1.w):
            Code06_Riddle1.cntt = jcast('int', (Code06_Riddle1.cntt + 1))
            Code06_Riddle1.addEdge(Code06_Riddle1.cntt, jcast('int', jadd(Code06_Riddle1.arr[i], Code06_Riddle1.n)))
            Code06_Riddle1.addEdge(Code06_Riddle1.arr[i], jcast('int', (Code06_Riddle1.cntt - 1)))
            Code06_Riddle1.addEdge(Code06_Riddle1.cntt, jcast('int', (Code06_Riddle1.cntt - 1)))
            i = jcast('int', (i + 1))
        Code06_Riddle1.cntt = jcast('int', (Code06_Riddle1.cntt + 1))
        Code06_Riddle1.addEdge(Code06_Riddle1.cntt, jcast('int', jadd(Code06_Riddle1.arr[Code06_Riddle1.w], Code06_Riddle1.n)))
        i = jcast('int', jcast('int', (Code06_Riddle1.w - 1)))
        while (i >= 1):
            Code06_Riddle1.cntt = jcast('int', (Code06_Riddle1.cntt + 1))
            Code06_Riddle1.addEdge(Code06_Riddle1.cntt, jcast('int', jadd(Code06_Riddle1.arr[i], Code06_Riddle1.n)))
            Code06_Riddle1.addEdge(Code06_Riddle1.arr[i], jcast('int', (Code06_Riddle1.cntt - 1)))
            Code06_Riddle1.addEdge(Code06_Riddle1.cntt, jcast('int', (Code06_Riddle1.cntt - 1)))
            i = jcast('int', (i - 1))

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code06_Riddle1.dfn, u, jset(Code06_Riddle1.low, u, ((_java_obj_4 := Code06_Riddle1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code06_Riddle1.sta, ((_java_obj_7 := Code06_Riddle1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code06_Riddle1.head[u])
        while (e > 0):
            v = jcast('int', Code06_Riddle1.to[e])
            if (Code06_Riddle1.dfn[v] == 0):
                Code06_Riddle1.tarjan1(v)
                jset(Code06_Riddle1.low, u, jstatic('Math', 'min', Code06_Riddle1.low[u], Code06_Riddle1.low[v]))
            else:
                if (Code06_Riddle1.belong[v] == 0):
                    jset(Code06_Riddle1.low, u, jstatic('Math', 'min', Code06_Riddle1.low[u], Code06_Riddle1.dfn[v]))
            e = jcast('int', Code06_Riddle1.nxt[e])
        if (Code06_Riddle1.dfn[u] == Code06_Riddle1.low[u]):
            Code06_Riddle1.sccCnt = jcast('int', (Code06_Riddle1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code06_Riddle1.sta[((_java_obj_10 := Code06_Riddle1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code06_Riddle1.belong[pop] = jcast('int', Code06_Riddle1.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code06_Riddle1.stacksize = jcast('int', 0)
        Code06_Riddle1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code06_Riddle1.stacksize > 0):
            Code06_Riddle1.pop()
            if (Code06_Riddle1.status == jcast('int', (-1))):
                jset(Code06_Riddle1.dfn, Code06_Riddle1.u, jset(Code06_Riddle1.low, Code06_Riddle1.u, ((_java_obj_13 := Code06_Riddle1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code06_Riddle1.sta, ((_java_obj_16 := Code06_Riddle1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code06_Riddle1.u)
                Code06_Riddle1.e = jcast('int', Code06_Riddle1.head[Code06_Riddle1.u])
            else:
                v = jcast('int', Code06_Riddle1.to[Code06_Riddle1.e])
                if (Code06_Riddle1.status == 0):
                    jset(Code06_Riddle1.low, Code06_Riddle1.u, jstatic('Math', 'min', Code06_Riddle1.low[Code06_Riddle1.u], Code06_Riddle1.low[v]))
                if ((Code06_Riddle1.status == 1) and (Code06_Riddle1.belong[v] == 0)):
                    jset(Code06_Riddle1.low, Code06_Riddle1.u, jstatic('Math', 'min', Code06_Riddle1.low[Code06_Riddle1.u], Code06_Riddle1.dfn[v]))
                Code06_Riddle1.e = jcast('int', Code06_Riddle1.nxt[Code06_Riddle1.e])
            if (Code06_Riddle1.e != 0):
                v = jcast('int', Code06_Riddle1.to[Code06_Riddle1.e])
                if (Code06_Riddle1.dfn[v] == 0):
                    Code06_Riddle1.push(Code06_Riddle1.u, 0, Code06_Riddle1.e)
                    Code06_Riddle1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code06_Riddle1.push(Code06_Riddle1.u, 1, Code06_Riddle1.e)
            else:
                if (Code06_Riddle1.dfn[Code06_Riddle1.u] == Code06_Riddle1.low[Code06_Riddle1.u]):
                    Code06_Riddle1.sccCnt = jcast('int', (Code06_Riddle1.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code06_Riddle1.sta[((_java_obj_19 := Code06_Riddle1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code06_Riddle1.belong[pop] = jcast('int', Code06_Riddle1.sccCnt)
                        if not ((pop != Code06_Riddle1.u)):
                            break

    @staticmethod
    def main(args):
        in_ = Code06_Riddle1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Riddle1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_Riddle1.m = jcast('int', jcall(in_, 'nextInt'))
        Code06_Riddle1.k = jcast('int', jcall(in_, 'nextInt'))
        Code06_Riddle1.cntt = jcast('int', jcast('int', (Code06_Riddle1.n << (1 & 31))))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code06_Riddle1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code06_Riddle1.addEdge(jcast('int', jadd(u, Code06_Riddle1.n)), v)
            Code06_Riddle1.addEdge(jcast('int', jadd(v, Code06_Riddle1.n)), u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_Riddle1.k):
            Code06_Riddle1.w = jcast('int', jcall(in_, 'nextInt'))
            j = jcast('int', 1)
            while (j <= Code06_Riddle1.w):
                jset(Code06_Riddle1.arr, j, jcall(in_, 'nextInt'))
                j = jcast('int', (j + 1))
            Code06_Riddle1.link()
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_Riddle1.cntt):
            if (Code06_Riddle1.dfn[i] == 0):
                # tarjan1(i);
                Code06_Riddle1.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code06_Riddle1.n):
            try:
                if (Code06_Riddle1.belong[i] == Code06_Riddle1.belong[jcast('int', jadd(i, Code06_Riddle1.n))]):
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
        jcall(out, 'println', ('TAK' if check else 'NIE'))
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
            raise TypeError("No matching overload for Code06_Riddle1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Riddle1.MAXN = jcast('int', 5000001)
Code06_Riddle1.MAXM = jcast('int', 10000001)
Code06_Riddle1.n = jcast('int', 0)
Code06_Riddle1.m = jcast('int', 0)
Code06_Riddle1.k = jcast('int', 0)
Code06_Riddle1.w = jcast('int', 0)
Code06_Riddle1.cntt = jcast('int', 0)
Code06_Riddle1.arr = jarray('int', [Code06_Riddle1.MAXN])
Code06_Riddle1.head = jarray('int', [Code06_Riddle1.MAXN])
Code06_Riddle1.nxt = jarray('int', [Code06_Riddle1.MAXM])
Code06_Riddle1.to = jarray('int', [Code06_Riddle1.MAXM])
Code06_Riddle1.cntg = jcast('int', 0)
Code06_Riddle1.dfn = jarray('int', [Code06_Riddle1.MAXN])
Code06_Riddle1.low = jarray('int', [Code06_Riddle1.MAXN])
Code06_Riddle1.cntd = jcast('int', 0)
Code06_Riddle1.sta = jarray('int', [Code06_Riddle1.MAXN])
Code06_Riddle1.top = jcast('int', 0)
Code06_Riddle1.belong = jarray('int', [Code06_Riddle1.MAXN])
Code06_Riddle1.sccCnt = jcast('int', 0)
Code06_Riddle1.stack = jarray('int', [Code06_Riddle1.MAXN, 3])
Code06_Riddle1.u = jcast('int', 0)
Code06_Riddle1.status = jcast('int', 0)
Code06_Riddle1.e = jcast('int', 0)
Code06_Riddle1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code06_Riddle1.main([])
