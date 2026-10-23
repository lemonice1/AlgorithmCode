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

# 建造军营，Python版
# 一共n个城市、m条道路，道路是无向边，保证所有城市连通
# 你可以选择任何城市，在城市内建造军营，至少要选一座城市
# 你可以选择任何道路，在道路上派兵看守，也可以一条都不选
# 选择的城市集合 + 选择的道路集合，被认为是一种方案
# 敌人会袭击任意一条道路，如果有兵看守就不会被切断，否则会被切断
# 敌人袭击之后，如果造成任意两座军营无法连通，那么算你失败
# 确保不会失败的情况下，计算方案数，答案对 1000000007 取余
# 1 <= n <= 5 * 10^5
# 1 <= m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P8867
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_MilitaryCamp1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MOD': 'MOD', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'ebccSiz': 'ebccSiz', 'ebccCnt': 'ebccCnt', 'power2': 'power2', 'dp': 'dp', 'bridge': 'bridge', 'stack': 'stack', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'fa': 'fa', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    MOD = 0
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
    ebccSiz = None
    ebccCnt = 0
    # power2[i] = 2的i次方
    power2 = None
    # dp[u] : 子树u上，原图的点可以考虑造军营，至少造一个
    # 从所造军营到u的割边都派兵，其他割边随意，这样的方案数
    dp = None
    # bridge[u] : 子树u上割边的数量
    bridge = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    preEdge = 0
    status = 0
    fa = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, preEdge, status, fa, e):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        status = jcast('int', status)
        fa = jcast('int', fa)
        e = jcast('int', e)
        jset(Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize], 0, u)
        jset(Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize], 1, preEdge)
        jset(Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize], 2, status)
        jset(Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize], 3, fa)
        jset(Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize], 4, e)
        Code07_MilitaryCamp1.stacksize = jcast('int', (Code07_MilitaryCamp1.stacksize + 1))

    @staticmethod
    def pop():
        Code07_MilitaryCamp1.stacksize = jcast('int', (Code07_MilitaryCamp1.stacksize - 1))
        Code07_MilitaryCamp1.u = jcast('int', Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize][0])
        Code07_MilitaryCamp1.preEdge = jcast('int', Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize][1])
        Code07_MilitaryCamp1.status = jcast('int', Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize][2])
        Code07_MilitaryCamp1.fa = jcast('int', Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize][3])
        Code07_MilitaryCamp1.e = jcast('int', Code07_MilitaryCamp1.stack[Code07_MilitaryCamp1.stacksize][4])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_MilitaryCamp1.nxt, ((_java_obj_1 := Code07_MilitaryCamp1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_MilitaryCamp1.head[u])
        Code07_MilitaryCamp1.to[Code07_MilitaryCamp1.cntg] = jcast('int', v)
        Code07_MilitaryCamp1.head[u] = jcast('int', Code07_MilitaryCamp1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code07_MilitaryCamp1.dfn, u, jset(Code07_MilitaryCamp1.low, u, ((_java_obj_4 := Code07_MilitaryCamp1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code07_MilitaryCamp1.sta, ((_java_obj_7 := Code07_MilitaryCamp1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code07_MilitaryCamp1.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code07_MilitaryCamp1.to[e])
                if (Code07_MilitaryCamp1.dfn[v] == 0):
                    Code07_MilitaryCamp1.tarjan1(v, e)
                    jset(Code07_MilitaryCamp1.low, u, jstatic('Math', 'min', Code07_MilitaryCamp1.low[u], Code07_MilitaryCamp1.low[v]))
                else:
                    jset(Code07_MilitaryCamp1.low, u, jstatic('Math', 'min', Code07_MilitaryCamp1.low[u], Code07_MilitaryCamp1.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code07_MilitaryCamp1.nxt[e])
        if (Code07_MilitaryCamp1.dfn[u] == Code07_MilitaryCamp1.low[u]):
            Code07_MilitaryCamp1.ebccCnt = jcast('int', (Code07_MilitaryCamp1.ebccCnt + 1))
            Code07_MilitaryCamp1.ebccSiz[Code07_MilitaryCamp1.ebccCnt] = jcast('int', 0)
            pop = 0
            while True:
                pop = jcast('int', Code07_MilitaryCamp1.sta[((_java_obj_11 := Code07_MilitaryCamp1), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code07_MilitaryCamp1.belong[pop] = jcast('int', Code07_MilitaryCamp1.ebccCnt)
                Code07_MilitaryCamp1.ebccSiz[Code07_MilitaryCamp1.ebccCnt] = jcast('int', (Code07_MilitaryCamp1.ebccSiz[Code07_MilitaryCamp1.ebccCnt] + 1))
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code07_MilitaryCamp1.stacksize = jcast('int', 0)
        Code07_MilitaryCamp1.push(node, pree, jcast('int', (-1)), 0, jcast('int', (-1)))
        v = 0
        while (Code07_MilitaryCamp1.stacksize > 0):
            Code07_MilitaryCamp1.pop()
            if (Code07_MilitaryCamp1.status == jcast('int', (-1))):
                jset(Code07_MilitaryCamp1.dfn, Code07_MilitaryCamp1.u, jset(Code07_MilitaryCamp1.low, Code07_MilitaryCamp1.u, ((_java_obj_14 := Code07_MilitaryCamp1), (_java_key_15 := 'cntd'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3]))
                jset(Code07_MilitaryCamp1.sta, ((_java_obj_17 := Code07_MilitaryCamp1), (_java_key_18 := 'top'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))))[3], Code07_MilitaryCamp1.u)
                Code07_MilitaryCamp1.e = jcast('int', Code07_MilitaryCamp1.head[Code07_MilitaryCamp1.u])
            else:
                v = jcast('int', Code07_MilitaryCamp1.to[Code07_MilitaryCamp1.e])
                if (Code07_MilitaryCamp1.status == 0):
                    jset(Code07_MilitaryCamp1.low, Code07_MilitaryCamp1.u, jstatic('Math', 'min', Code07_MilitaryCamp1.low[Code07_MilitaryCamp1.u], Code07_MilitaryCamp1.low[v]))
                else:
                    jset(Code07_MilitaryCamp1.low, Code07_MilitaryCamp1.u, jstatic('Math', 'min', Code07_MilitaryCamp1.low[Code07_MilitaryCamp1.u], Code07_MilitaryCamp1.dfn[v]))
                Code07_MilitaryCamp1.e = jcast('int', Code07_MilitaryCamp1.nxt[Code07_MilitaryCamp1.e])
            if (jcast('int', (Code07_MilitaryCamp1.e ^ 1)) == Code07_MilitaryCamp1.preEdge):
                Code07_MilitaryCamp1.e = jcast('int', Code07_MilitaryCamp1.nxt[Code07_MilitaryCamp1.e])
            if (Code07_MilitaryCamp1.e != 0):
                v = jcast('int', Code07_MilitaryCamp1.to[Code07_MilitaryCamp1.e])
                if (Code07_MilitaryCamp1.dfn[v] == 0):
                    Code07_MilitaryCamp1.push(Code07_MilitaryCamp1.u, Code07_MilitaryCamp1.preEdge, 0, 0, Code07_MilitaryCamp1.e)
                    Code07_MilitaryCamp1.push(v, Code07_MilitaryCamp1.e, jcast('int', (-1)), 0, jcast('int', (-1)))
                else:
                    Code07_MilitaryCamp1.push(Code07_MilitaryCamp1.u, Code07_MilitaryCamp1.preEdge, 1, 0, Code07_MilitaryCamp1.e)
            else:
                if (Code07_MilitaryCamp1.dfn[Code07_MilitaryCamp1.u] == Code07_MilitaryCamp1.low[Code07_MilitaryCamp1.u]):
                    Code07_MilitaryCamp1.ebccCnt = jcast('int', (Code07_MilitaryCamp1.ebccCnt + 1))
                    Code07_MilitaryCamp1.ebccSiz[Code07_MilitaryCamp1.ebccCnt] = jcast('int', 0)
                    pop = 0
                    while True:
                        pop = jcast('int', Code07_MilitaryCamp1.sta[((_java_obj_20 := Code07_MilitaryCamp1), (_java_key_21 := 'top'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (-1)))), _java_old_22)[4]])
                        Code07_MilitaryCamp1.belong[pop] = jcast('int', Code07_MilitaryCamp1.ebccCnt)
                        Code07_MilitaryCamp1.ebccSiz[Code07_MilitaryCamp1.ebccCnt] = jcast('int', (Code07_MilitaryCamp1.ebccSiz[Code07_MilitaryCamp1.ebccCnt] + 1))
                        if not ((pop != Code07_MilitaryCamp1.u)):
                            break

    @staticmethod
    def condense():
        Code07_MilitaryCamp1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_MilitaryCamp1.ebccCnt):
            Code07_MilitaryCamp1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_MilitaryCamp1.m):
            ebcc1 = jcast('int', Code07_MilitaryCamp1.belong[Code07_MilitaryCamp1.a[i]])
            ebcc2 = jcast('int', Code07_MilitaryCamp1.belong[Code07_MilitaryCamp1.b[i]])
            if (ebcc1 != ebcc2):
                Code07_MilitaryCamp1.addEdge(ebcc1, ebcc2)
                Code07_MilitaryCamp1.addEdge(ebcc2, ebcc1)
            i = jcast('int', (i + 1))

    # 递归版
    @staticmethod
    def dpOnTree1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # 情况1，不考虑下方的节点，在u自己的边双连通分量里，选点造军营
        Code07_MilitaryCamp1.dp[u] = jcast('long', jcast('long', (Code07_MilitaryCamp1.power2[Code07_MilitaryCamp1.ebccSiz[u]] - 1)))
        Code07_MilitaryCamp1.bridge[u] = jcast('int', 0)
        e = jcast('int', Code07_MilitaryCamp1.head[u])
        while (e > 0):
            v = jcast('int', Code07_MilitaryCamp1.to[e])
            if (v != fa):
                Code07_MilitaryCamp1.dpOnTree1(v, u)
                # 情况2，之前部分的方案数 * 子树v完全不造军营时割边的自由发挥 * u到v的割边自由发挥
                # 情况3，之前部分完全不造军营时割边的自由发挥 * 子树v的方案数
                # 情况4，之前部分的方案数 * 子树v的方案数
                Code07_MilitaryCamp1.dp[u] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jadd(jcast('long', jmod(jcast('long', (jcast('long', (Code07_MilitaryCamp1.dp[u] * Code07_MilitaryCamp1.power2[Code07_MilitaryCamp1.bridge[v]])) * 2)), Code07_MilitaryCamp1.MOD)), jcast('long', jmod(jcast('long', (Code07_MilitaryCamp1.power2[Code07_MilitaryCamp1.bridge[u]] * Code07_MilitaryCamp1.dp[v])), Code07_MilitaryCamp1.MOD)))), jcast('long', jmod(jcast('long', (Code07_MilitaryCamp1.dp[u] * Code07_MilitaryCamp1.dp[v])), Code07_MilitaryCamp1.MOD)))), Code07_MilitaryCamp1.MOD)))
                Code07_MilitaryCamp1.bridge[u] = jcast('int', jcast('int', jadd(Code07_MilitaryCamp1.bridge[u], jcast('int', jadd(Code07_MilitaryCamp1.bridge[v], 1)))))
            e = jcast('int', Code07_MilitaryCamp1.nxt[e])

    # 迭代版
    @staticmethod
    def dpOnTree2(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code07_MilitaryCamp1.stacksize = jcast('int', 0)
        Code07_MilitaryCamp1.push(cur, 0, 0, father, jcast('int', (-1)))
        while (Code07_MilitaryCamp1.stacksize > 0):
            Code07_MilitaryCamp1.pop()
            if (Code07_MilitaryCamp1.e == jcast('int', (-1))):
                Code07_MilitaryCamp1.dp[Code07_MilitaryCamp1.u] = jcast('long', jcast('long', (Code07_MilitaryCamp1.power2[Code07_MilitaryCamp1.ebccSiz[Code07_MilitaryCamp1.u]] - 1)))
                Code07_MilitaryCamp1.bridge[Code07_MilitaryCamp1.u] = jcast('int', 0)
                Code07_MilitaryCamp1.e = jcast('int', Code07_MilitaryCamp1.head[Code07_MilitaryCamp1.u])
            else:
                Code07_MilitaryCamp1.e = jcast('int', Code07_MilitaryCamp1.nxt[Code07_MilitaryCamp1.e])
            if (Code07_MilitaryCamp1.e != 0):
                Code07_MilitaryCamp1.push(Code07_MilitaryCamp1.u, 0, 0, Code07_MilitaryCamp1.fa, Code07_MilitaryCamp1.e)
                v = jcast('int', Code07_MilitaryCamp1.to[Code07_MilitaryCamp1.e])
                if (v != Code07_MilitaryCamp1.fa):
                    Code07_MilitaryCamp1.push(v, 0, 0, Code07_MilitaryCamp1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code07_MilitaryCamp1.head[Code07_MilitaryCamp1.u])
                while (ei > 0):
                    v = jcast('int', Code07_MilitaryCamp1.to[ei])
                    if (v != Code07_MilitaryCamp1.fa):
                        Code07_MilitaryCamp1.dp[Code07_MilitaryCamp1.u] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jadd(jcast('long', jmod(jcast('long', (Code07_MilitaryCamp1.dp[Code07_MilitaryCamp1.u] * Code07_MilitaryCamp1.power2[jcast('int', jadd(Code07_MilitaryCamp1.bridge[v], 1))])), Code07_MilitaryCamp1.MOD)), jcast('long', jmod(jcast('long', (Code07_MilitaryCamp1.power2[Code07_MilitaryCamp1.bridge[Code07_MilitaryCamp1.u]] * Code07_MilitaryCamp1.dp[v])), Code07_MilitaryCamp1.MOD)))), jcast('long', jmod(jcast('long', (Code07_MilitaryCamp1.dp[Code07_MilitaryCamp1.u] * Code07_MilitaryCamp1.dp[v])), Code07_MilitaryCamp1.MOD)))), Code07_MilitaryCamp1.MOD)))
                        Code07_MilitaryCamp1.bridge[Code07_MilitaryCamp1.u] = jcast('int', jcast('int', jadd(Code07_MilitaryCamp1.bridge[Code07_MilitaryCamp1.u], jcast('int', jadd(Code07_MilitaryCamp1.bridge[v], 1)))))
                    ei = jcast('int', Code07_MilitaryCamp1.nxt[ei])

    @staticmethod
    def compute():
        Code07_MilitaryCamp1.power2[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code07_MilitaryCamp1.m):
            Code07_MilitaryCamp1.power2[i] = jcast('long', jcast('long', jmod(jcast('long', (Code07_MilitaryCamp1.power2[jcast('int', (i - 1))] * 2)), Code07_MilitaryCamp1.MOD)))
            i = jcast('int', (i + 1))
        # dpOnTree1(1, 0);
        Code07_MilitaryCamp1.dpOnTree2(1, 0)
        total = jcast('int', Code07_MilitaryCamp1.bridge[1])
        ans = jcast('long', Code07_MilitaryCamp1.dp[1])
        i = jcast('int', 2)
        while (i <= Code07_MilitaryCamp1.ebccCnt):
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', jmod(jcast('long', (Code07_MilitaryCamp1.dp[i] * Code07_MilitaryCamp1.power2[jcast('int', (jcast('int', (total - Code07_MilitaryCamp1.bridge[i])) - 1))])), Code07_MilitaryCamp1.MOD)))), Code07_MilitaryCamp1.MOD)))
            i = jcast('int', (i + 1))
        ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code07_MilitaryCamp1.power2[jcast('int', (Code07_MilitaryCamp1.m - total))])), Code07_MilitaryCamp1.MOD)))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code07_MilitaryCamp1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_MilitaryCamp1.cntg = jcast('int', 1)
        Code07_MilitaryCamp1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_MilitaryCamp1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_MilitaryCamp1.m):
            jset(Code07_MilitaryCamp1.a, i, jcall(in_, 'nextInt'))
            jset(Code07_MilitaryCamp1.b, i, jcall(in_, 'nextInt'))
            Code07_MilitaryCamp1.addEdge(Code07_MilitaryCamp1.a[i], Code07_MilitaryCamp1.b[i])
            Code07_MilitaryCamp1.addEdge(Code07_MilitaryCamp1.b[i], Code07_MilitaryCamp1.a[i])
            i = jcast('int', (i + 1))
        # tarjan1(1, 0);
        Code07_MilitaryCamp1.tarjan2(1, 0)
        Code07_MilitaryCamp1.condense()
        ans = jcast('long', Code07_MilitaryCamp1.compute())
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
            raise TypeError("No matching overload for Code07_MilitaryCamp1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_MilitaryCamp1.MAXN = jcast('int', 500001)
Code07_MilitaryCamp1.MAXM = jcast('int', 1000001)
Code07_MilitaryCamp1.MOD = jcast('int', 1000000007)
Code07_MilitaryCamp1.n = jcast('int', 0)
Code07_MilitaryCamp1.m = jcast('int', 0)
Code07_MilitaryCamp1.a = jarray('int', [Code07_MilitaryCamp1.MAXM])
Code07_MilitaryCamp1.b = jarray('int', [Code07_MilitaryCamp1.MAXM])
Code07_MilitaryCamp1.head = jarray('int', [Code07_MilitaryCamp1.MAXN])
Code07_MilitaryCamp1.nxt = jarray('int', [jcast('int', (Code07_MilitaryCamp1.MAXM << (1 & 31)))])
Code07_MilitaryCamp1.to = jarray('int', [jcast('int', (Code07_MilitaryCamp1.MAXM << (1 & 31)))])
Code07_MilitaryCamp1.cntg = jcast('int', 0)
Code07_MilitaryCamp1.dfn = jarray('int', [Code07_MilitaryCamp1.MAXN])
Code07_MilitaryCamp1.low = jarray('int', [Code07_MilitaryCamp1.MAXN])
Code07_MilitaryCamp1.cntd = jcast('int', 0)
Code07_MilitaryCamp1.sta = jarray('int', [Code07_MilitaryCamp1.MAXN])
Code07_MilitaryCamp1.top = jcast('int', 0)
Code07_MilitaryCamp1.belong = jarray('int', [Code07_MilitaryCamp1.MAXN])
Code07_MilitaryCamp1.ebccSiz = jarray('int', [Code07_MilitaryCamp1.MAXN])
Code07_MilitaryCamp1.ebccCnt = jcast('int', 0)
Code07_MilitaryCamp1.power2 = jarray('long', [Code07_MilitaryCamp1.MAXM])
Code07_MilitaryCamp1.dp = jarray('long', [Code07_MilitaryCamp1.MAXN])
Code07_MilitaryCamp1.bridge = jarray('int', [Code07_MilitaryCamp1.MAXN])
Code07_MilitaryCamp1.stack = jarray('int', [Code07_MilitaryCamp1.MAXN, 5])
Code07_MilitaryCamp1.u = jcast('int', 0)
Code07_MilitaryCamp1.preEdge = jcast('int', 0)
Code07_MilitaryCamp1.status = jcast('int', 0)
Code07_MilitaryCamp1.fa = jcast('int', 0)
Code07_MilitaryCamp1.e = jcast('int', 0)
Code07_MilitaryCamp1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code07_MilitaryCamp1.main([])
