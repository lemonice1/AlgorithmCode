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

# 删增边使其重心唯一
# 一共有n个节点，编号1~n，有n-1条边形成一棵树
# 现在希望重心是唯一的节点，调整的方式是先删除一条边、然后增加一条边
# 如果树上只有一个重心，需要删掉连接重心的任意一条边，再把这条边加上(否则无法通过已经实测)
# 如果树上有两个重心，调整的方式是先删除一条边、然后增加一条边，使重心是唯一的
# 如果方案有多种，打印其中一种即可
# 比如先删除节点3和节点4之间的边，再增加节点4和节点7之间的边，那么打印:
# "3 4"
# "4 7"
# 测试链接 : https://www.luogu.com.cn/problem/CF1406C
# 测试链接 : https://codeforces.com/problemset/problem/1406/C
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_LinkCutCentroids:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'size': 'size', 'maxsub': 'maxsub', 'centers': 'centers', 'leaf': 'leaf', 'leafFather': 'leafFather'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    cnt = 0
    # size[i] : 从1号节点开始dfs的过程中，以i为头的子树的节点数
    size = None
    # maxsub[i] : 如果节点i做整棵树的根，最大子树的大小
    maxsub = None
    # 收集所有的重心
    centers = None
    # 最大子树上的叶节点
    leaf = 0
    # 叶节点的父亲节点
    leafFather = 0
    @staticmethod
    def build():
        Code04_LinkCutCentroids.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code04_LinkCutCentroids.head, 1, jcast('int', jadd(Code04_LinkCutCentroids.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code04_LinkCutCentroids.next[Code04_LinkCutCentroids.cnt] = jcast('int', Code04_LinkCutCentroids.head[u])
        Code04_LinkCutCentroids.to[Code04_LinkCutCentroids.cnt] = jcast('int', v)
        jset(Code04_LinkCutCentroids.head, u, ((_java_obj_1 := Code04_LinkCutCentroids), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code04_LinkCutCentroids.size[u] = jcast('int', 1)
        Code04_LinkCutCentroids.maxsub[u] = jcast('int', 0)
        e = jcast('int', Code04_LinkCutCentroids.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code04_LinkCutCentroids.to[e])
            if (v != f):
                Code04_LinkCutCentroids.dfs(v, u)
                Code04_LinkCutCentroids.size[u] = jcast('int', jcast('int', jadd(Code04_LinkCutCentroids.size[u], Code04_LinkCutCentroids.size[v])))
                jset(Code04_LinkCutCentroids.maxsub, u, jstatic('Math', 'max', Code04_LinkCutCentroids.maxsub[u], Code04_LinkCutCentroids.size[v]))
            e = jcast('int', Code04_LinkCutCentroids.next[e])
        jset(Code04_LinkCutCentroids.maxsub, u, jstatic('Math', 'max', Code04_LinkCutCentroids.maxsub[u], jcast('int', (Code04_LinkCutCentroids.n - Code04_LinkCutCentroids.size[u]))))

    # 随意找一个叶节点和该叶节点的父亲节点
    # 哪一组都可以
    @staticmethod
    def find(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code04_LinkCutCentroids.head[u])
        while (e != 0):
            if (Code04_LinkCutCentroids.to[e] != f):
                Code04_LinkCutCentroids.find(Code04_LinkCutCentroids.to[e], u)
                return
            e = jcast('int', Code04_LinkCutCentroids.next[e])
        Code04_LinkCutCentroids.leaf = jcast('int', u)
        Code04_LinkCutCentroids.leafFather = jcast('int', f)

    # 返回重心的数量
    @staticmethod
    def centerCnt():
        m = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_LinkCutCentroids.n):
            if (Code04_LinkCutCentroids.maxsub[i] <= jcast('int', jdiv(Code04_LinkCutCentroids.n, 2))):
                jset(Code04_LinkCutCentroids.centers, ((_java_old_4 := m), (m := jcast('int', (m + (1)))), _java_old_4)[2], i)
            i = jcast('int', (i + 1))
        return jcast('int', m)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        testCase = jcast('int', jcast('int', jget(in_, 'nval')))
        t = jcast('int', 1)
        while (t <= testCase):
            jcall(in_, 'nextToken')
            Code04_LinkCutCentroids.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_LinkCutCentroids.build()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i < Code04_LinkCutCentroids.n):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                Code04_LinkCutCentroids.addEdge(u, v)
                Code04_LinkCutCentroids.addEdge(v, u)
                i = jcast('int', (i + 1))
            Code04_LinkCutCentroids.dfs(1, 0)
            if (Code04_LinkCutCentroids.centerCnt() == 1):
                jcall(out, 'println', jadd(jadd(Code04_LinkCutCentroids.centers[0], ' '), Code04_LinkCutCentroids.to[Code04_LinkCutCentroids.head[Code04_LinkCutCentroids.centers[0]]]))
                jcall(out, 'println', jadd(jadd(Code04_LinkCutCentroids.centers[0], ' '), Code04_LinkCutCentroids.to[Code04_LinkCutCentroids.head[Code04_LinkCutCentroids.centers[0]]]))
            else:
                Code04_LinkCutCentroids.find(Code04_LinkCutCentroids.centers[1], Code04_LinkCutCentroids.centers[0])
                jcall(out, 'println', jadd(jadd(Code04_LinkCutCentroids.leafFather, ' '), Code04_LinkCutCentroids.leaf))
                jcall(out, 'println', jadd(jadd(Code04_LinkCutCentroids.centers[0], ' '), Code04_LinkCutCentroids.leaf))
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_LinkCutCentroids.MAXN = jcast('int', 100001)
Code04_LinkCutCentroids.n = jcast('int', 0)
Code04_LinkCutCentroids.head = jarray('int', [Code04_LinkCutCentroids.MAXN])
Code04_LinkCutCentroids.next = jarray('int', [jcast('int', (Code04_LinkCutCentroids.MAXN << (1 & 31)))])
Code04_LinkCutCentroids.to = jarray('int', [jcast('int', (Code04_LinkCutCentroids.MAXN << (1 & 31)))])
Code04_LinkCutCentroids.cnt = jcast('int', 0)
Code04_LinkCutCentroids.size = jarray('int', [Code04_LinkCutCentroids.MAXN])
Code04_LinkCutCentroids.maxsub = jarray('int', [Code04_LinkCutCentroids.MAXN])
Code04_LinkCutCentroids.centers = jarray('int', [2])
Code04_LinkCutCentroids.leaf = jcast('int', 0)
Code04_LinkCutCentroids.leafFather = jcast('int', 0)

if __name__ == '__main__':
    Code04_LinkCutCentroids.main([])
