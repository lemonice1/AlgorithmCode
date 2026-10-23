# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 推导部分和，带权并查集模版题1
# 有n个数字，下标1 ~ n，但是并不知道每个数字是多少
# 先给出m个数字段的累加和，再查询q个数字段的累加和
# 给出数字段累加和的操作 l r v，代表l~r范围上的数字，累加和为v
# 查询数字段累加和的操作 l r，代表查询l~r范围上的数字累加和
# 请根据m个给定，完成q个查询，如果某个查询无法给出答案，打印"UNKNOWN"
# 1 <= n, m, q <= 10^5
# 累加和不会超过long类型范围
# 测试链接 : https://www.luogu.com.cn/problem/P8779
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DerivePartialSums:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'q': 'q', 'father': 'father', 'dist': 'dist'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    q = 0
    father = None
    dist = None
    @staticmethod
    def prepare():
        i = jcast('int', 0)
        while (i <= Code01_DerivePartialSums.n):
            Code01_DerivePartialSums.father[i] = jcast('int', i)
            Code01_DerivePartialSums.dist[i] = jcast('long', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code01_DerivePartialSums.father[i]):
            tmp = jcast('int', Code01_DerivePartialSums.father[i])
            jset(Code01_DerivePartialSums.father, i, Code01_DerivePartialSums.find(tmp))
            Code01_DerivePartialSums.dist[i] = jcast('long', jcast('long', jadd(Code01_DerivePartialSums.dist[i], Code01_DerivePartialSums.dist[tmp])))
        return jcast('int', Code01_DerivePartialSums.father[i])

    @staticmethod
    def union(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('long', v)
        lf = jcast('int', Code01_DerivePartialSums.find(l))
        rf = jcast('int', Code01_DerivePartialSums.find(r))
        if (lf != rf):
            Code01_DerivePartialSums.father[lf] = jcast('int', rf)
            Code01_DerivePartialSums.dist[lf] = jcast('long', jcast('long', (jcast('long', jadd(v, Code01_DerivePartialSums.dist[r])) - Code01_DerivePartialSums.dist[l])))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (Code01_DerivePartialSums.find(l) != Code01_DerivePartialSums.find(r)):
            return jcast('long', Code01_DerivePartialSums.INF)
        return jcast('long', jcast('long', (Code01_DerivePartialSums.dist[l] - Code01_DerivePartialSums.dist[r])))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_DerivePartialSums.n = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
        jcall(in_, 'nextToken')
        Code01_DerivePartialSums.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_DerivePartialSums.q = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_DerivePartialSums.prepare()
        l = 0
        r = 0
        v = 0
        i = jcast('int', 1)
        while (i <= Code01_DerivePartialSums.m):
            jcall(in_, 'nextToken')
            l = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
            jcall(in_, 'nextToken')
            v = jcast('long', jcast('long', jget(in_, 'nval')))
            Code01_DerivePartialSums.union(l, r, v)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_DerivePartialSums.q):
            jcall(in_, 'nextToken')
            l = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
            v = jcast('long', Code01_DerivePartialSums.query(l, r))
            if (v == Code01_DerivePartialSums.INF):
                jcall(out, 'println', 'UNKNOWN')
            else:
                jcall(out, 'println', v)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DerivePartialSums.MAXN = jcast('int', 100002)
Code01_DerivePartialSums.INF = jcast('long', jget(Long, 'MAX_VALUE'))
Code01_DerivePartialSums.n = jcast('int', 0)
Code01_DerivePartialSums.m = jcast('int', 0)
Code01_DerivePartialSums.q = jcast('int', 0)
Code01_DerivePartialSums.father = jarray('int', [Code01_DerivePartialSums.MAXN])
Code01_DerivePartialSums.dist = jarray('long', [Code01_DerivePartialSums.MAXN])

if __name__ == '__main__':
    Code01_DerivePartialSums.main([])
