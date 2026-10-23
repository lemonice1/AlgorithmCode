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

# 同谋者，Python版
# 一共n个人，编号1~n，分配每个人进入交流队或者保密队中的一个
# 交流队要求内部任意两人都认识，保密队要求内部任意两人都不认识
# 给定每人的认识列表，如果x的认识列表里有y，那么y的认识列表里有x
# 分配还要求交流队和保密队都不能为空，计算n个人分成两组的方法数
# 如果不存在任何方法，打印0
# 2 <= n <= 5000
# 所有认识列表的总人数 <= n * (n - 1)
# 测试链接 : https://www.luogu.com.cn/problem/P3513
# 测试链接 : https://loj.ac/p/2155
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Conspiracy2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXM': 'MAXM', 'n': 'n', 'k': 'k', 'x': 'x', 'know': 'know', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'team1': 'team1', 'team2': 'team2', 'cnt1': 'cnt1', 'cnt2': 'cnt2', 'other': 'other'}
    MAXN = 0
    MAXT = 0
    MAXM = 0
    n = 0
    k = 0
    x = 0
    know = None
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
    team1 = None
    team2 = None
    cnt1 = 0
    cnt2 = 0
    # 如果i在交流队
    # other[i] >= 1，表示i认识保密队中的人的编号
    # other[i] == 0，表示i不认识保密队中的所有人
    # other[i] == -1，表示i认识保密队中的人数，不止一个
    #
    # 如果i在保密队
    # other[i] >= 1，表示i不认识交流队中的人的编号
    # other[i] == 0，表示i认识交流队中的所有人
    # other[i] == -1，表示i不认识交流队中的人数，不止一个
    other = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Conspiracy2.nxt, ((_java_obj_1 := Code05_Conspiracy2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Conspiracy2.head[u])
        Code05_Conspiracy2.to[Code05_Conspiracy2.cntg] = jcast('int', v)
        Code05_Conspiracy2.head[u] = jcast('int', Code05_Conspiracy2.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code05_Conspiracy2.dfn, u, jset(Code05_Conspiracy2.low, u, ((_java_obj_4 := Code05_Conspiracy2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code05_Conspiracy2.sta, ((_java_obj_7 := Code05_Conspiracy2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code05_Conspiracy2.head[u])
        while (e > 0):
            v = jcast('int', Code05_Conspiracy2.to[e])
            if (Code05_Conspiracy2.dfn[v] == 0):
                Code05_Conspiracy2.tarjan(v)
                jset(Code05_Conspiracy2.low, u, jstatic('Math', 'min', Code05_Conspiracy2.low[u], Code05_Conspiracy2.low[v]))
            else:
                if (Code05_Conspiracy2.belong[v] == 0):
                    jset(Code05_Conspiracy2.low, u, jstatic('Math', 'min', Code05_Conspiracy2.low[u], Code05_Conspiracy2.dfn[v]))
            e = jcast('int', Code05_Conspiracy2.nxt[e])
        if (Code05_Conspiracy2.dfn[u] == Code05_Conspiracy2.low[u]):
            Code05_Conspiracy2.sccCnt = jcast('int', (Code05_Conspiracy2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code05_Conspiracy2.sta[((_java_obj_10 := Code05_Conspiracy2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code05_Conspiracy2.belong[pop] = jcast('int', Code05_Conspiracy2.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code05_Conspiracy2.n):
            if (Code05_Conspiracy2.belong[i] == Code05_Conspiracy2.belong[jcast('int', jadd(i, Code05_Conspiracy2.n))]):
                return jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Conspiracy2.n):
            if (Code05_Conspiracy2.belong[i] < Code05_Conspiracy2.belong[jcast('int', jadd(i, Code05_Conspiracy2.n))]):
                jset(Code05_Conspiracy2.team1, ((_java_obj_13 := Code05_Conspiracy2), (_java_key_14 := 'cnt1'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], i)
            else:
                jset(Code05_Conspiracy2.team2, ((_java_obj_16 := Code05_Conspiracy2), (_java_key_17 := 'cnt2'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], i)
            i = jcast('int', (i + 1))
        ans = jcast('int', (1 if ((Code05_Conspiracy2.cnt1 > 0) and (Code05_Conspiracy2.cnt2 > 0)) else 0))
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= Code05_Conspiracy2.cnt1):
            a = jcast('int', Code05_Conspiracy2.team1[i])
            j = jcast('int', 1)
            while (j <= Code05_Conspiracy2.cnt2):
                b = jcast('int', Code05_Conspiracy2.team2[j])
                if Code05_Conspiracy2.know[a][b]:
                    Code05_Conspiracy2.other[a] = jcast('int', (b if (Code05_Conspiracy2.other[a] == 0) else jcast('int', (-1))))
                else:
                    Code05_Conspiracy2.other[b] = jcast('int', (a if (Code05_Conspiracy2.other[b] == 0) else jcast('int', (-1))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        if (Code05_Conspiracy2.cnt1 > 1):
            i = jcast('int', 1)
            while (i <= Code05_Conspiracy2.cnt1):
                if (Code05_Conspiracy2.other[Code05_Conspiracy2.team1[i]] == 0):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
        if (Code05_Conspiracy2.cnt2 > 1):
            i = jcast('int', 1)
            while (i <= Code05_Conspiracy2.cnt2):
                if (Code05_Conspiracy2.other[Code05_Conspiracy2.team2[i]] == 0):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= Code05_Conspiracy2.cnt1):
            a = jcast('int', Code05_Conspiracy2.team1[i])
            j = jcast('int', 1)
            while (j <= Code05_Conspiracy2.cnt2):
                b = jcast('int', Code05_Conspiracy2.team2[j])
                if Code05_Conspiracy2.know[a][b]:
                    if ((Code05_Conspiracy2.other[a] == b) and (Code05_Conspiracy2.other[b] == 0)):
                        ans = jcast('int', (ans + 1))
                else:
                    if ((Code05_Conspiracy2.other[b] == a) and (Code05_Conspiracy2.other[a] == 0)):
                        ans = jcast('int', (ans + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code05_Conspiracy2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Conspiracy2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Conspiracy2.n):
            Code05_Conspiracy2.k = jcast('int', jcall(in_, 'nextInt'))
            j = jcast('int', 1)
            while (j <= Code05_Conspiracy2.k):
                Code05_Conspiracy2.x = jcast('int', jcall(in_, 'nextInt'))
                jset(Code05_Conspiracy2.know[i], Code05_Conspiracy2.x, True)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Conspiracy2.n):
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j <= Code05_Conspiracy2.n):
                if Code05_Conspiracy2.know[i][j]:
                    Code05_Conspiracy2.addEdge(jcast('int', jadd(i, Code05_Conspiracy2.n)), j)
                    Code05_Conspiracy2.addEdge(jcast('int', jadd(j, Code05_Conspiracy2.n)), i)
                else:
                    Code05_Conspiracy2.addEdge(i, jcast('int', jadd(j, Code05_Conspiracy2.n)))
                    Code05_Conspiracy2.addEdge(j, jcast('int', jadd(i, Code05_Conspiracy2.n)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code05_Conspiracy2.n << (1 & 31)))):
            if (Code05_Conspiracy2.dfn[i] == 0):
                Code05_Conspiracy2.tarjan(i)
            i = jcast('int', (i + 1))
        ans = jcast('int', Code05_Conspiracy2.compute())
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
            return jcast('int', self.buffer[((_java_obj_19 := self), (_java_key_20 := 'ptr'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]])

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
            raise TypeError("No matching overload for Code05_Conspiracy2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Conspiracy2.MAXN = jcast('int', 5001)
Code05_Conspiracy2.MAXT = jcast('int', jcast('int', (Code05_Conspiracy2.MAXN << (1 & 31))))
Code05_Conspiracy2.MAXM = jcast('int', jcast('int', (Code05_Conspiracy2.MAXN * Code05_Conspiracy2.MAXN)))
Code05_Conspiracy2.n = jcast('int', 0)
Code05_Conspiracy2.k = jcast('int', 0)
Code05_Conspiracy2.x = jcast('int', 0)
Code05_Conspiracy2.know = jarray('boolean', [Code05_Conspiracy2.MAXN, Code05_Conspiracy2.MAXN])
Code05_Conspiracy2.head = jarray('int', [Code05_Conspiracy2.MAXT])
Code05_Conspiracy2.nxt = jarray('int', [Code05_Conspiracy2.MAXM])
Code05_Conspiracy2.to = jarray('int', [Code05_Conspiracy2.MAXM])
Code05_Conspiracy2.cntg = jcast('int', 0)
Code05_Conspiracy2.dfn = jarray('int', [Code05_Conspiracy2.MAXT])
Code05_Conspiracy2.low = jarray('int', [Code05_Conspiracy2.MAXT])
Code05_Conspiracy2.cntd = jcast('int', 0)
Code05_Conspiracy2.sta = jarray('int', [Code05_Conspiracy2.MAXT])
Code05_Conspiracy2.top = jcast('int', 0)
Code05_Conspiracy2.belong = jarray('int', [Code05_Conspiracy2.MAXT])
Code05_Conspiracy2.sccCnt = jcast('int', 0)
Code05_Conspiracy2.team1 = jarray('int', [Code05_Conspiracy2.MAXN])
Code05_Conspiracy2.team2 = jarray('int', [Code05_Conspiracy2.MAXN])
Code05_Conspiracy2.cnt1 = jcast('int', 0)
Code05_Conspiracy2.cnt2 = jcast('int', 0)
Code05_Conspiracy2.other = jarray('int', [Code05_Conspiracy2.MAXN])

if __name__ == '__main__':
    Code05_Conspiracy2.main([])
