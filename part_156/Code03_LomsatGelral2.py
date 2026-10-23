# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 主导颜色累加和，Python版
# 一共有n个节点，编号1~n，给定n-1条边，所有节点连成一棵树，1号节点为树头
# 每个节点给定一种颜色值，主导颜色累加和定义如下
# 以x为头的子树上，哪种颜色出现最多，那种颜色就是主导颜色，主导颜色可能不止一种
# 所有主导颜色的值累加起来，每个主导颜色只累加一次，就是该子树的主导颜色累加和
# 打印1~n每个节点为头的子树的主导颜色累加和
# 1 <= n、颜色值 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF600E
# 测试链接 : https://codeforces.com/problemset/problem/600/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_LomsatGelral2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'color': 'color', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'fa': 'fa', 'siz': 'siz', 'son': 'son', 'colorCnt': 'colorCnt', 'maxCnt': 'maxCnt', 'ans': 'ans'}
    MAXN = 0
    n = 0
    color = None
    head = None
    next = None
    to = None
    cnt = 0
    fa = None
    siz = None
    son = None
    colorCnt = None
    maxCnt = None
    ans = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_LomsatGelral2.next, ((_java_obj_1 := Code03_LomsatGelral2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_LomsatGelral2.head[u])
        Code03_LomsatGelral2.to[Code03_LomsatGelral2.cnt] = jcast('int', v)
        Code03_LomsatGelral2.head[u] = jcast('int', Code03_LomsatGelral2.cnt)

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_LomsatGelral2.fa[u] = jcast('int', f)
        Code03_LomsatGelral2.siz[u] = jcast('int', 1)
        e = jcast('int', Code03_LomsatGelral2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_LomsatGelral2.to[e])
            if (v != f):
                Code03_LomsatGelral2.dfs1(v, u)
            e = jcast('int', Code03_LomsatGelral2.next[e])
        e = jcast('int', Code03_LomsatGelral2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_LomsatGelral2.to[e])
            if (v != f):
                Code03_LomsatGelral2.siz[u] = jcast('int', jcast('int', jadd(Code03_LomsatGelral2.siz[u], Code03_LomsatGelral2.siz[v])))
                if ((Code03_LomsatGelral2.son[u] == 0) or (Code03_LomsatGelral2.siz[Code03_LomsatGelral2.son[u]] < Code03_LomsatGelral2.siz[v])):
                    Code03_LomsatGelral2.son[u] = jcast('int', v)
            e = jcast('int', Code03_LomsatGelral2.next[e])

    @staticmethod
    def effect(u, h):
        u = jcast('int', u)
        h = jcast('int', h)
        ((_java_obj_4 := Code03_LomsatGelral2.colorCnt), (_java_key_5 := Code03_LomsatGelral2.color[u]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
        if (Code03_LomsatGelral2.colorCnt[Code03_LomsatGelral2.color[u]] == Code03_LomsatGelral2.maxCnt[h]):
            Code03_LomsatGelral2.ans[h] = jcast('long', jcast('long', jadd(Code03_LomsatGelral2.ans[h], Code03_LomsatGelral2.color[u])))
        else:
            if (Code03_LomsatGelral2.colorCnt[Code03_LomsatGelral2.color[u]] > Code03_LomsatGelral2.maxCnt[h]):
                Code03_LomsatGelral2.maxCnt[h] = jcast('int', Code03_LomsatGelral2.colorCnt[Code03_LomsatGelral2.color[u]])
                Code03_LomsatGelral2.ans[h] = jcast('long', Code03_LomsatGelral2.color[u])
        e = jcast('int', Code03_LomsatGelral2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_LomsatGelral2.to[e])
            if (v != Code03_LomsatGelral2.fa[u]):
                Code03_LomsatGelral2.effect(v, h)
            e = jcast('int', Code03_LomsatGelral2.next[e])

    @staticmethod
    def cancel(u):
        u = jcast('int', u)
        jset(Code03_LomsatGelral2.colorCnt, Code03_LomsatGelral2.color[u], 0)
        Code03_LomsatGelral2.maxCnt[u] = jcast('int', 0)
        e = jcast('int', Code03_LomsatGelral2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_LomsatGelral2.to[e])
            if (v != Code03_LomsatGelral2.fa[u]):
                Code03_LomsatGelral2.cancel(v)
            e = jcast('int', Code03_LomsatGelral2.next[e])

    @staticmethod
    def dfs2(u, keep):
        u = jcast('int', u)
        keep = jcast('int', keep)
        e = jcast('int', Code03_LomsatGelral2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_LomsatGelral2.to[e])
            if ((v != Code03_LomsatGelral2.fa[u]) and (v != Code03_LomsatGelral2.son[u])):
                Code03_LomsatGelral2.dfs2(v, 0)
            e = jcast('int', Code03_LomsatGelral2.next[e])
        if (Code03_LomsatGelral2.son[u] != 0):
            Code03_LomsatGelral2.dfs2(Code03_LomsatGelral2.son[u], 1)
        Code03_LomsatGelral2.maxCnt[u] = jcast('int', Code03_LomsatGelral2.maxCnt[Code03_LomsatGelral2.son[u]])
        Code03_LomsatGelral2.ans[u] = jcast('long', Code03_LomsatGelral2.ans[Code03_LomsatGelral2.son[u]])
        ((_java_obj_7 := Code03_LomsatGelral2.colorCnt), (_java_key_8 := Code03_LomsatGelral2.color[u]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]
        if (Code03_LomsatGelral2.colorCnt[Code03_LomsatGelral2.color[u]] == Code03_LomsatGelral2.maxCnt[u]):
            Code03_LomsatGelral2.ans[u] = jcast('long', jcast('long', jadd(Code03_LomsatGelral2.ans[u], Code03_LomsatGelral2.color[u])))
        else:
            if (Code03_LomsatGelral2.colorCnt[Code03_LomsatGelral2.color[u]] > Code03_LomsatGelral2.maxCnt[u]):
                Code03_LomsatGelral2.maxCnt[u] = jcast('int', Code03_LomsatGelral2.colorCnt[Code03_LomsatGelral2.color[u]])
                Code03_LomsatGelral2.ans[u] = jcast('long', Code03_LomsatGelral2.color[u])
        e = jcast('int', Code03_LomsatGelral2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_LomsatGelral2.to[e])
            if ((v != Code03_LomsatGelral2.fa[u]) and (v != Code03_LomsatGelral2.son[u])):
                Code03_LomsatGelral2.effect(v, u)
            e = jcast('int', Code03_LomsatGelral2.next[e])
        if (keep == 0):
            Code03_LomsatGelral2.cancel(u)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_LomsatGelral2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_LomsatGelral2.n):
            jcall(in_, 'nextToken')
            Code03_LomsatGelral2.color[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code03_LomsatGelral2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_LomsatGelral2.addEdge(u, v)
            Code03_LomsatGelral2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code03_LomsatGelral2.dfs1(1, 0)
        Code03_LomsatGelral2.dfs2(1, 0)
        i = jcast('int', 1)
        while (i <= Code03_LomsatGelral2.n):
            jcall(out, 'print', jadd(Code03_LomsatGelral2.ans[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_LomsatGelral2.MAXN = jcast('int', 100001)
Code03_LomsatGelral2.n = jcast('int', 0)
Code03_LomsatGelral2.color = jarray('int', [Code03_LomsatGelral2.MAXN])
Code03_LomsatGelral2.head = jarray('int', [Code03_LomsatGelral2.MAXN])
Code03_LomsatGelral2.next = jarray('int', [jcast('int', (Code03_LomsatGelral2.MAXN << (1 & 31)))])
Code03_LomsatGelral2.to = jarray('int', [jcast('int', (Code03_LomsatGelral2.MAXN << (1 & 31)))])
Code03_LomsatGelral2.cnt = jcast('int', 0)
Code03_LomsatGelral2.fa = jarray('int', [Code03_LomsatGelral2.MAXN])
Code03_LomsatGelral2.siz = jarray('int', [Code03_LomsatGelral2.MAXN])
Code03_LomsatGelral2.son = jarray('int', [Code03_LomsatGelral2.MAXN])
Code03_LomsatGelral2.colorCnt = jarray('int', [Code03_LomsatGelral2.MAXN])
Code03_LomsatGelral2.maxCnt = jarray('int', [Code03_LomsatGelral2.MAXN])
Code03_LomsatGelral2.ans = jarray('long', [Code03_LomsatGelral2.MAXN])

if __name__ == '__main__':
    Code03_LomsatGelral2.main([])
