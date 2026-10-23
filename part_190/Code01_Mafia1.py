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

# 黑手党，Python版
# 一共n个点，m条无向边，每条边给定端点x、端点y、颜色c、破坏时间t
# 图中保证没有自环，你可以选择一些边作为摧毁边，剩下的边作为幸存边
# 摧毁的方式是并行的，所以摧毁耗时 = max(所有摧毁边的破坏时间)
# 要求任意两条摧毁边不能在图中相邻，任意两条同色的幸存边也不能相邻
# 满足要求的前提下，摧毁耗时想尽可能的小，请找到可行的摧毁边集
# 不存在方案打印"No"，存在方案打印"Yes"，然后依次打印如下内容
# 摧毁耗时、摧毁边集的大小、摧毁边集每条边的序号，任何一个方案皆可
# 1 <= n、m <= 5 * 10^4    1 <= c、t <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/CF587D
# 测试链接 : https://codeforces.com/problemset/problem/587/D
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Mafia1:
    __java_fields__ = {'MAXM': 'MAXM', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'm': 'm', 'k': 'k', 'maxt': 'maxt', 'cntt': 'cntt', 'arr': 'arr', 'destroyTime': 'destroyTime', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'group': 'group', 'gsiz': 'gsiz', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'ansTime': 'ansTime', 'ansSize': 'ansSize', 'ansArr': 'ansArr'}
    MAXM = 0
    MAXT = 0
    MAXE = 0
    n = 0
    m = 0
    k = 0
    maxt = 0
    cntt = 0
    # 边的序号、所属节点、边的颜色
    arr = None
    # 边的破坏时间
    destroyTime = None
    head = None
    nxt = None
    to = None
    cntg = 0
    group = None
    gsiz = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    ansTime = 0
    ansSize = 0
    ansArr = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_Mafia1.nxt, ((_java_obj_1 := Code01_Mafia1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_Mafia1.head[u])
        Code01_Mafia1.to[Code01_Mafia1.cntg] = jcast('int', v)
        Code01_Mafia1.head[u] = jcast('int', Code01_Mafia1.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code01_Mafia1.dfn, u, jset(Code01_Mafia1.low, u, ((_java_obj_4 := Code01_Mafia1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code01_Mafia1.sta, ((_java_obj_7 := Code01_Mafia1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code01_Mafia1.head[u])
        while (e > 0):
            v = jcast('int', Code01_Mafia1.to[e])
            if (Code01_Mafia1.dfn[v] == 0):
                Code01_Mafia1.tarjan(v)
                jset(Code01_Mafia1.low, u, jstatic('Math', 'min', Code01_Mafia1.low[u], Code01_Mafia1.low[v]))
            else:
                if (Code01_Mafia1.belong[v] == 0):
                    jset(Code01_Mafia1.low, u, jstatic('Math', 'min', Code01_Mafia1.low[u], Code01_Mafia1.dfn[v]))
            e = jcast('int', Code01_Mafia1.nxt[e])
        if (Code01_Mafia1.dfn[u] == Code01_Mafia1.low[u]):
            Code01_Mafia1.sccCnt = jcast('int', (Code01_Mafia1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code01_Mafia1.sta[((_java_obj_10 := Code01_Mafia1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code01_Mafia1.belong[pop] = jcast('int', Code01_Mafia1.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def other(i):
        i = jcast('int', i)
        return jcast('int', (jcast('int', jadd(i, Code01_Mafia1.m)) if (i <= Code01_Mafia1.m) else jcast('int', (i - Code01_Mafia1.m))))

    # 前后缀优化建图
    @staticmethod
    def groupLink():
        if (Code01_Mafia1.gsiz > 1):
            Code01_Mafia1.cntt = jcast('int', (Code01_Mafia1.cntt + 1))
            Code01_Mafia1.addEdge(Code01_Mafia1.cntt, Code01_Mafia1.other(Code01_Mafia1.group[1]))
            i = jcast('int', 2)
            while (i <= Code01_Mafia1.gsiz):
                Code01_Mafia1.cntt = jcast('int', (Code01_Mafia1.cntt + 1))
                Code01_Mafia1.addEdge(Code01_Mafia1.cntt, Code01_Mafia1.other(Code01_Mafia1.group[i]))
                Code01_Mafia1.addEdge(Code01_Mafia1.group[i], jcast('int', (Code01_Mafia1.cntt - 1)))
                Code01_Mafia1.addEdge(Code01_Mafia1.cntt, jcast('int', (Code01_Mafia1.cntt - 1)))
                i = jcast('int', (i + 1))
            Code01_Mafia1.cntt = jcast('int', (Code01_Mafia1.cntt + 1))
            Code01_Mafia1.addEdge(Code01_Mafia1.cntt, Code01_Mafia1.other(Code01_Mafia1.group[Code01_Mafia1.gsiz]))
            i = jcast('int', jcast('int', (Code01_Mafia1.gsiz - 1)))
            while (i >= 1):
                Code01_Mafia1.cntt = jcast('int', (Code01_Mafia1.cntt + 1))
                Code01_Mafia1.addEdge(Code01_Mafia1.cntt, Code01_Mafia1.other(Code01_Mafia1.group[i]))
                Code01_Mafia1.addEdge(Code01_Mafia1.group[i], jcast('int', (Code01_Mafia1.cntt - 1)))
                Code01_Mafia1.addEdge(Code01_Mafia1.cntt, jcast('int', (Code01_Mafia1.cntt - 1)))
                i = jcast('int', (i - 1))

    @staticmethod
    def buildGraph(limit):
        limit = jcast('int', limit)
        Code01_Mafia1.cntt = jcast('int', jcast('int', (Code01_Mafia1.m << (1 & 31))))
        i = jcast('int', 1)
        while (i <= Code01_Mafia1.m):
            if (Code01_Mafia1.destroyTime[i] > limit):
                Code01_Mafia1.addEdge(i, jcast('int', jadd(i, Code01_Mafia1.m)))
            i = jcast('int', (i + 1))
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code01_Mafia1.k):
            curx = jcast('int', Code01_Mafia1.arr[l][1])
            while ((jcast('int', jadd(r, 1)) <= Code01_Mafia1.k) and (curx == Code01_Mafia1.arr[jcast('int', jadd(r, 1))][1])):
                r = jcast('int', (r + 1))
            Code01_Mafia1.gsiz = jcast('int', 0)
            i = jcast('int', l)
            while (i <= r):
                jset(Code01_Mafia1.group, ((_java_obj_13 := Code01_Mafia1), (_java_key_14 := 'gsiz'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code01_Mafia1.arr[i][0])
                i = jcast('int', (i + 1))
            Code01_Mafia1.groupLink()
            l = jcast('int', (r := jcast('int', (r + (1)))))
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code01_Mafia1.k):
            curx = jcast('int', Code01_Mafia1.arr[l][1])
            curc = jcast('int', Code01_Mafia1.arr[l][2])
            while (((jcast('int', jadd(r, 1)) <= Code01_Mafia1.k) and (curx == Code01_Mafia1.arr[jcast('int', jadd(r, 1))][1])) and (curc == Code01_Mafia1.arr[jcast('int', jadd(r, 1))][2])):
                r = jcast('int', (r + 1))
            Code01_Mafia1.gsiz = jcast('int', 0)
            i = jcast('int', l)
            while (i <= r):
                jset(Code01_Mafia1.group, ((_java_obj_16 := Code01_Mafia1), (_java_key_17 := 'gsiz'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code01_Mafia1.other(Code01_Mafia1.arr[i][0]))
                i = jcast('int', (i + 1))
            Code01_Mafia1.groupLink()
            l = jcast('int', (r := jcast('int', (r + (1)))))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code01_Mafia1.cntt):
            jset(Code01_Mafia1.head, i, jset(Code01_Mafia1.dfn, i, jset(Code01_Mafia1.belong, i, 0)))
            i = jcast('int', (i + 1))
        Code01_Mafia1.cntt = jcast('int', jset(Code01_Mafia1, 'cntg', jset(Code01_Mafia1, 'cntd', jset(Code01_Mafia1, 'top', jset(Code01_Mafia1, 'sccCnt', 0)))))

    @staticmethod
    def getAns(limit):
        limit = jcast('int', limit)
        Code01_Mafia1.buildGraph(limit)
        i = jcast('int', 1)
        while (i <= jcast('int', (Code01_Mafia1.m << (1 & 31)))):
            if (Code01_Mafia1.dfn[i] == 0):
                Code01_Mafia1.tarjan(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code01_Mafia1.m):
            try:
                if (Code01_Mafia1.belong[i] == Code01_Mafia1.belong[jcast('int', jadd(i, Code01_Mafia1.m))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_19:
                if _java_control_19.label not in (None,):
                    raise
            except JBreak as _java_control_19:
                if _java_control_19.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if check:
            Code01_Mafia1.ansTime = jcast('int', jset(Code01_Mafia1, 'ansSize', 0))
            i = jcast('int', 1)
            while (i <= Code01_Mafia1.m):
                if (Code01_Mafia1.belong[i] < Code01_Mafia1.belong[jcast('int', jadd(i, Code01_Mafia1.m))]):
                    Code01_Mafia1.ansTime = jcast('int', jstatic('Math', 'max', Code01_Mafia1.ansTime, Code01_Mafia1.destroyTime[i]))
                    jset(Code01_Mafia1.ansArr, ((_java_obj_20 := Code01_Mafia1), (_java_key_21 := 'ansSize'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (1)))))[3], i)
                i = jcast('int', (i + 1))
        Code01_Mafia1.clear()
        return jcast('boolean', check)

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code01_Mafia1.arr, 1, jcast('int', jadd(Code01_Mafia1.k, 1)), (lambda a, b: ((a[1] - b[1]) if (a[1] != b[1]) else (a[2] - b[2]))))
        l = jcast('int', 1)
        r = jcast('int', Code01_Mafia1.maxt)
        mid = 0
        hasAns = jcast('boolean', False)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if Code01_Mafia1.getAns(mid):
                hasAns = jcast('boolean', True)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('boolean', hasAns)

    @staticmethod
    def main(args):
        in_ = Code01_Mafia1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_Mafia1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_Mafia1.m = jcast('int', jcall(in_, 'nextInt'))
        Code01_Mafia1.maxt = jcast('int', 0)
        i = jcast('int', 1)
        x = 0
        y = 0
        c = 0
        t = 0
        while (i <= Code01_Mafia1.m):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            t = jcast('int', jcall(in_, 'nextInt'))
            jset(Code01_Mafia1.arr[((_java_obj_23 := Code01_Mafia1), (_java_key_24 := 'k'), (_java_old_25 := jget(_java_obj_23, _java_key_24)), jset(_java_obj_23, _java_key_24, jcast('int', (_java_old_25 + (1)))))[3]], 0, i)
            jset(Code01_Mafia1.arr[Code01_Mafia1.k], 1, x)
            jset(Code01_Mafia1.arr[Code01_Mafia1.k], 2, c)
            jset(Code01_Mafia1.arr[((_java_obj_26 := Code01_Mafia1), (_java_key_27 := 'k'), (_java_old_28 := jget(_java_obj_26, _java_key_27)), jset(_java_obj_26, _java_key_27, jcast('int', (_java_old_28 + (1)))))[3]], 0, i)
            jset(Code01_Mafia1.arr[Code01_Mafia1.k], 1, y)
            jset(Code01_Mafia1.arr[Code01_Mafia1.k], 2, c)
            Code01_Mafia1.destroyTime[i] = jcast('int', t)
            Code01_Mafia1.maxt = jcast('int', jstatic('Math', 'max', Code01_Mafia1.maxt, t))
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code01_Mafia1.compute())
        if check:
            jcall(out, 'println', 'Yes')
            jcall(out, 'println', jadd(jadd(Code01_Mafia1.ansTime, ' '), Code01_Mafia1.ansSize))
            i = jcast('int', 1)
            while (i <= Code01_Mafia1.ansSize):
                jcall(out, 'print', jadd(Code01_Mafia1.ansArr[i], ' '))
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', 'No')
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
            return jcast('int', self.buffer[((_java_obj_29 := self), (_java_key_30 := 'ptr'), (_java_old_31 := jget(_java_obj_29, _java_key_30)), jset(_java_obj_29, _java_key_30, jcast('int', (_java_old_31 + (1)))), _java_old_31)[4]])

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
            raise TypeError("No matching overload for Code01_Mafia1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Mafia1.MAXM = jcast('int', 50001)
Code01_Mafia1.MAXT = jcast('int', 500001)
Code01_Mafia1.MAXE = jcast('int', 1000001)
Code01_Mafia1.n = jcast('int', 0)
Code01_Mafia1.m = jcast('int', 0)
Code01_Mafia1.k = jcast('int', 0)
Code01_Mafia1.maxt = jcast('int', 0)
Code01_Mafia1.cntt = jcast('int', 0)
Code01_Mafia1.arr = jarray('int', [jcast('int', (Code01_Mafia1.MAXM << (1 & 31))), 3])
Code01_Mafia1.destroyTime = jarray('int', [Code01_Mafia1.MAXM])
Code01_Mafia1.head = jarray('int', [Code01_Mafia1.MAXT])
Code01_Mafia1.nxt = jarray('int', [Code01_Mafia1.MAXE])
Code01_Mafia1.to = jarray('int', [Code01_Mafia1.MAXE])
Code01_Mafia1.cntg = jcast('int', 0)
Code01_Mafia1.group = jarray('int', [Code01_Mafia1.MAXM])
Code01_Mafia1.gsiz = jcast('int', 0)
Code01_Mafia1.dfn = jarray('int', [Code01_Mafia1.MAXT])
Code01_Mafia1.low = jarray('int', [Code01_Mafia1.MAXT])
Code01_Mafia1.cntd = jcast('int', 0)
Code01_Mafia1.sta = jarray('int', [Code01_Mafia1.MAXT])
Code01_Mafia1.top = jcast('int', 0)
Code01_Mafia1.belong = jarray('int', [Code01_Mafia1.MAXT])
Code01_Mafia1.sccCnt = jcast('int', 0)
Code01_Mafia1.ansTime = jcast('int', 0)
Code01_Mafia1.ansSize = jcast('int', 0)
Code01_Mafia1.ansArr = jarray('int', [Code01_Mafia1.MAXM])

if __name__ == '__main__':
    Code01_Mafia1.main([])
