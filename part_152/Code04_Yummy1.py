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

# 美味，Python版
# 给定一个长度为n的数组arr，一共有m条查询，查询格式如下
# b x l r : 从arr[l..r]中选一个数字，希望b ^ (该数字 + x)的值最大，打印这个值
# 1 <= n <= 2 * 10^5
# 1 <= m <= 10^5
# 0 <= arr[i]、b、x < 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3293
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Yummy1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'BIT': 'BIT', 'n': 'n', 'm': 'm', 's': 's', 'arr': 'arr', 'root': 'root', 'left': 'left', 'right': 'right', 'size': 'size', 'cnt': 'cnt'}
    MAXN = 0
    MAXT = 0
    BIT = 0
    n = 0
    m = 0
    s = 0
    arr = None
    # 可持久化线段树需要
    root = None
    left = None
    right = None
    size = None
    cnt = 0
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code04_Yummy1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        Code04_Yummy1.size[rt] = jcast('int', 0)
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code04_Yummy1.left, rt, Code04_Yummy1.build(l, mid))
            jset(Code04_Yummy1.right, rt, Code04_Yummy1.build(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    @staticmethod
    def insert(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code04_Yummy1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code04_Yummy1.left[rt] = jcast('int', Code04_Yummy1.left[i])
        Code04_Yummy1.right[rt] = jcast('int', Code04_Yummy1.right[i])
        Code04_Yummy1.size[rt] = jcast('int', jcast('int', jadd(Code04_Yummy1.size[i], 1)))
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code04_Yummy1.left, rt, Code04_Yummy1.insert(jobi, l, mid, Code04_Yummy1.left[rt]))
            else:
                jset(Code04_Yummy1.right, rt, Code04_Yummy1.insert(jobi, jcast('int', jadd(mid, 1)), r, Code04_Yummy1.right[rt]))
        return jcast('int', rt)

    @staticmethod
    def query(jobl, jobr, l, r, u, v):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        u = jcast('int', u)
        v = jcast('int', v)
        if ((jobr < l) or (jobl > r)):
            return jcast('int', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', jcast('int', (Code04_Yummy1.size[v] - Code04_Yummy1.size[u])))
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code04_Yummy1.query(jobl, jobr, l, mid, Code04_Yummy1.left[u], Code04_Yummy1.left[v]))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code04_Yummy1.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code04_Yummy1.right[u], Code04_Yummy1.right[v]))))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        Code04_Yummy1.cnt = jcast('int', 0)
        Code04_Yummy1.s = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Yummy1.n):
            Code04_Yummy1.s = jcast('int', jstatic('Math', 'max', Code04_Yummy1.s, Code04_Yummy1.arr[i]))
            i = jcast('int', (i + 1))
        jset(Code04_Yummy1.root, 0, Code04_Yummy1.build(0, Code04_Yummy1.s))
        i = jcast('int', 1)
        while (i <= Code04_Yummy1.n):
            jset(Code04_Yummy1.root, i, Code04_Yummy1.insert(Code04_Yummy1.arr[i], 0, Code04_Yummy1.s, Code04_Yummy1.root[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))

    @staticmethod
    def compute(b, x, l, r):
        b = jcast('int', b)
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        best = jcast('int', 0)
        i = jcast('int', Code04_Yummy1.BIT)
        while (i >= 0):
            if (jcast('int', (jcast('int', (b >> (i & 31))) & 1)) == 1):
                if (Code04_Yummy1.query(jcast('int', (best - x)), jcast('int', (jcast('int', (jcast('int', jadd(best, jcast('int', (1 << (i & 31))))) - 1)) - x)), 0, Code04_Yummy1.s, Code04_Yummy1.root[jcast('int', (l - 1))], Code04_Yummy1.root[r]) == 0):
                    best = jcast('int', jcast('int', jadd(best, jcast('int', (1 << (i & 31))))))
            else:
                if (Code04_Yummy1.query(jcast('int', (jcast('int', jadd(best, jcast('int', (1 << (i & 31))))) - x)), jcast('int', (jcast('int', (jcast('int', jadd(best, jcast('int', (1 << (jcast('int', jadd(i, 1)) & 31))))) - 1)) - x)), 0, Code04_Yummy1.s, Code04_Yummy1.root[jcast('int', (l - 1))], Code04_Yummy1.root[r]) != 0):
                    best = jcast('int', jcast('int', jadd(best, jcast('int', (1 << (i & 31))))))
            i = jcast('int', (i - 1))
        return jcast('int', jcast('int', (best ^ b)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_Yummy1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_Yummy1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code04_Yummy1.n):
            jcall(in_, 'nextToken')
            Code04_Yummy1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code04_Yummy1.prepare()
        i = jcast('int', 1)
        b = 0
        x = 0
        l = 0
        r = 0
        while (i <= Code04_Yummy1.m):
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            l = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code04_Yummy1.compute(b, x, l, r))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Yummy1.MAXN = jcast('int', 200001)
Code04_Yummy1.MAXT = jcast('int', 4000001)
Code04_Yummy1.BIT = jcast('int', 18)
Code04_Yummy1.n = jcast('int', 0)
Code04_Yummy1.m = jcast('int', 0)
Code04_Yummy1.s = jcast('int', 0)
Code04_Yummy1.arr = jarray('int', [Code04_Yummy1.MAXN])
Code04_Yummy1.root = jarray('int', [Code04_Yummy1.MAXN])
Code04_Yummy1.left = jarray('int', [Code04_Yummy1.MAXT])
Code04_Yummy1.right = jarray('int', [Code04_Yummy1.MAXT])
Code04_Yummy1.size = jarray('int', [Code04_Yummy1.MAXT])
Code04_Yummy1.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code04_Yummy1.main([])
