# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 矿场搭建，Python版
# 一共n个地点，地点至少2个，每个地点都有人，m条双向道路连通所有地点
# 地震会发生在任何一个地点，地震发生时，其他地点的人都要去往救援点
# 你可以在任何地点设立救援点，但是发生地震的地点，道路和救援点都会失效
# 打印至少需要几个救援点，打印设立救援点的方案总数，方案认为是无序集合
# 1 <= n <= 1000
# 1 <= m <= 1000
# 测试链接 : https://www.luogu.com.cn/problem/P3225
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_MiningFarm1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 't': 't', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'cutVertex': 'cutVertex', 'vbccSiz': 'vbccSiz', 'vbccArr': 'vbccArr', 'vbccl': 'vbccl', 'vbccr': 'vbccr', 'idx': 'idx', 'vbccCnt': 'vbccCnt', 'ans1': 'ans1', 'ans2': 'ans2'}
    MAXN = 0
    MAXM = 0
    t = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    cutVertex = None
    vbccSiz = None
    vbccArr = None
    vbccl = None
    vbccr = None
    idx = 0
    vbccCnt = 0
    ans1 = 0
    ans2 = 0
    @staticmethod
    def prepare():
        Code07_MiningFarm1.cntg = jcast('int', jset(Code07_MiningFarm1, 'cntd', jset(Code07_MiningFarm1, 'top', jset(Code07_MiningFarm1, 'idx', jset(Code07_MiningFarm1, 'vbccCnt', 0)))))
        i = jcast('int', 1)
        while (i < Code07_MiningFarm1.MAXN):
            jset(Code07_MiningFarm1.head, i, jset(Code07_MiningFarm1.dfn, i, jset(Code07_MiningFarm1.low, i, 0)))
            Code07_MiningFarm1.cutVertex[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        Code07_MiningFarm1.n = jcast('int', 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_MiningFarm1.nxt, ((_java_obj_1 := Code07_MiningFarm1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_MiningFarm1.head[u])
        Code07_MiningFarm1.to[Code07_MiningFarm1.cntg] = jcast('int', v)
        Code07_MiningFarm1.head[u] = jcast('int', Code07_MiningFarm1.cntg)

    @staticmethod
    def tarjan(u, root):
        u = jcast('int', u)
        root = jcast('boolean', root)
        jset(Code07_MiningFarm1.dfn, u, jset(Code07_MiningFarm1.low, u, ((_java_obj_4 := Code07_MiningFarm1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code07_MiningFarm1.sta, ((_java_obj_7 := Code07_MiningFarm1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        son = jcast('int', 0)
        e = jcast('int', Code07_MiningFarm1.head[u])
        while (e > 0):
            v = jcast('int', Code07_MiningFarm1.to[e])
            if (Code07_MiningFarm1.dfn[v] == 0):
                son = jcast('int', (son + 1))
                Code07_MiningFarm1.tarjan(v, False)
                jset(Code07_MiningFarm1.low, u, jstatic('Math', 'min', Code07_MiningFarm1.low[u], Code07_MiningFarm1.low[v]))
                if (Code07_MiningFarm1.low[v] >= Code07_MiningFarm1.dfn[u]):
                    if ((not root) or (son >= 2)):
                        Code07_MiningFarm1.cutVertex[u] = jcast('boolean', True)
                    Code07_MiningFarm1.vbccCnt = jcast('int', (Code07_MiningFarm1.vbccCnt + 1))
                    Code07_MiningFarm1.vbccSiz[Code07_MiningFarm1.vbccCnt] = jcast('int', 1)
                    jset(Code07_MiningFarm1.vbccArr, ((_java_obj_10 := Code07_MiningFarm1), (_java_key_11 := 'idx'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
                    Code07_MiningFarm1.vbccl[Code07_MiningFarm1.vbccCnt] = jcast('int', Code07_MiningFarm1.idx)
                    pop = 0
                    while True:
                        pop = jcast('int', Code07_MiningFarm1.sta[((_java_obj_13 := Code07_MiningFarm1), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code07_MiningFarm1.vbccSiz[Code07_MiningFarm1.vbccCnt] = jcast('int', (Code07_MiningFarm1.vbccSiz[Code07_MiningFarm1.vbccCnt] + 1))
                        jset(Code07_MiningFarm1.vbccArr, ((_java_obj_16 := Code07_MiningFarm1), (_java_key_17 := 'idx'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], pop)
                        if not ((pop != v)):
                            break
                    Code07_MiningFarm1.vbccr[Code07_MiningFarm1.vbccCnt] = jcast('int', Code07_MiningFarm1.idx)
            else:
                jset(Code07_MiningFarm1.low, u, jstatic('Math', 'min', Code07_MiningFarm1.low[u], Code07_MiningFarm1.dfn[v]))
            e = jcast('int', Code07_MiningFarm1.nxt[e])

    @staticmethod
    def compute():
        if (Code07_MiningFarm1.vbccCnt == 1):
            Code07_MiningFarm1.ans1 = jcast('long', 2)
            Code07_MiningFarm1.ans2 = jcast('long', jcast('int', jdiv(jcast('int', (Code07_MiningFarm1.n * jcast('int', (Code07_MiningFarm1.n - 1)))), 2)))
        else:
            Code07_MiningFarm1.ans1 = jcast('long', 0)
            Code07_MiningFarm1.ans2 = jcast('long', 1)
            i = jcast('int', 1)
            while (i <= Code07_MiningFarm1.vbccCnt):
                siz = jcast('int', Code07_MiningFarm1.vbccSiz[i])
                cut = jcast('int', 0)
                j = jcast('int', Code07_MiningFarm1.vbccl[i])
                while (j <= Code07_MiningFarm1.vbccr[i]):
                    if Code07_MiningFarm1.cutVertex[Code07_MiningFarm1.vbccArr[j]]:
                        cut = jcast('int', (cut + 1))
                    j = jcast('int', (j + 1))
                if (cut == 1):
                    Code07_MiningFarm1.ans1 = jcast('long', jcast('long', jadd(Code07_MiningFarm1.ans1, 1)))
                    Code07_MiningFarm1.ans2 = jcast('long', jcast('long', (Code07_MiningFarm1.ans2 * jcast('int', (siz - 1)))))
                i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_MiningFarm1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_MiningFarm1.t = jcast('int', 0)
        Code07_MiningFarm1.m = jcast('int', jcall(in_, 'nextInt'))
        while (Code07_MiningFarm1.m != 0):
            Code07_MiningFarm1.prepare()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i <= Code07_MiningFarm1.m):
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code07_MiningFarm1.n = jcast('int', jstatic('Math', 'max', Code07_MiningFarm1.n, u))
                Code07_MiningFarm1.n = jcast('int', jstatic('Math', 'max', Code07_MiningFarm1.n, v))
                Code07_MiningFarm1.addEdge(u, v)
                Code07_MiningFarm1.addEdge(v, u)
                i = jcast('int', (i + 1))
            Code07_MiningFarm1.tarjan(1, True)
            Code07_MiningFarm1.compute()
            jcall(out, 'println', jadd(jadd(jadd(jadd(jadd('Case ', ((_java_obj_19 := Code07_MiningFarm1), (_java_key_20 := 't'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3]), ': '), Code07_MiningFarm1.ans1), ' '), Code07_MiningFarm1.ans2))
            Code07_MiningFarm1.m = jcast('int', jcall(in_, 'nextInt'))
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
            return jcast('int', self.buffer[((_java_obj_22 := self), (_java_key_23 := 'ptr'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]])

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
            raise TypeError("No matching overload for Code07_MiningFarm1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_MiningFarm1.MAXN = jcast('int', 1001)
Code07_MiningFarm1.MAXM = jcast('int', 1001)
Code07_MiningFarm1.t = jcast('int', 0)
Code07_MiningFarm1.n = jcast('int', 0)
Code07_MiningFarm1.m = jcast('int', 0)
Code07_MiningFarm1.head = jarray('int', [Code07_MiningFarm1.MAXN])
Code07_MiningFarm1.nxt = jarray('int', [jcast('int', (Code07_MiningFarm1.MAXM << (1 & 31)))])
Code07_MiningFarm1.to = jarray('int', [jcast('int', (Code07_MiningFarm1.MAXM << (1 & 31)))])
Code07_MiningFarm1.cntg = jcast('int', 0)
Code07_MiningFarm1.dfn = jarray('int', [Code07_MiningFarm1.MAXN])
Code07_MiningFarm1.low = jarray('int', [Code07_MiningFarm1.MAXN])
Code07_MiningFarm1.cntd = jcast('int', 0)
Code07_MiningFarm1.sta = jarray('int', [Code07_MiningFarm1.MAXN])
Code07_MiningFarm1.top = jcast('int', 0)
Code07_MiningFarm1.cutVertex = jarray('boolean', [Code07_MiningFarm1.MAXN])
Code07_MiningFarm1.vbccSiz = jarray('int', [Code07_MiningFarm1.MAXN])
Code07_MiningFarm1.vbccArr = jarray('int', [jcast('int', (Code07_MiningFarm1.MAXN << (1 & 31)))])
Code07_MiningFarm1.vbccl = jarray('int', [Code07_MiningFarm1.MAXN])
Code07_MiningFarm1.vbccr = jarray('int', [Code07_MiningFarm1.MAXN])
Code07_MiningFarm1.idx = jcast('int', 0)
Code07_MiningFarm1.vbccCnt = jcast('int', 0)
Code07_MiningFarm1.ans1 = jcast('long', 0)
Code07_MiningFarm1.ans2 = jcast('long', 0)

if __name__ == '__main__':
    Code07_MiningFarm1.main([])
