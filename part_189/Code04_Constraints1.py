# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 约束条件，Python版
# 你需要构造长度为n的数组arr，每个元素的值在1~k之间，数组是非递减的
# 接下来给定m个约束条件，构造方案要满足所有约束条件，约束的格式如下
# 约束 1 i x   : arr[i] != x
# 约束 2 i j x : arr[i] + arr[j] <= x
# 约束 3 i j x : arr[i] + arr[j] >= x
# 如果不存在构造方案打印-1，存在方案就打印arr，任何一种方案都可以
# n、m <= 2 * 10^4
# 2 <= k <= 10
# 测试链接 : https://www.luogu.com.cn/problem/CF1697F
# 测试链接 : https://codeforces.com/problemset/problem/1697/F
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Constraints1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXK': 'MAXK', 'MAXT': 'MAXT', 't': 't', 'n': 'n', 'm': 'm', 'k': 'k', 'id': 'id', 'cntt': 'cntt', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt'}
    MAXN = 0
    MAXM = 0
    MAXK = 0
    MAXT = 0
    t = 0
    n = 0
    m = 0
    k = 0
    id = None
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
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_Constraints1.nxt, ((_java_obj_1 := Code04_Constraints1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Constraints1.head[u])
        Code04_Constraints1.to[Code04_Constraints1.cntg] = jcast('int', v)
        Code04_Constraints1.head[u] = jcast('int', Code04_Constraints1.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code04_Constraints1.dfn, u, jset(Code04_Constraints1.low, u, ((_java_obj_4 := Code04_Constraints1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code04_Constraints1.sta, ((_java_obj_7 := Code04_Constraints1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code04_Constraints1.head[u])
        while (e > 0):
            v = jcast('int', Code04_Constraints1.to[e])
            if (Code04_Constraints1.dfn[v] == 0):
                Code04_Constraints1.tarjan(v)
                jset(Code04_Constraints1.low, u, jstatic('Math', 'min', Code04_Constraints1.low[u], Code04_Constraints1.low[v]))
            else:
                if (Code04_Constraints1.belong[v] == 0):
                    jset(Code04_Constraints1.low, u, jstatic('Math', 'min', Code04_Constraints1.low[u], Code04_Constraints1.dfn[v]))
            e = jcast('int', Code04_Constraints1.nxt[e])
        if (Code04_Constraints1.dfn[u] == Code04_Constraints1.low[u]):
            Code04_Constraints1.sccCnt = jcast('int', (Code04_Constraints1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code04_Constraints1.sta[((_java_obj_10 := Code04_Constraints1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code04_Constraints1.belong[pop] = jcast('int', Code04_Constraints1.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def prepare():
        Code04_Constraints1.cntg = jcast('int', jset(Code04_Constraints1, 'cntd', jset(Code04_Constraints1, 'sccCnt', 0)))
        i = jcast('int', 1)
        while (i <= Code04_Constraints1.cntt):
            jset(Code04_Constraints1.head, i, jset(Code04_Constraints1.dfn, i, jset(Code04_Constraints1.low, i, jset(Code04_Constraints1.belong, i, 0))))
            i = jcast('int', (i + 1))
        # 每个假设分配节点编号
        Code04_Constraints1.cntt = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Constraints1.n):
            v = jcast('int', 1)
            while (v <= jcast('int', jadd(Code04_Constraints1.k, 1))):
                jset(Code04_Constraints1.id[i][v], 0, ((_java_obj_13 := Code04_Constraints1), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
                jset(Code04_Constraints1.id[i][v], 1, ((_java_obj_16 := Code04_Constraints1), (_java_key_17 := 'cntt'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3])
                v = jcast('int', (v + 1))
            i = jcast('int', (i + 1))
        # 天然成立
        i = jcast('int', 1)
        while (i <= Code04_Constraints1.n):
            v = jcast('int', 1)
            while (v <= Code04_Constraints1.k):
                Code04_Constraints1.addEdge(Code04_Constraints1.id[i][v][0], Code04_Constraints1.id[i][jcast('int', jadd(v, 1))][0])
                Code04_Constraints1.addEdge(Code04_Constraints1.id[i][jcast('int', jadd(v, 1))][1], Code04_Constraints1.id[i][v][1])
                v = jcast('int', (v + 1))
            i = jcast('int', (i + 1))
        # 数组非递减
        i = jcast('int', 1)
        while (i < Code04_Constraints1.n):
            v = jcast('int', 1)
            while (v <= Code04_Constraints1.k):
                Code04_Constraints1.addEdge(Code04_Constraints1.id[jcast('int', jadd(i, 1))][v][0], Code04_Constraints1.id[i][v][0])
                Code04_Constraints1.addEdge(Code04_Constraints1.id[i][v][1], Code04_Constraints1.id[jcast('int', jadd(i, 1))][v][1])
                v = jcast('int', (v + 1))
            i = jcast('int', (i + 1))
        # 每个位置的值在[1, k]范围
        # 规避错误假设
        # 强连通分量解决2-SAT问题的特性，永远选择拓扑序靠后的假设
        # (值 < 1) -> (值 >= 1)，推出矛盾固然不可行，如果无矛盾，会以后者为准
        # (值 >= k+1) -> (值 < k+1)，推出矛盾固然不可行，如果无矛盾，会以后者为准
        i = jcast('int', 1)
        while (i <= Code04_Constraints1.n):
            Code04_Constraints1.addEdge(Code04_Constraints1.id[i][1][0], Code04_Constraints1.id[i][1][1])
            Code04_Constraints1.addEdge(Code04_Constraints1.id[i][jcast('int', jadd(Code04_Constraints1.k, 1))][1], Code04_Constraints1.id[i][jcast('int', jadd(Code04_Constraints1.k, 1))][0])
            i = jcast('int', (i + 1))

    @staticmethod
    def notEqual(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        Code04_Constraints1.addEdge(Code04_Constraints1.id[i][x][1], Code04_Constraints1.id[i][jcast('int', jadd(x, 1))][1])
        Code04_Constraints1.addEdge(Code04_Constraints1.id[i][jcast('int', jadd(x, 1))][0], Code04_Constraints1.id[i][x][0])

    @staticmethod
    def lessEqual(i, j, x):
        i = jcast('int', i)
        j = jcast('int', j)
        x = jcast('int', x)
        w = jcast('int', 1)
        while (w <= Code04_Constraints1.k):
            if (w >= x):
                Code04_Constraints1.notEqual(i, w)
            else:
                if (jcast('int', jadd(jcast('int', (x - w)), 1)) <= Code04_Constraints1.k):
                    Code04_Constraints1.addEdge(Code04_Constraints1.id[i][w][1], Code04_Constraints1.id[j][jcast('int', jadd(jcast('int', (x - w)), 1))][0])
                    Code04_Constraints1.addEdge(Code04_Constraints1.id[j][jcast('int', jadd(jcast('int', (x - w)), 1))][1], Code04_Constraints1.id[i][w][0])
            w = jcast('int', (w + 1))

    @staticmethod
    def moreEqual(i, j, x):
        i = jcast('int', i)
        j = jcast('int', j)
        x = jcast('int', x)
        w = jcast('int', 1)
        while (w <= Code04_Constraints1.k):
            if (w <= jcast('int', (jcast('int', (x - Code04_Constraints1.k)) - 1))):
                Code04_Constraints1.notEqual(i, w)
            else:
                if (jcast('int', (x - w)) > 1):
                    Code04_Constraints1.addEdge(Code04_Constraints1.id[i][jcast('int', jadd(w, 1))][0], Code04_Constraints1.id[j][jcast('int', (x - w))][1])
                    Code04_Constraints1.addEdge(Code04_Constraints1.id[j][jcast('int', (x - w))][0], Code04_Constraints1.id[i][jcast('int', jadd(w, 1))][1])
            w = jcast('int', (w + 1))

    @staticmethod
    def main(args):
        in_ = Code04_Constraints1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Constraints1.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code04_Constraints1.t):
            try:
                Code04_Constraints1.n = jcast('int', jcall(in_, 'nextInt'))
                Code04_Constraints1.m = jcast('int', jcall(in_, 'nextInt'))
                Code04_Constraints1.k = jcast('int', jcall(in_, 'nextInt'))
                Code04_Constraints1.prepare()
                i = jcast('int', 1)
                op = 0
                x = 0
                y = 0
                v = 0
                while (i <= Code04_Constraints1.m):
                    op = jcast('int', jcall(in_, 'nextInt'))
                    if (op == 1):
                        x = jcast('int', jcall(in_, 'nextInt'))
                        v = jcast('int', jcall(in_, 'nextInt'))
                        Code04_Constraints1.notEqual(x, v)
                    else:
                        if (op == 2):
                            x = jcast('int', jcall(in_, 'nextInt'))
                            y = jcast('int', jcall(in_, 'nextInt'))
                            v = jcast('int', jcall(in_, 'nextInt'))
                            Code04_Constraints1.lessEqual(x, y, v)
                            tmp = jcast('int', x)
                            x = jcast('int', y)
                            y = jcast('int', tmp)
                            Code04_Constraints1.lessEqual(x, y, v)
                        else:
                            x = jcast('int', jcall(in_, 'nextInt'))
                            y = jcast('int', jcall(in_, 'nextInt'))
                            v = jcast('int', jcall(in_, 'nextInt'))
                            Code04_Constraints1.moreEqual(x, y, v)
                            tmp = jcast('int', x)
                            x = jcast('int', y)
                            y = jcast('int', tmp)
                            Code04_Constraints1.moreEqual(x, y, v)
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= Code04_Constraints1.cntt):
                    if (Code04_Constraints1.dfn[i] == 0):
                        Code04_Constraints1.tarjan(i)
                    i = jcast('int', (i + 1))
                check = jcast('boolean', True)
                i = jcast('int', 1)
                while (i <= Code04_Constraints1.n):
                    try:
                        v = jcast('int', 1)
                        while (v <= jcast('int', jadd(Code04_Constraints1.k, 1))):
                            try:
                                if (Code04_Constraints1.belong[Code04_Constraints1.id[i][v][0]] == Code04_Constraints1.belong[Code04_Constraints1.id[i][v][1]]):
                                    check = jcast('boolean', False)
                                    raise JBreak(None)
                            except JContinue as _java_control_21:
                                if _java_control_21.label not in (None,):
                                    raise
                            except JBreak as _java_control_21:
                                if _java_control_21.label not in (None,):
                                    raise
                                break
                            v = jcast('int', (v + 1))
                        if (not check):
                            raise JBreak(None)
                    except JContinue as _java_control_20:
                        if _java_control_20.label not in (None,):
                            raise
                    except JBreak as _java_control_20:
                        if _java_control_20.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
                if check:
                    i = jcast('int', 1)
                    while (i <= Code04_Constraints1.n):
                        try:
                            v = jcast('int', Code04_Constraints1.k)
                            while (v >= 1):
                                try:
                                    if (Code04_Constraints1.belong[Code04_Constraints1.id[i][v][1]] < Code04_Constraints1.belong[Code04_Constraints1.id[i][v][0]]):
                                        jcall(out, 'print', jadd(v, ' '))
                                        raise JBreak(None)
                                except JContinue as _java_control_23:
                                    if _java_control_23.label not in (None,):
                                        raise
                                except JBreak as _java_control_23:
                                    if _java_control_23.label not in (None,):
                                        raise
                                    break
                                v = jcast('int', (v - 1))
                        except JContinue as _java_control_22:
                            if _java_control_22.label not in (None,):
                                raise
                        except JBreak as _java_control_22:
                            if _java_control_22.label not in (None,):
                                raise
                            break
                        i = jcast('int', (i + 1))
                    jcall(out, 'println')
                else:
                    jcall(out, 'println', jcast('int', (-1)))
            except JContinue as _java_control_19:
                if _java_control_19.label not in (None,):
                    raise
            except JBreak as _java_control_19:
                if _java_control_19.label not in (None,):
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
            return jcast('int', self.buffer[((_java_obj_24 := self), (_java_key_25 := 'ptr'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))), _java_old_26)[4]])

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
            raise TypeError("No matching overload for Code04_Constraints1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Constraints1.MAXN = jcast('int', 20001)
Code04_Constraints1.MAXM = jcast('int', 2000001)
Code04_Constraints1.MAXK = jcast('int', 12)
Code04_Constraints1.MAXT = jcast('int', jcast('int', (jcast('int', (Code04_Constraints1.MAXN * Code04_Constraints1.MAXK)) * 2)))
Code04_Constraints1.t = jcast('int', 0)
Code04_Constraints1.n = jcast('int', 0)
Code04_Constraints1.m = jcast('int', 0)
Code04_Constraints1.k = jcast('int', 0)
Code04_Constraints1.id = jarray('int', [Code04_Constraints1.MAXN, Code04_Constraints1.MAXK, 2])
Code04_Constraints1.cntt = jcast('int', 0)
Code04_Constraints1.head = jarray('int', [Code04_Constraints1.MAXT])
Code04_Constraints1.nxt = jarray('int', [Code04_Constraints1.MAXM])
Code04_Constraints1.to = jarray('int', [Code04_Constraints1.MAXM])
Code04_Constraints1.cntg = jcast('int', 0)
Code04_Constraints1.dfn = jarray('int', [Code04_Constraints1.MAXT])
Code04_Constraints1.low = jarray('int', [Code04_Constraints1.MAXT])
Code04_Constraints1.cntd = jcast('int', 0)
Code04_Constraints1.sta = jarray('int', [Code04_Constraints1.MAXT])
Code04_Constraints1.top = jcast('int', 0)
Code04_Constraints1.belong = jarray('int', [Code04_Constraints1.MAXT])
Code04_Constraints1.sccCnt = jcast('int', 0)

if __name__ == '__main__':
    Code04_Constraints1.main([])
