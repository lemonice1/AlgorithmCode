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

# 翻转道路数量最少的首都
# 给定一棵n个点的树，但是给定的每条边都是有向的
# 需要选择某个城市为首都，要求首都一定可以去往任何一个城市
# 这样一来，可能需要翻转一些边的方向才能做到，现在想翻转道路的数量尽量少
# 打印最少翻转几条道路就可以拥有首都
# 如果有若干点做首都时，翻转道路的数量都是最少的，那么打印这些点
# 测试链接 : https://www.luogu.com.cn/problem/CF219D
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_ChooseCapital:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'reverse': 'reverse', 'dp': 'dp'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # reverse[u] : u到所有子节点需要逆转的边数
    reverse = None
    # dp[u] : u做根到全树节点需要逆转的边数
    dp = None
    @staticmethod
    def build():
        Code03_ChooseCapital.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code03_ChooseCapital.head, 1, jcast('int', jadd(Code03_ChooseCapital.n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_ChooseCapital.reverse, 1, jcast('int', jadd(Code03_ChooseCapital.n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_ChooseCapital.dp, 1, jcast('int', jadd(Code03_ChooseCapital.n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code03_ChooseCapital.next[Code03_ChooseCapital.cnt] = jcast('int', Code03_ChooseCapital.head[u])
        Code03_ChooseCapital.to[Code03_ChooseCapital.cnt] = jcast('int', v)
        Code03_ChooseCapital.weight[Code03_ChooseCapital.cnt] = jcast('int', w)
        jset(Code03_ChooseCapital.head, u, ((_java_obj_1 := Code03_ChooseCapital), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code03_ChooseCapital.head[u])
        v = 0
        w = 0
        while (e != 0):
            v = jcast('int', Code03_ChooseCapital.to[e])
            w = jcast('int', Code03_ChooseCapital.weight[e])
            if (v != f):
                Code03_ChooseCapital.dfs1(v, u)
                Code03_ChooseCapital.reverse[u] = jcast('int', jcast('int', jadd(Code03_ChooseCapital.reverse[u], jcast('int', jadd(Code03_ChooseCapital.reverse[v], w)))))
            e = jcast('int', Code03_ChooseCapital.next[e])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code03_ChooseCapital.head[u])
        v = 0
        w = 0
        while (e != 0):
            v = jcast('int', Code03_ChooseCapital.to[e])
            w = jcast('int', Code03_ChooseCapital.weight[e])
            if (v != f):
                if (w == 0):
                    # 边的方向 : u -> v
                    Code03_ChooseCapital.dp[v] = jcast('int', jcast('int', jadd(Code03_ChooseCapital.dp[u], 1)))
                else:
                    # 边的方向 : v -> u
                    Code03_ChooseCapital.dp[v] = jcast('int', jcast('int', (Code03_ChooseCapital.dp[u] - 1)))
                Code03_ChooseCapital.dfs2(v, u)
            e = jcast('int', Code03_ChooseCapital.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_ChooseCapital.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_ChooseCapital.build()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i < Code03_ChooseCapital.n):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                Code03_ChooseCapital.addEdge(u, v, 0)
                Code03_ChooseCapital.addEdge(v, u, 1)
                i = jcast('int', (i + 1))
            Code03_ChooseCapital.dfs1(1, 0)
            Code03_ChooseCapital.dp[1] = jcast('int', Code03_ChooseCapital.reverse[1])
            Code03_ChooseCapital.dfs2(1, 0)
            min = jcast('int', jget(Integer, 'MAX_VALUE'))
            i = jcast('int', 1)
            while (i <= Code03_ChooseCapital.n):
                if (min > Code03_ChooseCapital.dp[i]):
                    min = jcast('int', Code03_ChooseCapital.dp[i])
                i = jcast('int', (i + 1))
            jcall(out, 'println', min)
            i = jcast('int', 1)
            while (i <= Code03_ChooseCapital.n):
                if (min == Code03_ChooseCapital.dp[i]):
                    jcall(out, 'print', jadd(i, ' '))
                i = jcast('int', (i + 1))
            jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_ChooseCapital.MAXN = jcast('int', 200001)
Code03_ChooseCapital.n = jcast('int', 0)
Code03_ChooseCapital.head = jarray('int', [Code03_ChooseCapital.MAXN])
Code03_ChooseCapital.next = jarray('int', [jcast('int', (Code03_ChooseCapital.MAXN << (1 & 31)))])
Code03_ChooseCapital.to = jarray('int', [jcast('int', (Code03_ChooseCapital.MAXN << (1 & 31)))])
Code03_ChooseCapital.weight = jarray('int', [jcast('int', (Code03_ChooseCapital.MAXN << (1 & 31)))])
Code03_ChooseCapital.cnt = jcast('int', 0)
Code03_ChooseCapital.reverse = jarray('int', [Code03_ChooseCapital.MAXN])
Code03_ChooseCapital.dp = jarray('int', [Code03_ChooseCapital.MAXN])

if __name__ == '__main__':
    Code03_ChooseCapital.main([])
