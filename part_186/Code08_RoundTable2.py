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

# 圆桌骑士，Python版
# 一共n个骑士，有m条厌恶关系，每条厌恶关系代表两个骑士互相讨厌对方
# 你可以任选骑士参加圆桌会议，但是厌恶关系的骑士无法在圆桌中相邻
# 圆桌会议的骑士数量必须是大于1的奇数，以防止赞同票和反对票一样多
# 也许有的骑士，不管怎么安排都无法参加圆桌会议，打印这个数量
# 1 <= n <= 10^3
# 1 <= m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/SP2878
# 测试链接 : https://www.spoj.com/problems/KNIGHTS/
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_RoundTable2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'hate': 'hate', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'vbccArr': 'vbccArr', 'vbccl': 'vbccl', 'vbccr': 'vbccr', 'idx': 'idx', 'vbccCnt': 'vbccCnt', 'curVbcc': 'curVbcc', 'color': 'color', 'ok': 'ok'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    hate = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    vbccArr = None
    vbccl = None
    vbccr = None
    idx = 0
    vbccCnt = 0
    curVbcc = None
    color = None
    ok = None
    @staticmethod
    def prepare():
        Code08_RoundTable2.cntg = jcast('int', jset(Code08_RoundTable2, 'cntd', jset(Code08_RoundTable2, 'top', jset(Code08_RoundTable2, 'idx', jset(Code08_RoundTable2, 'vbccCnt', 0)))))
        i = jcast('int', 1)
        while (i <= Code08_RoundTable2.n):
            jset(Code08_RoundTable2.head, i, jset(Code08_RoundTable2.dfn, i, jset(Code08_RoundTable2.low, i, 0)))
            Code08_RoundTable2.ok[i] = jcast('boolean', False)
            j = jcast('int', 1)
            while (j <= Code08_RoundTable2.n):
                jset(Code08_RoundTable2.hate[i], j, False)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_RoundTable2.nxt, ((_java_obj_1 := Code08_RoundTable2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_RoundTable2.head[u])
        Code08_RoundTable2.to[Code08_RoundTable2.cntg] = jcast('int', v)
        Code08_RoundTable2.head[u] = jcast('int', Code08_RoundTable2.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code08_RoundTable2.dfn, u, jset(Code08_RoundTable2.low, u, ((_java_obj_4 := Code08_RoundTable2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code08_RoundTable2.sta, ((_java_obj_7 := Code08_RoundTable2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code08_RoundTable2.head[u])
        while (e > 0):
            v = jcast('int', Code08_RoundTable2.to[e])
            if (Code08_RoundTable2.dfn[v] == 0):
                Code08_RoundTable2.tarjan(v)
                jset(Code08_RoundTable2.low, u, jstatic('Math', 'min', Code08_RoundTable2.low[u], Code08_RoundTable2.low[v]))
                if (Code08_RoundTable2.low[v] >= Code08_RoundTable2.dfn[u]):
                    Code08_RoundTable2.vbccCnt = jcast('int', (Code08_RoundTable2.vbccCnt + 1))
                    jset(Code08_RoundTable2.vbccArr, ((_java_obj_10 := Code08_RoundTable2), (_java_key_11 := 'idx'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
                    Code08_RoundTable2.vbccl[Code08_RoundTable2.vbccCnt] = jcast('int', Code08_RoundTable2.idx)
                    pop = 0
                    while True:
                        pop = jcast('int', Code08_RoundTable2.sta[((_java_obj_13 := Code08_RoundTable2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        jset(Code08_RoundTable2.vbccArr, ((_java_obj_16 := Code08_RoundTable2), (_java_key_17 := 'idx'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], pop)
                        if not ((pop != v)):
                            break
                    Code08_RoundTable2.vbccr[Code08_RoundTable2.vbccCnt] = jcast('int', Code08_RoundTable2.idx)
            else:
                jset(Code08_RoundTable2.low, u, jstatic('Math', 'min', Code08_RoundTable2.low[u], Code08_RoundTable2.dfn[v]))
            e = jcast('int', Code08_RoundTable2.nxt[e])

    # u表示当前节点，c表示当前分配给u节点的颜色，只有1和2两种颜色
    # 返回是否发现了节点数量为奇数的环
    @staticmethod
    def oddLoop(u, c):
        u = jcast('int', u)
        c = jcast('int', c)
        Code08_RoundTable2.color[u] = jcast('int', c)
        e = jcast('int', Code08_RoundTable2.head[u])
        while (e > 0):
            v = jcast('int', Code08_RoundTable2.to[e])
            if Code08_RoundTable2.curVbcc[v]:
                if (Code08_RoundTable2.color[v] == c):
                    return jcast('boolean', True)
                if ((Code08_RoundTable2.color[v] == 0) and Code08_RoundTable2.oddLoop(v, (2 if (c == 1) else 1))):
                    return jcast('boolean', True)
            e = jcast('int', Code08_RoundTable2.nxt[e])
        return jcast('boolean', False)

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code08_RoundTable2.vbccCnt):
            j = jcast('int', Code08_RoundTable2.vbccl[i])
            while (j <= Code08_RoundTable2.vbccr[i]):
                jset(Code08_RoundTable2.curVbcc, Code08_RoundTable2.vbccArr[j], True)
                jset(Code08_RoundTable2.color, Code08_RoundTable2.vbccArr[j], 0)
                j = jcast('int', (j + 1))
            check = jcast('boolean', Code08_RoundTable2.oddLoop(Code08_RoundTable2.vbccArr[Code08_RoundTable2.vbccl[i]], 1))
            j = jcast('int', Code08_RoundTable2.vbccl[i])
            while (j <= Code08_RoundTable2.vbccr[i]):
                jset(Code08_RoundTable2.curVbcc, Code08_RoundTable2.vbccArr[j], False)
                ((_java_obj_19 := Code08_RoundTable2.ok), (_java_key_20 := Code08_RoundTable2.vbccArr[j]), jset(_java_obj_19, _java_key_20, (jget(_java_obj_19, _java_key_20) | check)))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code08_RoundTable2.n):
            if (not Code08_RoundTable2.ok[i]):
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code08_RoundTable2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_RoundTable2.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_RoundTable2.m = jcast('int', jcall(in_, 'nextInt'))
        while ((Code08_RoundTable2.n != 0) or (Code08_RoundTable2.m != 0)):
            Code08_RoundTable2.prepare()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i <= Code08_RoundTable2.m):
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                jset(Code08_RoundTable2.hate[u], v, True)
                jset(Code08_RoundTable2.hate[v], u, True)
                i = jcast('int', (i + 1))
            u = jcast('int', 1)
            while (u <= Code08_RoundTable2.n):
                v = jcast('int', jcast('int', jadd(u, 1)))
                while (v <= Code08_RoundTable2.n):
                    if (not Code08_RoundTable2.hate[u][v]):
                        Code08_RoundTable2.addEdge(u, v)
                        Code08_RoundTable2.addEdge(v, u)
                    v = jcast('int', (v + 1))
                u = jcast('int', (u + 1))
            i = jcast('int', 1)
            while (i <= Code08_RoundTable2.n):
                if (Code08_RoundTable2.dfn[i] == 0):
                    Code08_RoundTable2.tarjan(i)
                i = jcast('int', (i + 1))
            ans = jcast('int', Code08_RoundTable2.compute())
            jcall(out, 'println', ans)
            Code08_RoundTable2.n = jcast('int', jcall(in_, 'nextInt'))
            Code08_RoundTable2.m = jcast('int', jcall(in_, 'nextInt'))
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
            return jcast('int', self.buffer[((_java_obj_21 := self), (_java_key_22 := 'ptr'), (_java_old_23 := jget(_java_obj_21, _java_key_22)), jset(_java_obj_21, _java_key_22, jcast('int', (_java_old_23 + (1)))), _java_old_23)[4]])

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
            raise TypeError("No matching overload for Code08_RoundTable2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_RoundTable2.MAXN = jcast('int', 1001)
Code08_RoundTable2.MAXM = jcast('int', 1000001)
Code08_RoundTable2.n = jcast('int', 0)
Code08_RoundTable2.m = jcast('int', 0)
Code08_RoundTable2.hate = jarray('boolean', [Code08_RoundTable2.MAXN, Code08_RoundTable2.MAXN])
Code08_RoundTable2.head = jarray('int', [Code08_RoundTable2.MAXN])
Code08_RoundTable2.nxt = jarray('int', [jcast('int', (Code08_RoundTable2.MAXM << (1 & 31)))])
Code08_RoundTable2.to = jarray('int', [jcast('int', (Code08_RoundTable2.MAXM << (1 & 31)))])
Code08_RoundTable2.cntg = jcast('int', 0)
Code08_RoundTable2.dfn = jarray('int', [Code08_RoundTable2.MAXN])
Code08_RoundTable2.low = jarray('int', [Code08_RoundTable2.MAXN])
Code08_RoundTable2.cntd = jcast('int', 0)
Code08_RoundTable2.sta = jarray('int', [Code08_RoundTable2.MAXN])
Code08_RoundTable2.top = jcast('int', 0)
Code08_RoundTable2.vbccArr = jarray('int', [jcast('int', (Code08_RoundTable2.MAXN << (1 & 31)))])
Code08_RoundTable2.vbccl = jarray('int', [Code08_RoundTable2.MAXN])
Code08_RoundTable2.vbccr = jarray('int', [Code08_RoundTable2.MAXN])
Code08_RoundTable2.idx = jcast('int', 0)
Code08_RoundTable2.vbccCnt = jcast('int', 0)
Code08_RoundTable2.curVbcc = jarray('boolean', [Code08_RoundTable2.MAXN])
Code08_RoundTable2.color = jarray('int', [Code08_RoundTable2.MAXN])
Code08_RoundTable2.ok = jarray('boolean', [Code08_RoundTable2.MAXN])

if __name__ == '__main__':
    Code08_RoundTable2.main([])
