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

# 牛群聚集(递归版)
# 一共有n个节点，编号1~n，每个点有牛的数量
# 一共有n-1条边把所有点连通起来形成一棵树，每条边有权值
# 想把所有的牛汇聚在一点，希望走过的总距离最小
# 返回总距离最小是多少
# 利用重心的性质：
# 树上的边权如果都>=0，不管边权怎么分布，所有节点都走向重心的总距离和最小
# 测试链接 : https://www.luogu.com.cn/problem/P2986
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code03_GreatCowGathering2.py
class Code03_GreatCowGathering1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'cow': 'cow', 'cowSum': 'cowSum', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'best': 'best', 'center': 'center', 'size': 'size', 'path': 'path'}
    MAXN = 0
    n = 0
    # cow[i] : i号农场牛的数量
    cow = None
    # 牛的总数
    cowSum = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    best = 0
    center = 0
    # size[i] : 从1号节点开始dfs的过程中，以i为头的子树，牛的总量
    size = None
    # path[i] : 从重心节点开始dfs的过程中，从重心到达i节点，距离是多少
    path = None
    @staticmethod
    def build():
        Code03_GreatCowGathering1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code03_GreatCowGathering1.head, 1, jcast('int', jadd(Code03_GreatCowGathering1.n, 1)), 0)
        Code03_GreatCowGathering1.cowSum = jcast('int', 0)
        Code03_GreatCowGathering1.best = jcast('int', jget(Integer, 'MAX_VALUE'))

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code03_GreatCowGathering1.next[Code03_GreatCowGathering1.cnt] = jcast('int', Code03_GreatCowGathering1.head[u])
        Code03_GreatCowGathering1.to[Code03_GreatCowGathering1.cnt] = jcast('int', v)
        Code03_GreatCowGathering1.weight[Code03_GreatCowGathering1.cnt] = jcast('int', w)
        jset(Code03_GreatCowGathering1.head, u, ((_java_obj_1 := Code03_GreatCowGathering1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def findCenter(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_GreatCowGathering1.size[u] = jcast('int', Code03_GreatCowGathering1.cow[u])
        e = jcast('int', Code03_GreatCowGathering1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_GreatCowGathering1.to[e])
            if (v != f):
                Code03_GreatCowGathering1.findCenter(v, u)
            e = jcast('int', Code03_GreatCowGathering1.next[e])
        # 如下代码是遍历完成后再做统计工作
        # 这个写法和之前的逻辑是一样的，为什么要拆开写？
        # 为了后续改迭代版方便
        maxsub = jcast('int', 0)
        e = jcast('int', Code03_GreatCowGathering1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_GreatCowGathering1.to[e])
            if (v != f):
                Code03_GreatCowGathering1.size[u] = jcast('int', jcast('int', jadd(Code03_GreatCowGathering1.size[u], Code03_GreatCowGathering1.size[v])))
                maxsub = jcast('int', jstatic('Math', 'max', maxsub, Code03_GreatCowGathering1.size[v]))
            e = jcast('int', Code03_GreatCowGathering1.next[e])
        maxsub = jcast('int', jstatic('Math', 'max', maxsub, jcast('int', (Code03_GreatCowGathering1.cowSum - Code03_GreatCowGathering1.size[u]))))
        if (maxsub < Code03_GreatCowGathering1.best):
            Code03_GreatCowGathering1.best = jcast('int', maxsub)
            Code03_GreatCowGathering1.center = jcast('int', u)

    @staticmethod
    def setPath(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code03_GreatCowGathering1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_GreatCowGathering1.to[e])
            if (v != f):
                Code03_GreatCowGathering1.path[v] = jcast('int', jcast('int', jadd(Code03_GreatCowGathering1.path[u], Code03_GreatCowGathering1.weight[e])))
                Code03_GreatCowGathering1.setPath(v, u)
            e = jcast('int', Code03_GreatCowGathering1.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_GreatCowGathering1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_GreatCowGathering1.build()
        i = jcast('int', 1)
        while (i <= Code03_GreatCowGathering1.n):
            jcall(in_, 'nextToken')
            Code03_GreatCowGathering1.cow[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code03_GreatCowGathering1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_GreatCowGathering1.addEdge(u, v, w)
            Code03_GreatCowGathering1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code03_GreatCowGathering1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code03_GreatCowGathering1.n):
            Code03_GreatCowGathering1.cowSum = jcast('int', jcast('int', jadd(Code03_GreatCowGathering1.cowSum, Code03_GreatCowGathering1.cow[i])))
            i = jcast('int', (i + 1))
        Code03_GreatCowGathering1.findCenter(1, 0)
        Code03_GreatCowGathering1.path[Code03_GreatCowGathering1.center] = jcast('int', 0)
        Code03_GreatCowGathering1.setPath(Code03_GreatCowGathering1.center, 0)
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code03_GreatCowGathering1.n):
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', Code03_GreatCowGathering1.cow[i]) * Code03_GreatCowGathering1.path[i])))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_GreatCowGathering1.MAXN = jcast('int', 100001)
Code03_GreatCowGathering1.n = jcast('int', 0)
Code03_GreatCowGathering1.cow = jarray('int', [Code03_GreatCowGathering1.MAXN])
Code03_GreatCowGathering1.cowSum = jcast('int', 0)
Code03_GreatCowGathering1.head = jarray('int', [Code03_GreatCowGathering1.MAXN])
Code03_GreatCowGathering1.next = jarray('int', [jcast('int', (Code03_GreatCowGathering1.MAXN << (1 & 31)))])
Code03_GreatCowGathering1.to = jarray('int', [jcast('int', (Code03_GreatCowGathering1.MAXN << (1 & 31)))])
Code03_GreatCowGathering1.weight = jarray('int', [jcast('int', (Code03_GreatCowGathering1.MAXN << (1 & 31)))])
Code03_GreatCowGathering1.cnt = jcast('int', 0)
Code03_GreatCowGathering1.best = jcast('int', 0)
Code03_GreatCowGathering1.center = jcast('int', 0)
Code03_GreatCowGathering1.size = jarray('int', [Code03_GreatCowGathering1.MAXN])
Code03_GreatCowGathering1.path = jarray('int', [Code03_GreatCowGathering1.MAXN])

if __name__ == '__main__':
    Code03_GreatCowGathering1.main([])
