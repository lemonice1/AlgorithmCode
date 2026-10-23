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

# 带修改的区间第k小，Python版
# 给定一个长度为n的数组arr，接下来是m条操作，每种操作是如下两种类型的一种
# 操作 C x y   : 把x位置的值修改成y
# 操作 Q x y v : 查询arr[x..y]范围上第v小的值
# 1 <= n、m <= 10^5
# 1 <= 数组中的值 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P2617
# 本题是讲解160，树套树模版题，现在作为带修改的整体二分模版题
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_DynamicRankings2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXE': 'MAXE', 'INF': 'INF', 'n': 'n', 'm': 'm', 'arr': 'arr', 'eid': 'eid', 'op': 'op', 'x': 'x', 'y': 'y', 'v': 'v', 'q': 'q', 'cnte': 'cnte', 'cntq': 'cntq', 'tree': 'tree', 'lset': 'lset', 'rset': 'rset', 'ans': 'ans'}
    MAXN = 0
    MAXE = 0
    INF = 0
    n = 0
    m = 0
    arr = None
    # 事件编号组成的数组
    eid = None
    # op == 1，代表修改事件，x处，值y，效果v
    # op == 2，代表查询事件，[x..y]范围上查询第v小，q表示问题的编号
    op = None
    x = None
    y = None
    v = None
    q = None
    cnte = 0
    cntq = 0
    # 树状数组
    tree = None
    # 整体二分
    lset = None
    rset = None
    # 查询的答案
    ans = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code02_DynamicRankings2.n):
            Code02_DynamicRankings2.tree[i] = jcast('int', jcast('int', jadd(Code02_DynamicRankings2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code02_DynamicRankings2.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code02_DynamicRankings2.tree[i])))
            i = jcast('int', jcast('int', (i - Code02_DynamicRankings2.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        return jcast('int', jcast('int', (Code02_DynamicRankings2.sum(r) - Code02_DynamicRankings2.sum(jcast('int', (l - 1))))))

    @staticmethod
    def compute(el, er, vl, vr):
        el = jcast('int', el)
        er = jcast('int', er)
        vl = jcast('int', vl)
        vr = jcast('int', vr)
        if (el > er):
            return
        if (vl == vr):
            i = jcast('int', el)
            while (i <= er):
                id = jcast('int', Code02_DynamicRankings2.eid[i])
                if (Code02_DynamicRankings2.op[id] == 2):
                    jset(Code02_DynamicRankings2.ans, Code02_DynamicRankings2.q[id], vl)
                i = jcast('int', (i + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(vl, vr)) >> (1 & 31))))
            lsiz = jcast('int', 0)
            rsiz = jcast('int', 0)
            i = jcast('int', el)
            while (i <= er):
                id = jcast('int', Code02_DynamicRankings2.eid[i])
                if (Code02_DynamicRankings2.op[id] == 1):
                    if (Code02_DynamicRankings2.y[id] <= mid):
                        Code02_DynamicRankings2.add(Code02_DynamicRankings2.x[id], Code02_DynamicRankings2.v[id])
                        jset(Code02_DynamicRankings2.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                    else:
                        jset(Code02_DynamicRankings2.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                else:
                    satisfy = jcast('int', Code02_DynamicRankings2.query(Code02_DynamicRankings2.x[id], Code02_DynamicRankings2.y[id]))
                    if (Code02_DynamicRankings2.v[id] <= satisfy):
                        jset(Code02_DynamicRankings2.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                    else:
                        Code02_DynamicRankings2.v[id] = jcast('int', jcast('int', (Code02_DynamicRankings2.v[id] - satisfy)))
                        jset(Code02_DynamicRankings2.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= lsiz):
                Code02_DynamicRankings2.eid[jcast('int', (jcast('int', jadd(el, i)) - 1))] = jcast('int', Code02_DynamicRankings2.lset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                Code02_DynamicRankings2.eid[jcast('int', (jcast('int', jadd(jcast('int', jadd(el, lsiz)), i)) - 1))] = jcast('int', Code02_DynamicRankings2.rset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= lsiz):
                id = jcast('int', Code02_DynamicRankings2.lset[i])
                if ((Code02_DynamicRankings2.op[id] == 1) and (Code02_DynamicRankings2.y[id] <= mid)):
                    Code02_DynamicRankings2.add(Code02_DynamicRankings2.x[id], jcast('int', (-Code02_DynamicRankings2.v[id])))
                i = jcast('int', (i + 1))
            Code02_DynamicRankings2.compute(el, jcast('int', (jcast('int', jadd(el, lsiz)) - 1)), vl, mid)
            Code02_DynamicRankings2.compute(jcast('int', jadd(el, lsiz)), er, jcast('int', jadd(mid, 1)), vr)

    @staticmethod
    def main(args):
        in_ = Code02_DynamicRankings2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_DynamicRankings2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_DynamicRankings2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_DynamicRankings2.n):
            jset(Code02_DynamicRankings2.arr, i, jcall(in_, 'nextInt'))
            jset(Code02_DynamicRankings2.op, ((_java_obj_1 := Code02_DynamicRankings2), (_java_key_2 := 'cnte'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], 1)
            Code02_DynamicRankings2.x[Code02_DynamicRankings2.cnte] = jcast('int', i)
            Code02_DynamicRankings2.y[Code02_DynamicRankings2.cnte] = jcast('int', Code02_DynamicRankings2.arr[i])
            Code02_DynamicRankings2.v[Code02_DynamicRankings2.cnte] = jcast('int', 1)
            i = jcast('int', (i + 1))
        type = jchar(0)
        i = jcast('int', 1)
        while (i <= Code02_DynamicRankings2.m):
            type = jcast('char', jcall(in_, 'nextChar'))
            if (type == jchar('C')):
                a = jcast('int', jcall(in_, 'nextInt'))
                b = jcast('int', jcall(in_, 'nextInt'))
                jset(Code02_DynamicRankings2.op, ((_java_obj_4 := Code02_DynamicRankings2), (_java_key_5 := 'cnte'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], 1)
                Code02_DynamicRankings2.x[Code02_DynamicRankings2.cnte] = jcast('int', a)
                Code02_DynamicRankings2.y[Code02_DynamicRankings2.cnte] = jcast('int', Code02_DynamicRankings2.arr[a])
                Code02_DynamicRankings2.v[Code02_DynamicRankings2.cnte] = jcast('int', jcast('int', (-1)))
                jset(Code02_DynamicRankings2.op, ((_java_obj_7 := Code02_DynamicRankings2), (_java_key_8 := 'cnte'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], 1)
                Code02_DynamicRankings2.x[Code02_DynamicRankings2.cnte] = jcast('int', a)
                Code02_DynamicRankings2.y[Code02_DynamicRankings2.cnte] = jcast('int', b)
                Code02_DynamicRankings2.v[Code02_DynamicRankings2.cnte] = jcast('int', 1)
                Code02_DynamicRankings2.arr[a] = jcast('int', b)
            else:
                jset(Code02_DynamicRankings2.op, ((_java_obj_10 := Code02_DynamicRankings2), (_java_key_11 := 'cnte'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], 2)
                jset(Code02_DynamicRankings2.x, Code02_DynamicRankings2.cnte, jcall(in_, 'nextInt'))
                jset(Code02_DynamicRankings2.y, Code02_DynamicRankings2.cnte, jcall(in_, 'nextInt'))
                jset(Code02_DynamicRankings2.v, Code02_DynamicRankings2.cnte, jcall(in_, 'nextInt'))
                jset(Code02_DynamicRankings2.q, Code02_DynamicRankings2.cnte, ((_java_obj_13 := Code02_DynamicRankings2), (_java_key_14 := 'cntq'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_DynamicRankings2.cnte):
            Code02_DynamicRankings2.eid[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code02_DynamicRankings2.compute(1, Code02_DynamicRankings2.cnte, 0, Code02_DynamicRankings2.INF)
        i = jcast('int', 1)
        while (i <= Code02_DynamicRankings2.cntq):
            jcall(out, 'println', Code02_DynamicRankings2.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_DynamicRankings2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DynamicRankings2.MAXN = jcast('int', 100001)
Code02_DynamicRankings2.MAXE = jcast('int', jcast('int', (Code02_DynamicRankings2.MAXN << (2 & 31))))
Code02_DynamicRankings2.INF = jcast('int', 1000000001)
Code02_DynamicRankings2.n = jcast('int', 0)
Code02_DynamicRankings2.m = jcast('int', 0)
Code02_DynamicRankings2.arr = jarray('int', [Code02_DynamicRankings2.MAXN])
Code02_DynamicRankings2.eid = jarray('int', [Code02_DynamicRankings2.MAXE])
Code02_DynamicRankings2.op = jarray('int', [Code02_DynamicRankings2.MAXE])
Code02_DynamicRankings2.x = jarray('int', [Code02_DynamicRankings2.MAXE])
Code02_DynamicRankings2.y = jarray('int', [Code02_DynamicRankings2.MAXE])
Code02_DynamicRankings2.v = jarray('int', [Code02_DynamicRankings2.MAXE])
Code02_DynamicRankings2.q = jarray('int', [Code02_DynamicRankings2.MAXE])
Code02_DynamicRankings2.cnte = jcast('int', 0)
Code02_DynamicRankings2.cntq = jcast('int', 0)
Code02_DynamicRankings2.tree = jarray('int', [Code02_DynamicRankings2.MAXN])
Code02_DynamicRankings2.lset = jarray('int', [Code02_DynamicRankings2.MAXE])
Code02_DynamicRankings2.rset = jarray('int', [Code02_DynamicRankings2.MAXE])
Code02_DynamicRankings2.ans = jarray('int', [Code02_DynamicRankings2.MAXN])

if __name__ == '__main__':
    Code02_DynamicRankings2.main([])
