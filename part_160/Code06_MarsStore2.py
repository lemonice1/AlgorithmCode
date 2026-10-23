# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 火星商店，Python版
# 有n个商店，每个商店只有一种初始商品，给出每个商店的初始商品价格
# 有m条操作，每种操作是如下两种类型中的一种
# 操作 0 s v     : 操作0会让天数+1，第s号商店，在这天增加了价格为v的新商品
# 操作 1 l r x d : 只能在商店[l..r]中挑选，只能挑选初始商品或d天内出现的新商品
# 只能挑选一件商品，打印 商品的价格 ^ x 的最大值
# 注意，只有操作0能让天数+1，操作1不会
# 0 <= 所有数据 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4585
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_MarsStore2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'BIT': 'BIT', 'n': 'n', 'm': 'm', 't': 't', 'arr': 'arr', 'op': 'op', 's': 's', 'v': 'v', 'sl': 'sl', 'sr': 'sr', 'x': 'x', 'd': 'd', 'tim': 'tim', 'root': 'root', 'tree': 'tree', 'pass': 'pass_', 'cntt': 'cntt', 'headp': 'headp', 'nextp': 'nextp', 'pid': 'pid', 'cntp': 'cntp', 'headb': 'headb', 'nextb': 'nextb', 'bid': 'bid', 'cntb': 'cntb', 'product': 'product', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    BIT = 0
    n = 0
    m = 0
    t = 0
    arr = None
    op = None
    s = None
    v = None
    sl = None
    sr = None
    x = None
    d = None
    tim = None
    root = None
    tree = None
    pass_ = None
    cntt = 0
    headp = None
    nextp = None
    pid = None
    cntp = 0
    headb = None
    nextb = None
    bid = None
    cntb = 0
    # 每个商品(所属的商店编号，该商品的价格)
    product = None
    ans = None
    # 可持久化前缀树
    # 基于i版本的树，添加num，返回新版本的编号
    @staticmethod
    def insert(num, i):
        num = jcast('int', num)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_1 := Code06_MarsStore2), (_java_key_2 := 'cntt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        jset(Code06_MarsStore2.tree[rt], 0, Code06_MarsStore2.tree[i][0])
        jset(Code06_MarsStore2.tree[rt], 1, Code06_MarsStore2.tree[i][1])
        Code06_MarsStore2.pass_[rt] = jcast('int', jcast('int', jadd(Code06_MarsStore2.pass_[i], 1)))
        b = jcast('int', Code06_MarsStore2.BIT)
        path = 0
        pre = jcast('int', rt)
        cur = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            i = jcast('int', Code06_MarsStore2.tree[i][path])
            cur = jcast('int', ((_java_obj_4 := Code06_MarsStore2), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            jset(Code06_MarsStore2.tree[cur], 0, Code06_MarsStore2.tree[i][0])
            jset(Code06_MarsStore2.tree[cur], 1, Code06_MarsStore2.tree[i][1])
            Code06_MarsStore2.pass_[cur] = jcast('int', jcast('int', jadd(Code06_MarsStore2.pass_[i], 1)))
            jset(Code06_MarsStore2.tree[pre], path, cur)
            b = jcast('int', (b - 1))
            pre = jcast('int', cur)
        return jcast('int', rt)

    # 可持久化前缀树
    # 根据(v版本 - u版本)的数据状况，看看哪个数字 ^ num能得到最大值并返回
    @staticmethod
    def query(num, u, v):
        num = jcast('int', num)
        u = jcast('int', u)
        v = jcast('int', v)
        ans = jcast('int', 0)
        b = jcast('int', Code06_MarsStore2.BIT)
        path = 0
        best = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            best = jcast('int', jcast('int', (path ^ 1)))
            if (Code06_MarsStore2.pass_[Code06_MarsStore2.tree[v][best]] > Code06_MarsStore2.pass_[Code06_MarsStore2.tree[u][best]]):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', (1 << (b & 31))))))
                u = jcast('int', Code06_MarsStore2.tree[u][best])
                v = jcast('int', Code06_MarsStore2.tree[v][best])
            else:
                u = jcast('int', Code06_MarsStore2.tree[u][path])
                v = jcast('int', Code06_MarsStore2.tree[v][path])
            b = jcast('int', (b - 1))
        return jcast('int', ans)

    @staticmethod
    def addInfoP(i, pi):
        i = jcast('int', i)
        pi = jcast('int', pi)
        jset(Code06_MarsStore2.nextp, ((_java_obj_7 := Code06_MarsStore2), (_java_key_8 := 'cntp'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code06_MarsStore2.headp[i])
        Code06_MarsStore2.pid[Code06_MarsStore2.cntp] = jcast('int', pi)
        Code06_MarsStore2.headp[i] = jcast('int', Code06_MarsStore2.cntp)

    @staticmethod
    def addInfoB(i, bi):
        i = jcast('int', i)
        bi = jcast('int', bi)
        jset(Code06_MarsStore2.nextb, ((_java_obj_10 := Code06_MarsStore2), (_java_key_11 := 'cntb'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code06_MarsStore2.headb[i])
        Code06_MarsStore2.bid[Code06_MarsStore2.cntb] = jcast('int', bi)
        Code06_MarsStore2.headb[i] = jcast('int', Code06_MarsStore2.cntb)

    # 当前商品编号pi，沿途经过的所有区间，都把该商品加上
    @staticmethod
    def addProduct(jobi, pi, l, r, i):
        jobi = jcast('int', jobi)
        pi = jcast('int', pi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        Code06_MarsStore2.addInfoP(i, pi)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code06_MarsStore2.addProduct(jobi, pi, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code06_MarsStore2.addProduct(jobi, pi, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    # 当前购买行为编号bi，命中的线段树区间，把该购买行为加上
    @staticmethod
    def addBuy(jobl, jobr, bi, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        bi = jcast('int', bi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_MarsStore2.addInfoB(i, bi)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code06_MarsStore2.addBuy(jobl, jobr, bi, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_MarsStore2.addBuy(jobl, jobr, bi, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def lower(size, num):
        size = jcast('int', size)
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', size)
        ans = jcast('int', jcast('int', jadd(size, 1)))
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code06_MarsStore2.product[mid][0] >= num):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def upper(size, num):
        size = jcast('int', size)
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', size)
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code06_MarsStore2.product[mid][0] <= num):
                ans = jcast('int', mid)
                l = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                r = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ans)

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        pcnt = jcast('int', 0)
        e = jcast('int', Code06_MarsStore2.headp[i])
        while (e > 0):
            jset(Code06_MarsStore2.product[(pcnt := jcast('int', (pcnt + (1))))], 0, Code06_MarsStore2.s[Code06_MarsStore2.pid[e]])
            jset(Code06_MarsStore2.product[pcnt], 1, Code06_MarsStore2.v[Code06_MarsStore2.pid[e]])
            e = jcast('int', Code06_MarsStore2.nextp[e])
        jstatic('Arrays', 'sort', Code06_MarsStore2.product, 1, jcast('int', jadd(pcnt, 1)), (lambda a, b: (a[0] - b[0])))
        Code06_MarsStore2.cntt = jcast('int', 0)
        k = jcast('int', 1)
        while (k <= pcnt):
            jset(Code06_MarsStore2.root, k, Code06_MarsStore2.insert(Code06_MarsStore2.product[k][1], Code06_MarsStore2.root[jcast('int', (k - 1))]))
            k = jcast('int', (k + 1))
        e = jcast('int', Code06_MarsStore2.headb[i])
        id = 0
        pre = 0
        post = 0
        while (e > 0):
            id = jcast('int', Code06_MarsStore2.bid[e])
            pre = jcast('int', jcast('int', (Code06_MarsStore2.lower(pcnt, Code06_MarsStore2.sl[id]) - 1)))
            post = jcast('int', Code06_MarsStore2.upper(pcnt, Code06_MarsStore2.sr[id]))
            jset(Code06_MarsStore2.ans, id, jstatic('Math', 'max', Code06_MarsStore2.ans[id], Code06_MarsStore2.query(Code06_MarsStore2.x[id], Code06_MarsStore2.root[pre], Code06_MarsStore2.root[post])))
            e = jcast('int', Code06_MarsStore2.nextb[e])
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_MarsStore2.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code06_MarsStore2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code06_MarsStore2.n):
            jset(Code06_MarsStore2.root, i, Code06_MarsStore2.insert(Code06_MarsStore2.arr[i], Code06_MarsStore2.root[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_MarsStore2.m):
            if (Code06_MarsStore2.op[i] == 0):
                Code06_MarsStore2.addProduct(Code06_MarsStore2.tim[i], i, 1, Code06_MarsStore2.t, 1)
            else:
                jset(Code06_MarsStore2.ans, i, Code06_MarsStore2.query(Code06_MarsStore2.x[i], Code06_MarsStore2.root[jcast('int', (Code06_MarsStore2.sl[i] - 1))], Code06_MarsStore2.root[Code06_MarsStore2.sr[i]]))
                start = jcast('int', jstatic('Math', 'max', jcast('int', jadd(jcast('int', (Code06_MarsStore2.tim[i] - Code06_MarsStore2.d[i])), 1)), 1))
                if (start <= Code06_MarsStore2.tim[i]):
                    Code06_MarsStore2.addBuy(start, Code06_MarsStore2.tim[i], i, 1, Code06_MarsStore2.t, 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code06_MarsStore2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_MarsStore2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_MarsStore2.m = jcast('int', jcall(in_, 'nextInt'))
        Code06_MarsStore2.t = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_MarsStore2.n):
            jset(Code06_MarsStore2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_MarsStore2.m):
            jset(Code06_MarsStore2.op, i, jcall(in_, 'nextInt'))
            if (Code06_MarsStore2.op[i] == 0):
                Code06_MarsStore2.t = jcast('int', (Code06_MarsStore2.t + 1))
                jset(Code06_MarsStore2.s, i, jcall(in_, 'nextInt'))
                jset(Code06_MarsStore2.v, i, jcall(in_, 'nextInt'))
            else:
                jset(Code06_MarsStore2.sl, i, jcall(in_, 'nextInt'))
                jset(Code06_MarsStore2.sr, i, jcall(in_, 'nextInt'))
                jset(Code06_MarsStore2.x, i, jcall(in_, 'nextInt'))
                jset(Code06_MarsStore2.d, i, jcall(in_, 'nextInt'))
            Code06_MarsStore2.tim[i] = jcast('int', Code06_MarsStore2.t)
            i = jcast('int', (i + 1))
        Code06_MarsStore2.prepare()
        Code06_MarsStore2.dfs(1, Code06_MarsStore2.t, 1)
        i = jcast('int', 1)
        while (i <= Code06_MarsStore2.m):
            if (Code06_MarsStore2.op[i] == 1):
                jcall(out, 'println', Code06_MarsStore2.ans[i])
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
            return jcast('byte', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

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
            raise TypeError("No matching overload for Code06_MarsStore2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_MarsStore2.MAXN = jcast('int', 100001)
Code06_MarsStore2.MAXT = jcast('int', 2000001)
Code06_MarsStore2.BIT = jcast('int', 16)
Code06_MarsStore2.n = jcast('int', 0)
Code06_MarsStore2.m = jcast('int', 0)
Code06_MarsStore2.t = jcast('int', 0)
Code06_MarsStore2.arr = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.op = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.s = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.v = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.sl = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.sr = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.x = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.d = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.tim = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.root = jarray('int', [Code06_MarsStore2.MAXN])
Code06_MarsStore2.tree = jarray('int', [Code06_MarsStore2.MAXT, 2])
Code06_MarsStore2.pass_ = jarray('int', [Code06_MarsStore2.MAXT])
Code06_MarsStore2.cntt = jcast('int', 0)
Code06_MarsStore2.headp = jarray('int', [jcast('int', (Code06_MarsStore2.MAXN << (2 & 31)))])
Code06_MarsStore2.nextp = jarray('int', [Code06_MarsStore2.MAXT])
Code06_MarsStore2.pid = jarray('int', [Code06_MarsStore2.MAXT])
Code06_MarsStore2.cntp = jcast('int', 0)
Code06_MarsStore2.headb = jarray('int', [jcast('int', (Code06_MarsStore2.MAXN << (2 & 31)))])
Code06_MarsStore2.nextb = jarray('int', [Code06_MarsStore2.MAXT])
Code06_MarsStore2.bid = jarray('int', [Code06_MarsStore2.MAXT])
Code06_MarsStore2.cntb = jcast('int', 0)
Code06_MarsStore2.product = jarray('int', [Code06_MarsStore2.MAXN, 2])
Code06_MarsStore2.ans = jarray('int', [Code06_MarsStore2.MAXN])

if __name__ == '__main__':
    Code06_MarsStore2.main([])
