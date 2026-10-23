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

# 树上启发式合并模版题，Python版
# 一共有n个节点，编号1~n，给定n-1条边，所有节点连成一棵树，1号节点为树头
# 每个节点给定一种颜色值，一共有m条查询，每条查询给定参数x
# 每条查询打印x为头的子树上，一共有多少种不同的颜色
# 1 <= n、m、颜色值 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/U41492
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DsuOnTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'fa': 'fa', 'siz': 'siz', 'son': 'son', 'colorCnt': 'colorCnt', 'ans': 'ans', 'diffColors': 'diffColors'}
    MAXN = 0
    n = 0
    m = 0
    # 每个节点的颜色
    arr = None
    # 链式前向星
    head = None
    next = None
    to = None
    cnt = 0
    # 树链剖分
    fa = None
    siz = None
    son = None
    # 树上启发式合并
    # colorCnt[i] = j，表示i这种颜色出现了j次
    colorCnt = None
    ans = None
    diffColors = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_DsuOnTree1.next, ((_java_obj_1 := Code01_DsuOnTree1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_DsuOnTree1.head[u])
        Code01_DsuOnTree1.to[Code01_DsuOnTree1.cnt] = jcast('int', v)
        Code01_DsuOnTree1.head[u] = jcast('int', Code01_DsuOnTree1.cnt)

    # 重链剖分
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code01_DsuOnTree1.fa[u] = jcast('int', f)
        Code01_DsuOnTree1.siz[u] = jcast('int', 1)
        e = jcast('int', Code01_DsuOnTree1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_DsuOnTree1.to[e])
            if (v != f):
                Code01_DsuOnTree1.dfs1(v, u)
            e = jcast('int', Code01_DsuOnTree1.next[e])
        e = jcast('int', Code01_DsuOnTree1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_DsuOnTree1.to[e])
            if (v != f):
                Code01_DsuOnTree1.siz[u] = jcast('int', jcast('int', jadd(Code01_DsuOnTree1.siz[u], Code01_DsuOnTree1.siz[v])))
                if ((Code01_DsuOnTree1.son[u] == 0) or (Code01_DsuOnTree1.siz[Code01_DsuOnTree1.son[u]] < Code01_DsuOnTree1.siz[v])):
                    Code01_DsuOnTree1.son[u] = jcast('int', v)
            e = jcast('int', Code01_DsuOnTree1.next[e])

    # 子树u每个节点贡献信息
    @staticmethod
    def effect(u):
        u = jcast('int', u)
        if (((_java_obj_4 := Code01_DsuOnTree1.colorCnt), (_java_key_5 := Code01_DsuOnTree1.arr[u]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3] == 1):
            Code01_DsuOnTree1.diffColors = jcast('int', (Code01_DsuOnTree1.diffColors + 1))
        e = jcast('int', Code01_DsuOnTree1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_DsuOnTree1.to[e])
            if (v != Code01_DsuOnTree1.fa[u]):
                Code01_DsuOnTree1.effect(v)
            e = jcast('int', Code01_DsuOnTree1.next[e])

    # 子树u每个节点取消贡献
    @staticmethod
    def cancel(u):
        u = jcast('int', u)
        if (((_java_obj_7 := Code01_DsuOnTree1.colorCnt), (_java_key_8 := Code01_DsuOnTree1.arr[u]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3] == 0):
            Code01_DsuOnTree1.diffColors = jcast('int', (Code01_DsuOnTree1.diffColors - 1))
        e = jcast('int', Code01_DsuOnTree1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_DsuOnTree1.to[e])
            if (v != Code01_DsuOnTree1.fa[u]):
                Code01_DsuOnTree1.cancel(v)
            e = jcast('int', Code01_DsuOnTree1.next[e])

    # 树上启发式合并的过程
    @staticmethod
    def dfs2(u, keep):
        u = jcast('int', u)
        keep = jcast('int', keep)
        # 遍历轻儿子的子树，统计子树的答案，然后取消贡献
        e = jcast('int', Code01_DsuOnTree1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_DsuOnTree1.to[e])
            if ((v != Code01_DsuOnTree1.fa[u]) and (v != Code01_DsuOnTree1.son[u])):
                Code01_DsuOnTree1.dfs2(v, 0)
            e = jcast('int', Code01_DsuOnTree1.next[e])
        # 遍历重儿子的子树，统计子树的答案，然后保留贡献
        if (Code01_DsuOnTree1.son[u] != 0):
            Code01_DsuOnTree1.dfs2(Code01_DsuOnTree1.son[u], 1)
        # 当前节点贡献信息
        if (((_java_obj_10 := Code01_DsuOnTree1.colorCnt), (_java_key_11 := Code01_DsuOnTree1.arr[u]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3] == 1):
            Code01_DsuOnTree1.diffColors = jcast('int', (Code01_DsuOnTree1.diffColors + 1))
        # 遍历轻儿子的子树，重新贡献一遍
        e = jcast('int', Code01_DsuOnTree1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_DsuOnTree1.to[e])
            if ((v != Code01_DsuOnTree1.fa[u]) and (v != Code01_DsuOnTree1.son[u])):
                Code01_DsuOnTree1.effect(v)
            e = jcast('int', Code01_DsuOnTree1.next[e])
        # 记录子树u的答案
        Code01_DsuOnTree1.ans[u] = jcast('int', Code01_DsuOnTree1.diffColors)
        # 如果u是上级节点的轻儿子，子树u的贡献取消，否则保留
        if (keep == 0):
            Code01_DsuOnTree1.cancel(u)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_DsuOnTree1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_DsuOnTree1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_DsuOnTree1.addEdge(u, v)
            Code01_DsuOnTree1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_DsuOnTree1.n):
            jcall(in_, 'nextToken')
            Code01_DsuOnTree1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_DsuOnTree1.dfs1(1, 0)
        Code01_DsuOnTree1.dfs2(1, 0)
        jcall(in_, 'nextToken')
        Code01_DsuOnTree1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        cur = 0
        while (i <= Code01_DsuOnTree1.m):
            jcall(in_, 'nextToken')
            cur = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code01_DsuOnTree1.ans[cur])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DsuOnTree1.MAXN = jcast('int', 100001)
Code01_DsuOnTree1.n = jcast('int', 0)
Code01_DsuOnTree1.m = jcast('int', 0)
Code01_DsuOnTree1.arr = jarray('int', [Code01_DsuOnTree1.MAXN])
Code01_DsuOnTree1.head = jarray('int', [Code01_DsuOnTree1.MAXN])
Code01_DsuOnTree1.next = jarray('int', [jcast('int', (Code01_DsuOnTree1.MAXN << (1 & 31)))])
Code01_DsuOnTree1.to = jarray('int', [jcast('int', (Code01_DsuOnTree1.MAXN << (1 & 31)))])
Code01_DsuOnTree1.cnt = jcast('int', 0)
Code01_DsuOnTree1.fa = jarray('int', [Code01_DsuOnTree1.MAXN])
Code01_DsuOnTree1.siz = jarray('int', [Code01_DsuOnTree1.MAXN])
Code01_DsuOnTree1.son = jarray('int', [Code01_DsuOnTree1.MAXN])
Code01_DsuOnTree1.colorCnt = jarray('int', [Code01_DsuOnTree1.MAXN])
Code01_DsuOnTree1.ans = jarray('int', [Code01_DsuOnTree1.MAXN])
Code01_DsuOnTree1.diffColors = jcast('int', 0)

if __name__ == '__main__':
    Code01_DsuOnTree1.main([])
