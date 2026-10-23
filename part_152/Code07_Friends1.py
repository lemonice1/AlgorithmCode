# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 前m大两两异或值的和，Python版
# 本题只用到了经典前缀树，没有用到可持久化前缀树
# 给定一个长度为n的数组arr，下标1~n
# 你可以随意选两个不同位置的数字进行异或，得到两两异或值，顺序不同的话，算做一个两两异或值
# 那么，两两异或值，就有第1大、第2大...
# 返回前k大两两异或值的累加和，答案对1000000007取模
# 1 <= n <= 5 * 10^4
# 0 <= k <= n * (n-1) / 2
# 0 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/CF241B
# 测试链接 : https://codeforces.com/problemset/problem/241/B
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Friends1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'BIT': 'BIT', 'MOD': 'MOD', 'INV2': 'INV2', 'n': 'n', 'k': 'k', 'arr': 'arr', 'tree': 'tree', 'pass': 'pass_', 'cnt': 'cnt', 'sum': 'sum'}
    MAXN = 0
    MAXT = 0
    BIT = 0
    MOD = 0
    INV2 = 0
    n = 0
    k = 0
    arr = None
    tree = None
    pass_ = None
    cnt = 0
    sum = None
    @staticmethod
    def insert(num):
        num = jcast('int', num)
        cur = jcast('int', 1)
        Code07_Friends1.pass_[1] = jcast('int', (Code07_Friends1.pass_[1] + 1))
        b = jcast('int', Code07_Friends1.BIT)
        path = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            if (Code07_Friends1.tree[cur][path] == 0):
                jset(Code07_Friends1.tree[cur], path, ((_java_obj_1 := Code07_Friends1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            cur = jcast('int', Code07_Friends1.tree[cur][path])
            Code07_Friends1.pass_[cur] = jcast('int', (Code07_Friends1.pass_[cur] + 1))
            b = jcast('int', (b - 1))

    @staticmethod
    def dfs(i, h, s):
        i = jcast('int', i)
        h = jcast('int', h)
        s = jcast('int', s)
        if (i == 0):
            return
        if (h == 0):
            j = jcast('int', 0)
            while (j <= Code07_Friends1.BIT):
                if (jcast('int', (jcast('int', (s >> (j & 31))) & 1)) == 1):
                    jset(Code07_Friends1.sum[i], j, Code07_Friends1.pass_[i])
                j = jcast('int', (j + 1))
        else:
            Code07_Friends1.dfs(Code07_Friends1.tree[i][0], jcast('int', (h - 1)), s)
            Code07_Friends1.dfs(Code07_Friends1.tree[i][1], jcast('int', (h - 1)), jcast('int', (s | jcast('int', (1 << (jcast('int', (h - 1)) & 31))))))
            j = jcast('int', 0)
            while (j <= Code07_Friends1.BIT):
                jset(Code07_Friends1.sum[i], j, jcast('int', jadd(Code07_Friends1.sum[Code07_Friends1.tree[i][0]][j], Code07_Friends1.sum[Code07_Friends1.tree[i][1]][j])))
                j = jcast('int', (j + 1))

    @staticmethod
    def moreEqual(x):
        x = jcast('int', x)
        ans = jcast('long', 0)
        i = jcast('int', 1)
        num = 0
        cur = 0
        while (i <= Code07_Friends1.n):
            try:
                num = jcast('int', Code07_Friends1.arr[i])
                cur = jcast('int', 1)
                b = jcast('int', Code07_Friends1.BIT)
                path = 0
                best = 0
                xpath = 0
                while (b >= 0):
                    try:
                        path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
                        best = jcast('int', jcast('int', (path ^ 1)))
                        xpath = jcast('int', jcast('int', (jcast('int', (x >> (b & 31))) & 1)))
                        if (xpath == 0):
                            ans = jcast('long', jcast('long', jadd(ans, Code07_Friends1.pass_[Code07_Friends1.tree[cur][best]])))
                            cur = jcast('int', Code07_Friends1.tree[cur][path])
                        else:
                            cur = jcast('int', Code07_Friends1.tree[cur][best])
                        if (cur == 0):
                            raise JBreak(None)
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
                    b = jcast('int', (b - 1))
                ans = jcast('long', jcast('long', jadd(ans, Code07_Friends1.pass_[cur])))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if (x == 0):
            ans = jcast('long', jcast('long', (ans - Code07_Friends1.n)))
        return jcast('long', jcast('long', jdiv(ans, 2)))

    @staticmethod
    def maxKth():
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (1 << (Code07_Friends1.BIT & 31))))
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code07_Friends1.moreEqual(m) >= Code07_Friends1.k):
                ans = jcast('int', m)
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('int', ans)

    @staticmethod
    def compute():
        kth = jcast('int', Code07_Friends1.maxKth())
        ans = jcast('long', 0)
        i = jcast('int', 1)
        cur = 0
        while (i <= Code07_Friends1.n):
            try:
                cur = jcast('int', 1)
                b = jcast('int', Code07_Friends1.BIT)
                path = 0
                best = 0
                kpath = 0
                while (b >= 0):
                    try:
                        path = jcast('int', jcast('int', (jcast('int', (Code07_Friends1.arr[i] >> (b & 31))) & 1)))
                        best = jcast('int', jcast('int', (path ^ 1)))
                        kpath = jcast('int', jcast('int', (jcast('int', (kth >> (b & 31))) & 1)))
                        if (kpath == 0):
                            j = jcast('int', 0)
                            while (j <= Code07_Friends1.BIT):
                                if (jcast('int', (jcast('int', (Code07_Friends1.arr[i] >> (j & 31))) & 1)) == 1):
                                    ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', (jcast('long', (jcast('long', Code07_Friends1.pass_[Code07_Friends1.tree[cur][best]]) - Code07_Friends1.sum[Code07_Friends1.tree[cur][best]][j])) * jcast('long', (1 << (j & 63))))))), Code07_Friends1.MOD)))
                                else:
                                    ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', (jcast('long', Code07_Friends1.sum[Code07_Friends1.tree[cur][best]][j]) * jcast('long', (1 << (j & 63))))))), Code07_Friends1.MOD)))
                                j = jcast('int', (j + 1))
                            cur = jcast('int', Code07_Friends1.tree[cur][path])
                        else:
                            cur = jcast('int', Code07_Friends1.tree[cur][best])
                        if (cur == 0):
                            raise JBreak(None)
                    except JContinue as _java_control_7:
                        if _java_control_7.label not in (None,):
                            raise
                    except JBreak as _java_control_7:
                        if _java_control_7.label not in (None,):
                            raise
                        break
                    b = jcast('int', (b - 1))
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', (jcast('long', Code07_Friends1.pass_[cur]) * kth)))), Code07_Friends1.MOD)))
            except JContinue as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
            except JBreak as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code07_Friends1.INV2)), Code07_Friends1.MOD)))
        ans = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(jcast('long', (ans - jcast('long', jmod(jcast('long', (jcast('long', (Code07_Friends1.moreEqual(kth) - Code07_Friends1.k)) * kth)), Code07_Friends1.MOD)))), Code07_Friends1.MOD)), Code07_Friends1.MOD)), Code07_Friends1.MOD)))
        return jcast('long', ans)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_Friends1.n):
            Code07_Friends1.insert(Code07_Friends1.arr[i])
            i = jcast('int', (i + 1))
        Code07_Friends1.dfs(Code07_Friends1.tree[1][0], Code07_Friends1.BIT, 0)
        Code07_Friends1.dfs(Code07_Friends1.tree[1][1], Code07_Friends1.BIT, jcast('int', (1 << (Code07_Friends1.BIT & 31))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code07_Friends1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code07_Friends1.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code07_Friends1.n):
            jcall(in_, 'nextToken')
            Code07_Friends1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        if (Code07_Friends1.k == 0):
            jcall(out, 'println', 0)
        else:
            Code07_Friends1.prepare()
            jcall(out, 'println', Code07_Friends1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Friends1.MAXN = jcast('int', 50001)
Code07_Friends1.MAXT = jcast('int', jcast('int', (Code07_Friends1.MAXN * 20)))
Code07_Friends1.BIT = jcast('int', 30)
Code07_Friends1.MOD = jcast('int', 1000000007)
Code07_Friends1.INV2 = jcast('int', 500000004)
Code07_Friends1.n = jcast('int', 0)
Code07_Friends1.k = jcast('int', 0)
Code07_Friends1.arr = jarray('int', [Code07_Friends1.MAXN])
Code07_Friends1.tree = jarray('int', [Code07_Friends1.MAXT, 2])
Code07_Friends1.pass_ = jarray('int', [Code07_Friends1.MAXT])
Code07_Friends1.cnt = jcast('int', 1)
Code07_Friends1.sum = jarray('int', [Code07_Friends1.MAXT, jcast('int', jadd(Code07_Friends1.BIT, 1))])

if __name__ == '__main__':
    Code07_Friends1.main([])
