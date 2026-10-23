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

# 树上倍增解法迭代版
# 测试链接 : https://www.luogu.com.cn/problem/P3379
# 所有递归函数一律改成等义的迭代版
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Multiply2:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'cnt': 'cnt', 'head': 'head', 'next': 'next', 'to': 'to', 'stjump': 'stjump', 'deep': 'deep', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    LIMIT = 0
    power = 0
    @staticmethod
    def log2(n):
        n = jcast('int', n)
        ans = jcast('int', 0)
        while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    cnt = 0
    head = None
    next = None
    to = None
    stjump = None
    deep = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code02_Multiply2.power = jcast('int', Code02_Multiply2.log2(n))
        Code02_Multiply2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code02_Multiply2.head, 1, jcast('int', jadd(n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code02_Multiply2.next[Code02_Multiply2.cnt] = jcast('int', Code02_Multiply2.head[u])
        Code02_Multiply2.to[Code02_Multiply2.cnt] = jcast('int', v)
        jset(Code02_Multiply2.head, u, ((_java_obj_1 := Code02_Multiply2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # dfs迭代版
    # ufe是为了实现迭代版而准备的栈
    ufe = None
    stackSize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code02_Multiply2.ufe[Code02_Multiply2.stackSize], 0, u)
        jset(Code02_Multiply2.ufe[Code02_Multiply2.stackSize], 1, f)
        jset(Code02_Multiply2.ufe[Code02_Multiply2.stackSize], 2, e)
        Code02_Multiply2.stackSize = jcast('int', (Code02_Multiply2.stackSize + 1))

    @staticmethod
    def pop():
        Code02_Multiply2.stackSize = jcast('int', (Code02_Multiply2.stackSize - 1))
        Code02_Multiply2.u = jcast('int', Code02_Multiply2.ufe[Code02_Multiply2.stackSize][0])
        Code02_Multiply2.f = jcast('int', Code02_Multiply2.ufe[Code02_Multiply2.stackSize][1])
        Code02_Multiply2.e = jcast('int', Code02_Multiply2.ufe[Code02_Multiply2.stackSize][2])

    @staticmethod
    def dfs(root):
        root = jcast('int', root)
        Code02_Multiply2.stackSize = jcast('int', 0)
        # 栈里存放三个信息
        # u : 当前处理的点
        # f : 当前点u的父节点
        # e : 处理到几号边了
        # 如果e==-1，表示之前没有处理过u的任何边
        # 如果e==0，表示u的边都已经处理完了
        Code02_Multiply2.push(root, 0, jcast('int', (-1)))
        while (Code02_Multiply2.stackSize > 0):
            Code02_Multiply2.pop()
            if (Code02_Multiply2.e == jcast('int', (-1))):
                Code02_Multiply2.deep[Code02_Multiply2.u] = jcast('int', jcast('int', jadd(Code02_Multiply2.deep[Code02_Multiply2.f], 1)))
                jset(Code02_Multiply2.stjump[Code02_Multiply2.u], 0, Code02_Multiply2.f)
                p = jcast('int', 1)
                while (p <= Code02_Multiply2.power):
                    jset(Code02_Multiply2.stjump[Code02_Multiply2.u], p, Code02_Multiply2.stjump[Code02_Multiply2.stjump[Code02_Multiply2.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code02_Multiply2.e = jcast('int', Code02_Multiply2.head[Code02_Multiply2.u])
            else:
                Code02_Multiply2.e = jcast('int', Code02_Multiply2.next[Code02_Multiply2.e])
            if (Code02_Multiply2.e != 0):
                Code02_Multiply2.push(Code02_Multiply2.u, Code02_Multiply2.f, Code02_Multiply2.e)
                if (Code02_Multiply2.to[Code02_Multiply2.e] != Code02_Multiply2.f):
                    Code02_Multiply2.push(Code02_Multiply2.to[Code02_Multiply2.e], Code02_Multiply2.u, jcast('int', (-1)))

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code02_Multiply2.deep[a] < Code02_Multiply2.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', Code02_Multiply2.power)
        while (p >= 0):
            if (Code02_Multiply2.deep[Code02_Multiply2.stjump[a][p]] >= Code02_Multiply2.deep[b]):
                a = jcast('int', Code02_Multiply2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', Code02_Multiply2.power)
        while (p >= 0):
            if (Code02_Multiply2.stjump[a][p] != Code02_Multiply2.stjump[b][p]):
                a = jcast('int', Code02_Multiply2.stjump[a][p])
                b = jcast('int', Code02_Multiply2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code02_Multiply2.stjump[a][0])

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
        Code02_Multiply2.build(n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_Multiply2.addEdge(u, v)
            Code02_Multiply2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code02_Multiply2.dfs(root)
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code02_Multiply2.lca(a, b))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Multiply2.MAXN = jcast('int', 500001)
Code02_Multiply2.LIMIT = jcast('int', 20)
Code02_Multiply2.power = jcast('int', 0)
Code02_Multiply2.cnt = jcast('int', 0)
Code02_Multiply2.head = jarray('int', [Code02_Multiply2.MAXN])
Code02_Multiply2.next = jarray('int', [jcast('int', (Code02_Multiply2.MAXN << (1 & 31)))])
Code02_Multiply2.to = jarray('int', [jcast('int', (Code02_Multiply2.MAXN << (1 & 31)))])
Code02_Multiply2.stjump = jarray('int', [Code02_Multiply2.MAXN, Code02_Multiply2.LIMIT])
Code02_Multiply2.deep = jarray('int', [Code02_Multiply2.MAXN])
Code02_Multiply2.ufe = jarray('int', [Code02_Multiply2.MAXN, 3])
Code02_Multiply2.stackSize = jcast('int', 0)
Code02_Multiply2.u = jcast('int', 0)
Code02_Multiply2.f = jcast('int', 0)
Code02_Multiply2.e = jcast('int', 0)

if __name__ == '__main__':
    Code02_Multiply2.main([])
