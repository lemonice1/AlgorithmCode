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

# 旗帜，Python版
# 一共n个旗子，第i号旗子有a[i]和b[i]两个可选位置
# 你需要决定每个旗子，到底放在两个可选位置中的哪一个
# 两面旗子之间的最小距离 d 越大，排列看起来就越美观
# 找到最美观的情况，即求出所有可能的 d 值中的最大值
# 2 <= n <= 10^4
# 1 <= a[i]、b[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/AT_arc069_d
# 测试链接 : https://atcoder.jp/contests/arc069/tasks/arc069_d
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Flags2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'k': 'k', 'a': 'a', 'b': 'b', 'arr': 'arr', 'ls': 'ls', 'rs': 'rs', 'root': 'root', 'cntt': 'cntt', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    n = 0
    k = 0
    a = None
    b = None
    # 所在的地点pos、决定的编号xid
    arr = None
    ls = None
    rs = None
    root = 0
    cntt = 0
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
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', Code02_Flags2.k)
        mid = 0
        ans = jcast('int', jcast('int', jadd(Code02_Flags2.k, 1)))
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code02_Flags2.arr[mid][0] >= num):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_Flags2.nxt, ((_java_obj_1 := Code02_Flags2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Flags2.head[u])
        Code02_Flags2.to[Code02_Flags2.cntg] = jcast('int', v)
        Code02_Flags2.head[u] = jcast('int', Code02_Flags2.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code02_Flags2.dfn, u, jset(Code02_Flags2.low, u, ((_java_obj_4 := Code02_Flags2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code02_Flags2.sta, ((_java_obj_7 := Code02_Flags2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code02_Flags2.head[u])
        while (e > 0):
            v = jcast('int', Code02_Flags2.to[e])
            if (Code02_Flags2.dfn[v] == 0):
                Code02_Flags2.tarjan(v)
                jset(Code02_Flags2.low, u, jstatic('Math', 'min', Code02_Flags2.low[u], Code02_Flags2.low[v]))
            else:
                if (Code02_Flags2.belong[v] == 0):
                    jset(Code02_Flags2.low, u, jstatic('Math', 'min', Code02_Flags2.low[u], Code02_Flags2.dfn[v]))
            e = jcast('int', Code02_Flags2.nxt[e])
        if (Code02_Flags2.dfn[u] == Code02_Flags2.low[u]):
            Code02_Flags2.sccCnt = jcast('int', (Code02_Flags2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code02_Flags2.sta[((_java_obj_10 := Code02_Flags2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code02_Flags2.belong[pop] = jcast('int', Code02_Flags2.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def other(i):
        i = jcast('int', i)
        return jcast('int', (jcast('int', jadd(i, Code02_Flags2.n)) if (i <= Code02_Flags2.n) else jcast('int', (i - Code02_Flags2.n))))

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', Code02_Flags2.other(Code02_Flags2.arr[l][1]))
        else:
            rt = jcast('int', ((_java_obj_13 := Code02_Flags2), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code02_Flags2.ls, rt, Code02_Flags2.build(l, mid))
            jset(Code02_Flags2.rs, rt, Code02_Flags2.build(jcast('int', jadd(mid, 1)), r))
            Code02_Flags2.addEdge(rt, Code02_Flags2.ls[rt])
            Code02_Flags2.addEdge(rt, Code02_Flags2.rs[rt])
        return jcast('int', rt)

    @staticmethod
    def xToRange(xid, jobl, jobr, l, r, i):
        xid = jcast('int', xid)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobl > jobr):
            return
        if ((jobl <= l) and (r <= jobr)):
            Code02_Flags2.addEdge(xid, i)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code02_Flags2.xToRange(xid, jobl, jobr, l, mid, Code02_Flags2.ls[i])
            if (jobr > mid):
                Code02_Flags2.xToRange(xid, jobl, jobr, jcast('int', jadd(mid, 1)), r, Code02_Flags2.rs[i])

    @staticmethod
    def buildGraph(d):
        d = jcast('int', d)
        Code02_Flags2.cntt = jcast('int', Code02_Flags2.k)
        Code02_Flags2.root = jcast('int', Code02_Flags2.build(1, Code02_Flags2.k))
        i = jcast('int', 1)
        while (i <= Code02_Flags2.k):
            pos = jcast('int', Code02_Flags2.arr[i][0])
            l = jcast('int', Code02_Flags2.kth(jcast('int', jadd(jcast('int', (pos - d)), 1))))
            r = jcast('int', jcast('int', (Code02_Flags2.kth(jcast('int', jadd(pos, d))) - 1)))
            x = jcast('int', Code02_Flags2.arr[i][1])
            Code02_Flags2.xToRange(x, l, jcast('int', (i - 1)), 1, Code02_Flags2.k, Code02_Flags2.root)
            Code02_Flags2.xToRange(x, jcast('int', jadd(i, 1)), r, 1, Code02_Flags2.k, Code02_Flags2.root)
            i = jcast('int', (i + 1))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code02_Flags2.cntt):
            jset(Code02_Flags2.head, i, jset(Code02_Flags2.dfn, i, jset(Code02_Flags2.belong, i, 0)))
            i = jcast('int', (i + 1))
        Code02_Flags2.cntt = jcast('int', jset(Code02_Flags2, 'cntg', jset(Code02_Flags2, 'cntd', jset(Code02_Flags2, 'top', jset(Code02_Flags2, 'sccCnt', 0)))))

    @staticmethod
    def check(d):
        d = jcast('int', d)
        Code02_Flags2.buildGraph(d)
        i = jcast('int', 1)
        while (i <= jcast('int', (Code02_Flags2.n << (1 & 31)))):
            if (Code02_Flags2.dfn[i] == 0):
                Code02_Flags2.tarjan(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code02_Flags2.n):
            try:
                if (Code02_Flags2.belong[i] == Code02_Flags2.belong[jcast('int', jadd(i, Code02_Flags2.n))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_16:
                if _java_control_16.label not in (None,):
                    raise
            except JBreak as _java_control_16:
                if _java_control_16.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        Code02_Flags2.clear()
        return jcast('boolean', check)

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code02_Flags2.n):
            jset(Code02_Flags2.arr[i], 0, Code02_Flags2.a[i])
            jset(Code02_Flags2.arr[i], 1, i)
            jset(Code02_Flags2.arr[jcast('int', jadd(i, Code02_Flags2.n))], 0, Code02_Flags2.b[i])
            jset(Code02_Flags2.arr[jcast('int', jadd(i, Code02_Flags2.n))], 1, jcast('int', jadd(i, Code02_Flags2.n)))
            i = jcast('int', (i + 1))
        Code02_Flags2.k = jcast('int', jcast('int', (Code02_Flags2.n << (1 & 31))))
        jstatic('Arrays', 'sort', Code02_Flags2.arr, 1, jcast('int', jadd(Code02_Flags2.k, 1)), (lambda x, y: ((x[0] - y[0]) if (x[0] != y[0]) else (x[1] - y[1]))))
        l = jcast('int', 0)
        r = jcast('int', Code02_Flags2.arr[Code02_Flags2.k][0])
        d = 0
        ans = jcast('int', 0)
        while (l <= r):
            d = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if Code02_Flags2.check(d):
                ans = jcast('int', d)
                l = jcast('int', jcast('int', jadd(d, 1)))
            else:
                r = jcast('int', jcast('int', (d - 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code02_Flags2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Flags2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_Flags2.n):
            jset(Code02_Flags2.a, i, jcall(in_, 'nextInt'))
            jset(Code02_Flags2.b, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        ans = jcast('int', Code02_Flags2.compute())
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
            return jcast('int', self.buffer[((_java_obj_17 := self), (_java_key_18 := 'ptr'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))), _java_old_19)[4]])

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
            raise TypeError("No matching overload for Code02_Flags2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Flags2.MAXN = jcast('int', 10001)
Code02_Flags2.MAXT = jcast('int', 100001)
Code02_Flags2.MAXE = jcast('int', 1000001)
Code02_Flags2.n = jcast('int', 0)
Code02_Flags2.k = jcast('int', 0)
Code02_Flags2.a = jarray('int', [Code02_Flags2.MAXN])
Code02_Flags2.b = jarray('int', [Code02_Flags2.MAXN])
Code02_Flags2.arr = jarray('int', [jcast('int', (Code02_Flags2.MAXN << (1 & 31))), 2])
Code02_Flags2.ls = jarray('int', [Code02_Flags2.MAXT])
Code02_Flags2.rs = jarray('int', [Code02_Flags2.MAXT])
Code02_Flags2.root = jcast('int', 0)
Code02_Flags2.cntt = jcast('int', 0)
Code02_Flags2.head = jarray('int', [Code02_Flags2.MAXT])
Code02_Flags2.nxt = jarray('int', [Code02_Flags2.MAXE])
Code02_Flags2.to = jarray('int', [Code02_Flags2.MAXE])
Code02_Flags2.cntg = jcast('int', 0)
Code02_Flags2.dfn = jarray('int', [Code02_Flags2.MAXT])
Code02_Flags2.low = jarray('int', [Code02_Flags2.MAXT])
Code02_Flags2.cntd = jcast('int', 0)
Code02_Flags2.sta = jarray('int', [Code02_Flags2.MAXT])
Code02_Flags2.top = jcast('int', 0)
Code02_Flags2.belong = jarray('int', [Code02_Flags2.MAXT])
Code02_Flags2.sccCnt = jcast('int', 0)

if __name__ == '__main__':
    Code02_Flags2.main([])
