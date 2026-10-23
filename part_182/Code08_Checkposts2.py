# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 检查站，Python版
# 给定一张n个点，m条边的有向图，每个点有点权
# 一个强连通分量内部，选点权最小的点，就能控制该连通分量里的所有点
# 你的目的是选择若干点之后，图上所有的点都能控制，打印最小点权和
# 打印选择点的方案数，方案数可能较大，对 1000000007 取余
# 1 <= n <= 10^5
# 1 <= m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF427C
# 测试链接 : https://codeforces.com/problemset/problem/427/C
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_Checkposts2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MOD': 'MOD', 'n': 'n', 'm': 'm', 'val': 'val', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'minVal': 'minVal', 'minCnt': 'minCnt', 'sccCnt': 'sccCnt'}
    MAXN = 0
    MAXM = 0
    MOD = 0
    n = 0
    m = 0
    val = None
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
    minVal = None
    minCnt = None
    sccCnt = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_Checkposts2.nxt, ((_java_obj_1 := Code08_Checkposts2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_Checkposts2.head[u])
        Code08_Checkposts2.to[Code08_Checkposts2.cntg] = jcast('int', v)
        Code08_Checkposts2.head[u] = jcast('int', Code08_Checkposts2.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code08_Checkposts2.dfn, u, jset(Code08_Checkposts2.low, u, ((_java_obj_4 := Code08_Checkposts2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code08_Checkposts2.sta, ((_java_obj_7 := Code08_Checkposts2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code08_Checkposts2.head[u])
        while (e > 0):
            v = jcast('int', Code08_Checkposts2.to[e])
            if (Code08_Checkposts2.dfn[v] == 0):
                Code08_Checkposts2.tarjan(v)
                jset(Code08_Checkposts2.low, u, jstatic('Math', 'min', Code08_Checkposts2.low[u], Code08_Checkposts2.low[v]))
            else:
                if (Code08_Checkposts2.belong[v] == 0):
                    jset(Code08_Checkposts2.low, u, jstatic('Math', 'min', Code08_Checkposts2.low[u], Code08_Checkposts2.dfn[v]))
            e = jcast('int', Code08_Checkposts2.nxt[e])
        if (Code08_Checkposts2.dfn[u] == Code08_Checkposts2.low[u]):
            Code08_Checkposts2.sccCnt = jcast('int', (Code08_Checkposts2.sccCnt + 1))
            Code08_Checkposts2.minVal[Code08_Checkposts2.sccCnt] = jcast('int', 1000000001)
            Code08_Checkposts2.minCnt[Code08_Checkposts2.sccCnt] = jcast('int', 0)
            pop = 0
            while True:
                pop = jcast('int', Code08_Checkposts2.sta[((_java_obj_10 := Code08_Checkposts2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code08_Checkposts2.belong[pop] = jcast('int', Code08_Checkposts2.sccCnt)
                if (Code08_Checkposts2.minVal[Code08_Checkposts2.sccCnt] > Code08_Checkposts2.val[pop]):
                    Code08_Checkposts2.minVal[Code08_Checkposts2.sccCnt] = jcast('int', Code08_Checkposts2.val[pop])
                    Code08_Checkposts2.minCnt[Code08_Checkposts2.sccCnt] = jcast('int', 1)
                else:
                    if (Code08_Checkposts2.minVal[Code08_Checkposts2.sccCnt] == Code08_Checkposts2.val[pop]):
                        Code08_Checkposts2.minCnt[Code08_Checkposts2.sccCnt] = jcast('int', (Code08_Checkposts2.minCnt[Code08_Checkposts2.sccCnt] + 1))
                if not ((pop != u)):
                    break

    @staticmethod
    def main(args):
        in_ = Code08_Checkposts2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_Checkposts2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code08_Checkposts2.n):
            jset(Code08_Checkposts2.val, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code08_Checkposts2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code08_Checkposts2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code08_Checkposts2.addEdge(u, v)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_Checkposts2.n):
            if (Code08_Checkposts2.dfn[i] == 0):
                Code08_Checkposts2.tarjan(i)
            i = jcast('int', (i + 1))
        ans1 = jcast('long', 0)
        ans2 = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code08_Checkposts2.sccCnt):
            ans1 = jcast('long', jcast('long', jadd(ans1, Code08_Checkposts2.minVal[i])))
            ans2 = jcast('long', jcast('long', jmod(jcast('long', (ans2 * Code08_Checkposts2.minCnt[i])), Code08_Checkposts2.MOD)))
            i = jcast('int', (i + 1))
        jcall(out, 'println', jadd(jadd(ans1, ' '), ans2))
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
            return jcast('int', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

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
            raise TypeError("No matching overload for Code08_Checkposts2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_Checkposts2.MAXN = jcast('int', 100001)
Code08_Checkposts2.MAXM = jcast('int', 300001)
Code08_Checkposts2.MOD = jcast('int', 1000000007)
Code08_Checkposts2.n = jcast('int', 0)
Code08_Checkposts2.m = jcast('int', 0)
Code08_Checkposts2.val = jarray('int', [Code08_Checkposts2.MAXN])
Code08_Checkposts2.head = jarray('int', [Code08_Checkposts2.MAXN])
Code08_Checkposts2.nxt = jarray('int', [Code08_Checkposts2.MAXM])
Code08_Checkposts2.to = jarray('int', [Code08_Checkposts2.MAXM])
Code08_Checkposts2.cntg = jcast('int', 0)
Code08_Checkposts2.dfn = jarray('int', [Code08_Checkposts2.MAXN])
Code08_Checkposts2.low = jarray('int', [Code08_Checkposts2.MAXN])
Code08_Checkposts2.cntd = jcast('int', 0)
Code08_Checkposts2.sta = jarray('int', [Code08_Checkposts2.MAXN])
Code08_Checkposts2.top = jcast('int', 0)
Code08_Checkposts2.belong = jarray('int', [Code08_Checkposts2.MAXN])
Code08_Checkposts2.minVal = jarray('int', [Code08_Checkposts2.MAXN])
Code08_Checkposts2.minCnt = jarray('int', [Code08_Checkposts2.MAXN])
Code08_Checkposts2.sccCnt = jcast('int', 0)

if __name__ == '__main__':
    Code08_Checkposts2.main([])
