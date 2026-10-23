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

# 仙人掌加边方案数，Python版
# 给定n个点、m条边的无向连通图，输入保证没有自环、没有重边
# 可以在图中加入一些新的边，如果加入后得到的图是仙人掌，就叫有效的加边方案
# 允许一条边也不加，但不允许加边后，形成自环或二元环，计算有效的加边方案数
# 答案对 998244353 取余，每次输入可能有多组测试数据
# 1 <= n <= 5 * 10^5
# 1 <= m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P3687
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_CactusAddEdge1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MOD': 'MOD', 't': 't', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cycleEdge': 'cycleEdge', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'fromEdge': 'fromEdge', 'cycleCnt': 'cycleCnt', 'vis': 'vis', 'f': 'f', 'dp': 'dp', 'stau': 'stau', 'stap': 'stap', 'stas': 'stas', 'staf': 'staf', 'stae': 'stae', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'fa': 'fa', 'e': 'e', 'stacksiz': 'stacksiz'}
    MAXN = 0
    MAXM = 0
    MOD = 0
    t = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cycleEdge = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    fromEdge = None
    cycleCnt = None
    vis = None
    # f[i] : 点周围有i个方向，一旦两个方向配对，不可再用
    # 方向也可不配对，总的配对方法数
    f = None
    # dp[u] : u周围的每个支路配对或者不配对，形成的方案数
    # 两个支路配对是指，各自选出一个端点然后连边
    # 如果u是根，认为上方没有支路
    # 如果u不是根，认为上方有支路，内有一个点
    dp = None
    # 递归改迭代需要的栈
    stau = None
    stap = None
    stas = None
    staf = None
    stae = None
    u = 0
    preEdge = 0
    status = 0
    fa = 0
    e = 0
    stacksiz = 0
    @staticmethod
    def push(u, preEdge, status, fa, e):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        status = jcast('int', status)
        fa = jcast('int', fa)
        e = jcast('int', e)
        Code02_CactusAddEdge1.stau[Code02_CactusAddEdge1.stacksiz] = jcast('int', u)
        Code02_CactusAddEdge1.stap[Code02_CactusAddEdge1.stacksiz] = jcast('int', preEdge)
        Code02_CactusAddEdge1.stas[Code02_CactusAddEdge1.stacksiz] = jcast('int', status)
        Code02_CactusAddEdge1.staf[Code02_CactusAddEdge1.stacksiz] = jcast('int', fa)
        Code02_CactusAddEdge1.stae[Code02_CactusAddEdge1.stacksiz] = jcast('int', e)
        Code02_CactusAddEdge1.stacksiz = jcast('int', (Code02_CactusAddEdge1.stacksiz + 1))

    @staticmethod
    def pop():
        Code02_CactusAddEdge1.stacksiz = jcast('int', (Code02_CactusAddEdge1.stacksiz - 1))
        Code02_CactusAddEdge1.u = jcast('int', Code02_CactusAddEdge1.stau[Code02_CactusAddEdge1.stacksiz])
        Code02_CactusAddEdge1.preEdge = jcast('int', Code02_CactusAddEdge1.stap[Code02_CactusAddEdge1.stacksiz])
        Code02_CactusAddEdge1.status = jcast('int', Code02_CactusAddEdge1.stas[Code02_CactusAddEdge1.stacksiz])
        Code02_CactusAddEdge1.fa = jcast('int', Code02_CactusAddEdge1.staf[Code02_CactusAddEdge1.stacksiz])
        Code02_CactusAddEdge1.e = jcast('int', Code02_CactusAddEdge1.stae[Code02_CactusAddEdge1.stacksiz])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_CactusAddEdge1.nxt, ((_java_obj_1 := Code02_CactusAddEdge1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_CactusAddEdge1.head[u])
        Code02_CactusAddEdge1.to[Code02_CactusAddEdge1.cntg] = jcast('int', v)
        Code02_CactusAddEdge1.cycleEdge[Code02_CactusAddEdge1.cntg] = jcast('boolean', False)
        Code02_CactusAddEdge1.head[u] = jcast('int', Code02_CactusAddEdge1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code02_CactusAddEdge1.dfn, u, jset(Code02_CactusAddEdge1.low, u, ((_java_obj_4 := Code02_CactusAddEdge1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code02_CactusAddEdge1.sta, ((_java_obj_7 := Code02_CactusAddEdge1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code02_CactusAddEdge1.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code02_CactusAddEdge1.to[e])
                if (Code02_CactusAddEdge1.dfn[v] == 0):
                    Code02_CactusAddEdge1.tarjan1(v, e)
                    Code02_CactusAddEdge1.fromEdge[v] = jcast('int', e)
                    if (Code02_CactusAddEdge1.low[v] < Code02_CactusAddEdge1.dfn[u]):
                        jset(Code02_CactusAddEdge1.low, u, jstatic('Math', 'min', Code02_CactusAddEdge1.low[u], Code02_CactusAddEdge1.low[v]))
                        Code02_CactusAddEdge1.cycleCnt[u] = jcast('int', (Code02_CactusAddEdge1.cycleCnt[u] + 1))
                    else:
                        if (Code02_CactusAddEdge1.low[v] > Code02_CactusAddEdge1.dfn[u]):
                            Code02_CactusAddEdge1.top = jcast('int', (Code02_CactusAddEdge1.top - 1))
                        else:
                            pop = 0
                            edge = jcast('int', Code02_CactusAddEdge1.fromEdge[u])
                            jset(Code02_CactusAddEdge1.cycleEdge, edge, jset(Code02_CactusAddEdge1.cycleEdge, jcast('int', (edge ^ 1)), True))
                            while True:
                                pop = jcast('int', Code02_CactusAddEdge1.sta[((_java_obj_11 := Code02_CactusAddEdge1), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                                edge = jcast('int', Code02_CactusAddEdge1.fromEdge[pop])
                                jset(Code02_CactusAddEdge1.cycleEdge, edge, jset(Code02_CactusAddEdge1.cycleEdge, jcast('int', (edge ^ 1)), True))
                                if not ((pop != v)):
                                    break
                else:
                    if (Code02_CactusAddEdge1.dfn[v] < Code02_CactusAddEdge1.dfn[u]):
                        Code02_CactusAddEdge1.fromEdge[v] = jcast('int', e)
                        jset(Code02_CactusAddEdge1.low, u, jstatic('Math', 'min', Code02_CactusAddEdge1.low[u], Code02_CactusAddEdge1.dfn[v]))
                        Code02_CactusAddEdge1.cycleCnt[u] = jcast('int', (Code02_CactusAddEdge1.cycleCnt[u] + 1))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code02_CactusAddEdge1.nxt[e])

    # 迭代版
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code02_CactusAddEdge1.stacksiz = jcast('int', 0)
        Code02_CactusAddEdge1.push(node, pree, jcast('int', (-1)), 0, jcast('int', (-1)))
        v = 0
        while (Code02_CactusAddEdge1.stacksiz > 0):
            Code02_CactusAddEdge1.pop()
            if (Code02_CactusAddEdge1.status == jcast('int', (-1))):
                jset(Code02_CactusAddEdge1.dfn, Code02_CactusAddEdge1.u, jset(Code02_CactusAddEdge1.low, Code02_CactusAddEdge1.u, ((_java_obj_14 := Code02_CactusAddEdge1), (_java_key_15 := 'cntd'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3]))
                jset(Code02_CactusAddEdge1.sta, ((_java_obj_17 := Code02_CactusAddEdge1), (_java_key_18 := 'top'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))))[3], Code02_CactusAddEdge1.u)
                Code02_CactusAddEdge1.e = jcast('int', Code02_CactusAddEdge1.head[Code02_CactusAddEdge1.u])
            else:
                v = jcast('int', Code02_CactusAddEdge1.to[Code02_CactusAddEdge1.e])
                if (Code02_CactusAddEdge1.status == 0):
                    Code02_CactusAddEdge1.fromEdge[v] = jcast('int', Code02_CactusAddEdge1.e)
                    if (Code02_CactusAddEdge1.low[v] < Code02_CactusAddEdge1.dfn[Code02_CactusAddEdge1.u]):
                        jset(Code02_CactusAddEdge1.low, Code02_CactusAddEdge1.u, jstatic('Math', 'min', Code02_CactusAddEdge1.low[Code02_CactusAddEdge1.u], Code02_CactusAddEdge1.low[v]))
                        Code02_CactusAddEdge1.cycleCnt[Code02_CactusAddEdge1.u] = jcast('int', (Code02_CactusAddEdge1.cycleCnt[Code02_CactusAddEdge1.u] + 1))
                    else:
                        if (Code02_CactusAddEdge1.low[v] > Code02_CactusAddEdge1.dfn[Code02_CactusAddEdge1.u]):
                            Code02_CactusAddEdge1.top = jcast('int', (Code02_CactusAddEdge1.top - 1))
                        else:
                            pop = 0
                            edge = jcast('int', Code02_CactusAddEdge1.fromEdge[Code02_CactusAddEdge1.u])
                            jset(Code02_CactusAddEdge1.cycleEdge, edge, jset(Code02_CactusAddEdge1.cycleEdge, jcast('int', (edge ^ 1)), True))
                            while True:
                                pop = jcast('int', Code02_CactusAddEdge1.sta[((_java_obj_20 := Code02_CactusAddEdge1), (_java_key_21 := 'top'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (-1)))), _java_old_22)[4]])
                                edge = jcast('int', Code02_CactusAddEdge1.fromEdge[pop])
                                jset(Code02_CactusAddEdge1.cycleEdge, edge, jset(Code02_CactusAddEdge1.cycleEdge, jcast('int', (edge ^ 1)), True))
                                if not ((pop != v)):
                                    break
                else:
                    if (Code02_CactusAddEdge1.dfn[v] < Code02_CactusAddEdge1.dfn[Code02_CactusAddEdge1.u]):
                        Code02_CactusAddEdge1.fromEdge[v] = jcast('int', Code02_CactusAddEdge1.e)
                        jset(Code02_CactusAddEdge1.low, Code02_CactusAddEdge1.u, jstatic('Math', 'min', Code02_CactusAddEdge1.low[Code02_CactusAddEdge1.u], Code02_CactusAddEdge1.dfn[v]))
                        Code02_CactusAddEdge1.cycleCnt[Code02_CactusAddEdge1.u] = jcast('int', (Code02_CactusAddEdge1.cycleCnt[Code02_CactusAddEdge1.u] + 1))
                Code02_CactusAddEdge1.e = jcast('int', Code02_CactusAddEdge1.nxt[Code02_CactusAddEdge1.e])
            if (jcast('int', (Code02_CactusAddEdge1.e ^ 1)) == Code02_CactusAddEdge1.preEdge):
                Code02_CactusAddEdge1.e = jcast('int', Code02_CactusAddEdge1.nxt[Code02_CactusAddEdge1.e])
            if (Code02_CactusAddEdge1.e != 0):
                v = jcast('int', Code02_CactusAddEdge1.to[Code02_CactusAddEdge1.e])
                if (Code02_CactusAddEdge1.dfn[v] == 0):
                    Code02_CactusAddEdge1.push(Code02_CactusAddEdge1.u, Code02_CactusAddEdge1.preEdge, 0, 0, Code02_CactusAddEdge1.e)
                    Code02_CactusAddEdge1.push(v, Code02_CactusAddEdge1.e, jcast('int', (-1)), 0, jcast('int', (-1)))
                else:
                    Code02_CactusAddEdge1.push(Code02_CactusAddEdge1.u, Code02_CactusAddEdge1.preEdge, 1, 0, Code02_CactusAddEdge1.e)

    # 递归版
    @staticmethod
    def dpOnTree1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_CactusAddEdge1.vis[u] = jcast('boolean', True)
        ans = jcast('long', 1)
        direction = jcast('int', (0 if (fa == 0) else 1))
        e = jcast('int', Code02_CactusAddEdge1.head[u])
        while (e > 0):
            v = jcast('int', Code02_CactusAddEdge1.to[e])
            if ((v != fa) and (not Code02_CactusAddEdge1.cycleEdge[e])):
                Code02_CactusAddEdge1.dpOnTree1(v, u)
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code02_CactusAddEdge1.dp[v])), Code02_CactusAddEdge1.MOD)))
                direction = jcast('int', (direction + 1))
            e = jcast('int', Code02_CactusAddEdge1.nxt[e])
        Code02_CactusAddEdge1.dp[u] = jcast('long', jcast('long', jmod(jcast('long', (ans * Code02_CactusAddEdge1.f[direction])), Code02_CactusAddEdge1.MOD)))

    # 迭代版
    @staticmethod
    def dpOnTree2(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code02_CactusAddEdge1.stacksiz = jcast('int', 0)
        Code02_CactusAddEdge1.push(cur, 0, 0, father, jcast('int', (-1)))
        while (Code02_CactusAddEdge1.stacksiz > 0):
            Code02_CactusAddEdge1.pop()
            if (Code02_CactusAddEdge1.e == jcast('int', (-1))):
                Code02_CactusAddEdge1.vis[Code02_CactusAddEdge1.u] = jcast('boolean', True)
                Code02_CactusAddEdge1.e = jcast('int', Code02_CactusAddEdge1.head[Code02_CactusAddEdge1.u])
            else:
                Code02_CactusAddEdge1.e = jcast('int', Code02_CactusAddEdge1.nxt[Code02_CactusAddEdge1.e])
            if (Code02_CactusAddEdge1.e != 0):
                Code02_CactusAddEdge1.push(Code02_CactusAddEdge1.u, 0, 0, Code02_CactusAddEdge1.fa, Code02_CactusAddEdge1.e)
                v = jcast('int', Code02_CactusAddEdge1.to[Code02_CactusAddEdge1.e])
                if ((v != Code02_CactusAddEdge1.fa) and (not Code02_CactusAddEdge1.cycleEdge[Code02_CactusAddEdge1.e])):
                    Code02_CactusAddEdge1.push(v, 0, 0, Code02_CactusAddEdge1.u, jcast('int', (-1)))
            else:
                ans = jcast('long', 1)
                direction = jcast('int', (0 if (Code02_CactusAddEdge1.fa == 0) else 1))
                e = jcast('int', Code02_CactusAddEdge1.head[Code02_CactusAddEdge1.u])
                while (e > 0):
                    v = jcast('int', Code02_CactusAddEdge1.to[e])
                    if ((v != Code02_CactusAddEdge1.fa) and (not Code02_CactusAddEdge1.cycleEdge[e])):
                        ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code02_CactusAddEdge1.dp[v])), Code02_CactusAddEdge1.MOD)))
                        direction = jcast('int', (direction + 1))
                    e = jcast('int', Code02_CactusAddEdge1.nxt[e])
                Code02_CactusAddEdge1.dp[Code02_CactusAddEdge1.u] = jcast('long', jcast('long', jmod(jcast('long', (ans * Code02_CactusAddEdge1.f[direction])), Code02_CactusAddEdge1.MOD)))

    @staticmethod
    def prepare():
        jset(Code02_CactusAddEdge1.f, 0, jset(Code02_CactusAddEdge1.f, 1, 1))
        Code02_CactusAddEdge1.f[2] = jcast('long', 2)
        i = jcast('int', 3)
        while (i <= Code02_CactusAddEdge1.n):
            Code02_CactusAddEdge1.f[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code02_CactusAddEdge1.f[jcast('int', (i - 1))], jcast('long', (Code02_CactusAddEdge1.f[jcast('int', (i - 2))] * jcast('int', (i - 1)))))), Code02_CactusAddEdge1.MOD)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_CactusAddEdge1.n):
            jset(Code02_CactusAddEdge1.head, i, jset(Code02_CactusAddEdge1.dfn, i, jset(Code02_CactusAddEdge1.low, i, jset(Code02_CactusAddEdge1.fromEdge, i, jset(Code02_CactusAddEdge1.cycleCnt, i, 0)))))
            Code02_CactusAddEdge1.vis[i] = jcast('boolean', False)
            Code02_CactusAddEdge1.dp[i] = jcast('long', 0)
            i = jcast('int', (i + 1))
        Code02_CactusAddEdge1.cntg = jcast('int', 1)
        Code02_CactusAddEdge1.cntd = jcast('int', jset(Code02_CactusAddEdge1, 'top', 0))

    @staticmethod
    def main(args):
        in_ = Code02_CactusAddEdge1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_CactusAddEdge1.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code02_CactusAddEdge1.t):
            try:
                Code02_CactusAddEdge1.n = jcast('int', jcall(in_, 'nextInt'))
                Code02_CactusAddEdge1.m = jcast('int', jcall(in_, 'nextInt'))
                Code02_CactusAddEdge1.prepare()
                i = jcast('int', 1)
                u = 0
                v = 0
                while (i <= Code02_CactusAddEdge1.m):
                    u = jcast('int', jcall(in_, 'nextInt'))
                    v = jcast('int', jcall(in_, 'nextInt'))
                    Code02_CactusAddEdge1.addEdge(u, v)
                    Code02_CactusAddEdge1.addEdge(v, u)
                    i = jcast('int', (i + 1))
                # tarjan1(1, 0);
                Code02_CactusAddEdge1.tarjan2(1, 0)
                check = jcast('boolean', True)
                i = jcast('int', 1)
                while (i <= Code02_CactusAddEdge1.n):
                    try:
                        if (Code02_CactusAddEdge1.cycleCnt[i] >= 2):
                            check = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_24:
                        if _java_control_24.label not in (None,):
                            raise
                    except JBreak as _java_control_24:
                        if _java_control_24.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
                if check:
                    ans = jcast('long', 1)
                    i = jcast('int', 1)
                    while (i <= Code02_CactusAddEdge1.n):
                        if (not Code02_CactusAddEdge1.vis[i]):
                            # dpOnTree1(i, 0);
                            Code02_CactusAddEdge1.dpOnTree2(i, 0)
                            ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code02_CactusAddEdge1.dp[i])), Code02_CactusAddEdge1.MOD)))
                        i = jcast('int', (i + 1))
                    jcall(out, 'println', ans)
                else:
                    jcall(out, 'println', 0)
            except JContinue as _java_control_23:
                if _java_control_23.label not in (None,):
                    raise
            except JBreak as _java_control_23:
                if _java_control_23.label not in (None,):
                    raise
                break
            c = jcast('int', (c + 1))
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
            return jcast('int', self.buffer[((_java_obj_25 := self), (_java_key_26 := 'ptr'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))), _java_old_27)[4]])

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
            raise TypeError("No matching overload for Code02_CactusAddEdge1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CactusAddEdge1.MAXN = jcast('int', 500001)
Code02_CactusAddEdge1.MAXM = jcast('int', 1000001)
Code02_CactusAddEdge1.MOD = jcast('int', 998244353)
Code02_CactusAddEdge1.t = jcast('int', 0)
Code02_CactusAddEdge1.n = jcast('int', 0)
Code02_CactusAddEdge1.m = jcast('int', 0)
Code02_CactusAddEdge1.head = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.nxt = jarray('int', [jcast('int', (Code02_CactusAddEdge1.MAXM << (1 & 31)))])
Code02_CactusAddEdge1.to = jarray('int', [jcast('int', (Code02_CactusAddEdge1.MAXM << (1 & 31)))])
Code02_CactusAddEdge1.cycleEdge = jarray('boolean', [jcast('int', (Code02_CactusAddEdge1.MAXM << (1 & 31)))])
Code02_CactusAddEdge1.cntg = jcast('int', 0)
Code02_CactusAddEdge1.dfn = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.low = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.cntd = jcast('int', 0)
Code02_CactusAddEdge1.sta = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.top = jcast('int', 0)
Code02_CactusAddEdge1.fromEdge = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.cycleCnt = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.vis = jarray('boolean', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.f = jarray('long', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.dp = jarray('long', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.stau = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.stap = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.stas = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.staf = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.stae = jarray('int', [Code02_CactusAddEdge1.MAXN])
Code02_CactusAddEdge1.u = jcast('int', 0)
Code02_CactusAddEdge1.preEdge = jcast('int', 0)
Code02_CactusAddEdge1.status = jcast('int', 0)
Code02_CactusAddEdge1.fa = jcast('int', 0)
Code02_CactusAddEdge1.e = jcast('int', 0)
Code02_CactusAddEdge1.stacksiz = jcast('int', 0)

if __name__ == '__main__':
    Code02_CactusAddEdge1.main([])
