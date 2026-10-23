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

# 喵了个喵 II，树状数组优化建图，Python版
# 给定一个长度为4n的数组arr，1~n每种数字都出现4次
# 从左到右把每个数字划分进序列0或序列1，要求划分出的两个序列完全相等
# 如果能做到，先打印"Yes"，然后从左到右打印每个位置划分进了什么序列
# 如果不能做到，打印"No"
# 1 <= n <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P9139
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Meow_II_java_1:
    __java_fields__ = {'MAXV': 'MAXV', 'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'v': 'v', 'n': 'n', 'cntt': 'cntt', 'vi': 'vi', 'group': 'group', 'cntp': 'cntp', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'inTree': 'inTree', 'outTree': 'outTree', 'ans': 'ans', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXV = 0
    MAXN = 0
    MAXT = 0
    MAXE = 0
    v = 0
    n = 0
    cntt = 0
    # 值v、位置i
    vi = None
    # 左l、右r、决定编号x
    group = None
    cntp = 0
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
    # 树状数组
    inTree = None
    outTree = None
    ans = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stau = None
    stas = None
    stae = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        Code06_Meow_II_java_1.stau[Code06_Meow_II_java_1.stacksize] = jcast('int', u)
        Code06_Meow_II_java_1.stas[Code06_Meow_II_java_1.stacksize] = jcast('int', status)
        Code06_Meow_II_java_1.stae[Code06_Meow_II_java_1.stacksize] = jcast('int', e)
        Code06_Meow_II_java_1.stacksize = jcast('int', (Code06_Meow_II_java_1.stacksize + 1))

    @staticmethod
    def pop():
        Code06_Meow_II_java_1.stacksize = jcast('int', (Code06_Meow_II_java_1.stacksize - 1))
        Code06_Meow_II_java_1.u = jcast('int', Code06_Meow_II_java_1.stau[Code06_Meow_II_java_1.stacksize])
        Code06_Meow_II_java_1.status = jcast('int', Code06_Meow_II_java_1.stas[Code06_Meow_II_java_1.stacksize])
        Code06_Meow_II_java_1.e = jcast('int', Code06_Meow_II_java_1.stae[Code06_Meow_II_java_1.stacksize])

    @staticmethod
    def addGroup(l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        jset(Code06_Meow_II_java_1.group[((_java_obj_1 := Code06_Meow_II_java_1), (_java_key_2 := 'cntp'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, l)
        jset(Code06_Meow_II_java_1.group[Code06_Meow_II_java_1.cntp], 1, r)
        jset(Code06_Meow_II_java_1.group[Code06_Meow_II_java_1.cntp], 2, x)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_Meow_II_java_1.nxt, ((_java_obj_4 := Code06_Meow_II_java_1), (_java_key_5 := 'cntg'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code06_Meow_II_java_1.head[u])
        Code06_Meow_II_java_1.to[Code06_Meow_II_java_1.cntg] = jcast('int', v)
        Code06_Meow_II_java_1.head[u] = jcast('int', Code06_Meow_II_java_1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code06_Meow_II_java_1.dfn, u, jset(Code06_Meow_II_java_1.low, u, ((_java_obj_7 := Code06_Meow_II_java_1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code06_Meow_II_java_1.sta, ((_java_obj_10 := Code06_Meow_II_java_1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code06_Meow_II_java_1.head[u])
        while (e > 0):
            v = jcast('int', Code06_Meow_II_java_1.to[e])
            if (Code06_Meow_II_java_1.dfn[v] == 0):
                Code06_Meow_II_java_1.tarjan1(v)
                jset(Code06_Meow_II_java_1.low, u, jstatic('Math', 'min', Code06_Meow_II_java_1.low[u], Code06_Meow_II_java_1.low[v]))
            else:
                if (Code06_Meow_II_java_1.belong[v] == 0):
                    jset(Code06_Meow_II_java_1.low, u, jstatic('Math', 'min', Code06_Meow_II_java_1.low[u], Code06_Meow_II_java_1.dfn[v]))
            e = jcast('int', Code06_Meow_II_java_1.nxt[e])
        if (Code06_Meow_II_java_1.dfn[u] == Code06_Meow_II_java_1.low[u]):
            Code06_Meow_II_java_1.sccCnt = jcast('int', (Code06_Meow_II_java_1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code06_Meow_II_java_1.sta[((_java_obj_13 := Code06_Meow_II_java_1), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                Code06_Meow_II_java_1.belong[pop] = jcast('int', Code06_Meow_II_java_1.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code06_Meow_II_java_1.stacksize = jcast('int', 0)
        Code06_Meow_II_java_1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code06_Meow_II_java_1.stacksize > 0):
            Code06_Meow_II_java_1.pop()
            if (Code06_Meow_II_java_1.status == jcast('int', (-1))):
                jset(Code06_Meow_II_java_1.dfn, Code06_Meow_II_java_1.u, jset(Code06_Meow_II_java_1.low, Code06_Meow_II_java_1.u, ((_java_obj_16 := Code06_Meow_II_java_1), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code06_Meow_II_java_1.sta, ((_java_obj_19 := Code06_Meow_II_java_1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code06_Meow_II_java_1.u)
                Code06_Meow_II_java_1.e = jcast('int', Code06_Meow_II_java_1.head[Code06_Meow_II_java_1.u])
            else:
                v = jcast('int', Code06_Meow_II_java_1.to[Code06_Meow_II_java_1.e])
                if (Code06_Meow_II_java_1.status == 0):
                    jset(Code06_Meow_II_java_1.low, Code06_Meow_II_java_1.u, jstatic('Math', 'min', Code06_Meow_II_java_1.low[Code06_Meow_II_java_1.u], Code06_Meow_II_java_1.low[v]))
                if ((Code06_Meow_II_java_1.status == 1) and (Code06_Meow_II_java_1.belong[v] == 0)):
                    jset(Code06_Meow_II_java_1.low, Code06_Meow_II_java_1.u, jstatic('Math', 'min', Code06_Meow_II_java_1.low[Code06_Meow_II_java_1.u], Code06_Meow_II_java_1.dfn[v]))
                Code06_Meow_II_java_1.e = jcast('int', Code06_Meow_II_java_1.nxt[Code06_Meow_II_java_1.e])
            if (Code06_Meow_II_java_1.e != 0):
                v = jcast('int', Code06_Meow_II_java_1.to[Code06_Meow_II_java_1.e])
                if (Code06_Meow_II_java_1.dfn[v] == 0):
                    Code06_Meow_II_java_1.push(Code06_Meow_II_java_1.u, 0, Code06_Meow_II_java_1.e)
                    Code06_Meow_II_java_1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code06_Meow_II_java_1.push(Code06_Meow_II_java_1.u, 1, Code06_Meow_II_java_1.e)
            else:
                if (Code06_Meow_II_java_1.dfn[Code06_Meow_II_java_1.u] == Code06_Meow_II_java_1.low[Code06_Meow_II_java_1.u]):
                    Code06_Meow_II_java_1.sccCnt = jcast('int', (Code06_Meow_II_java_1.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code06_Meow_II_java_1.sta[((_java_obj_22 := Code06_Meow_II_java_1), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                        Code06_Meow_II_java_1.belong[pop] = jcast('int', Code06_Meow_II_java_1.sccCnt)
                        if not ((pop != Code06_Meow_II_java_1.u)):
                            break

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def addOut(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        while (i <= Code06_Meow_II_java_1.n):
            preo = jcast('int', Code06_Meow_II_java_1.outTree[i])
            curo = jcast('int', ((_java_obj_25 := Code06_Meow_II_java_1), (_java_key_26 := 'cntt'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
            if (preo > 0):
                Code06_Meow_II_java_1.addEdge(preo, curo)
            Code06_Meow_II_java_1.addEdge(x, curo)
            Code06_Meow_II_java_1.outTree[i] = jcast('int', curo)
            i = jcast('int', jcast('int', jadd(i, Code06_Meow_II_java_1.lowbit(i))))

    @staticmethod
    def addIn(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        while (i <= Code06_Meow_II_java_1.n):
            prei = jcast('int', Code06_Meow_II_java_1.inTree[i])
            curi = jcast('int', ((_java_obj_28 := Code06_Meow_II_java_1), (_java_key_29 := 'cntt'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3])
            if (prei > 0):
                Code06_Meow_II_java_1.addEdge(curi, prei)
            Code06_Meow_II_java_1.addEdge(curi, x)
            Code06_Meow_II_java_1.inTree[i] = jcast('int', curi)
            i = jcast('int', jcast('int', jadd(i, Code06_Meow_II_java_1.lowbit(i))))

    @staticmethod
    def rangeToX(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        while (i > 0):
            if (Code06_Meow_II_java_1.outTree[i] > 0):
                Code06_Meow_II_java_1.addEdge(Code06_Meow_II_java_1.outTree[i], x)
            i = jcast('int', jcast('int', (i - Code06_Meow_II_java_1.lowbit(i))))

    @staticmethod
    def xToRange(x, i):
        x = jcast('int', x)
        i = jcast('int', i)
        while (i > 0):
            if (Code06_Meow_II_java_1.inTree[i] > 0):
                Code06_Meow_II_java_1.addEdge(x, Code06_Meow_II_java_1.inTree[i])
            i = jcast('int', jcast('int', (i - Code06_Meow_II_java_1.lowbit(i))))

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', jadd(x, Code06_Meow_II_java_1.v)) if (x <= Code06_Meow_II_java_1.v) else jcast('int', (x - Code06_Meow_II_java_1.v))))

    @staticmethod
    def buildGraph():
        jstatic('Arrays', 'sort', Code06_Meow_II_java_1.group, 1, jcast('int', jadd(Code06_Meow_II_java_1.cntp, 1)), (lambda a, b: (a[1] - b[1])))
        Code06_Meow_II_java_1.cntt = jcast('int', jcast('int', (Code06_Meow_II_java_1.v << (1 & 31))))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_java_1.cntp):
            l = jcast('int', Code06_Meow_II_java_1.group[i][0])
            # 后缀查询转化成前缀查询
            p = jcast('int', jcast('int', jadd(jcast('int', (Code06_Meow_II_java_1.n - l)), 1)))
            x = jcast('int', Code06_Meow_II_java_1.group[i][2])
            Code06_Meow_II_java_1.xToRange(x, p)
            Code06_Meow_II_java_1.rangeToX(p, Code06_Meow_II_java_1.other(x))
            Code06_Meow_II_java_1.addIn(p, Code06_Meow_II_java_1.other(x))
            Code06_Meow_II_java_1.addOut(p, x)
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code06_Meow_II_java_1.vi, 1, jcast('int', jadd(Code06_Meow_II_java_1.n, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_java_1.n):
            x = jcast('int', Code06_Meow_II_java_1.vi[i][0])
            a = jcast('int', Code06_Meow_II_java_1.vi[i][1])
            b = jcast('int', Code06_Meow_II_java_1.vi[jcast('int', jadd(i, 1))][1])
            c = jcast('int', Code06_Meow_II_java_1.vi[jcast('int', jadd(i, 2))][1])
            d = jcast('int', Code06_Meow_II_java_1.vi[jcast('int', jadd(i, 3))][1])
            Code06_Meow_II_java_1.addGroup(a, c, x)
            Code06_Meow_II_java_1.addGroup(b, d, x)
            Code06_Meow_II_java_1.addGroup(a, b, jcast('int', jadd(x, Code06_Meow_II_java_1.v)))
            Code06_Meow_II_java_1.addGroup(c, d, jcast('int', jadd(x, Code06_Meow_II_java_1.v)))
            i = jcast('int', jcast('int', jadd(i, 4)))
        Code06_Meow_II_java_1.buildGraph()
        i = jcast('int', 1)
        while (i <= jcast('int', (Code06_Meow_II_java_1.v << (1 & 31)))):
            if (Code06_Meow_II_java_1.dfn[i] == 0):
                # tarjan1(i);
                Code06_Meow_II_java_1.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_java_1.v):
            try:
                if (Code06_Meow_II_java_1.belong[i] == Code06_Meow_II_java_1.belong[jcast('int', jadd(i, Code06_Meow_II_java_1.v))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_31:
                if _java_control_31.label not in (None,):
                    raise
            except JBreak as _java_control_31:
                if _java_control_31.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if check:
            i = jcast('int', 1)
            while (i <= Code06_Meow_II_java_1.n):
                x = jcast('int', Code06_Meow_II_java_1.vi[i][0])
                a = jcast('int', Code06_Meow_II_java_1.vi[i][1])
                b = jcast('int', Code06_Meow_II_java_1.vi[jcast('int', jadd(i, 1))][1])
                c = jcast('int', Code06_Meow_II_java_1.vi[jcast('int', jadd(i, 2))][1])
                d = jcast('int', Code06_Meow_II_java_1.vi[jcast('int', jadd(i, 3))][1])
                if (Code06_Meow_II_java_1.belong[x] < Code06_Meow_II_java_1.belong[jcast('int', jadd(x, Code06_Meow_II_java_1.v))]):
                    Code06_Meow_II_java_1.ans[a] = jcast('int', 0)
                    Code06_Meow_II_java_1.ans[b] = jcast('int', 0)
                    Code06_Meow_II_java_1.ans[c] = jcast('int', 1)
                    Code06_Meow_II_java_1.ans[d] = jcast('int', 1)
                else:
                    Code06_Meow_II_java_1.ans[a] = jcast('int', 0)
                    Code06_Meow_II_java_1.ans[b] = jcast('int', 1)
                    Code06_Meow_II_java_1.ans[c] = jcast('int', 0)
                    Code06_Meow_II_java_1.ans[d] = jcast('int', 1)
                i = jcast('int', jcast('int', jadd(i, 4)))
        return jcast('boolean', check)

    @staticmethod
    def main(args):
        in_ = Code06_Meow_II_java_1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Meow_II_java_1.v = jcast('int', jcall(in_, 'nextInt'))
        Code06_Meow_II_java_1.n = jcast('int', jcast('int', (Code06_Meow_II_java_1.v << (2 & 31))))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_java_1.n):
            jset(Code06_Meow_II_java_1.vi[i], 0, jcall(in_, 'nextInt'))
            jset(Code06_Meow_II_java_1.vi[i], 1, i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code06_Meow_II_java_1.compute())
        if check:
            jcall(out, 'println', 'Yes')
            i = jcast('int', 1)
            while (i <= Code06_Meow_II_java_1.n):
                jcall(out, 'print', Code06_Meow_II_java_1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_32 := self), (_java_key_33 := 'ptr'), (_java_old_34 := jget(_java_obj_32, _java_key_33)), jset(_java_obj_32, _java_key_33, jcast('int', (_java_old_34 + (1)))), _java_old_34)[4]])

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
            raise TypeError("No matching overload for Code06_Meow_II_java_1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Meow_II_java_1.MAXV = jcast('int', 50001)
Code06_Meow_II_java_1.MAXN = jcast('int', 200001)
Code06_Meow_II_java_1.MAXT = jcast('int', 5000001)
Code06_Meow_II_java_1.MAXE = jcast('int', 20000001)
Code06_Meow_II_java_1.v = jcast('int', 0)
Code06_Meow_II_java_1.n = jcast('int', 0)
Code06_Meow_II_java_1.cntt = jcast('int', 0)
Code06_Meow_II_java_1.vi = jarray('int', [Code06_Meow_II_java_1.MAXN, 2])
Code06_Meow_II_java_1.group = jarray('int', [Code06_Meow_II_java_1.MAXN, 3])
Code06_Meow_II_java_1.cntp = jcast('int', 0)
Code06_Meow_II_java_1.head = jarray('int', [Code06_Meow_II_java_1.MAXT])
Code06_Meow_II_java_1.nxt = jarray('int', [Code06_Meow_II_java_1.MAXE])
Code06_Meow_II_java_1.to = jarray('int', [Code06_Meow_II_java_1.MAXE])
Code06_Meow_II_java_1.cntg = jcast('int', 0)
Code06_Meow_II_java_1.dfn = jarray('int', [Code06_Meow_II_java_1.MAXT])
Code06_Meow_II_java_1.low = jarray('int', [Code06_Meow_II_java_1.MAXT])
Code06_Meow_II_java_1.cntd = jcast('int', 0)
Code06_Meow_II_java_1.sta = jarray('int', [Code06_Meow_II_java_1.MAXT])
Code06_Meow_II_java_1.top = jcast('int', 0)
Code06_Meow_II_java_1.belong = jarray('int', [Code06_Meow_II_java_1.MAXT])
Code06_Meow_II_java_1.sccCnt = jcast('int', 0)
Code06_Meow_II_java_1.inTree = jarray('int', [Code06_Meow_II_java_1.MAXN])
Code06_Meow_II_java_1.outTree = jarray('int', [Code06_Meow_II_java_1.MAXN])
Code06_Meow_II_java_1.ans = jarray('int', [Code06_Meow_II_java_1.MAXN])
Code06_Meow_II_java_1.stau = jarray('int', [Code06_Meow_II_java_1.MAXT])
Code06_Meow_II_java_1.stas = jarray('int', [Code06_Meow_II_java_1.MAXT])
Code06_Meow_II_java_1.stae = jarray('int', [Code06_Meow_II_java_1.MAXT])
Code06_Meow_II_java_1.u = jcast('int', 0)
Code06_Meow_II_java_1.status = jcast('int', 0)
Code06_Meow_II_java_1.e = jcast('int', 0)
Code06_Meow_II_java_1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code06_Meow_II_java_1.main([])
