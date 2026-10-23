# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 博物馆劫案，Python版
# 给定n件商品，商品有价值v和重量w，1~n号商品加入集合s
# 接下来有q个操作，每种操作是如下三种类型中的一种
# 操作 1 x y : 集合s中增加价值x、重量y的商品，商品编号自增得到
# 操作 2 x   : 集合s中删除编号为x的商品，删除时保证x号商品存在
# 操作 3     : 查询当前的f(s)
# 定义a(s, m) = 集合s中，挑选商品总重量<=m，能获得的最大价值
# 给定正数k、BAS、MOD，定义f(s) = ∑(m = 1...k) (a(s, m) * BAS的m-1次方 % MOD)
# 1 <= n <= 5 * 10^3    1 <= q <= 3 * 10^4
# 1 <= k、每件商品重量 <= 10^3    1 <= 每件商品价值 <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/CF601E
# 测试链接 : https://codeforces.com/problemset/problem/601/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MuseumRobbery2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXQ': 'MAXQ', 'MAXK': 'MAXK', 'MAXT': 'MAXT', 'DEEP': 'DEEP', 'BAS': 'BAS', 'MOD': 'MOD', 'n': 'n', 'k': 'k', 'q': 'q', 'v': 'v', 'w': 'w', 'op': 'op', 'x': 'x', 'y': 'y', 'from': 'from_', 'to': 'to', 'head': 'head', 'next': 'next', 'tov': 'tov', 'tow': 'tow', 'cnt': 'cnt', 'dp': 'dp', 'backup': 'backup', 'ans': 'ans'}
    MAXN = 0
    MAXQ = 0
    MAXK = 0
    MAXT = 0
    DEEP = 0
    BAS = 0
    MOD = 0
    n = 0
    k = 0
    q = 0
    v = None
    w = None
    op = None
    x = None
    y = None
    # 第i号商品的生效时间段，从from[i]持续到to[i]
    from_ = None
    to = None
    # 时间轴线段树的区间上挂上生效的商品，价值v，重量w
    head = None
    next = None
    tov = None
    tow = None
    cnt = 0
    # 动态规划表
    dp = None
    # 动态规划表的备份
    backup = None
    # 答案
    ans = None
    @staticmethod
    def clone(a, b):
        i = jcast('int', 0)
        while (i <= Code01_MuseumRobbery2.k):
            a[i] = jcast('long', b[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(i, v, w):
        i = jcast('int', i)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code01_MuseumRobbery2.next, ((_java_obj_1 := Code01_MuseumRobbery2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_MuseumRobbery2.head[i])
        Code01_MuseumRobbery2.tov[Code01_MuseumRobbery2.cnt] = jcast('int', v)
        Code01_MuseumRobbery2.tow[Code01_MuseumRobbery2.cnt] = jcast('int', w)
        Code01_MuseumRobbery2.head[i] = jcast('int', Code01_MuseumRobbery2.cnt)

    @staticmethod
    def add(jobl, jobr, jobv, jobw, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        jobw = jcast('int', jobw)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_MuseumRobbery2.addEdge(i, jobv, jobw)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code01_MuseumRobbery2.add(jobl, jobr, jobv, jobw, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_MuseumRobbery2.add(jobl, jobr, jobv, jobw, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i, dep):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dep = jcast('int', dep)
        Code01_MuseumRobbery2.clone(Code01_MuseumRobbery2.backup[dep], Code01_MuseumRobbery2.dp)
        e = jcast('int', Code01_MuseumRobbery2.head[i])
        while (e > 0):
            v = jcast('int', Code01_MuseumRobbery2.tov[e])
            w = jcast('int', Code01_MuseumRobbery2.tow[e])
            j = jcast('int', Code01_MuseumRobbery2.k)
            while (j >= w):
                jset(Code01_MuseumRobbery2.dp, j, jstatic('Math', 'max', Code01_MuseumRobbery2.dp[j], jcast('long', jadd(Code01_MuseumRobbery2.dp[jcast('int', (j - w))], v))))
                j = jcast('int', (j - 1))
            e = jcast('int', Code01_MuseumRobbery2.next[e])
        if (l == r):
            if (Code01_MuseumRobbery2.op[l] == 3):
                ret = jcast('long', 0)
                base = jcast('long', 1)
                j = jcast('int', 1)
                while (j <= Code01_MuseumRobbery2.k):
                    ret = jcast('long', jcast('long', jmod(jcast('long', jadd(ret, jcast('long', (Code01_MuseumRobbery2.dp[j] * base)))), Code01_MuseumRobbery2.MOD)))
                    base = jcast('long', jcast('long', jmod(jcast('long', (base * Code01_MuseumRobbery2.BAS)), Code01_MuseumRobbery2.MOD)))
                    j = jcast('int', (j + 1))
                Code01_MuseumRobbery2.ans[l] = jcast('long', ret)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_MuseumRobbery2.dfs(l, mid, jcast('int', (i << (1 & 31))), jcast('int', jadd(dep, 1)))
            Code01_MuseumRobbery2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)), jcast('int', jadd(dep, 1)))
        Code01_MuseumRobbery2.clone(Code01_MuseumRobbery2.dp, Code01_MuseumRobbery2.backup[dep])

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code01_MuseumRobbery2.n):
            Code01_MuseumRobbery2.from_[i] = jcast('int', 1)
            Code01_MuseumRobbery2.to[i] = jcast('int', Code01_MuseumRobbery2.q)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_MuseumRobbery2.q):
            if (Code01_MuseumRobbery2.op[i] == 1):
                Code01_MuseumRobbery2.n = jcast('int', (Code01_MuseumRobbery2.n + 1))
                Code01_MuseumRobbery2.v[Code01_MuseumRobbery2.n] = jcast('int', Code01_MuseumRobbery2.x[i])
                Code01_MuseumRobbery2.w[Code01_MuseumRobbery2.n] = jcast('int', Code01_MuseumRobbery2.y[i])
                Code01_MuseumRobbery2.from_[Code01_MuseumRobbery2.n] = jcast('int', i)
                Code01_MuseumRobbery2.to[Code01_MuseumRobbery2.n] = jcast('int', Code01_MuseumRobbery2.q)
            else:
                if (Code01_MuseumRobbery2.op[i] == 2):
                    jset(Code01_MuseumRobbery2.to, Code01_MuseumRobbery2.x[i], jcast('int', (i - 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_MuseumRobbery2.n):
            if (Code01_MuseumRobbery2.from_[i] <= Code01_MuseumRobbery2.to[i]):
                Code01_MuseumRobbery2.add(Code01_MuseumRobbery2.from_[i], Code01_MuseumRobbery2.to[i], Code01_MuseumRobbery2.v[i], Code01_MuseumRobbery2.w[i], 1, Code01_MuseumRobbery2.q, 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code01_MuseumRobbery2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_MuseumRobbery2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_MuseumRobbery2.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_MuseumRobbery2.n):
            jset(Code01_MuseumRobbery2.v, i, jcall(in_, 'nextInt'))
            jset(Code01_MuseumRobbery2.w, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_MuseumRobbery2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_MuseumRobbery2.q):
            jset(Code01_MuseumRobbery2.op, i, jcall(in_, 'nextInt'))
            if (Code01_MuseumRobbery2.op[i] == 1):
                jset(Code01_MuseumRobbery2.x, i, jcall(in_, 'nextInt'))
                jset(Code01_MuseumRobbery2.y, i, jcall(in_, 'nextInt'))
            else:
                if (Code01_MuseumRobbery2.op[i] == 2):
                    jset(Code01_MuseumRobbery2.x, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_MuseumRobbery2.prepare()
        Code01_MuseumRobbery2.dfs(1, Code01_MuseumRobbery2.q, 1, 1)
        i = jcast('int', 1)
        while (i <= Code01_MuseumRobbery2.q):
            if (Code01_MuseumRobbery2.op[i] == 3):
                jcall(out, 'println', Code01_MuseumRobbery2.ans[i])
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_MuseumRobbery2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MuseumRobbery2.MAXN = jcast('int', 40001)
Code01_MuseumRobbery2.MAXQ = jcast('int', 30001)
Code01_MuseumRobbery2.MAXK = jcast('int', 1001)
Code01_MuseumRobbery2.MAXT = jcast('int', 1000001)
Code01_MuseumRobbery2.DEEP = jcast('int', 20)
Code01_MuseumRobbery2.BAS = jcast('int', 10000019)
Code01_MuseumRobbery2.MOD = jcast('int', 1000000007)
Code01_MuseumRobbery2.n = jcast('int', 0)
Code01_MuseumRobbery2.k = jcast('int', 0)
Code01_MuseumRobbery2.q = jcast('int', 0)
Code01_MuseumRobbery2.v = jarray('int', [Code01_MuseumRobbery2.MAXN])
Code01_MuseumRobbery2.w = jarray('int', [Code01_MuseumRobbery2.MAXN])
Code01_MuseumRobbery2.op = jarray('int', [Code01_MuseumRobbery2.MAXQ])
Code01_MuseumRobbery2.x = jarray('int', [Code01_MuseumRobbery2.MAXQ])
Code01_MuseumRobbery2.y = jarray('int', [Code01_MuseumRobbery2.MAXQ])
Code01_MuseumRobbery2.from_ = jarray('int', [Code01_MuseumRobbery2.MAXN])
Code01_MuseumRobbery2.to = jarray('int', [Code01_MuseumRobbery2.MAXN])
Code01_MuseumRobbery2.head = jarray('int', [jcast('int', (Code01_MuseumRobbery2.MAXQ << (2 & 31)))])
Code01_MuseumRobbery2.next = jarray('int', [Code01_MuseumRobbery2.MAXT])
Code01_MuseumRobbery2.tov = jarray('int', [Code01_MuseumRobbery2.MAXT])
Code01_MuseumRobbery2.tow = jarray('int', [Code01_MuseumRobbery2.MAXT])
Code01_MuseumRobbery2.cnt = jcast('int', 0)
Code01_MuseumRobbery2.dp = jarray('long', [Code01_MuseumRobbery2.MAXK])
Code01_MuseumRobbery2.backup = jarray('long', [Code01_MuseumRobbery2.DEEP, Code01_MuseumRobbery2.MAXK])
Code01_MuseumRobbery2.ans = jarray('long', [Code01_MuseumRobbery2.MAXQ])

if __name__ == '__main__':
    Code01_MuseumRobbery2.main([])
