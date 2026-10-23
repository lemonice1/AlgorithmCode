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

# 表亲数量，Python版
# 一共有n个节点，编号1~n，给定每个节点的父亲节点编号，父亲节点为0，说明当前节点是某棵树的头
# 注意，n个节点组成的是森林结构，可能有若干棵树
# 一共有m条查询，每条查询 x k，含义如下
# 如果x往上走k的距离，没有祖先节点，打印0
# 如果x往上走k的距离，能找到祖先节点a，那么从a往下走k的距离，除了x之外，可能还有其他节点
# 这些节点叫做x的k级表亲，打印这个表亲的数量
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF208E
# 测试链接 : https://codeforces.com/problemset/problem/208/E
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_BloodCousins1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'root': 'root', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headq': 'headq', 'nextq': 'nextq', 'ansiq': 'ansiq', 'kq': 'kq', 'cntq': 'cntq', 'siz': 'siz', 'dep': 'dep', 'son': 'son', 'stjump': 'stjump', 'depCnt': 'depCnt', 'ans': 'ans'}
    MAXN = 0
    MAXP = 0
    n = 0
    m = 0
    root = None
    # 链式前向星
    headg = None
    nextg = None
    tog = None
    cntg = 0
    # 问题列表
    headq = None
    nextq = None
    ansiq = None
    kq = None
    cntq = 0
    # 树链剖分
    siz = None
    dep = None
    son = None
    stjump = None
    # 树上启发式合并
    depCnt = None
    ans = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_BloodCousins1.nextg, ((_java_obj_1 := Code05_BloodCousins1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_BloodCousins1.headg[u])
        Code05_BloodCousins1.tog[Code05_BloodCousins1.cntg] = jcast('int', v)
        Code05_BloodCousins1.headg[u] = jcast('int', Code05_BloodCousins1.cntg)

    @staticmethod
    def addQuestion(u, i, k):
        u = jcast('int', u)
        i = jcast('int', i)
        k = jcast('int', k)
        jset(Code05_BloodCousins1.nextq, ((_java_obj_4 := Code05_BloodCousins1), (_java_key_5 := 'cntq'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code05_BloodCousins1.headq[u])
        Code05_BloodCousins1.ansiq[Code05_BloodCousins1.cntq] = jcast('int', i)
        Code05_BloodCousins1.kq[Code05_BloodCousins1.cntq] = jcast('int', k)
        Code05_BloodCousins1.headq[u] = jcast('int', Code05_BloodCousins1.cntq)

    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_BloodCousins1.siz[u] = jcast('int', 1)
        Code05_BloodCousins1.dep[u] = jcast('int', jcast('int', jadd(Code05_BloodCousins1.dep[fa], 1)))
        jset(Code05_BloodCousins1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code05_BloodCousins1.MAXP):
            jset(Code05_BloodCousins1.stjump[u], p, Code05_BloodCousins1.stjump[Code05_BloodCousins1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code05_BloodCousins1.headg[u])
        while (e > 0):
            Code05_BloodCousins1.dfs1(Code05_BloodCousins1.tog[e], u)
            e = jcast('int', Code05_BloodCousins1.nextg[e])
        e = jcast('int', Code05_BloodCousins1.headg[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_BloodCousins1.tog[e])
            Code05_BloodCousins1.siz[u] = jcast('int', jcast('int', jadd(Code05_BloodCousins1.siz[u], Code05_BloodCousins1.siz[v])))
            if ((Code05_BloodCousins1.son[u] == 0) or (Code05_BloodCousins1.siz[Code05_BloodCousins1.son[u]] < Code05_BloodCousins1.siz[v])):
                Code05_BloodCousins1.son[u] = jcast('int', v)
            e = jcast('int', Code05_BloodCousins1.nextg[e])

    @staticmethod
    def kAncestor(u, k):
        u = jcast('int', u)
        k = jcast('int', k)
        p = jcast('int', jcast('int', (Code05_BloodCousins1.MAXP - 1)))
        while (p >= 0):
            if (k >= jcast('int', (1 << (p & 31)))):
                k = jcast('int', jcast('int', (k - jcast('int', (1 << (p & 31))))))
                u = jcast('int', Code05_BloodCousins1.stjump[u][p])
            p = jcast('int', (p - 1))
        return jcast('int', u)

    @staticmethod
    def effect(u):
        u = jcast('int', u)
        ((_java_obj_7 := Code05_BloodCousins1.depCnt), (_java_key_8 := Code05_BloodCousins1.dep[u]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]
        e = jcast('int', Code05_BloodCousins1.headg[u])
        while (e > 0):
            Code05_BloodCousins1.effect(Code05_BloodCousins1.tog[e])
            e = jcast('int', Code05_BloodCousins1.nextg[e])

    @staticmethod
    def cancel(u):
        u = jcast('int', u)
        ((_java_obj_10 := Code05_BloodCousins1.depCnt), (_java_key_11 := Code05_BloodCousins1.dep[u]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]
        e = jcast('int', Code05_BloodCousins1.headg[u])
        while (e > 0):
            Code05_BloodCousins1.cancel(Code05_BloodCousins1.tog[e])
            e = jcast('int', Code05_BloodCousins1.nextg[e])

    @staticmethod
    def dfs2(u, keep):
        u = jcast('int', u)
        keep = jcast('int', keep)
        e = jcast('int', Code05_BloodCousins1.headg[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_BloodCousins1.tog[e])
            if (v != Code05_BloodCousins1.son[u]):
                Code05_BloodCousins1.dfs2(v, 0)
            e = jcast('int', Code05_BloodCousins1.nextg[e])
        if (Code05_BloodCousins1.son[u] != 0):
            Code05_BloodCousins1.dfs2(Code05_BloodCousins1.son[u], 1)
        ((_java_obj_13 := Code05_BloodCousins1.depCnt), (_java_key_14 := Code05_BloodCousins1.dep[u]), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]
        e = jcast('int', Code05_BloodCousins1.headg[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_BloodCousins1.tog[e])
            if (v != Code05_BloodCousins1.son[u]):
                Code05_BloodCousins1.effect(v)
            e = jcast('int', Code05_BloodCousins1.nextg[e])
        i = jcast('int', Code05_BloodCousins1.headq[u])
        while (i > 0):
            jset(Code05_BloodCousins1.ans, Code05_BloodCousins1.ansiq[i], Code05_BloodCousins1.depCnt[jcast('int', jadd(Code05_BloodCousins1.dep[u], Code05_BloodCousins1.kq[i]))])
            i = jcast('int', Code05_BloodCousins1.nextq[i])
        if (keep == 0):
            Code05_BloodCousins1.cancel(u)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_BloodCousins1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        father = 0
        while (i <= Code05_BloodCousins1.n):
            jcall(in_, 'nextToken')
            father = jcast('int', jcast('int', jget(in_, 'nval')))
            if (father == 0):
                Code05_BloodCousins1.root[i] = jcast('boolean', True)
            else:
                Code05_BloodCousins1.addEdge(father, i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_BloodCousins1.n):
            if Code05_BloodCousins1.root[i]:
                Code05_BloodCousins1.dfs1(i, 0)
            i = jcast('int', (i + 1))
        jcall(in_, 'nextToken')
        Code05_BloodCousins1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        k = 0
        kfather = 0
        while (i <= Code05_BloodCousins1.m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            k = jcast('int', jcast('int', jget(in_, 'nval')))
            kfather = jcast('int', Code05_BloodCousins1.kAncestor(u, k))
            if (kfather != 0):
                Code05_BloodCousins1.addQuestion(kfather, i, k)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_BloodCousins1.n):
            if Code05_BloodCousins1.root[i]:
                Code05_BloodCousins1.dfs2(i, 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_BloodCousins1.m):
            if (Code05_BloodCousins1.ans[i] == 0):
                jcall(out, 'print', '0 ')
            else:
                jcall(out, 'print', jadd(jcast('int', (Code05_BloodCousins1.ans[i] - 1)), ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_BloodCousins1.MAXN = jcast('int', 100001)
Code05_BloodCousins1.MAXP = jcast('int', 20)
Code05_BloodCousins1.n = jcast('int', 0)
Code05_BloodCousins1.m = jcast('int', 0)
Code05_BloodCousins1.root = jarray('boolean', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.headg = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.nextg = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.tog = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.cntg = jcast('int', 0)
Code05_BloodCousins1.headq = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.nextq = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.ansiq = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.kq = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.cntq = jcast('int', 0)
Code05_BloodCousins1.siz = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.dep = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.son = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.stjump = jarray('int', [Code05_BloodCousins1.MAXN, Code05_BloodCousins1.MAXP])
Code05_BloodCousins1.depCnt = jarray('int', [Code05_BloodCousins1.MAXN])
Code05_BloodCousins1.ans = jarray('int', [Code05_BloodCousins1.MAXN])

if __name__ == '__main__':
    Code05_BloodCousins1.main([])
