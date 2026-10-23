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

# 路径和子树的异或，Python版
# 一共有n个节点，n-1条边，组成一棵树，1号节点为树头，每个节点给定点权
# 一共有m条查询，每条查询是如下两种类型中的一种
# 1 x y   : 以x为头的子树中任选一个值，希望异或y之后的值最大，打印最大值
# 2 x y z : 节点x到节点y的路径中任选一个值，希望异或z之后的值最大，打印最大值
# 2 <= n、m <= 10^5
# 1 <= 点权、z < 2^30
# 测试链接 : https://www.luogu.com.cn/problem/P4592
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 对应实现可参考 Code03_PathDfnXor2.py
# 两个版本保留相同的算法逻辑
class Code03_PathDfnXor1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXP': 'MAXP', 'BIT': 'BIT', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'deep': 'deep', 'size': 'size', 'stjump': 'stjump', 'dfn': 'dfn', 'cntd': 'cntd', 'root1': 'root1', 'root2': 'root2', 'tree': 'tree', 'pass': 'pass_', 'cntt': 'cntt'}
    MAXN = 0
    MAXT = 0
    MAXP = 0
    BIT = 0
    n = 0
    m = 0
    # 每个节点的点权
    arr = None
    # 链式前向星需要
    head = None
    next = None
    to = None
    # 链式前向星的边的计数
    cntg = 0
    # 树上dfs求节点深度
    deep = None
    # 树上dfs求子树大小
    size = None
    # 树上dfs求st表
    stjump = None
    # 树上dfs求每个节点的dfn序号
    dfn = None
    # dfn序号计数
    cntd = 0
    # 1类型的可持久化01Trie，根据dfn序号的次序建树
    root1 = None
    # 2类型的可持久化01Trie，根据父节点的版本建新树
    root2 = None
    # 1类型和2类型都可以用这个tree结构
    tree = None
    # 1类型和2类型都可以用这个pass数组
    pass_ = None
    # 1类型和2类型一起的节点计数
    cntt = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_PathDfnXor1.next, ((_java_obj_1 := Code03_PathDfnXor1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_PathDfnXor1.head[u])
        Code03_PathDfnXor1.to[Code03_PathDfnXor1.cntg] = jcast('int', v)
        Code03_PathDfnXor1.head[u] = jcast('int', Code03_PathDfnXor1.cntg)

    @staticmethod
    def insert(num, i):
        num = jcast('int', num)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code03_PathDfnXor1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        jset(Code03_PathDfnXor1.tree[rt], 0, Code03_PathDfnXor1.tree[i][0])
        jset(Code03_PathDfnXor1.tree[rt], 1, Code03_PathDfnXor1.tree[i][1])
        Code03_PathDfnXor1.pass_[rt] = jcast('int', jcast('int', jadd(Code03_PathDfnXor1.pass_[i], 1)))
        b = jcast('int', Code03_PathDfnXor1.BIT)
        path = 0
        pre = jcast('int', rt)
        cur = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            i = jcast('int', Code03_PathDfnXor1.tree[i][path])
            cur = jcast('int', ((_java_obj_7 := Code03_PathDfnXor1), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            jset(Code03_PathDfnXor1.tree[cur], 0, Code03_PathDfnXor1.tree[i][0])
            jset(Code03_PathDfnXor1.tree[cur], 1, Code03_PathDfnXor1.tree[i][1])
            Code03_PathDfnXor1.pass_[cur] = jcast('int', jcast('int', jadd(Code03_PathDfnXor1.pass_[i], 1)))
            jset(Code03_PathDfnXor1.tree[pre], path, cur)
            b = jcast('int', (b - 1))
            pre = jcast('int', cur)
        return jcast('int', rt)

    @staticmethod
    def query(num, u, v):
        num = jcast('int', num)
        u = jcast('int', u)
        v = jcast('int', v)
        ans = jcast('int', 0)
        b = jcast('int', Code03_PathDfnXor1.BIT)
        path = 0
        best = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            best = jcast('int', jcast('int', (path ^ 1)))
            if (Code03_PathDfnXor1.pass_[Code03_PathDfnXor1.tree[v][best]] > Code03_PathDfnXor1.pass_[Code03_PathDfnXor1.tree[u][best]]):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', (1 << (b & 31))))))
                u = jcast('int', Code03_PathDfnXor1.tree[u][best])
                v = jcast('int', Code03_PathDfnXor1.tree[v][best])
            else:
                u = jcast('int', Code03_PathDfnXor1.tree[u][path])
                v = jcast('int', Code03_PathDfnXor1.tree[v][path])
            b = jcast('int', (b - 1))
        return jcast('int', ans)

    # 按道理说dfs1应该改成迭代版，防止递归爆栈
    # 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
    # 有兴趣的同学可以看一下，讲解118，详解了树上dfs从递归版改迭代版
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_PathDfnXor1.deep[u] = jcast('int', jcast('int', jadd(Code03_PathDfnXor1.deep[fa], 1)))
        Code03_PathDfnXor1.size[u] = jcast('int', 1)
        jset(Code03_PathDfnXor1.stjump[u], 0, fa)
        jset(Code03_PathDfnXor1.dfn, u, ((_java_obj_10 := Code03_PathDfnXor1), (_java_key_11 := 'cntd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        p = jcast('int', 1)
        while (p < Code03_PathDfnXor1.MAXP):
            jset(Code03_PathDfnXor1.stjump[u], p, Code03_PathDfnXor1.stjump[Code03_PathDfnXor1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        ei = jcast('int', Code03_PathDfnXor1.head[u])
        v = 0
        while (ei > 0):
            v = jcast('int', Code03_PathDfnXor1.to[ei])
            if (v != fa):
                Code03_PathDfnXor1.dfs1(v, u)
                Code03_PathDfnXor1.size[u] = jcast('int', jcast('int', jadd(Code03_PathDfnXor1.size[u], Code03_PathDfnXor1.size[v])))
            ei = jcast('int', Code03_PathDfnXor1.next[ei])

    # 按道理说dfs2应该改成迭代版，防止递归爆栈
    # 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
    # 有兴趣的同学可以看一下，讲解118，详解了树上dfs从递归版改迭代版
    @staticmethod
    def dfs2(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code03_PathDfnXor1.root1, Code03_PathDfnXor1.dfn[u], Code03_PathDfnXor1.insert(Code03_PathDfnXor1.arr[u], Code03_PathDfnXor1.root1[jcast('int', (Code03_PathDfnXor1.dfn[u] - 1))]))
        jset(Code03_PathDfnXor1.root2, u, Code03_PathDfnXor1.insert(Code03_PathDfnXor1.arr[u], Code03_PathDfnXor1.root2[fa]))
        ei = jcast('int', Code03_PathDfnXor1.head[u])
        while (ei > 0):
            if (Code03_PathDfnXor1.to[ei] != fa):
                Code03_PathDfnXor1.dfs2(Code03_PathDfnXor1.to[ei], u)
            ei = jcast('int', Code03_PathDfnXor1.next[ei])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code03_PathDfnXor1.deep[a] < Code03_PathDfnXor1.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code03_PathDfnXor1.MAXP - 1)))
        while (p >= 0):
            if (Code03_PathDfnXor1.deep[Code03_PathDfnXor1.stjump[a][p]] >= Code03_PathDfnXor1.deep[b]):
                a = jcast('int', Code03_PathDfnXor1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code03_PathDfnXor1.MAXP - 1)))
        while (p >= 0):
            if (Code03_PathDfnXor1.stjump[a][p] != Code03_PathDfnXor1.stjump[b][p]):
                a = jcast('int', Code03_PathDfnXor1.stjump[a][p])
                b = jcast('int', Code03_PathDfnXor1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code03_PathDfnXor1.stjump[a][0])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_PathDfnXor1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_PathDfnXor1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_PathDfnXor1.n):
            jcall(in_, 'nextToken')
            Code03_PathDfnXor1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code03_PathDfnXor1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_PathDfnXor1.addEdge(u, v)
            Code03_PathDfnXor1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code03_PathDfnXor1.dfs1(1, 0)
        Code03_PathDfnXor1.dfs2(1, 0)
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= Code03_PathDfnXor1.m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            y = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(out, 'println', Code03_PathDfnXor1.query(y, Code03_PathDfnXor1.root1[jcast('int', (Code03_PathDfnXor1.dfn[x] - 1))], Code03_PathDfnXor1.root1[jcast('int', (jcast('int', jadd(Code03_PathDfnXor1.dfn[x], Code03_PathDfnXor1.size[x])) - 1))]))
            else:
                jcall(in_, 'nextToken')
                z = jcast('int', jcast('int', jget(in_, 'nval')))
                lcafa = jcast('int', Code03_PathDfnXor1.stjump[Code03_PathDfnXor1.lca(x, y)][0])
                ans = jcast('int', jstatic('Math', 'max', Code03_PathDfnXor1.query(z, Code03_PathDfnXor1.root2[lcafa], Code03_PathDfnXor1.root2[x]), Code03_PathDfnXor1.query(z, Code03_PathDfnXor1.root2[lcafa], Code03_PathDfnXor1.root2[y])))
                jcall(out, 'println', ans)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_PathDfnXor1.MAXN = jcast('int', 100001)
Code03_PathDfnXor1.MAXT = jcast('int', jcast('int', (Code03_PathDfnXor1.MAXN * 62)))
Code03_PathDfnXor1.MAXP = jcast('int', 16)
Code03_PathDfnXor1.BIT = jcast('int', 29)
Code03_PathDfnXor1.n = jcast('int', 0)
Code03_PathDfnXor1.m = jcast('int', 0)
Code03_PathDfnXor1.arr = jarray('int', [Code03_PathDfnXor1.MAXN])
Code03_PathDfnXor1.head = jarray('int', [Code03_PathDfnXor1.MAXN])
Code03_PathDfnXor1.next = jarray('int', [jcast('int', (Code03_PathDfnXor1.MAXN << (1 & 31)))])
Code03_PathDfnXor1.to = jarray('int', [jcast('int', (Code03_PathDfnXor1.MAXN << (1 & 31)))])
Code03_PathDfnXor1.cntg = jcast('int', 0)
Code03_PathDfnXor1.deep = jarray('int', [Code03_PathDfnXor1.MAXN])
Code03_PathDfnXor1.size = jarray('int', [Code03_PathDfnXor1.MAXN])
Code03_PathDfnXor1.stjump = jarray('int', [Code03_PathDfnXor1.MAXN, Code03_PathDfnXor1.MAXP])
Code03_PathDfnXor1.dfn = jarray('int', [Code03_PathDfnXor1.MAXN])
Code03_PathDfnXor1.cntd = jcast('int', 0)
Code03_PathDfnXor1.root1 = jarray('int', [Code03_PathDfnXor1.MAXN])
Code03_PathDfnXor1.root2 = jarray('int', [Code03_PathDfnXor1.MAXN])
Code03_PathDfnXor1.tree = jarray('int', [Code03_PathDfnXor1.MAXT, 2])
Code03_PathDfnXor1.pass_ = jarray('int', [Code03_PathDfnXor1.MAXT])
Code03_PathDfnXor1.cntt = jcast('int', 0)

if __name__ == '__main__':
    Code03_PathDfnXor1.main([])
