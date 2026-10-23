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

# 炸弹，Python版
# 一共有n个炸弹，所有炸弹排成一条直线，给定每个炸弹的坐标xi、爆炸半径ri
# 炸弹A引爆时，如果炸弹B在其影响范围里，那么炸弹B也会引爆，进而引发一连串的爆炸
# 炸弹i如果作为初始引爆的炸弹，最终会引爆多少个炸弹记为query(i)
# 计算i = 1 2 .. n时，i * query(i)的累加和，答案对 1000000007 取余
# 1 <= n <= 5 * 10^5
# -(10^18) <= xi <= +(10^18)，题目依次输入的坐标保证严格递增
# 0 <= ri <= 2 * 10^18
# 测试链接 : https://www.luogu.com.cn/problem/P5025
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Bomb1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'INF': 'INF', 'MOD': 'MOD', 'n': 'n', 'location': 'location', 'radius': 'radius', 'a': 'a', 'b': 'b', 'cnte': 'cnte', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'rangel': 'rangel', 'ranger': 'ranger', 'ls': 'ls', 'rs': 'rs', 'root': 'root', 'cntt': 'cntt', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'mostl': 'mostl', 'mostr': 'mostr', 'sccCnt': 'sccCnt', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    INF = 0
    MOD = 0
    n = 0
    location = None
    radius = None
    a = None
    b = None
    cnte = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    rangel = None
    ranger = None
    ls = None
    rs = None
    root = 0
    cntt = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    mostl = None
    mostr = None
    sccCnt = 0
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
        jset(Code05_Bomb1.stack[Code05_Bomb1.stacksize], 0, u)
        jset(Code05_Bomb1.stack[Code05_Bomb1.stacksize], 1, status)
        jset(Code05_Bomb1.stack[Code05_Bomb1.stacksize], 2, e)
        Code05_Bomb1.stacksize = jcast('int', (Code05_Bomb1.stacksize + 1))

    @staticmethod
    def pop():
        Code05_Bomb1.stacksize = jcast('int', (Code05_Bomb1.stacksize - 1))
        Code05_Bomb1.u = jcast('int', Code05_Bomb1.stack[Code05_Bomb1.stacksize][0])
        Code05_Bomb1.status = jcast('int', Code05_Bomb1.stack[Code05_Bomb1.stacksize][1])
        Code05_Bomb1.e = jcast('int', Code05_Bomb1.stack[Code05_Bomb1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Bomb1.nxt, ((_java_obj_1 := Code05_Bomb1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Bomb1.head[u])
        Code05_Bomb1.to[Code05_Bomb1.cntg] = jcast('int', v)
        Code05_Bomb1.head[u] = jcast('int', Code05_Bomb1.cntg)

    @staticmethod
    def saveEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Bomb1.a, ((_java_obj_4 := Code05_Bomb1), (_java_key_5 := 'cnte'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)
        Code05_Bomb1.b[Code05_Bomb1.cnte] = jcast('int', v)

    @staticmethod
    def lower(num):
        num = jcast('long', num)
        l = jcast('int', 1)
        r = jcast('int', Code05_Bomb1.n)
        mid = 0
        ans = jcast('int', jcast('int', jadd(Code05_Bomb1.n, 1)))
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code05_Bomb1.location[mid] >= num):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_7 := Code05_Bomb1), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code05_Bomb1.ls, rt, Code05_Bomb1.build(l, mid))
            jset(Code05_Bomb1.rs, rt, Code05_Bomb1.build(jcast('int', jadd(mid, 1)), r))
            Code05_Bomb1.addEdge(Code05_Bomb1.ls[rt], rt)
            Code05_Bomb1.addEdge(Code05_Bomb1.rs[rt], rt)
            Code05_Bomb1.saveEdge(Code05_Bomb1.ls[rt], rt)
            Code05_Bomb1.saveEdge(Code05_Bomb1.rs[rt], rt)
        Code05_Bomb1.rangel[rt] = jcast('int', l)
        Code05_Bomb1.ranger[rt] = jcast('int', r)
        return jcast('int', rt)

    @staticmethod
    def rangeToX(jobl, jobr, jobx, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_Bomb1.addEdge(i, jobx)
            Code05_Bomb1.saveEdge(i, jobx)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code05_Bomb1.rangeToX(jobl, jobr, jobx, l, mid, Code05_Bomb1.ls[i])
            if (jobr > mid):
                Code05_Bomb1.rangeToX(jobl, jobr, jobx, jcast('int', jadd(mid, 1)), r, Code05_Bomb1.rs[i])

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code05_Bomb1.dfn, u, jset(Code05_Bomb1.low, u, ((_java_obj_10 := Code05_Bomb1), (_java_key_11 := 'cntd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3]))
        jset(Code05_Bomb1.sta, ((_java_obj_13 := Code05_Bomb1), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], u)
        e = jcast('int', Code05_Bomb1.head[u])
        while (e > 0):
            v = jcast('int', Code05_Bomb1.to[e])
            if (Code05_Bomb1.dfn[v] == 0):
                Code05_Bomb1.tarjan1(v)
                jset(Code05_Bomb1.low, u, jstatic('Math', 'min', Code05_Bomb1.low[u], Code05_Bomb1.low[v]))
            else:
                if (Code05_Bomb1.belong[v] == 0):
                    jset(Code05_Bomb1.low, u, jstatic('Math', 'min', Code05_Bomb1.low[u], Code05_Bomb1.dfn[v]))
            e = jcast('int', Code05_Bomb1.nxt[e])
        if (Code05_Bomb1.dfn[u] == Code05_Bomb1.low[u]):
            Code05_Bomb1.sccCnt = jcast('int', (Code05_Bomb1.sccCnt + 1))
            Code05_Bomb1.mostl[Code05_Bomb1.sccCnt] = jcast('int', Code05_Bomb1.INF)
            Code05_Bomb1.mostr[Code05_Bomb1.sccCnt] = jcast('int', jcast('int', (-Code05_Bomb1.INF)))
            pop = 0
            while True:
                pop = jcast('int', Code05_Bomb1.sta[((_java_obj_16 := Code05_Bomb1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (-1)))), _java_old_18)[4]])
                Code05_Bomb1.belong[pop] = jcast('int', Code05_Bomb1.sccCnt)
                jset(Code05_Bomb1.mostl, Code05_Bomb1.sccCnt, jstatic('Math', 'min', Code05_Bomb1.mostl[Code05_Bomb1.sccCnt], Code05_Bomb1.rangel[pop]))
                jset(Code05_Bomb1.mostr, Code05_Bomb1.sccCnt, jstatic('Math', 'max', Code05_Bomb1.mostr[Code05_Bomb1.sccCnt], Code05_Bomb1.ranger[pop]))
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code05_Bomb1.stacksize = jcast('int', 0)
        Code05_Bomb1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_Bomb1.stacksize > 0):
            Code05_Bomb1.pop()
            if (Code05_Bomb1.status == jcast('int', (-1))):
                jset(Code05_Bomb1.dfn, Code05_Bomb1.u, jset(Code05_Bomb1.low, Code05_Bomb1.u, ((_java_obj_19 := Code05_Bomb1), (_java_key_20 := 'cntd'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3]))
                jset(Code05_Bomb1.sta, ((_java_obj_22 := Code05_Bomb1), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], Code05_Bomb1.u)
                Code05_Bomb1.e = jcast('int', Code05_Bomb1.head[Code05_Bomb1.u])
            else:
                v = jcast('int', Code05_Bomb1.to[Code05_Bomb1.e])
                if (Code05_Bomb1.status == 0):
                    jset(Code05_Bomb1.low, Code05_Bomb1.u, jstatic('Math', 'min', Code05_Bomb1.low[Code05_Bomb1.u], Code05_Bomb1.low[v]))
                if ((Code05_Bomb1.status == 1) and (Code05_Bomb1.belong[v] == 0)):
                    jset(Code05_Bomb1.low, Code05_Bomb1.u, jstatic('Math', 'min', Code05_Bomb1.low[Code05_Bomb1.u], Code05_Bomb1.dfn[v]))
                Code05_Bomb1.e = jcast('int', Code05_Bomb1.nxt[Code05_Bomb1.e])
            if (Code05_Bomb1.e != 0):
                v = jcast('int', Code05_Bomb1.to[Code05_Bomb1.e])
                if (Code05_Bomb1.dfn[v] == 0):
                    Code05_Bomb1.push(Code05_Bomb1.u, 0, Code05_Bomb1.e)
                    Code05_Bomb1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_Bomb1.push(Code05_Bomb1.u, 1, Code05_Bomb1.e)
            else:
                if (Code05_Bomb1.dfn[Code05_Bomb1.u] == Code05_Bomb1.low[Code05_Bomb1.u]):
                    Code05_Bomb1.sccCnt = jcast('int', (Code05_Bomb1.sccCnt + 1))
                    Code05_Bomb1.mostl[Code05_Bomb1.sccCnt] = jcast('int', Code05_Bomb1.INF)
                    Code05_Bomb1.mostr[Code05_Bomb1.sccCnt] = jcast('int', jcast('int', (-Code05_Bomb1.INF)))
                    pop = 0
                    while True:
                        pop = jcast('int', Code05_Bomb1.sta[((_java_obj_25 := Code05_Bomb1), (_java_key_26 := 'top'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (-1)))), _java_old_27)[4]])
                        Code05_Bomb1.belong[pop] = jcast('int', Code05_Bomb1.sccCnt)
                        jset(Code05_Bomb1.mostl, Code05_Bomb1.sccCnt, jstatic('Math', 'min', Code05_Bomb1.mostl[Code05_Bomb1.sccCnt], Code05_Bomb1.rangel[pop]))
                        jset(Code05_Bomb1.mostr, Code05_Bomb1.sccCnt, jstatic('Math', 'max', Code05_Bomb1.mostr[Code05_Bomb1.sccCnt], Code05_Bomb1.ranger[pop]))
                        if not ((pop != Code05_Bomb1.u)):
                            break

    @staticmethod
    def condense():
        Code05_Bomb1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_Bomb1.sccCnt):
            Code05_Bomb1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Bomb1.cnte):
            scc1 = jcast('int', Code05_Bomb1.belong[Code05_Bomb1.a[i]])
            scc2 = jcast('int', Code05_Bomb1.belong[Code05_Bomb1.b[i]])
            if (scc1 != scc2):
                Code05_Bomb1.addEdge(scc1, scc2)
            i = jcast('int', (i + 1))

    @staticmethod
    def dpOnDAG():
        u = jcast('int', Code05_Bomb1.sccCnt)
        while (u > 0):
            e = jcast('int', Code05_Bomb1.head[u])
            while (e > 0):
                v = jcast('int', Code05_Bomb1.to[e])
                jset(Code05_Bomb1.mostl, v, jstatic('Math', 'min', Code05_Bomb1.mostl[v], Code05_Bomb1.mostl[u]))
                jset(Code05_Bomb1.mostr, v, jstatic('Math', 'max', Code05_Bomb1.mostr[v], Code05_Bomb1.mostr[u]))
                e = jcast('int', Code05_Bomb1.nxt[e])
            u = jcast('int', (u - 1))

    @staticmethod
    def query(u):
        u = jcast('int', u)
        scc = jcast('int', Code05_Bomb1.belong[u])
        num = jcast('int', jcast('int', jadd(jcast('int', (Code05_Bomb1.mostr[scc] - Code05_Bomb1.mostl[scc])), 1)))
        return jcast('int', num)

    @staticmethod
    def main(args):
        in_ = Code05_Bomb1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Bomb1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Bomb1.cntt = jcast('int', Code05_Bomb1.n)
        i = jcast('int', 1)
        while (i <= Code05_Bomb1.n):
            jset(Code05_Bomb1.location, i, jcall(in_, 'nextLong'))
            jset(Code05_Bomb1.radius, i, jcall(in_, 'nextLong'))
            i = jcast('int', (i + 1))
        Code05_Bomb1.root = jcast('int', Code05_Bomb1.build(1, Code05_Bomb1.n))
        i = jcast('int', 1)
        while (i <= Code05_Bomb1.n):
            l = jcast('int', Code05_Bomb1.lower(jcast('long', (Code05_Bomb1.location[i] - Code05_Bomb1.radius[i]))))
            r = jcast('int', jcast('int', (Code05_Bomb1.lower(jcast('long', jadd(jcast('long', jadd(Code05_Bomb1.location[i], Code05_Bomb1.radius[i])), 1))) - 1)))
            Code05_Bomb1.rangeToX(l, r, i, 1, Code05_Bomb1.n, Code05_Bomb1.root)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Bomb1.cntt):
            if (Code05_Bomb1.dfn[i] == 0):
                # tarjan1(i);
                Code05_Bomb1.tarjan2(i)
            i = jcast('int', (i + 1))
        Code05_Bomb1.condense()
        Code05_Bomb1.dpOnDAG()
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code05_Bomb1.n):
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', (jcast('long', (1 * Code05_Bomb1.query(i))) * i)))), Code05_Bomb1.MOD)))
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_28 := self), (_java_key_29 := 'ptr'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))), _java_old_30)[4]])

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

        def nextLong(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('long', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('long', jcast('long', jadd(jcast('long', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('long', (jcast('long', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_Bomb1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Bomb1.MAXN = jcast('int', 500001)
Code05_Bomb1.MAXT = jcast('int', jcast('int', (Code05_Bomb1.MAXN * 5)))
Code05_Bomb1.MAXE = jcast('int', jcast('int', (Code05_Bomb1.MAXN * 20)))
Code05_Bomb1.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code05_Bomb1.MOD = jcast('int', 1000000007)
Code05_Bomb1.n = jcast('int', 0)
Code05_Bomb1.location = jarray('long', [Code05_Bomb1.MAXN])
Code05_Bomb1.radius = jarray('long', [Code05_Bomb1.MAXN])
Code05_Bomb1.a = jarray('int', [Code05_Bomb1.MAXE])
Code05_Bomb1.b = jarray('int', [Code05_Bomb1.MAXE])
Code05_Bomb1.cnte = jcast('int', 0)
Code05_Bomb1.head = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.nxt = jarray('int', [Code05_Bomb1.MAXE])
Code05_Bomb1.to = jarray('int', [Code05_Bomb1.MAXE])
Code05_Bomb1.cntg = jcast('int', 0)
Code05_Bomb1.rangel = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.ranger = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.ls = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.rs = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.root = jcast('int', 0)
Code05_Bomb1.cntt = jcast('int', 0)
Code05_Bomb1.dfn = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.low = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.cntd = jcast('int', 0)
Code05_Bomb1.sta = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.top = jcast('int', 0)
Code05_Bomb1.belong = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.mostl = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.mostr = jarray('int', [Code05_Bomb1.MAXT])
Code05_Bomb1.sccCnt = jcast('int', 0)
Code05_Bomb1.stack = jarray('int', [Code05_Bomb1.MAXT, 3])
Code05_Bomb1.u = jcast('int', 0)
Code05_Bomb1.status = jcast('int', 0)
Code05_Bomb1.e = jcast('int', 0)
Code05_Bomb1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code05_Bomb1.main([])
