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

# 火热旅馆，Python版
# 一共有n个节点，给定n-1条边，所有节点连成一棵树
# 三个点构成一个点组(a, b, c)，打乱顺序认为是同一个点组
# 求树上有多少点组，内部任意两个节点之间的距离是一样的
# 1 <= n <= 10^5
# 答案一定在long类型范围内
# 测试链接 : https://www.luogu.com.cn/problem/P5904
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_HotHotels1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'son': 'son', 'len': 'len', 'cntd': 'cntd', 'fid': 'fid', 'gid': 'gid', 'f': 'f', 'g': 'g', 'ans': 'ans'}
    MAXN = 0
    n = 0
    # 链式前向星
    head = None
    next = None
    to = None
    cntg = 0
    # 长链剖分
    fa = None
    son = None
    len = None
    cntd = 0
    # 动态规划
    # 每个点在动态规划表f中的开始位置，就是dfn序
    fid = None
    # 每个点在动态规划表g中的开始位置，课上讲的设计
    gid = None
    # 动态规划表f，f[父][i]依赖f[子][i-1]
    f = None
    # 动态规划表g，g[父][i]依赖g[子][i+1]
    g = None
    # 答案
    ans = 0
    @staticmethod
    def setf(u, i, v):
        u = jcast('int', u)
        i = jcast('int', i)
        v = jcast('long', v)
        jset(Code07_HotHotels1.f, jcast('int', jadd(Code07_HotHotels1.fid[u], i)), v)

    @staticmethod
    def getf(u, i):
        u = jcast('int', u)
        i = jcast('int', i)
        return jcast('long', Code07_HotHotels1.f[jcast('int', jadd(Code07_HotHotels1.fid[u], i))])

    @staticmethod
    def setg(u, i, v):
        u = jcast('int', u)
        i = jcast('int', i)
        v = jcast('long', v)
        jset(Code07_HotHotels1.g, jcast('int', jadd(Code07_HotHotels1.gid[u], i)), v)

    @staticmethod
    def getg(u, i):
        u = jcast('int', u)
        i = jcast('int', i)
        return jcast('long', Code07_HotHotels1.g[jcast('int', jadd(Code07_HotHotels1.gid[u], i))])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_HotHotels1.next, ((_java_obj_1 := Code07_HotHotels1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_HotHotels1.head[u])
        Code07_HotHotels1.to[Code07_HotHotels1.cntg] = jcast('int', v)
        Code07_HotHotels1.head[u] = jcast('int', Code07_HotHotels1.cntg)

    # 本版本保留递归写法，深层遍历需考虑调用栈与内存开销
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code07_HotHotels1.fa[u] = jcast('int', f)
        e = jcast('int', Code07_HotHotels1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_HotHotels1.to[e])
            if (v != f):
                Code07_HotHotels1.dfs1(v, u)
            e = jcast('int', Code07_HotHotels1.next[e])
        e = jcast('int', Code07_HotHotels1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_HotHotels1.to[e])
            if (v != f):
                if ((Code07_HotHotels1.son[u] == 0) or (Code07_HotHotels1.len[Code07_HotHotels1.son[u]] < Code07_HotHotels1.len[v])):
                    Code07_HotHotels1.son[u] = jcast('int', v)
            e = jcast('int', Code07_HotHotels1.next[e])
        Code07_HotHotels1.len[u] = jcast('int', jcast('int', jadd(Code07_HotHotels1.len[Code07_HotHotels1.son[u]], 1)))

    # 本版本保留递归写法，深层遍历需考虑调用栈与内存开销
    # 给每个节点分配fid和gid
    @staticmethod
    def dfs2(u, top):
        u = jcast('int', u)
        top = jcast('int', top)
        jset(Code07_HotHotels1.fid, u, ((_java_obj_4 := Code07_HotHotels1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])
        if (Code07_HotHotels1.son[u] == 0):
            Code07_HotHotels1.gid[u] = jcast('int', jcast('int', (Code07_HotHotels1.fid[top] * 2)))
            return
        Code07_HotHotels1.dfs2(Code07_HotHotels1.son[u], top)
        e = jcast('int', Code07_HotHotels1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_HotHotels1.to[e])
            if ((v != Code07_HotHotels1.son[u]) and (v != Code07_HotHotels1.fa[u])):
                Code07_HotHotels1.dfs2(v, v)
            e = jcast('int', Code07_HotHotels1.next[e])
        Code07_HotHotels1.gid[u] = jcast('int', jcast('int', jadd(Code07_HotHotels1.gid[Code07_HotHotels1.son[u]], 1)))

    # 本版本保留递归写法，深层遍历需考虑调用栈与内存开销
    # 计算每个节点的f信息和g信息，同时统计答案
    @staticmethod
    def dfs3(u):
        u = jcast('int', u)
        Code07_HotHotels1.setf(u, 0, 1)
        if (Code07_HotHotels1.son[u] == 0):
            return
        Code07_HotHotels1.dfs3(Code07_HotHotels1.son[u])
        e = jcast('int', Code07_HotHotels1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_HotHotels1.to[e])
            if ((v != Code07_HotHotels1.son[u]) and (v != Code07_HotHotels1.fa[u])):
                Code07_HotHotels1.dfs3(v)
            e = jcast('int', Code07_HotHotels1.next[e])
        e = jcast('int', Code07_HotHotels1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_HotHotels1.to[e])
            if ((v != Code07_HotHotels1.son[u]) and (v != Code07_HotHotels1.fa[u])):
                # 情况2，u树上，选择三个点，u没被选中，但跨u选点
                i = jcast('int', 0)
                while (i <= Code07_HotHotels1.len[v]):
                    # 情况2的分支一，之前遍历的子树里选两个点，当前子树里选一个点
                    if ((i < Code07_HotHotels1.len[u]) and (jcast('int', (i - 1)) >= 0)):
                        Code07_HotHotels1.ans = jcast('long', jcast('long', jadd(Code07_HotHotels1.ans, jcast('long', (Code07_HotHotels1.getg(u, i) * Code07_HotHotels1.getf(v, jcast('int', (i - 1))))))))
                    # 情况2的分支二，之前遍历的子树里选一个点，当前子树里选两个点
                    if ((i > 0) and (jcast('int', jadd(i, 1)) < Code07_HotHotels1.len[v])):
                        Code07_HotHotels1.ans = jcast('long', jcast('long', jadd(Code07_HotHotels1.ans, jcast('long', (Code07_HotHotels1.getf(u, i) * Code07_HotHotels1.getg(v, jcast('int', jadd(i, 1))))))))
                    i = jcast('int', (i + 1))
                i = jcast('int', 0)
                while (i <= Code07_HotHotels1.len[v]):
                    if (jcast('int', jadd(i, 1)) < Code07_HotHotels1.len[v]):
                        Code07_HotHotels1.setg(u, i, jcast('long', jadd(Code07_HotHotels1.getg(u, i), Code07_HotHotels1.getg(v, jcast('int', jadd(i, 1))))))
                    if (jcast('int', (i - 1)) >= 0):
                        Code07_HotHotels1.setg(u, i, jcast('long', jadd(Code07_HotHotels1.getg(u, i), jcast('long', (Code07_HotHotels1.getf(u, i) * Code07_HotHotels1.getf(v, jcast('int', (i - 1))))))))
                    i = jcast('int', (i + 1))
                i = jcast('int', 0)
                while (i <= Code07_HotHotels1.len[v]):
                    if (jcast('int', (i - 1)) >= 0):
                        Code07_HotHotels1.setf(u, i, jcast('long', jadd(Code07_HotHotels1.getf(u, i), Code07_HotHotels1.getf(v, jcast('int', (i - 1))))))
                    i = jcast('int', (i + 1))
            e = jcast('int', Code07_HotHotels1.next[e])
        # 情况1，u树上，选择三个点，u被选中
        Code07_HotHotels1.ans = jcast('long', jcast('long', jadd(Code07_HotHotels1.ans, Code07_HotHotels1.getg(u, 0))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code07_HotHotels1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_HotHotels1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code07_HotHotels1.addEdge(u, v)
            Code07_HotHotels1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code07_HotHotels1.dfs1(1, 0)
        Code07_HotHotels1.dfs2(1, 1)
        Code07_HotHotels1.dfs3(1)
        jcall(out, 'println', Code07_HotHotels1.ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_HotHotels1.MAXN = jcast('int', 100001)
Code07_HotHotels1.n = jcast('int', 0)
Code07_HotHotels1.head = jarray('int', [Code07_HotHotels1.MAXN])
Code07_HotHotels1.next = jarray('int', [jcast('int', (Code07_HotHotels1.MAXN << (1 & 31)))])
Code07_HotHotels1.to = jarray('int', [jcast('int', (Code07_HotHotels1.MAXN << (1 & 31)))])
Code07_HotHotels1.cntg = jcast('int', 0)
Code07_HotHotels1.fa = jarray('int', [Code07_HotHotels1.MAXN])
Code07_HotHotels1.son = jarray('int', [Code07_HotHotels1.MAXN])
Code07_HotHotels1.len = jarray('int', [Code07_HotHotels1.MAXN])
Code07_HotHotels1.cntd = jcast('int', 0)
Code07_HotHotels1.fid = jarray('int', [Code07_HotHotels1.MAXN])
Code07_HotHotels1.gid = jarray('int', [Code07_HotHotels1.MAXN])
Code07_HotHotels1.f = jarray('long', [Code07_HotHotels1.MAXN])
Code07_HotHotels1.g = jarray('long', [jcast('int', (Code07_HotHotels1.MAXN << (1 & 31)))])
Code07_HotHotels1.ans = jcast('long', 0)

if __name__ == '__main__':
    Code07_HotHotels1.main([])
