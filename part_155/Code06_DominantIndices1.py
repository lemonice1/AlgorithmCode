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

# 长链剖分优化动态规划模版题，Python版
# 一共有n个节点，给定n-1条边，所有节点连成一棵树，规定1号节点是头
# 规定任何点到自己的距离为0
# 定义d(u, x)，以u为头的子树中，到u的距离为x的节点数
# 对于每个点u，想知道哪个尽量小的x，能取得最大的d(u, x)值
# 打印每个点的答案x
# 1 <= n <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/CF1009F
# 测试链接 : https://codeforces.com/problemset/problem/1009/F
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_DominantIndices1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'len': 'len', 'son': 'son', 'dfn': 'dfn', 'cntd': 'cntd', 'dp': 'dp', 'ansx': 'ansx', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    n = 0
    # 链式前向星
    head = None
    next = None
    to = None
    cntg = 0
    # 长链剖分
    len = None
    son = None
    dfn = None
    cntd = 0
    # 动态规划
    dp = None
    # 答案数组
    ansx = None
    @staticmethod
    def setdp(u, i, v):
        u = jcast('int', u)
        i = jcast('int', i)
        v = jcast('int', v)
        jset(Code06_DominantIndices1.dp, jcast('int', jadd(Code06_DominantIndices1.dfn[u], i)), v)

    @staticmethod
    def getdp(u, i):
        u = jcast('int', u)
        i = jcast('int', i)
        return jcast('int', Code06_DominantIndices1.dp[jcast('int', jadd(Code06_DominantIndices1.dfn[u], i))])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_DominantIndices1.next, ((_java_obj_1 := Code06_DominantIndices1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_DominantIndices1.head[u])
        Code06_DominantIndices1.to[Code06_DominantIndices1.cntg] = jcast('int', v)
        Code06_DominantIndices1.head[u] = jcast('int', Code06_DominantIndices1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用；迭代写法见 dfs3 方法
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code06_DominantIndices1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_DominantIndices1.to[e])
            if (v != fa):
                Code06_DominantIndices1.dfs1(v, u)
            e = jcast('int', Code06_DominantIndices1.next[e])
        e = jcast('int', Code06_DominantIndices1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_DominantIndices1.to[e])
            if (v != fa):
                if ((Code06_DominantIndices1.son[u] == 0) or (Code06_DominantIndices1.len[Code06_DominantIndices1.son[u]] < Code06_DominantIndices1.len[v])):
                    Code06_DominantIndices1.son[u] = jcast('int', v)
            e = jcast('int', Code06_DominantIndices1.next[e])
        Code06_DominantIndices1.len[u] = jcast('int', jcast('int', jadd(Code06_DominantIndices1.len[Code06_DominantIndices1.son[u]], 1)))

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用；迭代写法见 dfs4 方法
    @staticmethod
    def dfs2(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code06_DominantIndices1.dfn, u, ((_java_obj_4 := Code06_DominantIndices1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code06_DominantIndices1.setdp(u, 0, 1)
        Code06_DominantIndices1.ansx[u] = jcast('int', 0)
        if (Code06_DominantIndices1.son[u] == 0):
            return
        Code06_DominantIndices1.dfs2(Code06_DominantIndices1.son[u], u)
        e = jcast('int', Code06_DominantIndices1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_DominantIndices1.to[e])
            if ((v != fa) and (v != Code06_DominantIndices1.son[u])):
                Code06_DominantIndices1.dfs2(v, u)
            e = jcast('int', Code06_DominantIndices1.next[e])
        # 注意一定要在合并其他儿子dp信息的过程中，去更新ansx
        # 千万不要，最后再遍历一遍u的dp信息，然后更新ansx
        # 因为任何for循环，都不能是长链的规模！
        # 如果for循环是长链的规模，那么u遍历下去，u的重儿子又遍历下去，长链上每个节点都遍历下去
        # 时间复杂度必然不再是O(n)，而是O(n^2)，长链剖分的优势就不存在了！
        # 所以长链信息会被u直接继承，绝对不要有任何与长链的长度等规模的循环出现！
        Code06_DominantIndices1.ansx[u] = jcast('int', jcast('int', jadd(Code06_DominantIndices1.ansx[Code06_DominantIndices1.son[u]], 1)))
        e = jcast('int', Code06_DominantIndices1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_DominantIndices1.to[e])
            if ((v != fa) and (v != Code06_DominantIndices1.son[u])):
                i = jcast('int', 1)
                while (i <= Code06_DominantIndices1.len[v]):
                    Code06_DominantIndices1.setdp(u, i, jcast('int', jadd(Code06_DominantIndices1.getdp(u, i), Code06_DominantIndices1.getdp(v, jcast('int', (i - 1))))))
                    if ((Code06_DominantIndices1.getdp(u, i) > Code06_DominantIndices1.getdp(u, Code06_DominantIndices1.ansx[u])) or ((Code06_DominantIndices1.getdp(u, i) == Code06_DominantIndices1.getdp(u, Code06_DominantIndices1.ansx[u])) and (i < Code06_DominantIndices1.ansx[u]))):
                        Code06_DominantIndices1.ansx[u] = jcast('int', i)
                    i = jcast('int', (i + 1))
            e = jcast('int', Code06_DominantIndices1.next[e])
        # 如果u的某个距离，获得的最大节点数为1
        # 那么u答案就是0距离，因为u到u自己的距离是0，也有1个节点了
        # 根据题目要求，返回尽量小的距离
        if (Code06_DominantIndices1.getdp(u, Code06_DominantIndices1.ansx[u]) == 1):
            Code06_DominantIndices1.ansx[u] = jcast('int', 0)

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
    ufe = None
    stacksize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        jset(Code06_DominantIndices1.ufe[Code06_DominantIndices1.stacksize], 0, a)
        jset(Code06_DominantIndices1.ufe[Code06_DominantIndices1.stacksize], 1, b)
        jset(Code06_DominantIndices1.ufe[Code06_DominantIndices1.stacksize], 2, c)
        Code06_DominantIndices1.stacksize = jcast('int', (Code06_DominantIndices1.stacksize + 1))

    @staticmethod
    def pop():
        Code06_DominantIndices1.stacksize = jcast('int', (Code06_DominantIndices1.stacksize - 1))
        Code06_DominantIndices1.u = jcast('int', Code06_DominantIndices1.ufe[Code06_DominantIndices1.stacksize][0])
        Code06_DominantIndices1.f = jcast('int', Code06_DominantIndices1.ufe[Code06_DominantIndices1.stacksize][1])
        Code06_DominantIndices1.e = jcast('int', Code06_DominantIndices1.ufe[Code06_DominantIndices1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code06_DominantIndices1.stacksize = jcast('int', 0)
        Code06_DominantIndices1.push(1, 0, jcast('int', (-1)))
        v = 0
        while (Code06_DominantIndices1.stacksize > 0):
            Code06_DominantIndices1.pop()
            if (Code06_DominantIndices1.e == jcast('int', (-1))):
                Code06_DominantIndices1.e = jcast('int', Code06_DominantIndices1.head[Code06_DominantIndices1.u])
            else:
                Code06_DominantIndices1.e = jcast('int', Code06_DominantIndices1.next[Code06_DominantIndices1.e])
            if (Code06_DominantIndices1.e != 0):
                Code06_DominantIndices1.push(Code06_DominantIndices1.u, Code06_DominantIndices1.f, Code06_DominantIndices1.e)
                v = jcast('int', Code06_DominantIndices1.to[Code06_DominantIndices1.e])
                if (v != Code06_DominantIndices1.f):
                    Code06_DominantIndices1.push(v, Code06_DominantIndices1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code06_DominantIndices1.head[Code06_DominantIndices1.u])
                while (ei > 0):
                    v = jcast('int', Code06_DominantIndices1.to[ei])
                    if (v != Code06_DominantIndices1.f):
                        if ((Code06_DominantIndices1.son[Code06_DominantIndices1.u] == 0) or (Code06_DominantIndices1.len[Code06_DominantIndices1.son[Code06_DominantIndices1.u]] < Code06_DominantIndices1.len[v])):
                            Code06_DominantIndices1.son[Code06_DominantIndices1.u] = jcast('int', v)
                    ei = jcast('int', Code06_DominantIndices1.next[ei])
                Code06_DominantIndices1.len[Code06_DominantIndices1.u] = jcast('int', jcast('int', jadd(Code06_DominantIndices1.len[Code06_DominantIndices1.son[Code06_DominantIndices1.u]], 1)))

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code06_DominantIndices1.stacksize = jcast('int', 0)
        Code06_DominantIndices1.push(1, 0, jcast('int', (-1)))
        v = 0
        while (Code06_DominantIndices1.stacksize > 0):
            try:
                Code06_DominantIndices1.pop()
                if (Code06_DominantIndices1.e == jcast('int', (-1))):
                    jset(Code06_DominantIndices1.dfn, Code06_DominantIndices1.u, ((_java_obj_8 := Code06_DominantIndices1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    Code06_DominantIndices1.setdp(Code06_DominantIndices1.u, 0, 1)
                    Code06_DominantIndices1.ansx[Code06_DominantIndices1.u] = jcast('int', 0)
                    if (Code06_DominantIndices1.son[Code06_DominantIndices1.u] == 0):
                        raise JContinue(None)
                    Code06_DominantIndices1.push(Code06_DominantIndices1.u, Code06_DominantIndices1.f, jcast('int', (-2)))
                    Code06_DominantIndices1.push(Code06_DominantIndices1.son[Code06_DominantIndices1.u], Code06_DominantIndices1.u, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code06_DominantIndices1.e == jcast('int', (-2))):
                        Code06_DominantIndices1.e = jcast('int', Code06_DominantIndices1.head[Code06_DominantIndices1.u])
                    else:
                        Code06_DominantIndices1.e = jcast('int', Code06_DominantIndices1.next[Code06_DominantIndices1.e])
                if (Code06_DominantIndices1.e != 0):
                    Code06_DominantIndices1.push(Code06_DominantIndices1.u, Code06_DominantIndices1.f, Code06_DominantIndices1.e)
                    v = jcast('int', Code06_DominantIndices1.to[Code06_DominantIndices1.e])
                    if ((v != Code06_DominantIndices1.f) and (v != Code06_DominantIndices1.son[Code06_DominantIndices1.u])):
                        Code06_DominantIndices1.push(v, Code06_DominantIndices1.u, jcast('int', (-1)))
                else:
                    Code06_DominantIndices1.ansx[Code06_DominantIndices1.u] = jcast('int', jcast('int', jadd(Code06_DominantIndices1.ansx[Code06_DominantIndices1.son[Code06_DominantIndices1.u]], 1)))
                    e = jcast('int', Code06_DominantIndices1.head[Code06_DominantIndices1.u])
                    while (e > 0):
                        v = jcast('int', Code06_DominantIndices1.to[e])
                        if ((v != Code06_DominantIndices1.f) and (v != Code06_DominantIndices1.son[Code06_DominantIndices1.u])):
                            i = jcast('int', 1)
                            while (i <= Code06_DominantIndices1.len[v]):
                                Code06_DominantIndices1.setdp(Code06_DominantIndices1.u, i, jcast('int', jadd(Code06_DominantIndices1.getdp(Code06_DominantIndices1.u, i), Code06_DominantIndices1.getdp(v, jcast('int', (i - 1))))))
                                if ((Code06_DominantIndices1.getdp(Code06_DominantIndices1.u, i) > Code06_DominantIndices1.getdp(Code06_DominantIndices1.u, Code06_DominantIndices1.ansx[Code06_DominantIndices1.u])) or ((Code06_DominantIndices1.getdp(Code06_DominantIndices1.u, i) == Code06_DominantIndices1.getdp(Code06_DominantIndices1.u, Code06_DominantIndices1.ansx[Code06_DominantIndices1.u])) and (i < Code06_DominantIndices1.ansx[Code06_DominantIndices1.u]))):
                                    Code06_DominantIndices1.ansx[Code06_DominantIndices1.u] = jcast('int', i)
                                i = jcast('int', (i + 1))
                        e = jcast('int', Code06_DominantIndices1.next[e])
                    if (Code06_DominantIndices1.getdp(Code06_DominantIndices1.u, Code06_DominantIndices1.ansx[Code06_DominantIndices1.u]) == 1):
                        Code06_DominantIndices1.ansx[Code06_DominantIndices1.u] = jcast('int', 0)
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_DominantIndices1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code06_DominantIndices1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code06_DominantIndices1.addEdge(u, v)
            Code06_DominantIndices1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code06_DominantIndices1.dfs3()
        Code06_DominantIndices1.dfs4()
        i = jcast('int', 1)
        while (i <= Code06_DominantIndices1.n):
            jcall(out, 'println', Code06_DominantIndices1.ansx[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_DominantIndices1.MAXN = jcast('int', 1000001)
Code06_DominantIndices1.n = jcast('int', 0)
Code06_DominantIndices1.head = jarray('int', [Code06_DominantIndices1.MAXN])
Code06_DominantIndices1.next = jarray('int', [jcast('int', (Code06_DominantIndices1.MAXN << (1 & 31)))])
Code06_DominantIndices1.to = jarray('int', [jcast('int', (Code06_DominantIndices1.MAXN << (1 & 31)))])
Code06_DominantIndices1.cntg = jcast('int', 0)
Code06_DominantIndices1.len = jarray('int', [Code06_DominantIndices1.MAXN])
Code06_DominantIndices1.son = jarray('int', [Code06_DominantIndices1.MAXN])
Code06_DominantIndices1.dfn = jarray('int', [Code06_DominantIndices1.MAXN])
Code06_DominantIndices1.cntd = jcast('int', 0)
Code06_DominantIndices1.dp = jarray('int', [Code06_DominantIndices1.MAXN])
Code06_DominantIndices1.ansx = jarray('int', [Code06_DominantIndices1.MAXN])
Code06_DominantIndices1.ufe = jarray('int', [Code06_DominantIndices1.MAXN, 3])
Code06_DominantIndices1.stacksize = jcast('int', 0)
Code06_DominantIndices1.u = jcast('int', 0)
Code06_DominantIndices1.f = jcast('int', 0)
Code06_DominantIndices1.e = jcast('int', 0)

if __name__ == '__main__':
    Code06_DominantIndices1.main([])
