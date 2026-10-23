# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 神会作弊，Python版
# 给定一张无向图，一共n个点、m条边，保证所有点连通，两点间出现重边只连一次
# 边双连通分量缩点后，如果点x和点y属于同一个边双连通分量，认为两点距离是1
# 如果不属于同一个边双连通分量，距离为缩点后的树上，两点简单路径上的节点个数
# 一共有q条查询，格式 x y : 计算点x和点y的距离，打印距离的二进制形式
# 1 <= n <= 10000
# 1 <= m <= 50000
# 测试链接 : https://www.luogu.com.cn/problem/P2783
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_GodCheat2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'edgeArr': 'edgeArr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'ebccCnt': 'ebccCnt', 'dep': 'dep', 'stjump': 'stjump'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    edgeArr = None
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
    ebccCnt = 0
    dep = None
    stjump = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_GodCheat2.nxt, ((_java_obj_1 := Code04_GodCheat2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_GodCheat2.head[u])
        Code04_GodCheat2.to[Code04_GodCheat2.cntg] = jcast('int', v)
        Code04_GodCheat2.head[u] = jcast('int', Code04_GodCheat2.cntg)

    @staticmethod
    def buildGraph():
        jstatic('Arrays', 'sort', Code04_GodCheat2.edgeArr, 1, jcast('int', jadd(Code04_GodCheat2.m, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        k = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code04_GodCheat2.m):
            if ((Code04_GodCheat2.edgeArr[k][0] != Code04_GodCheat2.edgeArr[i][0]) or (Code04_GodCheat2.edgeArr[k][1] != Code04_GodCheat2.edgeArr[i][1])):
                jset(Code04_GodCheat2.edgeArr[(k := jcast('int', (k + (1))))], 0, Code04_GodCheat2.edgeArr[i][0])
                jset(Code04_GodCheat2.edgeArr[k], 1, Code04_GodCheat2.edgeArr[i][1])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= k):
            Code04_GodCheat2.addEdge(Code04_GodCheat2.edgeArr[i][0], Code04_GodCheat2.edgeArr[i][1])
            Code04_GodCheat2.addEdge(Code04_GodCheat2.edgeArr[i][1], Code04_GodCheat2.edgeArr[i][0])
            i = jcast('int', (i + 1))
        Code04_GodCheat2.m = jcast('int', k)

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code04_GodCheat2.dfn, u, jset(Code04_GodCheat2.low, u, ((_java_obj_4 := Code04_GodCheat2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code04_GodCheat2.sta, ((_java_obj_7 := Code04_GodCheat2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code04_GodCheat2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code04_GodCheat2.to[e])
                if (Code04_GodCheat2.dfn[v] == 0):
                    Code04_GodCheat2.tarjan(v, e)
                    jset(Code04_GodCheat2.low, u, jstatic('Math', 'min', Code04_GodCheat2.low[u], Code04_GodCheat2.low[v]))
                else:
                    jset(Code04_GodCheat2.low, u, jstatic('Math', 'min', Code04_GodCheat2.low[u], Code04_GodCheat2.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code04_GodCheat2.nxt[e])
        if (Code04_GodCheat2.dfn[u] == Code04_GodCheat2.low[u]):
            Code04_GodCheat2.ebccCnt = jcast('int', (Code04_GodCheat2.ebccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code04_GodCheat2.sta[((_java_obj_11 := Code04_GodCheat2), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code04_GodCheat2.belong[pop] = jcast('int', Code04_GodCheat2.ebccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code04_GodCheat2.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_GodCheat2.ebccCnt):
            Code04_GodCheat2.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_GodCheat2.m):
            ebcc1 = jcast('int', Code04_GodCheat2.belong[Code04_GodCheat2.edgeArr[i][0]])
            ebcc2 = jcast('int', Code04_GodCheat2.belong[Code04_GodCheat2.edgeArr[i][1]])
            if (ebcc1 != ebcc2):
                Code04_GodCheat2.addEdge(ebcc1, ebcc2)
                Code04_GodCheat2.addEdge(ebcc2, ebcc1)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_GodCheat2.dep[u] = jcast('int', jcast('int', jadd(Code04_GodCheat2.dep[fa], 1)))
        jset(Code04_GodCheat2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code04_GodCheat2.MAXP):
            jset(Code04_GodCheat2.stjump[u], p, Code04_GodCheat2.stjump[Code04_GodCheat2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code04_GodCheat2.head[u])
        while (e > 0):
            v = jcast('int', Code04_GodCheat2.to[e])
            if (v != fa):
                Code04_GodCheat2.dfs(v, u)
            e = jcast('int', Code04_GodCheat2.nxt[e])

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code04_GodCheat2.dep[a] < Code04_GodCheat2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code04_GodCheat2.MAXP - 1)))
        while (p >= 0):
            if (Code04_GodCheat2.dep[Code04_GodCheat2.stjump[a][p]] >= Code04_GodCheat2.dep[b]):
                a = jcast('int', Code04_GodCheat2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code04_GodCheat2.MAXP - 1)))
        while (p >= 0):
            if (Code04_GodCheat2.stjump[a][p] != Code04_GodCheat2.stjump[b][p]):
                a = jcast('int', Code04_GodCheat2.stjump[a][p])
                b = jcast('int', Code04_GodCheat2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code04_GodCheat2.stjump[a][0])

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code04_GodCheat2.dep[x], Code04_GodCheat2.dep[y])) - jcast('int', (2 * Code04_GodCheat2.dep[Code04_GodCheat2.getLca(x, y)])))))

    @staticmethod
    def main(args):
        in_ = Code04_GodCheat2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_GodCheat2.cntg = jcast('int', 1)
        Code04_GodCheat2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_GodCheat2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code04_GodCheat2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            jset(Code04_GodCheat2.edgeArr[i], 0, jstatic('Math', 'min', u, v))
            jset(Code04_GodCheat2.edgeArr[i], 1, jstatic('Math', 'max', u, v))
            i = jcast('int', (i + 1))
        Code04_GodCheat2.buildGraph()
        Code04_GodCheat2.tarjan(1, 0)
        Code04_GodCheat2.condense()
        Code04_GodCheat2.dfs(1, 0)
        Code04_GodCheat2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code04_GodCheat2.q):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', Code04_GodCheat2.belong[x])
            y = jcast('int', Code04_GodCheat2.belong[y])
            jcall(out, 'println', jstatic('Integer', 'toBinaryString', jcast('int', jadd(Code04_GodCheat2.getDist(x, y), 1))))
            i = jcast('int', (i + 1))
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
            raise TypeError("No matching overload for Code04_GodCheat2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_GodCheat2.MAXN = jcast('int', 10001)
Code04_GodCheat2.MAXM = jcast('int', 50001)
Code04_GodCheat2.MAXP = jcast('int', 15)
Code04_GodCheat2.n = jcast('int', 0)
Code04_GodCheat2.m = jcast('int', 0)
Code04_GodCheat2.q = jcast('int', 0)
Code04_GodCheat2.edgeArr = jarray('int', [Code04_GodCheat2.MAXM, 2])
Code04_GodCheat2.head = jarray('int', [Code04_GodCheat2.MAXN])
Code04_GodCheat2.nxt = jarray('int', [jcast('int', (Code04_GodCheat2.MAXM << (1 & 31)))])
Code04_GodCheat2.to = jarray('int', [jcast('int', (Code04_GodCheat2.MAXM << (1 & 31)))])
Code04_GodCheat2.cntg = jcast('int', 0)
Code04_GodCheat2.dfn = jarray('int', [Code04_GodCheat2.MAXN])
Code04_GodCheat2.low = jarray('int', [Code04_GodCheat2.MAXN])
Code04_GodCheat2.cntd = jcast('int', 0)
Code04_GodCheat2.sta = jarray('int', [Code04_GodCheat2.MAXN])
Code04_GodCheat2.top = jcast('int', 0)
Code04_GodCheat2.belong = jarray('int', [Code04_GodCheat2.MAXN])
Code04_GodCheat2.ebccCnt = jcast('int', 0)
Code04_GodCheat2.dep = jarray('int', [Code04_GodCheat2.MAXN])
Code04_GodCheat2.stjump = jarray('int', [Code04_GodCheat2.MAXN, Code04_GodCheat2.MAXP])

if __name__ == '__main__':
    Code04_GodCheat2.main([])
