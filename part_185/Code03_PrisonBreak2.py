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

# 越狱老虎桥，Python版
# 给定一张无向图，一共n个点、m条边，保证所有点连通
# 每条边给定边权，表示破坏这条边需要花费的钱数
# 敌人可能在任意两点之间新增一条边，新增的这条边无法被破坏
# 敌人新增一条边之后，你的目标是只破坏一条边，就让图变成两个连通区
# 你不知道敌人会选择哪两个端点来新增这条边，你需要尽可能的做好准备
# 假设遭遇最差情况，打印你至少准备多少钱才能完成目标，无法完成目标打印-1
# 1 <= n <= 5 * 10^5
# 1 <= m <= 10^6
# 1 <= 边权 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5234
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_PrisonBreak2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'maxv': 'maxv', 'a': 'a', 'b': 'b', 'c': 'c', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'ebccCnt': 'ebccCnt', 'dist': 'dist', 'diameter': 'diameter', 'edgeCnt': 'edgeCnt'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    maxv = 0
    a = None
    b = None
    c = None
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
    ebccCnt = 0
    dist = None
    diameter = 0
    edgeCnt = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_PrisonBreak2.nxt, ((_java_obj_1 := Code03_PrisonBreak2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_PrisonBreak2.head[u])
        Code03_PrisonBreak2.to[Code03_PrisonBreak2.cntg] = jcast('int', v)
        Code03_PrisonBreak2.weight[Code03_PrisonBreak2.cntg] = jcast('int', w)
        Code03_PrisonBreak2.head[u] = jcast('int', Code03_PrisonBreak2.cntg)

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code03_PrisonBreak2.dfn, u, jset(Code03_PrisonBreak2.low, u, ((_java_obj_4 := Code03_PrisonBreak2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code03_PrisonBreak2.sta, ((_java_obj_7 := Code03_PrisonBreak2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code03_PrisonBreak2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code03_PrisonBreak2.to[e])
                if (Code03_PrisonBreak2.dfn[v] == 0):
                    Code03_PrisonBreak2.tarjan(v, e)
                    jset(Code03_PrisonBreak2.low, u, jstatic('Math', 'min', Code03_PrisonBreak2.low[u], Code03_PrisonBreak2.low[v]))
                else:
                    jset(Code03_PrisonBreak2.low, u, jstatic('Math', 'min', Code03_PrisonBreak2.low[u], Code03_PrisonBreak2.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code03_PrisonBreak2.nxt[e])
        if (Code03_PrisonBreak2.dfn[u] == Code03_PrisonBreak2.low[u]):
            Code03_PrisonBreak2.ebccCnt = jcast('int', (Code03_PrisonBreak2.ebccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code03_PrisonBreak2.sta[((_java_obj_11 := Code03_PrisonBreak2), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code03_PrisonBreak2.belong[pop] = jcast('int', Code03_PrisonBreak2.ebccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code03_PrisonBreak2.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_PrisonBreak2.ebccCnt):
            Code03_PrisonBreak2.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_PrisonBreak2.m):
            ebcc1 = jcast('int', Code03_PrisonBreak2.belong[Code03_PrisonBreak2.a[i]])
            ebcc2 = jcast('int', Code03_PrisonBreak2.belong[Code03_PrisonBreak2.b[i]])
            w = jcast('int', Code03_PrisonBreak2.c[i])
            if (ebcc1 != ebcc2):
                Code03_PrisonBreak2.addEdge(ebcc1, ebcc2, w)
                Code03_PrisonBreak2.addEdge(ebcc2, ebcc1, w)
            i = jcast('int', (i + 1))

    @staticmethod
    def dpOnTree(u, fa, limit):
        u = jcast('int', u)
        fa = jcast('int', fa)
        limit = jcast('int', limit)
        e = jcast('int', Code03_PrisonBreak2.head[u])
        while (e > 0):
            v = jcast('int', Code03_PrisonBreak2.to[e])
            if (v != fa):
                Code03_PrisonBreak2.dpOnTree(v, u, limit)
                w = jcast('int', (1 if (Code03_PrisonBreak2.weight[e] <= limit) else 0))
                Code03_PrisonBreak2.edgeCnt = jcast('int', jcast('int', jadd(Code03_PrisonBreak2.edgeCnt, w)))
                Code03_PrisonBreak2.diameter = jcast('int', jstatic('Math', 'max', Code03_PrisonBreak2.diameter, jcast('int', jadd(jcast('int', jadd(Code03_PrisonBreak2.dist[u], Code03_PrisonBreak2.dist[v])), w))))
                jset(Code03_PrisonBreak2.dist, u, jstatic('Math', 'max', Code03_PrisonBreak2.dist[u], jcast('int', jadd(Code03_PrisonBreak2.dist[v], w))))
            e = jcast('int', Code03_PrisonBreak2.nxt[e])

    @staticmethod
    def check(limit):
        limit = jcast('int', limit)
        i = jcast('int', 1)
        while (i <= Code03_PrisonBreak2.ebccCnt):
            Code03_PrisonBreak2.dist[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code03_PrisonBreak2.diameter = jcast('int', jset(Code03_PrisonBreak2, 'edgeCnt', 0))
        Code03_PrisonBreak2.dpOnTree(1, 0, limit)
        return jcast('boolean', (Code03_PrisonBreak2.diameter < Code03_PrisonBreak2.edgeCnt))

    @staticmethod
    def compute():
        l = jcast('int', 1)
        r = jcast('int', Code03_PrisonBreak2.maxv)
        mid = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if Code03_PrisonBreak2.check(mid):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code03_PrisonBreak2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_PrisonBreak2.cntg = jcast('int', 1)
        Code03_PrisonBreak2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_PrisonBreak2.m = jcast('int', jcall(in_, 'nextInt'))
        Code03_PrisonBreak2.maxv = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_PrisonBreak2.m):
            jset(Code03_PrisonBreak2.a, i, jcall(in_, 'nextInt'))
            jset(Code03_PrisonBreak2.b, i, jcall(in_, 'nextInt'))
            jset(Code03_PrisonBreak2.c, i, jcall(in_, 'nextInt'))
            Code03_PrisonBreak2.addEdge(Code03_PrisonBreak2.a[i], Code03_PrisonBreak2.b[i], 0)
            Code03_PrisonBreak2.addEdge(Code03_PrisonBreak2.b[i], Code03_PrisonBreak2.a[i], 0)
            Code03_PrisonBreak2.maxv = jcast('int', jstatic('Math', 'max', Code03_PrisonBreak2.maxv, Code03_PrisonBreak2.c[i]))
            i = jcast('int', (i + 1))
        Code03_PrisonBreak2.tarjan(1, 0)
        Code03_PrisonBreak2.condense()
        jcall(out, 'println', Code03_PrisonBreak2.compute())
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
            return jcast('int', self.buffer[((_java_obj_14 := self), (_java_key_15 := 'ptr'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]])

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
            raise TypeError("No matching overload for Code03_PrisonBreak2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_PrisonBreak2.MAXN = jcast('int', 500001)
Code03_PrisonBreak2.MAXM = jcast('int', 1000001)
Code03_PrisonBreak2.n = jcast('int', 0)
Code03_PrisonBreak2.m = jcast('int', 0)
Code03_PrisonBreak2.maxv = jcast('int', 0)
Code03_PrisonBreak2.a = jarray('int', [Code03_PrisonBreak2.MAXM])
Code03_PrisonBreak2.b = jarray('int', [Code03_PrisonBreak2.MAXM])
Code03_PrisonBreak2.c = jarray('int', [Code03_PrisonBreak2.MAXM])
Code03_PrisonBreak2.head = jarray('int', [Code03_PrisonBreak2.MAXN])
Code03_PrisonBreak2.nxt = jarray('int', [jcast('int', (Code03_PrisonBreak2.MAXM << (1 & 31)))])
Code03_PrisonBreak2.to = jarray('int', [jcast('int', (Code03_PrisonBreak2.MAXM << (1 & 31)))])
Code03_PrisonBreak2.weight = jarray('int', [jcast('int', (Code03_PrisonBreak2.MAXM << (1 & 31)))])
Code03_PrisonBreak2.cntg = jcast('int', 0)
Code03_PrisonBreak2.dfn = jarray('int', [Code03_PrisonBreak2.MAXN])
Code03_PrisonBreak2.low = jarray('int', [Code03_PrisonBreak2.MAXN])
Code03_PrisonBreak2.cntd = jcast('int', 0)
Code03_PrisonBreak2.sta = jarray('int', [Code03_PrisonBreak2.MAXN])
Code03_PrisonBreak2.top = jcast('int', 0)
Code03_PrisonBreak2.belong = jarray('int', [Code03_PrisonBreak2.MAXN])
Code03_PrisonBreak2.ebccCnt = jcast('int', 0)
Code03_PrisonBreak2.dist = jarray('int', [Code03_PrisonBreak2.MAXN])
Code03_PrisonBreak2.diameter = jcast('int', 0)
Code03_PrisonBreak2.edgeCnt = jcast('int', 0)

if __name__ == '__main__':
    Code03_PrisonBreak2.main([])
