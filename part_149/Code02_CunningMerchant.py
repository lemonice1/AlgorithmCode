# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 狡猾的商人，带权并查集模版题2
# 有n个月的收入，下标1 ~ n，但是并不知道每个月收入是多少
# 操作 l r v，代表从第l个月到第r个月，总收入为v
# 一共给你m个操作，请判断给定的数据是自洽还是自相矛盾
# 自洽打印true，自相矛盾打印false
# 1 <= n <= 100    1 <= m <= 1000
# 总收入不会超过int类型范围
# 测试链接 : https://www.luogu.com.cn/problem/P2294
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_CunningMerchant:
    __java_fields__ = {'MAXN': 'MAXN', 't': 't', 'n': 'n', 'm': 'm', 'ans': 'ans', 'father': 'father', 'dist': 'dist'}
    MAXN = 0
    t = 0
    n = 0
    m = 0
    ans = False
    father = None
    dist = None
    @staticmethod
    def prepare():
        Code02_CunningMerchant.ans = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code02_CunningMerchant.n):
            Code02_CunningMerchant.father[i] = jcast('int', i)
            Code02_CunningMerchant.dist[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code02_CunningMerchant.father[i]):
            tmp = jcast('int', Code02_CunningMerchant.father[i])
            jset(Code02_CunningMerchant.father, i, Code02_CunningMerchant.find(tmp))
            Code02_CunningMerchant.dist[i] = jcast('int', jcast('int', jadd(Code02_CunningMerchant.dist[i], Code02_CunningMerchant.dist[tmp])))
        return jcast('int', Code02_CunningMerchant.father[i])

    @staticmethod
    def union(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        lf = jcast('int', Code02_CunningMerchant.find(l))
        rf = jcast('int', Code02_CunningMerchant.find(r))
        if (lf != rf):
            Code02_CunningMerchant.father[lf] = jcast('int', rf)
            Code02_CunningMerchant.dist[lf] = jcast('int', jcast('int', (jcast('int', jadd(v, Code02_CunningMerchant.dist[r])) - Code02_CunningMerchant.dist[l])))

    @staticmethod
    def check(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        if (Code02_CunningMerchant.find(l) == Code02_CunningMerchant.find(r)):
            if (jcast('int', (Code02_CunningMerchant.dist[l] - Code02_CunningMerchant.dist[r])) != v):
                return jcast('boolean', False)
        return jcast('boolean', True)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_CunningMerchant.t = jcast('int', jcast('int', jget(in_, 'nval')))
        c = jcast('int', 1)
        while (c <= Code02_CunningMerchant.t):
            jcall(in_, 'nextToken')
            Code02_CunningMerchant.n = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
            jcall(in_, 'nextToken')
            Code02_CunningMerchant.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_CunningMerchant.prepare()
            i = jcast('int', 1)
            l = 0
            r = 0
            v = 0
            while (i <= Code02_CunningMerchant.m):
                jcall(in_, 'nextToken')
                l = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                r = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                if (not Code02_CunningMerchant.check(l, r, v)):
                    Code02_CunningMerchant.ans = jcast('boolean', False)
                else:
                    Code02_CunningMerchant.union(l, r, v)
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code02_CunningMerchant.ans)
            c = jcast('int', (c + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CunningMerchant.MAXN = jcast('int', 102)
Code02_CunningMerchant.t = jcast('int', 0)
Code02_CunningMerchant.n = jcast('int', 0)
Code02_CunningMerchant.m = jcast('int', 0)
Code02_CunningMerchant.ans = jcast('boolean', False)
Code02_CunningMerchant.father = jarray('int', [Code02_CunningMerchant.MAXN])
Code02_CunningMerchant.dist = jarray('int', [Code02_CunningMerchant.MAXN])

if __name__ == '__main__':
    Code02_CunningMerchant.main([])
