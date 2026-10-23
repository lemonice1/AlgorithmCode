# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 只能一个方向，Python版
# 给定一张无向图，一共n个点、m条边，图上可能有多个连通区
# 给定q条要求，格式 x y : 从点x出发，要求可以去往点y
# 你必须把每条无向边变成有向边，也就是每条边确定唯一的方向
# 如果改造后能满足所有要求，打印"Yes"，如果不存在方案，打印"No"
# 1 <= n、m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF555E
# 测试链接 : https://codeforces.com/problemset/problem/555/E
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_OneDirection1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'ebccCnt': 'ebccCnt', 'block': 'block', 'dep': 'dep', 'stjump': 'stjump', 'vis': 'vis', 'upCnt': 'upCnt', 'downCnt': 'downCnt'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
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
    ebccCnt = 0
    block = None
    dep = None
    stjump = None
    vis = None
    upCnt = None
    downCnt = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_OneDirection1.nxt, ((_java_obj_1 := Code06_OneDirection1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_OneDirection1.head[u])
        Code06_OneDirection1.to[Code06_OneDirection1.cntg] = jcast('int', v)
        Code06_OneDirection1.head[u] = jcast('int', Code06_OneDirection1.cntg)

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code06_OneDirection1.dfn, u, jset(Code06_OneDirection1.low, u, ((_java_obj_4 := Code06_OneDirection1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code06_OneDirection1.sta, ((_java_obj_7 := Code06_OneDirection1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code06_OneDirection1.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code06_OneDirection1.to[e])
                if (Code06_OneDirection1.dfn[v] == 0):
                    Code06_OneDirection1.tarjan(v, e)
                    jset(Code06_OneDirection1.low, u, jstatic('Math', 'min', Code06_OneDirection1.low[u], Code06_OneDirection1.low[v]))
                else:
                    jset(Code06_OneDirection1.low, u, jstatic('Math', 'min', Code06_OneDirection1.low[u], Code06_OneDirection1.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code06_OneDirection1.nxt[e])
        if (Code06_OneDirection1.dfn[u] == Code06_OneDirection1.low[u]):
            Code06_OneDirection1.ebccCnt = jcast('int', (Code06_OneDirection1.ebccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code06_OneDirection1.sta[((_java_obj_11 := Code06_OneDirection1), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code06_OneDirection1.belong[pop] = jcast('int', Code06_OneDirection1.ebccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code06_OneDirection1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_OneDirection1.ebccCnt):
            Code06_OneDirection1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_OneDirection1.m):
            ebcc1 = jcast('int', Code06_OneDirection1.belong[Code06_OneDirection1.a[i]])
            ebcc2 = jcast('int', Code06_OneDirection1.belong[Code06_OneDirection1.b[i]])
            if (ebcc1 != ebcc2):
                Code06_OneDirection1.addEdge(ebcc1, ebcc2)
                Code06_OneDirection1.addEdge(ebcc2, ebcc1)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, fa, bid):
        u = jcast('int', u)
        fa = jcast('int', fa)
        bid = jcast('int', bid)
        Code06_OneDirection1.block[u] = jcast('int', bid)
        Code06_OneDirection1.dep[u] = jcast('int', jcast('int', jadd(Code06_OneDirection1.dep[fa], 1)))
        jset(Code06_OneDirection1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code06_OneDirection1.MAXP):
            jset(Code06_OneDirection1.stjump[u], p, Code06_OneDirection1.stjump[Code06_OneDirection1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code06_OneDirection1.head[u])
        while (e > 0):
            v = jcast('int', Code06_OneDirection1.to[e])
            if (v != fa):
                Code06_OneDirection1.dfs(v, u, bid)
            e = jcast('int', Code06_OneDirection1.nxt[e])

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code06_OneDirection1.dep[a] < Code06_OneDirection1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code06_OneDirection1.MAXP - 1)))
        while (p >= 0):
            if (Code06_OneDirection1.dep[Code06_OneDirection1.stjump[a][p]] >= Code06_OneDirection1.dep[b]):
                a = jcast('int', Code06_OneDirection1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code06_OneDirection1.MAXP - 1)))
        while (p >= 0):
            if (Code06_OneDirection1.stjump[a][p] != Code06_OneDirection1.stjump[b][p]):
                a = jcast('int', Code06_OneDirection1.stjump[a][p])
                b = jcast('int', Code06_OneDirection1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code06_OneDirection1.stjump[a][0])

    @staticmethod
    def check(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code06_OneDirection1.vis[u] = jcast('boolean', True)
        e = jcast('int', Code06_OneDirection1.head[u])
        while (e > 0):
            v = jcast('int', Code06_OneDirection1.to[e])
            if (v != fa):
                if (not Code06_OneDirection1.check(v, u)):
                    return jcast('boolean', False)
                Code06_OneDirection1.upCnt[u] = jcast('int', jcast('int', jadd(Code06_OneDirection1.upCnt[u], Code06_OneDirection1.upCnt[v])))
                Code06_OneDirection1.downCnt[u] = jcast('int', jcast('int', jadd(Code06_OneDirection1.downCnt[u], Code06_OneDirection1.downCnt[v])))
            e = jcast('int', Code06_OneDirection1.nxt[e])
        return jcast('boolean', ((Code06_OneDirection1.upCnt[u] == 0) or (Code06_OneDirection1.downCnt[u] == 0)))

    @staticmethod
    def main(args):
        in_ = Code06_OneDirection1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_OneDirection1.cntg = jcast('int', 1)
        Code06_OneDirection1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_OneDirection1.m = jcast('int', jcall(in_, 'nextInt'))
        Code06_OneDirection1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_OneDirection1.m):
            jset(Code06_OneDirection1.a, i, jcall(in_, 'nextInt'))
            jset(Code06_OneDirection1.b, i, jcall(in_, 'nextInt'))
            Code06_OneDirection1.addEdge(Code06_OneDirection1.a[i], Code06_OneDirection1.b[i])
            Code06_OneDirection1.addEdge(Code06_OneDirection1.b[i], Code06_OneDirection1.a[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_OneDirection1.n):
            if (Code06_OneDirection1.dfn[i] == 0):
                Code06_OneDirection1.tarjan(i, 0)
            i = jcast('int', (i + 1))
        Code06_OneDirection1.condense()
        i = jcast('int', 1)
        b = jcast('int', 0)
        while (i <= Code06_OneDirection1.ebccCnt):
            if (Code06_OneDirection1.block[i] == 0):
                Code06_OneDirection1.dfs(i, 0, (b := jcast('int', (b + (1)))))
            i = jcast('int', (i + 1))
        ans = jcast('boolean', True)
        i = jcast('int', 1)
        x = 0
        y = 0
        xylca = 0
        while (i <= Code06_OneDirection1.q):
            try:
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                x = jcast('int', Code06_OneDirection1.belong[x])
                y = jcast('int', Code06_OneDirection1.belong[y])
                if (Code06_OneDirection1.block[x] != Code06_OneDirection1.block[y]):
                    ans = jcast('boolean', False)
                    raise JBreak(None)
                xylca = jcast('int', Code06_OneDirection1.getLca(x, y))
                Code06_OneDirection1.upCnt[x] = jcast('int', (Code06_OneDirection1.upCnt[x] + 1))
                Code06_OneDirection1.upCnt[xylca] = jcast('int', (Code06_OneDirection1.upCnt[xylca] - 1))
                Code06_OneDirection1.downCnt[y] = jcast('int', (Code06_OneDirection1.downCnt[y] + 1))
                Code06_OneDirection1.downCnt[xylca] = jcast('int', (Code06_OneDirection1.downCnt[xylca] - 1))
            except JContinue as _java_control_14:
                if _java_control_14.label not in (None,):
                    raise
            except JBreak as _java_control_14:
                if _java_control_14.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if ans:
            i = jcast('int', 1)
            while (i <= Code06_OneDirection1.ebccCnt):
                try:
                    if ((not Code06_OneDirection1.vis[i]) and (not Code06_OneDirection1.check(i, 0))):
                        ans = jcast('boolean', False)
                        raise JBreak(None)
                except JContinue as _java_control_15:
                    if _java_control_15.label not in (None,):
                        raise
                except JBreak as _java_control_15:
                    if _java_control_15.label not in (None,):
                        raise
                    break
                i = jcast('int', (i + 1))
        jcall(out, 'println', ('Yes' if ans else 'No'))
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
            return jcast('int', self.buffer[((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]])

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
            raise TypeError("No matching overload for Code06_OneDirection1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_OneDirection1.MAXN = jcast('int', 200001)
Code06_OneDirection1.MAXM = jcast('int', 200001)
Code06_OneDirection1.MAXP = jcast('int', 20)
Code06_OneDirection1.n = jcast('int', 0)
Code06_OneDirection1.m = jcast('int', 0)
Code06_OneDirection1.q = jcast('int', 0)
Code06_OneDirection1.a = jarray('int', [Code06_OneDirection1.MAXM])
Code06_OneDirection1.b = jarray('int', [Code06_OneDirection1.MAXM])
Code06_OneDirection1.head = jarray('int', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.nxt = jarray('int', [jcast('int', (Code06_OneDirection1.MAXM << (1 & 31)))])
Code06_OneDirection1.to = jarray('int', [jcast('int', (Code06_OneDirection1.MAXM << (1 & 31)))])
Code06_OneDirection1.cntg = jcast('int', 0)
Code06_OneDirection1.dfn = jarray('int', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.low = jarray('int', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.cntd = jcast('int', 0)
Code06_OneDirection1.sta = jarray('int', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.top = jcast('int', 0)
Code06_OneDirection1.belong = jarray('int', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.ebccCnt = jcast('int', 0)
Code06_OneDirection1.block = jarray('int', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.dep = jarray('int', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.stjump = jarray('int', [Code06_OneDirection1.MAXN, Code06_OneDirection1.MAXP])
Code06_OneDirection1.vis = jarray('boolean', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.upCnt = jarray('int', [Code06_OneDirection1.MAXN])
Code06_OneDirection1.downCnt = jarray('int', [Code06_OneDirection1.MAXN])

if __name__ == '__main__':
    Code06_OneDirection1.main([])
