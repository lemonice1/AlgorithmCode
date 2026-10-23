# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 追寻文物，Python版
# 给定一张无向图，一共n个点、m条边，保证所有点连通
# 每条边除了端点之外，还有一个属性，值为1表示该边上有商品，值为0表示该边上无商品
# 给定起点s和终点t，路途怎么走随意，但是沿途每条边只能经过一次
# 从s到t的路途中能遇到商品打印"YES"，否则打印"NO"
# 1 <= n、m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF652E
# 测试链接 : https://codeforces.com/problemset/problem/652/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_PursuitArtifacts2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 's': 's', 't': 't', 'a': 'a', 'b': 'b', 'c': 'c', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'val': 'val', 'ebccCnt': 'ebccCnt'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    s = 0
    t = 0
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
    val = None
    ebccCnt = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code01_PursuitArtifacts2.nxt, ((_java_obj_1 := Code01_PursuitArtifacts2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_PursuitArtifacts2.head[u])
        Code01_PursuitArtifacts2.to[Code01_PursuitArtifacts2.cntg] = jcast('int', v)
        Code01_PursuitArtifacts2.weight[Code01_PursuitArtifacts2.cntg] = jcast('int', w)
        Code01_PursuitArtifacts2.head[u] = jcast('int', Code01_PursuitArtifacts2.cntg)

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code01_PursuitArtifacts2.dfn, u, jset(Code01_PursuitArtifacts2.low, u, ((_java_obj_4 := Code01_PursuitArtifacts2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code01_PursuitArtifacts2.sta, ((_java_obj_7 := Code01_PursuitArtifacts2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code01_PursuitArtifacts2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code01_PursuitArtifacts2.to[e])
                if (Code01_PursuitArtifacts2.dfn[v] == 0):
                    Code01_PursuitArtifacts2.tarjan(v, e)
                    jset(Code01_PursuitArtifacts2.low, u, jstatic('Math', 'min', Code01_PursuitArtifacts2.low[u], Code01_PursuitArtifacts2.low[v]))
                else:
                    jset(Code01_PursuitArtifacts2.low, u, jstatic('Math', 'min', Code01_PursuitArtifacts2.low[u], Code01_PursuitArtifacts2.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code01_PursuitArtifacts2.nxt[e])
        if (Code01_PursuitArtifacts2.dfn[u] == Code01_PursuitArtifacts2.low[u]):
            Code01_PursuitArtifacts2.ebccCnt = jcast('int', (Code01_PursuitArtifacts2.ebccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code01_PursuitArtifacts2.sta[((_java_obj_11 := Code01_PursuitArtifacts2), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code01_PursuitArtifacts2.belong[pop] = jcast('int', Code01_PursuitArtifacts2.ebccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code01_PursuitArtifacts2.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_PursuitArtifacts2.ebccCnt):
            Code01_PursuitArtifacts2.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_PursuitArtifacts2.m):
            ebcc1 = jcast('int', Code01_PursuitArtifacts2.belong[Code01_PursuitArtifacts2.a[i]])
            ebcc2 = jcast('int', Code01_PursuitArtifacts2.belong[Code01_PursuitArtifacts2.b[i]])
            w = jcast('int', Code01_PursuitArtifacts2.c[i])
            if (ebcc1 == ebcc2):
                if (w == 1):
                    Code01_PursuitArtifacts2.val[ebcc1] = jcast('int', 1)
            else:
                Code01_PursuitArtifacts2.addEdge(ebcc1, ebcc2, w)
                Code01_PursuitArtifacts2.addEdge(ebcc2, ebcc1, w)
            i = jcast('int', (i + 1))

    @staticmethod
    def check(u, fa, ok):
        u = jcast('int', u)
        fa = jcast('int', fa)
        ok = jcast('boolean', ok)
        ok = jcast('boolean', (ok | (Code01_PursuitArtifacts2.val[u] > 0)))
        if (u == Code01_PursuitArtifacts2.t):
            return jcast('boolean', ok)
        e = jcast('int', Code01_PursuitArtifacts2.head[u])
        while (e > 0):
            v = jcast('int', Code01_PursuitArtifacts2.to[e])
            w = jcast('int', Code01_PursuitArtifacts2.weight[e])
            if (v != fa):
                if Code01_PursuitArtifacts2.check(v, u, (ok or (w > 0))):
                    return jcast('boolean', True)
            e = jcast('int', Code01_PursuitArtifacts2.nxt[e])
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        in_ = Code01_PursuitArtifacts2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_PursuitArtifacts2.cntg = jcast('int', 1)
        Code01_PursuitArtifacts2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_PursuitArtifacts2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_PursuitArtifacts2.m):
            jset(Code01_PursuitArtifacts2.a, i, jcall(in_, 'nextInt'))
            jset(Code01_PursuitArtifacts2.b, i, jcall(in_, 'nextInt'))
            jset(Code01_PursuitArtifacts2.c, i, jcall(in_, 'nextInt'))
            Code01_PursuitArtifacts2.addEdge(Code01_PursuitArtifacts2.a[i], Code01_PursuitArtifacts2.b[i], 0)
            Code01_PursuitArtifacts2.addEdge(Code01_PursuitArtifacts2.b[i], Code01_PursuitArtifacts2.a[i], 0)
            i = jcast('int', (i + 1))
        Code01_PursuitArtifacts2.tarjan(1, 0)
        Code01_PursuitArtifacts2.condense()
        Code01_PursuitArtifacts2.s = jcast('int', jcall(in_, 'nextInt'))
        Code01_PursuitArtifacts2.t = jcast('int', jcall(in_, 'nextInt'))
        Code01_PursuitArtifacts2.s = jcast('int', Code01_PursuitArtifacts2.belong[Code01_PursuitArtifacts2.s])
        Code01_PursuitArtifacts2.t = jcast('int', Code01_PursuitArtifacts2.belong[Code01_PursuitArtifacts2.t])
        if Code01_PursuitArtifacts2.check(Code01_PursuitArtifacts2.s, 0, False):
            jcall(out, 'println', 'YES')
        else:
            jcall(out, 'println', 'NO')
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
            raise TypeError("No matching overload for Code01_PursuitArtifacts2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_PursuitArtifacts2.MAXN = jcast('int', 300001)
Code01_PursuitArtifacts2.MAXM = jcast('int', 300001)
Code01_PursuitArtifacts2.n = jcast('int', 0)
Code01_PursuitArtifacts2.m = jcast('int', 0)
Code01_PursuitArtifacts2.s = jcast('int', 0)
Code01_PursuitArtifacts2.t = jcast('int', 0)
Code01_PursuitArtifacts2.a = jarray('int', [Code01_PursuitArtifacts2.MAXM])
Code01_PursuitArtifacts2.b = jarray('int', [Code01_PursuitArtifacts2.MAXM])
Code01_PursuitArtifacts2.c = jarray('int', [Code01_PursuitArtifacts2.MAXM])
Code01_PursuitArtifacts2.head = jarray('int', [Code01_PursuitArtifacts2.MAXN])
Code01_PursuitArtifacts2.nxt = jarray('int', [jcast('int', (Code01_PursuitArtifacts2.MAXM << (1 & 31)))])
Code01_PursuitArtifacts2.to = jarray('int', [jcast('int', (Code01_PursuitArtifacts2.MAXM << (1 & 31)))])
Code01_PursuitArtifacts2.weight = jarray('int', [jcast('int', (Code01_PursuitArtifacts2.MAXM << (1 & 31)))])
Code01_PursuitArtifacts2.cntg = jcast('int', 0)
Code01_PursuitArtifacts2.dfn = jarray('int', [Code01_PursuitArtifacts2.MAXN])
Code01_PursuitArtifacts2.low = jarray('int', [Code01_PursuitArtifacts2.MAXN])
Code01_PursuitArtifacts2.cntd = jcast('int', 0)
Code01_PursuitArtifacts2.sta = jarray('int', [Code01_PursuitArtifacts2.MAXN])
Code01_PursuitArtifacts2.top = jcast('int', 0)
Code01_PursuitArtifacts2.belong = jarray('int', [Code01_PursuitArtifacts2.MAXN])
Code01_PursuitArtifacts2.val = jarray('int', [Code01_PursuitArtifacts2.MAXN])
Code01_PursuitArtifacts2.ebccCnt = jcast('int', 0)

if __name__ == '__main__':
    Code01_PursuitArtifacts2.main([])
