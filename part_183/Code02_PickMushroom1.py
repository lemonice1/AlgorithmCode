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

# 采蘑菇，Python版
# 给定一张n个点，m条边的有向图，每条边有初始收益、恢复系数两种边权
# 初始收益为非负整数，恢复系数范围[0, 0.8]，并且最多有一位小数
# 比如，如果重复走过一条边，该边的初始收益为10，恢复系数为0.6
# 那么依次获得的收益为，10、6、3、1、0，随后重复经过就没有收益了
# 给定起点s，找到一条必须从s出发的路径，打印收益累加和的最大值
# 1 <= n <= 8 * 10^4
# 1 <= m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2656
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_PickMushroom1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 's': 's', 'a': 'a', 'b': 'b', 'init': 'init', 'recover': 'recover', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'sum': 'sum', 'dp': 'dp', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    m = 0
    s = 0
    a = None
    b = None
    init = None
    recover = None
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    sum = None
    dp = None
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
        jset(Code02_PickMushroom1.stack[Code02_PickMushroom1.stacksize], 0, u)
        jset(Code02_PickMushroom1.stack[Code02_PickMushroom1.stacksize], 1, status)
        jset(Code02_PickMushroom1.stack[Code02_PickMushroom1.stacksize], 2, e)
        Code02_PickMushroom1.stacksize = jcast('int', (Code02_PickMushroom1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_PickMushroom1.stacksize = jcast('int', (Code02_PickMushroom1.stacksize - 1))
        Code02_PickMushroom1.u = jcast('int', Code02_PickMushroom1.stack[Code02_PickMushroom1.stacksize][0])
        Code02_PickMushroom1.status = jcast('int', Code02_PickMushroom1.stack[Code02_PickMushroom1.stacksize][1])
        Code02_PickMushroom1.e = jcast('int', Code02_PickMushroom1.stack[Code02_PickMushroom1.stacksize][2])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code02_PickMushroom1.nxt, ((_java_obj_1 := Code02_PickMushroom1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_PickMushroom1.head[u])
        Code02_PickMushroom1.to[Code02_PickMushroom1.cntg] = jcast('int', v)
        Code02_PickMushroom1.weight[Code02_PickMushroom1.cntg] = jcast('int', w)
        Code02_PickMushroom1.head[u] = jcast('int', Code02_PickMushroom1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code02_PickMushroom1.dfn, u, jset(Code02_PickMushroom1.low, u, ((_java_obj_4 := Code02_PickMushroom1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code02_PickMushroom1.sta, ((_java_obj_7 := Code02_PickMushroom1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code02_PickMushroom1.head[u])
        while (e > 0):
            v = jcast('int', Code02_PickMushroom1.to[e])
            if (Code02_PickMushroom1.dfn[v] == 0):
                Code02_PickMushroom1.tarjan1(v)
                jset(Code02_PickMushroom1.low, u, jstatic('Math', 'min', Code02_PickMushroom1.low[u], Code02_PickMushroom1.low[v]))
            else:
                if (Code02_PickMushroom1.belong[v] == 0):
                    jset(Code02_PickMushroom1.low, u, jstatic('Math', 'min', Code02_PickMushroom1.low[u], Code02_PickMushroom1.dfn[v]))
            e = jcast('int', Code02_PickMushroom1.nxt[e])
        if (Code02_PickMushroom1.dfn[u] == Code02_PickMushroom1.low[u]):
            Code02_PickMushroom1.sccCnt = jcast('int', (Code02_PickMushroom1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code02_PickMushroom1.sta[((_java_obj_10 := Code02_PickMushroom1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code02_PickMushroom1.belong[pop] = jcast('int', Code02_PickMushroom1.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code02_PickMushroom1.stacksize = jcast('int', 0)
        Code02_PickMushroom1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code02_PickMushroom1.stacksize > 0):
            Code02_PickMushroom1.pop()
            if (Code02_PickMushroom1.status == jcast('int', (-1))):
                jset(Code02_PickMushroom1.dfn, Code02_PickMushroom1.u, jset(Code02_PickMushroom1.low, Code02_PickMushroom1.u, ((_java_obj_13 := Code02_PickMushroom1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code02_PickMushroom1.sta, ((_java_obj_16 := Code02_PickMushroom1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code02_PickMushroom1.u)
                Code02_PickMushroom1.e = jcast('int', Code02_PickMushroom1.head[Code02_PickMushroom1.u])
            else:
                v = jcast('int', Code02_PickMushroom1.to[Code02_PickMushroom1.e])
                if (Code02_PickMushroom1.status == 0):
                    jset(Code02_PickMushroom1.low, Code02_PickMushroom1.u, jstatic('Math', 'min', Code02_PickMushroom1.low[Code02_PickMushroom1.u], Code02_PickMushroom1.low[v]))
                if ((Code02_PickMushroom1.status == 1) and (Code02_PickMushroom1.belong[v] == 0)):
                    jset(Code02_PickMushroom1.low, Code02_PickMushroom1.u, jstatic('Math', 'min', Code02_PickMushroom1.low[Code02_PickMushroom1.u], Code02_PickMushroom1.dfn[v]))
                Code02_PickMushroom1.e = jcast('int', Code02_PickMushroom1.nxt[Code02_PickMushroom1.e])
            if (Code02_PickMushroom1.e != 0):
                v = jcast('int', Code02_PickMushroom1.to[Code02_PickMushroom1.e])
                if (Code02_PickMushroom1.dfn[v] == 0):
                    Code02_PickMushroom1.push(Code02_PickMushroom1.u, 0, Code02_PickMushroom1.e)
                    Code02_PickMushroom1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code02_PickMushroom1.push(Code02_PickMushroom1.u, 1, Code02_PickMushroom1.e)
            else:
                if (Code02_PickMushroom1.dfn[Code02_PickMushroom1.u] == Code02_PickMushroom1.low[Code02_PickMushroom1.u]):
                    Code02_PickMushroom1.sccCnt = jcast('int', (Code02_PickMushroom1.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code02_PickMushroom1.sta[((_java_obj_19 := Code02_PickMushroom1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code02_PickMushroom1.belong[pop] = jcast('int', Code02_PickMushroom1.sccCnt)
                        if not ((pop != Code02_PickMushroom1.u)):
                            break

    @staticmethod
    def condense():
        Code02_PickMushroom1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_PickMushroom1.sccCnt):
            Code02_PickMushroom1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_PickMushroom1.m):
            scc1 = jcast('int', Code02_PickMushroom1.belong[Code02_PickMushroom1.a[i]])
            scc2 = jcast('int', Code02_PickMushroom1.belong[Code02_PickMushroom1.b[i]])
            if ((scc1 > 0) and (scc2 > 0)):
                val = jcast('int', Code02_PickMushroom1.init[i])
                rec = jcast('int', Code02_PickMushroom1.recover[i])
                if (scc1 == scc2):
                    while (val > 0):
                        Code02_PickMushroom1.sum[scc1] = jcast('int', jcast('int', jadd(Code02_PickMushroom1.sum[scc1], val)))
                        val = jcast('int', jcast('int', jdiv(jcast('int', (val * rec)), 10)))
                else:
                    Code02_PickMushroom1.addEdge(scc1, scc2, val)
            i = jcast('int', (i + 1))

    @staticmethod
    def dpOnDAG():
        u = jcast('int', 1)
        while (u <= Code02_PickMushroom1.sccCnt):
            Code02_PickMushroom1.dp[u] = jcast('int', jcast('int', (-Code02_PickMushroom1.INF)))
            u = jcast('int', (u + 1))
        jset(Code02_PickMushroom1.dp, Code02_PickMushroom1.belong[Code02_PickMushroom1.s], Code02_PickMushroom1.sum[Code02_PickMushroom1.belong[Code02_PickMushroom1.s]])
        u = jcast('int', Code02_PickMushroom1.sccCnt)
        while (u > 0):
            e = jcast('int', Code02_PickMushroom1.head[u])
            while (e > 0):
                v = jcast('int', Code02_PickMushroom1.to[e])
                w = jcast('int', Code02_PickMushroom1.weight[e])
                jset(Code02_PickMushroom1.dp, v, jstatic('Math', 'max', Code02_PickMushroom1.dp[v], jcast('int', jadd(jcast('int', jadd(Code02_PickMushroom1.dp[u], w)), Code02_PickMushroom1.sum[v]))))
                e = jcast('int', Code02_PickMushroom1.nxt[e])
            u = jcast('int', (u - 1))
        ans = jcast('int', 0)
        u = jcast('int', 1)
        while (u <= Code02_PickMushroom1.sccCnt):
            ans = jcast('int', jstatic('Math', 'max', ans, Code02_PickMushroom1.dp[u]))
            u = jcast('int', (u + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code02_PickMushroom1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_PickMushroom1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_PickMushroom1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_PickMushroom1.m):
            jset(Code02_PickMushroom1.a, i, jcall(in_, 'nextInt'))
            jset(Code02_PickMushroom1.b, i, jcall(in_, 'nextInt'))
            jset(Code02_PickMushroom1.init, i, jcall(in_, 'nextInt'))
            rec = jcast('double', jcall(in_, 'nextDouble'))
            Code02_PickMushroom1.recover[i] = jcast('int', jcast('int', (rec * 10)))
            Code02_PickMushroom1.addEdge(Code02_PickMushroom1.a[i], Code02_PickMushroom1.b[i], 0)
            i = jcast('int', (i + 1))
        Code02_PickMushroom1.s = jcast('int', jcall(in_, 'nextInt'))
        # tarjan1(s);
        Code02_PickMushroom1.tarjan2(Code02_PickMushroom1.s)
        Code02_PickMushroom1.condense()
        ans = jcast('int', Code02_PickMushroom1.dpOnDAG())
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

        def nextDouble(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            intPart = jcast('long', 0)
            while (((c > jchar(' ')) and (c != jcast('int', (-1)))) and (c != jchar('.'))):
                intPart = jcast('long', jcast('long', jadd(jcast('long', (intPart * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            val = jcast('double', jcast('double', intPart))
            if (c == jchar('.')):
                c = jcast('int', self.readByte())
                base = jcast('double', 0.1)
                while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                    val = jcast('double', jadd(val, (jcast('int', (c - jchar('0'))) * base)))
                    base = jcast('double', (base * 0.1))
                    c = jcast('int', self.readByte())
            return jcast('double', ((-val) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_PickMushroom1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_PickMushroom1.MAXN = jcast('int', 80001)
Code02_PickMushroom1.MAXM = jcast('int', 200001)
Code02_PickMushroom1.INF = jcast('int', 1000000001)
Code02_PickMushroom1.n = jcast('int', 0)
Code02_PickMushroom1.m = jcast('int', 0)
Code02_PickMushroom1.s = jcast('int', 0)
Code02_PickMushroom1.a = jarray('int', [Code02_PickMushroom1.MAXM])
Code02_PickMushroom1.b = jarray('int', [Code02_PickMushroom1.MAXM])
Code02_PickMushroom1.init = jarray('int', [Code02_PickMushroom1.MAXM])
Code02_PickMushroom1.recover = jarray('int', [Code02_PickMushroom1.MAXM])
Code02_PickMushroom1.head = jarray('int', [Code02_PickMushroom1.MAXN])
Code02_PickMushroom1.nxt = jarray('int', [Code02_PickMushroom1.MAXM])
Code02_PickMushroom1.to = jarray('int', [Code02_PickMushroom1.MAXM])
Code02_PickMushroom1.weight = jarray('int', [Code02_PickMushroom1.MAXM])
Code02_PickMushroom1.cntg = jcast('int', 0)
Code02_PickMushroom1.dfn = jarray('int', [Code02_PickMushroom1.MAXN])
Code02_PickMushroom1.low = jarray('int', [Code02_PickMushroom1.MAXN])
Code02_PickMushroom1.cntd = jcast('int', 0)
Code02_PickMushroom1.sta = jarray('int', [Code02_PickMushroom1.MAXN])
Code02_PickMushroom1.top = jcast('int', 0)
Code02_PickMushroom1.belong = jarray('int', [Code02_PickMushroom1.MAXN])
Code02_PickMushroom1.sccCnt = jcast('int', 0)
Code02_PickMushroom1.sum = jarray('int', [Code02_PickMushroom1.MAXN])
Code02_PickMushroom1.dp = jarray('int', [Code02_PickMushroom1.MAXN])
Code02_PickMushroom1.stack = jarray('int', [Code02_PickMushroom1.MAXN, 3])
Code02_PickMushroom1.u = jcast('int', 0)
Code02_PickMushroom1.status = jcast('int', 0)
Code02_PickMushroom1.e = jcast('int', 0)
Code02_PickMushroom1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code02_PickMushroom1.main([])
