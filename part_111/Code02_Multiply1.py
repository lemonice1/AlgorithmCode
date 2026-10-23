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

# 树上倍增解法
# 测试链接 : https://www.luogu.com.cn/problem/P3379
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code02_Multiply2.py
class Code02_Multiply1:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'deep': 'deep', 'stjump': 'stjump'}
    MAXN = 0
    LIMIT = 0
    # 根据节点个数n，计算出2的几次方就够用了
    power = 0
    @staticmethod
    def log2(n):
        n = jcast('int', n)
        ans = jcast('int', 0)
        while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    # 链式前向星建图
    head = None
    next = None
    to = None
    cnt = 0
    # deep[i] : 节点i在第几层
    deep = None
    # stjump[i][p] : 节点i往上跳2的p次方步，到达的节点编号
    stjump = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code02_Multiply1.power = jcast('int', Code02_Multiply1.log2(n))
        Code02_Multiply1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code02_Multiply1.head, 1, jcast('int', jadd(n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code02_Multiply1.next[Code02_Multiply1.cnt] = jcast('int', Code02_Multiply1.head[u])
        Code02_Multiply1.to[Code02_Multiply1.cnt] = jcast('int', v)
        jset(Code02_Multiply1.head, u, ((_java_obj_1 := Code02_Multiply1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # dfs递归版
    # 一般来说都这么写，但是本题附加的测试数据很毒
    # 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code02_Multiply1.deep[u] = jcast('int', jcast('int', jadd(Code02_Multiply1.deep[f], 1)))
        jset(Code02_Multiply1.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p <= Code02_Multiply1.power):
            jset(Code02_Multiply1.stjump[u], p, Code02_Multiply1.stjump[Code02_Multiply1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code02_Multiply1.head[u])
        while (e != 0):
            if (Code02_Multiply1.to[e] != f):
                Code02_Multiply1.dfs(Code02_Multiply1.to[e], u)
            e = jcast('int', Code02_Multiply1.next[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code02_Multiply1.deep[a] < Code02_Multiply1.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', Code02_Multiply1.power)
        while (p >= 0):
            if (Code02_Multiply1.deep[Code02_Multiply1.stjump[a][p]] >= Code02_Multiply1.deep[b]):
                a = jcast('int', Code02_Multiply1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', Code02_Multiply1.power)
        while (p >= 0):
            if (Code02_Multiply1.stjump[a][p] != Code02_Multiply1.stjump[b][p]):
                a = jcast('int', Code02_Multiply1.stjump[a][p])
                b = jcast('int', Code02_Multiply1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code02_Multiply1.stjump[a][0])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        root = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_Multiply1.build(n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_Multiply1.addEdge(u, v)
            Code02_Multiply1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code02_Multiply1.dfs(root, 0)
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code02_Multiply1.lca(a, b))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Multiply1.MAXN = jcast('int', 500001)
Code02_Multiply1.LIMIT = jcast('int', 20)
Code02_Multiply1.power = jcast('int', 0)
Code02_Multiply1.head = jarray('int', [Code02_Multiply1.MAXN])
Code02_Multiply1.next = jarray('int', [jcast('int', (Code02_Multiply1.MAXN << (1 & 31)))])
Code02_Multiply1.to = jarray('int', [jcast('int', (Code02_Multiply1.MAXN << (1 & 31)))])
Code02_Multiply1.cnt = jcast('int', 0)
Code02_Multiply1.deep = jarray('int', [Code02_Multiply1.MAXN])
Code02_Multiply1.stjump = jarray('int', [Code02_Multiply1.MAXN, Code02_Multiply1.LIMIT])

if __name__ == '__main__':
    Code02_Multiply1.main([])
