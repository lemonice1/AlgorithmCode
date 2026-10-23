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

# 喵了个喵 II，cdq优化建图，Python版
# 给定一个长度为4n的数组arr，1~n每种数字都出现4次
# 从左到右把每个数字划分进序列0或序列1，要求划分出的两个序列完全相等
# 如果能做到，先打印"Yes"，然后从左到右打印每个位置划分进了什么序列
# 如果不能做到，打印"No"
# 1 <= n <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P9139
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Meow_II_cpp_3:
    __java_fields__ = {'MAXV': 'MAXV', 'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'v': 'v', 'n': 'n', 'cntt': 'cntt', 'vi': 'vi', 'group': 'group', 'cntp': 'cntp', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'arr': 'arr', 'tmp': 'tmp', 'ans': 'ans', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXV = 0
    MAXN = 0
    MAXT = 0
    MAXE = 0
    v = 0
    n = 0
    cntt = 0
    vi = None
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
    # cdq
    arr = None
    tmp = None
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
        Code06_Meow_II_cpp_3.stau[Code06_Meow_II_cpp_3.stacksize] = jcast('int', u)
        Code06_Meow_II_cpp_3.stas[Code06_Meow_II_cpp_3.stacksize] = jcast('int', status)
        Code06_Meow_II_cpp_3.stae[Code06_Meow_II_cpp_3.stacksize] = jcast('int', e)
        Code06_Meow_II_cpp_3.stacksize = jcast('int', (Code06_Meow_II_cpp_3.stacksize + 1))

    @staticmethod
    def pop():
        Code06_Meow_II_cpp_3.stacksize = jcast('int', (Code06_Meow_II_cpp_3.stacksize - 1))
        Code06_Meow_II_cpp_3.u = jcast('int', Code06_Meow_II_cpp_3.stau[Code06_Meow_II_cpp_3.stacksize])
        Code06_Meow_II_cpp_3.status = jcast('int', Code06_Meow_II_cpp_3.stas[Code06_Meow_II_cpp_3.stacksize])
        Code06_Meow_II_cpp_3.e = jcast('int', Code06_Meow_II_cpp_3.stae[Code06_Meow_II_cpp_3.stacksize])

    @staticmethod
    def addGroup(l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        jset(Code06_Meow_II_cpp_3.group[((_java_obj_1 := Code06_Meow_II_cpp_3), (_java_key_2 := 'cntp'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, l)
        jset(Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.cntp], 1, r)
        jset(Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.cntp], 2, x)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_Meow_II_cpp_3.nxt, ((_java_obj_4 := Code06_Meow_II_cpp_3), (_java_key_5 := 'cntg'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code06_Meow_II_cpp_3.head[u])
        Code06_Meow_II_cpp_3.to[Code06_Meow_II_cpp_3.cntg] = jcast('int', v)
        Code06_Meow_II_cpp_3.head[u] = jcast('int', Code06_Meow_II_cpp_3.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code06_Meow_II_cpp_3.dfn, u, jset(Code06_Meow_II_cpp_3.low, u, ((_java_obj_7 := Code06_Meow_II_cpp_3), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code06_Meow_II_cpp_3.sta, ((_java_obj_10 := Code06_Meow_II_cpp_3), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code06_Meow_II_cpp_3.head[u])
        while (e > 0):
            v = jcast('int', Code06_Meow_II_cpp_3.to[e])
            if (Code06_Meow_II_cpp_3.dfn[v] == 0):
                Code06_Meow_II_cpp_3.tarjan1(v)
                jset(Code06_Meow_II_cpp_3.low, u, jstatic('Math', 'min', Code06_Meow_II_cpp_3.low[u], Code06_Meow_II_cpp_3.low[v]))
            else:
                if (Code06_Meow_II_cpp_3.belong[v] == 0):
                    jset(Code06_Meow_II_cpp_3.low, u, jstatic('Math', 'min', Code06_Meow_II_cpp_3.low[u], Code06_Meow_II_cpp_3.dfn[v]))
            e = jcast('int', Code06_Meow_II_cpp_3.nxt[e])
        if (Code06_Meow_II_cpp_3.dfn[u] == Code06_Meow_II_cpp_3.low[u]):
            Code06_Meow_II_cpp_3.sccCnt = jcast('int', (Code06_Meow_II_cpp_3.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code06_Meow_II_cpp_3.sta[((_java_obj_13 := Code06_Meow_II_cpp_3), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                Code06_Meow_II_cpp_3.belong[pop] = jcast('int', Code06_Meow_II_cpp_3.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code06_Meow_II_cpp_3.stacksize = jcast('int', 0)
        Code06_Meow_II_cpp_3.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code06_Meow_II_cpp_3.stacksize > 0):
            Code06_Meow_II_cpp_3.pop()
            if (Code06_Meow_II_cpp_3.status == jcast('int', (-1))):
                jset(Code06_Meow_II_cpp_3.dfn, Code06_Meow_II_cpp_3.u, jset(Code06_Meow_II_cpp_3.low, Code06_Meow_II_cpp_3.u, ((_java_obj_16 := Code06_Meow_II_cpp_3), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code06_Meow_II_cpp_3.sta, ((_java_obj_19 := Code06_Meow_II_cpp_3), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code06_Meow_II_cpp_3.u)
                Code06_Meow_II_cpp_3.e = jcast('int', Code06_Meow_II_cpp_3.head[Code06_Meow_II_cpp_3.u])
            else:
                v = jcast('int', Code06_Meow_II_cpp_3.to[Code06_Meow_II_cpp_3.e])
                if (Code06_Meow_II_cpp_3.status == 0):
                    jset(Code06_Meow_II_cpp_3.low, Code06_Meow_II_cpp_3.u, jstatic('Math', 'min', Code06_Meow_II_cpp_3.low[Code06_Meow_II_cpp_3.u], Code06_Meow_II_cpp_3.low[v]))
                if ((Code06_Meow_II_cpp_3.status == 1) and (Code06_Meow_II_cpp_3.belong[v] == 0)):
                    jset(Code06_Meow_II_cpp_3.low, Code06_Meow_II_cpp_3.u, jstatic('Math', 'min', Code06_Meow_II_cpp_3.low[Code06_Meow_II_cpp_3.u], Code06_Meow_II_cpp_3.dfn[v]))
                Code06_Meow_II_cpp_3.e = jcast('int', Code06_Meow_II_cpp_3.nxt[Code06_Meow_II_cpp_3.e])
            if (Code06_Meow_II_cpp_3.e != 0):
                v = jcast('int', Code06_Meow_II_cpp_3.to[Code06_Meow_II_cpp_3.e])
                if (Code06_Meow_II_cpp_3.dfn[v] == 0):
                    Code06_Meow_II_cpp_3.push(Code06_Meow_II_cpp_3.u, 0, Code06_Meow_II_cpp_3.e)
                    Code06_Meow_II_cpp_3.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code06_Meow_II_cpp_3.push(Code06_Meow_II_cpp_3.u, 1, Code06_Meow_II_cpp_3.e)
            else:
                if (Code06_Meow_II_cpp_3.dfn[Code06_Meow_II_cpp_3.u] == Code06_Meow_II_cpp_3.low[Code06_Meow_II_cpp_3.u]):
                    Code06_Meow_II_cpp_3.sccCnt = jcast('int', (Code06_Meow_II_cpp_3.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code06_Meow_II_cpp_3.sta[((_java_obj_22 := Code06_Meow_II_cpp_3), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                        Code06_Meow_II_cpp_3.belong[pop] = jcast('int', Code06_Meow_II_cpp_3.sccCnt)
                        if not ((pop != Code06_Meow_II_cpp_3.u)):
                            break

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', jadd(x, Code06_Meow_II_cpp_3.v)) if (x <= Code06_Meow_II_cpp_3.v) else jcast('int', (x - Code06_Meow_II_cpp_3.v))))

    @staticmethod
    def merge(l, mid, r):
        l = jcast('int', l)
        mid = jcast('int', mid)
        r = jcast('int', r)
        preOut = jcast('int', 0)
        curOut = jcast('int', 0)
        preIn = jcast('int', 0)
        curIn = jcast('int', 0)
        p1 = jcast('int', jcast('int', jadd(mid, 1)))
        p2 = jcast('int', r)
        while (p2 >= jcast('int', jadd(mid, 1))):
            curOut = jcast('int', ((_java_obj_25 := Code06_Meow_II_cpp_3), (_java_key_26 := 'cntt'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
            curIn = jcast('int', ((_java_obj_28 := Code06_Meow_II_cpp_3), (_java_key_29 := 'cntt'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3])
            while ((jcast('int', (p1 - 1)) >= l) and (Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.arr[jcast('int', (p1 - 1))]][0] >= Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.arr[p2]][0])):
                p1 = jcast('int', (p1 - 1))
                Code06_Meow_II_cpp_3.addEdge(Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.arr[p1]][2], curOut)
                Code06_Meow_II_cpp_3.addEdge(curIn, Code06_Meow_II_cpp_3.other(Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.arr[p1]][2]))
            if (preOut > 0):
                Code06_Meow_II_cpp_3.addEdge(preOut, curOut)
                Code06_Meow_II_cpp_3.addEdge(curIn, preIn)
            Code06_Meow_II_cpp_3.addEdge(curOut, Code06_Meow_II_cpp_3.other(Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.arr[p2]][2]))
            Code06_Meow_II_cpp_3.addEdge(Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.arr[p2]][2], curIn)
            preOut = jcast('int', curOut)
            preIn = jcast('int', curIn)
            p2 = jcast('int', (p2 - 1))
        p1 = jcast('int', l)
        p2 = jcast('int', jcast('int', jadd(mid, 1)))
        ti = jcast('int', 0)
        while ((p1 <= mid) and (p2 <= r)):
            if (Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.arr[p1]][0] <= Code06_Meow_II_cpp_3.group[Code06_Meow_II_cpp_3.arr[p2]][0]):
                jset(Code06_Meow_II_cpp_3.tmp, (ti := jcast('int', (ti + (1)))), Code06_Meow_II_cpp_3.arr[((_java_old_31 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_31)[2]])
            else:
                jset(Code06_Meow_II_cpp_3.tmp, (ti := jcast('int', (ti + (1)))), Code06_Meow_II_cpp_3.arr[((_java_old_32 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_32)[2]])
        while (p1 <= mid):
            jset(Code06_Meow_II_cpp_3.tmp, (ti := jcast('int', (ti + (1)))), Code06_Meow_II_cpp_3.arr[((_java_old_33 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_33)[2]])
        while (p2 <= r):
            jset(Code06_Meow_II_cpp_3.tmp, (ti := jcast('int', (ti + (1)))), Code06_Meow_II_cpp_3.arr[((_java_old_34 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_34)[2]])
        i = jcast('int', l)
        j = jcast('int', 1)
        while (i <= r):
            Code06_Meow_II_cpp_3.arr[i] = jcast('int', Code06_Meow_II_cpp_3.tmp[j])
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))

    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code06_Meow_II_cpp_3.cdq(l, mid)
        Code06_Meow_II_cpp_3.cdq(jcast('int', jadd(mid, 1)), r)
        Code06_Meow_II_cpp_3.merge(l, mid, r)

    @staticmethod
    def buildGraph():
        jstatic('Arrays', 'sort', Code06_Meow_II_cpp_3.group, 1, jcast('int', jadd(Code06_Meow_II_cpp_3.cntp, 1)), (lambda a, b: (a[1] - b[1])))
        Code06_Meow_II_cpp_3.cntt = jcast('int', jcast('int', (Code06_Meow_II_cpp_3.v << (1 & 31))))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_cpp_3.cntp):
            Code06_Meow_II_cpp_3.arr[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code06_Meow_II_cpp_3.cdq(1, Code06_Meow_II_cpp_3.cntp)

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code06_Meow_II_cpp_3.vi, 1, jcast('int', jadd(Code06_Meow_II_cpp_3.n, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_cpp_3.n):
            x = jcast('int', Code06_Meow_II_cpp_3.vi[i][0])
            a = jcast('int', Code06_Meow_II_cpp_3.vi[i][1])
            b = jcast('int', Code06_Meow_II_cpp_3.vi[jcast('int', jadd(i, 1))][1])
            c = jcast('int', Code06_Meow_II_cpp_3.vi[jcast('int', jadd(i, 2))][1])
            d = jcast('int', Code06_Meow_II_cpp_3.vi[jcast('int', jadd(i, 3))][1])
            Code06_Meow_II_cpp_3.addGroup(a, c, x)
            Code06_Meow_II_cpp_3.addGroup(b, d, x)
            Code06_Meow_II_cpp_3.addGroup(a, b, jcast('int', jadd(x, Code06_Meow_II_cpp_3.v)))
            Code06_Meow_II_cpp_3.addGroup(c, d, jcast('int', jadd(x, Code06_Meow_II_cpp_3.v)))
            i = jcast('int', jcast('int', jadd(i, 4)))
        Code06_Meow_II_cpp_3.buildGraph()
        i = jcast('int', 1)
        while (i <= jcast('int', (Code06_Meow_II_cpp_3.v << (1 & 31)))):
            if (Code06_Meow_II_cpp_3.dfn[i] == 0):
                # tarjan1(i);
                Code06_Meow_II_cpp_3.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_cpp_3.v):
            try:
                if (Code06_Meow_II_cpp_3.belong[i] == Code06_Meow_II_cpp_3.belong[jcast('int', jadd(i, Code06_Meow_II_cpp_3.v))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_35:
                if _java_control_35.label not in (None,):
                    raise
            except JBreak as _java_control_35:
                if _java_control_35.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if check:
            i = jcast('int', 1)
            while (i <= Code06_Meow_II_cpp_3.n):
                x = jcast('int', Code06_Meow_II_cpp_3.vi[i][0])
                a = jcast('int', Code06_Meow_II_cpp_3.vi[i][1])
                b = jcast('int', Code06_Meow_II_cpp_3.vi[jcast('int', jadd(i, 1))][1])
                c = jcast('int', Code06_Meow_II_cpp_3.vi[jcast('int', jadd(i, 2))][1])
                d = jcast('int', Code06_Meow_II_cpp_3.vi[jcast('int', jadd(i, 3))][1])
                if (Code06_Meow_II_cpp_3.belong[x] < Code06_Meow_II_cpp_3.belong[jcast('int', jadd(x, Code06_Meow_II_cpp_3.v))]):
                    Code06_Meow_II_cpp_3.ans[a] = jcast('int', 0)
                    Code06_Meow_II_cpp_3.ans[b] = jcast('int', 0)
                    Code06_Meow_II_cpp_3.ans[c] = jcast('int', 1)
                    Code06_Meow_II_cpp_3.ans[d] = jcast('int', 1)
                else:
                    Code06_Meow_II_cpp_3.ans[a] = jcast('int', 0)
                    Code06_Meow_II_cpp_3.ans[b] = jcast('int', 1)
                    Code06_Meow_II_cpp_3.ans[c] = jcast('int', 0)
                    Code06_Meow_II_cpp_3.ans[d] = jcast('int', 1)
                i = jcast('int', jcast('int', jadd(i, 4)))
        return jcast('boolean', check)

    @staticmethod
    def main(args):
        in_ = Code06_Meow_II_cpp_3.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Meow_II_cpp_3.v = jcast('int', jcall(in_, 'nextInt'))
        Code06_Meow_II_cpp_3.n = jcast('int', jcast('int', (Code06_Meow_II_cpp_3.v << (2 & 31))))
        i = jcast('int', 1)
        while (i <= Code06_Meow_II_cpp_3.n):
            jset(Code06_Meow_II_cpp_3.vi[i], 0, jcall(in_, 'nextInt'))
            jset(Code06_Meow_II_cpp_3.vi[i], 1, i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code06_Meow_II_cpp_3.compute())
        if check:
            jcall(out, 'println', 'Yes')
            i = jcast('int', 1)
            while (i <= Code06_Meow_II_cpp_3.n):
                jcall(out, 'print', Code06_Meow_II_cpp_3.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_36 := self), (_java_key_37 := 'ptr'), (_java_old_38 := jget(_java_obj_36, _java_key_37)), jset(_java_obj_36, _java_key_37, jcast('int', (_java_old_38 + (1)))), _java_old_38)[4]])

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
            raise TypeError("No matching overload for Code06_Meow_II_cpp_3.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Meow_II_cpp_3.MAXV = jcast('int', 50001)
Code06_Meow_II_cpp_3.MAXN = jcast('int', 200001)
Code06_Meow_II_cpp_3.MAXT = jcast('int', 5000001)
Code06_Meow_II_cpp_3.MAXE = jcast('int', 20000001)
Code06_Meow_II_cpp_3.v = jcast('int', 0)
Code06_Meow_II_cpp_3.n = jcast('int', 0)
Code06_Meow_II_cpp_3.cntt = jcast('int', 0)
Code06_Meow_II_cpp_3.vi = jarray('int', [Code06_Meow_II_cpp_3.MAXN, 2])
Code06_Meow_II_cpp_3.group = jarray('int', [Code06_Meow_II_cpp_3.MAXN, 3])
Code06_Meow_II_cpp_3.cntp = jcast('int', 0)
Code06_Meow_II_cpp_3.head = jarray('int', [Code06_Meow_II_cpp_3.MAXT])
Code06_Meow_II_cpp_3.nxt = jarray('int', [Code06_Meow_II_cpp_3.MAXE])
Code06_Meow_II_cpp_3.to = jarray('int', [Code06_Meow_II_cpp_3.MAXE])
Code06_Meow_II_cpp_3.cntg = jcast('int', 0)
Code06_Meow_II_cpp_3.dfn = jarray('int', [Code06_Meow_II_cpp_3.MAXT])
Code06_Meow_II_cpp_3.low = jarray('int', [Code06_Meow_II_cpp_3.MAXT])
Code06_Meow_II_cpp_3.cntd = jcast('int', 0)
Code06_Meow_II_cpp_3.sta = jarray('int', [Code06_Meow_II_cpp_3.MAXT])
Code06_Meow_II_cpp_3.top = jcast('int', 0)
Code06_Meow_II_cpp_3.belong = jarray('int', [Code06_Meow_II_cpp_3.MAXT])
Code06_Meow_II_cpp_3.sccCnt = jcast('int', 0)
Code06_Meow_II_cpp_3.arr = jarray('int', [Code06_Meow_II_cpp_3.MAXN])
Code06_Meow_II_cpp_3.tmp = jarray('int', [Code06_Meow_II_cpp_3.MAXN])
Code06_Meow_II_cpp_3.ans = jarray('int', [Code06_Meow_II_cpp_3.MAXN])
Code06_Meow_II_cpp_3.stau = jarray('int', [Code06_Meow_II_cpp_3.MAXT])
Code06_Meow_II_cpp_3.stas = jarray('int', [Code06_Meow_II_cpp_3.MAXT])
Code06_Meow_II_cpp_3.stae = jarray('int', [Code06_Meow_II_cpp_3.MAXT])
Code06_Meow_II_cpp_3.u = jcast('int', 0)
Code06_Meow_II_cpp_3.status = jcast('int', 0)
Code06_Meow_II_cpp_3.e = jcast('int', 0)
Code06_Meow_II_cpp_3.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code06_Meow_II_cpp_3.main([])
