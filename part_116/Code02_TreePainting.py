# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 染色的最大收益
# 给定一棵n个点的树，初始时所有节点全是白点
# 第一次操作，你可以选择任意点染黑
# 以后每次操作，必须选择已经染黑的点的相邻点继续染黑，一直到所有的点都被染完
# 每次都获得，当前被染色点的白色连通块大小，作为收益
# 返回可获得的最大收益和
# 测试链接 : https://www.luogu.com.cn/problem/CF1187E
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_TreePainting:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'size': 'size', 'dp': 'dp'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    cnt = 0
    size = None
    dp = None
    @staticmethod
    def build():
        Code02_TreePainting.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code02_TreePainting.head, 1, jcast('int', jadd(Code02_TreePainting.n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_TreePainting.size, 1, jcast('int', jadd(Code02_TreePainting.n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_TreePainting.dp, 1, jcast('int', jadd(Code02_TreePainting.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code02_TreePainting.next[Code02_TreePainting.cnt] = jcast('int', Code02_TreePainting.head[u])
        Code02_TreePainting.to[Code02_TreePainting.cnt] = jcast('int', v)
        jset(Code02_TreePainting.head, u, ((_java_obj_1 := Code02_TreePainting), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # dp[i]更新成
    # 节点i作为自己这棵子树最先染的点，染完子树后，收益是多少
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code02_TreePainting.size[u] = jcast('int', 1)
        e = jcast('int', Code02_TreePainting.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code02_TreePainting.to[e])
            if (v != f):
                Code02_TreePainting.dfs1(v, u)
                Code02_TreePainting.size[u] = jcast('int', jcast('int', jadd(Code02_TreePainting.size[u], Code02_TreePainting.size[v])))
                Code02_TreePainting.dp[u] = jcast('long', jcast('long', jadd(Code02_TreePainting.dp[u], Code02_TreePainting.dp[v])))
            e = jcast('int', Code02_TreePainting.next[e])
        Code02_TreePainting.dp[u] = jcast('long', jcast('long', jadd(Code02_TreePainting.dp[u], Code02_TreePainting.size[u])))

    # dp[i]更新成
    # 节点i作为整棵树最先染的点，染完整棵树后，收益是多少
    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code02_TreePainting.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code02_TreePainting.to[e])
            if (v != f):
                Code02_TreePainting.dp[v] = jcast('long', jcast('long', (jcast('long', (jcast('long', jadd(Code02_TreePainting.dp[u], Code02_TreePainting.n)) - Code02_TreePainting.size[v])) - Code02_TreePainting.size[v])))
                Code02_TreePainting.dfs2(v, u)
            e = jcast('int', Code02_TreePainting.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_TreePainting.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_TreePainting.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code02_TreePainting.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_TreePainting.addEdge(u, v)
            Code02_TreePainting.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code02_TreePainting.dfs1(1, 0)
        Code02_TreePainting.dfs2(1, 0)
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code02_TreePainting.n):
            ans = jcast('long', jstatic('Math', 'max', ans, Code02_TreePainting.dp[i]))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_TreePainting.MAXN = jcast('int', 200001)
Code02_TreePainting.n = jcast('int', 0)
Code02_TreePainting.head = jarray('int', [Code02_TreePainting.MAXN])
Code02_TreePainting.next = jarray('int', [jcast('int', (Code02_TreePainting.MAXN << (1 & 31)))])
Code02_TreePainting.to = jarray('int', [jcast('int', (Code02_TreePainting.MAXN << (1 & 31)))])
Code02_TreePainting.cnt = jcast('int', 0)
Code02_TreePainting.size = jarray('int', [Code02_TreePainting.MAXN])
Code02_TreePainting.dp = jarray('long', [Code02_TreePainting.MAXN])

if __name__ == '__main__':
    Code02_TreePainting.main([])
