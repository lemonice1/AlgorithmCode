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

# 红黑蛛网，Python版
# 一共n个节点，给定n-1条边，所有节点组成一棵树
# 每条边有两种边权，w为重量，c为颜色，颜色只有红和黑
# 考虑点对(x, y)的简单路径，x和y必须不同，假设红边数量r、黑边数量b
# 如果 2 * min(r, b) >= max(r, b)，那么路径是合法的
# 合法路径的收益 = 路径所有边的重量乘积，(x, y)和(y, x)的路径只算一次收益
# 打印所有合法路径的收益总乘积，结果对 1000000007 取余，不存在任何合法路径打印1
# 2 <= n <= 10^5
# 1 <= w <= 10^9 + 6
# 测试链接 : https://www.luogu.com.cn/problem/CF833D
# 测试链接 : https://codeforces.com/problemset/problem/833/D
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Cobweb1:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'n': 'n', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'weight1': 'weight1', 'color1': 'color1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'weight2': 'weight2', 'color2': 'color2', 'cnt2': 'cnt2', 'vis': 'vis', 'siz': 'siz', 'redKey': 'redKey', 'redPath': 'redPath', 'blackKey': 'blackKey', 'blackPath': 'blackPath', 'cnta': 'cnta', 'ans1': 'ans1', 'ans2': 'ans2'}
    MAXN = 0
    MOD = 0
    n = 0
    cntn = 0
    head1 = None
    next1 = None
    to1 = None
    weight1 = None
    color1 = None
    cnt1 = 0
    head2 = None
    next2 = None
    to2 = None
    weight2 = None
    color2 = None
    cnt2 = 0
    vis = None
    siz = None
    redKey = None
    redPath = None
    blackKey = None
    blackPath = None
    cnta = 0
    ans1 = 0
    ans2 = 0
    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p != 0):
            if (jcast('long', (p & 1)) != 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code02_Cobweb1.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code02_Cobweb1.MOD)))
        return jcast('long', ans)

    @staticmethod
    def addEdge1(u, v, w, c):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        c = jcast('int', c)
        jset(Code02_Cobweb1.next1, ((_java_obj_1 := Code02_Cobweb1), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Cobweb1.head1[u])
        Code02_Cobweb1.to1[Code02_Cobweb1.cnt1] = jcast('int', v)
        Code02_Cobweb1.weight1[Code02_Cobweb1.cnt1] = jcast('int', w)
        Code02_Cobweb1.color1[Code02_Cobweb1.cnt1] = jcast('int', c)
        Code02_Cobweb1.head1[u] = jcast('int', Code02_Cobweb1.cnt1)

    @staticmethod
    def addEdge2(u, v, w, c):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        c = jcast('int', c)
        jset(Code02_Cobweb1.next2, ((_java_obj_4 := Code02_Cobweb1), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code02_Cobweb1.head2[u])
        Code02_Cobweb1.to2[Code02_Cobweb1.cnt2] = jcast('int', v)
        Code02_Cobweb1.weight2[Code02_Cobweb1.cnt2] = jcast('int', w)
        Code02_Cobweb1.color2[Code02_Cobweb1.cnt2] = jcast('int', c)
        Code02_Cobweb1.head2[u] = jcast('int', Code02_Cobweb1.cnt2)

    @staticmethod
    def rebuild(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        last = jcast('int', 0)
        e = jcast('int', Code02_Cobweb1.head1[u])
        while (e > 0):
            v = jcast('int', Code02_Cobweb1.to1[e])
            w = jcast('int', Code02_Cobweb1.weight1[e])
            c = jcast('int', Code02_Cobweb1.color1[e])
            if (v != fa):
                if (last == 0):
                    last = jcast('int', u)
                    Code02_Cobweb1.addEdge2(u, v, w, c)
                    Code02_Cobweb1.addEdge2(v, u, w, c)
                else:
                    add = jcast('int', ((_java_obj_7 := Code02_Cobweb1), (_java_key_8 := 'cntn'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                    Code02_Cobweb1.addEdge2(last, add, 1, jcast('int', (-1)))
                    Code02_Cobweb1.addEdge2(add, last, 1, jcast('int', (-1)))
                    Code02_Cobweb1.addEdge2(add, v, w, c)
                    Code02_Cobweb1.addEdge2(v, add, w, c)
                    last = jcast('int', add)
                Code02_Cobweb1.rebuild(v, u)
            e = jcast('int', Code02_Cobweb1.next1[e])

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Cobweb1.siz[u] = jcast('int', 1)
        e = jcast('int', Code02_Cobweb1.head2[u])
        while (e > 0):
            v = jcast('int', Code02_Cobweb1.to2[e])
            if ((v != fa) and (not Code02_Cobweb1.vis[jcast('int', (e >> (1 & 31)))])):
                Code02_Cobweb1.getSize(v, u)
                Code02_Cobweb1.siz[u] = jcast('int', jcast('int', jadd(Code02_Cobweb1.siz[u], Code02_Cobweb1.siz[v])))
            e = jcast('int', Code02_Cobweb1.next2[e])

    @staticmethod
    def getCentroidEdge(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Cobweb1.getSize(u, fa)
        total = jcast('int', Code02_Cobweb1.siz[u])
        half = jcast('int', jcast('int', (total >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code02_Cobweb1.head2[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code02_Cobweb1.to2[e])
                        if (((v != fa) and (not Code02_Cobweb1.vis[jcast('int', (e >> (1 & 31)))])) and (Code02_Cobweb1.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_11:
                        if _java_control_11.label not in (None,):
                            raise
                    except JBreak as _java_control_11:
                        if _java_control_11.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code02_Cobweb1.next2[e])
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
        best = jcast('int', 0)
        edge = jcast('int', 0)
        e = jcast('int', Code02_Cobweb1.head2[u])
        while (e > 0):
            if (not Code02_Cobweb1.vis[jcast('int', (e >> (1 & 31)))]):
                v = jcast('int', Code02_Cobweb1.to2[e])
                sub = jcast('int', (jcast('int', (total - Code02_Cobweb1.siz[u])) if (v == fa) else Code02_Cobweb1.siz[v]))
                if (sub > best):
                    best = jcast('int', sub)
                    edge = jcast('int', e)
            e = jcast('int', Code02_Cobweb1.next2[e])
        return jcast('int', edge)

    @staticmethod
    def sort(key, path, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', key[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        while (i <= j):
            while (key[i] < pivot):
                i = jcast('int', (i + 1))
            while (key[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp1 = jcast('int', key[i])
                key[i] = jcast('int', key[j])
                key[j] = jcast('int', tmp1)
                tmp2 = jcast('long', path[i])
                path[i] = jcast('long', path[j])
                path[j] = jcast('long', tmp2)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code02_Cobweb1.sort(key, path, l, j)
        Code02_Cobweb1.sort(key, path, i, r)

    @staticmethod
    def lessThan(arr, len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', len)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (arr[mid] < num):
                ans = jcast('int', mid)
                l = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                r = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ans)

    @staticmethod
    def dfsLeft(u, fa, red, black, path):
        u = jcast('int', u)
        fa = jcast('int', fa)
        red = jcast('int', red)
        black = jcast('int', black)
        path = jcast('long', path)
        if (u <= Code02_Cobweb1.n):
            jset(Code02_Cobweb1.redKey, ((_java_obj_12 := Code02_Cobweb1), (_java_key_13 := 'cnta'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3], jcast('int', (jcast('int', (2 * red)) - black)))
            Code02_Cobweb1.redPath[Code02_Cobweb1.cnta] = jcast('long', path)
            Code02_Cobweb1.blackKey[Code02_Cobweb1.cnta] = jcast('int', jcast('int', (jcast('int', (2 * black)) - red)))
            Code02_Cobweb1.blackPath[Code02_Cobweb1.cnta] = jcast('long', path)
        e = jcast('int', Code02_Cobweb1.head2[u])
        while (e > 0):
            v = jcast('int', Code02_Cobweb1.to2[e])
            if ((v != fa) and (not Code02_Cobweb1.vis[jcast('int', (e >> (1 & 31)))])):
                nextRed = jcast('int', jcast('int', jadd(red, (1 if (Code02_Cobweb1.color2[e] == 0) else 0))))
                nextBlack = jcast('int', jcast('int', jadd(black, (1 if (Code02_Cobweb1.color2[e] == 1) else 0))))
                Code02_Cobweb1.dfsLeft(v, u, nextRed, nextBlack, jcast('long', jmod(jcast('long', (path * Code02_Cobweb1.weight2[e])), Code02_Cobweb1.MOD)))
            e = jcast('int', Code02_Cobweb1.next2[e])

    @staticmethod
    def dfsRight(u, fa, red, black, path):
        u = jcast('int', u)
        fa = jcast('int', fa)
        red = jcast('int', red)
        black = jcast('int', black)
        path = jcast('long', path)
        if (u <= Code02_Cobweb1.n):
            r = jcast('int', Code02_Cobweb1.lessThan(Code02_Cobweb1.redKey, Code02_Cobweb1.cnta, jcast('int', (black - jcast('int', (2 * red))))))
            b = jcast('int', Code02_Cobweb1.lessThan(Code02_Cobweb1.blackKey, Code02_Cobweb1.cnta, jcast('int', (red - jcast('int', (2 * black))))))
            if (r > 0):
                Code02_Cobweb1.ans2 = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code02_Cobweb1.ans2 * Code02_Cobweb1.power(path, r))), Code02_Cobweb1.MOD)) * Code02_Cobweb1.redPath[r])), Code02_Cobweb1.MOD)))
            if (b > 0):
                Code02_Cobweb1.ans2 = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code02_Cobweb1.ans2 * Code02_Cobweb1.power(path, b))), Code02_Cobweb1.MOD)) * Code02_Cobweb1.blackPath[b])), Code02_Cobweb1.MOD)))
        e = jcast('int', Code02_Cobweb1.head2[u])
        while (e > 0):
            v = jcast('int', Code02_Cobweb1.to2[e])
            if ((v != fa) and (not Code02_Cobweb1.vis[jcast('int', (e >> (1 & 31)))])):
                nextRed = jcast('int', jcast('int', jadd(red, (1 if (Code02_Cobweb1.color2[e] == 0) else 0))))
                nextBlack = jcast('int', jcast('int', jadd(black, (1 if (Code02_Cobweb1.color2[e] == 1) else 0))))
                Code02_Cobweb1.dfsRight(v, u, nextRed, nextBlack, jcast('long', jmod(jcast('long', (path * Code02_Cobweb1.weight2[e])), Code02_Cobweb1.MOD)))
            e = jcast('int', Code02_Cobweb1.next2[e])

    @staticmethod
    def calc(edge):
        edge = jcast('int', edge)
        Code02_Cobweb1.cnta = jcast('int', 0)
        v1 = jcast('int', Code02_Cobweb1.to2[edge])
        Code02_Cobweb1.dfsLeft(v1, 0, 0, 0, 1)
        Code02_Cobweb1.sort(Code02_Cobweb1.redKey, Code02_Cobweb1.redPath, 1, Code02_Cobweb1.cnta)
        Code02_Cobweb1.sort(Code02_Cobweb1.blackKey, Code02_Cobweb1.blackPath, 1, Code02_Cobweb1.cnta)
        i = jcast('int', 2)
        while (i <= Code02_Cobweb1.cnta):
            Code02_Cobweb1.redPath[i] = jcast('long', jcast('long', jmod(jcast('long', (Code02_Cobweb1.redPath[jcast('int', (i - 1))] * Code02_Cobweb1.redPath[i])), Code02_Cobweb1.MOD)))
            Code02_Cobweb1.blackPath[i] = jcast('long', jcast('long', jmod(jcast('long', (Code02_Cobweb1.blackPath[jcast('int', (i - 1))] * Code02_Cobweb1.blackPath[i])), Code02_Cobweb1.MOD)))
            i = jcast('int', (i + 1))
        v2 = jcast('int', Code02_Cobweb1.to2[jcast('int', (edge ^ 1))])
        red = jcast('int', (1 if (Code02_Cobweb1.color2[edge] == 0) else 0))
        black = jcast('int', (1 if (Code02_Cobweb1.color2[edge] == 1) else 0))
        Code02_Cobweb1.dfsRight(v2, 0, red, black, jcast('int', jmod(Code02_Cobweb1.weight2[edge], Code02_Cobweb1.MOD)))

    @staticmethod
    def getAns2(u):
        u = jcast('int', u)
        edge = jcast('int', Code02_Cobweb1.getCentroidEdge(u, 0))
        if (edge > 0):
            Code02_Cobweb1.vis[jcast('int', (edge >> (1 & 31)))] = jcast('boolean', True)
            Code02_Cobweb1.calc(edge)
            Code02_Cobweb1.getAns2(Code02_Cobweb1.to2[edge])
            Code02_Cobweb1.getAns2(Code02_Cobweb1.to2[jcast('int', (edge ^ 1))])

    @staticmethod
    def getAns1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Cobweb1.siz[u] = jcast('int', 1)
        e = jcast('int', Code02_Cobweb1.head1[u])
        while (e > 0):
            v = jcast('int', Code02_Cobweb1.to1[e])
            if (v != fa):
                Code02_Cobweb1.getAns1(v, u)
                Code02_Cobweb1.siz[u] = jcast('int', jcast('int', jadd(Code02_Cobweb1.siz[u], Code02_Cobweb1.siz[v])))
                Code02_Cobweb1.ans1 = jcast('long', jcast('long', jmod(jcast('long', (Code02_Cobweb1.ans1 * Code02_Cobweb1.power(Code02_Cobweb1.weight1[e], jcast('long', (jcast('long', Code02_Cobweb1.siz[v]) * jcast('int', (Code02_Cobweb1.n - Code02_Cobweb1.siz[v]))))))), Code02_Cobweb1.MOD)))
            e = jcast('int', Code02_Cobweb1.next1[e])

    @staticmethod
    def main(args):
        in_ = Code02_Cobweb1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Cobweb1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        c = 0
        while (i < Code02_Cobweb1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            Code02_Cobweb1.addEdge1(u, v, w, c)
            Code02_Cobweb1.addEdge1(v, u, w, c)
            i = jcast('int', (i + 1))
        Code02_Cobweb1.cntn = jcast('int', Code02_Cobweb1.n)
        Code02_Cobweb1.cnt2 = jcast('int', 1)
        Code02_Cobweb1.ans1 = jcast('long', jset(Code02_Cobweb1, 'ans2', 1))
        Code02_Cobweb1.getAns1(1, 0)
        Code02_Cobweb1.rebuild(1, 0)
        Code02_Cobweb1.getAns2(1)
        ans = jcast('long', jcast('long', jmod(jcast('long', (Code02_Cobweb1.ans1 * Code02_Cobweb1.power(Code02_Cobweb1.ans2, jcast('int', (Code02_Cobweb1.MOD - 2))))), Code02_Cobweb1.MOD)))
        jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_15 := self), (_java_key_16 := 'ptr'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))), _java_old_17)[4]])

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
            raise TypeError("No matching overload for Code02_Cobweb1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Cobweb1.MAXN = jcast('int', 200001)
Code02_Cobweb1.MOD = jcast('int', 1000000007)
Code02_Cobweb1.n = jcast('int', 0)
Code02_Cobweb1.cntn = jcast('int', 0)
Code02_Cobweb1.head1 = jarray('int', [Code02_Cobweb1.MAXN])
Code02_Cobweb1.next1 = jarray('int', [jcast('int', (Code02_Cobweb1.MAXN << (1 & 31)))])
Code02_Cobweb1.to1 = jarray('int', [jcast('int', (Code02_Cobweb1.MAXN << (1 & 31)))])
Code02_Cobweb1.weight1 = jarray('int', [jcast('int', (Code02_Cobweb1.MAXN << (1 & 31)))])
Code02_Cobweb1.color1 = jarray('int', [jcast('int', (Code02_Cobweb1.MAXN << (1 & 31)))])
Code02_Cobweb1.cnt1 = jcast('int', 0)
Code02_Cobweb1.head2 = jarray('int', [Code02_Cobweb1.MAXN])
Code02_Cobweb1.next2 = jarray('int', [jcast('int', (Code02_Cobweb1.MAXN << (1 & 31)))])
Code02_Cobweb1.to2 = jarray('int', [jcast('int', (Code02_Cobweb1.MAXN << (1 & 31)))])
Code02_Cobweb1.weight2 = jarray('int', [jcast('int', (Code02_Cobweb1.MAXN << (1 & 31)))])
Code02_Cobweb1.color2 = jarray('int', [jcast('int', (Code02_Cobweb1.MAXN << (1 & 31)))])
Code02_Cobweb1.cnt2 = jcast('int', 0)
Code02_Cobweb1.vis = jarray('boolean', [Code02_Cobweb1.MAXN])
Code02_Cobweb1.siz = jarray('int', [Code02_Cobweb1.MAXN])
Code02_Cobweb1.redKey = jarray('int', [Code02_Cobweb1.MAXN])
Code02_Cobweb1.redPath = jarray('long', [Code02_Cobweb1.MAXN])
Code02_Cobweb1.blackKey = jarray('int', [Code02_Cobweb1.MAXN])
Code02_Cobweb1.blackPath = jarray('long', [Code02_Cobweb1.MAXN])
Code02_Cobweb1.cnta = jcast('int', 0)
Code02_Cobweb1.ans1 = jcast('long', 0)
Code02_Cobweb1.ans2 = jcast('long', 0)

if __name__ == '__main__':
    Code02_Cobweb1.main([])
