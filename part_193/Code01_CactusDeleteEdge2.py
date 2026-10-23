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

# 仙人掌删边方案数，Python版
# 给定n个点、m条路径表示无向图，每条路径的相邻两点之间都有边
# 如果图不是仙人掌打印0，如果图是仙人掌，可以在图中删除一些边
# 如果删除后剩下的图仍然连通，就叫有效的删边方案
# 允许一条边也不删，打印有效删边的方案数，答案可能很大，需要高精度
# 1 <= n <= 2 * 10^4
# 1 <= 边总数 <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P4129
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_CactusDeleteEdge2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'edgeCnt': 'edgeCnt', 'cntc': 'cntc', 'cycleCnt': 'cycleCnt', 'ans': 'ans', 'stau': 'stau', 'stap': 'stap', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'e': 'e', 'stacksiz': 'stacksiz'}
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
    # 统计每个环的边数
    edgeCnt = None
    cntc = 0
    # 不作为环顶节点的情况下，参与了几个环
    cycleCnt = None
    # 本题需要高精度乘法
    ans = None
    # 递归改迭代需要的栈
    stau = None
    stap = None
    stas = None
    stae = None
    u = 0
    preEdge = 0
    status = 0
    e = 0
    stacksiz = 0
    @staticmethod
    def push(u, preEdge, status, e):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        status = jcast('int', status)
        e = jcast('int', e)
        Code01_CactusDeleteEdge2.stau[Code01_CactusDeleteEdge2.stacksiz] = jcast('int', u)
        Code01_CactusDeleteEdge2.stap[Code01_CactusDeleteEdge2.stacksiz] = jcast('int', preEdge)
        Code01_CactusDeleteEdge2.stas[Code01_CactusDeleteEdge2.stacksiz] = jcast('int', status)
        Code01_CactusDeleteEdge2.stae[Code01_CactusDeleteEdge2.stacksiz] = jcast('int', e)
        Code01_CactusDeleteEdge2.stacksiz = jcast('int', (Code01_CactusDeleteEdge2.stacksiz + 1))

    @staticmethod
    def pop():
        Code01_CactusDeleteEdge2.stacksiz = jcast('int', (Code01_CactusDeleteEdge2.stacksiz - 1))
        Code01_CactusDeleteEdge2.u = jcast('int', Code01_CactusDeleteEdge2.stau[Code01_CactusDeleteEdge2.stacksiz])
        Code01_CactusDeleteEdge2.preEdge = jcast('int', Code01_CactusDeleteEdge2.stap[Code01_CactusDeleteEdge2.stacksiz])
        Code01_CactusDeleteEdge2.status = jcast('int', Code01_CactusDeleteEdge2.stas[Code01_CactusDeleteEdge2.stacksiz])
        Code01_CactusDeleteEdge2.e = jcast('int', Code01_CactusDeleteEdge2.stae[Code01_CactusDeleteEdge2.stacksiz])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_CactusDeleteEdge2.nxt, ((_java_obj_1 := Code01_CactusDeleteEdge2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_CactusDeleteEdge2.head[u])
        Code01_CactusDeleteEdge2.to[Code01_CactusDeleteEdge2.cntg] = jcast('int', v)
        Code01_CactusDeleteEdge2.head[u] = jcast('int', Code01_CactusDeleteEdge2.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code01_CactusDeleteEdge2.dfn, u, jset(Code01_CactusDeleteEdge2.low, u, ((_java_obj_4 := Code01_CactusDeleteEdge2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code01_CactusDeleteEdge2.sta, ((_java_obj_7 := Code01_CactusDeleteEdge2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code01_CactusDeleteEdge2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code01_CactusDeleteEdge2.to[e])
                if (Code01_CactusDeleteEdge2.dfn[v] == 0):
                    Code01_CactusDeleteEdge2.tarjan1(v, e)
                    if (Code01_CactusDeleteEdge2.low[v] < Code01_CactusDeleteEdge2.dfn[u]):
                        jset(Code01_CactusDeleteEdge2.low, u, jstatic('Math', 'min', Code01_CactusDeleteEdge2.low[u], Code01_CactusDeleteEdge2.low[v]))
                        Code01_CactusDeleteEdge2.cycleCnt[u] = jcast('int', (Code01_CactusDeleteEdge2.cycleCnt[u] + 1))
                    else:
                        if (Code01_CactusDeleteEdge2.low[v] > Code01_CactusDeleteEdge2.dfn[u]):
                            Code01_CactusDeleteEdge2.top = jcast('int', (Code01_CactusDeleteEdge2.top - 1))
                        else:
                            Code01_CactusDeleteEdge2.cntc = jcast('int', (Code01_CactusDeleteEdge2.cntc + 1))
                            Code01_CactusDeleteEdge2.edgeCnt[Code01_CactusDeleteEdge2.cntc] = jcast('int', 1)
                            pop = 0
                            while True:
                                pop = jcast('int', Code01_CactusDeleteEdge2.sta[((_java_obj_11 := Code01_CactusDeleteEdge2), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                                Code01_CactusDeleteEdge2.edgeCnt[Code01_CactusDeleteEdge2.cntc] = jcast('int', (Code01_CactusDeleteEdge2.edgeCnt[Code01_CactusDeleteEdge2.cntc] + 1))
                                if not ((pop != v)):
                                    break
                else:
                    if (Code01_CactusDeleteEdge2.dfn[v] < Code01_CactusDeleteEdge2.dfn[u]):
                        jset(Code01_CactusDeleteEdge2.low, u, jstatic('Math', 'min', Code01_CactusDeleteEdge2.low[u], Code01_CactusDeleteEdge2.dfn[v]))
                        Code01_CactusDeleteEdge2.cycleCnt[u] = jcast('int', (Code01_CactusDeleteEdge2.cycleCnt[u] + 1))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code01_CactusDeleteEdge2.nxt[e])

    # 迭代版
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code01_CactusDeleteEdge2.stacksiz = jcast('int', 0)
        Code01_CactusDeleteEdge2.push(node, pree, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code01_CactusDeleteEdge2.stacksiz > 0):
            Code01_CactusDeleteEdge2.pop()
            if (Code01_CactusDeleteEdge2.status == jcast('int', (-1))):
                jset(Code01_CactusDeleteEdge2.dfn, Code01_CactusDeleteEdge2.u, jset(Code01_CactusDeleteEdge2.low, Code01_CactusDeleteEdge2.u, ((_java_obj_14 := Code01_CactusDeleteEdge2), (_java_key_15 := 'cntd'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3]))
                jset(Code01_CactusDeleteEdge2.sta, ((_java_obj_17 := Code01_CactusDeleteEdge2), (_java_key_18 := 'top'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))))[3], Code01_CactusDeleteEdge2.u)
                Code01_CactusDeleteEdge2.e = jcast('int', Code01_CactusDeleteEdge2.head[Code01_CactusDeleteEdge2.u])
            else:
                v = jcast('int', Code01_CactusDeleteEdge2.to[Code01_CactusDeleteEdge2.e])
                if (Code01_CactusDeleteEdge2.status == 0):
                    if (Code01_CactusDeleteEdge2.low[v] < Code01_CactusDeleteEdge2.dfn[Code01_CactusDeleteEdge2.u]):
                        jset(Code01_CactusDeleteEdge2.low, Code01_CactusDeleteEdge2.u, jstatic('Math', 'min', Code01_CactusDeleteEdge2.low[Code01_CactusDeleteEdge2.u], Code01_CactusDeleteEdge2.low[v]))
                        Code01_CactusDeleteEdge2.cycleCnt[Code01_CactusDeleteEdge2.u] = jcast('int', (Code01_CactusDeleteEdge2.cycleCnt[Code01_CactusDeleteEdge2.u] + 1))
                    else:
                        if (Code01_CactusDeleteEdge2.low[v] > Code01_CactusDeleteEdge2.dfn[Code01_CactusDeleteEdge2.u]):
                            Code01_CactusDeleteEdge2.top = jcast('int', (Code01_CactusDeleteEdge2.top - 1))
                        else:
                            Code01_CactusDeleteEdge2.cntc = jcast('int', (Code01_CactusDeleteEdge2.cntc + 1))
                            Code01_CactusDeleteEdge2.edgeCnt[Code01_CactusDeleteEdge2.cntc] = jcast('int', 1)
                            pop = 0
                            while True:
                                pop = jcast('int', Code01_CactusDeleteEdge2.sta[((_java_obj_20 := Code01_CactusDeleteEdge2), (_java_key_21 := 'top'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (-1)))), _java_old_22)[4]])
                                Code01_CactusDeleteEdge2.edgeCnt[Code01_CactusDeleteEdge2.cntc] = jcast('int', (Code01_CactusDeleteEdge2.edgeCnt[Code01_CactusDeleteEdge2.cntc] + 1))
                                if not ((pop != v)):
                                    break
                else:
                    if (Code01_CactusDeleteEdge2.dfn[v] < Code01_CactusDeleteEdge2.dfn[Code01_CactusDeleteEdge2.u]):
                        jset(Code01_CactusDeleteEdge2.low, Code01_CactusDeleteEdge2.u, jstatic('Math', 'min', Code01_CactusDeleteEdge2.low[Code01_CactusDeleteEdge2.u], Code01_CactusDeleteEdge2.dfn[v]))
                        Code01_CactusDeleteEdge2.cycleCnt[Code01_CactusDeleteEdge2.u] = jcast('int', (Code01_CactusDeleteEdge2.cycleCnt[Code01_CactusDeleteEdge2.u] + 1))
                Code01_CactusDeleteEdge2.e = jcast('int', Code01_CactusDeleteEdge2.nxt[Code01_CactusDeleteEdge2.e])
            if (jcast('int', (Code01_CactusDeleteEdge2.e ^ 1)) == Code01_CactusDeleteEdge2.preEdge):
                Code01_CactusDeleteEdge2.e = jcast('int', Code01_CactusDeleteEdge2.nxt[Code01_CactusDeleteEdge2.e])
            if (Code01_CactusDeleteEdge2.e != 0):
                v = jcast('int', Code01_CactusDeleteEdge2.to[Code01_CactusDeleteEdge2.e])
                if (Code01_CactusDeleteEdge2.dfn[v] == 0):
                    Code01_CactusDeleteEdge2.push(Code01_CactusDeleteEdge2.u, Code01_CactusDeleteEdge2.preEdge, 0, Code01_CactusDeleteEdge2.e)
                    Code01_CactusDeleteEdge2.push(v, Code01_CactusDeleteEdge2.e, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code01_CactusDeleteEdge2.push(Code01_CactusDeleteEdge2.u, Code01_CactusDeleteEdge2.preEdge, 1, Code01_CactusDeleteEdge2.e)

    @staticmethod
    def main(args):
        in_ = Code01_CactusDeleteEdge2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_CactusDeleteEdge2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_CactusDeleteEdge2.m = jcast('int', jcall(in_, 'nextInt'))
        Code01_CactusDeleteEdge2.cntg = jcast('int', 1)
        i = jcast('int', 1)
        k = 0
        x = 0
        y = 0
        while (i <= Code01_CactusDeleteEdge2.m):
            k = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            j = jcast('int', 2)
            while (j <= k):
                y = jcast('int', jcall(in_, 'nextInt'))
                Code01_CactusDeleteEdge2.addEdge(x, y)
                Code01_CactusDeleteEdge2.addEdge(y, x)
                x = jcast('int', y)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        # tarjan1(1, 0);
        Code01_CactusDeleteEdge2.tarjan2(1, 0)
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code01_CactusDeleteEdge2.n):
            try:
                if ((Code01_CactusDeleteEdge2.dfn[i] == 0) or (Code01_CactusDeleteEdge2.cycleCnt[i] >= 2)):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_23:
                if _java_control_23.label not in (None,):
                    raise
            except JBreak as _java_control_23:
                if _java_control_23.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if check:
            Code01_CactusDeleteEdge2.ans = jget(BigInteger, 'ONE')
            i = jcast('int', 1)
            while (i <= Code01_CactusDeleteEdge2.cntc):
                Code01_CactusDeleteEdge2.ans = jcall(Code01_CactusDeleteEdge2.ans, 'multiply', jstatic('BigInteger', 'valueOf', jcast('int', jadd(Code01_CactusDeleteEdge2.edgeCnt[i], 1))))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code01_CactusDeleteEdge2.ans)
        else:
            jcall(out, 'println', 0)
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
            return jcast('int', self.buffer[((_java_obj_24 := self), (_java_key_25 := 'ptr'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))), _java_old_26)[4]])

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
            raise TypeError("No matching overload for Code01_CactusDeleteEdge2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CactusDeleteEdge2.MAXN = jcast('int', 20001)
Code01_CactusDeleteEdge2.MAXM = jcast('int', 1000001)
Code01_CactusDeleteEdge2.n = jcast('int', 0)
Code01_CactusDeleteEdge2.m = jcast('int', 0)
Code01_CactusDeleteEdge2.head = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.nxt = jarray('int', [jcast('int', (Code01_CactusDeleteEdge2.MAXM << (1 & 31)))])
Code01_CactusDeleteEdge2.to = jarray('int', [jcast('int', (Code01_CactusDeleteEdge2.MAXM << (1 & 31)))])
Code01_CactusDeleteEdge2.cntg = jcast('int', 0)
Code01_CactusDeleteEdge2.dfn = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.low = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.cntd = jcast('int', 0)
Code01_CactusDeleteEdge2.sta = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.top = jcast('int', 0)
Code01_CactusDeleteEdge2.edgeCnt = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.cntc = jcast('int', 0)
Code01_CactusDeleteEdge2.cycleCnt = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.ans = None
Code01_CactusDeleteEdge2.stau = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.stap = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.stas = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.stae = jarray('int', [Code01_CactusDeleteEdge2.MAXN])
Code01_CactusDeleteEdge2.u = jcast('int', 0)
Code01_CactusDeleteEdge2.preEdge = jcast('int', 0)
Code01_CactusDeleteEdge2.status = jcast('int', 0)
Code01_CactusDeleteEdge2.e = jcast('int', 0)
Code01_CactusDeleteEdge2.stacksiz = jcast('int', 0)

if __name__ == '__main__':
    Code01_CactusDeleteEdge2.main([])
