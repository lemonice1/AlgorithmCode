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

# 电台，Python版
# 给定数值f，范围[1, f]上，你要选一个数字ansx作为固定频率
# 一共p个电台，每个电台给定频率范围[l, r]，频率范围包含ansx的电台才能签约
# 签约电台还要满足n个要求和m个限制，具体格式如下
# 要求 u v : 必须签下电台u或者电台v
# 限制 u v : 电台u和电台v不能同时签下
# 如果存在签约方案，找到任何一种即可，依次打印，签约电台的数量、ansx、所有签约电台的编号
# 如果不存在签约方案，打印-1
# 2 <= n、p、f、m <= 4 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1215F
# 测试链接 : https://codeforces.com/problemset/problem/1215/F
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_RadioStations2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXM': 'MAXM', 'n': 'n', 'p': 'p', 'f': 'f', 'm': 'm', 'cntt': 'cntt', 'l': 'l', 'r': 'r', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'pre': 'pre', 'suf': 'suf', 'ansx': 'ansx', 'pick': 'pick', 'siz': 'siz'}
    MAXN = 0
    MAXT = 0
    MAXM = 0
    n = 0
    p = 0
    f = 0
    m = 0
    cntt = 0
    l = None
    r = None
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
    pre = None
    suf = None
    ansx = 0
    pick = None
    siz = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_RadioStations2.nxt, ((_java_obj_1 := Code08_RadioStations2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_RadioStations2.head[u])
        Code08_RadioStations2.to[Code08_RadioStations2.cntg] = jcast('int', v)
        Code08_RadioStations2.head[u] = jcast('int', Code08_RadioStations2.cntg)

    @staticmethod
    def link():
        jset(Code08_RadioStations2.pre, 1, ((_java_obj_4 := Code08_RadioStations2), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        i = jcast('int', 2)
        while (i <= Code08_RadioStations2.f):
            jset(Code08_RadioStations2.pre, i, ((_java_obj_7 := Code08_RadioStations2), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            Code08_RadioStations2.addEdge(Code08_RadioStations2.pre[jcast('int', (i - 1))], Code08_RadioStations2.pre[i])
            i = jcast('int', (i + 1))
        jset(Code08_RadioStations2.suf, Code08_RadioStations2.f, ((_java_obj_10 := Code08_RadioStations2), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        i = jcast('int', jcast('int', (Code08_RadioStations2.f - 1)))
        while (i >= 1):
            jset(Code08_RadioStations2.suf, i, ((_java_obj_13 := Code08_RadioStations2), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
            Code08_RadioStations2.addEdge(Code08_RadioStations2.suf[jcast('int', jadd(i, 1))], Code08_RadioStations2.suf[i])
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        while (i <= Code08_RadioStations2.p):
            Code08_RadioStations2.addEdge(i, Code08_RadioStations2.pre[Code08_RadioStations2.r[i]])
            Code08_RadioStations2.addEdge(i, Code08_RadioStations2.suf[Code08_RadioStations2.l[i]])
            if (jcast('int', (Code08_RadioStations2.l[i] - 1)) >= 1):
                Code08_RadioStations2.addEdge(Code08_RadioStations2.pre[jcast('int', (Code08_RadioStations2.l[i] - 1))], jcast('int', jadd(i, Code08_RadioStations2.p)))
            if (jcast('int', jadd(Code08_RadioStations2.r[i], 1)) <= Code08_RadioStations2.f):
                Code08_RadioStations2.addEdge(Code08_RadioStations2.suf[jcast('int', jadd(Code08_RadioStations2.r[i], 1))], jcast('int', jadd(i, Code08_RadioStations2.p)))
            i = jcast('int', (i + 1))

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code08_RadioStations2.dfn, u, jset(Code08_RadioStations2.low, u, ((_java_obj_16 := Code08_RadioStations2), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
        jset(Code08_RadioStations2.sta, ((_java_obj_19 := Code08_RadioStations2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], u)
        e = jcast('int', Code08_RadioStations2.head[u])
        while (e > 0):
            v = jcast('int', Code08_RadioStations2.to[e])
            if (Code08_RadioStations2.dfn[v] == 0):
                Code08_RadioStations2.tarjan(v)
                jset(Code08_RadioStations2.low, u, jstatic('Math', 'min', Code08_RadioStations2.low[u], Code08_RadioStations2.low[v]))
            else:
                if (Code08_RadioStations2.belong[v] == 0):
                    jset(Code08_RadioStations2.low, u, jstatic('Math', 'min', Code08_RadioStations2.low[u], Code08_RadioStations2.dfn[v]))
            e = jcast('int', Code08_RadioStations2.nxt[e])
        if (Code08_RadioStations2.dfn[u] == Code08_RadioStations2.low[u]):
            Code08_RadioStations2.sccCnt = jcast('int', (Code08_RadioStations2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code08_RadioStations2.sta[((_java_obj_22 := Code08_RadioStations2), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                Code08_RadioStations2.belong[pop] = jcast('int', Code08_RadioStations2.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def compute():
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code08_RadioStations2.p):
            try:
                if (Code08_RadioStations2.belong[i] == Code08_RadioStations2.belong[jcast('int', jadd(i, Code08_RadioStations2.p))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
                else:
                    if (Code08_RadioStations2.belong[i] < Code08_RadioStations2.belong[jcast('int', jadd(i, Code08_RadioStations2.p))]):
                        Code08_RadioStations2.ansx = jcast('int', jstatic('Math', 'max', Code08_RadioStations2.ansx, Code08_RadioStations2.l[i]))
                        jset(Code08_RadioStations2.pick, ((_java_obj_26 := Code08_RadioStations2), (_java_key_27 := 'siz'), (_java_old_28 := jget(_java_obj_26, _java_key_27)), jset(_java_obj_26, _java_key_27, jcast('int', (_java_old_28 + (1)))))[3], i)
            except JContinue as _java_control_25:
                if _java_control_25.label not in (None,):
                    raise
            except JBreak as _java_control_25:
                if _java_control_25.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        return jcast('boolean', check)

    @staticmethod
    def main(args):
        in_ = Code08_RadioStations2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_RadioStations2.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_RadioStations2.p = jcast('int', jcall(in_, 'nextInt'))
        Code08_RadioStations2.f = jcast('int', jcall(in_, 'nextInt'))
        Code08_RadioStations2.m = jcast('int', jcall(in_, 'nextInt'))
        Code08_RadioStations2.cntt = jcast('int', jcast('int', (Code08_RadioStations2.p << (1 & 31))))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code08_RadioStations2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code08_RadioStations2.addEdge(jcast('int', jadd(u, Code08_RadioStations2.p)), v)
            Code08_RadioStations2.addEdge(jcast('int', jadd(v, Code08_RadioStations2.p)), u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_RadioStations2.p):
            jset(Code08_RadioStations2.l, i, jcall(in_, 'nextInt'))
            jset(Code08_RadioStations2.r, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code08_RadioStations2.link()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code08_RadioStations2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code08_RadioStations2.addEdge(u, jcast('int', jadd(v, Code08_RadioStations2.p)))
            Code08_RadioStations2.addEdge(v, jcast('int', jadd(u, Code08_RadioStations2.p)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_RadioStations2.cntt):
            if (Code08_RadioStations2.dfn[i] == 0):
                Code08_RadioStations2.tarjan(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code08_RadioStations2.compute())
        if check:
            jcall(out, 'println', jadd(jadd(Code08_RadioStations2.siz, ' '), Code08_RadioStations2.ansx))
            i = jcast('int', 1)
            while (i <= Code08_RadioStations2.siz):
                jcall(out, 'print', jadd(Code08_RadioStations2.pick[i], ' '))
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', jcast('int', (-1)))
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
            raise TypeError("No matching overload for Code08_RadioStations2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_RadioStations2.MAXN = jcast('int', 400001)
Code08_RadioStations2.MAXT = jcast('int', 2000001)
Code08_RadioStations2.MAXM = jcast('int', 4000001)
Code08_RadioStations2.n = jcast('int', 0)
Code08_RadioStations2.p = jcast('int', 0)
Code08_RadioStations2.f = jcast('int', 0)
Code08_RadioStations2.m = jcast('int', 0)
Code08_RadioStations2.cntt = jcast('int', 0)
Code08_RadioStations2.l = jarray('int', [Code08_RadioStations2.MAXN])
Code08_RadioStations2.r = jarray('int', [Code08_RadioStations2.MAXN])
Code08_RadioStations2.head = jarray('int', [Code08_RadioStations2.MAXT])
Code08_RadioStations2.nxt = jarray('int', [Code08_RadioStations2.MAXM])
Code08_RadioStations2.to = jarray('int', [Code08_RadioStations2.MAXM])
Code08_RadioStations2.cntg = jcast('int', 0)
Code08_RadioStations2.dfn = jarray('int', [Code08_RadioStations2.MAXT])
Code08_RadioStations2.low = jarray('int', [Code08_RadioStations2.MAXT])
Code08_RadioStations2.cntd = jcast('int', 0)
Code08_RadioStations2.sta = jarray('int', [Code08_RadioStations2.MAXT])
Code08_RadioStations2.top = jcast('int', 0)
Code08_RadioStations2.belong = jarray('int', [Code08_RadioStations2.MAXT])
Code08_RadioStations2.sccCnt = jcast('int', 0)
Code08_RadioStations2.pre = jarray('int', [Code08_RadioStations2.MAXN])
Code08_RadioStations2.suf = jarray('int', [Code08_RadioStations2.MAXN])
Code08_RadioStations2.ansx = jcast('int', 0)
Code08_RadioStations2.pick = jarray('int', [Code08_RadioStations2.MAXN])
Code08_RadioStations2.siz = jcast('int', 0)

if __name__ == '__main__':
    Code08_RadioStations2.main([])
